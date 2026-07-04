"""Project 1 — Bucket 2: single-dimension spike detector (multi-grain).

Reads the per-question feature tables produced by project1_extract_features.py /
project1_backfill_features.py (PROJECT1/*-{product}-features.csv), builds a count
series per (dimension, value) at the chosen GRAIN (daily / weekly / monthly),
compares each period to a trailing baseline, and flags spikes — each backed by
clickable example questions (priority-1 requirement).

Dimensions: total volume, os, tb_version_major, mail_provider, isp, protocol, av.
Multi-tag questions count toward EACH of their values (confirmed decision).

A (dimension, value, period) is flagged a SPIKE when, that period:
  count >= MIN_COUNT  AND  ( baseline == 0  -> count >= MIN_COUNT   ["new/dormant"]
                             baseline  > 0  -> count >= MULT * baseline )
baseline = median of the trailing WINDOW periods (excluding the period itself),
requiring >= MIN_PERIODS periods of prior history.

WHY MULTI-GRAIN: a slow-burn incident never clears a daily floor. The March 2026
GMX provider outage (~1–2 questions/day for a month) is invisible daily but an
obvious 4.3× spike at MONTHLY grain. See project1_grains.py. Per-grain defaults
live there; override on the CLI. Cause-dimension spikes from this detector are
surfaced in the report (provider/protocol/ISP/AV incidents); version/os spikes
stay a manual-checking artifact.

No AI — pure pandas.

Usage:
  uv run scripts/project1_spike_detect.py desktop --grain monthly
  uv run scripts/project1_spike_detect.py desktop --grain daily --min-count 8 --mult 3
"""
import sys
import csv
import glob
import argparse
import pandas as pd

sys.path.insert(0, "scripts")
from project1_grains import GRAINS, GRAIN_FREQ, GRAIN_DEFAULTS, period_dt, period_label

csv.field_size_limit(sys.maxsize)

FEATURES_GLOB = "PROJECT1/*-{product}-features.csv"
OUT = "PROJECT1/{product}-{grain}-single-spikes.csv"
TAG_DIMS = ["os", "tb_version_major", "mail_provider", "protocol", "av"]
N_EXAMPLE_TITLES = 5  # title previews are capped for readability; IDs/URLs are not


def load_features(product):
    files = sorted(glob.glob(FEATURES_GLOB.format(product=product)))
    if not files:
        sys.exit(f"no feature files match {FEATURES_GLOB.format(product=product)}")
    df = pd.concat([pd.read_csv(f, dtype=str, keep_default_na=False) for f in files],
                   ignore_index=True)
    df = df.drop_duplicates(subset="id")
    df = df[df["created_date"].str.strip() != ""].copy()
    return df, files


def explode_long(df, grain):
    """One row per (period, dim, value, question). `period` is the grain-period
    label; `pdt` its start Timestamp (for ordering/rolling)."""
    recs = []
    for _, r in df.iterrows():
        date = r["created_date"]
        recs.append((date, "total", "all", r["id"], r["title"], r["question_url"]))
        for dim in TAG_DIMS:
            cell = r.get(dim, "")
            for v in (cell.split(";") if cell else []):
                if v:
                    recs.append((date, dim, v, r["id"], r["title"], r["question_url"]))
    long = pd.DataFrame(recs, columns=["date", "dim", "value", "id", "title", "url"])
    long["pdt"] = period_dt(long["date"], grain)
    long["period"] = long["pdt"].map(lambda t: period_label(t, grain))
    return long[long["pdt"].notna()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("product", choices=["desktop", "android"])
    ap.add_argument("--grain", default="daily", choices=GRAINS)
    ap.add_argument("--window", type=int, help="trailing baseline periods")
    ap.add_argument("--min-periods", type=int, help="min prior periods of history")
    ap.add_argument("--min-count", type=int, help="absolute floor for a spike period")
    ap.add_argument("--mult", type=float, help="count >= mult x baseline")
    args = ap.parse_args()
    grain = args.grain
    d = GRAIN_DEFAULTS[grain]
    window = args.window if args.window is not None else d["window"]
    min_periods = args.min_periods if args.min_periods is not None else d["min_periods"]
    min_count = args.min_count if args.min_count is not None else d["single_min_count"]
    mult = args.mult if args.mult is not None else d["single_mult"]

    df, files = load_features(args.product)
    long = explode_long(df, grain)
    all_pdt = pd.date_range(long["pdt"].min(), long["pdt"].max(), freq=GRAIN_FREQ[grain])

    # count per (dim, value, period), distinct questions
    counts = (long.groupby(["dim", "value", "pdt"])["id"].nunique()
                  .rename("count").reset_index())

    spikes = []
    for (dim, value), g in counts.groupby(["dim", "value"]):
        s = (g.set_index("pdt")["count"].reindex(all_pdt, fill_value=0).sort_index())
        baseline = s.rolling(window, min_periods=min_periods).median().shift(1)
        for pdt, cnt in s.items():
            base = baseline.get(pdt)
            if pd.isna(base) or cnt < min_count:
                continue
            if base == 0:
                mag, kind = float("inf"), "new/dormant"
            elif cnt >= mult * base:
                mag, kind = cnt / base, "above-baseline"
            else:
                continue
            spikes.append({
                "period": period_label(pdt, grain), "dim": dim, "value": value,
                "count": int(cnt), "baseline_median": round(float(base), 2),
                "magnitude": round(mag, 2) if mag != float("inf") else "new",
                "kind": kind,
            })

    cols = ["period", "dim", "value", "count", "baseline_median", "magnitude",
            "kind", "question_ids", "example_urls", "example_titles"]
    out = OUT.format(product=args.product, grain=grain)
    if not spikes:
        print(f"No {grain} spikes flagged at current thresholds.")
        pd.DataFrame(columns=cols).to_csv(out, index=False)
        return

    sp = pd.DataFrame(spikes)

    # attach example questions for each flagged (period,dim,value)
    def examples(row):
        m = long[(long["period"] == row["period"]) & (long["dim"] == row["dim"])
                 & (long["value"] == row["value"])].drop_duplicates("id")
        return pd.Series({
            "question_ids": " ".join(m["id"]),                       # ALL ids, for manual checking
            "example_urls": " ".join(m["url"]),                      # ALL clickable links
            "example_titles": " | ".join(t[:60] for t in m["title"].head(N_EXAMPLE_TITLES)),
        })

    sp = pd.concat([sp, sp.apply(examples, axis=1)], axis=1)
    sp["_magsort"] = pd.to_numeric(sp["magnitude"].replace("new", 1e9), errors="coerce")
    sp = sp.sort_values(["period", "_magsort"], ascending=[False, False]).drop(columns="_magsort")
    sp[cols].to_csv(out, index=False)

    # --- summary ------------------------------------------------------------
    print(f"=== {args.product} {grain} single-dim spike detector ===")
    print(f"inputs: {len(files)} feature files, {len(df)} questions, "
          f"periods {period_label(all_pdt.min(), grain)}..{period_label(all_pdt.max(), grain)}")
    print(f"params: window={window} min_periods={min_periods} "
          f"min_count={min_count} mult={mult}x")
    print(f"wrote {out} — {len(sp)} spikes\n")
    print("spikes per dimension:", sp["dim"].value_counts().to_dict())
    print("\nTOP spikes (most recent first):")
    for _, r in sp.head(15).iterrows():
        print(f"  {r['period']}  {r['dim']:16} {r['value']:18} "
              f"count={r['count']:<3} base={r['baseline_median']:<5} "
              f"x{r['magnitude']:<5} [{r['kind']}]")


if __name__ == "__main__":
    main()
