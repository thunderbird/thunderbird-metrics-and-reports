---
layout: base
title: "2026-11 exec summary: Thunderbird Desktop support spikes"
---

# November 2026: Thunderbird Desktop support spikes

Executive summary for 2026-11. It covers 250 Thunderbird Desktop support questions. The tool wrote this page on 2026-11-10 05:31 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## November 2026: 6 spikes to investigate

4 of them tie to a Thunderbird version. 2 of them are cause-level. Every row is in the collapsed blocks below.

November 2026 is still in progress. The counts will grow.

In short: Calendar and OAuth. Both are in [What stands out](#what-stands-out), with 2 smaller clusters.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 2 | 2 | 0 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 2 | 0 |

Three more numbers for context:

- Volume: 250 questions. 119 of them (48%) carry a cause tag. The count per day was `▆██▇▇▆▅▅█▂`, one block per day from November 1 to November 10.
- Answers: 179 of the 250 questions (72%) got an answer from somebody other than the person who asked. The middle time to the first answer was 2.0 hours.
- Release-adoption version spikes: 15. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All November 2026 detail](#all-november-2026-detail) below.

## What stands out {#what-stands-out}

1. Calendar ([`feat:calendar`](explorer.html#grain=monthly&cause=feat:calendar&period=2026-11), 3 spikes): 13 questions in November, under the monthly bar. It peaked on 2026-11-01 at 8.8 times expected, on Thunderbird 159.
2. OAuth ([`proto:oauth`](explorer.html#grain=monthly&cause=proto:oauth&period=2026-11), 1 spike): 6 questions in November, under the monthly bar. It peaked in the week of 2026-10-26 at 7.0 times expected, on Thunderbird 158.
3. Spectrum ([`m:spectrum`](explorer.html#grain=monthly&cause=m:spectrum&period=2026-11), 1 spike): 9 questions in November, under the monthly bar. It peaked in the week of 2026-11-02 at 3.5 times its baseline.
4. Gmail ([`m:gmail`](explorer.html#grain=monthly&cause=m:gmail&period=2026-11), 1 spike): 21 questions in November, under the monthly bar. It peaked on 2026-11-05 at 3.1 times expected, on Thunderbird 159.

In 4 clusters, fewer than 60% of the questions got an answer: `v159 × feat:calendar` on 2026-11-01 (25% answered), `v159 × m:gmail` on 2026-11-05 (50% answered), `v158 × proto:oauth` in the week of 2026-10-26 (0% answered), `feat:calendar` in the week of 2026-10-26 (56% answered).

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 6 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Version and cause together:

| Grain | Lift | When | Version × Cause | Questions | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| weekly | 3.0× | 2026-10-26 | v153 × proto:oauth | 4 | 50% answered (below 60%), 2.9h | [1614258](https://support.mozilla.org/questions/1614258 "Yahoo-Mail lässt sich in Thunderbird 153.5 unter macOS nicht anmelden – „Es ist ") [1614417](https://support.mozilla.org/questions/1614417 "Thunderbird Hotmail Problem") [1614449](https://support.mozilla.org/questions/1614449 "I am receiving regular Thunderbird notifications of errors for a Yahoo mail acco") [1615236](https://support.mozilla.org/questions/1615236 "Outlook.com SMTP OAuth2 authentication fails with error 535 despite successful s") |
| weekly | 2.5× | 2026-10-26 | v153 × feat:attachments | 4 | 75% answered, 2.4h | [1614267](https://support.mozilla.org/questions/1614267 "Problema invio allegati") [1614411](https://support.mozilla.org/questions/1614411 "Why are Symbolic links in thunderbird attachments replaced with target?") [1614932](https://support.mozilla.org/questions/1614932 "Ifound an email using search but the contents are empty How can I see contents/a") [1614975](https://support.mozilla.org/questions/1614975 "Adding attachments") |
| monthly | 2.5× | 2026-11 | v159 × feat:calendar | 10 | 50% answered (below 60%), 1.1h | [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615363](https://support.mozilla.org/questions/1615363 "TB 159 - Graph Calendar not automatically detected on account setup") [1615397](https://support.mozilla.org/questions/1615397 "Make Calendar Notification Window AlwaysOnTop") [1615399](https://support.mozilla.org/questions/1615399 "＂Thunderbird＂ access to Calendar functions are NOT FUNCTIONING at all. Thanks fo") [1615555](https://support.mozilla.org/questions/1615555 "Thunderbird Calendar does not react anymore - how can it be reactivated?") [1615605](https://support.mozilla.org/questions/1615605 "events missing from calendar on one pc,  other pc ok") +4 |
| weekly | 2.3× | 2026-11-02 | v159 × m:spectrum | 4 | 75% answered, 3.1h | [1616136](https://support.mozilla.org/questions/1616136 "Intermittent server refusals on Spectrum") [1616242](https://support.mozilla.org/questions/1616242 "Issue is with spectrum server mail.twc.com   error message sending and rec e mai") [1616383](https://support.mozilla.org/questions/1616383 "Not able to send mail") [1616559](https://support.mozilla.org/questions/1616559 "ACCESS TO INCOMING SERVER FAILED") |
| monthly | 2.3× | 2026-11 | v159 × feat:junk | 7 | 57% answered (below 60%), 2.3h | [1615531](https://support.mozilla.org/questions/1615531 "Thunderbird does not download SPAM until I open the spam folder") [1615533](https://support.mozilla.org/questions/1615533 "Thunderbird has changed!  I now have 2 spam folders and my normal senders are go") [1615795](https://support.mozilla.org/questions/1615795 "Spam Folder") [1615828](https://support.mozilla.org/questions/1615828 "Spam folder shows there are messages but when I open it nothing is there.") [1616310](https://support.mozilla.org/questions/1616310 "De map Prullenbak (eerst Trash) wordt na een bepaalde tijd ongewenst automatisch") [1616825](https://support.mozilla.org/questions/1616825 "I have no spam folder just downloaded Thunderbird last week") +1 |

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.3× | 2026-11-02 | feat:addressbook | 7 | 100% answered, 1.2h | 3.0 | [1615608](https://support.mozilla.org/questions/1615608 "Need to download address book but cannot find MAB file, only abook.sqlite files") [1615725](https://support.mozilla.org/questions/1615725 "Why can't I edit my contacts in yahoo.co.uk") [1615821](https://support.mozilla.org/questions/1615821 "How to move entries between address books and import") [1616089](https://support.mozilla.org/questions/1616089 "I just transferred Thunderbird to new laptop. emails are still there but not con") [1616151](https://support.mozilla.org/questions/1616151 "Address Book Every Entry Is Duplicated") [1616334](https://support.mozilla.org/questions/1616334 "The functionality of the addressbook is frustrating") +1 |


</details>

---

## All November 2026 detail {#all-november-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 4 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | 8.8× | 2026-11-01 | v159 × feat:calendar | 4 | 25% answered (below 60%), 0.5h | spreading | [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615363](https://support.mozilla.org/questions/1615363 "TB 159 - Graph Calendar not automatically detected on account setup") [1615397](https://support.mozilla.org/questions/1615397 "Make Calendar Notification Window AlwaysOnTop") [1615399](https://support.mozilla.org/questions/1615399 "＂Thunderbird＂ access to Calendar functions are NOT FUNCTIONING at all. Thanks fo") |
| weekly | 7.0× | 2026-10-26 | v158 × proto:oauth | 5 | 0% answered (below 60%) | spreading | [1614222](https://support.mozilla.org/questions/1614222 "Outlook.de receives mail but cannot send with OAuth2: “SmtpClientAuthentication ") [1614358](https://support.mozilla.org/questions/1614358 "Thunderbird has stopped downloading emails from Yahoo") [1614376](https://support.mozilla.org/questions/1614376 "Outlook email account can receive mail but loses authentication and stop sending") [1614513](https://support.mozilla.org/questions/1614513 "Thunderbird 158.1 receives emails from my new Outlook.com account but cannot sen") [1614656](https://support.mozilla.org/questions/1614656 "Authentication Failure (outlook)") |
| weekly | 5.1× | 2026-10-26 | v159 × feat:calendar | 10 | 70% answered, 17.5h | spreading | [1614718](https://support.mozilla.org/questions/1614718 "How do I turn off the sound for event notifications in the calendar?") [1614764](https://support.mozilla.org/questions/1614764 "My calendar stopped working (will not load my calendars), cannot change day , mo") [1614798](https://support.mozilla.org/questions/1614798 "Das Update killt den Kalender") [1614819](https://support.mozilla.org/questions/1614819 "il calendario non funziona") [1614962](https://support.mozilla.org/questions/1614962 "159.0 - Calendar is blanked post-update, & my Advanced Settings screens don't ma") [1615035](https://support.mozilla.org/questions/1615035 "How do I connect to a Microsoft 365 calendar with the new 159 version of Thunder") +4 |
| daily | 3.1× | 2026-11-05 | v159 × m:gmail | 4 | 50% answered (below 60%), 5.5h | spreading | [1616042](https://support.mozilla.org/questions/1616042 "How do I unsync my old email account that no longer exists from Thunderbird?") [1616054](https://support.mozilla.org/questions/1616054 "About the Gmail Data Transfer to Thunderbird") [1616142](https://support.mozilla.org/questions/1616142 "Google Caldav: Microsoft meeting notices stored locally but not on Google calend") [1616165](https://support.mozilla.org/questions/1616165 "One email account will not open.") |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 2 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 4.0× | 2026-10-26 | feat:calendar | 16 | 56% answered (below 60%), 10.7h | 4.0 | [1614162](https://support.mozilla.org/questions/1614162 "Subscribed (internet) calendars disappear") [1614410](https://support.mozilla.org/questions/1614410 "Calendar sidebar - missing data for series") [1614493](https://support.mozilla.org/questions/1614493 "Calendar Event Automatically Created from Email") [1614652](https://support.mozilla.org/questions/1614652 "How do I stop notifications from one calendar?") [1614718](https://support.mozilla.org/questions/1614718 "How do I turn off the sound for event notifications in the calendar?") [1614764](https://support.mozilla.org/questions/1614764 "My calendar stopped working (will not load my calendars), cannot change day , mo") +10 |
| weekly | 3.5× | 2026-11-02 | m:spectrum | 7 | 71% answered, 1.8h | 2.0 | [1616136](https://support.mozilla.org/questions/1616136 "Intermittent server refusals on Spectrum") [1616162](https://support.mozilla.org/questions/1616162 "How do I change email servers?") [1616242](https://support.mozilla.org/questions/1616242 "Issue is with spectrum server mail.twc.com   error message sending and rec e mai") [1616383](https://support.mozilla.org/questions/1616383 "Not able to send mail") [1616508](https://support.mozilla.org/questions/1616508 "Keeps asking for passwords") [1616527](https://support.mozilla.org/questions/1616527 "Issues with spectrum email") +1 |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 15 rows</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | new | 2026-11-01 | tb_version_major | 159 | 14 [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615314](https://support.mozilla.org/questions/1615314 "I got a mail from Roundcube Webmail who asks me to upgrade. Shoul I upgrade?") | 0.0 |
| daily | new | 2026-11-02 | tb_version_major | 159 | 20 [1615502](https://support.mozilla.org/questions/1615502 "Unable to create a new email Folder") [1615510](https://support.mozilla.org/questions/1615510 "Wie kann die Schriftfarbe in Thunderbird/Terminkalender/Neuer Termin/Beschreibun") | 0.0 |
| daily | new | 2026-11-03 | tb_version_major | 159 | 15 [1615642](https://support.mozilla.org/questions/1615642 "I can't get Thunderbird to go due to password problems") [1615655](https://support.mozilla.org/questions/1615655 "Deleted emails Not showing in trash folder") | 0.0 |
| daily | new | 2026-11-05 | tb_version_major | 159 | 14 [1616042](https://support.mozilla.org/questions/1616042 "How do I unsync my old email account that no longer exists from Thunderbird?") [1616054](https://support.mozilla.org/questions/1616054 "About the Gmail Data Transfer to Thunderbird") | 0.0 |
| daily | new | 2026-11-06 | tb_version_major | 159 | 13 [1616228](https://support.mozilla.org/questions/1616228 "thunderbird keeps asking for a password before sending email") [1616236](https://support.mozilla.org/questions/1616236 "cannot download my email, connection times out right away") | 0.0 |
| daily | new | 2026-11-07 | tb_version_major | 159 | 8 [1616454](https://support.mozilla.org/questions/1616454 "Stop double spacing in composition editor") [1616485](https://support.mozilla.org/questions/1616485 "email transferred from internode to messenger co") | 0.0 |
| daily | new | 2026-11-08 | tb_version_major | 159 | 11 [1616602](https://support.mozilla.org/questions/1616602 "Exactly how to export my Thunderbird Calendar to an .ics file?") [1616639](https://support.mozilla.org/questions/1616639 "How do I change the page zoom so the emails stay at ＂110＂ or ＂125＂ like in a bro") | 0.0 |
| daily | new | 2026-11-09 | tb_version_major | 159 | 18 [1616747](https://support.mozilla.org/questions/1616747 "Why is my email blocked?") [1616749](https://support.mozilla.org/questions/1616749 "159.0 (64-bit) update zapped my email account (gmail)") | 0.0 |
| monthly | new | 2026-11 | tb_version_major | 158 | 10 [1615305](https://support.mozilla.org/questions/1615305 "Alert from added account: failure due to backend error") [1615599](https://support.mozilla.org/questions/1615599 "Persistent Microsoft 365 / GoDaddy SMTP authentication failure in Thunderbird de") | 0.0 |
| monthly | new | 2026-11 | tb_version_major | 159 | 121 [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615314](https://support.mozilla.org/questions/1615314 "I got a mail from Roundcube Webmail who asks me to upgrade. Shoul I upgrade?") | 0.0 |
| weekly | new | 2026-10-26 | tb_version_major | 158 | 24 [1614162](https://support.mozilla.org/questions/1614162 "Subscribed (internet) calendars disappear") [1614179](https://support.mozilla.org/questions/1614179 "[URGENT] Request to Force Stop Email Loop & Clear Server Queue - [redacted]@lead") | 0.0 |
| weekly | new | 2026-10-26 | tb_version_major | 159 | 60 [1614545](https://support.mozilla.org/questions/1614545 "Address book hangs when I click on any entry in it") [1614661](https://support.mozilla.org/questions/1614661 "Warum ＂keine Nachrichten＂ bevor die E-Mails aufklappen?") | 0.0 |
| weekly | new | 2026-11-02 | tb_version_major | 159 | 88 [1615502](https://support.mozilla.org/questions/1615502 "Unable to create a new email Folder") [1615510](https://support.mozilla.org/questions/1615510 "Wie kann die Schriftfarbe in Thunderbird/Terminkalender/Neuer Termin/Beschreibun") | 0.0 |
| weekly | 12.0× | 2026-11-02 | tb_version_major | 158 | 6 [1615599](https://support.mozilla.org/questions/1615599 "Persistent Microsoft 365 / GoDaddy SMTP authentication failure in Thunderbird de") [1615737](https://support.mozilla.org/questions/1615737 "Unread emails appear red") | 0.5 |
| weekly | 38.0× | 2026-11-09 | tb_version_major | 159 | 19 [1616747](https://support.mozilla.org/questions/1616747 "Why is my email blocked?") [1616749](https://support.mozilla.org/questions/1616749 "159.0 (64-bit) update zapped my email account (gmail)") | 0.5 |

</details>

<details markdown="1">
<summary>November 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v159 | 121 | `▆█▆▃▆▆▄▅▇▁` |
| v153 | 47 | `▃▄▅▆▆▆▆▅█▂` |
| v158 | 10 | `▅▅██▅▁▁▁█▅` |
| v140 | 8 | `▃█▃▃▁▃▁▁▃▁` |
| v115 | 6 | `▅▅▁▁█▅▁▁▅▁` |
| v150 | 6 | `▅▅█▅▁▁▅▁▁▁` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 21 | `▃▅▃▅█▃▁▁▅▁` |
| m:microsoftemail | 12 | `███▁█▅▅▁█▁` |
| m:spectrum | 9 | `▁▁▁▁▆▆█▁▆▁` |
| m:yahooemail | 8 | `▁▃▃▁▃▁▁█▃▁` |
| m:thundermail | 3 | `█▁▁█▁▁▁▁█▁` |
| m:comcast | 2 | `█▁▁▁▁█▁▁▁▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:calendar | 13 | `█▅▄▁▂▁▂▂▁▁` |
| feat:junk | 9 | `▁██▁█▅▁▁█▁` |
| feat:addressbook | 8 | `▁▅█▁█▅▅▁▅▁` |
| feat:import_export | 6 | `▁▃▃▁▁▁▁▃█▁` |
| feat:search | 2 | `█▁█▁▁▁▁▁▁▁` |
| feat:notifications | 2 | `█▁▁█▁▁▁▁▁▁` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 24 | `▂▃▆▄▄█▂▁▃▁` |
| proto:smtp | 15 | `▆▅▃▃▃█▁▁▆▁` |
| proto:pop | 12 | `▁▃█▆▁█▃▃▁▃` |
| proto:oauth | 6 | `▅▅▁▁█▅▁▅▁▁` |
| proto:ews | 2 | `█▁█▁▁▁▁▁▁▁` |
| proto:caldav | 1 | `▁▁▁▁█▁▁▁▁▁` |

The antivirus products named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| av:defender | 1 | `█▁▁▁▁▁▁▁▁▁` |
| av:comodo | 1 | `▁█▁▁▁▁▁▁▁▁` |
| av:zonealarm | 1 | `▁▁█▁▁▁▁▁▁▁` |
| av:mcafee | 1 | `▁▁▁▁▁█▁▁▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 206 | `▅█▇▆▆▆▅▄▇▁` |
| os:linux | 26 | `▄▂▄▅█▄▄█▇▁` |
| os:macos | 13 | `█▁▁▅▁▃▁▃█▃` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:tahoe | 2 | `▁▁▁▁▁▁▁▁█▁` |
| macos:high_sierra | 1 | `█▁▁▁▁▁▁▁▁▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward November 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
