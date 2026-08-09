"""Project 1 — explorer data: one compact JSON behind PROJECT1/REPORTS/{product}/explorer.html.

WHY this exists: the spike-report tables link the questions of the ONE period that
fired as a spike. A reader who sees an interesting bump elsewhere on a sparkline
has no way to reach those questions — the sparkline is dead text. The explorer page
fixes that by letting you pick a grain + version + cause, then CLICK any point to
list that bucket's questions. To keep the page independent of a backend, all the
raw material ships as a sibling JSON that the browser aggregates.

So this script does NOT pre-aggregate. It emits one row per question (columnar,
index-encoded) and lets the page bucket them — that is what makes every
grain × version × cause × period combination reachable from a single cached fetch.
Pre-aggregating would have to enumerate 24 versions × ~110 causes × 5 grains and
still carry the ids and titles, which is strictly bigger and less flexible.

Encoding (all of it exists to keep the file small — ~48k desktop questions):
  versions[]   value list; a row's `v` is an index (0 = no usable version)
  tags[]       ONE flat vocabulary across every cause/filter dimension
               ('m:gmail', 'proto:imap', 'av:eset', 'os:windows', 'macos:sequoia'),
               with tag_dim[i] naming the dimension of tags[i]. A flat list keeps a
               row's tags to a single small array instead of five mostly-empty ones.
  rows[]       [id, day, verIdx, flags, fah, [tagIdx...], title]
               day   = days since `epoch` (dates only — see the grain note below)
               flags = bit0 answered by a non-creator, bit1 solved
               fah   = first-answer hours, rounded; -1 when unanswered/unknown
               title = truncated, for the link text

Bucket labels the page derives from `day` MUST match the detectors' period keys
(daily/weekly 'YYYY-MM-DD' with a week keyed by its Monday, monthly 'YYYY-MM'), or
the "explore ↗" deep links from the spike reports would not resolve to a bucket.
Day resolution is deliberate: it makes the hourly grain impossible, which is fine —
an hourly view over 3.5 years is unreadable and the hourly spike report already
covers the trailing week.

No AI, no API calls. Reads only the committed feature tables, so it is cheap and
can run on its own schedule:
  uv run scripts/project1_explorer_data.py desktop
"""
import argparse
import csv
import glob
import json
import os
import sys
from datetime import datetime, timedelta, timezone

import pandas as pd

csv.field_size_limit(sys.maxsize)

FEATURES_GLOB = "PROJECT1/*-{product}-features.csv"
OUT = "PROJECT1/REPORTS/{product}/explorer.json"
JOINT_CSV = "PROJECT1/{product}-{grain}-version-cause-spikes.csv"
SINGLE_CSV = "PROJECT1/{product}-{grain}-single-spikes.csv"
VERIFY_GRAINS = ["daily", "weekly", "monthly"]
QUESTION_URL_PREFIX = "https://support.mozilla.org/questions/"
TITLE_MAX = 90  # link text only; the full title is one click away on SUMO

# Cause dimensions (what the joint detector ranks) then the filter dimensions.
# Same split as project1_report.py: OS and macos_release are FILTERS, not causes.
CAUSE_DIMS = ["mail_provider", "protocol", "av"]
FILTER_DIMS = ["os", "macos_release"]
DIM_LABELS = {
    "mail_provider": "Mail provider",
    "protocol": "Protocol",
    "av": "Antivirus",
    "os": "OS",
    "macos_release": "macOS release",
}


def load_features(product):
    files = sorted(glob.glob(FEATURES_GLOB.format(product=product)))
    if not files:
        sys.exit(f"no feature files for {product}")
    df = pd.concat([pd.read_csv(f, dtype=str, keep_default_na=False) for f in files],
                   ignore_index=True).drop_duplicates(subset="id")
    # created_date is the already-normalized 'YYYY-MM-DD' the detectors group on --
    # use it rather than the raw `created`, whose format is mixed across months.
    df["day_dt"] = pd.to_datetime(df["created_date"], errors="coerce")
    df = df[df["day_dt"].notna()].copy()
    for c in CAUSE_DIMS + FILTER_DIMS + ["tb_version_major", "title",
                                         "is_answered", "is_solved",
                                         "first_answer_hours"]:
        if c not in df.columns:
            df[c] = ""
        df[c] = df[c].fillna("")
    return df.sort_values("day_dt"), files


def clean_title(s):
    """Collapse whitespace and drop control chars. The page renders titles with
    textContent (never innerHTML), so this is about tidiness, not escaping."""
    s = " ".join(str(s or "").split())
    return "".join(ch for ch in s if ch >= " ")[:TITLE_MAX]


def build(df):
    versions = [""] + sorted({v for v in df["tb_version_major"] if v},
                             key=lambda v: -int(v) if v.isdigit() else 0)
    vidx = {v: i for i, v in enumerate(versions)}

    tags, tag_dim = [], []
    tidx = {}
    for dim in CAUSE_DIMS + FILTER_DIMS:
        vals = set()
        for cell in df[dim]:
            vals.update(t for t in cell.split(";") if t)
        for t in sorted(vals):
            tidx[t] = len(tags)
            tags.append(t)
            tag_dim.append(dim)

    epoch = df["day_dt"].min()
    rows = []
    for r in df.itertuples(index=False):
        flags = (1 if str(r.is_answered).lower() == "true" else 0) \
            | (2 if str(r.is_solved).lower() == "true" else 0)
        try:
            fah = round(float(r.first_answer_hours))
        except (TypeError, ValueError):
            fah = -1
        rtags = []
        for dim in CAUSE_DIMS + FILTER_DIMS:
            cell = getattr(r, dim)
            rtags.extend(tidx[t] for t in cell.split(";") if t)
        rows.append([int(r.id) if str(r.id).isdigit() else r.id,
                     (r.day_dt - epoch).days, vidx.get(r.tb_version_major, 0),
                     flags, fah, sorted(rtags), clean_title(r.title)])
    return versions, tags, tag_dim, epoch, rows


