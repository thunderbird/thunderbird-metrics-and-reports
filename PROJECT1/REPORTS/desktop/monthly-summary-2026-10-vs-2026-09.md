---
layout: base
title: Desktop Engineering Support Summary — October 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## October 2026 vs September 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **October 2026 is in progress** — data through day 7 of 31. Counts are partial, so the deltas below understate October 2026; treat volume changes as directional until the month closes.

## Headline

| | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 976 | 304 | ▼ -672 (-69%) |
| Version × cause spikes flagged | 5 | 7 | ▲ +2 |
| — of which **new** regressions | 2 | 2 | ▬ 0 |
| Cause-level surges flagged | 1 | 1 | ▬ 0 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| 🆕 new | 2026-10-06 | v140 × m:att | 4 | 111.0× | ⚠️ 50% ans · 1.4h | [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") [1610258](https://support.mozilla.org/questions/1610258 "The certificate for inbound.att.net does not come from a trusted source.") [1610259](https://support.mozilla.org/questions/1610259 "Why Thunderbird on Linux will no longer connect to att.net email with POP3.") [1610309](https://support.mozilla.org/questions/1610309 "AOL setup on MX Linux... fails authentication") |
| 🆕 new | 2026-10-04 | v157 × feat:attachments | 5 | 9.1× | 100% ans · 12.1h | [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") [1609601](https://support.mozilla.org/questions/1609601 "Change the app that opens email attachments") [1609642](https://support.mozilla.org/questions/1609642 "Attach button does not respond. Drag and Drop works. (bug2077590)") [1609643](https://support.mozilla.org/questions/1609643 "email beantwoorden, bijlage knop werkt niet") [1609719](https://support.mozilla.org/questions/1609719 "Unable to attach files to email") |
| ↗ spreading | 2026-10-05 | v153 × feat:attachments | 6 | 13.9× | 83% ans · 0.6h | [1609864](https://support.mozilla.org/questions/1609864 "allegati che non si possono più inserire nell'email") [1609904](https://support.mozilla.org/questions/1609904 "Unable to attach a document to a return email") [1609918](https://support.mozilla.org/questions/1609918 "allegati") [1609979](https://support.mozilla.org/questions/1609979 "why can't i attach files to sent email?") [1609986](https://support.mozilla.org/questions/1609986 "not launching file explorer to attach files") +1 |
| ↻ recurring | 2026-10-07 | v153 × feat:attachments | 4 | 10.7× | 75% ans · 0.3h | [1610392](https://support.mozilla.org/questions/1610392 "Recurring Issue with Attachment Button in Thunderbird Desktop") [1610416](https://support.mozilla.org/questions/1610416 "sinds de update 153.4.0esr van 05 oktober kan ik geen bijlagen meer koppelen aan") [1610444](https://support.mozilla.org/questions/1610444 "Thunderbird has stopped to include attachments via key. Only drag and drop funct") [1610449](https://support.mozilla.org/questions/1610449 "A problem with sending attachments with an email") |
| ↻ recurring | 2026-10-06 | v153 × feat:attachments | 5 | 7.5× | 80% ans · 0.9h | [1610087](https://support.mozilla.org/questions/1610087 "Email attachment - version 153.4.0esr") [1610100](https://support.mozilla.org/questions/1610100 "unable to attach desktop files to outgoing emails when attachment function activ") [1610118](https://support.mozilla.org/questions/1610118 "All of a sudden Thunderbird won't let me attach images") [1610206](https://support.mozilla.org/questions/1610206 "I have lost the attach file link since last up date") [1610244](https://support.mozilla.org/questions/1610244 "I can't add any attachments. The button doesn't work") |
| ↻ recurring | 2026-10-06 | v157 × feat:attachments | 5 | 6.2× | 100% ans · 0.9h | [1610097](https://support.mozilla.org/questions/1610097 "Since that last update I can no longer attach files to emails. Can You help?") [1610225](https://support.mozilla.org/questions/1610225 "Suddenly I can neither attach nor insert files into an outgoing email.") [1610267](https://support.mozilla.org/questions/1610267 "Attach File no longer Works as of 10/05 W11") [1610268](https://support.mozilla.org/questions/1610268 "Unable to attach files to emails (the ‘Attachments’ button does not respond)./ A") [1610276](https://support.mozilla.org/questions/1610276 "Attach button not working on new emails") |
| ↻ recurring | 2026-10-05 | v157 × feat:attachments | 4 | 5.8× | 100% ans · 5.4h | [1609825](https://support.mozilla.org/questions/1609825 "nach dem letzten Update kann ich keine Attachments versenden") [1609880](https://support.mozilla.org/questions/1609880 "I cannot add an attachment, when I press the attachment button nothing happens") [1609897](https://support.mozilla.org/questions/1609897 "The 'Attach' button does not respond to outgoing emails") [1609916](https://support.mozilla.org/questions/1609916 "Attach button dont work after updating to tb 157") |

### Cause-level surges — provider / protocol / AV / feature (any version)

Version-agnostic (a provider outage spans versions), vs a trailing-month baseline.

| Cause | Qs | Served | vs baseline | Rise | Example questions |
|:--|--:|:--|--:|:--|:--|
| m:att | 18 | ⚠️ 33% ans · 2.4h | 4.0 | 4.5× | [1609929](https://support.mozilla.org/questions/1609929 "＂We've identified a site certificate problem＂") [1609983](https://support.mozilla.org/questions/1609983 "I cannot bring mail from AT&T  into my Thunderbird app on my home computer, what") [1610002](https://support.mozilla.org/questions/1610002 "'Digicert Global G2' revoked Oct 5, 2026") [1610037](https://support.mozilla.org/questions/1610037 "Thunderbird suddenly stopped receiving AT&T email ?") [1610152](https://support.mozilla.org/questions/1610152 "Certificate revoked for inbound.att.net?  What do we do?") +13 |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| proto:imap | 79 | 22 | ▼ -57 (-72%) |
| m:microsoftemail | 67 | 16 | ▼ -51 (-76%) |
| proto:pop | 62 | 13 | ▼ -49 (-79%) |
| m:yahooemail | 60 | 13 | ▼ -47 (-78%) |
| m:gmail | 66 | 21 | ▼ -45 (-68%) |
| proto:smtp | 53 | 11 | ▼ -42 (-79%) |
| feat:attachments | 20 | 43 | ▲ +23 (+115%) |
| proto:oauth | 27 | 5 | ▼ -22 (-81%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in October 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| v153 | 193 | 78 | ▼ -115 (-60%) |
| v155 | 239 | 0 | ▼ -239 (-100%) |
| v156 | 203 | 14 | ▼ -189 (-93%) |
| v157 | 3 | 131 | ▲ +128 |
| v140 | 44 | 15 | ▼ -29 (-66%) |
| v154 | 42 | 0 | ▼ -42 (-100%) |

### Operating-system mix

| Operating-system mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 815 | 262 | ▼ -553 (-68%) |
| os:linux | 63 | 19 | ▼ -44 (-70%) |
| os:macos | 62 | 13 | ▼ -49 (-79%) |
| os:other | 7 | 4 | ▼ -3 |
| os:android | 5 | 2 | ▼ -3 |

### Topic mix

| Topic mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 317 | 68 | ▼ -249 (-79%) |
| attachments | 28 | 87 | ▲ +59 (+211%) |
| email-and-messaging | 85 | 18 | ▼ -67 (-79%) |
| customization | 71 | 23 | ▼ -48 (-68%) |
| passwords-and-sign-in | 54 | 12 | ▼ -42 (-78%) |
| connectivity | 50 | 8 | ▼ -42 (-84%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · October 2026 vs September 2026._

_Last updated: 2026-10-07 20:08 UTC_
