"""Project 1 — Bucket 3: reporting (CSV rollups + blog post with sparklines).

Presentation layer over the feature tables and the spike detectors. Produces:
  1. PROJECT1/{product}-{grain}-rollup.csv  — long-format counts per
     (period, dim, value): the time series behind every sparkline and the
     basis for future grains.
  2. PROJECT1/REPORTS/{product}/{grain}-spike-report.md — a Jekyll-ready blog
     post: the version×cause "tell engineering" table (ranked by lift, with
     clickable question IDs and a per-signal sparkline), plus volume / version /
     cause trends and a responsiveness summary.

Sparklines are Unicode blocks (no image assets). All five grains
(hourly/daily/monthly/quarterly/yearly) are live post-backfill — they share this
machinery; only GRAINS + the period key differ. Volume/cause/OS trends span the
full history; version×cause is naturally limited to versioned rows (2026-02+).

No AI — pure pandas + stdlib. Run AFTER extract/backfill + joint detector:
  uv run scripts/project1_backfill_features.py desktop        (all months)
  uv run scripts/project1_joint_spike_detect.py desktop
  uv run scripts/project1_report.py desktop --grain monthly   (per grain)
"""
import sys
import csv
import glob
import os
import argparse
import pandas as pd

csv.field_size_limit(sys.maxsize)

FEATURES_GLOB = "PROJECT1/*-{product}-features.csv"
JOINT_CSV = "PROJECT1/{product}-version-cause-spikes.csv"
ROLLUP = "PROJECT1/{product}-{grain}-rollup.csv"
REPORT_DIR = "PROJECT1/REPORTS/{product}"
QUESTION_URL = "https://support.mozilla.org/questions/{id}"
BLOCKS = "▁▂▃▄▅▆▇█"

# grain -> (pandas floor freq, label formatter). Only 'daily' is exercised today.
GRAINS = {
    "hourly":    ("h",  lambda t: t.strftime("%Y-%m-%d %H:00")),
    "daily":     ("D",  lambda t: t.strftime("%Y-%m-%d")),
    "monthly":   ("MS", lambda t: t.strftime("%Y-%m")),
    "quarterly": ("QS", lambda t: f"{t.year}-Q{(t.month - 1) // 3 + 1}"),
    "yearly":    ("YS", lambda t: t.strftime("%Y")),
}
UNIT = {"hourly": "hour", "daily": "day", "monthly": "month",
        "quarterly": "quarter", "yearly": "year"}
# Default window = how many trailing periods (buckets) each grain shows, so
# sparklines stay readable as history grows. None = all history. Override with
# --window N (N periods); --window 0 = all.
WINDOW_DEFAULTS = {"hourly": 168, "daily": 90, "monthly": 24,
                   "quarterly": 12, "yearly": None}
CAUSE_DIMS = ["mail_provider", "isp", "protocol", "av"]  # OS is a filter, not a cause
TREND_DIMS = ["tb_version_major"] + CAUSE_DIMS + ["os"]


def spark(vals):
    if not vals:
        return ""
    mx = max(vals)
    if mx == 0:
        return BLOCKS[0] * len(vals)
    return "".join(BLOCKS[min(len(BLOCKS) - 1, round(v / mx * (len(BLOCKS) - 1)))]
                   for v in vals)


def md_safe(s):
    """Neutralize chars that break markdown tables / link tooltips (per repo
    convention): pipe -> broken bar, double-quote -> fullwidth quote."""
    return (s or "").replace("|", "¦").replace('"', "＂")[:80]


