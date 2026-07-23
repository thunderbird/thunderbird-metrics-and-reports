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
| Support questions (load) | 724 | 501 | ▼ -223 (-31%) |
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
| m:microsoftemail | 54 | 29 | ▼ -25 (-46%) |
| m:spectrum | 20 | 4 | ▼ -16 (-80%) |
| proto:imap | 51 | 41 | ▼ -10 (-20%) |
| m:yahooemail | 26 | 17 | ▼ -9 (-35%) |
| m:comcast | 14 | 8 | ▼ -6 (-43%) |
| m:gmail | 52 | 47 | ▼ -5 (-10%) |
| proto:smtp | 25 | 29 | ▲ +4 (+16%) |
| m:icloud | 8 | 5 | ▼ -3 |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 200 | ▲ +42 (+27%) |
| v140 | 179 | 134 | ▼ -45 (-25%) |
| v151 | 189 | 3 | ▼ -186 (-98%) |
| v150 | 17 | 23 | ▲ +6 (+35%) |
| v115 | 26 | 10 | ▼ -16 (-62%) |
| v149 | 11 | 5 | ▼ -6 (-55%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 402 | ▼ -187 (-32%) |
| os:linux | 62 | 34 | ▼ -28 (-45%) |
| os:macos | 49 | 35 | ▼ -14 (-29%) |
| os:other | 11 | 9 | ▼ -2 (-18%) |
| os:android | 4 | 6 | ▲ +2 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 127 | ▼ -77 (-38%) |
| customization | 65 | 49 | ▼ -16 (-25%) |
| email-and-messaging | 49 | 59 | ▲ +10 (+20%) |
| passwords-and-sign-in | 32 | 38 | ▲ +6 (+19%) |
| connectivity | 34 | 21 | ▼ -13 (-38%) |
| import-and-export-email | 28 | 19 | ▼ -9 (-32%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-23 20:23 UTC_
