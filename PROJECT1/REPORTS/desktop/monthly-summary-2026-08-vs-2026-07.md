---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **August 2026 is in progress** — data through day 4 of 31. Counts are partial, so the deltas below understate August 2026; treat volume changes as directional until the month closes.

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 89 | ▼ -642 (-88%) |
| Version × cause spikes flagged | 0 | 1 | ▲ +1 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 0 | 0 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-08-04 | v153 × m:microsoftemail | 5 | 4.3× | 100% ans · 0.8h | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") |

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 73 | 9 | ▼ -64 (-88%) |
| proto:imap | 56 | 7 | ▼ -49 (-88%) |
| proto:pop | 42 | 6 | ▼ -36 (-86%) |
| proto:smtp | 35 | 4 | ▼ -31 (-89%) |
| m:microsoftemail | 36 | 12 | ▼ -24 (-67%) |
| m:yahooemail | 30 | 7 | ▼ -23 (-77%) |
| proto:oauth | 20 | 1 | ▼ -19 (-95%) |
| m:comcast | 13 | 2 | ▼ -11 (-85%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v152 | 211 | 2 | ▼ -209 (-99%) |
| v140 | 186 | 6 | ▼ -180 (-97%) |
| v153 | 101 | 58 | ▼ -43 (-43%) |
| v150 | 26 | 2 | ▼ -24 (-92%) |
| v115 | 16 | 3 | ▼ -13 (-81%) |
| v149 | 6 | 0 | ▼ -6 |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 66 | ▼ -523 (-89%) |
| os:linux | 61 | 12 | ▼ -49 (-80%) |
| os:macos | 45 | 5 | ▼ -40 (-89%) |
| os:other | 11 | 2 | ▼ -9 (-82%) |
| os:android | 7 | 1 | ▼ -6 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 17 | ▼ -168 (-91%) |
| email-and-messaging | 82 | 6 | ▼ -76 (-93%) |
| customization | 73 | 9 | ▼ -64 (-88%) |
| passwords-and-sign-in | 53 | 4 | ▼ -49 (-92%) |
| junk-mail-and-spam | 24 | 11 | ▼ -13 (-54%) |
| account-management | 28 | 6 | ▼ -22 (-79%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-08-04 20:31 UTC_
