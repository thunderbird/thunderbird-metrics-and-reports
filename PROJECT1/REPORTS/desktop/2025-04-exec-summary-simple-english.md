---
layout: base
title: "2025-04 exec summary in plain English: Thunderbird Desktop support spikes"
---

# April 2025 in plain English: Thunderbird Desktop support spikes

This page is a plain-English rewrite of the [April 2025 executive summary](2025-04-exec-summary.html).
The numbers are the same. Both pages come from the same 1173 Thunderbird Desktop
support questions of April 2025. No AI read the questions. The tool uses regular
expressions and standard statistics only. The source page carried the timestamp
2026-09-10 00:28 UTC.

## Words on this page

- A question is one post by a user on the Thunderbird support site.
- A cause tag says what a question is about. `m:gmail` is the mail host Gmail, and `proto:oauth` is the sign-in protocol OAuth. `av:avast` is the antivirus product Avast, and `feat:printing` is the printing feature of Thunderbird.
- A spike is a period with many more questions of one kind than normal.
- The baseline is the normal count for that kind of question. The tool takes the middle value of earlier periods.
- The rise is the measured count divided by the expected count. A rise of 3.0× means three times as many questions as expected.
- The grain is the length of the period that the tool measured: one day, one week, or one month.
- Served says how many of the questions got an answer from somebody other than the person who asked. Served also gives the time to the first answer.
- A version×cause spike ties a rise to one Thunderbird version and one cause. Such a spike points to a problem that a Thunderbird release caused.
- A cause-level spike ignores the version. Such a spike points to a problem at a mail host, in a protocol, in an antivirus product, or in one Thunderbird feature.

## Result for April 2025

The tool found four spikes worth a look in April 2025. All four are cause-level.
None of them tie to a Thunderbird version.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 0 | 0 | 0 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 3 | 1 |

The zero in the version×cause row is missing data, not a clean month. The support
site began to record the Thunderbird version of a question in April 2026. Only
questions from February 2026 onward carry that version in useful numbers. For April
2025 the tool cannot tie any spike to a version.

Three more numbers for context:

- Volume: 1173 questions. 510 of them (43%) carry a cause tag. The count per day
  was `█▆▅▅▄▆▇▆▆▆▆▄▄▇▇█▇▅▅▄▅▅▆▆▇▄▄█▇▇`, one block per day from April 1 to April 30.
- Answers: 904 of the 1173 questions (77%) got an answer from somebody other than the person who asked. The middle time to the first answer was 3.6 hours.
- Release-adoption version spikes: 0. Such spikes follow a new release and are not incidents.

## What the four spikes say

Printing was the story of April 2025. Questions about printing reached 24 for the
month, three times the baseline of 8. The same cluster fired in two separate
weeks, and the week of April 7 reached six times its baseline. Many of the
printing questions came from users who printed a PDF file or an attachment.
Sign-in questions (`proto:oauth`) reached three times the baseline in the week of
April 28. Users got good service in all four clusters: 67% to 83% of the
questions got an answer.

| Grain | Rise | When | Cause | Questions | Served | Baseline |
|:--|--:|:--|:--|--:|:--|--:|
| weekly | 6.0× | 2025-04-07 | feat:printing | 12 | 83% answered, 4.2h | 2.0 |
| weekly | 3.0× | 2025-04-28 | proto:oauth | 9 | 67% answered, 12.4h | 3.0 |
| weekly | 3.0× | 2025-04-14 | feat:printing | 6 | 83% answered, 1.4h | 2.0 |
| monthly | 3.0× | 2025-04 | feat:printing | 24 | 83% answered, 2.8h | 8.0 |

