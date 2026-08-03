"""Project 1 — one-month EXECUTIVE summary: "was <month> clean?", verdict first.

Audience: Thunderbird engineering (and their management) who want the answer, not
the analysis. The page leads with a single verdict and a detector x grain count
table, then hides ALL of the month's detail behind collapsed <details> blocks.

Distinct from the two existing Project 1 pages:
  - {grain}-spike-report.md  — a trailing window per grain, browsing-oriented.
  - monthly-summary-*.md     — current vs previous month, a "what moved" narrative.
  - THIS                     — one calendar month, clean-or-not, everything else
                               collapsed. Answers "do we need to look at July?"

Run per month (auto-rolls in CI: the most recent COMPLETE month plus the
in-progress one, so July keeps refreshing through August):
  uv run scripts/project1_exec_summary.py 2026-07 desktop --latest
  uv run scripts/project1_exec_summary.py 2026-08 desktop

--latest also writes exec-summary-latest.md, the bookmarkable copy.

WHY REGENERATE A CLOSED MONTH DAILY: the month's verdict is NOT frozen when the
month ends. The joint detector ranks by lift = observed / (version_volume x
cause_rate_overall), and cause_rate_overall is computed across ALL history — so
questions arriving in August shift July's expected values and July rows can cross
the threshold in EITHER direction after the fact. Observed on 2026-08-03: a
`v140 x proto:smtp` July row sat at lift exactly 3.00 in the morning and dropped
below the floor hours later when fresh August data raised its expected value.
Answered-% and first-answer-time also keep firming up as late answers land.

No AI — pure pandas + stdlib. Run AFTER the detectors for all three grains.
"""
import os
import sys
import argparse
from datetime import datetime, timezone

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from project1_report import (  # noqa: E402  (shared with the spike reports)
    JOINT_CSV, SINGLE_CSV, QUESTION_URL, CAUSE_DIMS, TREND_DIMS,
    spark, md_safe, load_features,
)

REPORT_DIR = "PROJECT1/REPORTS/{product}"
DETECTOR_GRAINS = ["daily", "weekly", "monthly"]
# A weekly period is keyed by its Monday, so a week can straddle two months. For a
# "did anything happen in <month>" verdict we take any week that OVERLAPS the
# month — missing an incident because its week began on the 29th of the previous
# month would be the worse error.
WEEK_LEN_DAYS = 7


def month_bounds(month):
    """(first instant, LAST instant) of the month, tz-naive UTC.

    Deliberately not `start + MonthEnd(1)`: that returns the last DAY at 00:00:00,
    so an inclusive `<= end` silently drops everything created during the final day
    of the month (32 of July 2026's 731 questions, when this was first written)."""
    start = pd.Timestamp(month + "-01")
    return start, start + pd.offsets.MonthBegin(1) - pd.Timedelta(nanoseconds=1)


def in_month(periods, month, grain):
    """Boolean mask: which detector period labels fall in `month`."""
    if periods.empty:
        return periods.astype(bool)
    if grain == "monthly":
        return periods.astype(str) == month
    start, end = month_bounds(month)
    dt = pd.to_datetime(periods, errors="coerce")
    if grain == "weekly":  # overlap, not containment
        return (dt <= end) & (dt + pd.Timedelta(days=WEEK_LEN_DAYS - 1) >= start)
    return (dt >= start) & (dt <= end)


