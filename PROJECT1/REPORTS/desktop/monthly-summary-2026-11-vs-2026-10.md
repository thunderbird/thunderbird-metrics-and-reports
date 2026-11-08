---
layout: base
title: Desktop Engineering Support Summary — November 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## November 2026 vs October 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **November 2026 is in progress** — data through day 8 of 30. Counts are partial, so the deltas below understate November 2026; treat volume changes as directional until the month closes.

## Headline

| | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 1030 | 194 | ▼ -836 (-81%) |
| Version × cause spikes flagged | 15 | 2 | ▼ -13 |
| — of which **new** regressions | 2 | 0 | ▼ -2 |
| Cause-level surges flagged | 3 | 0 | ▼ -3 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-11-01 | v159 × feat:calendar | 4 | 8.7× | ⚠️ 25% ans · 0.5h | [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615363](https://support.mozilla.org/questions/1615363 "TB 159 - Graph Calendar not automatically detected on account setup") [1615397](https://support.mozilla.org/questions/1615397 "Make Calendar Notification Window AlwaysOnTop") [1615399](https://support.mozilla.org/questions/1615399 "＂Thunderbird＂ access to Calendar functions are NOT FUNCTIONING at all. Thanks fo") |
| ↗ spreading | 2026-11-05 | v159 × m:gmail | 4 | 3.1× | ⚠️ 50% ans · 5.5h | [1616042](https://support.mozilla.org/questions/1616042 "How do I unsync my old email account that no longer exists from Thunderbird?") [1616054](https://support.mozilla.org/questions/1616054 "About the Gmail Data Transfer to Thunderbird") [1616142](https://support.mozilla.org/questions/1616142 "Google Caldav: Microsoft meeting notices stored locally but not on Google calend") [1616165](https://support.mozilla.org/questions/1616165 "One email account will not open.") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| feat:attachments | 106 | 1 | ▼ -105 (-99%) |
| m:gmail | 96 | 18 | ▼ -78 (-81%) |
| proto:imap | 82 | 22 | ▼ -60 (-73%) |
| m:yahooemail | 53 | 3 | ▼ -50 (-94%) |
| m:microsoftemail | 60 | 10 | ▼ -50 (-83%) |
| proto:pop | 55 | 10 | ▼ -45 (-82%) |
| proto:oauth | 32 | 5 | ▼ -27 (-84%) |
| m:att | 28 | 2 | ▼ -26 (-93%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in November 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| v153 | 251 | 34 | ▼ -217 (-86%) |
| v157 | 262 | 2 | ▼ -260 (-99%) |
| v158 | 169 | 7 | ▼ -162 (-96%) |
| v159 | 48 | 92 | ▲ +44 (+92%) |
| v140 | 43 | 7 | ▼ -36 (-84%) |
| v115 | 19 | 5 | ▼ -14 (-74%) |

### Operating-system mix

| Operating-system mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 848 | 165 | ▼ -683 (-81%) |
| os:linux | 83 | 17 | ▼ -66 (-80%) |
| os:macos | 66 | 7 | ▼ -59 (-89%) |
| os:other | 9 | 0 | ▼ -9 |
| os:android | 8 | 0 | ▼ -8 |

### Topic mix

| Topic mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 246 | 45 | ▼ -201 (-82%) |
| attachments | 183 | 1 | ▼ -182 (-99%) |
| customization | 90 | 21 | ▼ -69 (-77%) |
| email-and-messaging | 88 | 18 | ▼ -70 (-80%) |
| passwords-and-sign-in | 46 | 8 | ▼ -38 (-83%) |
| account-management | 38 | 14 | ▼ -24 (-63%) |

---

_Prototype engineering month-over-month summary · from SUMO Spike Detector feature tables + spike detectors · November 2026 vs October 2026._

_Last updated: 2026-11-08 08:05 UTC_
