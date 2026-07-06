---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 6 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 128 | ▼ -596 (-82%) |
| Version × cause spikes flagged | 3 | 0 | ▼ -3 |
| — of which **new** regressions | 2 | 0 | ▼ -2 |
| Cause-level surges flagged | 0 | 0 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

_No spikes flagged this month at current thresholds._

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| m:microsoftemail | 54 | 7 | ▼ -47 (-87%) |
| proto:imap | 51 | 12 | ▼ -39 (-76%) |
| m:gmail | 52 | 15 | ▼ -37 (-71%) |
| proto:pop | 30 | 9 | ▼ -21 (-70%) |
| proto:smtp | 25 | 4 | ▼ -21 (-84%) |
| m:spectrum | 20 | 1 | ▼ -19 (-95%) |
| m:yahooemail | 26 | 7 | ▼ -19 (-73%) |
| m:comcast | 14 | 2 | ▼ -12 (-86%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 58 | ▼ -100 (-63%) |
| v140 | 179 | 36 | ▼ -143 (-80%) |
| v151 | 189 | 0 | ▼ -189 (-100%) |
| v115 | 26 | 4 | ▼ -22 (-85%) |
| v150 | 17 | 2 | ▼ -15 (-88%) |
| v149 | 11 | 2 | ▼ -9 (-82%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 95 | ▼ -494 (-84%) |
| os:linux | 62 | 12 | ▼ -50 (-81%) |
| os:macos | 49 | 10 | ▼ -39 (-80%) |
| os:other | 11 | 5 | ▼ -6 (-55%) |
| os:android | 4 | 2 | ▼ -2 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 24 | ▼ -180 (-88%) |
| customization | 65 | 15 | ▼ -50 (-77%) |
| email-and-messaging | 49 | 15 | ▼ -34 (-69%) |
| passwords-and-sign-in | 32 | 13 | ▼ -19 (-59%) |
| connectivity | 34 | 4 | ▼ -30 (-88%) |
| import-and-export-email | 28 | 9 | ▼ -19 (-68%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-06 20:38 UTC_
