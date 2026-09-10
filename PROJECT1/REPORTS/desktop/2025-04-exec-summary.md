---
layout: base
title: "2025-04 exec summary: Thunderbird Desktop support spikes"
---

# April 2025: Thunderbird Desktop support spikes

Executive summary for 2025-04. It covers 1173 Thunderbird Desktop support questions. The tool wrote this page on 2026-09-10 04:38 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## April 2025: 4 spikes to investigate

None of them tie to a Thunderbird version. All 4 are cause-level. Every row is in the collapsed blocks below.

In short: Printing and OAuth. The list below has the detail.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 0 | 0 | 0 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 3 | 1 |

Almost no April 2025 question carries a Thunderbird version. The version×cause detector therefore cannot fire. Read its zero as missing data, not as a clean result.

Three more numbers for context:

- Volume: 1173 questions. 510 of them (43%) carry a cause tag. The count per day was `█▆▅▅▄▆▇▆▆▆▆▄▄▇▇█▇▅▅▄▅▅▆▆▇▄▄█▇▇`, one block per day from April 1 to April 30.
- Answers: 904 of the 1173 questions (77%) got an answer from somebody other than the person who asked. The middle time to the first answer was 3.6 hours.
- Release-adoption version spikes: 0. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All April 2025 detail](#all-april-2025-detail) below.

## What stands out

1. Printing ([`feat:printing`](explorer.html#grain=monthly&cause=feat:printing&period=2025-04), 3 spikes): 24 questions in April, 3.0 times the baseline of 8.0. It peaked in the week of 2025-04-07 at 6.0 times its baseline.
2. OAuth ([`proto:oauth`](explorer.html#grain=monthly&cause=proto:oauth&period=2025-04), 1 spike): 19 questions in April, under the monthly bar. It peaked in the week of 2025-04-28 at 3.0 times its baseline.

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 4 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| daily | 2.7× | 2025-04-28 | m:gmail | 8 | 62% answered, 6.5h | 3.0 | [1508473](https://support.mozilla.org/questions/1508473 "undable to connect to gmail with thunderbird after thunderbird update") [1508490](https://support.mozilla.org/questions/1508490 "Microsofft Windows ＂Send to＂ Shortcut with Attachments") [1508499](https://support.mozilla.org/questions/1508499 "Cannot send email - Error ＂Sending of the message failed. The message could not ") [1508519](https://support.mozilla.org/questions/1508519 "Adding a Gmail mailbox in Thunderbird，but localhost refuses the request") [1508546](https://support.mozilla.org/questions/1508546 "Thunderbird Cannot Connect to Corporate Gmail After Okta Password Reset") [1508586](https://support.mozilla.org/questions/1508586 "Suddenly I can no longer send emails although I can receive them") +2 |
| monthly | 2.5× | 2025-04 | feat:notifications | 15 | 60% answered, 9.3h | 6.0 | [1503150](https://support.mozilla.org/questions/1503150 "New border around notification popup") [1504010](https://support.mozilla.org/questions/1504010 "Sound notifications") [1504103](https://support.mozilla.org/questions/1504103 "Random notifications") [1504726](https://support.mozilla.org/questions/1504726 "Email notifications in Calendar") [1505558](https://support.mozilla.org/questions/1505558 "Thunderbird Calendar  Please re- add the Reminder Notification via email !") [1505808](https://support.mozilla.org/questions/1505808 "Calendar reminder notifications window not showing in Windows 11") +9 |
| weekly | 2.2× | 2025-04-28 | feat:attachments | 9 | 78% answered, 9.8h | 4.0 | [1508474](https://support.mozilla.org/questions/1508474 "Cannot Rotate a JPEG Attachment in an E-mail") [1508490](https://support.mozilla.org/questions/1508490 "Microsofft Windows ＂Send to＂ Shortcut with Attachments") [1508576](https://support.mozilla.org/questions/1508576 "documents attached to strings of emails") [1508746](https://support.mozilla.org/questions/1508746 "Unable to open or save attachment") [1509229](https://support.mozilla.org/questions/1509229 "attachment for emails") [1509257](https://support.mozilla.org/questions/1509257 "Thunderbird 128.10.0 Filter's not saving email with attachment") +3 |
| weekly | 2.2× | 2025-04-07 | feat:attachments | 9 | 78% answered, 12.2h | 4.0 | [1504522](https://support.mozilla.org/questions/1504522 "Attachments to a message will not be printed directly from Thunderbird.") [1504827](https://support.mozilla.org/questions/1504827 "allegati") [1505274](https://support.mozilla.org/questions/1505274 "Emails being quarantined dues to Thunderbird Filelink HTML attachments") [1505281](https://support.mozilla.org/questions/1505281 "Problem with printing email attachments") [1505330](https://support.mozilla.org/questions/1505330 "How to open attached file in email?") [1505373](https://support.mozilla.org/questions/1505373 "Problema trascinamento allegati su scrivania MacBook") +3 |


</details>

---

## All April 2025 detail {#all-april-2025-detail}

<details markdown="1">
<summary>Version × cause spikes, 0 rows</summary>

None.

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 4 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 6.0× | 2025-04-07 | feat:printing | 12 | 83% answered, 4.2h | 2.0 | [1504337](https://support.mozilla.org/questions/1504337 "problemi stampa pdf") [1504385](https://support.mozilla.org/questions/1504385 "no pdf print - the system informs that there is no associated mail program in wi") [1504522](https://support.mozilla.org/questions/1504522 "Attachments to a message will not be printed directly from Thunderbird.") [1504666](https://support.mozilla.org/questions/1504666 "Zugferd   *.PDF Print") [1504872](https://support.mozilla.org/questions/1504872 "problemi stampa") [1505057](https://support.mozilla.org/questions/1505057 "Can't print attachement in PDF") +6 |
| weekly | 3.0× | 2025-04-28 | proto:oauth | 9 | 67% answered, 12.4h | 3.0 | [1508481](https://support.mozilla.org/questions/1508481 "OAuth2 popup is blank") [1508586](https://support.mozilla.org/questions/1508586 "Suddenly I can no longer send emails although I can receive them") [1508618](https://support.mozilla.org/questions/1508618 "Thunderbird Settings, here: POP3 Settings.") [1508668](https://support.mozilla.org/questions/1508668 "google oauth authentication page has ＂allow＂ outside the borders") [1509045](https://support.mozilla.org/questions/1509045 "I can receive emails - IMAP.gmail.com but can't send emails - SMTP.gmail.com") [1509287](https://support.mozilla.org/questions/1509287 "Hotmail is niet werkend te krijgen met Oauth2") +3 |
| weekly | 3.0× | 2025-04-14 | feat:printing | 6 | 83% answered, 1.4h | 2.0 | [1505912](https://support.mozilla.org/questions/1505912 "HP LASER JET 1020 prints blank pdf pages after latest update of thunderbird. Oth") [1505938](https://support.mozilla.org/questions/1505938 "stampa bianca") [1506136](https://support.mozilla.org/questions/1506136 "Print preview and Print...(NG)  in Thunderbird 102.15.1 (64-bit)") [1506201](https://support.mozilla.org/questions/1506201 "Impressão de PDF em branco pelo Thumderbird") [1506317](https://support.mozilla.org/questions/1506317 "Printing issue with attachments in Thunderbird") [1507077](https://support.mozilla.org/questions/1507077 "Nefunkční tisk PDF z Thunderbird") |
| monthly | 3.0× | 2025-04 | feat:printing | 24 | 83% answered, 2.8h | 8.0 | [1503165](https://support.mozilla.org/questions/1503165 "How to print out a single Thunderbird calendar event") [1504181](https://support.mozilla.org/questions/1504181 "Printing Calendars from Thunderbird - Team Events with extra data") [1504337](https://support.mozilla.org/questions/1504337 "problemi stampa pdf") [1504385](https://support.mozilla.org/questions/1504385 "no pdf print - the system informs that there is no associated mail program in wi") [1504522](https://support.mozilla.org/questions/1504522 "Attachments to a message will not be printed directly from Thunderbird.") [1504666](https://support.mozilla.org/questions/1504666 "Zugferd   *.PDF Print") +18 |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 0 rows</summary>

None.

</details>

<details markdown="1">
<summary>April 2025 trends, 7 rows</summary>

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 109 | `▄▅▂▄▄▄▃▁▇▁▃▄▄▅▄▇▃▄▅▃▂▄▇▄▅▃▅█▇▇` |
| m:microsoftemail | 69 | `▇▄▄▂▅▅▂▁▇▂█▁▅▄▇█▁▂▂▁▄▄▄▁▂▇▅█▅█` |
| m:yahooemail | 19 | `█▁▁▃▁▃▁▁▃▃▃▁▆▃▃▁▁▁▆▁▁▃▆▁▁▁▁▆▁▁` |
| m:comcast | 12 | `▁▁▅▅▁▅▅▁▁▁▅▁▁▅▁▁▁▁▅▁▁▅▅▁▁▁▁█▁▅` |
| m:spectrum | 10 | `▁▁▁▁▅▁▁▅▁▁▅▅▁█▁▁▅▁▁▁▁▁▁▁▁▁▅█▁▁` |
| m:icloud | 6 | `▁▁▁▁▁▅▁▁▁▁█▁▁▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:calendar | 36 | `█▁▁▁▁▄▁▅▄▁▂▇▂▁▇▂▄▂▂▁▄▁▄▂▁▁▁▂▂▄` |
| feat:import_export | 33 | `▃▁▃▁▁█▆▁▃▁▃▃▁▁▅▅▃▆▁▃▅▁▅▅▁▁▁▃▅▆` |
| feat:attachments | 32 | `▄▄▁▂▁▁▁▂▂▁█▂▂▄▁▇▂▄▁▂▁▂▂▁▄▁▁▅▂▁` |
| feat:junk | 29 | `█▃▁▃▃▆▁▃▁▁▅▁▃▁▆▃▁▅▅▃▁▃▃▃▃▁▃▁▁▃` |
| feat:printing | 24 | `▃▁▁▁▁▃▆▆▃██▁▃▆▆▃▁▁▁▃▁▁▁█▃▁▁▁▁▁` |
| feat:filters | 19 | `▁▁▅▁▅▅▅▁▅▁▁▁▅▁██▅▅▁▁▁▅▁▅▅▁▅▅▁█` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 81 | `▅▇▅▆▆▅▅▁▅▂▂▁▁▂▇▆▅▇▂▅▅▂▃▃▅▂▅▆█▆` |
| proto:pop | 54 | `▃▅▅▂▂▅▂▁▂▂▁▂▂▅▂▃▃▆▃▂▂▂▆▂▃▃▂█▃▂` |
| proto:smtp | 51 | `▂▅▂▄▅▂▂▁▂▄▄▁▂▂▄▇▁▄▂▁▄▁█▁▁▇▅█▂▅` |
| proto:oauth | 19 | `▁▁▁▃▃▃▁▁▁▁▆▁▁▃▃▃▁▃▁▁▁▁█▃▁▁▃█▃▃` |
| proto:carddav | 2 | `▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:caldav | 2 | `▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

The antivirus products named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| av:avast | 3 | `▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁` |
| av:defender | 2 | `▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:bitdefender | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁█` |
| av:norton | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁█▁▁▁▁▁` |
| av:mcafee | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁` |
| av:malwarebytes | 1 | `█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 150 | `▅▆▄▄▃█▅▅▇█▄▅▂▇▅▆▄▂▅▂▅▃▅▄▂▃▅▇▂▅` |
| os:linux | 37 | `▃▁▁▁▃▃▅▃▁▃▁█▁▃▅▃▃▃▅▁▅▆▅▃▆▃▃▅▅▃` |
| os:macos | 19 | `▅▅▅▁█▁▅█▅▁▅▁▁▅▁▅▅█▁▁█▁▁▁▅▅▁▁▁▁` |
| os:android | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁██▁` |
| os:other | 1 | `█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:sequoia | 9 | `▁▁▅▁█▁▁▁▁▁▅▁▁▅▁▅▅▅▁▁▅▁▁▁▁▁▁▁▁▁` |
| macos:ventura | 1 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:mavericks | 1 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:monterey | 1 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sonoma | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:catalina | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward April 2025 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
