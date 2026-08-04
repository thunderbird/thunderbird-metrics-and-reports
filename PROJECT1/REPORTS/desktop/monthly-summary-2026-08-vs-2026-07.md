---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **August 2026 is in progress** — data through day 4 of 31. Counts are partial, so the deltas below understate August 2026; treat volume changes as directional until the month closes.

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 72 | ▼ -659 (-90%) |
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
| m:gmail | 73 | 7 | ▼ -66 (-90%) |
| proto:imap | 56 | 6 | ▼ -50 (-89%) |
| proto:pop | 42 | 5 | ▼ -37 (-88%) |
| proto:smtp | 35 | 4 | ▼ -31 (-89%) |
| m:microsoftemail | 36 | 7 | ▼ -29 (-81%) |
| m:yahooemail | 30 | 6 | ▼ -24 (-80%) |
| proto:oauth | 20 | 1 | ▼ -19 (-95%) |
| m:comcast | 13 | 2 | ▼ -11 (-85%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v152 | 211 | 2 | ▼ -209 (-99%) |
| v140 | 186 | 5 | ▼ -181 (-97%) |
| v153 | 101 | 44 | ▼ -57 (-56%) |
| v150 | 26 | 2 | ▼ -24 (-92%) |
| v115 | 16 | 3 | ▼ -13 (-81%) |
| v149 | 6 | 0 | ▼ -6 |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 55 | ▼ -534 (-91%) |
| os:linux | 61 | 10 | ▼ -51 (-84%) |
| os:macos | 45 | 3 | ▼ -42 (-93%) |
| os:other | 11 | 1 | ▼ -10 (-91%) |
| os:android | 7 | 1 | ▼ -6 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 14 | ▼ -171 (-92%) |
| email-and-messaging | 82 | 5 | ▼ -77 (-94%) |
| customization | 73 | 9 | ▼ -64 (-88%) |
| passwords-and-sign-in | 53 | 3 | ▼ -50 (-94%) |
| junk-mail-and-spam | 24 | 10 | ▼ -14 (-58%) |
| account-management | 28 | 5 | ▼ -23 (-82%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-08-04 08:56 UTC_
