---
layout: base
title: Desktop Engineering Support Summary — June 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## June 2026 vs May 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

## Headline

| | May 2026 | June 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 812 | 724 | ▼ -88 (-11%) |
| Version × cause spikes flagged | 5 | 3 | ▼ -2 |
| — of which **new** regressions | 3 | 2 | ▼ -1 |
| Cause-level surges flagged | 0 | 0 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| 🆕 new | 2026-06-09 | v151 × m:spectrum | 7 | 21.6× | 100% ans · 14.3h | [1586383](https://support.mozilla.org/questions/1586383 "Email Accounts are highlighted RED") [1586405](https://support.mozilla.org/questions/1586405 "The certificate for mobile.charter.net does not come from a trusted source.") [1586446](https://support.mozilla.org/questions/1586446 "Unable to receive and send emails.") [1586481](https://support.mozilla.org/questions/1586481 "Connetion error, can't recieve emails") [1586486](https://support.mozilla.org/questions/1586486 "Thunderbird is showing Certificate for mobile.charter.net:993 does not come from") +2 |
| 🆕 new | 2026-06-30 | v152 × m:gmail | 4 | 4.7× | ⚠️ 50% ans · 2.5h | [1590372](https://support.mozilla.org/questions/1590372 "Urgent question: Wrong email group when I sign in coming up") [1590393](https://support.mozilla.org/questions/1590393 "Storende pop-up naar aanleiding van verwijderde google-account") [1590463](https://support.mozilla.org/questions/1590463 "Message not visible with no filter activated, all account are synchronized") [1590499](https://support.mozilla.org/questions/1590499 "archive Gmail to local storage　by Tb") |
| ↗ spreading | 2026-06-29 | v152 × m:microsoftemail | 6 | 4.3× | ⚠️ 33% ans · 4.1h | [1590178](https://support.mozilla.org/questions/1590178 "Adding 2nd outlook accound") [1590198](https://support.mozilla.org/questions/1590198 "Thunderbird emails have started to only show links and not the pictures within t") [1590208](https://support.mozilla.org/questions/1590208 "Can't connect to my live and outlook accounts since 2 weeks") [1590210](https://support.mozilla.org/questions/1590210 "TBird152.0  is not displaing HTML emails properly.") [1590301](https://support.mozilla.org/questions/1590301 "One-hour delay in the guest's meeting schedule (Atraso de uma hora na agenda do ") +1 |

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | May 2026 | June 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 76 | 52 | ▼ -24 (-32%) |
| m:microsoftemail | 75 | 54 | ▼ -21 (-28%) |
| m:yahooemail | 43 | 26 | ▼ -17 (-40%) |
| proto:imap | 65 | 51 | ▼ -14 (-22%) |
| proto:smtp | 36 | 25 | ▼ -11 (-31%) |
| proto:pop | 41 | 30 | ▼ -11 (-27%) |
| proto:oauth | 17 | 12 | ▼ -5 (-29%) |
| m:icloud | 5 | 8 | ▲ +3 |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in June 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | May 2026 | June 2026 | Change |
|:--|--:|--:|:--|
| v140 | 205 | 179 | ▼ -26 (-13%) |
| v151 | 136 | 189 | ▲ +53 (+39%) |
| v150 | 274 | 17 | ▼ -257 (-94%) |
| v152 | 1 | 158 | ▲ +157 |
| v115 | 23 | 26 | ▲ +3 (+13%) |
| v149 | 17 | 11 | ▼ -6 (-35%) |

### Operating-system mix

| Operating-system mix | May 2026 | June 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 655 | 589 | ▼ -66 (-10%) |
| os:linux | 69 | 62 | ▼ -7 (-10%) |
| os:macos | 53 | 49 | ▼ -4 (-8%) |
| os:other | 8 | 11 | ▲ +3 |
| os:android | 6 | 4 | ▼ -2 |

### Topic mix

| Topic mix | May 2026 | June 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 215 | 204 | ▼ -11 (-5%) |
| customization | 103 | 65 | ▼ -38 (-37%) |
| email-and-messaging | 90 | 49 | ▼ -41 (-46%) |
| passwords-and-sign-in | 56 | 32 | ▼ -24 (-43%) |
| connectivity | 37 | 34 | ▼ -3 (-8%) |
| junk-mail-and-spam | 35 | 29 | ▼ -6 (-17%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · June 2026 vs May 2026._

_Last updated: 2026-07-08 08:51 UTC_
