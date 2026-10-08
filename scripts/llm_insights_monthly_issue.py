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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--month", help="YYYY-MM to report on (default: the month "
                    "that just closed)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--title-prefix", default="",
                    help="prepended to the title, for a test run")
    args = ap.parse_args()

    cur = args.month or month_before(date.today().strftime("%Y-%m"))
    prev = month_before(cur)
    title = (f"{args.title_prefix}LLM Insights: generate the {human(cur)} "
             f"desktop and android reports")

    inputs, rows, notes = [], [], []
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
    rows.append(f"| Total | | about ${total['expected']:.2f} | about ${total['high']:.2f} |")
    over = total["high"] > COST_CEILING_USD

    body = f"""This issue tracks the {human(cur)} LLM Insights reports for desktop and android. Each report compares {human(cur)} with {human(prev)}. The workflow `gha-llm-insights-cost-preview.yml` opened it on {date.today():%Y-%m-%d} and spent nothing.

### Non-AI inputs

| Input | State |
|:--|:--|
{chr(10).join(inputs)}

The scheduled workflows refresh the concat files, the Project 1 feature tables and the spike CSVs. Make sure that the spike workflow ran after the month closed, because `split_by_cause()` reads the spike CSVs.

### Cost estimate

| Stage | Questions | Expected | High |
|:--|--:|--:|--:|
{chr(10).join(rows)}

{"The high estimate is OVER the $" + f"{COST_CEILING_USD:.0f}" + " per-run ceiling. Do not approve it as is." if over else "All figures are under the $" + f"{COST_CEILING_USD:.0f}" + " per-run ceiling."} The estimate comes from text length, not from the exact token count. In September 2026 it read $5.80 for desktop, against $6.17 actually spent. Stage 2 uses the measured cost of earlier runs.
{chr(10).join(chr(10) + n for n in notes)}

### Checklist, in order

1. [ ] Approve the spend above.
2. [ ] Classify {cur} for both products: `uv run scripts/llm_insights_classify.py {cur} --product desktop`, then the same with `--product android`.
3. [ ] Make sure that every {cur} question has a label.
4. [ ] Generate both reports: `uv run scripts/llm_insights_mom_report.py {cur} {prev} desktop --latest`, then the same for `android`.
5. [ ] Read the "spiking cause has no cluster" warnings in the run output, if any.
6. [ ] Review `LLM_INSIGHTS/known-status.csv`. Add any fix or provider outcome from {human(cur)}.
7. [ ] Run `scripts/check_report_render.py` on both pages.
8. [ ] Log the actual cost in `LLM_INSIGHTS/COSTS.md`, commit, and deploy the website.
9. [ ] Read both live pages and close this issue.
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
