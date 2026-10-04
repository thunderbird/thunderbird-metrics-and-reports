---
layout: base
title: "2026-10 exec summary: Thunderbird Desktop support spikes"
---

# October 2026: Thunderbird Desktop support spikes

Executive summary for 2026-10. It covers 111 Thunderbird Desktop support questions. The tool wrote this page on 2026-10-04 07:22 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## October 2026: 5 spikes to investigate

3 of them tie to a Thunderbird version. 2 of them are cause-level. Every row is in the collapsed blocks below.

October 2026 is still in progress. The counts will grow.

In short: Shaw and Attachments. Both are in [What stands out](#what-stands-out), with 1 smaller cluster.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 0 | 2 | 1 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 2 | 0 |

October 2026 holds 111 questions, about 28 a day. The detectors need 8 questions of one kind in a day, 6 in a week or 8 in a month before they call a spike. At this volume most real clusters cannot clear those floors, so read a zero as "nothing large enough to fire", not as "nothing happened".

Three more numbers for context:

- Volume: 111 questions. 53 of them (48%) carry a cause tag. The count per day was `██▇▂`, one block per day from October 1 to October 4.
- Answers: 69 of the 111 questions (62%) got an answer from somebody other than the person who asked. The middle time to the first answer was 3.4 hours.
- Release-adoption version spikes: 7. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All October 2026 detail](#all-october-2026-detail) below.

## What stands out {#what-stands-out}

1. Shaw ([`m:shaw`](explorer.html#grain=monthly&cause=m:shaw&period=2026-10), 1 spike): 3 questions in October, under the monthly bar. It peaked in the week of 2026-09-28 at 14.0 times its baseline.
2. Attachments ([`feat:attachments`](explorer.html#grain=monthly&cause=feat:attachments&period=2026-10), 3 spikes): 11 questions in October, under the monthly bar. It peaked in 2026-10 at 4.9 times expected, on Thunderbird 157.
3. Address book ([`feat:addressbook`](explorer.html#grain=monthly&cause=feat:addressbook&period=2026-10), 1 spike): 1 question in October, under the monthly bar. It peaked in the week of 2026-09-28 at 3.1 times expected, on Thunderbird 156.

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
| weekly | 2.9× | 2026-09-28 | v157 × feat:calendar | 4 | 50% answered (below 60%), 1.3h | [1608944](https://support.mozilla.org/questions/1608944 "Thunderbird 157 breaks google calendar add-on") [1608983](https://support.mozilla.org/questions/1608983 "Google Calendar & Tasks suddenly fail in Thunderbird 157 64bit") [1609243](https://support.mozilla.org/questions/1609243 "How to change font color in Thunderbird Calendar events?") [1609292](https://support.mozilla.org/questions/1609292 "thunderbird 157 update deactivated all my calendars") |

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.7× | 2026-09-28 | feat:calendar | 8 | 38% answered (below 60%), 2.0h | 3.0 | [1608156](https://support.mozilla.org/questions/1608156 "Thunderbird calendar not respecting timezone when subscribing to RFC5545-complia") [1608285](https://support.mozilla.org/questions/1608285 "Calendar Reminders Box fails to automatically disappear when empty") [1608702](https://support.mozilla.org/questions/1608702 "Calendar broken?") [1608944](https://support.mozilla.org/questions/1608944 "Thunderbird 157 breaks google calendar add-on") [1608983](https://support.mozilla.org/questions/1608983 "Google Calendar & Tasks suddenly fail in Thunderbird 157 64bit") [1609243](https://support.mozilla.org/questions/1609243 "How to change font color in Thunderbird Calendar events?") +2 |
| weekly | 2.6× | 2026-09-28 | feat:import_export | 9 | 44% answered (below 60%), 0.7h | 3.5 | [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") [1608076](https://support.mozilla.org/questions/1608076 "Import from Outlook") [1608137](https://support.mozilla.org/questions/1608137 "Missing Outlook import information") [1608271](https://support.mozilla.org/questions/1608271 "preciso de ajuda para fazer backup no thunderbird.") [1608318](https://support.mozilla.org/questions/1608318 "How do I migrate local folders from Outlook for Mac to Thunderbird") [1608366](https://support.mozilla.org/questions/1608366 "Since thunderbird freezes when I try to import from outlook 2016 (Win 7), how ca") +3 |


</details>

---

## All October 2026 detail {#all-october-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 3 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| monthly | 4.9× | 2026-10 | v157 × feat:attachments | 5 | 80% answered, 3.7h | new | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") [1609461](https://support.mozilla.org/questions/1609461 "I am unable to attach files using either the button or the keyboard.") |
| weekly | 4.7× | 2026-09-28 | v157 × feat:attachments | 5 | 80% answered, 3.7h | spreading | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") [1609461](https://support.mozilla.org/questions/1609461 "I am unable to attach files using either the button or the keyboard.") |
| weekly | 3.1× | 2026-09-28 | v156 × feat:addressbook | 4 | 75% answered, 0.1h | spreading | [1608295](https://support.mozilla.org/questions/1608295 "reloaded Thuderbird but address book .sqlite file not reloading") [1608307](https://support.mozilla.org/questions/1608307 "How to sync iCloud Contacts to Thunderbird") [1608370](https://support.mozilla.org/questions/1608370 "How to import contacts from Thunderbird to Zoho") [1608602](https://support.mozilla.org/questions/1608602 "Remove Personall Address Book and Collected Addresses from Address Book") |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 2 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 14.0× | 2026-09-28 | m:shaw | 7 | 71% answered, 11.1h | 0.5 | [1608189](https://support.mozilla.org/questions/1608189 "Host Name and Port error as I try to set up Thunderbird. I have shaw mail.") [1608378](https://support.mozilla.org/questions/1608378 "certificate for imap.shaw.ca does not come from a trusted source") [1608647](https://support.mozilla.org/questions/1608647 "Certificate not from trusted source.") [1608660](https://support.mozilla.org/questions/1608660 "Repeated message 'Thunderbird: The certificate for imap.shaw.ca ' keeps showing ") [1608967](https://support.mozilla.org/questions/1608967 "I lost the ability to sync thunderbird to shaw rmail6") [1608978](https://support.mozilla.org/questions/1608978 "Windows 11 preview update results in invalid certificate error - timezone change") +1 |
| weekly | 3.7× | 2026-09-28 | feat:attachments | 11 | 91% answered, 4.4h | 3.0 | [1608942](https://support.mozilla.org/questions/1608942 "Attachment bug") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") [1609191](https://support.mozilla.org/questions/1609191 "thunderbird will not allow attachments of any kind or size") [1609202](https://support.mozilla.org/questions/1609202 "Unable to attach files to emails since 30 Sept update") [1609259](https://support.mozilla.org/questions/1609259 "attachment dialogue not executing!") [1609307](https://support.mozilla.org/questions/1609307 "attaching files to outgoing emails stopped working, what is going on?") +5 |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 7 rows</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | new | 2026-10-01 | tb_version_major | 157 | 12 [1608779](https://support.mozilla.org/questions/1608779 "アカウント削除した元に戻したい") [1608924](https://support.mozilla.org/questions/1608924 "Installing language dictionary") | 0.0 |
| daily | new | 2026-10-02 | tb_version_major | 157 | 13 [1609137](https://support.mozilla.org/questions/1609137 "Accesso server smtp.gmail.com con nome utente pasquale.cristillo@gmail.com non r") [1609154](https://support.mozilla.org/questions/1609154 "Nejde přiložit jakákoli příloha") | 0.0 |
| daily | new | 2026-10-03 | tb_version_major | 157 | 16 [1609341](https://support.mozilla.org/questions/1609341 "for the life of me I can not get the new password to work in Thunderbird. I have") [1609345](https://support.mozilla.org/questions/1609345 "How do make to where not the whole conversation open when viewing on email in a ") | 0.0 |
| monthly | new | 2026-10 | tb_version_major | 156 | 12 [1608889](https://support.mozilla.org/questions/1608889 "Thunderbird Gone!  - no icon, not in app list in windows 11") [1608938](https://support.mozilla.org/questions/1608938 "Thunderbird non riceve i miei indirizzi maxs21r@hotmail-it e maxs21r  ò   gmail.") | 0.0 |
| monthly | new | 2026-10 | tb_version_major | 157 | 43 [1608779](https://support.mozilla.org/questions/1608779 "アカウント削除した元に戻したい") [1608924](https://support.mozilla.org/questions/1608924 "Installing language dictionary") | 0.0 |
| weekly | new | 2026-09-28 | tb_version_major | 156 | 63 [1607958](https://support.mozilla.org/questions/1607958 "free large video and large file  sender  to send large files  videos in Thunderb") [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") | 0.0 |
| weekly | new | 2026-09-28 | tb_version_major | 157 | 45 [1608636](https://support.mozilla.org/questions/1608636 "problème archivage des messages envoyés") [1608734](https://support.mozilla.org/questions/1608734 "I can no longer copy and paste") | 0.0 |

</details>

<details markdown="1">
<summary>October 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v157 | 43 | `▆▇█▂` |
| v153 | 25 | `▅█▇▂` |
| v156 | 12 | `█▆▃▁` |
| v140 | 4 | `▃█▁▁` |
| v150 | 3 | `▁▅█▁` |
| v102 | 1 | `█▁▁▁` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 10 | `▂█▅▁` |
| m:microsoftemail | 8 | `██▆▁` |
| m:yahooemail | 6 | `██▁▁` |
| m:shaw | 3 | `█▁▅▁` |
| m:spectrum | 2 | `██▁▁` |
| m:rogers | 1 | `█▁▁▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:attachments | 11 | `▂█▆▁` |
| feat:calendar | 5 | `██▅▁` |
| feat:addons | 2 | `█▁▁▁` |
| feat:junk | 2 | `▁▁█▁` |
| feat:spellcheck | 1 | `█▁▁▁` |
| feat:addressbook | 1 | `█▁▁▁` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 8 | `▅█▅▁` |
| proto:smtp | 7 | `▅█▃▁` |
| proto:pop | 5 | `█▆▁▁` |
| proto:caldav | 2 | `▁██▁` |
| proto:oauth | 1 | `▁█▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 99 | `▇█▇▂` |
| os:linux | 7 | `█▆▆▁` |
| os:macos | 2 | `▁██▁` |
| os:android | 1 | `█▁▁▁` |
| os:other | 1 | `▁█▁▁` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:golden_gate | 1 | `▁█▁▁` |
| macos:catalina | 1 | `▁█▁▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward October 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
