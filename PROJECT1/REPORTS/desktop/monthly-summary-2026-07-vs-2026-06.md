---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 30 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 680 | ▼ -44 (-6%) |
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
| m:microsoftemail | 54 | 35 | ▼ -19 (-35%) |
| m:spectrum | 20 | 5 | ▼ -15 (-75%) |
| m:gmail | 52 | 66 | ▲ +14 (+27%) |
| proto:pop | 30 | 39 | ▲ +9 (+30%) |
| proto:oauth | 12 | 20 | ▲ +8 (+67%) |
| proto:smtp | 25 | 33 | ▲ +8 (+32%) |
| m:comcast | 14 | 11 | ▼ -3 (-21%) |
| proto:imap | 51 | 54 | ▲ +3 (+6%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 210 | ▲ +52 (+33%) |
| v140 | 179 | 178 | ▼ -1 (-1%) |
| v151 | 189 | 4 | ▼ -185 (-98%) |
| v153 | 3 | 74 | ▲ +71 |
| v150 | 17 | 26 | ▲ +9 (+53%) |
| v115 | 26 | 15 | ▼ -11 (-42%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 544 | ▼ -45 (-8%) |
| os:linux | 62 | 56 | ▼ -6 (-10%) |
| os:macos | 49 | 43 | ▼ -6 (-12%) |
| os:other | 11 | 11 | ▬ 0 (+0%) |
| os:android | 4 | 8 | ▲ +4 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 178 | ▼ -26 (-13%) |
| customization | 65 | 63 | ▼ -2 (-3%) |
| email-and-messaging | 49 | 76 | ▲ +27 (+55%) |
| passwords-and-sign-in | 32 | 51 | ▲ +19 (+59%) |
| connectivity | 34 | 24 | ▼ -10 (-29%) |
| import-and-export-email | 28 | 29 | ▲ +1 (+4%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-30 08:54 UTC_
