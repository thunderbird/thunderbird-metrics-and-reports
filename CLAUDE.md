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

## Important Notes

- The script `plot-sumo-keyword-count.py` uses `datetime.utcnow()` which is deprecated. This generates a warning but doesn't affect functionality.
- CSV field size limits are increased to `sys.maxsize` in `generate_reports.py` to handle large content fields.
- Question titles are truncated to 80 characters for markdown tooltips.
- When searching for keywords, the match is case-insensitive by default (use `(?i)` flag in regex).
