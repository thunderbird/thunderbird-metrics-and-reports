---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **August 2026 is in progress** — data through day 1 of 31. Counts are partial, so the deltas below understate August 2026; treat volume changes as directional until the month closes.

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 730 | 22 | ▼ -708 (-97%) |
| Version × cause spikes flagged | 0 | 0 | ▬ 0 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 0 | 0 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

_No spikes flagged this month at current thresholds._

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 73 | 1 | ▼ -72 (-99%) |
| proto:imap | 56 | 2 | ▼ -54 (-96%) |
| proto:pop | 42 | 1 | ▼ -41 (-98%) |
| proto:smtp | 34 | 0 | ▼ -34 (-100%) |
| m:microsoftemail | 36 | 2 | ▼ -34 (-94%) |
| m:yahooemail | 30 | 1 | ▼ -29 (-97%) |
| proto:oauth | 20 | 0 | ▼ -20 (-100%) |
| m:comcast | 13 | 1 | ▼ -12 (-92%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v152 | 211 | 1 | ▼ -210 (-100%) |
| v140 | 186 | 1 | ▼ -185 (-99%) |
| v153 | 101 | 13 | ▼ -88 (-87%) |
| v150 | 26 | 0 | ▼ -26 (-100%) |
| v115 | 16 | 1 | ▼ -15 (-94%) |
| v149 | 6 | 0 | ▼ -6 |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 588 | 15 | ▼ -573 (-97%) |
| os:linux | 61 | 4 | ▼ -57 (-93%) |
| os:macos | 45 | 1 | ▼ -44 (-98%) |
| os:other | 11 | 0 | ▼ -11 (-100%) |
| os:android | 7 | 0 | ▼ -7 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 4 | ▼ -181 (-98%) |
| email-and-messaging | 82 | 2 | ▼ -80 (-98%) |
| customization | 73 | 4 | ▼ -69 (-95%) |
| passwords-and-sign-in | 53 | 2 | ▼ -51 (-96%) |
| account-management | 28 | 2 | ▼ -26 (-93%) |
| import-and-export-email | 30 | 0 | ▼ -30 (-100%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-08-02 08:47 UTC_
