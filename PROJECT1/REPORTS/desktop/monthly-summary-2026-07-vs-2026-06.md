---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 4 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 99 | ▼ -625 (-86%) |
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
| m:microsoftemail | 54 | 6 | ▼ -48 (-89%) |
| proto:imap | 51 | 9 | ▼ -42 (-82%) |
| m:gmail | 52 | 11 | ▼ -41 (-79%) |
| proto:pop | 30 | 4 | ▼ -26 (-87%) |
| m:yahooemail | 26 | 4 | ▼ -22 (-85%) |
| proto:smtp | 25 | 3 | ▼ -22 (-88%) |
| m:spectrum | 20 | 1 | ▼ -19 (-95%) |
| m:comcast | 14 | 2 | ▼ -12 (-86%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 48 | ▼ -110 (-70%) |
| v140 | 179 | 26 | ▼ -153 (-85%) |
| v151 | 189 | 0 | ▼ -189 (-100%) |
| v115 | 26 | 3 | ▼ -23 (-88%) |
| v150 | 17 | 2 | ▼ -15 (-88%) |
| v149 | 11 | 2 | ▼ -9 (-82%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 71 | ▼ -518 (-88%) |
| os:linux | 62 | 12 | ▼ -50 (-81%) |
| os:macos | 49 | 8 | ▼ -41 (-84%) |
| os:other | 11 | 5 | ▼ -6 (-55%) |
| os:android | 4 | 1 | ▼ -3 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 13 | ▼ -191 (-94%) |
| customization | 65 | 13 | ▼ -52 (-80%) |
| email-and-messaging | 49 | 13 | ▼ -36 (-73%) |
| passwords-and-sign-in | 32 | 10 | ▼ -22 (-69%) |
| connectivity | 34 | 4 | ▼ -30 (-88%) |
| import-and-export-email | 28 | 6 | ▼ -22 (-79%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-05 09:01 UTC_
