---
layout: base
title: Desktop Engineering Support Summary — October 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## October 2026 vs September 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **October 2026 is in progress** — data through day 6 of 31. Counts are partial, so the deltas below understate October 2026; treat volume changes as directional until the month closes.

## Headline

| | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 976 | 232 | ▼ -744 (-76%) |
| Version × cause spikes flagged | 5 | 3 | ▼ -2 |
| — of which **new** regressions | 2 | 1 | ▼ -1 |
| Cause-level surges flagged | 1 | 0 | ▼ -1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| 🆕 new | 2026-10-04 | v157 × feat:attachments | 5 | 9.8× | 80% ans · 6.8h | [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") [1609601](https://support.mozilla.org/questions/1609601 "Change the app that opens email attachments") [1609642](https://support.mozilla.org/questions/1609642 "Attach button does not respond. Drag and Drop works. (bug2077590)") [1609643](https://support.mozilla.org/questions/1609643 "email beantwoorden, bijlage knop werkt niet") [1609719](https://support.mozilla.org/questions/1609719 "Unable to attach files to email") |
| ↗ spreading | 2026-10-05 | v153 × feat:attachments | 6 | 14.8× | 83% ans · 0.6h | [1609864](https://support.mozilla.org/questions/1609864 "allegati che non si possono più inserire nell'email") [1609904](https://support.mozilla.org/questions/1609904 "Unable to attach a document to a return email") [1609918](https://support.mozilla.org/questions/1609918 "allegati") [1609979](https://support.mozilla.org/questions/1609979 "why can't i attach files to sent email?") [1609986](https://support.mozilla.org/questions/1609986 "not launching file explorer to attach files") +1 |
| ↻ recurring | 2026-10-05 | v157 × feat:attachments | 4 | 6.2× | 100% ans · 5.4h | [1609825](https://support.mozilla.org/questions/1609825 "nach dem letzten Update kann ich keine Attachments versenden") [1609880](https://support.mozilla.org/questions/1609880 "I cannot add an attachment, when I press the attachment button nothing happens") [1609897](https://support.mozilla.org/questions/1609897 "The 'Attach' button does not respond to outgoing emails") [1609916](https://support.mozilla.org/questions/1609916 "Attach button dont work after updating to tb 157") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| proto:imap | 79 | 17 | ▼ -62 (-78%) |
| proto:pop | 62 | 9 | ▼ -53 (-85%) |
| m:microsoftemail | 67 | 15 | ▼ -52 (-78%) |
| m:yahooemail | 60 | 9 | ▼ -51 (-85%) |
| m:gmail | 66 | 18 | ▼ -48 (-73%) |
| proto:smtp | 53 | 11 | ▼ -42 (-79%) |
| proto:oauth | 27 | 4 | ▼ -23 (-85%) |
| feat:import_export | 23 | 2 | ▼ -21 (-91%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in October 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| v153 | 193 | 59 | ▼ -134 (-69%) |
| v155 | 239 | 0 | ▼ -239 (-100%) |
| v156 | 203 | 12 | ▼ -191 (-94%) |
| v157 | 3 | 97 | ▲ +94 |
| v140 | 44 | 9 | ▼ -35 (-80%) |
| v154 | 42 | 0 | ▼ -42 (-100%) |

### Operating-system mix

| Operating-system mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 815 | 206 | ▼ -609 (-75%) |
| os:linux | 63 | 12 | ▼ -51 (-81%) |
| os:macos | 62 | 7 | ▼ -55 (-89%) |
| os:other | 7 | 3 | ▼ -4 |
| os:android | 5 | 2 | ▼ -3 |

### Topic mix

| Topic mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 317 | 55 | ▼ -262 (-83%) |
| email-and-messaging | 85 | 14 | ▼ -71 (-84%) |
| customization | 71 | 18 | ▼ -53 (-75%) |
| attachments | 28 | 59 | ▲ +31 (+111%) |
| passwords-and-sign-in | 54 | 9 | ▼ -45 (-83%) |
| account-management | 50 | 5 | ▼ -45 (-90%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · October 2026 vs September 2026._

_Last updated: 2026-10-06 20:08 UTC_
