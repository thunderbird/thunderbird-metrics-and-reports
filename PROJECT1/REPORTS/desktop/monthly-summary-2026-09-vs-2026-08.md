---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 9 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 941 | 309 | ▼ -632 (-67%) |
| Version × cause spikes flagged | 4 | 1 | ▼ -3 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 1 | 0 | ▼ -1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-09-07 | v155 × proto:pop | 4 | 4.0× | 75% ans · 5.2h | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 75 | 27 | ▼ -48 (-64%) |
| proto:imap | 71 | 29 | ▼ -42 (-59%) |
| m:yahooemail | 55 | 14 | ▼ -41 (-75%) |
| m:microsoftemail | 53 | 12 | ▼ -41 (-77%) |
| proto:pop | 46 | 15 | ▼ -31 (-67%) |
| proto:smtp | 44 | 15 | ▼ -29 (-66%) |
| m:spectrum | 34 | 9 | ▼ -25 (-74%) |
| proto:oauth | 19 | 9 | ▼ -10 (-53%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 45 | ▼ -396 (-90%) |
| v154 | 202 | 38 | ▼ -164 (-81%) |
| v155 | 0 | 117 | ▲ +117 |
| v140 | 67 | 19 | ▼ -48 (-72%) |
| v115 | 24 | 11 | ▼ -13 (-54%) |
| v150 | 25 | 4 | ▼ -21 (-84%) |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 262 | ▼ -488 (-65%) |
| os:linux | 93 | 16 | ▼ -77 (-83%) |
| os:macos | 59 | 18 | ▼ -41 (-69%) |
| os:android | 10 | 2 | ▼ -8 (-80%) |
| os:other | 6 | 4 | ▼ -2 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 105 | ▼ -128 (-55%) |
| email-and-messaging | 80 | 30 | ▼ -50 (-62%) |
| customization | 86 | 18 | ▼ -68 (-79%) |
| passwords-and-sign-in | 60 | 19 | ▼ -41 (-68%) |
| attachments | 49 | 14 | ▼ -35 (-71%) |
| connectivity | 48 | 9 | ▼ -39 (-81%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-09 20:07 UTC_
