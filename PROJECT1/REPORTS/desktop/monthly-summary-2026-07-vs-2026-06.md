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
| Support questions (load) | 724 | 201 | ▼ -523 (-72%) |
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
| m:microsoftemail | 54 | 9 | ▼ -45 (-83%) |
| proto:imap | 51 | 17 | ▼ -34 (-67%) |
| m:gmail | 52 | 22 | ▼ -30 (-58%) |
| m:spectrum | 20 | 2 | ▼ -18 (-90%) |
| m:yahooemail | 26 | 10 | ▼ -16 (-62%) |
| proto:smtp | 25 | 10 | ▼ -15 (-60%) |
| proto:pop | 30 | 16 | ▼ -14 (-47%) |
| m:comcast | 14 | 3 | ▼ -11 (-79%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 92 | ▼ -66 (-42%) |
| v140 | 179 | 56 | ▼ -123 (-69%) |
| v151 | 189 | 0 | ▼ -189 (-100%) |
| v115 | 26 | 4 | ▼ -22 (-85%) |
| v150 | 17 | 6 | ▼ -11 (-65%) |
| v149 | 11 | 2 | ▼ -9 (-82%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 155 | ▼ -434 (-74%) |
| os:linux | 62 | 17 | ▼ -45 (-73%) |
| os:macos | 49 | 17 | ▼ -32 (-65%) |
| os:other | 11 | 5 | ▼ -6 (-55%) |
| os:android | 4 | 3 | ▼ -1 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 38 | ▼ -166 (-81%) |
| customization | 65 | 24 | ▼ -41 (-63%) |
| email-and-messaging | 49 | 25 | ▼ -24 (-49%) |
| passwords-and-sign-in | 32 | 18 | ▼ -14 (-44%) |
| connectivity | 34 | 7 | ▼ -27 (-79%) |
| import-and-export-email | 28 | 11 | ▼ -17 (-61%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-09 09:06 UTC_
