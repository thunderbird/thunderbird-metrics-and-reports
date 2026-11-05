---
layout: base
title: Desktop Engineering Support Summary — November 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## November 2026 vs October 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **November 2026 is in progress** — data through day 5 of 30. Counts are partial, so the deltas below understate November 2026; treat volume changes as directional until the month closes.

## Headline

| | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 1030 | 121 | ▼ -909 (-88%) |
| Version × cause spikes flagged | 15 | 1 | ▼ -14 |
| — of which **new** regressions | 2 | 0 | ▼ -2 |
| Cause-level surges flagged | 3 | 0 | ▼ -3 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-11-01 | v159 × feat:calendar | 4 | 9.4× | ⚠️ 25% ans · 0.5h | [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615363](https://support.mozilla.org/questions/1615363 "TB 159 - Graph Calendar not automatically detected on account setup") [1615397](https://support.mozilla.org/questions/1615397 "Make Calendar Notification Window AlwaysOnTop") [1615399](https://support.mozilla.org/questions/1615399 "＂Thunderbird＂ access to Calendar functions are NOT FUNCTIONING at all. Thanks fo") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| feat:attachments | 106 | 0 | ▼ -106 (-100%) |
| m:gmail | 96 | 12 | ▼ -84 (-88%) |
| proto:imap | 82 | 11 | ▼ -71 (-87%) |
| m:microsoftemail | 60 | 6 | ▼ -54 (-90%) |
| m:yahooemail | 53 | 2 | ▼ -51 (-96%) |
| proto:pop | 55 | 6 | ▼ -49 (-89%) |
| proto:oauth | 32 | 2 | ▼ -30 (-94%) |
| proto:smtp | 36 | 8 | ▼ -28 (-78%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in November 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| v153 | 251 | 15 | ▼ -236 (-94%) |
| v157 | 262 | 1 | ▼ -261 (-100%) |
| v158 | 169 | 6 | ▼ -163 (-96%) |
| v159 | 48 | 58 | ▲ +10 (+21%) |
| v140 | 43 | 6 | ▼ -37 (-86%) |
| v115 | 19 | 2 | ▼ -17 (-89%) |

### Operating-system mix

| Operating-system mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 848 | 103 | ▼ -745 (-88%) |
| os:linux | 83 | 8 | ▼ -75 (-90%) |
| os:macos | 66 | 6 | ▼ -60 (-91%) |
| os:other | 9 | 0 | ▼ -9 |
| os:android | 8 | 0 | ▼ -8 |

### Topic mix

| Topic mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 246 | 27 | ▼ -219 (-89%) |
| attachments | 183 | 1 | ▼ -182 (-99%) |
| customization | 90 | 14 | ▼ -76 (-84%) |
| email-and-messaging | 88 | 12 | ▼ -76 (-86%) |
| passwords-and-sign-in | 46 | 4 | ▼ -42 (-91%) |
| account-management | 38 | 8 | ▼ -30 (-79%) |

---

_Prototype engineering month-over-month summary · from SUMO Spike Detector feature tables + spike detectors · November 2026 vs October 2026._

_Last updated: 2026-11-05 08:05 UTC_