def load_spikes(product, month):
    """-> {(kind, grain): DataFrame of that grain's spikes inside `month`}."""
    out = {}
    for grain in DETECTOR_GRAINS:
        for kind, tmpl in (("joint", JOINT_CSV), ("single", SINGLE_CSV)):
            path = tmpl.format(product=product, dgrain=grain)
            df = (pd.read_csv(path, dtype=str, keep_default_na=False)
                  if os.path.exists(path) else pd.DataFrame())
            if not df.empty:
                df = df[in_month(df["period"], month, grain)]
            out[(kind, grain)] = df
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("month", help="YYYY-MM")
    ap.add_argument("product", choices=["desktop", "android"])
    ap.add_argument("--latest", action="store_true",
                    help="also write exec-summary-latest.md (the bookmarkable copy)")
    args = ap.parse_args()
    product, month = args.product, args.month
    start, end = month_bounds(month)

    df, _ = load_features(product)
    naive = df["created_dt"].dt.tz_convert(None)
    df = df[(naive >= start) & (naive <= end)].copy()
    if df.empty:
        sys.exit(f"no {product} questions in {month} — nothing to summarise")
    df["day"] = df["created_dt"].dt.tz_convert(None).dt.normalize()

    spikes = load_spikes(product, month)
    # Cause-level = the single-dim detector restricted to CAUSE dims. The
    # tb_version_major / os rows are release-adoption noise by design and are
    # reported separately, never as an incident.
    cause = {g: (s[s["dim"].isin(CAUSE_DIMS)] if not s.empty else s)
             for g, s in ((g, spikes[("single", g)]) for g in DETECTOR_GRAINS)}
    verdim = {g: (s[~s["dim"].isin(CAUSE_DIMS)] if not s.empty else s)
              for g, s in ((g, spikes[("single", g)]) for g in DETECTOR_GRAINS)}
    joint = {g: spikes[("joint", g)] for g in DETECTOR_GRAINS}

    n_joint = sum(len(v) for v in joint.values())
    n_cause = sum(len(v) for v in cause.values())
    incidents = n_joint + n_cause

    n = len(df)
    answered = (df["is_answered"] == "true").sum()
    fat = pd.to_numeric(df["first_answer_hours"], errors="coerce").dropna()
    tagged = df[CAUSE_DIMS].apply(lambda r: any(r), axis=1).sum()
    days = pd.date_range(start, min(end, df["day"].max()), freq="D")
    title_by_id = dict(zip(df["id"], df["title"]))

    def links_for(ids):
        ids = [i for i in ids if i]
        s = " ".join(f'[{i}]({QUESTION_URL.format(id=i)} "{md_safe(title_by_id.get(i, ""))}")'
                     for i in ids[:6])
        return s + (f" +{len(ids) - 6}" if len(ids) > 6 else "")

    def served(r):
        ap_ = str(r.get("answered_pct", "")).strip()
        if not ap_:
            return ""
        ap_ = int(float(ap_))
        md = str(r.get("median_first_answer_h", "")).strip()
        return f"{'⚠️ ' if ap_ < 60 else ''}{ap_}% ans{f' · {md}h' if md else ''}"

    out, W = [], None
    W = out.append
    label = start.strftime("%B %Y")
    # month_bounds is tz-naive UTC, like created_dt after tz_convert(None)
    partial = end > pd.Timestamp.now(tz="UTC").tz_localize(None).normalize()

    W("---")
    W("layout: base")  # minima 3.x renamed 'default' -> 'base' (#72)
    W(f"title: \"{month} exec summary: Thunderbird {product.title()} support spikes\"")
    W("---")
    W("")
    W(f"# {label} — Thunderbird {product.title()} support spikes")
    W(f"\n_Executive summary · **{month}** · {n} questions · regenerated "
      f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC} · no AI (regex + "
      f"traditional stats)_\n")

    # ---- the verdict ------------------------------------------------------
    if incidents == 0:
        W(f"## ✅ {label} was clean\n")
        W(f"**No spike cleared threshold at any grain.** No provider outage, no "
          f"protocol surge, no AV breakage, and no release regression in "
          f"{label}.\n")
    else:
        W(f"## 🚨 {label}: {incidents} spike"
          f"{'s' if incidents != 1 else ''} to investigate\n")
        W(f"**{n_joint} version×cause** (release regressions) and **{n_cause} "
          f"cause-level** (provider / protocol / AV) spike(s) cleared threshold. "
          f"Detail is collapsed below.\n")
    if partial:
        W(f"> ⏳ **{label} is still in progress** — counts will grow.\n")

    W("")
    W("| Detector | daily | weekly | monthly |")
    W("|:--|--:|--:|--:|")
    W("| **version×cause** (release regressions) | "
      + " | ".join(str(len(joint[g])) for g in DETECTOR_GRAINS) + " |")
    W("| **cause-level** (provider · protocol · AV) | "
      + " | ".join(str(len(cause[g])) for g in DETECTOR_GRAINS) + " |")
    W("")

    W(f"- **Volume:** {n} questions "
      f"(`{spark([int((df['day'] == d).sum()) for d in days])}` by day), "
      f"{tagged} ({100*tagged/n:.0f}%) carry a cause tag")
    W(f"- **Answered (non-creator):** {answered}/{n} ({100*answered/n:.0f}%)"
      + (f" · median first answer {fat.median():.1f}h" if len(fat) else ""))
    nv = sum(len(v) for v in verdim.values())
    W(f"- **Release-adoption version spikes:** {nv} "
      f"(expected after a release — not incidents; collapsed below)\n")

    W("> ⏱ **Spike timing lags the incident.** A spike dates when users *piled "
      "in*, typically days after onset and often near resolution. Treat these as "
      "pain-cluster / triage signals, not real-time detection.\n")
    W("> 🔄 **This verdict is not frozen when the month ends.** Lift is measured "
      "against each cause's rate across all history, so later questions shift a "
      "closed month's expected values and rows can cross the threshold in either "
      "direction; answered-% keeps firming up as late answers land. That is why "
      "this page regenerates daily.\n")

    # ---- collapsed detail --------------------------------------------------
    W("---\n")
    W(f"## All {label} detail\n")

    def details(summary, body_fn, count):
        """One collapsed block. kramdown needs markdown="1" to parse markdown
        inside a block-level HTML element."""
        W(f'<details markdown="1">')
        W(f"<summary><strong>{summary}</strong> — {count} row"
          f"{'s' if count != 1 else ''}</summary>")
        W("")
        body_fn()
        W("")
        W("</details>")
        W("")

    def joint_body():
        rows = pd.concat([j.assign(_g=g) for g, j in joint.items() if not j.empty]) \
            if any(len(j) for j in joint.values()) else pd.DataFrame()
        if rows.empty:
            W("_None._")
            return
        rows = rows.assign(_l=pd.to_numeric(rows["lift"], errors="coerce")) \
                   .sort_values("_l", ascending=False)
        W("| Grain | Lift | When | Version × Cause | Qs | Served | Signal | Example questions |")
        W("|:--|--:|:--|:--|--:|:--|:--|:--|")
        for _, r in rows.iterrows():
            W(f"| {r['_g']} | **{r['lift']}×** | {r['period']} | "
              f"v{r['version_major']} × {r['cause_value']} | {r['observed']} | "
              f"{served(r)} | {r.get('novelty','')} | "
              f"{links_for(str(r['question_ids']).split())} |")

    def cause_body():
        rows = pd.concat([c.assign(_g=g) for g, c in cause.items() if not c.empty]) \
            if any(len(c) for c in cause.values()) else pd.DataFrame()
        if rows.empty:
            W("_None._")
            return
        rows = rows.assign(_m=pd.to_numeric(rows["magnitude"].replace("new", 1e9),
                                            errors="coerce")) \
                   .sort_values(["_m", "count"], ascending=False)
        W("| Grain | Rise | When | Cause | Qs | Served | Baseline | Example questions |")
        W("|:--|--:|:--|:--|--:|:--|--:|:--|")
        for _, r in rows.iterrows():
            mag = "new" if r["magnitude"] == "new" else f"{float(r['magnitude']):.1f}×"
            W(f"| {r['_g']} | **{mag}** | {r['period']} | {r['value']} | "
              f"{r['count']} | {served(r)} | {r['baseline_median']} | "
              f"{links_for(str(r['question_ids']).split())} |")

    def verdim_body():
        rows = pd.concat([v.assign(_g=g) for g, v in verdim.items() if not v.empty]) \
            if any(len(v) for v in verdim.values()) else pd.DataFrame()
        if rows.empty:
            W("_None._")
            return
        W("Version and OS are **filters, not causes** — a bare version spike is "
          "release adoption, not a regression. Listed for manual checking only.\n")
        W("| Grain | Rise | When | Dimension | Value | Qs | Baseline |")
        W("|:--|--:|:--|:--|:--|--:|--:|")
        for _, r in rows.sort_values(["_g", "period"]).iterrows():
            mag = "new" if r["magnitude"] == "new" else f"{float(r['magnitude']):.1f}×"
            W(f"| {r['_g']} | **{mag}** | {r['period']} | {r['dim']} | "
              f"{r['value']} | {r['count']} | {r['baseline_median']} |")

    def trends_body():
        for dim, heading in [("tb_version_major", "Top versions"),
                             ("mail_provider", "Top mail providers"),
                             ("protocol", "Top protocols"),
                             ("av", "Top antivirus"),
                             ("os", "OS mix (filter dimension)"),
                             ("macos_release", "macOS releases (filter dimension)")]:
            exploded = (df[dim].str.split(";").explode().dropna())
            exploded = exploded[exploded != ""]
            if exploded.empty:
                continue
            W(f"**{heading}**")
            W("")
            W("| Value | Questions | Trend (by day) |")
            W("|:--|--:|:--|")
            for value, cnt in exploded.value_counts().head(6).items():
                mask = df[dim].apply(lambda c: value in (c.split(";") if c else []))
                by_day = [int(((df["day"] == d) & mask).sum()) for d in days]
                disp = f"v{value}" if dim == "tb_version_major" else value
                W(f"| {disp} | {cnt} | `{spark(by_day)}` |")
            W("")

    details("🚨 Version × cause spikes", joint_body, n_joint)
    details("📮 Cause-level spikes (provider · protocol · AV)", cause_body, n_cause)
    details("📦 Release-adoption version/OS spikes (not incidents)", verdim_body, nv)
    details(f"📈 {label} trends", trends_body, len(TREND_DIMS))

    W("---")
    W(f"\n_Detectors run at daily / weekly / monthly grain; a weekly period is "
      f"included when its week overlaps {label}. Version×cause requires a known "
      f"version, which is only populated from 2026-02 onward; cause-level uses all "
      f"history. Full spike CSVs: "
      f"`PROJECT1/{product}-{{daily,weekly,monthly}}-{{single,version-cause}}-spikes.csv`._")

    os.makedirs(REPORT_DIR.format(product=product), exist_ok=True)
    body = "\n".join(out) + "\n"
    paths = [f"{REPORT_DIR.format(product=product)}/{month}-exec-summary.md"]
    if args.latest:
        paths.append(f"{REPORT_DIR.format(product=product)}/exec-summary-latest.md")
    for p in paths:
        with open(p, "w") as f:
            f.write(body)
        print(f"wrote {p}")
    print(f"=== {month} {product}: {incidents} incident spike(s) "
          f"({n_joint} version×cause, {n_cause} cause-level), "
          f"{nv} release-adoption, {n} questions ===")


if __name__ == "__main__":
    main()
