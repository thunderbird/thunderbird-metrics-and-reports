---
layout: base
title: Desktop Engineering Support Summary — October 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## October 2026 vs September 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **October 2026 is in progress** — data through day 2 of 31. Counts are partial, so the deltas below understate October 2026; treat volume changes as directional until the month closes.

## Headline

| | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 971 | 58 | ▼ -913 (-94%) |
| Version × cause spikes flagged | 5 | 0 | ▼ -5 |
| — of which **new** regressions | 2 | 0 | ▼ -2 |
| Cause-level surges flagged | 1 | 0 | ▼ -1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

_No spikes flagged this month at current thresholds._

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| proto:imap | 78 | 4 | ▼ -74 (-95%) |
| m:microsoftemail | 66 | 4 | ▼ -62 (-94%) |
| m:gmail | 66 | 4 | ▼ -62 (-94%) |
| proto:pop | 62 | 3 | ▼ -59 (-95%) |
| m:yahooemail | 59 | 5 | ▼ -54 (-92%) |
| proto:smtp | 53 | 4 | ▼ -49 (-92%) |
| proto:oauth | 27 | 1 | ▼ -26 (-96%) |
| feat:import_export | 23 | 0 | ▼ -23 (-100%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in October 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| v155 | 237 | 0 | ▼ -237 (-100%) |
| v156 | 203 | 10 | ▼ -193 (-95%) |
| v153 | 192 | 8 | ▼ -184 (-96%) |
| v140 | 44 | 2 | ▼ -42 (-95%) |
| v154 | 42 | 0 | ▼ -42 (-100%) |
| v157 | 3 | 21 | ▲ +18 |

### Operating-system mix

| Operating-system mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 811 | 49 | ▼ -762 (-94%) |
| os:linux | 62 | 5 | ▼ -57 (-92%) |
| os:macos | 62 | 1 | ▼ -61 (-98%) |
| os:other | 7 | 1 | ▼ -6 |
| os:android | 5 | 1 | ▼ -4 |

### Topic mix

| Topic mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 317 | 15 | ▼ -302 (-95%) |
| email-and-messaging | 84 | 3 | ▼ -81 (-96%) |
| customization | 71 | 6 | ▼ -65 (-92%) |
| passwords-and-sign-in | 51 | 3 | ▼ -48 (-94%) |
| account-management | 50 | 3 | ▼ -47 (-94%) |
| connectivity | 50 | 1 | ▼ -49 (-98%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · October 2026 vs September 2026._

_Last updated: 2026-10-02 20:07 UTC_
