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
| Support questions (load) | 971 | 39 | ▼ -932 (-96%) |
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
| proto:imap | 78 | 2 | ▼ -76 (-97%) |
| m:gmail | 66 | 1 | ▼ -65 (-98%) |
| m:microsoftemail | 66 | 3 | ▼ -63 (-95%) |
| proto:pop | 62 | 3 | ▼ -59 (-95%) |
| m:yahooemail | 59 | 3 | ▼ -56 (-95%) |
| proto:smtp | 53 | 2 | ▼ -51 (-96%) |
| proto:oauth | 27 | 0 | ▼ -27 (-100%) |
| feat:import_export | 23 | 0 | ▼ -23 (-100%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in October 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| v155 | 237 | 0 | ▼ -237 (-100%) |
| v156 | 203 | 8 | ▼ -195 (-96%) |
| v153 | 192 | 5 | ▼ -187 (-97%) |
| v140 | 44 | 2 | ▼ -42 (-95%) |
| v154 | 42 | 0 | ▼ -42 (-100%) |
| v115 | 24 | 0 | ▼ -24 (-100%) |

### Operating-system mix

| Operating-system mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 811 | 33 | ▼ -778 (-96%) |
| os:linux | 62 | 4 | ▼ -58 (-94%) |
| os:macos | 62 | 0 | ▼ -62 (-100%) |
| os:other | 7 | 0 | ▼ -7 |
| os:android | 5 | 1 | ▼ -4 |

### Topic mix

| Topic mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 317 | 7 | ▼ -310 (-98%) |
| email-and-messaging | 84 | 3 | ▼ -81 (-96%) |
| customization | 71 | 5 | ▼ -66 (-93%) |
| passwords-and-sign-in | 51 | 3 | ▼ -48 (-94%) |
| account-management | 50 | 3 | ▼ -47 (-94%) |
| connectivity | 50 | 0 | ▼ -50 (-100%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · October 2026 vs September 2026._

_Last updated: 2026-10-02 08:08 UTC_
