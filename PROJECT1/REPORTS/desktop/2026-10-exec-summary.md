---
layout: base
title: "2026-10 exec summary: Thunderbird Desktop support spikes"
---

# October 2026: Thunderbird Desktop support spikes

Executive summary for 2026-10. It covers 144 Thunderbird Desktop support questions. The tool wrote this page on 2026-10-05 05:48 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## October 2026: 7 spikes to investigate

4 of them tie to a Thunderbird version. 3 of them are cause-level. Every row is in the collapsed blocks below.

October 2026 is still in progress. The counts will grow.

In short: Shaw and Attachments. Both are in [What stands out](#what-stands-out), with 2 smaller clusters.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 1 | 2 | 1 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 3 | 0 |

October 2026 holds 144 questions, about 29 a day. The detectors need 8 questions of one kind in a day, 6 in a week or 8 in a month before they call a spike. At this volume most real clusters cannot clear those floors, so read a zero as "nothing large enough to fire", not as "nothing happened".

Three more numbers for context:

- Volume: 144 questions. 71 of them (49%) carry a cause tag. The count per day was `██▇▇▂`, one block per day from October 1 to October 5.
- Answers: 96 of the 144 questions (67%) got an answer from somebody other than the person who asked. The middle time to the first answer was 3.3 hours.
- Release-adoption version spikes: 8. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All October 2026 detail](#all-october-2026-detail) below.

## What stands out {#what-stands-out}

1. Shaw ([`m:shaw`](explorer.html#grain=monthly&cause=m:shaw&period=2026-10), 1 spike): 5 questions in October, under the monthly bar. It peaked in the week of 2026-09-28 at 18.0 times its baseline.
2. Attachments ([`feat:attachments`](explorer.html#grain=monthly&cause=feat:attachments&period=2026-10), 4 spikes): 17 questions in October, under the monthly bar. It peaked on 2026-10-04 at 10.8 times expected, on Thunderbird 157.
3. Address book ([`feat:addressbook`](explorer.html#grain=monthly&cause=feat:addressbook&period=2026-10), 1 spike): 1 question in October, under the monthly bar. It peaked in the week of 2026-09-28 at 3.1 times expected, on Thunderbird 156.
4. Calendar ([`feat:calendar`](explorer.html#grain=monthly&cause=feat:calendar&period=2026-10), 1 spike): 6 questions in October, under the monthly bar. It peaked in the week of 2026-09-28 at 3.0 times its baseline.

In 2 clusters, fewer than 60% of the questions got an answer: `v157 × feat:attachments` on 2026-10-04 (40% answered), `feat:calendar` in the week of 2026-09-28 (44% answered).

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 4 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Version and cause together:

| Grain | Lift | When | Version × Cause | Questions | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| weekly | 2.9× | 2026-09-28 | v156 × feat:import_export | 5 | 40% answered (below 60%), 1.0h | [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") [1608076](https://support.mozilla.org/questions/1608076 "Import from Outlook") [1608271](https://support.mozilla.org/questions/1608271 "preciso de ajuda para fazer backup no thunderbird.") [1608370](https://support.mozilla.org/questions/1608370 "How to import contacts from Thunderbird to Zoho") [1608599](https://support.mozilla.org/questions/1608599 "Export/Import accounts only") |
| weekly | 2.6× | 2026-09-28 | v157 × feat:calendar | 5 | 60% answered, 2.0h | [1608944](https://support.mozilla.org/questions/1608944 "Thunderbird 157 breaks google calendar add-on") [1608983](https://support.mozilla.org/questions/1608983 "Google Calendar & Tasks suddenly fail in Thunderbird 157 64bit") [1609243](https://support.mozilla.org/questions/1609243 "How to change font color in Thunderbird Calendar events?") [1609292](https://support.mozilla.org/questions/1609292 "thunderbird 157 update deactivated all my calendars") [1609695](https://support.mozilla.org/questions/1609695 "After a Thunderbird update I can not delete a calendar event") |
| monthly | 2.6× | 2026-10 | v157 × feat:calendar | 5 | 60% answered, 2.0h | [1608944](https://support.mozilla.org/questions/1608944 "Thunderbird 157 breaks google calendar add-on") [1608983](https://support.mozilla.org/questions/1608983 "Google Calendar & Tasks suddenly fail in Thunderbird 157 64bit") [1609243](https://support.mozilla.org/questions/1609243 "How to change font color in Thunderbird Calendar events?") [1609292](https://support.mozilla.org/questions/1609292 "thunderbird 157 update deactivated all my calendars") [1609695](https://support.mozilla.org/questions/1609695 "After a Thunderbird update I can not delete a calendar event") |

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.6× | 2026-09-28 | feat:import_export | 9 | 44% answered (below 60%), 0.7h | 3.5 | [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") [1608076](https://support.mozilla.org/questions/1608076 "Import from Outlook") [1608137](https://support.mozilla.org/questions/1608137 "Missing Outlook import information") [1608271](https://support.mozilla.org/questions/1608271 "preciso de ajuda para fazer backup no thunderbird.") [1608318](https://support.mozilla.org/questions/1608318 "How do I migrate local folders from Outlook for Mac to Thunderbird") [1608366](https://support.mozilla.org/questions/1608366 "Since thunderbird freezes when I try to import from outlook 2016 (Win 7), how ca") +3 |


</details>

---

## All October 2026 detail {#all-october-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 4 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | 10.8× | 2026-10-04 | v157 × feat:attachments | 5 | 40% answered (below 60%), 0.9h | new | [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") [1609601](https://support.mozilla.org/questions/1609601 "Change the app that opens email attachments") [1609642](https://support.mozilla.org/questions/1609642 "Attach button does not respond. Drag and Drop works. (bug2077590)") [1609643](https://support.mozilla.org/questions/1609643 "email beantwoorden, bijlage knop werkt niet") [1609719](https://support.mozilla.org/questions/1609719 "Unable to attach files to email") |
| monthly | 6.6× | 2026-10 | v157 × feat:attachments | 10 | 70% answered, 2.0h | new | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update (bug2077590)") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") [1609461](https://support.mozilla.org/questions/1609461 "I am unable to attach files using either the button or the keyboard.") [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") +4 |
| weekly | 6.5× | 2026-09-28 | v157 × feat:attachments | 10 | 70% answered, 2.0h | spreading | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update (bug2077590)") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") [1609461](https://support.mozilla.org/questions/1609461 "I am unable to attach files using either the button or the keyboard.") [1609599](https://support.mozilla.org/questions/1609599 "na de laatste update kan ik geen bijlages toevoegen aan een e-mail") +4 |
| weekly | 3.1× | 2026-09-28 | v156 × feat:addressbook | 4 | 75% answered, 0.1h | spreading | [1608295](https://support.mozilla.org/questions/1608295 "reloaded Thuderbird but address book .sqlite file not reloading") [1608307](https://support.mozilla.org/questions/1608307 "How to sync iCloud Contacts to Thunderbird") [1608370](https://support.mozilla.org/questions/1608370 "How to import contacts from Thunderbird to Zoho") [1608602](https://support.mozilla.org/questions/1608602 "Remove Personall Address Book and Collected Addresses from Address Book") |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 3 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 18.0× | 2026-09-28 | m:shaw | 9 | 78% answered, 3.1h | 0.5 | [1608189](https://support.mozilla.org/questions/1608189 "Host Name and Port error as I try to set up Thunderbird. I have shaw mail.") [1608378](https://support.mozilla.org/questions/1608378 "certificate for imap.shaw.ca does not come from a trusted source") [1608647](https://support.mozilla.org/questions/1608647 "Certificate not from trusted source.") [1608660](https://support.mozilla.org/questions/1608660 "Repeated message 'Thunderbird: The certificate for imap.shaw.ca ' keeps showing ") [1608967](https://support.mozilla.org/questions/1608967 "I lost the ability to sync thunderbird to shaw rmail6") [1608978](https://support.mozilla.org/questions/1608978 "Windows 11 preview update results in invalid certificate error - timezone change") +3 |
| weekly | 5.7× | 2026-09-28 | feat:attachments | 17 | 82% answered, 2.9h | 3.0 | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609191](https://support.mozilla.org/questions/1609191 "thunderbird will not allow attachments of any kind or size") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update (bug2077590)") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") [1609307](https://support.mozilla.org/questions/1609307 "attaching files to outgoing emails stopped working, what is going on?") +11 |
| weekly | 3.0× | 2026-09-28 | feat:calendar | 9 | 44% answered (below 60%), 11.5h | 3.0 | [1608156](https://support.mozilla.org/questions/1608156 "Thunderbird calendar not respecting timezone when subscribing to RFC5545-complia") [1608285](https://support.mozilla.org/questions/1608285 "Calendar Reminders Box fails to automatically disappear when empty") [1608702](https://support.mozilla.org/questions/1608702 "Calendar broken?") [1608944](https://support.mozilla.org/questions/1608944 "Thunderbird 157 breaks google calendar add-on") [1608983](https://support.mozilla.org/questions/1608983 "Google Calendar & Tasks suddenly fail in Thunderbird 157 64bit") [1609243](https://support.mozilla.org/questions/1609243 "How to change font color in Thunderbird Calendar events?") +3 |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 8 rows</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | new | 2026-10-01 | tb_version_major | 157 | 12 [1608779](https://support.mozilla.org/questions/1608779 "アカウント削除した元に戻したい") [1608924](https://support.mozilla.org/questions/1608924 "Installing language dictionary") | 0.0 |
| daily | new | 2026-10-02 | tb_version_major | 157 | 14 [1609137](https://support.mozilla.org/questions/1609137 "Accesso server smtp.gmail.com con nome utente pasquale.cristillo@gmail.com non r") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") | 0.0 |
| daily | new | 2026-10-03 | tb_version_major | 157 | 16 [1609341](https://support.mozilla.org/questions/1609341 "for the life of me I can not get the new password to work in Thunderbird. I have") [1609345](https://support.mozilla.org/questions/1609345 "How do make to where not the whole conversation open when viewing on email in a ") | 0.0 |
| daily | new | 2026-10-04 | tb_version_major | 157 | 19 [1609555](https://support.mozilla.org/questions/1609555 "non va la posta") [1609557](https://support.mozilla.org/questions/1609557 "Thunderbird is deleting emails in my inbox, it only retains 14 days, this is onl") | 0.0 |
| monthly | new | 2026-10 | tb_version_major | 156 | 12 [1608889](https://support.mozilla.org/questions/1608889 "Thunderbird Gone!  - no icon, not in app list in windows 11") [1608938](https://support.mozilla.org/questions/1608938 "Thunderbird non riceve i miei indirizzi maxs21r@hotmail-it e maxs21r  ò   gmail.") | 0.0 |
| monthly | new | 2026-10 | tb_version_major | 157 | 62 [1608779](https://support.mozilla.org/questions/1608779 "アカウント削除した元に戻したい") [1608924](https://support.mozilla.org/questions/1608924 "Installing language dictionary") | 0.0 |
| weekly | new | 2026-09-28 | tb_version_major | 156 | 63 [1607958](https://support.mozilla.org/questions/1607958 "free large video and large file  sender  to send large files  videos in Thunderb") [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") | 0.0 |
| weekly | new | 2026-09-28 | tb_version_major | 157 | 63 [1608636](https://support.mozilla.org/questions/1608636 "problème archivage des messages envoyés") [1608734](https://support.mozilla.org/questions/1608734 "I can no longer copy and paste") | 0.0 |

</details>

<details markdown="1">
<summary>October 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v157 | 62 | `▅▆▇█▁` |
| v153 | 29 | `▅█▇▄▂` |
| v156 | 12 | `█▆▃▁▁` |
| v140 | 6 | `▃█▁▃▃` |
| v150 | 4 | `▁▅█▅▁` |
| v128 | 2 | `█▁▁█▁` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:microsoftemail | 11 | `█▆▅▅▁` |
| m:gmail | 11 | `▂█▅▂▁` |
| m:yahooemail | 8 | `██▁▃▃` |
| m:shaw | 5 | `█▁▅█▁` |
| m:spectrum | 2 | `██▁▁▁` |
| m:libero | 2 | `▁█▁█▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:attachments | 17 | `▂█▆█▁` |
| feat:calendar | 6 | `██▅▅▁` |
| feat:junk | 5 | `▁▁██▅` |
| feat:addons | 2 | `█▁▁▁▁` |
| feat:spellcheck | 1 | `█▁▁▁▁` |
| feat:addressbook | 1 | `█▁▁▁▁` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 11 | `▅█▅▆▁` |
| proto:smtp | 7 | `▅█▃▁▁` |
| proto:pop | 6 | `█▆▁▃▁` |
| proto:oauth | 2 | `▁█▁█▁` |
| proto:caldav | 2 | `▁██▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 127 | `▇█▇▇▁` |
| os:linux | 10 | `█▆▆▆▃` |
| os:macos | 3 | `▁██▁█` |
| os:other | 2 | `▁█▁█▁` |
| os:android | 1 | `█▁▁▁▁` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:golden_gate | 1 | `▁█▁▁▁` |
| macos:catalina | 1 | `▁█▁▁▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward October 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
