---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 20 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 422 | ▼ -302 (-42%) |
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
| m:microsoftemail | 54 | 24 | ▼ -30 (-56%) |
| m:spectrum | 20 | 4 | ▼ -16 (-80%) |
| proto:imap | 51 | 35 | ▼ -16 (-31%) |
| m:yahooemail | 26 | 16 | ▼ -10 (-38%) |
| m:gmail | 52 | 44 | ▼ -8 (-15%) |
| m:comcast | 14 | 8 | ▼ -6 (-43%) |
| proto:smtp | 25 | 21 | ▼ -4 (-16%) |
| m:icloud | 8 | 5 | ▼ -3 |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 176 | ▲ +18 (+11%) |
| v140 | 179 | 112 | ▼ -67 (-37%) |
| v151 | 189 | 1 | ▼ -188 (-99%) |
| v115 | 26 | 10 | ▼ -16 (-62%) |
| v150 | 17 | 17 | ▬ 0 (+0%) |
| v149 | 11 | 5 | ▼ -6 (-55%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 335 | ▼ -254 (-43%) |
| os:linux | 62 | 29 | ▼ -33 (-53%) |
| os:macos | 49 | 32 | ▼ -17 (-35%) |
| os:other | 11 | 8 | ▼ -3 (-27%) |
| os:android | 4 | 6 | ▲ +2 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 99 | ▼ -105 (-51%) |
| customization | 65 | 43 | ▼ -22 (-34%) |
| email-and-messaging | 49 | 53 | ▲ +4 (+8%) |
| passwords-and-sign-in | 32 | 33 | ▲ +1 (+3%) |
| connectivity | 34 | 16 | ▼ -18 (-53%) |
| import-and-export-email | 28 | 16 | ▼ -12 (-43%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-20 20:29 UTC_
