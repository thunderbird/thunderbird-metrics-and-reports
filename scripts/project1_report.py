"""Project 1 — Bucket 3: reporting (CSV rollups + blog post with sparklines).

Presentation layer over the feature tables and the spike detectors. Produces:
  1. PROJECT1/{product}-{grain}-rollup.csv  — long-format counts per
     (period, dim, value): the time series behind every sparkline and the
     basis for future grains.
  2. PROJECT1/REPORTS/{product}/{grain}-spike-report.md — a Jekyll-ready blog
     post with TWO engineering signals, both with clickable IDs + sparklines:
       - version×cause spikes (ranked by lift — "is this a release regression?")
       - cause-level spikes (provider/protocol/AV surging regardless of
         version — provider outages like GMX that span versions), plus volume /
         version / cause trends and a responsiveness summary.

Sparklines are Unicode blocks (no image assets). All five report grains
(hourly/daily/monthly/quarterly/yearly) are live post-backfill. Each report grain
reads the spike DETECTOR grain it maps to (DETECTOR_GRAIN): fine grains read the
daily detector, coarse grains the monthly one — so slow-burn incidents surface at
the coarser reports. Volume/cause/OS trends span full history; version×cause is
limited to versioned rows (2026-02+); cause-level uses all history.

No AI — pure pandas + stdlib. Run AFTER extract/backfill + detectors (per grain):
  uv run scripts/project1_backfill_features.py desktop
  for g in daily weekly monthly; do
    uv run scripts/project1_spike_detect.py desktop --grain $g
    uv run scripts/project1_joint_spike_detect.py desktop --grain $g
  done
  uv run scripts/project1_report.py desktop --grain monthly   (per grain)
"""
import sys
import csv
import glob
import os
import argparse
from datetime import datetime, timezone
import pandas as pd

csv.field_size_limit(sys.maxsize)

FEATURES_GLOB = "PROJECT1/*-{product}-features.csv"
JOINT_CSV = "PROJECT1/{product}-{dgrain}-version-cause-spikes.csv"
SINGLE_CSV = "PROJECT1/{product}-{dgrain}-single-spikes.csv"
ROLLUP = "PROJECT1/{product}-{grain}-rollup.csv"
REPORT_DIR = "PROJECT1/REPORTS/{product}"
QUESTION_URL = "https://support.mozilla.org/questions/{id}"
BLOCKS = "▁▂▃▄▅▆▇█"

# Report grain -> spike-DETECTOR grain (project1_grains.py runs daily/weekly/
# monthly). Fine report grains read the daily detector; coarse ones read monthly.
DETECTOR_GRAIN = {"hourly": "daily", "daily": "daily", "monthly": "monthly",
                  "quarterly": "monthly", "yearly": "monthly"}
# joint-spike novelty (from project1_joint_spike_detect.py) -> report badge
NOVELTY_BADGE = {"new": "🆕 new", "spreading": "↗ spreading", "recurring": "↻ recurring"}

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
CAUSE_DIMS = ["mail_provider", "protocol", "av"]  # OS is a filter, not a cause
TREND_DIMS = ["tb_version_major"] + CAUSE_DIMS + ["os", "macos_release"]


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


