---
layout: base
title: Desktop Engineering Support Summary — August 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## August 2026 vs July 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

## Headline

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 941 | ▲ +210 (+29%) |
| Version × cause spikes flagged | 0 | 4 | ▲ +4 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 0 | 1 | ▲ +1 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| ↗ spreading | 2026-08-10 | v153 × proto:pop | 4 | 3.3× | 75% ans · 1.1h | [1597551](https://support.mozilla.org/questions/1597551 "Thunderbird POP stopped retrieving email from one mail box, No error message") [1597571](https://support.mozilla.org/questions/1597571 "Email collection over pop failed on one account, server settings rejected when I") [1597638](https://support.mozilla.org/questions/1597638 "How logging onto wowway with old password?") [1597683](https://support.mozilla.org/questions/1597683 "Hotmail personal account: IMAP OAuth2 works but SMTP OAuth2 fails with message: ") |
| ↗ spreading | 2026-08-04 | v153 × m:microsoftemail | 5 | 3.2× | 100% ans · 0.8h | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") |
| ↻ recurring | 2026-08-14 | v153 × proto:pop | 4 | 3.5× | 100% ans · 8.0h | [1598311](https://support.mozilla.org/questions/1598311 "Thunderbird went goofy for multiple gmail accounts - deleted email does not show") [1598314](https://support.mozilla.org/questions/1598314 "Email from Roadrunner.com does not show but server test works") [1598327](https://support.mozilla.org/questions/1598327 "Unable to receive e-mail") [1598357](https://support.mozilla.org/questions/1598357 "Recently Unable to send (SMTP) from Thunderbird from Cox.com (now thru Yahoo).") |
| ↻ recurring | 2026-08-13 | v153 × proto:pop | 4 | 3.3× | 100% ans · 1.2h | [1598091](https://support.mozilla.org/questions/1598091 "thunderbird has stopped receiving emails from century link") [1598146](https://support.mozilla.org/questions/1598146 "Can't access my account") [1598151](https://support.mozilla.org/questions/1598151 "How to set up automatic email forwarding from Thunderbird to Gmail") [1598175](https://support.mozilla.org/questions/1598175 "Thunderbird won't download email messages from Yahoo (formerly Cox) account") |

### Cause-level surges — provider / protocol / AV (any version)

Version-agnostic (a provider outage spans versions), vs a trailing-month baseline.

| Cause | Qs | Served | vs baseline | Rise | Example questions |
|:--|--:|:--|--:|:--|:--|
| m:spectrum | 34 | 79% ans · 3.7h | 10.5 | 3.24× | [1596316](https://support.mozilla.org/questions/1596316 "Thunderbird 1 of 7  email account stopped working from the Provider Spectrum and") [1596807](https://support.mozilla.org/questions/1596807 "Receiving, deleting, and sending messages is extremely slow for 1 of 2 users on ") [1597319](https://support.mozilla.org/questions/1597319 "thunderbird not able to access mail.twc.com") [1597495](https://support.mozilla.org/questions/1597495 "NO longer have Spectrum as email provider but need to preserve emails .") [1597964](https://support.mozilla.org/questions/1597964 "Roadrunner / TWC IMAP settings") +29 |

## What moved

### Cause clusters (provider / protocol / AV)

| Cause clusters (provider / protocol / AV) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| m:spectrum | 5 | 34 | ▲ +29 |
| m:yahooemail | 30 | 55 | ▲ +25 (+83%) |
| m:microsoftemail | 36 | 53 | ▲ +17 (+47%) |
| proto:imap | 56 | 70 | ▲ +14 (+25%) |
| proto:smtp | 35 | 44 | ▲ +9 (+26%) |
| proto:pop | 42 | 46 | ▲ +4 (+10%) |
| m:gmail | 73 | 75 | ▲ +2 (+3%) |
| proto:oauth | 20 | 19 | ▼ -1 (-5%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in August 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| v153 | 101 | 441 | ▲ +340 (+337%) |
| v140 | 186 | 67 | ▼ -119 (-64%) |
| v152 | 211 | 6 | ▼ -205 (-97%) |
| v154 | 2 | 202 | ▲ +200 |
| v150 | 26 | 25 | ▼ -1 (-4%) |
| v115 | 16 | 24 | ▲ +8 (+50%) |

### Operating-system mix

| Operating-system mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 589 | 750 | ▲ +161 (+27%) |
| os:linux | 61 | 93 | ▲ +32 (+52%) |
| os:macos | 45 | 59 | ▲ +14 (+31%) |
| os:other | 11 | 6 | ▼ -5 (-45%) |
| os:android | 7 | 10 | ▲ +3 |

### Topic mix

| Topic mix | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 185 | 233 | ▲ +48 (+26%) |
| email-and-messaging | 82 | 80 | ▼ -2 (-2%) |
| customization | 73 | 86 | ▲ +13 (+18%) |
| passwords-and-sign-in | 53 | 60 | ▲ +7 (+13%) |
| connectivity | 25 | 48 | ▲ +23 (+92%) |
| import-and-export-email | 30 | 35 | ▲ +5 (+17%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · August 2026 vs July 2026._

_Last updated: 2026-09-02 08:08 UTC_
