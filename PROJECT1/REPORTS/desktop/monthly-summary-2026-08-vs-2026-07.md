---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **August 2026 is in progress** — data through day 7 of 31. Counts are partial, so the deltas below understate August 2026; treat volume changes as directional until the month closes.

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 180 | ▼ -551 (-75%) |
| Version × cause spikes flagged | 0 | 1 | ▲ +1 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 0 | 0 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-08-04 | v153 × m:microsoftemail | 5 | 3.0× | 100% ans · 0.8h | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") |

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 73 | 14 | ▼ -59 (-81%) |
| proto:imap | 56 | 12 | ▼ -44 (-79%) |
| proto:pop | 42 | 12 | ▼ -30 (-71%) |
| proto:smtp | 35 | 7 | ▼ -28 (-80%) |
| proto:oauth | 20 | 1 | ▼ -19 (-95%) |
| m:microsoftemail | 36 | 17 | ▼ -19 (-53%) |
| m:yahooemail | 30 | 12 | ▼ -18 (-60%) |
| m:comcast | 13 | 3 | ▼ -10 (-77%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v152 | 211 | 4 | ▼ -207 (-98%) |
| v153 | 101 | 111 | ▲ +10 (+10%) |
| v140 | 186 | 16 | ▼ -170 (-91%) |
| v150 | 26 | 6 | ▼ -20 (-77%) |
| v115 | 16 | 6 | ▼ -10 (-62%) |
| v149 | 6 | 0 | ▼ -6 |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 128 | ▼ -461 (-78%) |
| os:linux | 61 | 23 | ▼ -38 (-62%) |
| os:macos | 45 | 17 | ▼ -28 (-62%) |
| os:other | 11 | 3 | ▼ -8 (-73%) |
| os:android | 7 | 3 | ▼ -4 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 33 | ▼ -152 (-82%) |
| email-and-messaging | 82 | 16 | ▼ -66 (-80%) |
| customization | 73 | 19 | ▼ -54 (-74%) |
| passwords-and-sign-in | 53 | 14 | ▼ -39 (-74%) |
| import-and-export-email | 30 | 9 | ▼ -21 (-70%) |
| junk-mail-and-spam | 24 | 12 | ▼ -12 (-50%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-08-07 20:12 UTC_
