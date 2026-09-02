---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 2 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 941 | 63 | ▼ -878 (-93%) |
| Version × cause spikes flagged | 4 | 0 | ▼ -4 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 1 | 0 | ▼ -1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

_No spikes flagged this month at current thresholds._

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 75 | 4 | ▼ -71 (-95%) |
| proto:imap | 70 | 7 | ▼ -63 (-90%) |
| m:yahooemail | 55 | 1 | ▼ -54 (-98%) |
| m:microsoftemail | 53 | 2 | ▼ -51 (-96%) |
| proto:pop | 46 | 2 | ▼ -44 (-96%) |
| proto:smtp | 44 | 2 | ▼ -42 (-95%) |
| m:spectrum | 34 | 2 | ▼ -32 (-94%) |
| proto:oauth | 19 | 1 | ▼ -18 (-95%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 8 | ▼ -433 (-98%) |
| v154 | 202 | 21 | ▼ -181 (-90%) |
| v140 | 67 | 8 | ▼ -59 (-88%) |
| v150 | 25 | 0 | ▼ -25 (-100%) |
| v115 | 24 | 0 | ▼ -24 (-100%) |
| v151 | 7 | 0 | ▼ -7 |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 52 | ▼ -698 (-93%) |
| os:linux | 93 | 1 | ▼ -92 (-99%) |
| os:macos | 59 | 3 | ▼ -56 (-95%) |
| os:android | 10 | 1 | ▼ -9 (-90%) |
| os:other | 6 | 3 | ▼ -3 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 18 | ▼ -215 (-92%) |
| customization | 86 | 2 | ▼ -84 (-98%) |
| email-and-messaging | 80 | 5 | ▼ -75 (-94%) |
| passwords-and-sign-in | 60 | 4 | ▼ -56 (-93%) |
| attachments | 49 | 8 | ▼ -41 (-84%) |
| connectivity | 48 | 3 | ▼ -45 (-94%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-02 20:07 UTC_
