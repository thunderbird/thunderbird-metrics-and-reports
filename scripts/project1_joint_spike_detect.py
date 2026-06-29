"""Project 1 — Bucket 2b: version x cause JOINT spike detector (the headline).

This is the priority-1 "tell engineering" signal: a cause cluster (mail
provider / ISP / protocol / OS / AV) that is BOTH spiking AND concentrated in a
specific Thunderbird major version — e.g. v151 x isp:spectrum cert errors.

ADOPTION SUPPRESSION (the key idea):
  A raw "v152 x imap" count rises simply because v152 adoption grows, not
  because IMAP is breaking. So we don't threshold the raw count. Instead, for a
  version V and cause X on day D:
      expected = (#questions on D with version V) x (X's overall rate)
      lift     = observed / expected
  Because `expected` scales with V's daily volume, pure adoption cancels out —
  only genuine OVER-representation of the cause within that version survives.

  A (date, version, cause) is flagged when:
      observed >= MIN_COUNT   AND   lift >= LIFT_MIN
  Cause rates are computed over the full available period for now; recalibrate
  after backfill widens history (per agreed plan).

Daily grain today; monthly/quarterly reuse the same machinery later.
No AI — pure pandas. Every flagged row carries ALL question_ids + URLs.

Usage:
  uv run scripts/project1_joint_spike_detect.py desktop
  uv run scripts/project1_joint_spike_detect.py desktop --min-count 4 --lift 3
"""
import sys
import csv
import glob
import argparse
import pandas as pd

csv.field_size_limit(sys.maxsize)

FEATURES_GLOB = "PROJECT1/*-{product}-features.csv"
OUT = "PROJECT1/{product}-version-cause-spikes.csv"
# OS is a secondary FILTER, not a primary cause (decision 2026-06-28): a bare
# v140 x os:linux joint is "Linux users ask varied things", not a root cause.
# Causes are the dimensions an engineer can act on.
CAUSE_DIMS = ["mail_provider", "isp", "protocol", "av"]
N_EXAMPLE_TITLES = 5


def load_features(product):
    files = sorted(glob.glob(FEATURES_GLOB.format(product=product)))
    if not files:
        sys.exit(f"no feature files match {FEATURES_GLOB.format(product=product)}")
    df = pd.concat([pd.read_csv(f, dtype=str, keep_default_na=False) for f in files],
                   ignore_index=True).drop_duplicates(subset="id")
    df = df[(df["created_date"].str.strip() != "")
            & (df["tb_version_major"].str.strip() != "")].copy()
    return df, files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("product", choices=["desktop", "android"])
    ap.add_argument("--min-count", type=int, default=4,
                    help="absolute floor: observed questions in the cluster")
    ap.add_argument("--lift", type=float, default=3.0,
                    help="observed/expected over-representation threshold")
    args = ap.parse_args()

    df, files = load_features(args.product)
    total_versioned = len(df)

    # cause overall rate (denominator = versioned questions)
    cause_rate = {}  # (dim, value) -> rate
    for dim in CAUSE_DIMS:
        n = {}
        for cell in df[dim]:
            for v in (cell.split(";") if cell else []):
                if v:
                    n[v] = n.get(v, 0) + 1
        for v, c in n.items():
            cause_rate[(dim, v)] = c / total_versioned

    # version volume per (date, version_major)
    vol = (df.groupby(["created_date", "tb_version_major"])["id"].nunique()
             .rename("version_total").reset_index())
    vol_lookup = {(r["created_date"], r["tb_version_major"]): r["version_total"]
                  for _, r in vol.iterrows()}

    # explode to (date, version, cause_dim, cause_value, id, title, url)
    recs = []
    for _, r in df.iterrows():
        ver = r["tb_version_major"]
        for dim in CAUSE_DIMS:
            for v in (r[dim].split(";") if r[dim] else []):
                if v:
                    recs.append((r["created_date"], ver, dim, v,
                                 r["id"], r["title"], r["question_url"]))
    long = pd.DataFrame(recs, columns=["date", "version", "dim", "value",
                                       "id", "title", "url"])

    obs = (long.groupby(["date", "version", "dim", "value"])["id"].nunique()
               .rename("observed").reset_index())

    rows = []
    for _, r in obs.iterrows():
        if r["observed"] < args.min_count:
            continue
        rate = cause_rate.get((r["dim"], r["value"]), 0.0)
        vtot = vol_lookup.get((r["date"], r["version"]), 0)
        expected = vtot * rate
        if expected <= 0:
            continue
        lift = r["observed"] / expected
        if lift < args.lift:
            continue
        sub = long[(long["date"] == r["date"]) & (long["version"] == r["version"])
                   & (long["dim"] == r["dim"]) & (long["value"] == r["value"])
                   ].drop_duplicates("id")
        rows.append({
            "date": r["date"],
            "headline": f"v{r['version']} x {r['value']}: {r['observed']} questions "
                        f"({lift:.0f}x expected)",
            "version_major": r["version"], "cause_dim": r["dim"],
            "cause_value": r["value"], "observed": int(r["observed"]),
            "version_total_day": int(vtot),
            "cause_rate_overall": round(rate, 4),
            "expected": round(expected, 2), "lift": round(lift, 1),
            "question_ids": " ".join(sub["id"]),
            "example_urls": " ".join(sub["url"]),
            "example_titles": " | ".join(t[:60] for t in sub["title"].head(N_EXAMPLE_TITLES)),
        })

    cols = ["date", "headline", "version_major", "cause_dim", "cause_value",
            "observed", "version_total_day", "cause_rate_overall", "expected",
            "lift", "question_ids", "example_urls", "example_titles"]
    sp = pd.DataFrame(rows, columns=cols)
    sp = sp.sort_values(["lift", "date"], ascending=[False, False])
    out = OUT.format(product=args.product)
    sp.to_csv(out, index=False)

    print(f"=== {args.product} version x cause joint spike detector ===")
    print(f"inputs: {len(files)} feature files, {total_versioned} versioned questions, "
          f"dates {df['created_date'].min()}..{df['created_date'].max()}")
    print(f"params: min_count={args.min_count} lift>={args.lift}x")
    print(f"wrote {out} — {len(sp)} joint spikes\n")
    if sp.empty:
        print("No version x cause spikes at current thresholds.")
        return
    print("FLAGGED (highest lift first):")
    for _, r in sp.iterrows():
        print(f"  {r['date']}  {r['headline']}   "
              f"[obs {r['observed']} / exp {r['expected']} of {r['version_total_day']} v{r['version_major']} qs]")
        print(f"      ids: {r['question_ids']}")
        print(f"      e.g. {r['example_titles'][:95]}")


if __name__ == "__main__":
    main()
