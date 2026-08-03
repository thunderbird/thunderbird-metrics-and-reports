---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **August 2026 is in progress** — data through day 3 of 31. Counts are partial, so the deltas below understate August 2026; treat volume changes as directional until the month closes.

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 40 | ▼ -691 (-95%) |
| Version × cause spikes flagged | 0 | 0 | ▬ 0 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 0 | 0 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

_No spikes flagged this month at current thresholds._

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 73 | 1 | ▼ -72 (-99%) |
| proto:imap | 56 | 2 | ▼ -54 (-96%) |
| proto:pop | 42 | 2 | ▼ -40 (-95%) |
| m:microsoftemail | 36 | 3 | ▼ -33 (-92%) |
| proto:smtp | 35 | 2 | ▼ -33 (-94%) |
| m:yahooemail | 30 | 3 | ▼ -27 (-90%) |
| proto:oauth | 20 | 0 | ▼ -20 (-100%) |
| m:comcast | 13 | 2 | ▼ -11 (-85%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v152 | 211 | 1 | ▼ -210 (-100%) |
| v140 | 186 | 2 | ▼ -184 (-99%) |
| v153 | 101 | 25 | ▼ -76 (-75%) |
| v150 | 26 | 1 | ▼ -25 (-96%) |
| v115 | 16 | 1 | ▼ -15 (-94%) |
| v149 | 6 | 0 | ▼ -6 |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 27 | ▼ -562 (-95%) |
| os:linux | 61 | 7 | ▼ -54 (-89%) |
| os:macos | 45 | 2 | ▼ -43 (-96%) |
| os:other | 11 | 1 | ▼ -10 (-91%) |
| os:android | 7 | 1 | ▼ -6 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 9 | ▼ -176 (-95%) |
| email-and-messaging | 82 | 3 | ▼ -79 (-96%) |
| customization | 73 | 6 | ▼ -67 (-92%) |
| passwords-and-sign-in | 53 | 2 | ▼ -51 (-96%) |
| account-management | 28 | 3 | ▼ -25 (-89%) |
| import-and-export-email | 30 | 0 | ▼ -30 (-100%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-08-03 09:06 UTC_
