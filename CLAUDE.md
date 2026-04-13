# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains scripts and tools for analyzing Thunderbird support metrics from Mozilla SUMO (Support Mozilla). It processes question and answer data to generate reports, visualizations, and track keyword trends over time.

## Key Scripts

### `scripts/plot-sumo-keyword-count.py`

Main script for keyword/regex analysis of SUMO data. Generates comprehensive reports with visualizations.

**Usage:**
```bash
# One argument mode (compares current vs previous calendar month)
uv run scripts/plot-sumo-keyword-count.py "(?i)oauth"

# Eight argument mode (custom date ranges)
uv run scripts/plot-sumo-keyword-count.py desktop 2026 3 1 2026 3 31 "(?i)oauth"
```

**Outputs 5 files:**
- CSV with daily counts and question IDs
- Markdown table with clickable question links
- Line plot (PNG)
- Daily comparison bar graph (PNG)
- Overall totals bar chart (PNG)

**Important details:**
- Searches both questions (title, content, tags) and answers (content)
- Counts unique question IDs per day (not total regex occurrences)
- Question IDs in markdown use U+FF02 (fullwidth quotation mark) to escape double quotes in tooltips
- Date range adjustments: when comparing months of different lengths, the script adjusts the start date of the comparison period to match lengths

### `scripts/generate_reports.py`

Converts CSV reports to markdown pages with linked question IDs.

**Usage:**
```bash
uv run scripts/generate_reports.py
```

Processes files from `REPORTS/DESKTOP/` and `REPORTS/ANDROID/` directories.

## Data Structure

### CONCATENATED_FILES/
Contains monthly concatenated CSV files from SUMO:
- `YYYY-MM-sumo-{product}-questions.csv` - Question data with fields: id, title, content, tags, created, is_solved, etc.
- `YYYY-MM-sumo-{product}-answers.csv` - Answer data linked to questions by question_id

**Products:** `desktop` or `android`

### REPORTS/
Output directory for generated reports and visualizations, organized by product (DESKTOP/ANDROID).

## Python Environment

This project uses `uv` for Python dependency management. Run Python scripts with:
```bash
uv run scripts/<script-name>.py
```

## Data Analysis Patterns

### Tag Analysis
Tags are semicolon-delimited in the CSV files. Use Miller (`mlr`) for tag counting:
```bash
mlr --csv nest --explode --values --across-records --nested-fs ";" -f tags \
  then filter -x 'is_null($tags) || $tags == ""' \
  then count-distinct -f tags \
  then sort -nr count <input.csv>
```

### Question/Answer Matching
- Questions have an `id` field
- Answers have a `question_id` field that references the question
- Both have `created` timestamps in format: `YYYY-MM-DD HH:MM:SS ±HHMM`
- All dates/times are converted to UTC for analysis

### `scripts/create-pain-point-report.py`

Analyzes SUMO questions and answers to identify top 3 user pain points.

**Usage:**
```bash
# Generate report for specific month
uv run scripts/create-pain-point-report.py desktop 2026 3
```

**Key features:**
- Filters for English-only questions (locale starts with 'en')
- Only includes answers from question creators OR trusted contributors
- Categorizes questions into pain point categories using keyword analysis
- Outputs CSV and markdown reports with top 3 pain points

**Pain point categories:**
1. OAuth/Authentication Issues
2. Cannot Send/Receive Emails
3. Email Account Setup/Configuration
4. Missing Emails or Folders
5. Calendar/Events Issues
6. Performance/Crashes
7. Update/Upgrade Issues

### `scripts/analyze-oauth-by-provider.py`

Breaks down OAuth/Authentication issues by email provider.

**Usage:**
```bash
uv run scripts/analyze-oauth-by-provider.py desktop 2026 3
```

**Provider detection patterns:**
- Microsoft Hosted Email: hotmail, outlook, office365
- Yahoo Hosted Email: yahoo, aol, att.net, sbcglobal
- Gmail/Google: gmail, googlemail, google workspace
- GMX: gmx.com, gmx.de, gmx.net
- And more...

### `scripts/analyze-send-receive-by-provider.py`

Breaks down Cannot Send/Receive Emails issues by email provider.

**Usage:**
```bash
uv run scripts/analyze-send-receive-by-provider.py desktop 2026 3
```

Uses same provider detection patterns as OAuth analysis.

### `scripts/compare-oauth-by-provider.py` and `scripts/compare-send-receive-by-provider.py`

Compare provider breakdowns across two months.

**Usage:**
```bash
uv run scripts/compare-oauth-by-provider.py desktop 2026 2 3
uv run scripts/compare-send-receive-by-provider.py desktop 2026 2 3
```

### `scripts/analyze-missing-emails-subcategories.py`

Breaks down Missing Emails or Folders issues using basic keyword matching.

**Usage:**
```bash
uv run scripts/analyze-missing-emails-subcategories.py desktop 2026 3
```

**Limitation:** Only captures ~20% of questions with specific categories (79.5% remain "Other/Unknown").

### `scripts/analyze-missing-emails-manual-clustering.py`

Breaks down Missing Emails or Folders issues using enhanced rule-based clustering.

**Usage:**
```bash
uv run scripts/analyze-missing-emails-manual-clustering.py desktop 2026 3
```

**Features:**
- Improved coverage: Only 26% uncategorized (vs 79.5% with basic keywords)
- Detects misclassified questions (questions not actually about missing emails/folders)
- 13+ categories including: All Emails Disappeared, Search/Filter Issues, Profile Issues, After Update, etc.

