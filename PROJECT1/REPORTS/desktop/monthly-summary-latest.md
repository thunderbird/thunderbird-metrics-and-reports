---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **July 2026 is in progress** — data through day 23 of 31. Counts are partial, so the deltas below understate July 2026; treat volume changes as directional until the month closes.

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 533 | ▼ -191 (-26%) |
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
| m:yahooemail | 26 | 17 | ▼ -9 (-35%) |
| proto:imap | 51 | 45 | ▼ -6 (-12%) |
| m:comcast | 14 | 9 | ▼ -5 (-36%) |
| proto:smtp | 25 | 29 | ▲ +4 (+16%) |
| m:gmail | 52 | 48 | ▼ -4 (-8%) |
| m:icloud | 8 | 5 | ▼ -3 |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 201 | ▲ +43 (+27%) |
| v140 | 179 | 140 | ▼ -39 (-22%) |
| v151 | 189 | 4 | ▼ -185 (-98%) |
| v150 | 17 | 23 | ▲ +6 (+35%) |
| v115 | 26 | 12 | ▼ -14 (-54%) |
| v153 | 3 | 18 | ▲ +15 |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 428 | ▼ -161 (-27%) |
| os:linux | 62 | 39 | ▼ -23 (-37%) |
| os:macos | 49 | 37 | ▼ -12 (-24%) |
| os:other | 11 | 9 | ▼ -2 (-18%) |
| os:android | 4 | 6 | ▲ +2 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 135 | ▼ -69 (-34%) |
| customization | 65 | 54 | ▼ -11 (-17%) |
| email-and-messaging | 49 | 61 | ▲ +12 (+24%) |
| passwords-and-sign-in | 32 | 38 | ▲ +6 (+19%) |
| connectivity | 34 | 21 | ▼ -13 (-38%) |
| import-and-export-email | 28 | 20 | ▼ -8 (-29%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-07-25 08:40 UTC_
