---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 4 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 941 | 132 | ▼ -809 (-86%) |
| Version × cause spikes flagged | 4 | 0 | ▼ -4 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 1 | 0 | ▼ -1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

_No spikes flagged this month at current thresholds._

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 75 | 8 | ▼ -67 (-89%) |
| proto:imap | 70 | 14 | ▼ -56 (-80%) |
| m:yahooemail | 55 | 3 | ▼ -52 (-95%) |
| m:microsoftemail | 53 | 5 | ▼ -48 (-91%) |
| proto:pop | 46 | 4 | ▼ -42 (-91%) |
| proto:smtp | 44 | 6 | ▼ -38 (-86%) |
| m:spectrum | 34 | 5 | ▼ -29 (-85%) |
| proto:oauth | 19 | 2 | ▼ -17 (-89%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 19 | ▼ -422 (-96%) |
| v154 | 202 | 29 | ▼ -173 (-86%) |
| v140 | 67 | 11 | ▼ -56 (-84%) |
| v155 | 0 | 34 | ▲ +34 |
| v115 | 24 | 1 | ▼ -23 (-96%) |
| v150 | 25 | 0 | ▼ -25 (-100%) |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 116 | ▼ -634 (-85%) |
| os:linux | 93 | 3 | ▼ -90 (-97%) |
| os:macos | 59 | 5 | ▼ -54 (-92%) |
| os:android | 10 | 2 | ▼ -8 (-80%) |
| os:other | 6 | 3 | ▼ -3 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 41 | ▼ -192 (-82%) |
| customization | 86 | 5 | ▼ -81 (-94%) |
| email-and-messaging | 80 | 11 | ▼ -69 (-86%) |
| passwords-and-sign-in | 60 | 10 | ▼ -50 (-83%) |
| attachments | 49 | 11 | ▼ -38 (-78%) |
| connectivity | 48 | 4 | ▼ -44 (-92%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-04 08:08 UTC_
