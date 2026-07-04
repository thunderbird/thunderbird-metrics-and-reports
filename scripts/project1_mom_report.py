"""Project 1 — engineering-management month-over-month summary (PROTOTYPE).

Audience: **Thunderbird engineering management** (NOT community/support ops — a
separate community report, with answered/solved/response-time KPIs, comes later).
So this leads with *what engineering should investigate*: the incidents flagged
this month (version×cause regressions + cause-level surges), what support-cause
clusters moved, and release adoption — CURRENT calendar month vs PREVIOUS.

No AI — pandas + the existing feature tables and spike CSVs.

  uv run scripts/project1_mom_report.py 2026-06 2026-05 desktop

Writes PROJECT1/REPORTS/{product}/monthly-summary-{cur}-vs-{prev}.md
"""
import sys
import csv
import os
import glob
import calendar
import argparse
from datetime import datetime
import pandas as pd

csv.field_size_limit(sys.maxsize)

FEATURES = "PROJECT1/{m}-{product}-features.csv"
JOINT = "PROJECT1/{product}-daily-version-cause-spikes.csv"
CAUSELVL = "PROJECT1/{product}-monthly-single-spikes.csv"
REPORT_DIR = "PROJECT1/REPORTS/{product}"
QUESTION_URL = "https://support.mozilla.org/questions/{id}"
CAUSE_DIMS = ["mail_provider", "protocol", "av"]


def human_month(m):
    return datetime.strptime(m, "%Y-%m").strftime("%B %Y")


def md_safe(s):
    return (s or "").replace("|", "¦").replace('"', "＂")[:80]


def load(m, product):
    p = FEATURES.format(m=m, product=product)
    if not os.path.exists(p):
        return None  # month not materialized yet (e.g. first hours of a new month)
    return pd.read_csv(p, dtype=str, keep_default_na=False)


def delta(old, new, unit="", pct=True):
    """Neutral MoM delta (no value judgement — engineering reads volume/counts
    contextually)."""
    d = new - old
    arrow = "▲" if d > 0 else ("▼" if d < 0 else "▬")
    txt = f"{arrow} {'+' if d > 0 else ''}{d:g}{unit}"
    if pct and old >= 10:  # skip % off a tiny base (e.g. v152 1->158 = +15700%, noise)
        txt += f" ({'+' if d >= 0 else ''}{100 * d / old:.0f}%)"
    return txt


def counts(df, dims):
    """value -> distinct-question count, unioned across the given tag columns."""
    c = {}
    for dim in dims:
        ex = df.assign(v=df[dim].str.split(";")).explode("v")
        for v, g in ex[ex["v"].str.len() > 0].groupby("v"):
            c[v] = c.get(v, 0) + g["id"].nunique()
    return c


def joint_in(product, month):
    p = JOINT.format(product=product)
    if not os.path.exists(p):
        return pd.DataFrame()
    j = pd.read_csv(p, dtype=str, keep_default_na=False)
    return j[j["period"].str.startswith(month)] if not j.empty else j


def causelvl_in(product, month):
    p = CAUSELVL.format(product=product)
    if not os.path.exists(p):
        return pd.DataFrame()
    s = pd.read_csv(p, dtype=str, keep_default_na=False)
    return s[(s["period"] == month) & (s["dim"].isin(CAUSE_DIMS))] if not s.empty else s


def movers_table(W, cur, prev, cdf, pdf, dims, label, min_either=8, top=8):
    cc, pc = counts(cdf, dims), counts(pdf, dims)
    rows = [(v, pc.get(v, 0), cc.get(v, 0), cc.get(v, 0) - pc.get(v, 0))
            for v in set(cc) | set(pc) if max(cc.get(v, 0), pc.get(v, 0)) >= min_either]
    rows.sort(key=lambda r: -abs(r[3]))
    if not rows:
        return
    W(f"### {label}\n")
    W(f"| {label} | {human_month(prev)} | {human_month(cur)} | Change |")
    W("|:--|--:|--:|:--|")
    for v, o, n, _ in rows[:top]:
        W(f"| {v} | {o} | {n} | {delta(o, n)} |")
    W("")


def mix_table(W, cur, prev, cdf, pdf, col, label, top=6, vprefix=""):
    """MoM breakdown of a single tag column (version / os / topic)."""
    cc, pc = counts(cdf, [col]), counts(pdf, [col])
    tops = sorted(set(cc) | set(pc), key=lambda v: -(cc.get(v, 0) + pc.get(v, 0)))[:top]
    if not tops:
        return
    W(f"### {label}\n")
    W(f"| {label} | {human_month(prev)} | {human_month(cur)} | Change |")
    W("|:--|--:|--:|:--|")
    for v in tops:
        W(f"| {vprefix}{v} | {pc.get(v,0)} | {cc.get(v,0)} | {delta(pc.get(v,0), cc.get(v,0))} |")
    W("")


