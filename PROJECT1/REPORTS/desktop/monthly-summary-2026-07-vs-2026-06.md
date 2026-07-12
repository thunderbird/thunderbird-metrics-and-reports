---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 9 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 221 | ▼ -503 (-69%) |
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
| m:microsoftemail | 54 | 14 | ▼ -40 (-74%) |
| m:gmail | 52 | 23 | ▼ -29 (-56%) |
| proto:imap | 51 | 22 | ▼ -29 (-57%) |
| m:spectrum | 20 | 2 | ▼ -18 (-90%) |
| m:yahooemail | 26 | 11 | ▼ -15 (-58%) |
| proto:pop | 30 | 18 | ▼ -12 (-40%) |
| proto:smtp | 25 | 14 | ▼ -11 (-44%) |
| m:comcast | 14 | 4 | ▼ -10 (-71%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 100 | ▼ -58 (-37%) |
| v140 | 179 | 63 | ▼ -116 (-65%) |
| v151 | 189 | 0 | ▼ -189 (-100%) |
| v115 | 26 | 6 | ▼ -20 (-77%) |
| v150 | 17 | 8 | ▼ -9 (-53%) |
| v149 | 11 | 2 | ▼ -9 (-82%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 175 | ▼ -414 (-70%) |
| os:linux | 62 | 17 | ▼ -45 (-73%) |
| os:macos | 49 | 17 | ▼ -32 (-65%) |
| os:other | 11 | 5 | ▼ -6 (-55%) |
| os:android | 4 | 3 | ▼ -1 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 46 | ▼ -158 (-77%) |
| customization | 65 | 26 | ▼ -39 (-60%) |
| email-and-messaging | 49 | 25 | ▼ -24 (-49%) |
| passwords-and-sign-in | 32 | 20 | ▼ -12 (-38%) |
| connectivity | 34 | 9 | ▼ -25 (-74%) |
| import-and-export-email | 28 | 12 | ▼ -16 (-57%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-12 20:16 UTC_
