---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 14 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 323 | ▼ -401 (-55%) |
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
| proto:imap | 51 | 25 | ▼ -26 (-51%) |
| m:gmail | 52 | 33 | ▼ -19 (-37%) |
| m:spectrum | 20 | 3 | ▼ -17 (-85%) |
| m:yahooemail | 26 | 14 | ▼ -12 (-46%) |
| m:comcast | 14 | 5 | ▼ -9 (-64%) |
| proto:pop | 30 | 21 | ▼ -9 (-30%) |
| proto:smtp | 25 | 17 | ▼ -8 (-32%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 142 | ▼ -16 (-10%) |
| v140 | 179 | 84 | ▼ -95 (-53%) |
| v151 | 189 | 1 | ▼ -188 (-99%) |
| v115 | 26 | 7 | ▼ -19 (-73%) |
| v150 | 17 | 12 | ▼ -5 (-29%) |
| v149 | 11 | 3 | ▼ -8 (-73%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 258 | ▼ -331 (-56%) |
| os:linux | 62 | 21 | ▼ -41 (-66%) |
| os:macos | 49 | 25 | ▼ -24 (-49%) |
| os:other | 11 | 7 | ▼ -4 (-36%) |
| os:android | 4 | 6 | ▲ +2 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 67 | ▼ -137 (-67%) |
| customization | 65 | 36 | ▼ -29 (-45%) |
| email-and-messaging | 49 | 44 | ▼ -5 (-10%) |
| passwords-and-sign-in | 32 | 27 | ▼ -5 (-16%) |
| connectivity | 34 | 14 | ▼ -20 (-59%) |
| import-and-export-email | 28 | 14 | ▼ -14 (-50%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-15 08:46 UTC_
