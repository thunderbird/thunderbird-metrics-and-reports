---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 3 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 941 | 112 | ▼ -829 (-88%) |
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
| m:yahooemail | 55 | 2 | ▼ -53 (-96%) |
| m:microsoftemail | 53 | 5 | ▼ -48 (-91%) |
| proto:pop | 46 | 4 | ▼ -42 (-91%) |
| proto:smtp | 44 | 6 | ▼ -38 (-86%) |
| m:spectrum | 34 | 4 | ▼ -30 (-88%) |
| proto:oauth | 19 | 2 | ▼ -17 (-89%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 17 | ▼ -424 (-96%) |
| v154 | 202 | 26 | ▼ -176 (-87%) |
| v140 | 67 | 10 | ▼ -57 (-85%) |
| v155 | 0 | 28 | ▲ +28 |
| v150 | 25 | 0 | ▼ -25 (-100%) |
| v115 | 24 | 0 | ▼ -24 (-100%) |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 97 | ▼ -653 (-87%) |
| os:linux | 93 | 3 | ▼ -90 (-97%) |
| os:macos | 59 | 4 | ▼ -55 (-93%) |
| os:android | 10 | 2 | ▼ -8 (-80%) |
| os:other | 6 | 3 | ▼ -3 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 36 | ▼ -197 (-85%) |
| email-and-messaging | 80 | 10 | ▼ -70 (-88%) |
| customization | 86 | 4 | ▼ -82 (-95%) |
| passwords-and-sign-in | 60 | 7 | ▼ -53 (-88%) |
| attachments | 49 | 10 | ▼ -39 (-80%) |
| connectivity | 48 | 4 | ▼ -44 (-92%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-03 20:07 UTC_
