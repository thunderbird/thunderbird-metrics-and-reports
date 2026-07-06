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
| Support questions (load) | 724 | 116 | ▼ -608 (-84%) |
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
| proto:imap | 51 | 10 | ▼ -41 (-80%) |
| m:gmail | 52 | 15 | ▼ -37 (-71%) |
| proto:pop | 30 | 8 | ▼ -22 (-73%) |
| proto:smtp | 25 | 4 | ▼ -21 (-84%) |
| m:yahooemail | 26 | 7 | ▼ -19 (-73%) |
| m:spectrum | 20 | 1 | ▼ -19 (-95%) |
| m:comcast | 14 | 2 | ▼ -12 (-86%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v140 | 179 | 34 | ▼ -145 (-81%) |
| v152 | 158 | 53 | ▼ -105 (-66%) |
| v151 | 189 | 0 | ▼ -189 (-100%) |
| v115 | 26 | 3 | ▼ -23 (-88%) |
| v150 | 17 | 2 | ▼ -15 (-88%) |
| v149 | 11 | 2 | ▼ -9 (-82%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 87 | ▼ -502 (-85%) |
| os:linux | 62 | 12 | ▼ -50 (-81%) |
| os:macos | 49 | 8 | ▼ -41 (-84%) |
| os:other | 11 | 5 | ▼ -6 (-55%) |
| os:android | 4 | 2 | ▼ -2 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 19 | ▼ -185 (-91%) |
| customization | 65 | 13 | ▼ -52 (-80%) |
| email-and-messaging | 49 | 14 | ▼ -35 (-71%) |
| passwords-and-sign-in | 32 | 13 | ▼ -19 (-59%) |
| connectivity | 34 | 4 | ▼ -30 (-88%) |
| junk-mail-and-spam | 29 | 7 | ▼ -22 (-76%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-06 09:20 UTC_
