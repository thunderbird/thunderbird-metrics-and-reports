---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **August 2026 is in progress** — data through day 13 of 31. Counts are partial, so the deltas below understate August 2026; treat volume changes as directional until the month closes.

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 326 | ▼ -405 (-55%) |
| Version × cause spikes flagged | 0 | 2 | ▲ +2 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 0 | 0 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-08-10 | v153 × proto:pop | 4 | 3.4× | 75% ans · 1.1h | [1597551](https://support.mozilla.org/questions/1597551 "Thunderbird POP stopped retrieving email from one mail box, No error message") [1597571](https://support.mozilla.org/questions/1597571 "Email collection over pop failed on one account, server settings rejected when I") [1597638](https://support.mozilla.org/questions/1597638 "How logging onto wowway with old password?") [1597683](https://support.mozilla.org/questions/1597683 "Hotmail personal account: IMAP OAuth2 works but SMTP OAuth2 fails with message: ") |
| ↗ spreading | 2026-08-04 | v153 × m:microsoftemail | 5 | 3.1× | 100% ans · 0.8h | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") |

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 73 | 26 | ▼ -47 (-64%) |
| proto:imap | 56 | 24 | ▼ -32 (-57%) |
| proto:smtp | 35 | 13 | ▼ -22 (-63%) |
| proto:pop | 42 | 21 | ▼ -21 (-50%) |
| proto:oauth | 20 | 8 | ▼ -12 (-60%) |
| m:microsoftemail | 36 | 24 | ▼ -12 (-33%) |
| m:comcast | 13 | 3 | ▼ -10 (-77%) |
| m:yahooemail | 30 | 27 | ▼ -3 (-10%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v153 | 101 | 213 | ▲ +112 (+111%) |
| v152 | 211 | 5 | ▼ -206 (-98%) |
| v140 | 186 | 29 | ▼ -157 (-84%) |
| v150 | 26 | 12 | ▼ -14 (-54%) |
| v115 | 16 | 10 | ▼ -6 (-38%) |
| v151 | 4 | 3 | ▼ -1 |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 238 | ▼ -351 (-60%) |
| os:linux | 61 | 44 | ▼ -17 (-28%) |
| os:macos | 45 | 26 | ▼ -19 (-42%) |
| os:other | 11 | 4 | ▼ -7 (-64%) |
| os:android | 7 | 6 | ▼ -1 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 66 | ▼ -119 (-64%) |
| email-and-messaging | 82 | 29 | ▼ -53 (-65%) |
| customization | 73 | 34 | ▼ -39 (-53%) |
| passwords-and-sign-in | 53 | 24 | ▼ -29 (-55%) |
| import-and-export-email | 30 | 20 | ▼ -10 (-33%) |
| junk-mail-and-spam | 24 | 18 | ▼ -6 (-25%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-08-13 08:30 UTC_
