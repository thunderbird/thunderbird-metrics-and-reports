---
layout: base
title: "2026-10 exec summary: Thunderbird Desktop support spikes"
---

# October 2026: Thunderbird Desktop support spikes

Executive summary for 2026-10. It covers 364 Thunderbird Desktop support questions. The tool wrote this page on 2026-10-09 05:39 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

<details markdown="1">
<summary>Glossary</summary>

| Term | Meaning |
|:--|:--|
| question | One post by a user on the Thunderbird support site. |
| cause tag | What a question is about. `m:spectrum` is the mail host Spectrum. `proto:pop` is the mail protocol POP. `av:avast` is the antivirus product Avast. `feat:printing` is the printing feature of Thunderbird. |
| spike | A period with many more questions of one kind than normal. |
| baseline | The normal count for that kind of question. The tool takes the middle value of earlier periods. |
| rise | The measured count divided by the baseline. A rise of 3.0× means three times as many questions as normal. |
| lift | The same idea for one version and one cause together. The tool divides the count by the count it expects from the number of questions about that version and the normal rate of that cause. A lift above 1 means the cause hits that version harder than the rest. |
| grain | The length of the period that the tool measured: one day, one week, or one month. |
| served | How many of the questions got an answer from somebody other than the person who asked, and the time to the first answer. Below 60% is marked. |
| novelty | Whether the tool saw the pair before. `new` is the first time. `spreading` is a known cause on a new version. `recurring` is a pair that fires again. |
| version×cause spike | A rise tied to one Thunderbird version and one cause. It points to a problem that a Thunderbird release caused. |
| cause-level spike | A rise that ignores the version. It points to a problem at a mail host, in a protocol, in an antivirus product, or in one Thunderbird feature. |
| release-adoption spike | A rise in the bare count of one version or one operating system. Users move to a new release, so the count rises. This is not an incident. |

</details>

## October 2026: 33 spikes to investigate

21 of them tie to a Thunderbird version. 12 of them are cause-level. Every row is in the collapsed blocks below.

October 2026 is still in progress. The counts will grow.

