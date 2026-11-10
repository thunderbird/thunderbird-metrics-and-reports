---
layout: base
title: Desktop Engineering Support Summary — November 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## November 2026 vs October 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **November 2026 is in progress** — data through day 10 of 30. Counts are partial, so the deltas below understate November 2026; treat volume changes as directional until the month closes.

## Headline

| | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 1030 | 269 | ▼ -761 (-74%) |
| Version × cause spikes flagged | 15 | 3 | ▼ -12 |
| — of which **new** regressions | 2 | 0 | ▼ -2 |
| Cause-level surges flagged | 3 | 0 | ▼ -3 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-11-01 | v159 × feat:calendar | 4 | 8.8× | ⚠️ 25% ans · 0.5h | [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615363](https://support.mozilla.org/questions/1615363 "TB 159 - Graph Calendar not automatically detected on account setup") [1615397](https://support.mozilla.org/questions/1615397 "Make Calendar Notification Window AlwaysOnTop") [1615399](https://support.mozilla.org/questions/1615399 "＂Thunderbird＂ access to Calendar functions are NOT FUNCTIONING at all. Thanks fo") |
| ↗ spreading | 2026-11-10 | v153 × m:gmail | 5 | 7.8× | ⚠️ 20% ans · 3.8h | [1617146](https://support.mozilla.org/questions/1617146 "I have one email that will not allow other emails to forward to it (inbox doesn'") [1617152](https://support.mozilla.org/questions/1617152 "Thunderbird cannot send emails from multiple accounts – SMTP timeouts and OAuth2") [1617168](https://support.mozilla.org/questions/1617168 "email scomparse") [1617219](https://support.mozilla.org/questions/1617219 "missing emails") [1617255](https://support.mozilla.org/questions/1617255 "su un PC non scarico più la posta di una casella Aruba e di una casella Gmail") |
| ↗ spreading | 2026-11-05 | v159 × m:gmail | 4 | 3.1× | ⚠️ 50% ans · 5.5h | [1616042](https://support.mozilla.org/questions/1616042 "How do I unsync my old email account that no longer exists from Thunderbird?") [1616054](https://support.mozilla.org/questions/1616054 "About the Gmail Data Transfer to Thunderbird") [1616142](https://support.mozilla.org/questions/1616142 "Google Caldav: Microsoft meeting notices stored locally but not on Google calend") [1616165](https://support.mozilla.org/questions/1616165 "One email account will not open.") |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| feat:attachments | 106 | 1 | ▼ -105 (-99%) |
| m:gmail | 96 | 29 | ▼ -67 (-70%) |
| proto:imap | 82 | 26 | ▼ -56 (-68%) |
| m:microsoftemail | 60 | 13 | ▼ -47 (-78%) |
| m:yahooemail | 53 | 9 | ▼ -44 (-83%) |
| proto:pop | 55 | 13 | ▼ -42 (-76%) |
| m:att | 28 | 2 | ▼ -26 (-93%) |
| proto:oauth | 32 | 8 | ▼ -24 (-75%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in November 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| v153 | 251 | 53 | ▼ -198 (-79%) |
| v157 | 262 | 2 | ▼ -260 (-99%) |
| v158 | 169 | 10 | ▼ -159 (-94%) |
| v159 | 48 | 129 | ▲ +81 (+169%) |
| v140 | 43 | 9 | ▼ -34 (-79%) |
| v115 | 19 | 6 | ▼ -13 (-68%) |

### Operating-system mix

| Operating-system mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 848 | 222 | ▼ -626 (-74%) |
| os:linux | 83 | 26 | ▼ -57 (-69%) |
| os:macos | 66 | 14 | ▼ -52 (-79%) |
| os:android | 8 | 2 | ▼ -6 |
| os:other | 9 | 0 | ▼ -9 |

### Topic mix

| Topic mix | October 2026 | November 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 246 | 69 | ▼ -177 (-72%) |
| attachments | 183 | 1 | ▼ -182 (-99%) |
| customization | 90 | 27 | ▼ -63 (-70%) |
| email-and-messaging | 88 | 28 | ▼ -60 (-68%) |
| passwords-and-sign-in | 46 | 10 | ▼ -36 (-78%) |
| account-management | 38 | 17 | ▼ -21 (-55%) |

---

_Prototype engineering month-over-month summary · from SUMO Spike Detector feature tables + spike detectors · November 2026 vs October 2026._

_Last updated: 2026-11-10 20:05 UTC_
