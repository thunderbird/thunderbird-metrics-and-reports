# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository generates two things from Thunderbird's Mozilla SUMO (Support
Mozilla) data and publishes them as a Jekyll site on GitHub Pages:

1. **Monthly reports** — per-month support-volume and community-activity metrics
   (desktop + android).
2. **Unanswered-questions triage** — twice-daily reports of questions with no
   non-creator answer in 72+ hours, with a Claim/Release self-assignment UI.

Both are regenerated automatically by GitHub Actions and committed to `main`.

## Data Source (important)

The SUMO AAQ API is blocked. Data now comes from a browser-based scraper in a
**separate repo: https://github.com/thunderbird/aaq-scraper** (primary scripts
`scrape_questions.py` / `scrape_answers.py`). It commits **one CSV per product
per day** into its `<year>/` directory, updated hourly:

- `questions-thunderbird-{desktop,android}-YYYY-MM-DD.csv`
- `answers-thunderbird-{desktop,android}-YYYY-MM-DD.csv`

GitHub Actions in this repo check that scraper repo out into `aaq-data/`
(gitignored) and concatenate the per-day files into the monthly inputs under
`CONCATENATED_FILES/`. **Only April 2026 onward uses the scraper**; earlier
reports were built from the old (now-dead) API and are frozen.

Questions CSV columns include: `id, created, updated, locale, product, title,
is_solved, solution, solved_by, is_spam, last_answer, answers, topic, tags,
creator, content, … metadata, num_answers, … operating_system,
thunderbird_version`. Answers: `id, question_id, created, updated, content,
creator, is_spam, num_helpful, num_unhelpful`. Dates are ISO 8601; tags are
semicolon-delimited. `operating_system` / `thunderbird_version` are derived by
the scraper and used by the unanswered-questions triage table.

## Monthly Reports Pipeline

Chained GitHub Actions, all committing to `main`:

1. **Concat** — `sumo-tb-{product}-concat-all-questions-answers` concatenates the
   scraper's per-day files for the current (and previous) month into
   `CONCATENATED_FILES/{DESKTOP,ANDROID}/{YYYY-MM}-sumo-{product}-{questions,answers}.csv`,
   preserving all columns (incl. `operating_system`/`thunderbird_version`) and
   deduping on `id`. (`gha-sumo-tb-{product}-concat-all-questions-answers.yml`,
   4×/day.)
2. **Compute** — `sumo-tb-{product}-create-monthly-csv` reads those concat files
   plus the trusted-contributors list and writes the one-row monthly report
   `REPORTS/{PRODUCT}/{YYYY-MM}-sumo-{product}-report.csv`. Triggered on
   completion of the concat workflow (also runs current + previous month).
3. **Render** — `scripts/generate_reports.py` renders every
   `REPORTS/**/*-sumo-*-report.csv` to markdown in `html_reports/{product}/`,
   converting the semicolon-delimited question IDs to links (titles pulled from
   the matching concat questions file).
4. **Publish** — `gha-tb-update-website.yml` (hourly) runs generate_reports,
   commits, and builds/deploys the Jekyll site.

Report row columns: `num_questions, num_solved, solved-percentage, num_ignored,
ignored-percentage, synthetic_solved_by_random_contributors (+%),
synthetic_solved_by_trusted_contributors (+%), synthetic_solved_rate`, plus
three question-ID buckets by who answered last (creator / trusted / random).
**"Synthetic solved"** is a heuristic — an unsolved question whose last answer is
by someone other than the creator — computed inside
`sumo-tb-{product}-create-monthly-csv`. It is kept unchanged for trend
continuity even though the scraper now provides real `is_solved`/`solved_by`.

## Unanswered-Questions Pipeline

`scripts/sumo-tb-{product}-questions-not-answered-report.py` reads the scraper's
per-day files from `aaq-data/<year>/` over a rolling window (questions created
between `WINDOW_DAYS` = 14 days and `WINDOW_HOURS` = 72 hours ago), filters out
spam, and keeps questions with no answer from a non-creator. It emits
CSV/Markdown/HTML into `UNANSWERED_QUESTIONS/{CSV,MARKDOWN,HTML}_REPORTS/`, plus
`index.html` and `*-latest-*` redirects. Run twice daily by
`gha-sumo-tb-{product}-questions-not-answered-report.yml` (staggered to avoid an
`index.html` race; both check out `aaq-scraper` into `aaq-data/`). The Version
and OS columns come from the scraper's native `thunderbird_version` /
`operating_system` columns, falling back to parsing the legacy `metadata` column
only when a native value is blank.

## Unanswered Questions Self-Assignment