def parse_period(label):
    """Detector-grain period label -> start Timestamp. 'YYYY-MM' (monthly) ->
    the 1st; 'YYYY-MM-DD' (daily/weekly) -> that day. For window filtering."""
    label = (label or "").strip()
    return pd.to_datetime(label + ("-01" if len(label) == 7 else ""), errors="coerce")


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
    # tolerate feature files that predate a newer tag column (e.g. macos_release
    # before a full re-extract) so trends don't crash on a missing/NaN column.
    for c in TREND_DIMS:
        df[c] = df[c].fillna("") if c in df.columns else ""
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
    W("layout: base")  # minima 3.x renamed 'default' -> 'base'; 'default' no longer exists (#72)
    W(f"title: {grain.upper()}: Thunderbird {product.title()} — Support Spike Report")
    W("---")
    W("")
    W(f"# {grain.upper()}: Thunderbird {product.title()} — Support Spike Report")
    W(f"\n_Generated {plabels[0]} … {plabels[-1]} · **{grain}** grain · "
      f"{win_txt} · {n} questions · no AI (regex + traditional stats)_\n")
    W(f"- **Volume:** {n} questions, {n / max(len(periods),1):.1f}/{UNIT[grain]} avg")
    W(f"- **Answered (non-creator):** {answered}/{n} ({100*answered/n:.0f}%)")
    if len(fat):
        W(f"- **First-answer time (median):** {fat.median():.1f}h "
          f"(p25 {fat.quantile(.25):.1f}h / p75 {fat.quantile(.75):.1f}h)")
    W(f"- **Total volume trend:** `{spark(series('total','all'))}`\n")

    W("> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a "
      "*lagging* signal, usually days after an incident's onset and often near its "
      "resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions "
      "spiked Jun 19). Treat these as pain-cluster / triage signals, **not** "
      "real-time incident detection.\n")

    # spike CSVs are read at the DETECTOR grain matching this report grain
    dgrain = DETECTOR_GRAIN[grain]
    title_by_id = dict(zip(df["id"], df["title"]))

    def in_window(spikes):
        if spikes.empty:
            return spikes
        return spikes[spikes["period"].map(parse_period) >= window_start]

    def links_for(ids):
        links = " ".join(
            f'[{i}]({QUESTION_URL.format(id=i)} "{md_safe(title_by_id.get(i, ""))}")'
            for i in ids[:6])
        return links + (f" +{len(ids) - 6}" if len(ids) > 6 else "")

    def served(r):
        """Responsiveness amplifier (#68): '⚠️ 43% ans · 8h' — ⚠️ when the spike's
        questions are answered below 60% (baseline is ~76%)."""
        ap = str(r.get("answered_pct", "")).strip()
        if ap == "":
            return ""
        ap = int(float(ap))
        md = str(r.get("median_first_answer_h", "")).strip()
        return f"{'⚠️ ' if ap < 60 else ''}{ap}% ans{f' · {md}h' if md else ''}"

    # Engineering signal #1 — version × cause (the "is this a release regression?")
    W("## 🚨 Engineering signal — version × cause spikes\n")
    W("Cause clusters over-represented in a specific Thunderbird version. The "
      "**Signal** column flags 🆕 **new** (cause never spiked before), ↗ "
      "**spreading** (known cause, new version), or ↻ **recurring** (chronic / seen "
      "before) — ranked new→spreading→recurring, then by **lift**. Click an ID to read it.\n")
    jpath = JOINT_CSV.format(product=product, dgrain=dgrain)
    j = in_window(pd.read_csv(jpath, dtype=str, keep_default_na=False)
                  if os.path.exists(jpath) else pd.DataFrame())
    if not j.empty and "novelty" in j.columns:  # rank new -> spreading -> recurring, then lift
        j = j.assign(_r=j["novelty"].map({"new": 0, "spreading": 1, "recurring": 2}).fillna(3),
                     _l=pd.to_numeric(j["lift"], errors="coerce"))
        j = j.sort_values(["_r", "_l"], ascending=[True, False])
    if j.empty:
        W("_No version×cause spikes in this window at current thresholds._\n")
    else:
        W("")  # kramdown needs a blank line before a table block
        W("| Signal | Lift | When | Version × Cause | Qs | Served | Trend | Example questions |")
        W("|:--|---:|:--|:--|--:|:--|:--|:--|")
        for _, r in j.iterrows():
            ver, dim, val = r["version_major"], r["cause_dim"], r["cause_value"]
            sl = spark(series_mask(
                (df["tb_version_major"] == ver) &
                df[dim].apply(lambda c: val in (c.split(";") if c else []))))
            W(f"| {NOVELTY_BADGE.get(r.get('novelty', ''), '')} | **{r['lift']}×** "
              f"| {r['period']} | v{ver} × {val} | {r['observed']} | {served(r)} "
              f"| `{sl}` | {links_for(r['question_ids'].split())} |")
        W("")

    # Engineering signal #2 — cause-level spikes (version-agnostic: provider/ISP
    # outages, protocol/AV surges — e.g. the March 2026 GMX provider outage, which
    # spans versions and so never shows up in the version×cause table above).
    W("## 📮 Cause-level spikes — provider / protocol / AV\n")
    W(f"Causes surging **regardless of version** vs a trailing {UNIT[dgrain]} "
      f"baseline — provider/ISP outages and protocol/AV issues. Not necessarily a "
      f"Thunderbird bug, but worth a triage look. Ranked by magnitude.\n")
    spath = SINGLE_CSV.format(product=product, dgrain=dgrain)
    s = pd.read_csv(spath, dtype=str, keep_default_na=False) if os.path.exists(spath) else pd.DataFrame()
    if not s.empty:
        s = in_window(s[s["dim"].isin(CAUSE_DIMS)])
        s["_mag"] = pd.to_numeric(s["magnitude"].replace("new", 1e9), errors="coerce")
        s = s.sort_values(["_mag", "count"], ascending=False)
    if s.empty:
        W("_No cause-level spikes in this window at current thresholds._\n")
    else:
        W("")
        W("| Rise | When | Cause | Qs | Served | Baseline | Trend | Example questions |")
        W("|---:|:--|:--|--:|:--|--:|:--|:--|")
        for _, r in s.iterrows():
            dim, val = r["dim"], r["value"]
            sl = spark(series_mask(df[dim].apply(lambda c: val in (c.split(";") if c else []))))
            mag = "new" if r["magnitude"] == "new" else f"{float(r['magnitude']):.1f}×"
            W(f"| **{mag}** | {r['period']} | {val} | {r['count']} | {served(r)} | {r['baseline_median']} "
              f"| `{sl}` | {links_for(r['question_ids'].split())} |")
        W("")

    # Trends
    W("## 📈 Trends\n")
    for dim, title in [("tb_version_major", "Top versions"),
                       ("mail_provider", "Top mail providers"),
                       ("protocol", "Top protocols"),
                       ("av", "Top antivirus"),
                       ("os", "OS mix (filter dimension)"),
                       ("macos_release", "macOS releases (filter dimension)")]:
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
    W(f"\n_Notes: spikes detected at **{dgrain}** grain (coarser grains catch "
      f"slow-burn incidents a daily threshold misses — e.g. the March 2026 GMX "
      f"provider outage). Volume / cause / OS trends span the full scraper history "
      f"(2023-01+). **Version×cause covers 2026-02 onward** — the native "
      f"`thunderbird_version` field ([Kitsune PR #7443](https://github.com/mozilla/kitsune/pull/7443)) "
      f"is only populated from Feb 2026 (~27% → 85% by mid-2026), so earlier "
      f"questions carry no version; cause-level spikes use all history. Thresholds "
      f"calibrated on the post-backfill baseline. Full IDs per spike in `{jpath}` "
      f"(version×cause) and `{spath}` (cause-level); full series in "
      f"`{ROLLUP.format(product=product, grain=grain)}`._")
    W(f"\n_Last updated: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}_")

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
