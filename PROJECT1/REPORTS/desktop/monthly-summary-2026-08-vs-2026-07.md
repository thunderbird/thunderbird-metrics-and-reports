---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **August 2026 is in progress** — data through day 3 of 31. Counts are partial, so the deltas below understate August 2026; treat volume changes as directional until the month closes.

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 59 | ▼ -672 (-92%) |
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
| m:gmail | 73 | 4 | ▼ -69 (-95%) |
| proto:imap | 56 | 4 | ▼ -52 (-93%) |
| proto:pop | 42 | 4 | ▼ -38 (-90%) |
| proto:smtp | 35 | 3 | ▼ -32 (-91%) |
| m:microsoftemail | 36 | 6 | ▼ -30 (-83%) |
| m:yahooemail | 30 | 3 | ▼ -27 (-90%) |
| proto:oauth | 20 | 0 | ▼ -20 (-100%) |
| m:comcast | 13 | 2 | ▼ -11 (-85%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v152 | 211 | 1 | ▼ -210 (-100%) |
| v140 | 186 | 3 | ▼ -183 (-98%) |
| v153 | 101 | 39 | ▼ -62 (-61%) |
| v150 | 26 | 2 | ▼ -24 (-92%) |
| v115 | 16 | 2 | ▼ -14 (-88%) |
| v149 | 6 | 0 | ▼ -6 |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 44 | ▼ -545 (-93%) |
| os:linux | 61 | 9 | ▼ -52 (-85%) |
| os:macos | 45 | 2 | ▼ -43 (-96%) |
| os:other | 11 | 1 | ▼ -10 (-91%) |
| os:android | 7 | 1 | ▼ -6 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 11 | ▼ -174 (-94%) |
| email-and-messaging | 82 | 5 | ▼ -77 (-94%) |
| customization | 73 | 9 | ▼ -64 (-88%) |
| passwords-and-sign-in | 53 | 3 | ▼ -50 (-94%) |
| account-management | 28 | 5 | ▼ -23 (-82%) |
| junk-mail-and-spam | 24 | 8 | ▼ -16 (-67%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-08-03 20:31 UTC_
