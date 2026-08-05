---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **August 2026 is in progress** — data through day 5 of 31. Counts are partial, so the deltas below understate August 2026; treat volume changes as directional until the month closes.

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 116 | ▼ -615 (-84%) |
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
| m:gmail | 73 | 11 | ▼ -62 (-85%) |
| proto:imap | 56 | 10 | ▼ -46 (-82%) |
| proto:pop | 42 | 8 | ▼ -34 (-81%) |
| proto:smtp | 35 | 5 | ▼ -30 (-86%) |
| m:microsoftemail | 36 | 14 | ▼ -22 (-61%) |
| m:yahooemail | 30 | 9 | ▼ -21 (-70%) |
| proto:oauth | 20 | 1 | ▼ -19 (-95%) |
| m:comcast | 13 | 3 | ▼ -10 (-77%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v152 | 211 | 2 | ▼ -209 (-99%) |
| v140 | 186 | 8 | ▼ -178 (-96%) |
| v153 | 101 | 72 | ▼ -29 (-29%) |
| v150 | 26 | 2 | ▼ -24 (-92%) |
| v115 | 16 | 5 | ▼ -11 (-69%) |
| v149 | 6 | 0 | ▼ -6 |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 84 | ▼ -505 (-86%) |
| os:linux | 61 | 14 | ▼ -47 (-77%) |
| os:macos | 45 | 11 | ▼ -34 (-76%) |
| os:other | 11 | 2 | ▼ -9 (-82%) |
| os:android | 7 | 2 | ▼ -5 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 22 | ▼ -163 (-88%) |
| email-and-messaging | 82 | 8 | ▼ -74 (-90%) |
| customization | 73 | 12 | ▼ -61 (-84%) |
| passwords-and-sign-in | 53 | 7 | ▼ -46 (-87%) |
| junk-mail-and-spam | 24 | 11 | ▼ -13 (-54%) |
| account-management | 28 | 7 | ▼ -21 (-75%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-08-05 20:30 UTC_