def load_features(product):
    files = sorted(glob.glob(FEATURES_GLOB.format(product=product)))
    if not files:
        sys.exit(f"no feature files for {product}")
    df = pd.concat([pd.read_csv(f, dtype=str, keep_default_na=False) for f in files],
                   ignore_index=True).drop_duplicates(subset="id")
    # `created` has mixed formats across months (old API '... -0700' vs scraper
    # ISO '...Z'); format="mixed" parses each row independently instead of
    # inferring one format and NaT-ing the rest.
    df["created_dt"] = pd.to_datetime(df["created"], utc=True, format="mixed",
                                      errors="coerce")
    df = df[df["created_dt"].notna()].copy()
    return df, files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("product", choices=["desktop", "android"])
    ap.add_argument("--grain", default="daily", choices=list(GRAINS))
    ap.add_argument("--window", type=int, default=None,
                    help="trailing periods to show (default per-grain; 0 = all history)")
    args = ap.parse_args()
    product, grain = args.product, args.grain
    freq, label = GRAINS[grain]

    df, files = load_features(product)
    naive = df["created_dt"].dt.tz_convert(None)  # UTC, tz-naive (silences to_period warning)
    df["period_dt"] = naive.dt.floor(freq) if freq == "h" \
        else naive.dt.to_period(freq[0]).dt.start_time
    full_periods = pd.date_range(df["period_dt"].min(), df["period_dt"].max(),
                                 freq={"h": "h", "D": "D", "MS": "MS",
                                       "QS": "QS", "YS": "YS"}[freq])
    # window: keep the trailing N periods, then filter df to match so stats,
    # trends, rollup and the spike list are all consistent with what's shown.
    win = args.window if args.window is not None else WINDOW_DEFAULTS[grain]
    periods = full_periods[-win:] if win and win > 0 else full_periods
    window_start = periods[0]
    df = df[df["period_dt"] >= window_start].copy()
    plabels = [label(p) for p in periods]

    # --- long rollup + per-(dim,value) series --------------------------------
    recs = [(label(r["period_dt"]), "total", "all", r["id"]) for _, r in df.iterrows()]
    for dim in TREND_DIMS:
        for _, r in df.iterrows():
            for v in (r[dim].split(";") if r[dim] else []):
                if v:
                    recs.append((label(r["period_dt"]), dim, v, r["id"]))
    long = pd.DataFrame(recs, columns=["period", "dim", "value", "id"])
    rollup = (long.groupby(["period", "dim", "value"])["id"].nunique()
                  .rename("count").reset_index().sort_values(["dim", "value", "period"]))
    rollup.to_csv(ROLLUP.format(product=product, grain=grain), index=False)

    def series(dim, value):
        s = rollup[(rollup["dim"] == dim) & (rollup["value"] == value)]
        m = dict(zip(s["period"], s["count"]))
        return [int(m.get(pl, 0)) for pl in plabels]

    def series_mask(mask):
        sub = df[mask]
        c = sub.groupby(sub["period_dt"].map(label))["id"].nunique()
        return [int(c.get(pl, 0)) for pl in plabels]

    # --- assemble markdown ---------------------------------------------------
    n = len(df)
    answered = (df["is_answered"] == "true").sum()
    fat = pd.to_numeric(df["first_answer_hours"], errors="coerce").dropna()
    out = []
    W = out.append
    win_txt = f"trailing {len(periods)} {UNIT[grain]}s" if (win and win > 0) else "all history"
    # Jekyll front matter so GitHub Pages renders this as a styled page
    # (matches html_reports/ convention: layout: default + title).
    W("---")
    W("layout: default")
    W(f"title: Spike Report — {product.title()} ({grain})")
    W("---")
    W("")
    W(f"# Thunderbird {product.title()} — Support Spike Report")
    W(f"\n_Generated {plabels[0]} … {plabels[-1]} · **{grain}** grain · "
      f"{win_txt} · {n} questions · no AI (regex + traditional stats)_\n")
    W(f"- **Volume:** {n} questions, {n / max(len(periods),1):.1f}/{UNIT[grain]} avg")
    W(f"- **Answered (non-creator):** {answered}/{n} ({100*answered/n:.0f}%)")
    if len(fat):
        W(f"- **First-answer time (median):** {fat.median():.1f}h "
          f"(p25 {fat.quantile(.25):.1f}h / p75 {fat.quantile(.75):.1f}h)")
    W(f"- **Total volume trend:** `{spark(series('total','all'))}`\n")

    # Engineering signal (the headline)
    W("## 🚨 Engineering signal — version × cause spikes\n")
    W("Cause clusters over-represented in a specific Thunderbird version, ranked "
      "by **lift** (× more than release-adoption alone explains). Click an ID to read it.\n")
    jpath = JOINT_CSV.format(product=product)
    if os.path.exists(jpath):
        j = pd.read_csv(jpath, dtype=str, keep_default_na=False)
    else:
        j = pd.DataFrame()
    if not j.empty:  # keep only spikes inside the window (ISO dates sort lexically)
        j = j[j["date"] >= window_start.date().isoformat()]
    if j.empty:
        W("_No version×cause spikes in this window at current thresholds._\n")
    else:
        W("")  # kramdown needs a blank line before a table block
        W("| Lift | When | Version × Cause | Qs | Trend | Example questions |")
        W("|---:|:--|:--|--:|:--|:--|")
        title_by_id = dict(zip(df["id"], df["title"]))
        for _, r in j.iterrows():
            ver, dim, val = r["version_major"], r["cause_dim"], r["cause_value"]
            sl = spark(series_mask(
                (df["tb_version_major"] == ver) &
                df[dim].apply(lambda c: val in (c.split(";") if c else []))))
            ids = r["question_ids"].split()
            links = " ".join(
                f'[{i}]({QUESTION_URL.format(id=i)} "{md_safe(title_by_id.get(i,""))}")'
                for i in ids[:6])
            if len(ids) > 6:
                links += f" +{len(ids)-6}"
            W(f"| **{r['lift']}×** | {r['date']} | v{ver} × {val} | {r['observed']} "
              f"| `{sl}` | {links} |")
        W("")

    # Trends
    W("## 📈 Trends\n")
    for dim, title in [("tb_version_major", "Top versions"),
                       ("mail_provider", "Top mail providers"),
                       ("protocol", "Top protocols"),
                       ("isp", "Top ISPs"),
                       ("av", "Top antivirus"),
                       ("os", "OS mix (filter dimension)")]:
        tot = (rollup[rollup["dim"] == dim].groupby("value")["count"].sum()
               .sort_values(ascending=False).head(6))
        if tot.empty:
            continue
        W(f"### {title}")
        W("")  # kramdown needs a blank line before a table block
        W("| Value | Total | Trend |")
        W("|:--|--:|:--|")
        for value, cnt in tot.items():
            disp = f"v{value}" if dim == "tb_version_major" else value
            W(f"| {disp} | {int(cnt)} | `{spark(series(dim, value))}` |")
        W("")

    W("---")
    W(f"\n_Notes: volume / cause / OS trends span the full scraper history "
      f"(2023-01+). **Version×cause covers 2026-02 onward** — the native "
      f"`thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) "
      f"is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier "
      f"questions carry no version. Thresholds (joint min_count=4/lift≥3) are "
      f"calibrated on the post-backfill baseline. Full question IDs per spike are "
      f"in `{jpath}`; full series in `{ROLLUP.format(product=product, grain=grain)}`._")

    os.makedirs(REPORT_DIR.format(product=product), exist_ok=True)
    rpath = f"{REPORT_DIR.format(product=product)}/{grain}-spike-report.md"
    with open(rpath, "w") as f:
        f.write("\n".join(out) + "\n")

    print(f"=== {product} {grain} report ===")
    print(f"inputs: {len(files)} feature files, {n} questions, "
          f"{plabels[0]}..{plabels[-1]} ({len(periods)} periods)")
    print(f"wrote {ROLLUP.format(product=product, grain=grain)} ({len(rollup)} rows)")
    print(f"wrote {rpath}")


if __name__ == "__main__":
    main()
