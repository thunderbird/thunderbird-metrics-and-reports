---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 5 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 941 | 174 | ▼ -767 (-82%) |
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
| m:gmail | 75 | 13 | ▼ -62 (-83%) |
| proto:imap | 70 | 16 | ▼ -54 (-77%) |
| m:yahooemail | 55 | 6 | ▼ -49 (-89%) |
| m:microsoftemail | 53 | 5 | ▼ -48 (-91%) |
| proto:pop | 46 | 6 | ▼ -40 (-87%) |
| proto:smtp | 44 | 9 | ▼ -35 (-80%) |
| m:spectrum | 34 | 6 | ▼ -28 (-82%) |
| proto:oauth | 19 | 6 | ▼ -13 (-68%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 24 | ▼ -417 (-95%) |
| v154 | 202 | 33 | ▼ -169 (-84%) |
| v140 | 67 | 13 | ▼ -54 (-81%) |
| v155 | 0 | 59 | ▲ +59 |
| v150 | 25 | 2 | ▼ -23 (-92%) |
| v115 | 24 | 1 | ▼ -23 (-96%) |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 150 | ▼ -600 (-80%) |
| os:linux | 93 | 9 | ▼ -84 (-90%) |
| os:macos | 59 | 7 | ▼ -52 (-88%) |
| os:android | 10 | 2 | ▼ -8 (-80%) |
| os:other | 6 | 3 | ▼ -3 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 55 | ▼ -178 (-76%) |
| email-and-messaging | 80 | 19 | ▼ -61 (-76%) |
| customization | 86 | 7 | ▼ -79 (-92%) |
| passwords-and-sign-in | 60 | 12 | ▼ -48 (-80%) |
| attachments | 49 | 13 | ▼ -36 (-73%) |
| connectivity | 48 | 4 | ▼ -44 (-92%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-05 20:06 UTC_
