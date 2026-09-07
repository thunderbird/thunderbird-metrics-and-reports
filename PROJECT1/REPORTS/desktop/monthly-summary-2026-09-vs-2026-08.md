---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 7 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 941 | 239 | ▼ -702 (-75%) |
| Version × cause spikes flagged | 4 | 1 | ▼ -3 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 1 | 0 | ▼ -1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-09-07 | v155 × proto:pop | 4 | 6.5× | 75% ans · 5.2h | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 75 | 15 | ▼ -60 (-80%) |
| m:microsoftemail | 53 | 5 | ▼ -48 (-91%) |
| m:yahooemail | 55 | 10 | ▼ -45 (-82%) |
| proto:imap | 70 | 27 | ▼ -43 (-61%) |
| proto:pop | 46 | 13 | ▼ -33 (-72%) |
| proto:smtp | 44 | 12 | ▼ -32 (-73%) |
| m:spectrum | 34 | 8 | ▼ -26 (-76%) |
| proto:oauth | 19 | 7 | ▼ -12 (-63%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 33 | ▼ -408 (-93%) |
| v154 | 202 | 35 | ▼ -167 (-83%) |
| v155 | 0 | 88 | ▲ +88 |
| v140 | 67 | 16 | ▼ -51 (-76%) |
| v115 | 24 | 6 | ▼ -18 (-75%) |
| v150 | 25 | 3 | ▼ -22 (-88%) |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 209 | ▼ -541 (-72%) |
| os:linux | 93 | 10 | ▼ -83 (-89%) |
| os:macos | 59 | 11 | ▼ -48 (-81%) |
| os:android | 10 | 2 | ▼ -8 (-80%) |
| os:other | 6 | 3 | ▼ -3 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 80 | ▼ -153 (-66%) |
| email-and-messaging | 80 | 22 | ▼ -58 (-72%) |
| customization | 86 | 14 | ▼ -72 (-84%) |
| passwords-and-sign-in | 60 | 17 | ▼ -43 (-72%) |
| attachments | 49 | 14 | ▼ -35 (-71%) |
| connectivity | 48 | 7 | ▼ -41 (-85%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-07 20:06 UTC_