The unanswered-questions reports have an **Assignee** column. Assignments live in
`UNANSWERED_QUESTIONS/desktop-assignments.csv` and `android-assignments.csv`
(schema: `question_id,assignee,assigned_at,assigned_by`).

- **These CSVs are the persistent source of truth.** The report scripts only
  READ them via `load_assignments()` in `scripts/assignments.py`, so the
  twice-daily regeneration never clobbers a manual claim.
- The HTML report's **Claim/Release** buttons WRITE the CSV directly via the
  GitHub API using each user's own fine-grained PAT (stored in browser
  localStorage) — no backend. Concurrency is handled with optimistic locking
  (GET→PUT with SHA, retry on 409). The HTML also has a live client-side
  **filter box** (matches creator/version/OS/title) and a **confirm() on
  Release**.
- `ASSIGNEES` in `scripts/assignments.py` holds the real GitHub usernames
  allowed to claim (`rtanglao`, `lisajill`, `wsmwk`, `monica-thunderbird`,
  `madhattermattic`) — go-live is done, the allowlist is active. The list is
  also injected into the report HTML (`window.TBQ.assignees`) so the Claim
  button can be disabled client-side for signed-in users who aren't on it
  (rather than letting their claim be silently auto-reverted). The column
  renders whatever is in the CSV regardless.
- Because the token lives in localStorage, HTML escaping of SUMO-derived fields
  in `write_html` is security-critical (an escaping bug = token theft).
- **Token validation (`validateToken` in `ASSIGN_JS`):** authenticates via
  `GET /user` and, at set-time, runs `probeWrite()` — a bogus-SHA `PUT` (403 = no
  write → reject; 409/422 = has write → accept). This is the authoritative,
  scope-accurate check. Do **not** reinstate a `GET /user/repos` "single-repo
  scope" guard: every fine-grained PAT carries implicit read-only access to all
  public repos, and `/user/repos` lists the user's affiliations rather than the
  token's selected-repo grant, so it returns many repos even for a correctly
  scoped single-repo token and falsely rejects it (verified empirically
  2026-06). The implicit public-read is read-only and can't be prevented; the
  guarantee that matters — single-repo *write* — is what `probeWrite` confirms.
- **Allowlist enforcement:** `gha-validate-assignments` (push-triggered on the
  two `*-assignments.csv`) runs `scripts/validate_assignments.py`, which removes
  any row whose assignee isn't in `ASSIGNEES`, commits the correction (via
  `GITHUB_TOKEN`, which doesn't re-trigger the workflow), and files an issue
  assigned to rtanglao. **Active** now that `ASSIGNEES` holds real usernames.
- See `UNANSWERED_QUESTIONS/README.md` for the user-facing workflow.

## Data Structure

### CONCATENATED_FILES/
Monthly concatenated CSVs per product (`DESKTOP`/`ANDROID`):
- `{YYYY-MM}-sumo-{product}-questions.csv`
- `{YYYY-MM}-sumo-{product}-answers.csv`

Answers link to questions via the answer's `question_id` → the question's `id`.
All timestamps are treated as UTC for analysis.

### REPORTS/ and html_reports/
`REPORTS/{PRODUCT}/` holds the computed monthly report CSVs;
`html_reports/{product}/` holds the rendered markdown the Jekyll site serves.

### Trusted Contributors
`CONCATENATED_FILES/{PRODUCT}/thunderbird-{product}-trusted-contributors.csv`
(desktop 29, android 3). The monthly report's synthetic-solved computation uses
this list to distinguish trusted vs random contributors.

## Python Environment

This project uses `uv`. Run scripts with `uv run scripts/<name>.py`; CI installs
`requirements.txt` (pandas, matplotlib, anthropic).

## Deprecated scripts

`scripts/` also contains older **exploratory analysis scripts that are obsolete
and unused** — pain-point reports, OAuth/send-receive "by provider" breakdowns,
missing-emails clustering (keyword / manual / LLM), question and Q&A summaries,
keyword/regex plots, and their `compare-*` variants. Only the monthly-report and
unanswered-questions pipelines described above are maintained. Ignore the rest
unless explicitly asked to work on one.

## Important Notes

- CSV field size limits are raised to `sys.maxsize` in the analysis scripts to
  handle large content fields.
- Question titles are truncated to 80 characters for markdown tooltips.
- Keyword/regex matching is case-insensitive by convention (use the `(?i)` flag).
- In markdown, pipe characters (`|`) are replaced with broken bar (`¦`) and
  double quotes (`"`) with U+FF02 (fullwidth quotation mark) to avoid breaking
  table parsing and link tooltips.
- The concat step dedups on `id`; date/time parsing uses UTC throughout.
