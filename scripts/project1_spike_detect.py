"""Project 1 — Bucket 2: daily spike detector (single-dimension).

Reads the per-question feature tables produced by project1_extract_features.py
(PROJECT1/*-{product}-features.csv), builds a daily count series for every
(dimension, value), compares each day to a trailing baseline, and flags spikes —
each backed by clickable example questions (priority-1 requirement).

Dimensions: total volume, os, tb_version_major, mail_provider, isp, protocol, av.
Multi-tag questions count toward EACH of their values (confirmed decision).

A (dimension, value, date) is flagged a SPIKE when, that day:
  count >= MIN_COUNT  AND  ( baseline == 0          -> count >= MIN_COUNT  ["new/dormant surge"]
                             baseline  > 0          -> count >= MULT * baseline )
baseline = median of the trailing WINDOW days (excluding the day itself),
requiring >= MIN_PERIODS days of prior history (so early dates don't all flag).

No AI — pure pandas. This detector is daily by design (a standalone
manual-checking dump, not consumed by the report); coarser-grain rollups live in
project1_report.py. Default min_count=8 was calibrated on the post-backfill
baseline (drops count-vs-tiny-baseline noise); retune via --min-count/--mult.

Usage:
  uv run scripts/project1_spike_detect.py desktop
  uv run scripts/project1_spike_detect.py desktop --mult 3 --min-count 5 --window 28
"""
import sys
import csv
import glob
import argparse
import pandas as pd

csv.field_size_limit(sys.maxsize)

FEATURES_GLOB = "PROJECT1/*-{product}-features.csv"
OUT = "PROJECT1/{product}-daily-spikes.csv"
TAG_DIMS = ["os", "tb_version_major", "mail_provider", "isp", "protocol", "av"]
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


def explode_long(df):
    """One row per (date, dim, value, question)."""
    recs = []
    for _, r in df.iterrows():
        date = r["created_date"]
        recs.append((date, "total", "all", r["id"], r["title"], r["question_url"]))
        for dim in TAG_DIMS:
            cell = r.get(dim, "")
            for v in (cell.split(";") if cell else []):
                if v:
                    recs.append((date, dim, v, r["id"], r["title"], r["question_url"]))
    return pd.DataFrame(recs, columns=["date", "dim", "value", "id", "title", "url"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("product", choices=["desktop", "android"])
    ap.add_argument("--window", type=int, default=28, help="trailing baseline days")
    ap.add_argument("--min-periods", type=int, default=14, help="min prior days of history")
    ap.add_argument("--min-count", type=int, default=8, help="absolute floor for a spike day")
    ap.add_argument("--mult", type=float, default=3.0, help="count >= mult x baseline")
    args = ap.parse_args()

    df, files = load_features(args.product)
    long = explode_long(df)
    all_dates = pd.date_range(long["date"].min(), long["date"].max(), freq="D")

    # daily counts per (dim, value), distinct questions
    daily = (long.groupby(["dim", "value", "date"])["id"].nunique()
                 .rename("count").reset_index())

    spikes = []
    for (dim, value), g in daily.groupby(["dim", "value"]):
        s = (g.set_index(pd.to_datetime(g["date"]))["count"]
               .reindex(all_dates, fill_value=0).sort_index())
        baseline = s.rolling(args.window, min_periods=args.min_periods).median().shift(1)
        for day, cnt in s.items():
            base = baseline.get(day)
            if pd.isna(base) or cnt < args.min_count:
                continue
            if base == 0:
                mag, kind = float("inf"), "new/dormant"
            elif cnt >= args.mult * base:
                mag, kind = cnt / base, "above-baseline"
            else:
                continue
            spikes.append({
                "date": day.date().isoformat(), "dim": dim, "value": value,
                "count": int(cnt), "baseline_median": round(float(base), 2),
                "magnitude": round(mag, 2) if mag != float("inf") else "new",
                "kind": kind,
            })

    sp = pd.DataFrame(spikes)
    if sp.empty:
        print("No spikes flagged at current thresholds.")
        sp = pd.DataFrame(columns=["date", "dim", "value", "count",
                                   "baseline_median", "magnitude", "kind",
                                   "question_ids", "example_urls", "example_titles"])
        sp.to_csv(OUT.format(product=args.product), index=False)
        return

    # attach example questions for each flagged (date,dim,value)
    def examples(row):
        m = long[(long["date"] == row["date"]) & (long["dim"] == row["dim"])
                 & (long["value"] == row["value"])].drop_duplicates("id")
        return pd.Series({
            "question_ids": " ".join(m["id"]),                       # ALL ids, for manual checking
            "example_urls": " ".join(m["url"]),                      # ALL clickable links
            "example_titles": " | ".join(t[:60] for t in m["title"].head(N_EXAMPLE_TITLES)),
        })

    sp = pd.concat([sp, sp.apply(examples, axis=1)], axis=1)
    sp["_magsort"] = pd.to_numeric(sp["magnitude"].replace("new", 1e9), errors="coerce")
    sp = sp.sort_values(["date", "_magsort"], ascending=[False, False]).drop(columns="_magsort")
    out = OUT.format(product=args.product)
    sp.to_csv(out, index=False)

    # --- summary ------------------------------------------------------------
    print(f"=== {args.product} daily spike detector ===")
    print(f"inputs: {len(files)} feature files, {len(df)} questions, "
          f"dates {all_dates.min().date()}..{all_dates.max().date()}")
    print(f"params: window={args.window}d min_periods={args.min_periods} "
          f"min_count={args.min_count} mult={args.mult}x")
    print(f"wrote {out} — {len(sp)} spikes\n")
    print("spikes per dimension:", sp["dim"].value_counts().to_dict())
    print("\nTOP spikes (most recent first):")
    for _, r in sp.head(15).iterrows():
        print(f"  {r['date']}  {r['dim']:16} {r['value']:18} "
              f"count={r['count']:<3} base={r['baseline_median']:<5} "
              f"x{r['magnitude']:<5} [{r['kind']}]")
        print(f"      e.g. {r['example_titles'][:90]}")


if __name__ == "__main__":
    main()
