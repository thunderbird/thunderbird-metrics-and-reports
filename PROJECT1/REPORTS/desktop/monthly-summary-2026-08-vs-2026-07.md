---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **August 2026 is in progress** — data through day 11 of 31. Counts are partial, so the deltas below understate August 2026; treat volume changes as directional until the month closes.

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 284 | ▼ -447 (-61%) |
| Version × cause spikes flagged | 0 | 2 | ▲ +2 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 0 | 0 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-08-10 | v153 × proto:pop | 4 | 3.3× | 75% ans · 1.1h | [1597551](https://support.mozilla.org/questions/1597551 "Thunderbird POP stopped retrieving email from one mail box, No error message") [1597571](https://support.mozilla.org/questions/1597571 "Email collection over pop failed on one account, server settings rejected when I") [1597638](https://support.mozilla.org/questions/1597638 "How logging onto wowway with old password?") [1597683](https://support.mozilla.org/questions/1597683 "Hotmail personal account: IMAP OAuth2 works but SMTP OAuth2 fails with message: ") |
| ↗ spreading | 2026-08-04 | v153 × m:microsoftemail | 5 | 3.1× | 100% ans · 0.8h | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") |

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 73 | 23 | ▼ -50 (-68%) |
| proto:imap | 56 | 21 | ▼ -35 (-62%) |
| proto:smtp | 35 | 10 | ▼ -25 (-71%) |
| proto:pop | 42 | 21 | ▼ -21 (-50%) |
| m:microsoftemail | 36 | 20 | ▼ -16 (-44%) |
| proto:oauth | 20 | 7 | ▼ -13 (-65%) |
| m:comcast | 13 | 3 | ▼ -10 (-77%) |
| m:yahooemail | 30 | 22 | ▼ -8 (-27%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v153 | 101 | 185 | ▲ +84 (+83%) |
| v152 | 211 | 5 | ▼ -206 (-98%) |
| v140 | 186 | 25 | ▼ -161 (-87%) |
| v150 | 26 | 12 | ▼ -14 (-54%) |
| v115 | 16 | 10 | ▼ -6 (-38%) |
| v128 | 5 | 1 | ▼ -4 |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 205 | ▼ -384 (-65%) |
| os:linux | 61 | 41 | ▼ -20 (-33%) |
| os:macos | 45 | 22 | ▼ -23 (-51%) |
| os:other | 11 | 4 | ▼ -7 (-64%) |
| os:android | 7 | 4 | ▼ -3 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 54 | ▼ -131 (-71%) |
| email-and-messaging | 82 | 23 | ▼ -59 (-72%) |
| customization | 73 | 31 | ▼ -42 (-58%) |
| passwords-and-sign-in | 53 | 22 | ▼ -31 (-58%) |
| import-and-export-email | 30 | 16 | ▼ -14 (-47%) |
| junk-mail-and-spam | 24 | 18 | ▼ -6 (-25%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-08-11 20:14 UTC_
