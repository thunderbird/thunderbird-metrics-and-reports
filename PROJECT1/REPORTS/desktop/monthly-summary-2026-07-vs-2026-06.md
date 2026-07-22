---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 22 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 484 | ▼ -240 (-33%) |
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
| m:microsoftemail | 54 | 27 | ▼ -27 (-50%) |
| m:spectrum | 20 | 4 | ▼ -16 (-80%) |
| proto:imap | 51 | 39 | ▼ -12 (-24%) |
| m:yahooemail | 26 | 17 | ▼ -9 (-35%) |
| m:gmail | 52 | 44 | ▼ -8 (-15%) |
| m:comcast | 14 | 8 | ▼ -6 (-43%) |
| m:icloud | 8 | 5 | ▼ -3 |
| proto:oauth | 12 | 14 | ▲ +2 (+17%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 197 | ▲ +39 (+25%) |
| v140 | 179 | 130 | ▼ -49 (-27%) |
| v151 | 189 | 3 | ▼ -186 (-98%) |
| v150 | 17 | 23 | ▲ +6 (+35%) |
| v115 | 26 | 10 | ▼ -16 (-62%) |
| v149 | 11 | 5 | ▼ -6 (-55%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 388 | ▼ -201 (-34%) |
| os:linux | 62 | 31 | ▼ -31 (-50%) |
| os:macos | 49 | 35 | ▼ -14 (-29%) |
| os:other | 11 | 8 | ▼ -3 (-27%) |
| os:android | 4 | 6 | ▲ +2 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 123 | ▼ -81 (-40%) |
| customization | 65 | 49 | ▼ -16 (-25%) |
| email-and-messaging | 49 | 56 | ▲ +7 (+14%) |
| passwords-and-sign-in | 32 | 33 | ▲ +1 (+3%) |
| connectivity | 34 | 18 | ▼ -16 (-47%) |
| import-and-export-email | 28 | 19 | ▼ -9 (-32%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-22 08:52 UTC_
