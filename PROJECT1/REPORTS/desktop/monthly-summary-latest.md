---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 22 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 942 | 676 | ▼ -266 (-28%) |
| Version × cause spikes flagged | 7 | 4 | ▼ -3 |
| — of which **new** regressions | 1 | 1 | ▬ 0 |
| Cause-level surges flagged | 2 | 0 | ▼ -2 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| 🆕 new | 2026-09-16 | v153 × m:yahooemail | 4 | 7.2× | 75% ans · 0.8h | [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604699](https://support.mozilla.org/questions/1604699 "I messaggi di un account vanno anche in un secondo account") [1604799](https://support.mozilla.org/questions/1604799 "thunderbird deleting my emails from the POP server") [1604953](https://support.mozilla.org/questions/1604953 "Thunderbird won't send emails between  2 AOL accounts") |
| ↗ spreading | 2026-09-16 | v156 × m:microsoftemail | 4 | 4.0× | 75% ans · 50.5h | [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") [1604697](https://support.mozilla.org/questions/1604697 "Authentication Failure outlook.office365.com only on startup") [1604835](https://support.mozilla.org/questions/1604835 "ERROR AL AÑADIR CUENTA DE OUTLOOK") [1604859](https://support.mozilla.org/questions/1604859 "autenticazione non riuscita durante la connessione al server outlook su thunderb") |
| ↗ spreading | 2026-09-07 | v155 × proto:pop | 4 | 3.7× | 75% ans · 5.2h | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |
| ↻ recurring | 2026-09-01 | v154 × feat:printing | 4 | 18.4× | 100% ans · 13.8h | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| feat:printing | 36 | 8 | ▼ -28 (-78%) |
| m:gmail | 75 | 51 | ▼ -24 (-32%) |
| m:spectrum | 34 | 17 | ▼ -17 (-50%) |
| feat:addressbook | 25 | 8 | ▼ -17 (-68%) |
| m:yahooemail | 55 | 41 | ▼ -14 (-25%) |
| feat:calendar | 16 | 3 | ▼ -13 (-81%) |
| feat:import_export | 23 | 11 | ▼ -12 (-52%) |
| m:microsoftemail | 53 | 42 | ▼ -11 (-21%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 127 | ▼ -314 (-71%) |
| v154 | 202 | 40 | ▼ -162 (-80%) |
| v155 | 0 | 229 | ▲ +229 |
| v140 | 68 | 33 | ▼ -35 (-51%) |
| v156 | 0 | 71 | ▲ +71 |
| v115 | 24 | 20 | ▼ -4 (-17%) |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 574 | ▼ -176 (-23%) |
| os:linux | 94 | 37 | ▼ -57 (-61%) |
| os:macos | 59 | 38 | ▼ -21 (-36%) |
| os:android | 10 | 4 | ▼ -6 (-60%) |
| os:other | 6 | 5 | ▼ -1 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 230 | ▼ -3 (-1%) |
| email-and-messaging | 80 | 57 | ▼ -23 (-29%) |
| customization | 86 | 48 | ▼ -38 (-44%) |
| passwords-and-sign-in | 60 | 35 | ▼ -25 (-42%) |
| connectivity | 48 | 33 | ▼ -15 (-31%) |
| attachments | 49 | 23 | ▼ -26 (-53%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-22 08:08 UTC_
