---
layout: base
title: Desktop Engineering Support Summary — October 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## October 2026 vs September 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **October 2026 is in progress** — data through day 3 of 31. Counts are partial, so the deltas below understate October 2026; treat volume changes as directional until the month closes.

## Headline

| | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 971 | 97 | ▼ -874 (-90%) |
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
| proto:imap | 78 | 8 | ▼ -70 (-90%) |
| m:microsoftemail | 66 | 7 | ▼ -59 (-89%) |
| m:gmail | 66 | 8 | ▼ -58 (-88%) |
| proto:pop | 62 | 5 | ▼ -57 (-92%) |
| m:yahooemail | 59 | 6 | ▼ -53 (-90%) |
| proto:smtp | 53 | 7 | ▼ -46 (-87%) |
| proto:oauth | 27 | 1 | ▼ -26 (-96%) |
| feat:import_export | 23 | 0 | ▼ -23 (-100%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in October 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| v155 | 237 | 0 | ▼ -237 (-100%) |
| v156 | 203 | 12 | ▼ -191 (-94%) |
| v153 | 192 | 22 | ▼ -170 (-89%) |
| v140 | 44 | 4 | ▼ -40 (-91%) |
| v154 | 42 | 0 | ▼ -42 (-100%) |
| v157 | 3 | 35 | ▲ +32 |

### Operating-system mix

| Operating-system mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 811 | 85 | ▼ -726 (-90%) |
| os:linux | 62 | 7 | ▼ -55 (-89%) |
| os:macos | 62 | 2 | ▼ -60 (-97%) |
| os:other | 7 | 1 | ▼ -6 |
| os:android | 5 | 1 | ▼ -4 |

### Topic mix

| Topic mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 317 | 28 | ▼ -289 (-91%) |
| email-and-messaging | 84 | 3 | ▼ -81 (-96%) |
| customization | 71 | 10 | ▼ -61 (-86%) |
| passwords-and-sign-in | 51 | 4 | ▼ -47 (-92%) |
| account-management | 50 | 5 | ▼ -45 (-90%) |
| connectivity | 50 | 1 | ▼ -49 (-98%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · October 2026 vs September 2026._

_Last updated: 2026-10-03 20:59 UTC_
