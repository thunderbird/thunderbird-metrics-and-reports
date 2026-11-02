---
layout: base
title: Desktop Engineering Support Summary — November 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## November 2026 vs October 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **November 2026 is in progress** — data through day 2 of 30. Counts are partial, so the deltas below understate November 2026; treat volume changes as directional until the month closes.

## Headline

| | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 1030 | 40 | ▼ -990 (-96%) |
| Version × cause spikes flagged | 15 | 1 | ▼ -14 |
| — of which **new** regressions | 2 | 0 | ▼ -2 |
| Cause-level surges flagged | 3 | 0 | ▼ -3 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-11-01 | v159 × feat:calendar | 4 | 9.5× | ⚠️ 25% ans · 0.5h | [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615363](https://support.mozilla.org/questions/1615363 "TB 159 - Graph Calendar not automatically detected on account setup") [1615397](https://support.mozilla.org/questions/1615397 "Make Calendar Notification Window AlwaysOnTop") [1615399](https://support.mozilla.org/questions/1615399 "＂Thunderbird＂ access to Calendar functions are NOT FUNCTIONING at all. Thanks fo") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| feat:attachments | 106 | 0 | ▼ -106 (-100%) |
| m:gmail | 96 | 3 | ▼ -93 (-97%) |
| proto:imap | 82 | 2 | ▼ -80 (-98%) |
| m:microsoftemail | 60 | 2 | ▼ -58 (-97%) |
| proto:pop | 55 | 1 | ▼ -54 (-98%) |
| m:yahooemail | 53 | 0 | ▼ -53 (-100%) |
| proto:smtp | 36 | 4 | ▼ -32 (-89%) |
| proto:oauth | 31 | 1 | ▼ -30 (-97%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in November 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| v157 | 262 | 0 | ▼ -262 (-100%) |
| v153 | 251 | 5 | ▼ -246 (-98%) |
| v158 | 169 | 1 | ▼ -168 (-99%) |
| v159 | 48 | 21 | ▼ -27 (-56%) |
| v140 | 43 | 3 | ▼ -40 (-93%) |
| v115 | 19 | 2 | ▼ -17 (-89%) |

### Operating-system mix

| Operating-system mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 848 | 32 | ▼ -816 (-96%) |
| os:linux | 83 | 3 | ▼ -80 (-96%) |
| os:macos | 66 | 4 | ▼ -62 (-94%) |
| os:other | 9 | 0 | ▼ -9 |
| os:android | 8 | 0 | ▼ -8 |

### Topic mix

| Topic mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 246 | 8 | ▼ -238 (-97%) |
| attachments | 183 | 1 | ▼ -182 (-99%) |
| customization | 90 | 4 | ▼ -86 (-96%) |
| email-and-messaging | 88 | 4 | ▼ -84 (-95%) |
| passwords-and-sign-in | 46 | 2 | ▼ -44 (-96%) |
| account-management | 38 | 3 | ▼ -35 (-92%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · November 2026 vs October 2026._

_Last updated: 2026-11-02 20:04 UTC_
