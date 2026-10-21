---
layout: base
title: Desktop Engineering Support Summary — October 2026
---

# Thunderbird Desktop — Monthly Engineering Support Summary

## October 2026 vs September 2026

_For **engineering**: the support signals worth investigating this month vs last — flagged incidents, moving cause clusters, and release adoption. (Community/support-ops KPIs — answered & solved rates, response time — are a separate upcoming report.) Non-AI: regex + traditional stats._

> ⚠️ **October 2026 is in progress** — data through day 21 of 31. Counts are partial, so the deltas below understate October 2026; treat volume changes as directional until the month closes.

## Headline

| | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 977 | 745 | ▼ -232 (-24%) |
| Version × cause spikes flagged | 5 | 13 | ▲ +8 |
| — of which **new** regressions | 2 | 2 | ▬ 0 |
| Cause-level surges flagged | 1 | 3 | ▲ +2 |

## 🚨 Incidents to investigate

> ⏱ **Reading spike timing:** a spike dates when users **piled in** — a *lagging* signal, usually days after an incident's onset and often near its resolution (e.g. the Jun 2023 Libero outage began ~Jun 14; the questions spiked Jun 19). Treat these as pain-cluster / triage signals, **not** real-time incident detection.

### Version × cause — possible release regressions

Ranked new → spreading → recurring, then by lift (× above what release adoption alone explains).

