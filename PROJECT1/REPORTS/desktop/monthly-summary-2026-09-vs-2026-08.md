---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 23 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 942 | 722 | ▼ -220 (-23%) |
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
| ↻ recurring | 2026-09-01 | v154 × feat:printing | 4 | 18.5× | 100% ans · 13.8h | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| feat:printing | 36 | 8 | ▼ -28 (-78%) |
| m:gmail | 75 | 57 | ▼ -18 (-24%) |
| feat:addressbook | 25 | 9 | ▼ -16 (-64%) |
| m:spectrum | 34 | 19 | ▼ -15 (-44%) |
| feat:calendar | 16 | 4 | ▼ -12 (-75%) |
| feat:import_export | 23 | 12 | ▼ -11 (-48%) |
| m:yahooemail | 55 | 44 | ▼ -11 (-20%) |
| feat:filters | 11 | 21 | ▲ +10 (+91%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 132 | ▼ -309 (-70%) |
| v154 | 202 | 42 | ▼ -160 (-79%) |
| v155 | 0 | 231 | ▲ +231 |
| v140 | 68 | 34 | ▼ -34 (-50%) |
| v156 | 0 | 87 | ▲ +87 |
| v115 | 24 | 21 | ▼ -3 (-12%) |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 611 | ▼ -139 (-19%) |
| os:linux | 94 | 41 | ▼ -53 (-56%) |
| os:macos | 59 | 41 | ▼ -18 (-31%) |
| os:android | 10 | 5 | ▼ -5 (-50%) |
| os:other | 6 | 5 | ▼ -1 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 245 | ▲ +12 (+5%) |
| email-and-messaging | 80 | 61 | ▼ -19 (-24%) |
| customization | 86 | 51 | ▼ -35 (-41%) |
| passwords-and-sign-in | 60 | 39 | ▼ -21 (-35%) |
| connectivity | 48 | 37 | ▼ -11 (-23%) |
| account-management | 34 | 38 | ▲ +4 (+12%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-23 08:08 UTC_
