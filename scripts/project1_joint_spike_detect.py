"""Project 1 — Bucket 2b: version x cause JOINT spike detector (multi-grain).

The priority-1 "tell engineering" signal: a cause cluster (mail provider / ISP /
protocol / AV) that is BOTH spiking AND concentrated in a specific Thunderbird
major version — e.g. v151 x isp:spectrum cert errors.

ADOPTION SUPPRESSION (the key idea):
  A raw "v152 x imap" count rises simply because v152 adoption grows, not
  because IMAP is breaking. So we don't threshold the raw count. Instead, for a
  version V and cause X in period P:
      expected = (#questions in P with version V) x (X's overall rate)
      lift     = observed / expected
  Because `expected` scales with V's volume in P, pure adoption cancels out —
  only genuine OVER-representation of the cause within that version survives.

  A (period, version, cause) is flagged when:
      observed >= MIN_COUNT   AND   lift >= LIFT_MIN

MULTI-GRAIN (daily/weekly/monthly, see project1_grains.py): a version-correlated
regression that trickles in below the daily floor still surfaces at a coarser
grain. Cause rates are computed over the full available (versioned) period.
Thresholds were calibrated on the post-backfill baseline (2026-02+, ~2.5k
versioned questions); retune per-grain via --min-count/--lift.

Note: a provider OUTAGE that spans versions (e.g. the March 2026 GMX incident,
split across v140/v148 with half the questions unversioned) is a CAUSE-level, not
version×cause, signal — it is caught by project1_spike_detect.py, not here.

No AI — pure pandas. Every flagged row carries ALL question_ids + URLs.

Usage:
  uv run scripts/project1_joint_spike_detect.py desktop --grain monthly
  uv run scripts/project1_joint_spike_detect.py desktop --grain daily --min-count 4 --lift 3
"""
import sys
import csv
import glob
import argparse
import pandas as pd

sys.path.insert(0, "scripts")
from project1_grains import GRAINS, GRAIN_DEFAULTS, period_dt, period_label

csv.field_size_limit(sys.maxsize)

FEATURES_GLOB = "PROJECT1/*-{product}-features.csv"
OUT = "PROJECT1/{product}-{grain}-version-cause-spikes.csv"
# OS is a secondary FILTER, not a primary cause (decision 2026-06-28): a bare
# v140 x os:linux joint is "Linux users ask varied things", not a root cause.
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
    ap.add_argument("--grain", default="daily", choices=GRAINS)
    ap.add_argument("--min-count", type=int, help="absolute floor: observed in the cluster")
    ap.add_argument("--lift", type=float, help="observed/expected over-representation threshold")
    args = ap.parse_args()
    grain = args.grain
    d = GRAIN_DEFAULTS[grain]
    min_count = args.min_count if args.min_count is not None else d["joint_min_count"]
    lift_min = args.lift if args.lift is not None else d["joint_lift"]

    df, files = load_features(args.product)
    df["period"] = period_dt(df["created_date"], grain).map(lambda t: period_label(t, grain))
    df = df[df["period"] != ""].copy()
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

    # version volume per (period, version_major)
    vol = (df.groupby(["period", "tb_version_major"])["id"].nunique()
             .rename("version_total").reset_index())
    vol_lookup = {(r["period"], r["tb_version_major"]): r["version_total"]
                  for _, r in vol.iterrows()}

    # explode to (period, version, cause_dim, cause_value, id, title, url)
    recs = []
    for _, r in df.iterrows():
        ver = r["tb_version_major"]
        for dim in CAUSE_DIMS:
            for v in (r[dim].split(";") if r[dim] else []):
                if v:
                    recs.append((r["period"], ver, dim, v,
                                 r["id"], r["title"], r["question_url"]))
    long = pd.DataFrame(recs, columns=["period", "version", "dim", "value",
                                       "id", "title", "url"])

    obs = (long.groupby(["period", "version", "dim", "value"])["id"].nunique()
               .rename("observed").reset_index())

    rows = []
    for _, r in obs.iterrows():
        if r["observed"] < min_count:
            continue
        rate = cause_rate.get((r["dim"], r["value"]), 0.0)
        vtot = vol_lookup.get((r["period"], r["version"]), 0)
        expected = vtot * rate
        if expected <= 0:
            continue
        lift = r["observed"] / expected
        if lift < lift_min:
            continue
        sub = long[(long["period"] == r["period"]) & (long["version"] == r["version"])
                   & (long["dim"] == r["dim"]) & (long["value"] == r["value"])
                   ].drop_duplicates("id")
        rows.append({
            "period": r["period"],
            "headline": f"v{r['version']} x {r['value']}: {r['observed']} questions "
                        f"({lift:.0f}x expected)",
            "version_major": r["version"], "cause_dim": r["dim"],
            "cause_value": r["value"], "observed": int(r["observed"]),
            "version_total_period": int(vtot),
            "cause_rate_overall": round(rate, 4),
            "expected": round(expected, 2), "lift": round(lift, 1),
            "question_ids": " ".join(sub["id"]),
            "example_urls": " ".join(sub["url"]),
            "example_titles": " | ".join(t[:60] for t in sub["title"].head(N_EXAMPLE_TITLES)),
        })

    cols = ["period", "headline", "version_major", "cause_dim", "cause_value",
            "observed", "version_total_period", "cause_rate_overall", "expected",
            "lift", "question_ids", "example_urls", "example_titles"]
    sp = pd.DataFrame(rows, columns=cols)
    sp = sp.sort_values(["lift", "period"], ascending=[False, False])
    out = OUT.format(product=args.product, grain=grain)
    sp.to_csv(out, index=False)

    print(f"=== {args.product} {grain} version x cause joint spike detector ===")
    print(f"inputs: {len(files)} feature files, {total_versioned} versioned questions, "
          f"periods {df['period'].min()}..{df['period'].max()}")
    print(f"params: min_count={min_count} lift>={lift_min}x")
    print(f"wrote {out} — {len(sp)} joint spikes\n")
    if sp.empty:
        print("No version x cause spikes at current thresholds.")
        return
    print("FLAGGED (highest lift first):")
    for _, r in sp.iterrows():
        print(f"  {r['period']}  {r['headline']}   "
              f"[obs {r['observed']} / exp {r['expected']} of {r['version_total_period']} v{r['version_major']} qs]")


if __name__ == "__main__":
    main()
