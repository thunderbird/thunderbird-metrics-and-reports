---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 25 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 942 | 812 | ▼ -130 (-14%) |
| Version × cause spikes flagged | 7 | 5 | ▼ -2 |
| — of which **new** regressions | 1 | 2 | ▲ +1 |
| Cause-level surges flagged | 2 | 1 | ▼ -1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| 🆕 new | 2026-09-23 | v153 × m:alice_it | 5 | 76.3× | 100% ans · 3.1h | [1606888](https://support.mozilla.org/questions/1606888 "non mi funziona la mail alice.it") [1606928](https://support.mozilla.org/questions/1606928 "non ricevo le mail di Alicemail") [1606938](https://support.mozilla.org/questions/1606938 "Alice mail") [1607000](https://support.mozilla.org/questions/1607000 "non scarico messaggi") [1607026](https://support.mozilla.org/questions/1607026 "Non riesco a scaricare posta alice su thunderbid, mi da errore di collegamento..") |
| 🆕 new | 2026-09-16 | v153 × m:yahooemail | 4 | 7.2× | 75% ans · 0.8h | [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604699](https://support.mozilla.org/questions/1604699 "I messaggi di un account vanno anche in un secondo account") [1604799](https://support.mozilla.org/questions/1604799 "thunderbird deleting my emails from the POP server") [1604953](https://support.mozilla.org/questions/1604953 "Thunderbird won't send emails between  2 AOL accounts") |
| ↗ spreading | 2026-09-16 | v156 × m:microsoftemail | 4 | 4.0× | 75% ans · 50.5h | [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") [1604697](https://support.mozilla.org/questions/1604697 "Authentication Failure outlook.office365.com only on startup") [1604835](https://support.mozilla.org/questions/1604835 "ERROR AL AÑADIR CUENTA DE OUTLOOK") [1604859](https://support.mozilla.org/questions/1604859 "autenticazione non riuscita durante la connessione al server outlook su thunderb") |
| ↗ spreading | 2026-09-07 | v155 × proto:pop | 4 | 3.7× | 75% ans · 5.2h | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |
| ↻ recurring | 2026-09-01 | v154 × feat:printing | 4 | 18.8× | 100% ans · 13.8h | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") |

### Cause-level surges — provider / protocol / AV / feature (any version)

Version-agnostic (a provider outage spans versions), vs a trailing-month baseline.

| Cause | Qs | Served | vs baseline | Rise | Example questions |
|:--|--:|:--|--:|:--|:--|
| m:alice_it | 20 | 95% ans · 1.2h | 1.0 | 20.0× | [1602510](https://support.mozilla.org/questions/1602510 "Connessione rifiutata con alice.it") [1605600](https://support.mozilla.org/questions/1605600 "Risposta alle mail diversa da prima") [1606403](https://support.mozilla.org/questions/1606403 "non ricevo posta su pino.[RIMOSSO]@alice.it, sono con starlink, nè riesco a invi") [1606677](https://support.mozilla.org/questions/1606677 "Uso Thunderbird e non ricevo più la posta dal server in.alice.it") [1606715](https://support.mozilla.org/questions/1606715 "Non ricevo i messaggi nella mia e.mail centrosaggi@alice.it") +15 |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| feat:printing | 36 | 8 | ▼ -28 (-78%) |
| m:alice_it | 1 | 20 | ▲ +19 |
| m:gmail | 75 | 59 | ▼ -16 (-21%) |
| feat:addressbook | 25 | 11 | ▼ -14 (-56%) |
| m:spectrum | 34 | 20 | ▼ -14 (-41%) |
| feat:filters | 11 | 21 | ▲ +10 (+91%) |
| feat:calendar | 16 | 6 | ▼ -10 (-62%) |
| feat:import_export | 23 | 13 | ▼ -10 (-43%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 155 | ▼ -286 (-65%) |
| v154 | 202 | 42 | ▼ -160 (-79%) |
| v155 | 0 | 233 | ▲ +233 |
| v156 | 0 | 126 | ▲ +126 |
| v140 | 68 | 40 | ▼ -28 (-41%) |
| v115 | 24 | 22 | ▼ -2 (-8%) |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 690 | ▼ -60 (-8%) |
| os:linux | 94 | 44 | ▼ -50 (-53%) |
| os:macos | 59 | 48 | ▼ -11 (-19%) |
| os:android | 10 | 4 | ▼ -6 (-60%) |
| os:other | 6 | 5 | ▼ -1 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 276 | ▲ +43 (+18%) |
| customization | 86 | 60 | ▼ -26 (-30%) |
| email-and-messaging | 80 | 66 | ▼ -14 (-18%) |
| passwords-and-sign-in | 60 | 43 | ▼ -17 (-28%) |
| connectivity | 48 | 45 | ▼ -3 (-6%) |
| account-management | 34 | 43 | ▲ +9 (+26%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-25 08:08 UTC_
