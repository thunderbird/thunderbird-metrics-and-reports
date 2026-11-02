#!/usr/bin/env python3
"""Decide whether the monthly LLM Insights run goes ahead (#90).

gha-llm-insights-auto-run.yml runs this at 0000 UTC on the 3rd, 12 hours after
gha-llm-insights-cost-preview.yml opens the approval issue. The issue opens
with "1. [x] Approve the spend above." checked. This script reads the issue and
its edit history and stops the run when any of these is true:

- there is no open approval issue for the month;
- a person who may not open it (not the github-actions bot, rtanglao or
  lisajill) opened the issue, because anybody can open an issue on a public repo;
- the approval line is missing, or its box is unchecked (by anybody);
- the box is checked, but the last person who changed it is not rtanglao or
  lisajill (an outsider cannot re-approve a stopped run);
- the issue already carries the "llm-auto-run-started" label;
- the API key does not work (checked with the free count_tokens endpoint);
- the high cost estimate is over the $50 ceiling.

In dry-run mode (the default; LLM_AUTO_RUN_MODE is not "live") the script never
lets the run go ahead. It comments what a live run would do and spends nothing.

    uv run scripts/llm_insights_auto_run.py --issue 92 --no-comment
    uv run scripts/llm_insights_auto_run.py --month 2026-10 --mode dry-run

The decision goes to stdout and, in GitHub Actions, to $GITHUB_OUTPUT
(run=true|false, issue, plan as JSON).
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from llm_insights_cost import COST_CEILING_USD  # noqa: E402
from llm_insights_monthly_issue import (REPO, STOPPERS, estimate, human,  # noqa: E402
                                        issue_title, month_before)

BOT = "github-actions"
STARTED_LABEL = "llm-auto-run-started"
MODEL = "claude-opus-5"
APPROVE_RE = re.compile(r"^1\. \[( |x|X)\] Approve the spend above", re.M)
QUERY = """query($owner: String!, $name: String!, $number: Int!) {
  repository(owner: $owner, name: $name) {
    issue(number: $number) {
      number title state body url
      author { __typename login }
      labels(first: 50) { nodes { name } }
      userContentEdits(first: 100) {
        nodes { editedAt editor { login } diff }
      }
    }
  }
}"""


def gh(*args):
    return subprocess.run(["gh", *args], check=True, capture_output=True,
                          text=True).stdout


def find_issue(title):
    issues = json.loads(gh("issue", "list", "--repo", REPO, "--state", "open",
                           "--limit", "200", "--json", "number,title"))
    return next((i["number"] for i in issues if i["title"] == title), None)


def load_issue(number):
    owner, name = REPO.split("/")
    out = gh("api", "graphql", "-f", f"query={QUERY}", "-f", f"owner={owner}",
             "-f", f"name={name}", "-F", f"number={number}")
    return json.loads(out)["data"]["repository"]["issue"]


def box_state(text):
    """True if checked, False if unchecked, None if the approval line is gone."""
    m = APPROVE_RE.search(text or "")
    return None if m is None else m.group(1).lower() == "x"


def last_changer(issue):
    """Who set the box to its current state: the author, or the last editor
    whose edit flipped it. GitHub lists edits newest first, and the oldest
    entry is the original body (it exists only once the issue was edited)."""
    author = issue["author"]["login"]
    revisions = [(e["editor"]["login"] if e["editor"] else "ghost", e["diff"])
                 for e in reversed(issue["userContentEdits"]["nodes"])]
    if not revisions:
        return author
    changer, state = author, box_state(revisions[0][1])
    for editor, text in revisions[1:]:
        s = box_state(text)
        if s != state:
            changer, state = editor, s
    return changer


def check_key():
    """Make sure that ANTHROPIC_API_KEY works. count_tokens is free."""
    if not os.getenv("ANTHROPIC_API_KEY"):
        return "the `ANTHROPIC_API_KEY` secret is not set"
    try:
        from anthropic import Anthropic
        Anthropic().messages.count_tokens(
            model=MODEL, messages=[{"role": "user", "content": "key check"}])
    except Exception as e:  # noqa: BLE001 - any failure means "do not spend"
        return f"the API key check failed ({type(e).__name__}: {e})"
    return None


def decide(args):
    """Return (go, issue_number, message, plan). go is True only in live mode."""
    cur = args.month or month_before(date.today().strftime("%Y-%m"))
    prev = month_before(cur)
    title = issue_title(cur, args.title_prefix)
    number = args.issue or find_issue(title)
    if number is None:
        return False, None, f"No open issue is titled {title!r}. Nothing to do.", {}
    issue = load_issue(number)
    stop = lambda why: (False, number, f"The automatic run stopped: {why}.", {})  # noqa: E731

    if issue["state"] != "OPEN":
        return stop(f"issue #{number} is closed")
    author = issue["author"]
    if not ((author["__typename"] == "Bot" and author["login"] == BOT)
            or author["login"] in STOPPERS):
        return stop(f"`{author['login']}` opened this issue, and only the "
                    f"scheduled workflow, {' or '.join(STOPPERS)} may open it")
    state = box_state(issue["body"])
    if state is None:
        return stop("the issue has no \"1. [x] Approve the spend above.\" line")
    changer = last_changer(issue)
    if state is False:
        return stop(f"`{changer}` un-checked the approval box")
    if changer not in STOPPERS and changer != author["login"]:
        return stop(f"`{changer}` checked the approval box, and only "
                    f"{' or '.join(STOPPERS)} may approve a run")
    if STARTED_LABEL in {n["name"] for n in issue["labels"]["nodes"]}:
        return stop(f"the issue already has the `{STARTED_LABEL}` label, so a run "
                    f"already started. Remove the label to allow another run")
    bad_key = check_key()
    if bad_key:
        return stop(bad_key)

    if args.estimate == "length":   # quick local tests: no per-question calls
        os.environ.pop("ANTHROPIC_API_KEY", None)
    est = estimate(cur, prev)
    total, plan = est["total"], est["plan"]
    if total["high"] > COST_CEILING_USD:
        return stop(f"the high estimate is ${total['high']:.2f}, over the "
                    f"${COST_CEILING_USD:.0f} ceiling")

    how = ("free `count_tokens` endpoint" if args.estimate == "count_tokens"
           else "text length")
    steps = "\n".join(
        [f"- Classify {p} {m}" for p, ms in plan.items() for m in ms]
        + [f"- Generate the {p} report for {human(cur)} against {human(prev)}"
           for p in plan])
    summary = (f"The approval box is checked (last changed by `{changer}`), the API "
               f"key works, and the estimate is about ${total['expected']:.2f}, "
               f"${total['high']:.2f} at most (counted with the {how}).\n\n{steps}")
    if args.mode != "live":
        return False, number, ("Dry run: a live run would go ahead now and spend about "
                               "the estimate below. This run "
                               "spent nothing.\n\n" + summary + "\n\nTo make the "
                               "next run live, set the repository variable "
                               "`LLM_AUTO_RUN_MODE` to `live`."), plan
    return True, number, "The automatic run starts now.\n\n" + summary, plan


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--month", help="YYYY-MM (default: the month that just closed)")
    ap.add_argument("--issue", type=int, help="read this issue instead of "
                    "finding the approval issue by its title")
    ap.add_argument("--title-prefix", default="", help="for a [TEST] issue")
    ap.add_argument("--mode", choices=["dry-run", "live"],
                    default=("live" if os.getenv("LLM_AUTO_RUN_MODE", "").strip()
                             .lower() == "live" else "dry-run"))
    ap.add_argument("--estimate", choices=["count_tokens", "length"],
                    default="count_tokens")
    ap.add_argument("--no-comment", action="store_true",
                    help="print the comment instead of posting it")
    args = ap.parse_args()

    go, number, message, plan = decide(args)
    print(f"mode: {args.mode}\nissue: {number}\nrun: {str(go).lower()}\n\n{message}")
    if number and not args.no_comment:
        gh("issue", "comment", str(number), "--repo", REPO, "--body", message)
    if os.getenv("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"run={str(go).lower()}\nissue={number or ''}\n"
                    f"plan={json.dumps(plan)}\n")
    # A broken key must turn the run red, so somebody notices before next month.
    if "API key check failed" in message or "secret is not set" in message:
        sys.exit(1)


if __name__ == "__main__":
    main()