def bucket_label(day, grain, epoch):
    """Mirror of the page's bucketLabel() — the day-offset encoding turned back into
    a detector period key. Deliberately written against `day` rather than reusing
    project1_grains.period_label (which takes date strings): the whole point of
    verify() is to prove the ENCODED form reproduces the detectors' keys."""
    d = epoch + timedelta(days=int(day))
    if grain == "daily":
        return d.strftime("%Y-%m-%d")
    if grain == "weekly":
        return (d - timedelta(days=d.weekday())).strftime("%Y-%m-%d")
    return d.strftime("%Y-%m")


def verify(payload, product):
    """Cross-check the emitted JSON against the committed spike CSVs.

    The failure this exists to catch is SILENT: if the bucket labels drift from the
    detectors' period keys, the explorer still loads, the chart still draws, and
    every "explore" deep link in every spike report quietly selects nothing.

    Two severities, and the distinction matters:
      * HARD (exit 1) — a spike's bucket resolves to ZERO questions. That is the
        label contract breaking; no legitimate data state produces it.
      * DRIFT (warn)  — the count differs but is non-zero. Legitimate: the feature
        tables get re-extracted and re-derive versions, so a committed spike CSV's
        `observed` can lag the features it was computed from.
    """
    epoch = datetime.strptime(payload["epoch"], "%Y-%m-%d")
    tag_idx = {t: i for i, t in enumerate(payload["tags"])}
    ver_of = payload["versions"]
    rows = payload["rows"]

    checked, hard, drift = 0, [], []
    for grain in VERIFY_GRAINS:
        # index the corpus once per grain, not once per spike row
        by_bucket = {}
        for r in rows:
            by_bucket.setdefault(bucket_label(r[1], grain, epoch), []).append(r)

        for path, is_joint in ((JOINT_CSV.format(product=product, grain=grain), True),
                              (SINGLE_CSV.format(product=product, grain=grain), False)):
            if not os.path.exists(path):
                continue
            spikes = pd.read_csv(path, dtype=str, keep_default_na=False)
            for _, s in spikes.iterrows():
                cause = s["cause_value"] if is_joint else s["value"]
                if cause not in tag_idx:      # version/os single-dim rows: not causes
                    continue
                want = int(s["observed"] if is_joint else s["count"])
                ti = tag_idx[cause]
                ver = s["version_major"] if is_joint else None
                got = 0
                for r in by_bucket.get(s["period"], []):
                    if ti not in r[5]:
                        continue
                    if ver is not None and ver_of[r[2]] != ver:
                        continue
                    got += 1
                checked += 1
                where = (f"{grain} {s['period']} "
                         f"{'v' + ver + ' × ' if ver else ''}{cause}")
                if got == 0:
                    hard.append(f"{where}: detector says {want}, explorer bucket is EMPTY")
                elif got != want:
                    drift.append(f"{where}: detector {want} vs explorer {got}")

    print(f"verify: {checked} spike rows cross-checked "
          f"({'/'.join(VERIFY_GRAINS)} grains)")
    for d in drift[:8]:
        print(f"  drift (ok — detector CSV older than the feature tables): {d}")
    if len(drift) > 8:
        print(f"  … and {len(drift) - 8} more drifting rows")
    if hard:
        print(f"  {len(hard)} BUCKET(S) DID NOT RESOLVE — deep links would select "
              f"nothing:", file=sys.stderr)
        for h in hard[:10]:
            print(f"    {h}", file=sys.stderr)
        sys.exit(1)
    print(f"verify: all {checked} spike buckets resolve "
          f"({len(drift)} with count drift)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("product", choices=["desktop", "android"])
    ap.add_argument("--out", default=None, help="override the output path")
    ap.add_argument("--verify", action="store_true",
                    help="cross-check every committed spike's bucket against the "
                         "emitted JSON (gates the workflow)")
    args = ap.parse_args()

    df, files = load_features(args.product)
    versions, tags, tag_dim, epoch, rows = build(df)

    payload = {
        "product": args.product,
        "generated": f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}",
        "epoch": epoch.strftime("%Y-%m-%d"),
        "question_url_prefix": QUESTION_URL_PREFIX,
        "cause_dims": CAUSE_DIMS,
        "filter_dims": FILTER_DIMS,
        "dim_labels": DIM_LABELS,
        "versions": versions,
        "tags": tags,
        "tag_dim": tag_dim,
        # documented here too: the page reads rows positionally
        "row_fields": ["id", "day", "version_idx", "flags", "first_answer_h",
                       "tag_idxs", "title"],
        "rows": rows,
    }

    path = args.out or OUT.format(product=args.product)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(payload, f, separators=(",", ":"), ensure_ascii=False)

    mb = os.path.getsize(path) / 1e6
    print(f"=== {args.product} explorer data ===")
    print(f"inputs: {len(files)} feature files, {len(rows)} questions, "
          f"{df['day_dt'].min():%Y-%m-%d}..{df['day_dt'].max():%Y-%m-%d}")
    print(f"vocab: {len(versions) - 1} versions, {len(tags)} tags "
          f"({', '.join(f'{d}={tag_dim.count(d)}' for d in CAUSE_DIMS + FILTER_DIMS)})")
    print(f"wrote {path} ({mb:.2f} MB)")

    if args.verify:
        verify(payload, args.product)


if __name__ == "__main__":
    main()