| Signal | When | Version × Cause | Qs | Lift | Served | Example questions |
|:--|:--|:--|--:|--:|:--|:--|
| 🆕 new | 2026-10-06 | v140 × m:att | 4 | 107.3× | 75% ans · 2.7h | [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") [1610258](https://support.mozilla.org/questions/1610258 "The certificate for inbound.att.net does not come from a trusted source.") [1610259](https://support.mozilla.org/questions/1610259 "Why Thunderbird on Linux will no longer connect to att.net email with POP3.") [1610309](https://support.mozilla.org/questions/1610309 "AOL setup on MX Linux... fails authentication") |
| 🆕 new | 2026-10-04 | v157 × feat:attachments | 5 | 7.1× | 100% ans · 12.1h | [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") [1609601](https://support.mozilla.org/questions/1609601 "Change the app that opens email attachments") [1609642](https://support.mozilla.org/questions/1609642 "Attach button does not respond. Drag and Drop works. (bug2077590)") [1609643](https://support.mozilla.org/questions/1609643 "email beantwoorden, bijlage knop werkt niet") [1609719](https://support.mozilla.org/questions/1609719 "Unable to attach files to email") |
| ↗ spreading | 2026-10-05 | v153 × feat:attachments | 6 | 10.8× | 83% ans · 0.6h | [1609864](https://support.mozilla.org/questions/1609864 "allegati che non si possono più inserire nell'email") [1609904](https://support.mozilla.org/questions/1609904 "Unable to attach a document to a return email") [1609918](https://support.mozilla.org/questions/1609918 "allegati") [1609979](https://support.mozilla.org/questions/1609979 "why can't i attach files to sent email?") [1609986](https://support.mozilla.org/questions/1609986 "not launching file explorer to attach files") +1 |
| ↗ spreading | 2026-10-14 | v158 × m:gmail | 5 | 4.0× | 80% ans · 20.5h | [1611781](https://support.mozilla.org/questions/1611781 "Unable to write the email to the mailbox - can't pop download emails from gmail") [1611880](https://support.mozilla.org/questions/1611880 "Unable to Add a Gmail Account to Thunderbird Despite Successful Authentication") [1611900](https://support.mozilla.org/questions/1611900 "Address Books in Desktop Thundermail in Windows 11") [1611935](https://support.mozilla.org/questions/1611935 "Google Popup Sign-in from T-0Bird links to a *ghost*/ disabled gmail account") [1611950](https://support.mozilla.org/questions/1611950 "problem with double entries in the sent folder") |
| ↻ recurring | 2026-10-10 | v153 × feat:attachments | 4 | 13.5× | 100% ans · 0.9h | [1611065](https://support.mozilla.org/questions/1611065 "Suddenly I can't attach anything to my emails!") [1611069](https://support.mozilla.org/questions/1611069 "it has not been possible to attach files to emails using the paperclip icon.") [1611096](https://support.mozilla.org/questions/1611096 "Can no longer attach photos with e-mail.") [1611102](https://support.mozilla.org/questions/1611102 "Can no longer attach photos with e-mail. (locked duplicate)") |
| ↻ recurring | 2026-10-08 | v153 × feat:attachments | 5 | 11.3× | 100% ans · 0.6h | [1610569](https://support.mozilla.org/questions/1610569 "The file picker does not open when you click the “Attach” button") [1610581](https://support.mozilla.org/questions/1610581 "Cannot attach files to emails in Thunderbird") [1610617](https://support.mozilla.org/questions/1610617 "Attachment function not accessible anymore") [1610652](https://support.mozilla.org/questions/1610652 "Attachment to an email is not possible with Tunderbird") [1610745](https://support.mozilla.org/questions/1610745 "Why can't I attach a document to my email") |
| ↻ recurring | 2026-10-07 | v153 × feat:attachments | 5 | 9.0× | 100% ans · 2.0h | [1610392](https://support.mozilla.org/questions/1610392 "Recurring Issue with Attachment Button in Thunderbird Desktop") [1610416](https://support.mozilla.org/questions/1610416 "sinds de update 153.4.0esr van 05 oktober kan ik geen bijlagen meer koppelen aan") [1610444](https://support.mozilla.org/questions/1610444 "Thunderbird has stopped to include attachments via key. Only drag and drop funct") [1610449](https://support.mozilla.org/questions/1610449 "A problem with sending attachments with an email") [1610548](https://support.mozilla.org/questions/1610548 "Unable to add an attachment to the email being sent") |
| ↻ recurring | 2026-10-09 | v157 × feat:attachments | 7 | 7.9× | 100% ans · 7.6h | [1610829](https://support.mozilla.org/questions/1610829 "impossibile inserire allegati") [1610832](https://support.mozilla.org/questions/1610832 "No attachment possible") [1610883](https://support.mozilla.org/questions/1610883 "Ik kan geen bijlagen voegen bij mijn email") [1610903](https://support.mozilla.org/questions/1610903 "blokkering van bijlagen koppelen in emailbericht") [1610926](https://support.mozilla.org/questions/1610926 "I cannot attach files") +2 |
| ↻ recurring | 2026-10-08 | v157 × feat:attachments | 6 | 7.4× | 100% ans · 0.7h | [1610602](https://support.mozilla.org/questions/1610602 "Nejde mi přidat do mailu příloha") [1610606](https://support.mozilla.org/questions/1610606 "The ＂Attach＂ button doesn't work when composing an email; it is not possible to ") [1610619](https://support.mozilla.org/questions/1610619 "Why can I no longer attach a file by clicking OPEN on the file location and why ") [1610638](https://support.mozilla.org/questions/1610638 "allegati mail") [1610666](https://support.mozilla.org/questions/1610666 "een blokkade om bijlagen te koppelen in email die ik verstuur") +1 |
| ↻ recurring | 2026-10-12 | v157 × feat:attachments | 5 | 6.8× | 80% ans · 0.7h | [1611426](https://support.mozilla.org/questions/1611426 "Chci do zprávy vložit přílohu a po kliknutí na ikonu příloha se mi nezobrazí nab") [1611443](https://support.mozilla.org/questions/1611443 "Attach button in write email no no longer working") [1611472](https://support.mozilla.org/questions/1611472 "Kan geen bijlage toevoegen in email") [1611511](https://support.mozilla.org/questions/1611511 "Signature attachment button in account settings no longer working; will not go t") [1611542](https://support.mozilla.org/questions/1611542 "thunderbird attach button does not work") |
| ↻ recurring | 2026-10-06 | v153 × feat:attachments | 5 | 5.9× | 100% ans · 1.2h | [1610087](https://support.mozilla.org/questions/1610087 "Email attachment - version 153.4.0esr") [1610100](https://support.mozilla.org/questions/1610100 "unable to attach desktop files to outgoing emails when attachment function activ") [1610118](https://support.mozilla.org/questions/1610118 "All of a sudden Thunderbird won't let me attach images") [1610206](https://support.mozilla.org/questions/1610206 "I have lost the attach file link since last up date") [1610244](https://support.mozilla.org/questions/1610244 "I can't add any attachments. The button doesn't work") |
| ↻ recurring | 2026-10-06 | v157 × feat:attachments | 5 | 4.8× | 100% ans · 0.9h | [1610097](https://support.mozilla.org/questions/1610097 "Since that last update I can no longer attach files to emails. Can You help?") [1610225](https://support.mozilla.org/questions/1610225 "Suddenly I can neither attach nor insert files into an outgoing email.") [1610267](https://support.mozilla.org/questions/1610267 "Attach File no longer Works as of 10/05 W11") [1610268](https://support.mozilla.org/questions/1610268 "Unable to attach files to emails (the ‘Attachments’ button does not respond)./ A") [1610276](https://support.mozilla.org/questions/1610276 "Attach button not working on new emails") |
| ↻ recurring | 2026-10-05 | v157 × feat:attachments | 4 | 4.5× | 100% ans · 5.4h | [1609825](https://support.mozilla.org/questions/1609825 "nach dem letzten Update kann ich keine Attachments versenden") [1609880](https://support.mozilla.org/questions/1609880 "I cannot add an attachment, when I press the attachment button nothing happens") [1609897](https://support.mozilla.org/questions/1609897 "The 'Attach' button does not respond to outgoing emails") [1609916](https://support.mozilla.org/questions/1609916 "Attach button dont work after updating to tb 157") |

### Cause-level surges — provider / protocol / AV / feature (any version)

Version-agnostic (a provider outage spans versions), vs a trailing-month baseline.

| Cause | Qs | Served | vs baseline | Rise | Example questions |
|:--|--:|:--|--:|:--|:--|
| feat:attachments | 101 | 98% ans · 1.4h | 15.0 | 6.73× | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609191](https://support.mozilla.org/questions/1609191 "thunderbird will not allow attachments of any kind or size") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update (bug2077590)") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") +96 |
| m:att | 26 | 81% ans · 24.1h | 4.0 | 6.5× | [1609929](https://support.mozilla.org/questions/1609929 "＂We've identified a site certificate problem＂") [1609983](https://support.mozilla.org/questions/1609983 "I cannot bring mail from AT&T  into my Thunderbird app on my home computer, what") [1610002](https://support.mozilla.org/questions/1610002 "'Digicert Global G2' revoked Oct 5, 2026") [1610037](https://support.mozilla.org/questions/1610037 "Thunderbird suddenly stopped receiving AT&T email ?") [1610152](https://support.mozilla.org/questions/1610152 "Certificate revoked for inbound.att.net?  What do we do?") +21 |
| m:thundermail | 9 | 67% ans · 18.0h | 1.5 | 6.0× | [1609189](https://support.mozilla.org/questions/1609189 "Il selettore di file non si apre cliccando sul pulsante Allega.") [1609761](https://support.mozilla.org/questions/1609761 "Can't upload files to Thundermail Send. Desktop send integration missing") [1610442](https://support.mozilla.org/questions/1610442 "When I") [1610567](https://support.mozilla.org/questions/1610567 "Why is my Thundermail email not arriving?") [1611594](https://support.mozilla.org/questions/1611594 "Emails not showing attachments, and not able to open most older emails.") +4 |

## What moved

### Cause clusters (provider / protocol / AV / feature)

| Cause clusters (provider / protocol / AV / feature) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| feat:attachments | 20 | 101 | ▲ +81 (+405%) |
| proto:smtp | 53 | 20 | ▼ -33 (-62%) |
| proto:imap | 79 | 49 | ▼ -30 (-38%) |
| proto:pop | 62 | 34 | ▼ -28 (-45%) |
| m:microsoftemail | 67 | 40 | ▼ -27 (-40%) |
| m:yahooemail | 60 | 34 | ▼ -26 (-43%) |
| m:att | 6 | 26 | ▲ +20 |
| m:alice_it | 20 | 1 | ▼ -19 (-95%) |

### 🆕 New cause clusters (first appearance ever)

_None — every cause cluster in October 2026 has appeared in a prior month._

### Release adoption (version mix)

| Release adoption (version mix) | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| v153 | 193 | 190 | ▼ -3 (-2%) |
| v157 | 3 | 257 | ▲ +254 |
| v155 | 239 | 2 | ▼ -237 (-99%) |
| v156 | 203 | 17 | ▼ -186 (-92%) |
| v158 | 0 | 87 | ▲ +87 |
| v140 | 44 | 34 | ▼ -10 (-23%) |

### Operating-system mix

| Operating-system mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| os:windows | 816 | 622 | ▼ -194 (-24%) |
| os:linux | 63 | 51 | ▼ -12 (-19%) |
| os:macos | 62 | 43 | ▼ -19 (-31%) |
| os:other | 7 | 9 | ▲ +2 |
| os:android | 5 | 6 | ▲ +1 |

### Topic mix

| Topic mix | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| send-and-receive-email | 317 | 172 | ▼ -145 (-46%) |
| attachments | 28 | 176 | ▲ +148 (+529%) |
| email-and-messaging | 85 | 52 | ▼ -33 (-39%) |
| customization | 71 | 60 | ▼ -11 (-15%) |
| passwords-and-sign-in | 54 | 29 | ▼ -25 (-46%) |
| connectivity | 50 | 26 | ▼ -24 (-48%) |

---

_Prototype engineering month-over-month summary · from Project 1 feature tables + spike detectors · October 2026 vs September 2026._

_Last updated: 2026-10-21 08:08 UTC_
