---
layout: base
title: Desktop Engineering Support Summary — October 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## October 2026 vs September 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **October 2026 is in progress** — data through day 5 of 31. Counts are partial, so the deltas below understate October 2026; treat volume changes as directional until the month closes.

## Headline

| | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 974 | 175 | ▼ -799 (-82%) |
| Version × cause spikes flagged | 5 | 2 | ▼ -3 |
| — of which **new** regressions | 2 | 1 | ▼ -1 |
| Cause-level surges flagged | 1 | 0 | ▼ -1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| 🆕 new | 2026-10-04 | v157 × feat:attachments | 5 | 10.2× | 80% ans · 6.8h | [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") [1609601](https://support.mozilla.org/questions/1609601 "Change the app that opens email attachments") [1609642](https://support.mozilla.org/questions/1609642 "Attach button does not respond. Drag and Drop works. (bug2077590)") [1609643](https://support.mozilla.org/questions/1609643 "email beantwoorden, bijlage knop werkt niet") [1609719](https://support.mozilla.org/questions/1609719 "Unable to attach files to email") |
| ↻ recurring | 2026-10-05 | v157 × feat:attachments | 4 | 9.7× | ⚠️ 50% ans · 2.2h | [1609825](https://support.mozilla.org/questions/1609825 "nach dem letzten Update kann ich keine Attachments versenden") [1609880](https://support.mozilla.org/questions/1609880 "I cannot add an attachment, when I press the attachment button nothing happens") [1609897](https://support.mozilla.org/questions/1609897 "The 'Attach' button does not respond to outgoing emails") [1609916](https://support.mozilla.org/questions/1609916 "Attach button dont work after updating to tb 157") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| proto:imap | 79 | 15 | ▼ -64 (-81%) |
| proto:pop | 62 | 8 | ▼ -54 (-87%) |
| m:gmail | 66 | 12 | ▼ -54 (-82%) |
| m:yahooemail | 60 | 8 | ▼ -52 (-87%) |
| m:microsoftemail | 66 | 14 | ▼ -52 (-79%) |
| proto:smtp | 53 | 7 | ▼ -46 (-87%) |
| proto:oauth | 27 | 3 | ▼ -24 (-89%) |
| feat:import_export | 23 | 1 | ▼ -22 (-96%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in October 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| v155 | 237 | 0 | ▼ -237 (-100%) |
| v153 | 193 | 37 | ▼ -156 (-81%) |
| v156 | 203 | 12 | ▼ -191 (-94%) |
| v157 | 3 | 77 | ▲ +74 |
| v140 | 44 | 8 | ▼ -36 (-82%) |
| v154 | 42 | 0 | ▼ -42 (-100%) |

### Operating-system mix

| Operating-system mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 814 | 154 | ▼ -660 (-81%) |
| os:linux | 62 | 11 | ▼ -51 (-82%) |
| os:macos | 62 | 4 | ▼ -58 (-94%) |
| os:other | 7 | 3 | ▼ -4 |
| os:android | 5 | 2 | ▼ -3 |

### Topic mix

| Topic mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 317 | 43 | ▼ -274 (-86%) |
| email-and-messaging | 84 | 10 | ▼ -74 (-88%) |
| customization | 71 | 13 | ▼ -58 (-82%) |
| attachments | 28 | 41 | ▲ +13 (+46%) |
| passwords-and-sign-in | 53 | 6 | ▼ -47 (-89%) |
| account-management | 50 | 5 | ▼ -45 (-90%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · October 2026 vs September 2026._

_Last updated: 2026-10-05 21:30 UTC_
