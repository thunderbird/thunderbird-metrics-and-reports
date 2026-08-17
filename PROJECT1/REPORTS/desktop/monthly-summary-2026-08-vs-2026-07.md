---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **August 2026 is in progress** — data through day 17 of 31. Counts are partial, so the deltas below understate August 2026; treat volume changes as directional until the month closes.

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 440 | ▼ -291 (-40%) |
| Version × cause spikes flagged | 0 | 4 | ▲ +4 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 0 | 0 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-08-10 | v153 × proto:pop | 4 | 3.2× | 75% ans · 1.1h | [1597551](https://support.mozilla.org/questions/1597551 "Thunderbird POP stopped retrieving email from one mail box, No error message") [1597571](https://support.mozilla.org/questions/1597571 "Email collection over pop failed on one account, server settings rejected when I") [1597638](https://support.mozilla.org/questions/1597638 "How logging onto wowway with old password?") [1597683](https://support.mozilla.org/questions/1597683 "Hotmail personal account: IMAP OAuth2 works but SMTP OAuth2 fails with message: ") |
| ↗ spreading | 2026-08-04 | v153 × m:microsoftemail | 5 | 3.1× | 100% ans · 0.8h | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") |
| ↻ recurring | 2026-08-14 | v153 × proto:pop | 4 | 3.3× | 100% ans · 8.0h | [1598311](https://support.mozilla.org/questions/1598311 "Thunderbird went goofy - multiple gmail accounts, authentication errors. And del") [1598314](https://support.mozilla.org/questions/1598314 "Email from Roadrunner.com does not show but server test works") [1598327](https://support.mozilla.org/questions/1598327 "Unable to receive e-mail") [1598357](https://support.mozilla.org/questions/1598357 "Recently Unable to send (SMTP) from Thunderbird from Cox.com (now thru Yahoo).") |
| ↻ recurring | 2026-08-13 | v153 × proto:pop | 4 | 3.2× | 100% ans · 1.2h | [1598091](https://support.mozilla.org/questions/1598091 "thunderbird has stopped receiving emails from century link") [1598146](https://support.mozilla.org/questions/1598146 "Can't access my account") [1598151](https://support.mozilla.org/questions/1598151 "How to set up automatic email forwarding from Thunderbird to Gmail") [1598175](https://support.mozilla.org/questions/1598175 "Thunderbird won't download email messages from Yahoo (formerly Cox) account") |

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 73 | 34 | ▼ -39 (-53%) |
| proto:imap | 56 | 33 | ▼ -23 (-41%) |
| proto:smtp | 35 | 17 | ▼ -18 (-51%) |
| proto:pop | 42 | 30 | ▼ -12 (-29%) |
| proto:oauth | 20 | 9 | ▼ -11 (-55%) |
| m:yahooemail | 30 | 37 | ▲ +7 (+23%) |
| m:microsoftemail | 36 | 29 | ▼ -7 (-19%) |
| m:comcast | 13 | 7 | ▼ -6 (-46%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v153 | 101 | 292 | ▲ +191 (+189%) |
| v140 | 186 | 37 | ▼ -149 (-80%) |
| v152 | 211 | 6 | ▼ -205 (-97%) |
| v150 | 26 | 15 | ▼ -11 (-42%) |
| v115 | 16 | 13 | ▼ -3 (-19%) |
| v151 | 4 | 5 | ▲ +1 |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 323 | ▼ -266 (-45%) |
| os:linux | 61 | 58 | ▼ -3 (-5%) |
| os:macos | 45 | 36 | ▼ -9 (-20%) |
| os:other | 11 | 4 | ▼ -7 (-64%) |
| os:android | 7 | 6 | ▼ -1 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 96 | ▼ -89 (-48%) |
| customization | 73 | 50 | ▼ -23 (-32%) |
| email-and-messaging | 82 | 39 | ▼ -43 (-52%) |
| passwords-and-sign-in | 53 | 27 | ▼ -26 (-49%) |
| import-and-export-email | 30 | 23 | ▼ -7 (-23%) |
| account-management | 28 | 18 | ▼ -10 (-36%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-08-17 08:12 UTC_
