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

**To explore any bump, not just the ones that fired** — [Interactive spike explorer](PROJECT1/REPORTS/desktop/explorer.html): pick a grain, version and cause, then **click any point on the chart** to read that period's questions. The spike reports below can only link the questions of the periods that cleared a threshold; their sparklines are static text. Each spike row links straight to its own bucket here.

Desktop spike report by time grain:

- [Hourly](PROJECT1/REPORTS/desktop/hourly-spike-report.html) (trailing 7 days)
- [Daily](PROJECT1/REPORTS/desktop/daily-spike-report.html) (trailing 90 days)
- [Weekly](PROJECT1/REPORTS/desktop/weekly-spike-report.html) (trailing 26 weeks) — the mid-duration incident: too diffuse for the daily floor, resolved before a month closes
- [Monthly](PROJECT1/REPORTS/desktop/monthly-spike-report.html) (trailing 24 months)
- [Quarterly](PROJECT1/REPORTS/desktop/quarterly-spike-report.html) (trailing 12 quarters)
- [Yearly](PROJECT1/REPORTS/desktop/yearly-spike-report.html) (all history)

### Back-tests and historical episodes

Known incidents used to check that the detector fires on real events, plus the
one-month pages for past episodes worth a look. Pre-2026-02 months have almost no
version data, so their signal is **cause-level only** (version×cause reads 0 —
that is missing data, not a clean month).

- [Aug 2025 — Bitdefender AV breakage](https://github.com/thunderbird/thunderbird-metrics-and-reports/blob/main/PROJECT1/validation/detector-backtest-bitdefender-2025-08.md) (back-test: caught, day one, all three grains)
- [Aug 2026 — v154 blank-printing regression](https://github.com/thunderbird/thunderbird-metrics-and-reports/blob/main/PROJECT1/validation/detector-backtest-printing-2026-08.md) (back-test: missed until the `feature` dimension existed, then caught on the onset day)
- [Apr 2025 exec summary](PROJECT1/REPORTS/desktop/2025-04-exec-summary.html) — `feat:printing` 24 questions, 3.0× ([vs Mar 2025](PROJECT1/REPORTS/desktop/monthly-summary-2025-04-vs-2025-03.html))
- [Oct 2023 exec summary](PROJECT1/REPORTS/desktop/2023-10-exec-summary.html) — `feat:search` 4.5× and `feat:addons` 4.0×, the Thunderbird 115 "Supernova" fallout ([vs Sep 2023](PROJECT1/REPORTS/desktop/monthly-summary-2023-10-vs-2023-09.html))
- [Spectrum / Charter, from Aug 21 2026](https://github.com/thunderbird/thunderbird-metrics-and-reports/blob/main/PROJECT1/validation/incident-spectrum-2026-08.md) — incident analysis of a **still-open** cluster: 6× baseline, provider-side (cross-provider control test), the third distinct Spectrum episode of 2026
- [Why volume rose in Aug 2026](https://github.com/thunderbird/thunderbird-metrics-and-reports/blob/main/PROJECT1/validation/volume-rise-2026-08-analysis.md) — 731 → 941 questions (+29%), and still climbing in September: what the corpus can and cannot explain

### Android (new, low volume)

Android carries about 40 support questions a month, against detector floors of 8
questions of one kind in a day, 6 in a week and 8 in a month. Nothing has cleared
those floors since 2024, and only 2% of android questions carry a Thunderbird
version, so the page reads "no spike cleared the threshold" rather than "clean".
Read it as a volume and answered-rate page for now. Thresholds tuned for android
are the open question.

- [Android executive summary (last complete month)](PROJECT1/REPORTS/android/exec-summary-latest.html)

## LLM Insights (experimental — AI)

The AI counterpart to Project 1. Claude reads each support question (plus the
creator's own follow-ups, the accepted solution, and trusted-contributor replies),
names the concrete problem, hypothesises a root cause, and rates severity —
surfacing **emerging and worst-served** issues that regex + stats can't. A
prototype for review.

**For engineering** — ranked issues to investigate, each with severity,
resolved-rate, and clickable example questions:

- [Desktop — LLM Insights monthly summary (latest)](LLM_INSIGHTS/REPORTS/desktop/monthly-summary-latest.html)
- [Desktop — LLM Insights monthly summary, plain English](LLM_INSIGHTS/REPORTS/desktop/monthly-summary-latest-plain-english.html) — the same month, same numbers and same ranking, written for a reader outside the team, with the jargon in a collapsed glossary
- [Android — LLM Insights monthly summary (latest)](LLM_INSIGHTS/REPORTS/android/monthly-summary-latest.html)

_(Prototype — feedback welcome.)_
