---
layout: base
title: "2026-07 exec summary: Thunderbird Desktop support spikes"
---

# July 2026: Thunderbird Desktop support spikes

Executive summary for 2026-07. It covers 731 Thunderbird Desktop support questions. The tool wrote this page on 2026-09-10 04:50 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## July 2026: 6 spikes to investigate

All 6 tie to a Thunderbird version. None of them are cause-level. Every row is in the collapsed blocks below.

In short: Search and Attachments. Both are in [What stands out](#what-stands-out), with 2 smaller clusters.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 0 | 5 | 1 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 0 | 0 |

Three more numbers for context:

- Volume: 731 questions. 314 of them (43%) carry a cause tag. The count per day was `▆▇▅▆▄▇▇▆▇▆▄▃▇▇▄▅▄▅▄▇▆▅█▆▃▇▇▆▆▅▇`, one block per day from July 1 to July 31.
- Answers: 600 of the 731 questions (82%) got an answer from somebody other than the person who asked. The middle time to the first answer was 3.6 hours.
- Release-adoption version spikes: 15. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All July 2026 detail](#all-july-2026-detail) below.

## What stands out {#what-stands-out}

1. Search ([`feat:search`](explorer.html#grain=monthly&cause=feat:search&period=2026-07), 2 spikes): 10 questions in July, under the monthly bar. It peaked in the week of 2026-07-06 at 12.5 times expected, on Thunderbird 140.
2. Attachments ([`feat:attachments`](explorer.html#grain=monthly&cause=feat:attachments&period=2026-07), 2 spikes): 16 questions in July, under the monthly bar. It peaked in the week of 2026-07-06 at 3.9 times expected, on Thunderbird 152.
3. Junk mail ([`feat:junk`](explorer.html#grain=monthly&cause=feat:junk&period=2026-07), 1 spike): 13 questions in July, under the monthly bar. It peaked in the week of 2026-06-29 at 3.2 times expected, on Thunderbird 140.
4. Comcast ([`m:comcast`](explorer.html#grain=monthly&cause=m:comcast&period=2026-07), 1 spike): 13 questions in July, under the monthly bar. It peaked in the week of 2026-07-27 at 3.1 times expected, on Thunderbird 153.

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 3 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Version and cause together:

| Grain | Lift | When | Version × Cause | Questions | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| daily | 2.7× | 2026-07-02 | v152 × proto:imap | 4 | 50% answered (below 60%), 7.6h | [1590718](https://support.mozilla.org/questions/1590718 "Accidentally moved IMAP Gmail label to Local Folders - Emails disappeared, Local") [1590790](https://support.mozilla.org/questions/1590790 "Thunderbird and GoDaddy account") [1590808](https://support.mozilla.org/questions/1590808 "Forwarded attachments disappear after first IMAP draft save and subsequent saves") [1590848](https://support.mozilla.org/questions/1590848 "Continue to have ＂Authentication Required＂ POPup errors at startup.") |
| weekly | 2.7× | 2026-07-06 | v152 × proto:oauth | 5 | 80% answered, 5.4h | [1591762](https://support.mozilla.org/questions/1591762 "Even with verions 152.01, Oauth for smtp through Yahoo.com is not an available c") [1591813](https://support.mozilla.org/questions/1591813 "Oauth challenge never appears") [1591979](https://support.mozilla.org/questions/1591979 "Outlook: OAuth Authentication failure with IMAP") [1592379](https://support.mozilla.org/questions/1592379 "Gmail oauth gives Authentication failure after restarting Thunderbird") [1592479](https://support.mozilla.org/questions/1592479 "cannot set OAuth authentication method in Thunderbird 152.0.1") |
| weekly | 2.5× | 2026-07-06 | v140 × proto:smtp | 5 | 100% answered, 6.1h | [1591795](https://support.mozilla.org/questions/1591795 "Impossibile inviare messaggi") [1591885](https://support.mozilla.org/questions/1591885 "Can't find outgoing server after login following Win 11 sleeps") [1591986](https://support.mozilla.org/questions/1591986 "After the last Thunderbird update I cannot send e-mails but still receive emails") [1592019](https://support.mozilla.org/questions/1592019 "IMAP, SMTP и POP3") [1592468](https://support.mozilla.org/questions/1592468 "I have problems with my Orcon emails and they say it is Thunderbird.") |


</details>

---

## All July 2026 detail {#all-july-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 6 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| weekly | 12.5× | 2026-07-06 | v140 × feat:search | 5 | 100% answered, 2.6h | new | [1591417](https://support.mozilla.org/questions/1591417 "How to prevent Thunderbird message search (ctrl+F) from continuing from the top?") [1591550](https://support.mozilla.org/questions/1591550 "Copying a saved search in Thunderbird") [1591650](https://support.mozilla.org/questions/1591650 "Searching by domain - issue?") [1592237](https://support.mozilla.org/questions/1592237 "Before the last update to TB I could easily search for a single email address me") [1592460](https://support.mozilla.org/questions/1592460 "Can I create a search based on text in the ＂message source＂?") |
| weekly | 3.9× | 2026-07-06 | v152 × feat:attachments | 6 | 83% answered, 9.4h | spreading | [1591539](https://support.mozilla.org/questions/1591539 "Couldn't forward attachment which I received.") [1591623](https://support.mozilla.org/questions/1591623 "Adding items to the files & attachment section") [1591963](https://support.mozilla.org/questions/1591963 "sending of the message failed. there was an error attaching file. please check t") [1592003](https://support.mozilla.org/questions/1592003 "**Intermittent error when forwarding emails with attachments (IMAP, Windows 11)*") [1592159](https://support.mozilla.org/questions/1592159 "In un ambiente aziendale, gli archivi localizzati o in dischi in rete o locali n") [1592598](https://support.mozilla.org/questions/1592598 "PDF file attachment does not print correctly") |
| monthly | 3.8× | 2026-07 | v140 × feat:search | 7 | 100% answered, 3.5h | new | [1591417](https://support.mozilla.org/questions/1591417 "How to prevent Thunderbird message search (ctrl+F) from continuing from the top?") [1591550](https://support.mozilla.org/questions/1591550 "Copying a saved search in Thunderbird") [1591650](https://support.mozilla.org/questions/1591650 "Searching by domain - issue?") [1592237](https://support.mozilla.org/questions/1592237 "Before the last update to TB I could easily search for a single email address me") [1592460](https://support.mozilla.org/questions/1592460 "Can I create a search based on text in the ＂message source＂?") [1592700](https://support.mozilla.org/questions/1592700 "Unable to see messages in Inbox but messages visible using search. Repair folder") +1 |
| weekly | 3.7× | 2026-07-20 | v140 × feat:attachments | 4 | 75% answered, 4.7h | spreading | [1593912](https://support.mozilla.org/questions/1593912 "How to open an attachment in Thunderbird?") [1594596](https://support.mozilla.org/questions/1594596 "Attachment preview problem") [1594642](https://support.mozilla.org/questions/1594642 "Delete attachments Thunderbird has opened.") [1594710](https://support.mozilla.org/questions/1594710 "Thunderbird email attachments disappear when message trashed") |
| weekly | 3.2× | 2026-06-29 | v140 × feat:junk | 4 | 100% answered, 6.7h | new | [1590147](https://support.mozilla.org/questions/1590147 "Way to Get spam and fake sites off") [1590586](https://support.mozilla.org/questions/1590586 "Mijn pc zou spam versturen.") [1590755](https://support.mozilla.org/questions/1590755 "How to run junk mail filters on a particular folder") [1591038](https://support.mozilla.org/questions/1591038 "How do I install a junk folder in with the other folders ( inbox, drafts, sent, ") |
| weekly | 3.1× | 2026-07-27 | v153 × m:comcast | 4 | 75% answered, 5.4h | spreading | [1595937](https://support.mozilla.org/questions/1595937 "Need help recovering my profile from a zip file") [1595941](https://support.mozilla.org/questions/1595941 "Why can't Thunderbird use new yahoo email platform for Comcast on MacBook Air?") [1596164](https://support.mozilla.org/questions/1596164 "With version 153: Unable to send from gmail account.  And cannot create a new gm") [1596297](https://support.mozilla.org/questions/1596297 "Trying to set APP Password to connect with Yahoo Mail conversion at Comcast.") |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 0 rows</summary>

None.

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 15 rows</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | 3.1× | 2026-07-01 | tb_version_major | 152 | 11 [1590558](https://support.mozilla.org/questions/1590558 "Chyba editoru při přeposílání (inline): Uzamčení dočasných souborů v Tempu při u") [1590593](https://support.mozilla.org/questions/1590593 "Too much disk space used by Thunderbird") | 3.5 |
| daily | new | 2026-07-23 | tb_version_major | 153 | 11 [1594355](https://support.mozilla.org/questions/1594355 "not sure i  lke the new version") [1594359](https://support.mozilla.org/questions/1594359 "How do I remove the English (US) dictionary from Thunderbird") | 0.0 |
| daily | new | 2026-07-24 | tb_version_major | 153 | 8 [1594604](https://support.mozilla.org/questions/1594604 "＂Current operation on Inbox did not succeed for yahoo account") [1594673](https://support.mozilla.org/questions/1594673 "Can't get back to inbox from local folders") | 0.0 |
| daily | new | 2026-07-26 | tb_version_major | 153 | 15 [1594896](https://support.mozilla.org/questions/1594896 "Lost my password") [1594901](https://support.mozilla.org/questions/1594901 "When opening Tbird 153.0, several servers give authentication errors") | 0.0 |
| daily | new | 2026-07-27 | tb_version_major | 153 | 11 [1595089](https://support.mozilla.org/questions/1595089 "add a yohoo email account") [1595090](https://support.mozilla.org/questions/1595090 "backup zip ,841mb ,will not import into thunderbird") | 0.0 |
| daily | new | 2026-07-28 | tb_version_major | 153 | 11 [1595265](https://support.mozilla.org/questions/1595265 "How to delete duplicate folders in three email acounts?") [1595273](https://support.mozilla.org/questions/1595273 "Adding a hotmail email account to Thunderbird 153.0 (64-bit) on Windows 11 Home ") | 0.0 |
| daily | new | 2026-07-30 | tb_version_major | 153 | 9 [1595713](https://support.mozilla.org/questions/1595713 "Why do deleted emails remain in my All Mail box?") [1595723](https://support.mozilla.org/questions/1595723 "Thunderbird editor line spacing") | 0.0 |
| daily | new | 2026-07-31 | tb_version_major | 153 | 18 [1595834](https://support.mozilla.org/questions/1595834 "Compacting folders progress bar") [1595845](https://support.mozilla.org/questions/1595845 "are you able to use thunderbird email without primary password") | 0.0 |
| monthly | new | 2026-07 | tb_version_major | 153 | 101 [1590618](https://support.mozilla.org/questions/1590618 "When a proper repository for .deb packages will be available?") [1590771](https://support.mozilla.org/questions/1590771 "Can't sign in to Thunderbird") | 0.0 |
| monthly | 422.0× | 2026-07 | tb_version_major | 152 | 211 [1590558](https://support.mozilla.org/questions/1590558 "Chyba editoru při přeposílání (inline): Uzamčení dočasných souborů v Tempu při u") [1590593](https://support.mozilla.org/questions/1590593 "Too much disk space used by Thunderbird") | 0.5 |
| monthly | 3.1× | 2026-07 | tb_version_major | 150 | 26 [1590853](https://support.mozilla.org/questions/1590853 "Have difficulty deleting emails") [1591057](https://support.mozilla.org/questions/1591057 "Thunderbird Error Message : Authentication Error :  Unable To Log in at Server. ") | 8.5 |
| weekly | 52.0× | 2026-06-29 | tb_version_major | 152 | 78 [1590162](https://support.mozilla.org/questions/1590162 "Funzionamento QRcode per condigurazione Tablet da PC (Trasferimento account)") [1590178](https://support.mozilla.org/questions/1590178 "Adding 2nd outlook accound") | 1.5 |
| weekly | 26.0× | 2026-07-06 | tb_version_major | 152 | 65 [1591418](https://support.mozilla.org/questions/1591418 "Pulsante ＂Esegui ora＂ del filtro messaggi non disponibile") [1591432](https://support.mozilla.org/questions/1591432 "code-uitvoering kan niet worden voortgezet") | 2.5 |
| weekly | new | 2026-07-20 | tb_version_major | 153 | 43 [1594201](https://support.mozilla.org/questions/1594201 "LỖi đăng nhập hotmail, email") [1594241](https://support.mozilla.org/questions/1594241 "Connection reset errors for CalDAV calendars when staritng Thunderbird") | 0.0 |
| weekly | new | 2026-07-27 | tb_version_major | 153 | 79 [1595089](https://support.mozilla.org/questions/1595089 "add a yohoo email account") [1595090](https://support.mozilla.org/questions/1595090 "backup zip ,841mb ,will not import into thunderbird") | 0.0 |

</details>

<details markdown="1">
<summary>July 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v152 | 211 | `▆█▄▆▃▆▇▆▆▄▂▃▆█▄▃▁▆▃▅▆▂▂▁▁▂▁▂▂▁▁` |
| v140 | 186 | `▅▆▆▇▆▇▅▅█▅▄▂▅▅▅▅▆▄▅▇▅▅▅█▂▇▅▄▇▃▅` |
| v153 | 101 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▅▄▃▇▅▅▄▅█` |
| v150 | 26 | `▁▃▃▁▁▃█▁▆▃▆▁▃▁▁▃▁█▆▆▆▃▁▁▁▃▁▃▃▁▁` |
| v115 | 16 | `▆▃▁▁▁▃▁▁▆▁▁▃▁▃▁▁▆▁▁▁▁▁▆▁▁▁▁▁█▁▃` |
| v149 | 6 | `█▁█▁▁▁▁▁▁▁▁▁█▁▁█▁▁█▁▁▁▁▁▁▁█▁▁▁▁` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 73 | `▃▅▅▅▆▂▃▅▅▆▅▁▁▆▁▃▅▅▂▁▁▅▂█▂█▃▅▂▆▃` |
| m:microsoftemail | 36 | `▁▅▃▂▂▁▁▃█▁▁▅▁▅▁▃▂▁▁▃▂▃▂▁▁▂▃▂▂▂▁` |
| m:yahooemail | 30 | `▃▅▃▁▆▃▃▃▃▃▁▃▃▁▁▁▁▃▃▁▃▁▁▅▁▅▃█▅▁▅` |
| m:comcast | 13 | `▁▅▁▅▁▁▁▅█▁▁▁▁▅▅▁▁▅▁▁▁▁▅▁▁▅▁▁▅▁█` |
| m:icloud | 6 | `▁▅▁▁▁▁▁█▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁` |
| m:btinternet | 6 | `▁▁▁▁▁▁█▁▁█▁▁▁▁▁█▁▁▁▁█▁█▁▁▁▁▁▁█▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:import_export | 27 | `▃▆▃▁▁▁▆▆▃▃▁▃▃▆▃▁▁▁▁█▁▁▆▁▃█▃▁▁▁▆` |
| feat:filters | 17 | `▅▅▁▁▁█▁▁▅▁▁▁▅▁▁▅▁▅▁█▅▅▅▁▁▁▅▁▅▁█` |
| feat:attachments | 16 | `▁▃▁▁▁▃▃▁▅▃▁▃▁▁▁▁▁▁▁▃▁▁▁█▁▁▅▁▅▁▁` |
| feat:calendar | 16 | `▁▁▃▃▁▃▁█▁▁▁▁▃▃▁▁▃▁▃▃▁▆▃▁▁▃▁▁▁▁▃` |
| feat:addressbook | 14 | `▃▁▁▁▁▁▃▃▁▁▁▁▁▁▁▃▃█▁▁▁▁▃▁▁▁▁▁▆▃▆` |
| feat:junk | 13 | `▃▃▃▁▃▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▃▁▁▃▁▅▁▁▁█▁` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 56 | `▂▇▄▄▂▅▄▄█▁▁▄▂▄▂▂▂█▁▄▄▄▇▁▁▅▅▂▄▁▄` |
| proto:pop | 42 | `▁▃▃▅█▅█▅▅▁▁▃▅▁▃▁▁█▅▁▃▃▃▅▃▁▃▆▁▃▆` |
| proto:smtp | 35 | `▂▂▂▁▂▁▄▇█▁▁▂▁▂▄▂▁▁▂▂█▄▁▁▂▂▂▁▂▂▂` |
| proto:oauth | 20 | `▁▅▁▅▁▁▁██▁▅▅▅▅▁▅▅▁▁▁█▁▁▁▅█▅█▁▁▁` |
| proto:caldav | 3 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁` |
| proto:ews | 1 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

The antivirus products named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| av:norton | 3 | `▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█` |
| av:bitdefender | 2 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:eset | 2 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |
| av:avast | 2 | `▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:defender | 2 | `▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█` |
| av:mcafee | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 589 | `▅▆▅▅▄▆▇▆▇▅▄▃▇▇▄▅▄▅▄▇▇▅█▆▂▆▇▆▆▄█` |
| os:linux | 61 | `▇▅▆▁▁▁▃▃▂▂▁▁▅▂▁▃▅▂▂▃▁▅▇▁▃█▅▆▃▅▃` |
| os:macos | 45 | `▂█▁▄▁█▁▅▂▄▂▄▄▄▄▁▂▅▁▄▁▂▄▄▁▁▂▁▅▂▂` |
| os:other | 11 | `▅▅█▅▁▁▁▁▁▅▁▁▁▅▁▅▁▁▁▁▁▅▁▅▁▁▅▁▁▁▁` |
| os:android | 7 | `█▁▁▁█▁█▁██▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:tahoe | 5 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁` |
| macos:sequoia | 2 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁` |
| macos:sonoma | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sierra | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |
| macos:monterey | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward July 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
