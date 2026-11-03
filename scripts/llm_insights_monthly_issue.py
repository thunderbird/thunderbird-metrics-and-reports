#!/usr/bin/env python3
"""Open the monthly LLM Insights cost-approval issue (#88).

Run on the 2nd of each month by gha-llm-insights-cost-preview.yml. It previews
the Stage-1 classification cost for the month that just closed, for desktop and
android, and opens an issue assigned to rtanglao with the estimate and the
ordered checklist from #84. It spends nothing: without ANTHROPIC_API_KEY the
preview estimates tokens from text length (September 2026: $5.80 estimated,
$6.17 spent).

    uv run scripts/llm_insights_monthly_issue.py                 # month that just closed
    uv run scripts/llm_insights_monthly_issue.py --month 2026-09 --dry-run

--dry-run prints the issue body and opens nothing. Without it the script calls
`gh issue create`, unless an open issue with the same title already exists.

The approval box starts checked (#90). The issue text explains the 12-hour rule
and, through LLM_AUTO_RUN_MODE (anything but "live" means dry run), whether the
automatic run will spend.
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from llm_insights_cost import COST_CEILING_USD, preview_map_cost  # noqa: E402

REPO = "thunderbird/thunderbird-metrics-and-reports"
ASSIGNEE = "rtanglao"
# The people who may stop the automatic run by un-checking the approval box (#90).
STOPPERS = ("rtanglao", "lisajill")
AUTO_RUN_WORKFLOW = "gha-llm-insights-auto-run.yml"
PRODUCTS = ("desktop", "android")
CONCAT = "CONCATENATED_FILES/{P}/{m}-sumo-{p}-{kind}.csv"
LABELS = "LLM_INSIGHTS/{m}-{p}-labels.csv"
REPORT = "LLM_INSIGHTS/REPORTS/{p}/monthly-summary-{cur}-vs-{prev}.md"
# Stage 2 (clustering + narrative) is close to fixed per product. Measured:
# desktop $0.64 (Aug 2026) and $0.71 (Sep 2026), android $0.12 and $0.11.
REDUCE = {"desktop": {"expected": 0.75, "high": 1.00},
          "android": {"expected": 0.12, "high": 0.20}}


def month_before(m):
    y, mo = map(int, m.split("-"))
    return f"{y - 1}-12" if mo == 1 else f"{y}-{mo - 1:02d}"


def human(m):
    return date(int(m[:4]), int(m[5:]), 1).strftime("%B %Y")


def auto_run_text(live):
    """The paragraph that explains the 12-hour rule (#90)."""
    stoppers = " or ".join(f"`{s}`" for s in STOPPERS)
    text = (f"The approval box below starts checked. At 0000 UTC on the 3rd, 12 hours "
            f"after the scheduled run opens this issue, `{AUTO_RUN_WORKFLOW}` reads it. "
            f"To stop the run, {stoppers} un-checks the box before then. An un-check "
            f"by any other person also stops the run. The run also stops if the high "
            f"estimate is over the ${COST_CEILING_USD:.0f} ceiling.")
    if live:
        return (text + " If nothing stops it, the workflow classifies both products, "
                "generates both reports, runs the render check, logs the cost in "
                "`LLM_INSIGHTS/COSTS.md`, commits, and comments the actual cost here.")
    return (text + " The repository variable `LLM_AUTO_RUN_MODE` is not `live`, so "
            "this month the workflow does a dry run. It makes sure that the API key "
            "works with the free `count_tokens` endpoint, comments what it would do, "
            "and spends nothing. You start the real run by hand.")


def checklist(live, cur, prev):
    """The ordered checklist. In live mode the workflow does steps 2 to 5."""
    by = "The workflow: " if live else ""
    steps = [
        "[x] Approve the spend above. Un-check this box to stop the run.",
        f"[ ] {by}Classify {cur} for both products: `uv run scripts/llm_insights_classify.py "
        f"{cur} --product desktop`, then the same with `--product android`.",
        f"[ ] {by}Make sure that every {cur} question has a label.",
        f"[ ] {by}Generate both reports: `uv run scripts/llm_insights_mom_report.py "
        f"{cur} {prev} desktop --latest`, then the same for `android`.",
        f"[ ] {by}Run `scripts/check_report_render.py` on both pages.",
        f"[ ] {by}Log the actual cost in `LLM_INSIGHTS/COSTS.md` and commit.",
        "[ ] Read the \"spiking cause has no cluster\" warnings in the run output, if any.",
        f"[ ] Review `LLM_INSIGHTS/known-status.csv`. Add any fix or provider outcome "
        f"from {human(cur)}, then generate the reports again. That rerun is free, "
        f"because both LLM calls are cached.",
        "[ ] Deploy the website, read both live pages, and close this issue.",
    ]
    return "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))


def issue_title(cur, prefix=""):
    return f"{prefix}LLM Insights: generate the {human(cur)} desktop and android reports"


def estimate(cur, prev):
    """Preview the cost of the month's run, for both products. Spends nothing.

    Returns the issue's table rows and notes, the totals, and `plan`: for each
    product, the months that need classifying (the previous month too when it
    has no labels yet). gha-llm-insights-auto-run.yml reuses this (#90).
    """
    inputs, rows, notes, plan = [], [], [], {}
    total = {"expected": 0.0, "high": 0.0}
    for p in PRODUCTS:
        missing = [k for k in ("questions", "answers")
                   if not os.path.exists(CONCAT.format(P=p.upper(), m=cur, p=p, kind=k))]
        if missing:
            sys.exit(f"{cur} {p}: no concat {' or '.join(missing)} file yet. "
                     f"The concat workflow runs four times a day; try later.")
        if os.path.exists(REPORT.format(p=p, cur=cur, prev=prev)):
            notes.append(f"The {p} page for {cur} against {prev} already exists. "
                         f"Generating it again overwrites it.")
        # Classify the previous month too if it has no labels yet.
        months = [cur] + ([] if os.path.exists(LABELS.format(m=prev, p=p)) else [prev])
        for m in months:
            est = preview_map_cost([m], p, enforce=False)
            b = est["bands"]
            rows.append(f"| Classify {p} {m} | {est['questions']} | "
                        f"${b['expected']:.2f} | ${b['high']:.2f} |")
            total["expected"] += b["expected"]
            total["high"] += b["high"]
            if m == cur:
                inputs.append(f"| `{CONCAT.format(P=p.upper(), m=cur, p=p, kind='questions')}` "
                              f"| {est['questions']} questions |")
        if prev in months:
            notes.append(f"{prev} {p} has no labels yet, so the estimate "
                         f"includes classifying it.")
        rows.append(f"| {p.capitalize()} clustering and narrative | | "
                    f"about ${REDUCE[p]['expected']:.2f} | about ${REDUCE[p]['high']:.2f} |")
        total["expected"] += REDUCE[p]["expected"]
        total["high"] += REDUCE[p]["high"]
        plan[p] = months
    rows.append(f"| Total | | about ${total['expected']:.2f} | about ${total['high']:.2f} |")
    return {"inputs": inputs, "rows": rows, "notes": notes, "total": total,
            "plan": plan}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--month", help="YYYY-MM to report on (default: the month "
                    "that just closed)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--title-prefix", default="",
                    help="prepended to the title, for a test run")
    args = ap.parse_args()
    # Anything but "live" means dry-run: the safe default when the variable is unset.
    live = os.getenv("LLM_AUTO_RUN_MODE", "").strip().lower() == "live"

    cur = args.month or month_before(date.today().strftime("%Y-%m"))
    prev = month_before(cur)
    title = issue_title(cur, args.title_prefix)
    est = estimate(cur, prev)
    inputs, rows, notes, total = est["inputs"], est["rows"], est["notes"], est["total"]
    over = total["high"] > COST_CEILING_USD


    body = f"""This issue tracks the {human(cur)} LLM Insights reports for desktop and android. Each report compares {human(cur)} with {human(prev)}. The workflow `gha-llm-insights-cost-preview.yml` opened it on {date.today():%Y-%m-%d} and spent nothing.

### Non-AI inputs

| Input | State |
|:--|:--|
{chr(10).join(inputs)}

The scheduled workflows refresh the concat files, the Spike Detector feature tables and the spike CSVs. Make sure that the spike workflow ran after the month closed, because `split_by_cause()` reads the spike CSVs.

### Cost estimate

| Stage | Questions | Expected | High |
|:--|--:|--:|--:|
{chr(10).join(rows)}

{"The high estimate is OVER the $" + f"{COST_CEILING_USD:.0f}" + " per-run ceiling. Do not approve it as is." if over else "All figures are under the $" + f"{COST_CEILING_USD:.0f}" + " per-run ceiling."} The estimate comes from text length, not from the exact token count. In September 2026 it read $5.80 for desktop, against $6.17 actually spent. Stage 2 uses the measured cost of earlier runs.
{chr(10).join(chr(10) + n for n in notes)}

### Automatic run

{auto_run_text(live)}

### Checklist, in order

{checklist(live, cur, prev)}
"""
    print(body)
    if args.dry_run:
        print(f"(dry run: no issue opened; title would be: {title})")
        return

    open_titles = json.loads(subprocess.run(
        ["gh", "issue", "list", "--repo", REPO, "--state", "open", "--limit", "200",
         "--json", "title"], check=True, capture_output=True, text=True).stdout)
    if any(i["title"] == title for i in open_titles):
        print(f"An open issue is already titled {title!r}; not opening another.")
        return
    url = subprocess.run(
        ["gh", "issue", "create", "--repo", REPO, "--title", title,
         "--assignee", ASSIGNEE, "--body", body],
        check=True, capture_output=True, text=True).stdout.strip()
    print(f"opened {url}")


if __name__ == "__main__":
    main()
