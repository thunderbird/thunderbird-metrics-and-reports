---
layout: base
title: "2026-11 exec summary: Thunderbird Desktop support spikes"
---

# November 2026: Thunderbird Desktop support spikes

Executive summary for 2026-11. It covers 175 Thunderbird Desktop support questions. The tool wrote this page on 2026-11-07 05:31 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

5 of them tie to a Thunderbird version. 1 of them are cause-level. Every row is in the collapsed blocks below.

November 2026 is still in progress. The counts will grow.

In short: Calendar and OAuth. Both are in [What stands out](#what-stands-out), with 1 smaller cluster.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 2 | 2 | 1 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 1 | 0 |

Three more numbers for context:

- Volume: 175 questions. 90 of them (51%) carry a cause tag. The count per day was `▇██▇▇▆▂`, one block per day from November 1 to November 7.
- Answers: 127 of the 175 questions (73%) got an answer from somebody other than the person who asked. The middle time to the first answer was 2.2 hours.
- Release-adoption version spikes: 10. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All November 2026 detail](#all-november-2026-detail) below.

## What stands out {#what-stands-out}

1. Calendar ([`feat:calendar`](explorer.html#grain=monthly&cause=feat:calendar&period=2026-11), 4 spikes): 11 questions in November, under the monthly bar. It peaked on 2026-11-01 at 8.8 times expected, on Thunderbird 159.
2. OAuth ([`proto:oauth`](explorer.html#grain=monthly&cause=proto:oauth&period=2026-11), 1 spike): 5 questions in November, under the monthly bar. It peaked in the week of 2026-10-26 at 6.9 times expected, on Thunderbird 158.
3. Gmail ([`m:gmail`](explorer.html#grain=monthly&cause=m:gmail&period=2026-11), 1 spike): 18 questions in November, under the monthly bar. It peaked on 2026-11-05 at 3.1 times expected, on Thunderbird 159.

In 5 clusters, fewer than 60% of the questions got an answer: `v159 × feat:calendar` on 2026-11-01 (25% answered), `v159 × m:gmail` on 2026-11-05 (50% answered), `v158 × proto:oauth` in the week of 2026-10-26 (0% answered), `v159 × feat:calendar` in 2026-11 (44% answered), and 1 more.

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 5 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Version and cause together:

| Grain | Lift | When | Version × Cause | Questions | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| weekly | 3.0× | 2026-10-26 | v153 × proto:oauth | 4 | 50% answered (below 60%), 2.9h | [1614258](https://support.mozilla.org/questions/1614258 "Yahoo-Mail lässt sich in Thunderbird 153.5 unter macOS nicht anmelden – „Es ist ") [1614417](https://support.mozilla.org/questions/1614417 "Thunderbird Hotmail Problem") [1614449](https://support.mozilla.org/questions/1614449 "I am receiving regular Thunderbird notifications of errors for a Yahoo mail acco") [1615236](https://support.mozilla.org/questions/1615236 "Outlook.com SMTP OAuth2 authentication fails with error 535 despite successful s") |
| weekly | 2.8× | 2026-11-02 | v159 × feat:junk | 5 | 60% answered, 2.5h | [1615531](https://support.mozilla.org/questions/1615531 "Thunderbird does not download SPAM until I open the spam folder") [1615533](https://support.mozilla.org/questions/1615533 "Thunderbird has changed!  I now have 2 spam folders and my normal senders are go") [1615795](https://support.mozilla.org/questions/1615795 "Spam Folder") [1615828](https://support.mozilla.org/questions/1615828 "Spam folder shows there are messages but when I open it nothing is there.") [1616310](https://support.mozilla.org/questions/1616310 "De map Prullenbak (eerst Trash) wordt na een bepaalde tijd ongewenst automatisch") |
| weekly | 2.7× | 2026-11-02 | v153 × proto:pop | 4 | 75% answered, 0.4h | [1615648](https://support.mozilla.org/questions/1615648 "TBird stopped working on one computer, not the other, all settings the same.") [1616297](https://support.mozilla.org/questions/1616297 "153.6.0esr crashing on start") [1616323](https://support.mozilla.org/questions/1616323 "Kan geen mail dturen/ontvangen, programma zegt ｀｀herinitialiseren｀｀ (ook de pop ") [1616426](https://support.mozilla.org/questions/1616426 "Thunderbird 153 ESR freezes during POP3 mail retrieval and while idle on Windows") |
| weekly | 2.5× | 2026-10-26 | v153 × feat:attachments | 4 | 75% answered, 2.4h | [1614267](https://support.mozilla.org/questions/1614267 "Problema invio allegati") [1614411](https://support.mozilla.org/questions/1614411 "Why are Symbolic links in thunderbird attachments replaced with target?") [1614932](https://support.mozilla.org/questions/1614932 "Ifound an email using search but the contents are empty How can I see contents/a") [1614975](https://support.mozilla.org/questions/1614975 "Adding attachments") |
| monthly | 2.4× | 2026-11 | v159 × feat:junk | 5 | 60% answered, 2.5h | [1615531](https://support.mozilla.org/questions/1615531 "Thunderbird does not download SPAM until I open the spam folder") [1615533](https://support.mozilla.org/questions/1615533 "Thunderbird has changed!  I now have 2 spam folders and my normal senders are go") [1615795](https://support.mozilla.org/questions/1615795 "Spam Folder") [1615828](https://support.mozilla.org/questions/1615828 "Spam folder shows there are messages but when I open it nothing is there.") [1616310](https://support.mozilla.org/questions/1616310 "De map Prullenbak (eerst Trash) wordt na een bepaalde tijd ongewenst automatisch") |


</details>

---

## All November 2026 detail {#all-november-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 5 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | 8.8× | 2026-11-01 | v159 × feat:calendar | 4 | 25% answered (below 60%), 0.5h | spreading | [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615363](https://support.mozilla.org/questions/1615363 "TB 159 - Graph Calendar not automatically detected on account setup") [1615397](https://support.mozilla.org/questions/1615397 "Make Calendar Notification Window AlwaysOnTop") [1615399](https://support.mozilla.org/questions/1615399 "＂Thunderbird＂ access to Calendar functions are NOT FUNCTIONING at all. Thanks fo") |
| weekly | 6.9× | 2026-10-26 | v158 × proto:oauth | 5 | 0% answered (below 60%) | spreading | [1614222](https://support.mozilla.org/questions/1614222 "Outlook.de receives mail but cannot send with OAuth2: “SmtpClientAuthentication ") [1614358](https://support.mozilla.org/questions/1614358 "Thunderbird has stopped downloading emails from Yahoo") [1614376](https://support.mozilla.org/questions/1614376 "Outlook email account can receive mail but loses authentication and stop sending") [1614513](https://support.mozilla.org/questions/1614513 "Thunderbird 158.1 receives emails from my new Outlook.com account but cannot sen") [1614656](https://support.mozilla.org/questions/1614656 "Authentication Failure (outlook)") |
| weekly | 5.1× | 2026-10-26 | v159 × feat:calendar | 10 | 70% answered, 17.5h | spreading | [1614718](https://support.mozilla.org/questions/1614718 "How do I turn off the sound for event notifications in the calendar?") [1614764](https://support.mozilla.org/questions/1614764 "My calendar stopped working (will not load my calendars), cannot change day , mo") [1614798](https://support.mozilla.org/questions/1614798 "Das Update killt den Kalender") [1614819](https://support.mozilla.org/questions/1614819 "il calendario non funziona") [1614962](https://support.mozilla.org/questions/1614962 "159.0 - Calendar is blanked post-update, & my Advanced Settings screens don't ma") [1615035](https://support.mozilla.org/questions/1615035 "How do I connect to a Microsoft 365 calendar with the new 159 version of Thunder") +4 |
| monthly | 3.3× | 2026-11 | v159 × feat:calendar | 9 | 44% answered (below 60%), 10.3h | recurring | [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615363](https://support.mozilla.org/questions/1615363 "TB 159 - Graph Calendar not automatically detected on account setup") [1615397](https://support.mozilla.org/questions/1615397 "Make Calendar Notification Window AlwaysOnTop") [1615399](https://support.mozilla.org/questions/1615399 "＂Thunderbird＂ access to Calendar functions are NOT FUNCTIONING at all. Thanks fo") [1615555](https://support.mozilla.org/questions/1615555 "Thunderbird Calendar does not react anymore - how can it be reactivated?") [1615605](https://support.mozilla.org/questions/1615605 "events missing from calendar on one pc,  other pc ok") +3 |
| daily | 3.1× | 2026-11-05 | v159 × m:gmail | 4 | 50% answered (below 60%), 5.5h | spreading | [1616042](https://support.mozilla.org/questions/1616042 "How do I unsync my old email account that no longer exists from Thunderbird?") [1616054](https://support.mozilla.org/questions/1616054 "About the Gmail Data Transfer to Thunderbird") [1616142](https://support.mozilla.org/questions/1616142 "Google Caldav: Microsoft meeting notices stored locally but not on Google calend") [1616165](https://support.mozilla.org/questions/1616165 "One email account will not open.") |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 1 row</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 4.0× | 2026-10-26 | feat:calendar | 16 | 56% answered (below 60%), 10.7h | 4.0 | [1614162](https://support.mozilla.org/questions/1614162 "Subscribed (internet) calendars disappear") [1614410](https://support.mozilla.org/questions/1614410 "Calendar sidebar - missing data for series") [1614493](https://support.mozilla.org/questions/1614493 "Calendar Event Automatically Created from Email") [1614652](https://support.mozilla.org/questions/1614652 "How do I stop notifications from one calendar?") [1614718](https://support.mozilla.org/questions/1614718 "How do I turn off the sound for event notifications in the calendar?") [1614764](https://support.mozilla.org/questions/1614764 "My calendar stopped working (will not load my calendars), cannot change day , mo") +10 |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 10 rows</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | new | 2026-11-01 | tb_version_major | 159 | 14 [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615314](https://support.mozilla.org/questions/1615314 "I got a mail from Roundcube Webmail who asks me to upgrade. Shoul I upgrade?") | 0.0 |
| daily | new | 2026-11-02 | tb_version_major | 159 | 20 [1615502](https://support.mozilla.org/questions/1615502 "Unable to create a new email Folder") [1615510](https://support.mozilla.org/questions/1615510 "Wie kann die Schriftfarbe in Thunderbird/Terminkalender/Neuer Termin/Beschreibun") | 0.0 |
| daily | new | 2026-11-03 | tb_version_major | 159 | 15 [1615642](https://support.mozilla.org/questions/1615642 "I can't get Thunderbird to go due to password problems") [1615655](https://support.mozilla.org/questions/1615655 "Deleted emails Not showing in trash folder") | 0.0 |
| daily | new | 2026-11-05 | tb_version_major | 159 | 14 [1616042](https://support.mozilla.org/questions/1616042 "How do I unsync my old email account that no longer exists from Thunderbird?") [1616054](https://support.mozilla.org/questions/1616054 "About the Gmail Data Transfer to Thunderbird") | 0.0 |
| daily | new | 2026-11-06 | tb_version_major | 159 | 13 [1616228](https://support.mozilla.org/questions/1616228 "thunderbird keeps asking for a password before sending email") [1616236](https://support.mozilla.org/questions/1616236 "cannot download my email, connection times out right away") | 0.0 |
| monthly | new | 2026-11 | tb_version_major | 159 | 83 [1615309](https://support.mozilla.org/questions/1615309 "When I create an event in the Thunderbird calendar and enter text in the “Detail") [1615314](https://support.mozilla.org/questions/1615314 "I got a mail from Roundcube Webmail who asks me to upgrade. Shoul I upgrade?") | 0.0 |
| weekly | new | 2026-10-26 | tb_version_major | 158 | 24 [1614162](https://support.mozilla.org/questions/1614162 "Subscribed (internet) calendars disappear") [1614179](https://support.mozilla.org/questions/1614179 "[URGENT] Request to Force Stop Email Loop & Clear Server Queue - [redacted]@lead") | 0.0 |
| weekly | new | 2026-10-26 | tb_version_major | 159 | 60 [1614545](https://support.mozilla.org/questions/1614545 "Address book hangs when I click on any entry in it") [1614661](https://support.mozilla.org/questions/1614661 "Warum ＂keine Nachrichten＂ bevor die E-Mails aufklappen?") | 0.0 |
| weekly | new | 2026-11-02 | tb_version_major | 159 | 69 [1615502](https://support.mozilla.org/questions/1615502 "Unable to create a new email Folder") [1615510](https://support.mozilla.org/questions/1615510 "Wie kann die Schriftfarbe in Thunderbird/Terminkalender/Neuer Termin/Beschreibun") | 0.0 |
| weekly | 12.0× | 2026-11-02 | tb_version_major | 158 | 6 [1615599](https://support.mozilla.org/questions/1615599 "Persistent Microsoft 365 / GoDaddy SMTP authentication failure in Thunderbird de") [1615737](https://support.mozilla.org/questions/1615737 "Unread emails appear red") | 0.5 |

</details>

<details markdown="1">
<summary>November 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v159 | 83 | `▆█▆▃▆▆▁` |
| v153 | 28 | `▃▅▆███▂` |
| v158 | 7 | `▅▅██▅▁▁` |
| v140 | 7 | `▃█▃▃▁▃▁` |
| v115 | 5 | `▅▅▁▁█▅▁` |
| v150 | 5 | `▅▅█▅▁▁▁` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 18 | `▃▅▃▅█▃▁` |
| m:microsoftemail | 9 | `███▁█▅▁` |
| m:spectrum | 4 | `▁▁▁▁██▁` |
| m:yahooemail | 3 | `▁██▁█▁▁` |
| m:thundermail | 2 | `█▁▁█▁▁▁` |
| m:comcast | 2 | `█▁▁▁▁█▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:calendar | 11 | `█▅▄▁▂▁▁` |
| feat:junk | 7 | `▁██▁█▅▁` |
| feat:addressbook | 6 | `▁▅█▁█▅▁` |
| feat:search | 2 | `█▁█▁▁▁▁` |
| feat:notifications | 2 | `█▁▁█▁▁▁` |
| feat:import_export | 2 | `▁██▁▁▁▁` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 21 | `▂▃▆▄▄█▁` |
| proto:smtp | 12 | `▆▅▃▃▃█▁` |
| proto:pop | 10 | `▁▃█▆▁█▃` |
| proto:oauth | 5 | `▅▅▁▁█▅▁` |
| proto:ews | 2 | `█▁█▁▁▁▁` |
| proto:caldav | 1 | `▁▁▁▁█▁▁` |

The antivirus products named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| av:defender | 1 | `█▁▁▁▁▁▁` |
| av:comodo | 1 | `▁█▁▁▁▁▁` |
| av:zonealarm | 1 | `▁▁█▁▁▁▁` |
| av:mcafee | 1 | `▁▁▁▁▁█▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 147 | `▅█▇▆▆▆▁` |
| os:linux | 16 | `▄▂▄▅█▄▂` |
| os:macos | 7 | `█▁▁▅▁▃▁` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:high_sierra | 1 | `█▁▁▁▁▁▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward November 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
