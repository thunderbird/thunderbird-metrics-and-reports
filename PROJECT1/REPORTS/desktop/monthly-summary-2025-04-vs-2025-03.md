---
layout: base
title: Desktop Engineering Support Summary — April 2025
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## April 2025 vs March 2025

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

## Headline

| | March 2025 | April 2025 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 1221 | 1173 | ▼ -48 (-4%) |
| Version × cause spikes flagged | 0 | 0 | ▬ 0 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 0 | 1 | ▲ +1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Cause-level surges — provider / protocol / AV / feature (any version)

Version-agnostic (a provider outage spans versions), vs a trailing-month baseline.

| Cause | Qs | Served | vs baseline | Rise | Example questions |
|:--|--:|:--|--:|:--|:--|
| feat:printing | 24 | 83% ans · 2.8h | 8.0 | 3.0× | [1503165](https://support.mozilla.org/questions/1503165 "How to print out a single Thunderbird calendar event") [1504181](https://support.mozilla.org/questions/1504181 "Printing Calendars from Thunderbird - Team Events with extra data") [1504337](https://support.mozilla.org/questions/1504337 "problemi stampa pdf") [1504385](https://support.mozilla.org/questions/1504385 "no pdf print - the system informs that there is no associated mail program in wi") [1504522](https://support.mozilla.org/questions/1504522 "Attachments to a message will not be printed directly from Thunderbird.") +19 |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | March 2025 | April 2025 | Change |
|:--|--:|--:|:--|
| feat:attachments | 13 | 32 | ▲ +19 (+146%) |
| feat:calendar | 55 | 36 | ▼ -19 (-35%) |
| m:microsoftemail | 84 | 69 | ▼ -15 (-18%) |
| feat:printing | 9 | 24 | ▲ +15 |
| proto:pop | 41 | 54 | ▲ +13 (+32%) |
| proto:imap | 68 | 81 | ▲ +13 (+19%) |
| feat:junk | 20 | 29 | ▲ +9 (+45%) |
| feat:import_export | 25 | 33 | ▲ +8 (+32%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in April 2025 has appeared in a prior month._

### Operating-system mix

| Operating-system mix | March 2025 | April 2025 | Change |
|:--|--:|--:|:--|
| os:windows | 132 | 150 | ▲ +18 (+14%) |
| os:linux | 28 | 37 | ▲ +9 (+32%) |
| os:macos | 21 | 19 | ▼ -2 (-10%) |
| os:android | 2 | 2 | ▬ 0 |
| os:other | 2 | 1 | ▼ -1 |

### Topic mix

| Topic mix | March 2025 | April 2025 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 344 | 328 | ▼ -16 (-5%) |
| customization | 155 | 146 | ▼ -9 (-6%) |
| email-and-messaging | 106 | 96 | ▼ -10 (-9%) |
| import-and-export-email | 55 | 53 | ▼ -2 (-4%) |
| passwords-and-sign-in | 54 | 45 | ▼ -9 (-17%) |
| connectivity | 42 | 49 | ▲ +7 (+17%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · April 2025 vs March 2025._

_Last updated: 2026-09-10 00:28 UTC_