In short: Attachments and AT&T. Both are in [What stands out](#what-stands-out), with 3 smaller clusters.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 9 | 8 | 4 |
| cause-level (mail host, protocol, antivirus, feature) | 5 | 5 | 2 |

Three more numbers for context:

- Volume: 364 questions. 179 of them (49%) carry a cause tag. The count per day was `▅▅▄▄▇█▇▅▁`, one block per day from October 1 to October 9.
- Answers: 256 of the 364 questions (70%) got an answer from somebody other than the person who asked. The middle time to the first answer was 2.4 hours.
- Release-adoption version spikes: 15. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All October 2026 detail](#all-october-2026-detail) below.

## What stands out {#what-stands-out}

1. Attachments ([`feat:attachments`](explorer.html#grain=monthly&cause=feat:attachments&period=2026-10), 20 spikes): 57 questions in October, 3.8 times the baseline of 15.0. It peaked on 2026-10-08 with 11 questions, where earlier periods had none.
2. AT&T ([`m:att`](explorer.html#grain=monthly&cause=m:att&period=2026-10), 10 spikes): 23 questions in October, 5.8 times the baseline of 4.0. It peaked on 2026-10-06 with 11 questions, where earlier periods had none.
3. Shaw ([`m:shaw`](explorer.html#grain=monthly&cause=m:shaw&period=2026-10), 1 spike): 5 questions in October, under the monthly bar. It peaked in the week of 2026-09-28 at 18.0 times its baseline.
4. Address book ([`feat:addressbook`](explorer.html#grain=monthly&cause=feat:addressbook&period=2026-10), 1 spike): 1 question in October, under the monthly bar. It peaked in the week of 2026-09-28 at 3.2 times expected, on Thunderbird 156.
5. Calendar ([`feat:calendar`](explorer.html#grain=monthly&cause=feat:calendar&period=2026-10), 1 spike): 10 questions in October, under the monthly bar. It peaked in the week of 2026-09-28 at 3.0 times its baseline.

In 11 clusters, fewer than 60% of the questions got an answer: `v140 × m:att` on 2026-10-06 (50% answered), `v115 × m:att` in the week of 2026-10-05 (40% answered), `v140 × m:att` in the week of 2026-10-05 (50% answered), `v157 × m:att` in the week of 2026-10-05 (33% answered), and 7 more.

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 3 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Version and cause together:

| Grain | Lift | When | Version × Cause | Questions | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| weekly | 2.9× | 2026-09-28 | v156 × feat:import_export | 5 | 40% answered (below 60%), 1.0h | [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") [1608076](https://support.mozilla.org/questions/1608076 "Import from Outlook") [1608271](https://support.mozilla.org/questions/1608271 "preciso de ajuda para fazer backup no thunderbird.") [1608370](https://support.mozilla.org/questions/1608370 "How to import contacts from Thunderbird to Zoho") [1608599](https://support.mozilla.org/questions/1608599 "Export/Import accounts only") |
| weekly | 2.6× | 2026-09-28 | v157 × feat:calendar | 5 | 60% answered, 2.0h | [1608944](https://support.mozilla.org/questions/1608944 "Thunderbird 157 breaks google calendar add-on") [1608983](https://support.mozilla.org/questions/1608983 "Google Calendar & Tasks suddenly fail in Thunderbird 157 64bit") [1609243](https://support.mozilla.org/questions/1609243 "How to change font color in Thunderbird Calendar events?") [1609292](https://support.mozilla.org/questions/1609292 "thunderbird 157 update deactivated all my calendars") [1609695](https://support.mozilla.org/questions/1609695 "After a Thunderbird update I can not delete a calendar event") |

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.6× | 2026-09-28 | feat:import_export | 9 | 44% answered (below 60%), 0.7h | 3.5 | [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") [1608076](https://support.mozilla.org/questions/1608076 "Import from Outlook") [1608137](https://support.mozilla.org/questions/1608137 "Missing Outlook import information") [1608271](https://support.mozilla.org/questions/1608271 "preciso de ajuda para fazer backup no thunderbird.") [1608318](https://support.mozilla.org/questions/1608318 "How do I migrate local folders from Outlook for Mac to Thunderbird") [1608366](https://support.mozilla.org/questions/1608366 "Since thunderbird freezes when I try to import from outlook 2016 (Win 7), how ca") +3 |


</details>

---

## All October 2026 detail {#all-october-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 21 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | 102.8× | 2026-10-06 | v140 × m:att | 4 | 50% answered (below 60%), 1.4h | new | [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") [1610258](https://support.mozilla.org/questions/1610258 "The certificate for inbound.att.net does not come from a trusted source.") [1610259](https://support.mozilla.org/questions/1610259 "Why Thunderbird on Linux will no longer connect to att.net email with POP3.") [1610309](https://support.mozilla.org/questions/1610309 "AOL setup on MX Linux... fails authentication") |
| monthly | 57.1× | 2026-10 | v115 × m:att | 5 | 40% answered (below 60%), 10.0h | new | [1609983](https://support.mozilla.org/questions/1609983 "I cannot bring mail from AT&T  into my Thunderbird app on my home computer, what") [1610152](https://support.mozilla.org/questions/1610152 "Certificate revoked for inbound.att.net?  What do we do?") [1610310](https://support.mozilla.org/questions/1610310 "New Messages go only to Local Folder; Account Inbox is bypassed and has no F5 fu") [1610321](https://support.mozilla.org/questions/1610321 "I can't recieve emails but can send the certification is revoked for inbound.att") [1610518](https://support.mozilla.org/questions/1610518 "suddenly can't retrieve ATT Yahoo emails with Thunderbird after trying every sug") |
| weekly | 57.1× | 2026-10-05 | v115 × m:att | 5 | 40% answered (below 60%), 10.0h | new | [1609983](https://support.mozilla.org/questions/1609983 "I cannot bring mail from AT&T  into my Thunderbird app on my home computer, what") [1610152](https://support.mozilla.org/questions/1610152 "Certificate revoked for inbound.att.net?  What do we do?") [1610310](https://support.mozilla.org/questions/1610310 "New Messages go only to Local Folder; Account Inbox is bypassed and has no F5 fu") [1610321](https://support.mozilla.org/questions/1610321 "I can't recieve emails but can send the certification is revoked for inbound.att") [1610518](https://support.mozilla.org/questions/1610518 "suddenly can't retrieve ATT Yahoo emails with Thunderbird after trying every sug") |
| weekly | 34.3× | 2026-10-05 | v140 × m:att | 4 | 50% answered (below 60%), 1.4h | new | [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") [1610258](https://support.mozilla.org/questions/1610258 "The certificate for inbound.att.net does not come from a trusted source.") [1610259](https://support.mozilla.org/questions/1610259 "Why Thunderbird on Linux will no longer connect to att.net email with POP3.") [1610309](https://support.mozilla.org/questions/1610309 "AOL setup on MX Linux... fails authentication") |
| daily | 13.3× | 2026-10-08 | v153 × feat:attachments | 5 | 100% answered, 0.6h | recurring | [1610569](https://support.mozilla.org/questions/1610569 "The file picker does not open when you click the “Attach” button") [1610581](https://support.mozilla.org/questions/1610581 "Cannot attach files to emails in Thunderbird") [1610617](https://support.mozilla.org/questions/1610617 "Attachment function not accessible anymore") [1610652](https://support.mozilla.org/questions/1610652 "Attachment to an email is not possible with Tunderbird") [1610745](https://support.mozilla.org/questions/1610745 "Why can't I attach a document to my email") |
| daily | 12.7× | 2026-10-05 | v153 × feat:attachments | 6 | 83% answered, 0.6h | spreading | [1609864](https://support.mozilla.org/questions/1609864 "allegati che non si possono più inserire nell'email") [1609904](https://support.mozilla.org/questions/1609904 "Unable to attach a document to a return email") [1609918](https://support.mozilla.org/questions/1609918 "allegati") [1609979](https://support.mozilla.org/questions/1609979 "why can't i attach files to sent email?") [1609986](https://support.mozilla.org/questions/1609986 "not launching file explorer to attach files") [1610030](https://support.mozilla.org/questions/1610030 "Thunderbird ＂Attach＂ button nor yellow attach bar reminder functioning.") |
| daily | 10.6× | 2026-10-07 | v153 × feat:attachments | 5 | 100% answered, 2.0h | recurring | [1610392](https://support.mozilla.org/questions/1610392 "Recurring Issue with Attachment Button in Thunderbird Desktop") [1610416](https://support.mozilla.org/questions/1610416 "sinds de update 153.4.0esr van 05 oktober kan ik geen bijlagen meer koppelen aan") [1610444](https://support.mozilla.org/questions/1610444 "Thunderbird has stopped to include attachments via key. Only drag and drop funct") [1610449](https://support.mozilla.org/questions/1610449 "A problem with sending attachments with an email") [1610548](https://support.mozilla.org/questions/1610548 "Unable to add an attachment to the email being sent") |
| weekly | 10.1× | 2026-10-05 | v153 × feat:attachments | 21 | 95% answered, 0.9h | spreading | [1609864](https://support.mozilla.org/questions/1609864 "allegati che non si possono più inserire nell'email") [1609904](https://support.mozilla.org/questions/1609904 "Unable to attach a document to a return email") [1609918](https://support.mozilla.org/questions/1609918 "allegati") [1609979](https://support.mozilla.org/questions/1609979 "why can't i attach files to sent email?") [1609986](https://support.mozilla.org/questions/1609986 "not launching file explorer to attach files") [1610030](https://support.mozilla.org/questions/1610030 "Thunderbird ＂Attach＂ button nor yellow attach bar reminder functioning.") +15 |
| daily | 8.7× | 2026-10-08 | v157 × feat:attachments | 6 | 100% answered, 0.7h | recurring | [1610602](https://support.mozilla.org/questions/1610602 "Nejde mi přidat do mailu příloha") [1610606](https://support.mozilla.org/questions/1610606 "The ＂Attach＂ button doesn't work when composing an email; it is not possible to ") [1610619](https://support.mozilla.org/questions/1610619 "Why can I no longer attach a file by clicking OPEN on the file location and why ") [1610638](https://support.mozilla.org/questions/1610638 "allegati mail") [1610666](https://support.mozilla.org/questions/1610666 "een blokkade om bijlagen te koppelen in email die ik verstuur") [1610758](https://support.mozilla.org/questions/1610758 "All of a sudden the attach button does nothing.") |
| daily | 8.4× | 2026-10-04 | v157 × feat:attachments | 5 | 100% answered, 12.1h | new | [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") [1609601](https://support.mozilla.org/questions/1609601 "Change the app that opens email attachments") [1609642](https://support.mozilla.org/questions/1609642 "Attach button does not respond. Drag and Drop works. (bug2077590)") [1609643](https://support.mozilla.org/questions/1609643 "email beantwoorden, bijlage knop werkt niet") [1609719](https://support.mozilla.org/questions/1609719 "Unable to attach files to email") |
| monthly | 7.9× | 2026-10 | v153 × feat:attachments | 23 | 96% answered, 1.4h | new | [1609328](https://support.mozilla.org/questions/1609328 "Can't add attachment to email message") [1609478](https://support.mozilla.org/questions/1609478 "Thunderbird Email senden mit Anhang funktioniert nicht mehr") [1609864](https://support.mozilla.org/questions/1609864 "allegati che non si possono più inserire nell'email") [1609904](https://support.mozilla.org/questions/1609904 "Unable to attach a document to a return email") [1609918](https://support.mozilla.org/questions/1609918 "allegati") [1609979](https://support.mozilla.org/questions/1609979 "why can't i attach files to sent email?") +17 |
| daily | 6.9× | 2026-10-06 | v153 × feat:attachments | 5 | 100% answered, 1.2h | recurring | [1610087](https://support.mozilla.org/questions/1610087 "Email attachment - version 153.4.0esr") [1610100](https://support.mozilla.org/questions/1610100 "unable to attach desktop files to outgoing emails when attachment function activ") [1610118](https://support.mozilla.org/questions/1610118 "All of a sudden Thunderbird won't let me attach images") [1610206](https://support.mozilla.org/questions/1610206 "I have lost the attach file link since last up date") [1610244](https://support.mozilla.org/questions/1610244 "I can't add any attachments. The button doesn't work") |
| weekly | 6.4× | 2026-10-05 | v157 × m:att | 6 | 33% answered (below 60%), 5.9h | new | [1609929](https://support.mozilla.org/questions/1609929 "＂We've identified a site certificate problem＂") [1610002](https://support.mozilla.org/questions/1610002 "'Digicert Global G2' revoked Oct 5, 2026") [1610193](https://support.mozilla.org/questions/1610193 "certificate has been revoked. unable to receive email.") [1610297](https://support.mozilla.org/questions/1610297 "Unable to receive messages due to certificate problem") [1610484](https://support.mozilla.org/questions/1610484 "tbird cannot download emails from my browser.") [1610523](https://support.mozilla.org/questions/1610523 "Thunderbird could not connect to server inbound.att.net. The connection was refu") |
| weekly | 6.2× | 2026-10-05 | v153 × m:att | 4 | 25% answered (below 60%), 24.1h | new | [1610171](https://support.mozilla.org/questions/1610171 "＂inbound.att.net (POP) .. certificate revoked＂? I can't download eMail!") [1610212](https://support.mozilla.org/questions/1610212 "pop from Tbird says connection to server inbound.att.net has been reset") [1610312](https://support.mozilla.org/questions/1610312 "Norton blocks Thunderbird email due to ＂expired certificate＂") [1610322](https://support.mozilla.org/questions/1610322 "No E-mail because of ＂The certificate for inbound.att.net:995 does not come from") |
| weekly | 5.9× | 2026-10-05 | v157 × feat:attachments | 18 | 100% answered, 1.3h | recurring | [1609825](https://support.mozilla.org/questions/1609825 "nach dem letzten Update kann ich keine Attachments versenden") [1609880](https://support.mozilla.org/questions/1609880 "I cannot add an attachment, when I press the attachment button nothing happens") [1609897](https://support.mozilla.org/questions/1609897 "The 'Attach' button does not respond to outgoing emails") [1609916](https://support.mozilla.org/questions/1609916 "Attach button dont work after updating to tb 157") [1610097](https://support.mozilla.org/questions/1610097 "Since that last update I can no longer attach files to emails. Can You help?") [1610225](https://support.mozilla.org/questions/1610225 "Suddenly I can neither attach nor insert files into an outgoing email.") +12 |
| daily | 5.7× | 2026-10-06 | v157 × feat:attachments | 5 | 100% answered, 0.9h | recurring | [1610097](https://support.mozilla.org/questions/1610097 "Since that last update I can no longer attach files to emails. Can You help?") [1610225](https://support.mozilla.org/questions/1610225 "Suddenly I can neither attach nor insert files into an outgoing email.") [1610267](https://support.mozilla.org/questions/1610267 "Attach File no longer Works as of 10/05 W11") [1610268](https://support.mozilla.org/questions/1610268 "Unable to attach files to emails (the ‘Attachments’ button does not respond)./ A") [1610276](https://support.mozilla.org/questions/1610276 "Attach button not working on new emails") |
| monthly | 5.6× | 2026-10 | v157 × feat:attachments | 28 | 100% answered, 2.0h | new | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update (bug2077590)") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") [1609461](https://support.mozilla.org/questions/1609461 "I am unable to attach files using either the button or the keyboard.") [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") +22 |
| daily | 5.3× | 2026-10-05 | v157 × feat:attachments | 4 | 100% answered, 5.4h | recurring | [1609825](https://support.mozilla.org/questions/1609825 "nach dem letzten Update kann ich keine Attachments versenden") [1609880](https://support.mozilla.org/questions/1609880 "I cannot add an attachment, when I press the attachment button nothing happens") [1609897](https://support.mozilla.org/questions/1609897 "The 'Attach' button does not respond to outgoing emails") [1609916](https://support.mozilla.org/questions/1609916 "Attach button dont work after updating to tb 157") |
| weekly | 5.1× | 2026-09-28 | v157 × feat:attachments | 10 | 100% answered, 8.8h | new | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update (bug2077590)") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") [1609461](https://support.mozilla.org/questions/1609461 "I am unable to attach files using either the button or the keyboard.") [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") +4 |
| monthly | 3.9× | 2026-10 | v157 × m:att | 6 | 33% answered (below 60%), 5.9h | new | [1609929](https://support.mozilla.org/questions/1609929 "＂We've identified a site certificate problem＂") [1610002](https://support.mozilla.org/questions/1610002 "'Digicert Global G2' revoked Oct 5, 2026") [1610193](https://support.mozilla.org/questions/1610193 "certificate has been revoked. unable to receive email.") [1610297](https://support.mozilla.org/questions/1610297 "Unable to receive messages due to certificate problem") [1610484](https://support.mozilla.org/questions/1610484 "tbird cannot download emails from my browser.") [1610523](https://support.mozilla.org/questions/1610523 "Thunderbird could not connect to server inbound.att.net. The connection was refu") |
| weekly | 3.2× | 2026-09-28 | v156 × feat:addressbook | 4 | 75% answered, 0.1h | spreading | [1608295](https://support.mozilla.org/questions/1608295 "reloaded Thuderbird but address book .sqlite file not reloading") [1608307](https://support.mozilla.org/questions/1608307 "How to sync iCloud Contacts to Thunderbird") [1608370](https://support.mozilla.org/questions/1608370 "How to import contacts from Thunderbird to Zoho") [1608602](https://support.mozilla.org/questions/1608602 "Remove Personall Address Book and Collected Addresses from Address Book") |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 12 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| daily | new | 2026-10-07 | feat:attachments | 8 | 100% answered, 1.3h | 0.0 | [1610366](https://support.mozilla.org/questions/1610366 "Thunderbird, button ＂attach＂") [1610392](https://support.mozilla.org/questions/1610392 "Recurring Issue with Attachment Button in Thunderbird Desktop") [1610416](https://support.mozilla.org/questions/1610416 "sinds de update 153.4.0esr van 05 oktober kan ik geen bijlagen meer koppelen aan") [1610444](https://support.mozilla.org/questions/1610444 "Thunderbird has stopped to include attachments via key. Only drag and drop funct") [1610449](https://support.mozilla.org/questions/1610449 "A problem with sending attachments with an email") [1610512](https://support.mozilla.org/questions/1610512 "Can't use Attachments like I have always done and need for work") +2 |
| daily | new | 2026-10-08 | feat:attachments | 11 | 100% answered, 0.6h | 0.0 | [1610569](https://support.mozilla.org/questions/1610569 "The file picker does not open when you click the “Attach” button") [1610581](https://support.mozilla.org/questions/1610581 "Cannot attach files to emails in Thunderbird") [1610602](https://support.mozilla.org/questions/1610602 "Nejde mi přidat do mailu příloha") [1610606](https://support.mozilla.org/questions/1610606 "The ＂Attach＂ button doesn't work when composing an email; it is not possible to ") [1610617](https://support.mozilla.org/questions/1610617 "Attachment function not accessible anymore") [1610619](https://support.mozilla.org/questions/1610619 "Why can I no longer attach a file by clicking OPEN on the file location and why ") +5 |
| daily | new | 2026-10-06 | feat:attachments | 11 | 100% answered, 1.2h | 0.0 | [1610087](https://support.mozilla.org/questions/1610087 "Email attachment - version 153.4.0esr") [1610097](https://support.mozilla.org/questions/1610097 "Since that last update I can no longer attach files to emails. Can You help?") [1610100](https://support.mozilla.org/questions/1610100 "unable to attach desktop files to outgoing emails when attachment function activ") [1610118](https://support.mozilla.org/questions/1610118 "All of a sudden Thunderbird won't let me attach images") [1610206](https://support.mozilla.org/questions/1610206 "I have lost the attach file link since last up date") [1610216](https://support.mozilla.org/questions/1610216 "Thunerbird suddenly won't allow me to attach documents") +5 |
| daily | new | 2026-10-06 | m:att | 11 | 36% answered (below 60%), 1.5h | 0.0 | [1610152](https://support.mozilla.org/questions/1610152 "Certificate revoked for inbound.att.net?  What do we do?") [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") [1610171](https://support.mozilla.org/questions/1610171 "＂inbound.att.net (POP) .. certificate revoked＂? I can't download eMail!") [1610193](https://support.mozilla.org/questions/1610193 "certificate has been revoked. unable to receive email.") [1610212](https://support.mozilla.org/questions/1610212 "pop from Tbird says connection to server inbound.att.net has been reset") [1610258](https://support.mozilla.org/questions/1610258 "The certificate for inbound.att.net does not come from a trusted source.") +5 |
| daily | new | 2026-10-05 | feat:attachments | 10 | 90% answered, 2.9h | 0.0 | [1609825](https://support.mozilla.org/questions/1609825 "nach dem letzten Update kann ich keine Attachments versenden") [1609864](https://support.mozilla.org/questions/1609864 "allegati che non si possono più inserire nell'email") [1609880](https://support.mozilla.org/questions/1609880 "I cannot add an attachment, when I press the attachment button nothing happens") [1609897](https://support.mozilla.org/questions/1609897 "The 'Attach' button does not respond to outgoing emails") [1609904](https://support.mozilla.org/questions/1609904 "Unable to attach a document to a return email") [1609916](https://support.mozilla.org/questions/1609916 "Attach button dont work after updating to tb 157") +4 |
| weekly | 23.0× | 2026-10-05 | m:att | 23 | 39% answered (below 60%), 8.1h | 1.0 | [1609929](https://support.mozilla.org/questions/1609929 "＂We've identified a site certificate problem＂") [1609983](https://support.mozilla.org/questions/1609983 "I cannot bring mail from AT&T  into my Thunderbird app on my home computer, what") [1610002](https://support.mozilla.org/questions/1610002 "'Digicert Global G2' revoked Oct 5, 2026") [1610037](https://support.mozilla.org/questions/1610037 "Thunderbird suddenly stopped receiving AT&T email ?") [1610152](https://support.mozilla.org/questions/1610152 "Certificate revoked for inbound.att.net?  What do we do?") [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") +17 |
| weekly | 18.0× | 2026-09-28 | m:shaw | 9 | 78% answered, 3.1h | 0.5 | [1608189](https://support.mozilla.org/questions/1608189 "Host Name and Port error as I try to set up Thunderbird. I have shaw mail.") [1608378](https://support.mozilla.org/questions/1608378 "certificate for imap.shaw.ca does not come from a trusted source") [1608647](https://support.mozilla.org/questions/1608647 "Certificate not from trusted source.") [1608660](https://support.mozilla.org/questions/1608660 "Repeated message 'Thunderbird: The certificate for imap.shaw.ca ' keeps showing ") [1608967](https://support.mozilla.org/questions/1608967 "I lost the ability to sync thunderbird to shaw rmail6") [1608978](https://support.mozilla.org/questions/1608978 "Windows 11 preview update results in invalid certificate error - timezone change") +3 |
| weekly | 7.3× | 2026-10-05 | feat:attachments | 40 | 98% answered, 1.2h | 5.5 | [1609825](https://support.mozilla.org/questions/1609825 "nach dem letzten Update kann ich keine Attachments versenden") [1609864](https://support.mozilla.org/questions/1609864 "allegati che non si possono più inserire nell'email") [1609880](https://support.mozilla.org/questions/1609880 "I cannot add an attachment, when I press the attachment button nothing happens") [1609897](https://support.mozilla.org/questions/1609897 "The 'Attach' button does not respond to outgoing emails") [1609904](https://support.mozilla.org/questions/1609904 "Unable to attach a document to a return email") [1609916](https://support.mozilla.org/questions/1609916 "Attach button dont work after updating to tb 157") +34 |
| monthly | 5.8× | 2026-10 | m:att | 23 | 39% answered (below 60%), 8.1h | 4.0 | [1609929](https://support.mozilla.org/questions/1609929 "＂We've identified a site certificate problem＂") [1609983](https://support.mozilla.org/questions/1609983 "I cannot bring mail from AT&T  into my Thunderbird app on my home computer, what") [1610002](https://support.mozilla.org/questions/1610002 "'Digicert Global G2' revoked Oct 5, 2026") [1610037](https://support.mozilla.org/questions/1610037 "Thunderbird suddenly stopped receiving AT&T email ?") [1610152](https://support.mozilla.org/questions/1610152 "Certificate revoked for inbound.att.net?  What do we do?") [1610156](https://support.mozilla.org/questions/1610156 "Gives error today - inbound.att.net certificate invalid !!??") +17 |
| weekly | 5.7× | 2026-09-28 | feat:attachments | 17 | 100% answered, 4.9h | 3.0 | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609191](https://support.mozilla.org/questions/1609191 "thunderbird will not allow attachments of any kind or size") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update (bug2077590)") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") [1609307](https://support.mozilla.org/questions/1609307 "attaching files to outgoing emails stopped working, what is going on?") +11 |
| monthly | 3.8× | 2026-10 | feat:attachments | 57 | 98% answered, 1.8h | 15.0 | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609191](https://support.mozilla.org/questions/1609191 "thunderbird will not allow attachments of any kind or size") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update (bug2077590)") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") [1609307](https://support.mozilla.org/questions/1609307 "attaching files to outgoing emails stopped working, what is going on?") +51 |
| weekly | 3.0× | 2026-09-28 | feat:calendar | 9 | 44% answered (below 60%), 11.5h | 3.0 | [1608156](https://support.mozilla.org/questions/1608156 "Thunderbird calendar not respecting timezone when subscribing to RFC5545-complia") [1608285](https://support.mozilla.org/questions/1608285 "Calendar Reminders Box fails to automatically disappear when empty") [1608702](https://support.mozilla.org/questions/1608702 "Calendar broken?") [1608944](https://support.mozilla.org/questions/1608944 "Thunderbird 157 breaks google calendar add-on") [1608983](https://support.mozilla.org/questions/1608983 "Google Calendar & Tasks suddenly fail in Thunderbird 157 64bit") [1609243](https://support.mozilla.org/questions/1609243 "How to change font color in Thunderbird Calendar events?") +3 |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 15 rows</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | new | 2026-10-01 | tb_version_major | 157 | 12 [1608779](https://support.mozilla.org/questions/1608779 "アカウント削除した元に戻したい") [1608924](https://support.mozilla.org/questions/1608924 "Installing language dictionary") | 0.0 |
| daily | new | 2026-10-02 | tb_version_major | 157 | 14 [1609137](https://support.mozilla.org/questions/1609137 "Accesso server smtp.gmail.com con nome utente pasquale.cristillo@gmail.com non r") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") | 0.0 |
| daily | new | 2026-10-03 | tb_version_major | 157 | 16 [1609341](https://support.mozilla.org/questions/1609341 "for the life of me I can not get the new password to work in Thunderbird. I have") [1609345](https://support.mozilla.org/questions/1609345 "How do make to where not the whole conversation open when viewing on email in a ") | 0.0 |
| daily | new | 2026-10-04 | tb_version_major | 157 | 19 [1609555](https://support.mozilla.org/questions/1609555 "non va la posta") [1609557](https://support.mozilla.org/questions/1609557 "Thunderbird is deleting emails in my inbox, it only retains 14 days, this is onl") | 0.0 |
| daily | new | 2026-10-05 | tb_version_major | 157 | 24 [1609778](https://support.mozilla.org/questions/1609778 "Yahoo has a single Spam folder, but Thunderbird shows 2 for Yahoo") [1609805](https://support.mozilla.org/questions/1609805 "My sent file disappeared. How do I restore my sent file?") | 0.0 |
| daily | new | 2026-10-06 | tb_version_major | 157 | 28 [1610061](https://support.mozilla.org/questions/1610061 "How Can I View All Messages in my Folders Automatically?") [1610072](https://support.mozilla.org/questions/1610072 "I cannot move emails from Inbox to another folder.") | 0.0 |
| daily | 3.3× | 2026-10-06 | tb_version_major | 153 | 23 [1610053](https://support.mozilla.org/questions/1610053 "Why does the same email address appear twice under spam ?") [1610058](https://support.mozilla.org/questions/1610058 "添付ができない（クリックしても選択画面にならない）") | 7.0 |
| daily | new | 2026-10-07 | tb_version_major | 157 | 23 [1610332](https://support.mozilla.org/questions/1610332 "メール作成時ファイルを添付できなくなった") [1610344](https://support.mozilla.org/questions/1610344 "Why are comments in the calendar description showing up suddenly black on black?") | 0.0 |
| daily | 8.0× | 2026-10-07 | os | os:macos | 8 [1610356](https://support.mozilla.org/questions/1610356 "Thunderbird add-on login issue.") [1610397](https://support.mozilla.org/questions/1610397 "Keine Anhänge mehr möglich.") | 1.0 |
| daily | new | 2026-10-08 | tb_version_major | 157 | 22 [1610602](https://support.mozilla.org/questions/1610602 "Nejde mi přidat do mailu příloha") [1610606](https://support.mozilla.org/questions/1610606 "The ＂Attach＂ button doesn't work when composing an email; it is not possible to ") | 0.0 |
| monthly | new | 2026-10 | tb_version_major | 156 | 15 [1608889](https://support.mozilla.org/questions/1608889 "Thunderbird Gone!  - no icon, not in app list in windows 11") [1608938](https://support.mozilla.org/questions/1608938 "Thunderbird non riceve i miei indirizzi maxs21r@hotmail-it e maxs21r  ò   gmail.") | 0.0 |
| monthly | new | 2026-10 | tb_version_major | 157 | 158 [1608779](https://support.mozilla.org/questions/1608779 "アカウント削除した元に戻したい") [1608924](https://support.mozilla.org/questions/1608924 "Installing language dictionary") | 0.0 |
| weekly | new | 2026-09-28 | tb_version_major | 156 | 63 [1607958](https://support.mozilla.org/questions/1607958 "free large video and large file  sender  to send large files  videos in Thunderb") [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") | 0.0 |
| weekly | new | 2026-09-28 | tb_version_major | 157 | 63 [1608636](https://support.mozilla.org/questions/1608636 "problème archivage des messages envoyés") [1608734](https://support.mozilla.org/questions/1608734 "I can no longer copy and paste") | 0.0 |
| weekly | new | 2026-10-05 | tb_version_major | 157 | 97 [1609778](https://support.mozilla.org/questions/1609778 "Yahoo has a single Spam folder, but Thunderbird shows 2 for Yahoo") [1609805](https://support.mozilla.org/questions/1609805 "My sent file disappeared. How do I restore my sent file?") | 0.0 |

</details>

<details markdown="1">
<summary>October 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v157 | 158 | `▄▅▅▆▇█▇▇▁` |
| v153 | 93 | `▃▄▃▂▆█▆▅▁` |
| v140 | 17 | `▃▆▁▃▆██▃▁` |
| v156 | 15 | `█▆▃▁▁▂▃▁▁` |
| v115 | 9 | `▁▁▁▁▆▆█▆▁` |
| v128 | 7 | `▃▁▁▃▆▁█▁▁` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 24 | `▂█▅▂▆▅▅▅▁` |
| m:att | 23 | `▁▁▁▁▄█▅▂▁` |
| m:microsoftemail | 19 | `█▆▅▅▆▅▁▆▁` |
| m:yahooemail | 17 | `▅▅▁▂▂█▅▁▂` |
| m:shaw | 5 | `█▁▅█▁▁▁▁▁` |
| m:thundermail | 4 | `▁█▁█▁▁██▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:attachments | 57 | `▂▅▄▅▇█▆█▁` |
| feat:calendar | 10 | `██▅▅▅▅▅▅▁` |
| feat:junk | 6 | `▁▁██▅▅▁▁▁` |
| feat:addons | 3 | `█▁▁▁▁▁▅▁▁` |
| feat:import_export | 3 | `▁▁▁▁█▁▁▅▁` |
| feat:spellcheck | 1 | `█▁▁▁▁▁▁▁▁` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 23 | `▅█▅▆██▆▁▃` |
| proto:pop | 15 | `█▆▁▃▆██▁▃` |
| proto:smtp | 11 | `▅█▃▁▃▅▃▁▁` |
| proto:oauth | 6 | `▁▅▁▅▅█▁▅▁` |
| proto:caldav | 4 | `▁██▁▁▁██▁` |
| proto:ews | 1 | `▁▁▁▁█▁▁▁▁` |

The antivirus products named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| av:norton | 4 | `▁▁▁▁██▁▁▁` |
| av:avast | 3 | `▁▁▁▁▁█▁▁▁` |
| av:defender | 1 | `▁▁▁▁▁▁█▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 313 | `▅▅▅▄▇█▆▆▁` |
| os:linux | 21 | `▅▃▃▃▃▆█▁▁` |
| os:macos | 17 | `▁▂▂▁▄▄█▂▁` |
| os:other | 4 | `▁█▁███▁▁▁` |
| os:android | 2 | `█▁▁▁█▁▁▁▁` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:golden_gate | 1 | `▁█▁▁▁▁▁▁▁` |
| macos:catalina | 1 | `▁█▁▁▁▁▁▁▁` |
| macos:tahoe | 1 | `▁▁▁▁▁█▁▁▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward October 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
