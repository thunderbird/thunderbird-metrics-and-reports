---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 701 | ▼ -23 (-3%) |
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
| m:microsoftemail | 54 | 36 | ▼ -18 (-33%) |
| m:gmail | 52 | 70 | ▲ +18 (+35%) |
| m:spectrum | 20 | 5 | ▼ -15 (-75%) |
| proto:pop | 30 | 40 | ▲ +10 (+33%) |
| proto:smtp | 25 | 34 | ▲ +9 (+36%) |
| proto:oauth | 12 | 20 | ▲ +8 (+67%) |
| proto:imap | 51 | 54 | ▲ +3 (+6%) |
| m:comcast | 14 | 11 | ▼ -3 (-21%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 210 | ▲ +52 (+33%) |
| v140 | 179 | 182 | ▲ +3 (+2%) |
| v151 | 189 | 4 | ▼ -185 (-98%) |
| v153 | 3 | 85 | ▲ +82 |
| v150 | 17 | 26 | ▲ +9 (+53%) |
| v115 | 26 | 15 | ▼ -11 (-42%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 560 | ▼ -29 (-5%) |
| os:linux | 62 | 60 | ▼ -2 (-3%) |
| os:macos | 49 | 44 | ▼ -5 (-10%) |
| os:other | 11 | 11 | ▬ 0 (+0%) |
| os:android | 4 | 8 | ▲ +4 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 182 | ▼ -22 (-11%) |
| customization | 65 | 68 | ▲ +3 (+5%) |
| email-and-messaging | 49 | 78 | ▲ +29 (+59%) |
| passwords-and-sign-in | 32 | 52 | ▲ +20 (+62%) |
| connectivity | 34 | 25 | ▼ -9 (-26%) |
| import-and-export-email | 28 | 29 | ▲ +1 (+4%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-31 09:00 UTC_
