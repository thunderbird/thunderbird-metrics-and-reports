---
layout: base
title: Desktop Engineering Support Summary — October 2023
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## October 2023 vs September 2023

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

## Headline

| | September 2023 | October 2023 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 1328 | 1977 | ▲ +649 (+49%) |
| Version × cause spikes flagged | 0 | 0 | ▬ 0 |
| — of which **new** regressions | 0 | 0 | ▬ 0 |
| Cause-level surges flagged | 1 | 3 | ▲ +2 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Cause-level surges — provider / protocol / AV / feature (any version)

Version-agnostic (a provider outage spans versions), vs a trailing-month baseline.

| Cause | Qs | Served | vs baseline | Rise | Example questions |
|:--|--:|:--|--:|:--|:--|
| m:frontier | 15 | ⚠️ 53% ans · 7.9h | 0.5 | 30.0× | [1426135](https://support.mozilla.org/questions/1426135 "Email not working after update to SuperNova?  Multiple - gmail, dreamhost, front") [1426500](https://support.mozilla.org/questions/1426500 "Thunderbird Version	119.0b3 - hangs") [1426532](https://support.mozilla.org/questions/1426532 "Thunderbird downloading messages from frontier.com") [1426537](https://support.mozilla.org/questions/1426537 "using Frontier.com for email.  TB v 102 stopped working yesterday.  Updated to v") [1426556](https://support.mozilla.org/questions/1426556 "Tbird 115.2.1 stopped downloading emails on all accounts.") +10 |
| feat:search | 34 | 68% ans · 4.3h | 7.5 | 4.53× | [1426165](https://support.mozilla.org/questions/1426165 "Ricerca messaggi funziona male") [1426197](https://support.mozilla.org/questions/1426197 "Global Search in Thunderbird 115.3 shows wrong sender and recipient in the resul") [1426395](https://support.mozilla.org/questions/1426395 "＂C＂ key creates new email, I can't type C on search (win10)") [1426476](https://support.mozilla.org/questions/1426476 "Problemi ricerca e posizionamento cursore, dopo aggiornamento.") [1426483](https://support.mozilla.org/questions/1426483 "Search feature still doesn't work") +29 |
| feat:addons | 16 | 69% ans · 4.4h | 4.0 | 4.0× | [1426361](https://support.mozilla.org/questions/1426361 "GTK (Linux Mint) Theme Broken After Thunderbird Update") [1426374](https://support.mozilla.org/questions/1426374 "Deselect on Delete TB78 add-on not working") [1426530](https://support.mozilla.org/questions/1426530 "Add-on questions regarding search engines?") [1426717](https://support.mozilla.org/questions/1426717 "Temporary extension location") [1426866](https://support.mozilla.org/questions/1426866 "Thunderbird 115 and up with IMAP ACL Extension") +11 |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | September 2023 | October 2023 | Change |
|:--|--:|--:|:--|
| proto:imap | 89 | 113 | ▲ +24 (+27%) |
| proto:pop | 60 | 81 | ▲ +21 (+35%) |
| proto:smtp | 54 | 75 | ▲ +21 (+39%) |
| m:microsoftemail | 109 | 130 | ▲ +21 (+19%) |
| m:yahooemail | 19 | 36 | ▲ +17 (+89%) |
| feat:attachments | 14 | 30 | ▲ +16 (+114%) |
| m:gmail | 131 | 146 | ▲ +15 (+11%) |
| feat:search | 20 | 34 | ▲ +14 (+70%) |

### 🆕 New cause clusters (first appearance ever)

Cause tags with no occurrence in any month before this one — a new entity or newly-matched pattern, worth a look.

| Cause | Qs | Example questions |
|:--|--:|:--|
| m:tutanota | 1 | [1428743](https://support.mozilla.org/questions/1428743 "How to start the setting of Mozilla TB to direct my email traffic from a sleuth ") |
| m:xtra_nz | 1 | [1427365](https://support.mozilla.org/questions/1427365 "MS Exchange (Outlook) account disappearing when exiting Thunderbird") |
| av:panda | 1 | [1427208](https://support.mozilla.org/questions/1427208 "Thunderbird email") |

### Operating-system mix

| Operating-system mix | September 2023 | October 2023 | Change |
|:--|--:|--:|:--|
| os:windows | 149 | 198 | ▲ +49 (+33%) |
| os:linux | 52 | 87 | ▲ +35 (+67%) |
| os:macos | 37 | 49 | ▲ +12 (+32%) |

### Topic mix

| Topic mix | September 2023 | October 2023 | Change |
|:--|--:|--:|:--|
| other | 558 | 803 | ▲ +245 (+44%) |
| settings | 252 | 417 | ▲ +165 (+65%) |
| troubleshooting | 253 | 393 | ▲ +140 (+55%) |
| installation-and-updates | 154 | 217 | ▲ +63 (+41%) |
| calendar | 57 | 55 | ▼ -2 (-4%) |
| privacy-and-security | 41 | 60 | ▲ +19 (+46%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · October 2023 vs September 2023._

_Last updated: 2026-09-10 00:28 UTC_