The example questions for each row are in the detail section below.

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day
the problem started. Users retry and wait before they post, so a spike usually
dates days after the start of a problem, often close to the fix. Use this page to
find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise
against the rate of that cause across all history. Questions that arrive later
therefore move the expected count for a past month. Rows can cross the threshold in both
directions, and the answered percentage rises as late answers land. This page is
a snapshot written by hand. The original page regenerates every day, and
`git log -p` on that file shows how its verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 4 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds.
The rows below came out of that second run and did not clear the real thresholds.
They are not incidents. They are context, so that a quiet month is not read as a
clean month.

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| daily | 2.7× | 2025-04-28 | m:gmail | 8 | 62% answered, 6.5h | 3.0 | [1508473](https://support.mozilla.org/questions/1508473 "undable to connect to gmail with thunderbird after thunderbird update") [1508490](https://support.mozilla.org/questions/1508490 "Microsofft Windows ＂Send to＂ Shortcut with Attachments") [1508499](https://support.mozilla.org/questions/1508499 "Cannot send email - Error ＂Sending of the message failed. The message could not ") [1508519](https://support.mozilla.org/questions/1508519 "Adding a Gmail mailbox in Thunderbird，but localhost refuses the request") [1508546](https://support.mozilla.org/questions/1508546 "Thunderbird Cannot Connect to Corporate Gmail After Okta Password Reset") [1508586](https://support.mozilla.org/questions/1508586 "Suddenly I can no longer send emails although I can receive them") +2 |
| monthly | 2.5× | 2025-04 | feat:notifications | 15 | 60% answered, 9.3h | 6.0 | [1503150](https://support.mozilla.org/questions/1503150 "New border around notification popup") [1504010](https://support.mozilla.org/questions/1504010 "Sound notifications") [1504103](https://support.mozilla.org/questions/1504103 "Random notifications") [1504726](https://support.mozilla.org/questions/1504726 "Email notifications in Calendar") [1505558](https://support.mozilla.org/questions/1505558 "Thunderbird Calendar  Please re- add the Reminder Notification via email !") [1505808](https://support.mozilla.org/questions/1505808 "Calendar reminder notifications window not showing in Windows 11") +9 |
| weekly | 2.2× | 2025-04-28 | feat:attachments | 9 | 78% answered, 9.8h | 4.0 | [1508474](https://support.mozilla.org/questions/1508474 "Cannot Rotate a JPEG Attachment in an E-mail") [1508490](https://support.mozilla.org/questions/1508490 "Microsofft Windows ＂Send to＂ Shortcut with Attachments") [1508576](https://support.mozilla.org/questions/1508576 "documents attached to strings of emails") [1508746](https://support.mozilla.org/questions/1508746 "Unable to open or save attachment") [1509229](https://support.mozilla.org/questions/1509229 "") [1509257](https://support.mozilla.org/questions/1509257 "") +3 |
| weekly | 2.2× | 2025-04-07 | feat:attachments | 9 | 78% answered, 12.2h | 4.0 | [1504522](https://support.mozilla.org/questions/1504522 "Attachments to a message will not be printed directly from Thunderbird.") [1504827](https://support.mozilla.org/questions/1504827 "allegati") [1505274](https://support.mozilla.org/questions/1505274 "Emails being quarantined dues to Thunderbird Filelink HTML attachments") [1505281](https://support.mozilla.org/questions/1505281 "Problem with printing email attachments") [1505330](https://support.mozilla.org/questions/1505330 "How to open attached file in email?") [1505373](https://support.mozilla.org/questions/1505373 "Problema trascinamento allegati su scrivania MacBook") +3 |

</details>

<details markdown="1">
<summary>The four cause-level spikes with example questions, 4 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 6.0× | 2025-04-07 | feat:printing | 12 | 83% answered, 4.2h | 2.0 | [1504337](https://support.mozilla.org/questions/1504337 "problemi stampa pdf") [1504385](https://support.mozilla.org/questions/1504385 "no pdf print - the system informs that there is no associated mail program in wi") [1504522](https://support.mozilla.org/questions/1504522 "Attachments to a message will not be printed directly from Thunderbird.") [1504666](https://support.mozilla.org/questions/1504666 "Zugferd   *.PDF Print") [1504872](https://support.mozilla.org/questions/1504872 "problemi stampa") [1505057](https://support.mozilla.org/questions/1505057 "Can't print attachement in PDF") +6 |
| weekly | 3.0× | 2025-04-28 | proto:oauth | 9 | 67% answered, 12.4h | 3.0 | [1508481](https://support.mozilla.org/questions/1508481 "OAuth2 popup is blank") [1508586](https://support.mozilla.org/questions/1508586 "Suddenly I can no longer send emails although I can receive them") [1508618](https://support.mozilla.org/questions/1508618 "Thunderbird Settings, here: POP3 Settings.") [1508668](https://support.mozilla.org/questions/1508668 "google oauth authentication page has ＂allow＂ outside the borders") [1509045](https://support.mozilla.org/questions/1509045 "I can receive emails - IMAP.gmail.com but can't send emails - SMTP.gmail.com") [1509287](https://support.mozilla.org/questions/1509287 "") +3 |
| weekly | 3.0× | 2025-04-14 | feat:printing | 6 | 83% answered, 1.4h | 2.0 | [1505912](https://support.mozilla.org/questions/1505912 "HP LASER JET 1020 prints blank pdf pages after latest update of thunderbird. Oth") [1505938](https://support.mozilla.org/questions/1505938 "stampa bianca") [1506136](https://support.mozilla.org/questions/1506136 "Print preview and Print...(NG)  in Thunderbird 102.15.1 (64-bit)") [1506201](https://support.mozilla.org/questions/1506201 "Impressão de PDF em branco pelo Thumderbird") [1506317](https://support.mozilla.org/questions/1506317 "Printing issue with attachments in Thunderbird") [1507077](https://support.mozilla.org/questions/1507077 "Nefunkční tisk PDF z Thunderbird") |
| monthly | 3.0× | 2025-04 | feat:printing | 24 | 83% answered, 2.8h | 8.0 | [1503165](https://support.mozilla.org/questions/1503165 "How to print out a single Thunderbird calendar event") [1504181](https://support.mozilla.org/questions/1504181 "Printing Calendars from Thunderbird - Team Events with extra data") [1504337](https://support.mozilla.org/questions/1504337 "problemi stampa pdf") [1504385](https://support.mozilla.org/questions/1504385 "no pdf print - the system informs that there is no associated mail program in wi") [1504522](https://support.mozilla.org/questions/1504522 "Attachments to a message will not be printed directly from Thunderbird.") [1504666](https://support.mozilla.org/questions/1504666 "Zugferd   *.PDF Print") +18 |

</details>

<details markdown="1">
<summary>Version × cause spikes, 0 rows</summary>

None. April 2025 has almost no version data.

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 0 rows</summary>

None.

</details>

<details markdown="1">
<summary>April 2025 trends</summary>

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

The tool ran its detectors at daily, weekly and monthly grain. A weekly period
counts toward April 2025 when its week overlaps the month. Version×cause needs a
known Thunderbird version, which the data carries only from 2026-02 onward.
Cause-level uses all history. The full spike tables are in
`PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
