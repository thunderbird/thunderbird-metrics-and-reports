---
layout: base
title: Desktop Engineering Support Summary — November 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## November 2026 vs October 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **November 2026 is in progress** — data through day 1 of 30. Counts are partial, so the deltas below understate November 2026; treat volume changes as directional until the month closes.

## Headline

| | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 1030 | 11 | ▼ -1019 (-99%) |
| Version × cause spikes flagged | 15 | 0 | ▼ -15 |
| — of which **new** regressions | 2 | 0 | ▼ -2 |
| Cause-level surges flagged | 3 | 0 | ▼ -3 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

_No spikes flagged this month at current thresholds._

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| feat:attachments | 106 | 0 | ▼ -106 (-100%) |
| m:gmail | 96 | 1 | ▼ -95 (-99%) |
| proto:imap | 82 | 1 | ▼ -81 (-99%) |
| m:microsoftemail | 60 | 1 | ▼ -59 (-98%) |
| proto:pop | 55 | 0 | ▼ -55 (-100%) |
| m:yahooemail | 52 | 0 | ▼ -52 (-100%) |
| proto:smtp | 36 | 1 | ▼ -35 (-97%) |
| feat:calendar | 34 | 3 | ▼ -31 (-91%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in November 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| v157 | 262 | 0 | ▼ -262 (-100%) |
| v153 | 251 | 1 | ▼ -250 (-100%) |
| v158 | 169 | 1 | ▼ -168 (-99%) |
| v159 | 48 | 3 | ▼ -45 (-94%) |
| v140 | 43 | 1 | ▼ -42 (-98%) |
| v115 | 19 | 0 | ▼ -19 (-100%) |

### Operating-system mix

| Operating-system mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 848 | 7 | ▼ -841 (-99%) |
| os:linux | 83 | 2 | ▼ -81 (-98%) |
| os:macos | 66 | 2 | ▼ -64 (-97%) |
| os:other | 9 | 0 | ▼ -9 |
| os:android | 8 | 0 | ▼ -8 |

### Topic mix

| Topic mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 246 | 1 | ▼ -245 (-100%) |
| attachments | 183 | 1 | ▼ -182 (-99%) |
| customization | 90 | 1 | ▼ -89 (-99%) |
| email-and-messaging | 88 | 1 | ▼ -87 (-99%) |
| passwords-and-sign-in | 46 | 0 | ▼ -46 (-100%) |
| connectivity | 39 | 1 | ▼ -38 (-97%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · November 2026 vs October 2026._

_Last updated: 2026-11-01 20:04 UTC_
