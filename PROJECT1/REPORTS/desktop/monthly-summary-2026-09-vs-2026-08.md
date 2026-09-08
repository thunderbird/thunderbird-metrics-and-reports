---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 8 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 941 | 272 | ▼ -669 (-71%) |
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
| m:gmail | 75 | 18 | ▼ -57 (-76%) |
| m:microsoftemail | 53 | 7 | ▼ -46 (-87%) |
| proto:imap | 70 | 27 | ▼ -43 (-61%) |
| m:yahooemail | 55 | 13 | ▼ -42 (-76%) |
| proto:pop | 46 | 14 | ▼ -32 (-70%) |
| proto:smtp | 44 | 13 | ▼ -31 (-70%) |
| m:spectrum | 34 | 8 | ▼ -26 (-76%) |
| proto:oauth | 19 | 8 | ▼ -11 (-58%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 39 | ▼ -402 (-91%) |
| v154 | 202 | 38 | ▼ -164 (-81%) |
| v155 | 0 | 100 | ▲ +100 |
| v140 | 67 | 17 | ▼ -50 (-75%) |
| v115 | 24 | 8 | ▼ -16 (-67%) |
| v150 | 25 | 3 | ▼ -22 (-88%) |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 234 | ▼ -516 (-69%) |
| os:linux | 93 | 12 | ▼ -81 (-87%) |
| os:macos | 59 | 14 | ▼ -45 (-76%) |
| os:android | 10 | 2 | ▼ -8 (-80%) |
| os:other | 6 | 4 | ▼ -2 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 91 | ▼ -142 (-61%) |
| email-and-messaging | 80 | 25 | ▼ -55 (-69%) |
| customization | 86 | 15 | ▼ -71 (-83%) |
| passwords-and-sign-in | 60 | 18 | ▼ -42 (-70%) |
| attachments | 49 | 14 | ▼ -35 (-71%) |
| connectivity | 48 | 8 | ▼ -40 (-83%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-08 20:06 UTC_
