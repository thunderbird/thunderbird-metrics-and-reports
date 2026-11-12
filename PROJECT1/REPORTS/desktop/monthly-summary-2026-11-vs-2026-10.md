---
layout: base
title: Desktop Engineering Support Summary — November 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## November 2026 vs October 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **November 2026 is in progress** — data through day 12 of 30. Counts are partial, so the deltas below understate November 2026; treat volume changes as directional until the month closes.

## Headline

| | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 1030 | 332 | ▼ -698 (-68%) |
| Version × cause spikes flagged | 15 | 3 | ▼ -12 |
| — of which **new** regressions | 2 | 0 | ▼ -2 |
| Cause-level surges flagged | 3 | 0 | ▼ -3 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-11-01 | v159 × feat:calendar | 4 | 8.9× | ⚠️ 25% ans · 0.5h | [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615363](https://support.mozilla.org/questions/1615363 "TB 159 - Graph Calendar not automatically detected on account setup") [1615397](https://support.mozilla.org/questions/1615397 "Make Calendar Notification Window AlwaysOnTop") [1615399](https://support.mozilla.org/questions/1615399 "＂Thunderbird＂ access to Calendar functions are NOT FUNCTIONING at all. Thanks fo") |
| ↗ spreading | 2026-11-10 | v153 × m:gmail | 5 | 6.0× | ⚠️ 40% ans · 2.0h | [1617146](https://support.mozilla.org/questions/1617146 "I have one email that will not allow other emails to forward to it (inbox doesn'") [1617152](https://support.mozilla.org/questions/1617152 "Thunderbird cannot send emails from multiple accounts – SMTP timeouts and OAuth2") [1617168](https://support.mozilla.org/questions/1617168 "email scomparse") [1617219](https://support.mozilla.org/questions/1617219 "missing emails") [1617255](https://support.mozilla.org/questions/1617255 "su un PC non scarico più la posta di una casella Aruba e di una casella Gmail") |
| ↗ spreading | 2026-11-05 | v159 × m:gmail | 4 | 3.1× | 75% ans · 8.4h | [1616042](https://support.mozilla.org/questions/1616042 "How do I unsync my old email account that no longer exists from Thunderbird?") [1616054](https://support.mozilla.org/questions/1616054 "About the Gmail Data Transfer to Thunderbird") [1616142](https://support.mozilla.org/questions/1616142 "Google Caldav: Microsoft meeting notices stored locally but not on Google calend") [1616165](https://support.mozilla.org/questions/1616165 "One email account will not open.") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| feat:attachments | 106 | 1 | ▼ -105 (-99%) |
| m:gmail | 96 | 39 | ▼ -57 (-59%) |
| proto:imap | 82 | 33 | ▼ -49 (-60%) |
| m:yahooemail | 53 | 11 | ▼ -42 (-79%) |
| m:microsoftemail | 60 | 18 | ▼ -42 (-70%) |
| proto:pop | 55 | 16 | ▼ -39 (-71%) |
| m:att | 28 | 2 | ▼ -26 (-93%) |
| proto:oauth | 32 | 10 | ▼ -22 (-69%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in November 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| v153 | 251 | 70 | ▼ -181 (-72%) |
| v157 | 262 | 3 | ▼ -259 (-99%) |
| v159 | 48 | 142 | ▲ +94 (+196%) |
| v158 | 169 | 10 | ▼ -159 (-94%) |
| v140 | 43 | 18 | ▼ -25 (-58%) |
| v115 | 19 | 6 | ▼ -13 (-68%) |

### Operating-system mix

| Operating-system mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 848 | 271 | ▼ -577 (-68%) |
| os:linux | 83 | 32 | ▼ -51 (-61%) |
| os:macos | 66 | 20 | ▼ -46 (-70%) |
| os:android | 8 | 3 | ▼ -5 |
| os:other | 9 | 1 | ▼ -8 |

### Topic mix

| Topic mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 246 | 80 | ▼ -166 (-67%) |
| attachments | 183 | 1 | ▼ -182 (-99%) |
| email-and-messaging | 88 | 32 | ▼ -56 (-64%) |
| customization | 90 | 30 | ▼ -60 (-67%) |
| account-management | 38 | 25 | ▼ -13 (-34%) |
| passwords-and-sign-in | 46 | 15 | ▼ -31 (-67%) |

---

_Prototype engineering month-over-month summary · from SUMO Spike Detector feature tables + spike detectors · November 2026 vs October 2026._

_Last updated: 2026-11-12 20:04 UTC_
