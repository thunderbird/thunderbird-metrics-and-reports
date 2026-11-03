"""Links between the Project 1 spike pages and the LLM Insights pages (#95).

Project 1 (no AI) counts questions per cause tag and flags a spike when a tag
rises well above its baseline. The LLM Insights page groups the same questions
into named problems. Before #95 neither page said what the other one found.

One source of truth, in one direction:

1. `llm_insights_mom_report.py` reads the committed spike CSVs through
   `spike_signals()`, decides which LLM issue holds each spiking tag, prints a
   "Project 1 signal" line and an anchor (`anchor(tag)`) on that issue, and
   writes a sidecar JSON next to the page (`sidecar_path()`).
2. `project1_exec_summary.py` reads that sidecar (`find_sidecar()`) and links
   each "What stands out" item to the LLM issue. It links only to anchors the
   sidecar lists, so a link can never point at a missing anchor.

Pure pandas, no LLM, no cost.
"""
import glob
import json
import os

import pandas as pd

SINGLE_CSV = "PROJECT1/{product}-{grain}-single-spikes.csv"
JOINT_CSV = "PROJECT1/{product}-{grain}-version-cause-spikes.csv"
GRAINS = ("daily", "weekly", "monthly")
# The cause dimensions the executive summary reports. `feature` is included
# here (unlike the LLM clustering hints), because "What stands out" lists
# feat: tags such as the v154 printing regression.
CAUSE_DIMS = ["mail_provider", "av", "protocol", "feature"]
FEATURES = "PROJECT1/{m}-{product}-features.csv"
LLM_DIR = "LLM_INSIGHTS/REPORTS/{product}"
P1_DIR = "PROJECT1/REPORTS/{product}"
WEEK_LEN_DAYS = 7


def anchor(tag):
    """Stable HTML id for a cause tag: `m:att` -> `p1-m-att`. Unlike
    `#issue-N`, it does not move when the issue order changes."""
    return "p1-" + "".join(c if c.isalnum() else "-" for c in tag.lower())


def month_bounds(month):
    """(first instant, last instant) of the month. Not MonthEnd(1): that is
    the last DAY at 00:00 and drops the final day (see CLAUDE.md)."""
    start = pd.Timestamp(month + "-01")
    return start, start + pd.offsets.MonthBegin(1) - pd.Timedelta(nanoseconds=1)


def in_month(periods, month, grain):
    """Same rule as the executive summary: a week counts when it OVERLAPS
    the month, so both pages agree on which spikes belong to a month."""
    if periods.empty:
        return periods.astype(bool)
    if grain == "monthly":
        return periods.astype(str) == month
    start, end = month_bounds(month)
    dt = pd.to_datetime(periods, errors="coerce")
    if grain == "weekly":
        return (dt <= end) & (dt + pd.Timedelta(days=WEEK_LEN_DAYS - 1) >= start)
    return (dt >= start) & (dt <= end)


def when(grain, period):
    if grain == "weekly":
        return f"in the week of {period}"
    if grain == "daily":
        return f"on {period}"
    return f"in {pd.Timestamp(period + '-01').strftime('%B %Y')}"


def spike_signals(product, month):
    """-> DataFrame, one row per cause-level or version x cause spike in
    `month`: tag, kind (cause|joint), grain, period, count, baseline, version,
    ratio (for ranking; a spike from a baseline of zero ranks first)."""
    rows = []
    for grain in GRAINS:
        p = SINGLE_CSV.format(product=product, grain=grain)
        if os.path.exists(p):
            df = pd.read_csv(p, dtype=str, keep_default_na=False)
            df = df[df["dim"].isin(CAUSE_DIMS)]
            df = df[in_month(df["period"], month, grain)]
            for _, r in df.iterrows():
                new = r["magnitude"] == "new"
                rows.append({
                    "tag": r["value"], "kind": "cause", "grain": grain,
                    "period": r["period"], "count": int(float(r["count"])),
                    "baseline": r["baseline_median"], "version": "",
                    "ratio": 1e9 if new else float(r["magnitude"] or 0),
                    "new": new})
        p = JOINT_CSV.format(product=product, grain=grain)
        if os.path.exists(p):
            df = pd.read_csv(p, dtype=str, keep_default_na=False)
            df = df[in_month(df["period"], month, grain)]
            for _, r in df.iterrows():
                rows.append({
                    "tag": r["cause_value"], "kind": "joint", "grain": grain,
                    "period": r["period"], "count": int(float(r["observed"])),
                    "baseline": r["expected"], "version": r["version_major"],
                    "ratio": float(r["lift"] or 0), "new": False})
    return pd.DataFrame(rows, columns=["tag", "kind", "grain", "period", "count",
                                       "baseline", "version", "ratio", "new"])


def signal_text(r):
    """One spike, read out loud."""
    if r["kind"] == "joint":
        return (f"`v{r['version']} × {r['tag']}`, {r['grain']} spike "
                f"{when(r['grain'], r['period'])}: {r['count']} questions, "
                f"{r['ratio']:.1f} times the expected {float(r['baseline']):.1f}")
    base = (f"where earlier periods had none" if r["new"]
            else f"against a baseline of {r['baseline']}")
    return (f"`{r['tag']}`, {r['grain']} spike {when(r['grain'], r['period'])}: "
            f"{r['count']} questions {base}")


def explore_link(product, r, from_dir):
    """Deep link into the Project 1 explorer, relative to `from_dir`, or ""
    when the product has no explorer (android today). Uses the DETECTOR grain
    and period, which is the explorer's contract (see project1_report.py)."""
    if not os.path.exists(f"{P1_DIR.format(product=product)}/explorer.html"):
        return ""
    rel = os.path.relpath(P1_DIR.format(product=product), from_dir)
    q = [f"grain={r['grain']}"]
    if r["version"]:
        q.append(f"version={r['version']}")
    q += [f"cause={r['tag']}", f"period={r['period']}"]
    return f"[explore ↗]({rel}/explorer.html#{'&'.join(q)})"


def tags_by_id(product, month):
    """-> {question id: set of cause tags} for `month`."""
    p = FEATURES.format(m=month, product=product)
    if not os.path.exists(p):
        return {}
    f = pd.read_csv(p, dtype=str, keep_default_na=False)
    out = {}
    for _, r in f.iterrows():
        tags = {t for d in CAUSE_DIMS for t in str(r[d]).split(";") if t}
        if tags:
            out[r["id"]] = tags
    return out


def sidecar_path(product, cur, prev):
    return f"{LLM_DIR.format(product=product)}/monthly-summary-{cur}-vs-{prev}.json"


def find_sidecar(product, month):
    """-> the sidecar dict for the LLM page whose CURRENT month is `month`,
    or None when there is no LLM page for that month yet."""
    hits = sorted(glob.glob(sidecar_path(product, month, "*")))
    if not hits:
        return None
    with open(hits[-1]) as f:
        return json.load(f)
