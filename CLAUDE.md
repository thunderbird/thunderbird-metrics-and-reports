# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository generates the following from Thunderbird's Mozilla SUMO (Support
Mozilla) data and publishes them as a Jekyll site on GitHub Pages:

1. **Monthly reports** — per-month support-volume and community-activity metrics
   (desktop + android).
2. **Unanswered-questions triage** — twice-daily reports of questions with no
   non-creator answer in 72+ hours, with a Claim/Release self-assignment UI.
3. **Project 1 — version × cause spike detector** (no-AI; experimental, desktop
   only so far). See the "Project 1" section below. Generated **manually** for
   now (not yet wired into a GitHub Action).

#1 and #2 are regenerated automatically by GitHub Actions and committed to `main`.

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

## Project 1 — Version × Cause Spike Detector (no-AI)

**Status:** experimental, desktop only. Parent tracking issue **#65** — do all
future Project 1 work as **sub-issues of #65**. Generated **manually** for now
(no GitHub Action yet). Reuses the same aaq-scraper `CONCATENATED_FILES/` monthly
CSVs as the other pipelines; all outputs go under `PROJECT1/`.

**Goal / the one decision it drives:** surface to Thunderbird *engineering*
(audience priority #1) the support-question spikes worth investigating *right
now*. A spike is actionable only when it is **cause-clustered** (mail provider /
ISP / protocol / AV) **and version-correlated**, rises a real margin above
baseline, and links to **clickable example questions**. Sentiment +
first-answer-time are amplifiers, not the headline. **OS is a secondary filter,
not a primary cause.** No AI/LLM — regex dictionaries + traditional stats only.

**Pipeline** (`scripts/project1_*.py`, run in order):

1. `project1_extract_features.py {YYYY-MM} {desktop|android}` → per-question
   feature table `PROJECT1/{month}-{product}-features.csv`. Native
   `operating_system`/`thunderbird_version` (regex fallback) + regex
   provider/isp/protocol/av over title+content; drops spam. Run **per month**.
2. `project1_spike_detect.py {product}` → single-dimension daily spikes
   `PROJECT1/{product}-daily-spikes.csv` vs a trailing-median baseline. (Bare
   version spikes ≈ release-adoption noise — hence the joint detector.)
3. `project1_joint_spike_detect.py {product}` → **headline** version×cause spikes
   `PROJECT1/{product}-version-cause-spikes.csv`, ranked by **lift = observed /
   (version_volume_that_day × cause_overall_rate)** so release adoption cancels
   out and only genuine over-representation survives. Flags `observed>=4 &
   lift>=3x`. Validated on `v151 × isp:spectrum` cert errors (~13×).
4. `project1_report.py {product} [--grain daily] [--window N]` → long-format
   rollup `PROJECT1/{product}-{grain}-rollup.csv` + Jekyll page
   `PROJECT1/REPORTS/{product}/{grain}-spike-report.md` (Unicode-block
   sparklines, clickable question IDs). Grain-agnostic (`GRAINS`); daily is live,
   others arrive post-backfill. Per-grain trailing `WINDOW_DEFAULTS`; `--window 0`
   = all history. Linked from `index.md`.

`scripts/project1_regexes.py` holds the detection dictionaries — ported from
`thunderbird/github-action-thunderbird-aaq/regexes.rb` (the `os:`/`av:`/`m:` tag
convention) plus net-new `proto:` and `isp:` dimensions and regional providers
(GMX, Telus). Both spike CSVs carry a `question_ids` column (ALL ids) for manual
checking.

**Locked decisions:** provider and ISP are SEPARATE dimensions (overlap allowed);
AV stays at 14 vendors (defer expansion to ~25); multi-tag questions count toward
each value; OS is a filter not a cause; thresholds calibrate AFTER backfill;
sparklines are Unicode blocks (can swap to SVG later).

**Data caveats (critical):**
- Native version/OS columns were added by Kitsune **PR #7443 on 2026-04-23**, so
  the **2026-04 monthly concat has no `thunderbird_version` column** →
  version×cause covers **May 2026 onward** until backfill re-runs Apr 23–30.
  Single-dimension spikes and trends still use all of April.
- The `created` column has **mixed formats** across months (old-API
  `2026-03-31 17:30:43 -0700` vs scraper ISO `...Z`). Any **cross-month**
  timestamp parse MUST use `pd.to_datetime(..., format="mixed", utc=True)` or
  May/June rows silently become `NaT`. (The detectors are safe — they group on
  the already-normalized `created_date` string, not the raw timestamp.)
- `tb_version_major` keeps only `\b1\d\d\b` (100–199) found anywhere in the
  string — recovers "Version 150.0.2" forms, rejects junk (333333) and EOL/typo
  majors (91/78/18/10). ~15% of questions have no usable version
  (`unknown`/`latest`/`I don't know`).
- Kramdown (GitHub Pages) needs a **blank line before every table block** — the
  report generator emits one. There is no local `jekyll-feed` gem, so verify the
  page renders with `ruby -e 'require "kramdown"...'` rather than `jekyll build`.

**Resume after backfill (~2026-06-29):** add hourly/monthly/quarterly/yearly
grains (machinery already in `project1_report.py`; just needs history) +
recalibrate the spike thresholds on the wider baselines; then Bucket 4 (sentiment
amplifier, traditional NLP), wire Project 1 into a GitHub Action, and port to
android (desktop-first, same code). Each is a sub-issue of #65.

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
