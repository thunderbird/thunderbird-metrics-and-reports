---
layout: base
title: Desktop Engineering Support Summary — October 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## October 2026 vs September 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **October 2026 is in progress** — data through day 4 of 31. Counts are partial, so the deltas below understate October 2026; treat volume changes as directional until the month closes.

## Headline

| | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 974 | 126 | ▼ -848 (-87%) |
| Version × cause spikes flagged | 5 | 1 | ▼ -4 |
| — of which **new** regressions | 2 | 1 | ▼ -1 |
| Cause-level surges flagged | 1 | 0 | ▼ -1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| 🆕 new | 2026-10-04 | v157 × feat:attachments | 4 | 13.7× | ⚠️ 50% ans · 0.9h | [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") [1609601](https://support.mozilla.org/questions/1609601 "Change the app that opens email attachments") [1609642](https://support.mozilla.org/questions/1609642 "Attach button does not respond. Drag and Drop works. (bug2077590)") [1609643](https://support.mozilla.org/questions/1609643 "email beantwoorden, bijlage knop werkt niet") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| proto:imap | 79 | 10 | ▼ -69 (-87%) |
| proto:pop | 62 | 6 | ▼ -56 (-90%) |
| m:gmail | 66 | 11 | ▼ -55 (-83%) |
| m:microsoftemail | 66 | 11 | ▼ -55 (-83%) |
| m:yahooemail | 60 | 6 | ▼ -54 (-90%) |
| proto:smtp | 53 | 7 | ▼ -46 (-87%) |
| proto:oauth | 27 | 1 | ▼ -26 (-96%) |
| feat:import_export | 23 | 0 | ▼ -23 (-100%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in October 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| v155 | 237 | 0 | ▼ -237 (-100%) |
| v153 | 193 | 26 | ▼ -167 (-87%) |
| v156 | 203 | 12 | ▼ -191 (-94%) |
| v157 | 3 | 54 | ▲ +51 |
| v140 | 44 | 4 | ▼ -40 (-91%) |
| v154 | 42 | 0 | ▼ -42 (-100%) |

### Operating-system mix

| Operating-system mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 814 | 112 | ▼ -702 (-86%) |
| os:linux | 62 | 9 | ▼ -53 (-85%) |
| os:macos | 62 | 2 | ▼ -60 (-97%) |
| os:other | 7 | 1 | ▼ -6 |
| os:android | 5 | 1 | ▼ -4 |

### Topic mix

| Topic mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 317 | 36 | ▼ -281 (-89%) |
| email-and-messaging | 84 | 6 | ▼ -78 (-93%) |
| customization | 71 | 10 | ▼ -61 (-86%) |
| passwords-and-sign-in | 53 | 5 | ▼ -48 (-91%) |
| attachments | 28 | 28 | ▬ 0 (+0%) |
| account-management | 50 | 5 | ▼ -45 (-90%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · October 2026 vs September 2026._

_Last updated: 2026-10-04 20:42 UTC_
