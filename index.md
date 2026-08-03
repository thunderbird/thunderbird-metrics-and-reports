---
layout: page
title: Thunderbird Support Metrics
---

## Unanswered Questions

Updated twice daily:

- [Latest Desktop Report](UNANSWERED_QUESTIONS/HTML_REPORTS/desktop-latest-unanswered-questions.html)
- [Latest Android Report](UNANSWERED_QUESTIONS/HTML_REPORTS/android-latest-unanswered-questions.html)
- [Full report history](UNANSWERED_QUESTIONS/)

[Monthly reports archive](reports.html)

## Spike Reports (Project 1 — experimental)

Engineering-focused spike detection (no AI; regex + traditional stats) over the
full scraper history (2023-01+). Two signals per report: **version × cause**
(release regressions, 2026-02+ when the native version field became populated) and
**cause-level** (provider/ISP/protocol/AV outages regardless of version — e.g. the
March 2026 GMX incident). Spikes are detected at multiple grains so slow-burn
incidents that a daily threshold misses surface at the monthly report.

**Start here** — [Executive summary (last complete month)](PROJECT1/REPORTS/desktop/exec-summary-latest.html): was last month clean? A single verdict and a detector × grain count table, with all the month's detail collapsed underneath. Regenerated daily, because a closed month's verdict keeps moving as later questions shift the baselines. (Bookmark this.)

**For engineering management** — [Monthly summary (current vs previous month)](PROJECT1/REPORTS/desktop/monthly-summary-latest.html): incidents to investigate, moving cause clusters, and release adoption, month over month. (Bookmark this — it always points to the latest complete comparison.)

Desktop spike report by time grain:

- [Hourly](PROJECT1/REPORTS/desktop/hourly-spike-report.html) (trailing 7 days)
- [Daily](PROJECT1/REPORTS/desktop/daily-spike-report.html) (trailing 90 days)
- [Weekly](PROJECT1/REPORTS/desktop/weekly-spike-report.html) (trailing 26 weeks) — the mid-duration incident: too diffuse for the daily floor, resolved before a month closes
- [Monthly](PROJECT1/REPORTS/desktop/monthly-spike-report.html) (trailing 24 months)
- [Quarterly](PROJECT1/REPORTS/desktop/quarterly-spike-report.html) (trailing 12 quarters)
- [Yearly](PROJECT1/REPORTS/desktop/yearly-spike-report.html) (all history)

## LLM Insights (experimental — AI)

The AI counterpart to Project 1. Claude reads each support question (plus the
creator's own follow-ups, the accepted solution, and trusted-contributor replies),
names the concrete problem, hypothesises a root cause, and rates severity —
surfacing **emerging and worst-served** issues that regex + stats can't. A
prototype for review.

**For engineering** — ranked issues to investigate, each with severity,
resolved-rate, and clickable example questions:

- [Desktop — LLM Insights monthly summary (latest)](LLM_INSIGHTS/REPORTS/desktop/monthly-summary-latest.html)
- [Android — LLM Insights monthly summary (latest)](LLM_INSIGHTS/REPORTS/android/monthly-summary-latest.html)

_(Prototype — feedback welcome.)_
