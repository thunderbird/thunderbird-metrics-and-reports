---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 26 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 594 | ▼ -130 (-18%) |
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
| m:microsoftemail | 54 | 31 | ▼ -23 (-43%) |
| m:spectrum | 20 | 5 | ▼ -15 (-75%) |
| m:gmail | 52 | 60 | ▲ +8 (+15%) |
| proto:smtp | 25 | 31 | ▲ +6 (+24%) |
| m:yahooemail | 26 | 21 | ▼ -5 (-19%) |
| proto:oauth | 12 | 17 | ▲ +5 (+42%) |
| m:comcast | 14 | 10 | ▼ -4 (-29%) |
| proto:pop | 30 | 34 | ▲ +4 (+13%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 205 | ▲ +47 (+30%) |
| v140 | 179 | 159 | ▼ -20 (-11%) |
| v151 | 189 | 4 | ▼ -185 (-98%) |
| v153 | 3 | 44 | ▲ +41 |
| v150 | 17 | 24 | ▲ +7 (+41%) |
| v115 | 26 | 12 | ▼ -14 (-54%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 476 | ▼ -113 (-19%) |
| os:linux | 62 | 47 | ▼ -15 (-24%) |
| os:macos | 49 | 39 | ▼ -10 (-20%) |
| os:other | 11 | 10 | ▼ -1 (-9%) |
| os:android | 4 | 7 | ▲ +3 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 149 | ▼ -55 (-27%) |
| customization | 65 | 57 | ▼ -8 (-12%) |
| email-and-messaging | 49 | 71 | ▲ +22 (+45%) |
| passwords-and-sign-in | 32 | 42 | ▲ +10 (+31%) |
| connectivity | 34 | 22 | ▼ -12 (-35%) |
| import-and-export-email | 28 | 22 | ▼ -6 (-21%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-28 08:55 UTC_
