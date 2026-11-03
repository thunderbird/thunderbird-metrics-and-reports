---
layout: base
title: Desktop Engineering Support Summary — November 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## November 2026 vs October 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **November 2026 is in progress** — data through day 3 of 30. Counts are partial, so the deltas below understate November 2026; treat volume changes as directional until the month closes.

## Headline

| | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 1030 | 76 | ▼ -954 (-93%) |
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
| m:gmail | 96 | 6 | ▼ -90 (-94%) |
| proto:imap | 82 | 7 | ▼ -75 (-91%) |
| m:microsoftemail | 60 | 5 | ▼ -55 (-92%) |
| proto:pop | 55 | 4 | ▼ -51 (-93%) |
| m:yahooemail | 53 | 2 | ▼ -51 (-96%) |
| proto:smtp | 36 | 6 | ▼ -30 (-83%) |
| proto:oauth | 31 | 2 | ▼ -29 (-94%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in November 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| v157 | 262 | 1 | ▼ -261 (-100%) |
| v153 | 251 | 7 | ▼ -244 (-97%) |
| v158 | 169 | 4 | ▼ -165 (-98%) |
| v159 | 48 | 40 | ▼ -8 (-17%) |
| v140 | 43 | 5 | ▼ -38 (-88%) |
| v115 | 19 | 2 | ▼ -17 (-89%) |

### Operating-system mix

| Operating-system mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 848 | 65 | ▼ -783 (-92%) |
| os:linux | 83 | 5 | ▼ -78 (-94%) |
| os:macos | 66 | 4 | ▼ -62 (-94%) |
| os:other | 9 | 0 | ▼ -9 |
| os:android | 8 | 0 | ▼ -8 |

### Topic mix

| Topic mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 246 | 18 | ▼ -228 (-93%) |
| attachments | 183 | 1 | ▼ -182 (-99%) |
| customization | 90 | 10 | ▼ -80 (-89%) |
| email-and-messaging | 88 | 7 | ▼ -81 (-92%) |
| passwords-and-sign-in | 46 | 3 | ▼ -43 (-93%) |
| account-management | 38 | 4 | ▼ -34 (-89%) |

---

_Prototype engineering month-over-month summary · from SUMO Spike Detector feature tables + spike detectors · November 2026 vs October 2026._

_Last updated: 2026-11-03 18:26 UTC_
