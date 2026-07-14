---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 13 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 303 | ▼ -421 (-58%) |
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
| m:microsoftemail | 54 | 18 | ▼ -36 (-67%) |
| proto:imap | 51 | 25 | ▼ -26 (-51%) |
| m:gmail | 52 | 31 | ▼ -21 (-40%) |
| m:spectrum | 20 | 3 | ▼ -17 (-85%) |
| m:yahooemail | 26 | 14 | ▼ -12 (-46%) |
| proto:smtp | 25 | 16 | ▼ -9 (-36%) |
| proto:pop | 30 | 21 | ▼ -9 (-30%) |
| m:comcast | 14 | 5 | ▼ -9 (-64%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 130 | ▼ -28 (-18%) |
| v140 | 179 | 80 | ▼ -99 (-55%) |
| v151 | 189 | 1 | ▼ -188 (-99%) |
| v115 | 26 | 7 | ▼ -19 (-73%) |
| v150 | 17 | 12 | ▼ -5 (-29%) |
| v149 | 11 | 3 | ▼ -8 (-73%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 240 | ▼ -349 (-59%) |
| os:linux | 62 | 21 | ▼ -41 (-66%) |
| os:macos | 49 | 24 | ▼ -25 (-51%) |
| os:other | 11 | 6 | ▼ -5 (-45%) |
| os:android | 4 | 6 | ▲ +2 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 61 | ▼ -143 (-70%) |
| customization | 65 | 35 | ▼ -30 (-46%) |
| email-and-messaging | 49 | 41 | ▼ -8 (-16%) |
| passwords-and-sign-in | 32 | 25 | ▼ -7 (-22%) |
| connectivity | 34 | 14 | ▼ -20 (-59%) |
| import-and-export-email | 28 | 14 | ▼ -14 (-50%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-14 08:43 UTC_
