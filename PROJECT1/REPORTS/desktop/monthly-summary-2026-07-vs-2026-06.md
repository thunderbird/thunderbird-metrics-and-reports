---
layout: base
title: Desktop Engineering Support Summary — July 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## July 2026 vs June 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

## Headline

| | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 724 | 731 | ▲ +7 (+1%) |
| Version × cause spikes flagged | 3 | 0 | ▼ -3 |
| — of which **new** regressions | 2 | 0 | ▼ -2 |
| Cause-level surges flagged | 0 | 0 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

_No spikes flagged this month at current thresholds._

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| m:gmail | 52 | 73 | ▲ +21 (+40%) |
| m:microsoftemail | 54 | 36 | ▼ -18 (-33%) |
| m:spectrum | 20 | 5 | ▼ -15 (-75%) |
| proto:pop | 30 | 42 | ▲ +12 (+40%) |
| proto:smtp | 25 | 35 | ▲ +10 (+40%) |
| proto:oauth | 12 | 20 | ▲ +8 (+67%) |
| proto:imap | 51 | 56 | ▲ +5 (+10%) |
| m:yahooemail | 26 | 30 | ▲ +4 (+15%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in July 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| v152 | 158 | 211 | ▲ +53 (+34%) |
| v140 | 179 | 186 | ▲ +7 (+4%) |
| v151 | 189 | 4 | ▼ -185 (-98%) |
| v153 | 3 | 101 | ▲ +98 |
| v150 | 17 | 26 | ▲ +9 (+53%) |
| v115 | 26 | 16 | ▼ -10 (-38%) |

### Operating-system mix

| Operating-system mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 589 | ▬ 0 (+0%) |
| os:linux | 62 | 61 | ▼ -1 (-2%) |
| os:macos | 49 | 45 | ▼ -4 (-8%) |
| os:other | 11 | 11 | ▬ 0 (+0%) |
| os:android | 4 | 7 | ▲ +3 |

### Topic mix

| Topic mix | June 2026 | July 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 204 | 185 | ▼ -19 (-9%) |
| customization | 65 | 73 | ▲ +8 (+12%) |
| email-and-messaging | 49 | 82 | ▲ +33 (+67%) |
| passwords-and-sign-in | 32 | 53 | ▲ +21 (+66%) |
| connectivity | 34 | 25 | ▼ -9 (-26%) |
| import-and-export-email | 28 | 30 | ▲ +2 (+7%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · July 2026 vs June 2026._

_Last updated: 2026-08-04 08:56 UTC_
