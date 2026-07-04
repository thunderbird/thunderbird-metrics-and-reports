"""Project 1 — full-history feature backfill.

One-shot / re-runnable companion to project1_extract_features.py. Instead of
reading the committed monthly CONCATENATED_FILES/ (only the last couple of
months exist, and the pre-2026-04 ones are frozen old-API files WITHOUT the
native operating_system / thunderbird_version columns), this reads the
aaq-scraper per-day CSVs directly from aaq-data/<year>/ and, for every month
present, concatenates them in memory (dedup on id, keep last — matching the
concat step) and runs the SAME build_features() core to emit
PROJECT1/{month}-{product}-features.csv.

This never writes to CONCATENATED_FILES/, so the frozen monthly-report inputs
stay untouched. Project 1 thus gets a consistent, version-bearing feature table
across all scraper history (version data is only populated ~2026-02 onward; the
detectors/report handle the split — cause/volume use all history, version×cause
is naturally limited to versioned rows).

Usage:
  uv run scripts/project1_backfill_features.py desktop
  uv run scripts/project1_backfill_features.py desktop --start 2026-02 --end 2026-07
"""
import sys
import csv
import re
import glob
import argparse
import pandas as pd

sys.path.insert(0, "scripts")
from project1_extract_features import build_features, OUT

csv.field_size_limit(sys.maxsize)

DATA_DIR = "aaq-data"
DAY_RE = re.compile(r"-(\d{4}-\d{2})-\d{2}\.csv$")


def months_available(product):
    """Set of YYYY-MM that have at least one questions day-file for product."""
    months = set()
    for f in glob.glob(f"{DATA_DIR}/*/questions-thunderbird-{product}-*.csv"):
        m = DAY_RE.search(f)
        if m:
            months.add(m.group(1))
    return sorted(months)


def read_month(product, month):
    """Concat all day-files for one YYYY-MM into (questions_df, answers_df),
    dedup on id keeping the last (freshest) copy — same as the concat step."""
    year = month[:4]
    q_files = sorted(glob.glob(
        f"{DATA_DIR}/{year}/questions-thunderbird-{product}-{month}-*.csv"))
    a_files = sorted(glob.glob(
        f"{DATA_DIR}/{year}/answers-thunderbird-{product}-{month}-*.csv"))

    def cat(files):
        if not files:
            return pd.DataFrame()
        df = pd.concat([pd.read_csv(f, dtype=str, keep_default_na=False)
                        for f in files], ignore_index=True)
        return df.drop_duplicates(subset="id", keep="last")

    return cat(q_files), cat(a_files), len(q_files)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("product", choices=["desktop", "android"])
    ap.add_argument("--start", help="first YYYY-MM (default: earliest available)")
    ap.add_argument("--end", help="last YYYY-MM (default: latest available)")
    args = ap.parse_args()
    product = args.product

    months = months_available(product)
    if not months:
        sys.exit(f"no aaq-data day-files for {product} under {DATA_DIR}/")
    if args.start:
        months = [m for m in months if m >= args.start]
    if args.end:
        months = [m for m in months if m <= args.end]
    if not months:
        sys.exit("no months in the requested range")

    print(f"=== {product} feature backfill: {months[0]}..{months[-1]} "
          f"({len(months)} months) ===")
    grand_q = grand_kept = grand_ver = 0
    for month in months:
        q, a, n_day = read_month(product, month)
        if q.empty:
            print(f"  {month}: no question files, skipped")
            continue
        feats, total_q, n_spam = build_features(q, a)
        out_path = OUT.format(month=month, product=product)
        feats.to_csv(out_path, index=False)
        n = len(feats)
        n_ver = int((feats["tb_version_major"].str.strip() != "").sum())
        grand_q += total_q
        grand_kept += n
        grand_ver += n_ver
        print(f"  {month}: {n_day:2d} day-files -> {total_q:5d} q "
              f"({n_spam} spam) -> {n:5d} kept, {n_ver:5d} versioned "
              f"({100 * n_ver / max(n, 1):3.0f}%)  wrote {out_path}")

    print(f"\ntotal: {grand_kept} questions kept across {len(months)} months, "
          f"{grand_ver} versioned ({100 * grand_ver / max(grand_kept, 1):.0f}%)")


if __name__ == "__main__":
    main()