**Recommended approach** for regular missing emails/folders analysis.

### `scripts/analyze-missing-emails-llm-clustering.py`

Breaks down Missing Emails or Folders issues using Claude AI for intelligent categorization.

**Usage:**
```bash
export ANTHROPIC_API_KEY=your_key_here
uv run scripts/analyze-missing-emails-llm-clustering.py desktop 2026 3
```

**Requirements:** ANTHROPIC_API_KEY environment variable

**Best accuracy** but requires API key and has associated costs (~$0.07-0.73 for 73 questions).

### `scripts/compare-missing-emails-enhanced-clustering.py`

Compare Missing Emails or Folders enhanced clustering results across two months.

**Usage:**
```bash
uv run scripts/compare-missing-emails-enhanced-clustering.py desktop 2026 2 3
```

## Key Insights and Patterns

### Android vs Desktop Differences

**OAuth/Authentication Issues:**
- **Desktop:** 306-319 issues/month, providers identified (Gmail 21.6%, Yahoo 17.2%, Microsoft 10%)
- **Android:** 21-24 issues/month, mostly generic (61.9% Other/Unknown in March)
- Pattern: Android users report OAuth issues more generically or with less provider detail

**Cannot Send/Receive Emails:**
- **Desktop:** 117-120 issues/month, 82-85% generic, some providers identified (Microsoft 8.5%, GMX 3.4%)
- **Android:** 6-8 issues/month, 100% generic (no providers identified)
- Pattern: ALL Android send/receive issues lack specific provider mentions

**Volume differences:**
- Desktop has 10-15x more OAuth issues than Android
- Desktop has 15-20x more send/receive issues than Android
- Android questions tend to be less detailed/technical

### Provider-Specific Patterns

**OAuth Issues (Desktop):**
- Gmail/Yahoo dominate OAuth problems (combined ~39%)
- GMX shows significant volatility (2 → 7, +250% Feb to Mar)
- Microsoft relatively stable (~10%)

**Send/Receive Issues (Desktop):**
- Mostly generic issues (82-85%)
- Microsoft leads identifiable providers (8.5%)
- Gmail/Yahoo notably ABSENT (authentication is the main issue, not send/receive)

### Top Pain Points Trending (Android)

**February 2026 top 3:**
1. OAuth/Authentication Issues - 24 questions
2. Cannot Send/Receive Emails - 8 questions
3. Missing Emails or Folders - 6 questions

**March 2026 top 3:**
1. OAuth/Authentication Issues - 21 questions
2. Performance/Crashes - 6 questions
3. Cannot Send/Receive Emails - 6 questions

**Key change:** Performance/Crashes emerged as new top 3 issue in March 2026, replacing Missing Emails or Folders from February's top 3.

### Missing Emails or Folders Clustering (Desktop)

**February vs March 2026 Comparison (Enhanced Rule-Based Clustering):**

**Overall Trend:**
- **February 2026:** 104 questions
- **March 2026:** 73 questions
- **Change:** -31 questions (-29.8% decrease)

**Largest Decreases (Improvements):**
1. Search/Filter/View Issues: 17 → 8 (-52.9%)
2. Profile/Installation Issues: 14 → 7 (-50.0%)
3. Local Folders: 5 → 1 (-80.0%)
4. Junk/Spam Folder: 3 → 0 (-100.0% - completely resolved!)
5. Other/Uncategorized: 25 → 19 (-24.0%)

**Largest Increases (Concerns):**
1. After Update/Upgrade: 1 → 3 (+200.0%)
2. Misclassified (Not Missing Emails/Folders): 10 → 12 (+20.0%)
3. Sent Folder Issues: 3 → 4 (+33.3%)

**Stable Categories:**
- All Emails Disappeared: 3 questions (no change)
- Emails/Folders Disappeared: 9 questions (no change)

**Key Insight:** The overall 29.8% decrease in Missing Emails or Folders issues from February to March is encouraging. The complete elimination of Junk/Spam folder issues and significant drops in Search/Filter and Profile issues suggest improvements in these areas. However, the tripling of "After Update/Upgrade" issues (1→3) may indicate problems introduced in recent Thunderbird updates.

**Clustering Methods Available:**
- Basic keyword matching: 79.5% uncategorized (poor coverage)
- Enhanced rule-based: 26.0% uncategorized (recommended for regular use)
- LLM-based (requires ANTHROPIC_API_KEY): Best accuracy, understands context

### Product-Specific Titles

All markdown reports include product-specific titles:
- Android reports: "Thunderbird for Android ..."
- Desktop reports: "Thunderbird Desktop ..."

## Trusted Contributors

Located in `CONCATENATED_FILES/{PRODUCT}/thunderbird-{product}-trusted-contributors.csv`
- Desktop: 29 trusted contributors
- Android: 3 trusted contributors

Pain point analysis only includes answers from question creators OR trusted contributors to ensure quality.

## Important Notes

- The script `plot-sumo-keyword-count.py` uses `datetime.utcnow()` which is deprecated. This generates a warning but doesn't affect functionality.
- CSV field size limits are increased to `sys.maxsize` in analysis scripts to handle large content fields.
- Question titles are truncated to 80 characters for markdown tooltips.
- When searching for keywords, the match is case-insensitive by default (use `(?i)` flag in regex).
- Pipe characters (|) are replaced with broken bar (¦) in markdown links to avoid table parsing issues.
- Double quotes (") are replaced with U+FF02 (fullwidth quotation mark) in markdown tooltips.
