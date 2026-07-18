---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 15 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 347 | ▼ -377 (-52%) |
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
| m:microsoftemail | 54 | 21 | ▼ -33 (-61%) |
| proto:imap | 51 | 28 | ▼ -23 (-45%) |
| m:spectrum | 20 | 3 | ▼ -17 (-85%) |
| m:gmail | 52 | 35 | ▼ -17 (-33%) |
| m:yahooemail | 26 | 14 | ▼ -12 (-46%) |
| proto:pop | 30 | 22 | ▼ -8 (-27%) |
| m:comcast | 14 | 7 | ▼ -7 (-50%) |
| proto:smtp | 25 | 19 | ▼ -6 (-24%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 153 | ▼ -5 (-3%) |
| v140 | 179 | 91 | ▼ -88 (-49%) |
| v151 | 189 | 1 | ▼ -188 (-99%) |
| v115 | 26 | 8 | ▼ -18 (-69%) |
| v150 | 17 | 12 | ▼ -5 (-29%) |
| v149 | 11 | 3 | ▼ -8 (-73%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 277 | ▼ -312 (-53%) |
| os:linux | 62 | 22 | ▼ -40 (-65%) |
| os:macos | 49 | 28 | ▼ -21 (-43%) |
| os:other | 11 | 7 | ▼ -4 (-36%) |
| os:android | 4 | 6 | ▲ +2 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 76 | ▼ -128 (-63%) |
| customization | 65 | 37 | ▼ -28 (-43%) |
| email-and-messaging | 49 | 45 | ▼ -4 (-8%) |
| passwords-and-sign-in | 32 | 29 | ▼ -3 (-9%) |
| connectivity | 34 | 14 | ▼ -20 (-59%) |
| import-and-export-email | 28 | 15 | ▼ -13 (-46%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-18 08:33 UTC_
