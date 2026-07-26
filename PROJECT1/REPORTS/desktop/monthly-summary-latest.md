---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 25 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 567 | ▼ -157 (-22%) |
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
| m:microsoftemail | 54 | 30 | ▼ -24 (-44%) |
| m:spectrum | 20 | 4 | ▼ -16 (-80%) |
| m:yahooemail | 26 | 19 | ▼ -7 (-27%) |
| proto:imap | 51 | 45 | ▼ -6 (-12%) |
| proto:smtp | 25 | 30 | ▲ +5 (+20%) |
| m:comcast | 14 | 9 | ▼ -5 (-36%) |
| proto:pop | 30 | 34 | ▲ +4 (+13%) |
| proto:oauth | 12 | 15 | ▲ +3 (+25%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 203 | ▲ +45 (+28%) |
| v140 | 179 | 151 | ▼ -28 (-16%) |
| v151 | 189 | 4 | ▼ -185 (-98%) |
| v150 | 17 | 23 | ▲ +6 (+35%) |
| v115 | 26 | 12 | ▼ -14 (-54%) |
| v153 | 3 | 29 | ▲ +26 |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 455 | ▼ -134 (-23%) |
| os:linux | 62 | 41 | ▼ -21 (-34%) |
| os:macos | 49 | 39 | ▼ -10 (-20%) |
| os:other | 11 | 10 | ▼ -1 (-9%) |
| os:android | 4 | 7 | ▲ +3 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 144 | ▼ -60 (-29%) |
| customization | 65 | 56 | ▼ -9 (-14%) |
| email-and-messaging | 49 | 68 | ▲ +19 (+39%) |
| passwords-and-sign-in | 32 | 40 | ▲ +8 (+25%) |
| connectivity | 34 | 22 | ▼ -12 (-35%) |
| import-and-export-email | 28 | 22 | ▼ -6 (-21%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-26 20:21 UTC_
