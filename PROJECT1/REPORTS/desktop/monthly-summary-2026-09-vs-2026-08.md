---
layout: base
title: Desktop Engineering Support Summary — September 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## September 2026 vs August 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **September 2026 is in progress** — data through day 15 of 30. Counts are partial, so the deltas below understate September 2026; treat volume changes as directional until the month closes.

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 941 | 474 | ▼ -467 (-50%) |
| Version × cause spikes flagged | 7 | 2 | ▼ -5 |
| — of which **new** regressions | 1 | 0 | ▼ -1 |
| Cause-level surges flagged | 2 | 0 | ▼ -2 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-09-07 | v155 × proto:pop | 4 | 3.8× | 75% ans · 5.2h | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |
| ↻ recurring | 2026-09-01 | v154 × feat:printing | 4 | 17.7× | 100% ans · 13.8h | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 75 | 40 | ▼ -35 (-47%) |
| m:microsoftemail | 53 | 22 | ▼ -31 (-58%) |
| feat:printing | 36 | 8 | ▼ -28 (-78%) |
| m:yahooemail | 55 | 28 | ▼ -27 (-49%) |
| proto:imap | 71 | 45 | ▼ -26 (-37%) |
| proto:pop | 46 | 25 | ▼ -21 (-46%) |
| proto:smtp | 44 | 24 | ▼ -20 (-45%) |
| feat:addressbook | 24 | 5 | ▼ -19 (-79%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in September 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| v153 | 441 | 84 | ▼ -357 (-81%) |
| v154 | 202 | 40 | ▼ -162 (-80%) |
| v155 | 0 | 195 | ▲ +195 |
| v140 | 67 | 28 | ▼ -39 (-58%) |
| v115 | 24 | 15 | ▼ -9 (-38%) |
| v150 | 25 | 7 | ▼ -18 (-72%) |

### Operating-system mix

| Operating-system mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 750 | 402 | ▼ -348 (-46%) |
| os:linux | 93 | 28 | ▼ -65 (-70%) |
| os:macos | 59 | 27 | ▼ -32 (-54%) |
| os:android | 10 | 2 | ▼ -8 (-80%) |
| os:other | 6 | 4 | ▼ -2 |

### Topic mix

| Topic mix | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 233 | 160 | ▼ -73 (-31%) |
| email-and-messaging | 80 | 43 | ▼ -37 (-46%) |
| customization | 86 | 31 | ▼ -55 (-64%) |
| passwords-and-sign-in | 60 | 25 | ▼ -35 (-58%) |
| connectivity | 48 | 19 | ▼ -29 (-60%) |
| attachments | 49 | 17 | ▼ -32 (-65%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · September 2026 vs August 2026._

_Last updated: 2026-09-15 08:08 UTC_