def causes_seen_before(product, cur):
    """Set of cause values that appear in ANY month strictly before `cur`."""
    seen = set()
    for f in glob.glob(FEATURES.format(m="*", product=product)):
        if os.path.basename(f)[:7] >= cur:
            continue
        d = pd.read_csv(f, dtype=str, keep_default_na=False,
                        usecols=lambda c: c in CAUSE_DIMS)
        for dim in CAUSE_DIMS:
            if dim in d:
                for cell in d[dim]:
                    seen.update(v for v in (cell.split(";") if cell else []) if v)
    return seen


def ids_for_cause(df, val):
    """Distinct question ids in df whose any cause column contains `val`."""
    ids = []
    for dim in CAUSE_DIMS:
        ids += list(df[df[dim].apply(lambda c: val in (c.split(";") if c else []))]["id"])
    return list(dict.fromkeys(ids))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("current", help="current calendar month YYYY-MM")
    ap.add_argument("previous", help="previous calendar month YYYY-MM")
    ap.add_argument("product", choices=["desktop", "android"])
    ap.add_argument("--latest", action="store_true",
                    help="also write monthly-summary-latest.md (the bookmarkable copy)")
    args = ap.parse_args()
    cur, prev, product = args.current, args.previous, args.product
    cdf, pdf = load(cur, product), load(prev, product)
    if cdf is None or pdf is None:
        print(f"skip {cur} vs {prev}: feature table(s) not available yet")
        return
    cj, pj = joint_in(product, cur), joint_in(product, prev)
    cs, ps = causelvl_in(product, cur), causelvl_in(product, prev)
    n_new = int((cj["novelty"] == "new").sum()) if not cj.empty and "novelty" in cj else 0
    p_new = int((pj["novelty"] == "new").sum()) if not pj.empty and "novelty" in pj else 0

    out, W = [], lambda s: out.append(s)
    W("---")
    W("layout: default")
    W(f"title: Desktop Engineering Support Summary — {human_month(cur)}")
    W("---")
    W("")
    W("# Thunderbird Desktop — Monthly Engineering Support Summary")
    W(f"\n## {human_month(cur)} vs {human_month(prev)}\n")
    W("_For **engineering**: the support signals worth investigating this month vs "
      "last — flagged incidents, moving cause clusters, and release adoption. "
      "(Community/support-ops KPIs — answered & solved rates, response time — are a "
      "separate upcoming report.) Non-AI: regex + traditional stats._\n")

    # partial-month caveat: the current calendar month is incomplete until it ends,
    # so raw counts (and MoM deltas) understate it. Detected from the latest data day.
    y, mo = map(int, cur.split("-"))
    last_day = calendar.monthrange(y, mo)[1]
    cur_days = pd.to_numeric(cdf["created_date"].str.slice(8, 10), errors="coerce")
    max_day = int(cur_days.max()) if cur_days.notna().any() else 0
    if max_day < last_day:
        W(f"> ⚠️ **{human_month(cur)} is in progress** — data through day {max_day} of "
          f"{last_day}. Counts are partial, so the deltas below understate "
          f"{human_month(cur)}; treat volume changes as directional until the month "
          f"closes.\n")

    # --- headline ------------------------------------------------------------
    W("## Headline\n")
    W(f"| | {human_month(prev)} | {human_month(cur)} | Change |")
    W("|:--|--:|--:|:--|")
    W(f"| Support questions (load) | {len(pdf)} | {len(cdf)} | {delta(len(pdf), len(cdf))} |")
    W(f"| Version × cause spikes flagged | {len(pj)} | {len(cj)} | {delta(len(pj), len(cj), pct=False)} |")
    W(f"| — of which **new** regressions | {p_new} | {n_new} | {delta(p_new, n_new, pct=False)} |")
    W(f"| Cause-level surges flagged | {len(ps)} | {len(cs)} | {delta(len(ps), len(cs), pct=False)} |")
    W("")

    # --- incidents (the lead for engineering) --------------------------------
    W("## 🚨 Incidents to investigate\n")
    W("> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a "
      "*lagging* signal, usually days after an incident's onset and often near its "
      "resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions "
      "spiked Jun 19). Treat these as pain-cluster / triage signals, **not** "
      "real-time incident detection.\n")
    title_by_id = dict(zip(cdf["id"], cdf["title"]))

    def links(ids):
        L = " ".join(f'[{i}]({QUESTION_URL.format(id=i)} "{md_safe(title_by_id.get(i,""))}")'
                     for i in ids[:5])
        return L + (f" +{len(ids)-5}" if len(ids) > 5 else "")

    if cj.empty and cs.empty:
        W("_No spikes flagged this month at current thresholds._\n")
    if not cj.empty:
        W("### Version × cause — possible release regressions\n")
        W("Ranked new → spreading → recurring, then by lift (× above what release "
          "adoption alone explains).\n")
        W("| Signal | When | Version × Cause | Qs | Lift | Example questions |")
        W("|:--|:--|:--|--:|--:|:--|")
        order = {"new": 0, "spreading": 1, "recurring": 2}
        cj = cj.assign(_r=cj.get("novelty", "").map(order).fillna(3),
                       _l=pd.to_numeric(cj["lift"], errors="coerce")).sort_values(
            ["_r", "_l"], ascending=[True, False])
        badge = {"new": "🆕 new", "spreading": "↗ spreading", "recurring": "↻ recurring"}
        for _, r in cj.iterrows():
            W(f"| {badge.get(r.get('novelty',''),'')} | {r['period']} | "
              f"v{r['version_major']} × {r['cause_value']} | {r['observed']} | {r['lift']}× "
              f"| {links(r['question_ids'].split())} |")
        W("")
    if not cs.empty:
        W("### Cause-level surges — provider / protocol / AV (any version)\n")
        W("Version-agnostic (a provider outage spans versions), vs a trailing-month baseline.\n")
        W("| Cause | Qs | vs baseline | Rise | Example questions |")
        W("|:--|--:|--:|:--|:--|")
        cs = cs.assign(_m=pd.to_numeric(cs["magnitude"].replace("new", 1e9), errors="coerce")
                       ).sort_values("_m", ascending=False)
        for _, r in cs.iterrows():
            mag = r["magnitude"]
            W(f"| {r['value']} | {r['count']} | {r['baseline_median']} "
              f"| {mag if mag=='new' else mag+'×'} | {links(r['question_ids'].split())} |")
        W("")

    # --- cause movers, new causes, versions, os, topics ---------------------
    W("## What moved\n")
    movers_table(W, cur, prev, cdf, pdf, CAUSE_DIMS, "Cause clusters (provider / protocol / AV)")

    # cause clusters that have NEVER appeared in any prior month
    seen = causes_seen_before(product, cur)
    new_causes = sorted(((v, n) for v, n in counts(cdf, CAUSE_DIMS).items() if v not in seen),
                        key=lambda x: -x[1])
    W("### 🆕 New cause clusters (first appearance ever)\n")
    if not new_causes:
        W(f"_None — every cause cluster in {human_month(cur)} has appeared in a prior month._\n")
    else:
        W("Cause tags with no occurrence in any month before this one — a new entity "
          "or newly-matched pattern, worth a look.\n")
        W("| Cause | Qs | Example questions |")
        W("|:--|--:|:--|")
        for v, n in new_causes:
            W(f"| {v} | {n} | {links(ids_for_cause(cdf, v))} |")
        W("")

    mix_table(W, cur, prev, cdf, pdf, "tb_version_major", "Release adoption (version mix)", vprefix="v")
    mix_table(W, cur, prev, cdf, pdf, "os", "Operating-system mix")
    mix_table(W, cur, prev, cdf, pdf, "topic", "Topic mix")

    W("---")
    W(f"\n_Prototype engineering month-over-month summary · from Project 1 feature "
      f"tables + spike detectors · {human_month(cur)} vs {human_month(prev)}._")

    rdir = REPORT_DIR.format(product=product)
    os.makedirs(rdir, exist_ok=True)
    content = "\n".join(out) + "\n"
    path = f"{rdir}/monthly-summary-{cur}-vs-{prev}.md"
    with open(path, "w") as f:
        f.write(content)
    print(f"wrote {path}")
    if args.latest:  # bookmarkable copy management links to
        latest = f"{rdir}/monthly-summary-latest.md"
        with open(latest, "w") as f:
            f.write(content)
        print(f"wrote {latest}")
    print(f"  {human_month(cur)}: {len(cdf)} qs · {len(cj)} version×cause ({n_new} new) "
          f"· {len(cs)} cause-level  |  {human_month(prev)}: {len(pdf)} qs · {len(pj)} v×c · {len(ps)} cause")


if __name__ == "__main__":
    main()
