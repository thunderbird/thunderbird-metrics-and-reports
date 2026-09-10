---
layout: base
title: "2026-09 exec summary: Thunderbird Desktop support spikes"
---

# September 2026: Thunderbird Desktop support spikes

Executive summary for 2026-09. It covers 328 Thunderbird Desktop support questions. The tool wrote this page on 2026-09-10 05:32 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## September 2026: 9 spikes to investigate

6 of them tie to a Thunderbird version. 3 of them are cause-level. Every row is in the collapsed blocks below.

September 2026 is still in progress. The counts will grow.

In short: Printing and POP. Both are in [What stands out](#what-stands-out), with 3 smaller clusters.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 2 | 3 | 1 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 3 | 0 |

Three more numbers for context:

- Volume: 328 questions. 157 of them (48%) carry a cause tag. The count per day was `▆█▇▆▄▄█▆▆▁`, one block per day from September 1 to September 10.
- Answers: 236 of the 328 questions (72%) got an answer from somebody other than the person who asked. The middle time to the first answer was 3.5 hours.
- Release-adoption version spikes: 15. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All September 2026 detail](#all-september-2026-detail) below.

## What stands out {#what-stands-out}

1. Printing ([`feat:printing`](explorer.html#grain=monthly&cause=feat:printing&period=2026-09), 4 spikes): 8 questions in September, under the monthly bar. It peaked on 2026-09-01 at 17.2 times expected, on Thunderbird 154.
2. POP ([`proto:pop`](explorer.html#grain=monthly&cause=proto:pop&period=2026-09), 1 spike): 15 questions in September, under the monthly bar. It peaked on 2026-09-07 at 4.1 times expected, on Thunderbird 155.
3. Filters ([`feat:filters`](explorer.html#grain=monthly&cause=feat:filters&period=2026-09), 1 spike): 11 questions in September, under the monthly bar. It peaked in the week of 2026-09-07 at 3.9 times expected, on Thunderbird 155.
4. Attachments ([`feat:attachments`](explorer.html#grain=monthly&cause=feat:attachments&period=2026-09), 2 spikes): 14 questions in September, under the monthly bar. It peaked in the week of 2026-08-31 at 3.8 times expected, on Thunderbird 154.
5. Spectrum ([`m:spectrum`](explorer.html#grain=monthly&cause=m:spectrum&period=2026-09), 1 spike): 10 questions in September, under the monthly bar. It peaked in the week of 2026-08-31 at 3.6 times its baseline.

In 1 cluster, fewer than 60% of the questions got an answer: `v155 × feat:filters` in the week of 2026-09-07 (50% answered).

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 6 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Version and cause together:

| Grain | Lift | When | Version × Cause | Questions | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| weekly | 2.9× | 2026-09-07 | v153 × m:gmail | 6 | 33% answered (below 60%), 5.7h | [1602816](https://support.mozilla.org/questions/1602816 "How can I get emails coming into the correct account and be able to send respons") [1602865](https://support.mozilla.org/questions/1602865 "I am being asked for ＂new password＂ when sending email and it doesn't recognise ") [1602984](https://support.mozilla.org/questions/1602984 "Emails not appearing in Thunderbird for days but appear in Outlook without delay") [1603033](https://support.mozilla.org/questions/1603033 "authentication errors") [1603075](https://support.mozilla.org/questions/1603075 "Inability to transfer Emails from one account in Thunderbird to another account ") [1603103](https://support.mozilla.org/questions/1603103 "Thunderbird Mail has 'stopped working'") |
| daily | 2.7× | 2026-09-01 | v154 × proto:imap | 4 | 25% answered (below 60%), 7.2h | [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601534](https://support.mozilla.org/questions/1601534 "Thunderbird on Win11 will not send or receive emails") [1601629](https://support.mozilla.org/questions/1601629 "Login to inbound server fails") [1601635](https://support.mozilla.org/questions/1601635 "missing email from flders") |
| monthly | 2.7× | 2026-09 | v155 × feat:filters | 7 | 71% answered, 4.3h | [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") [1601955](https://support.mozilla.org/questions/1601955 "Are you aware of a bug since yesterday to handling of spam filters?") [1602361](https://support.mozilla.org/questions/1602361 "Message filters has gone crazy for last 2 days") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") [1602916](https://support.mozilla.org/questions/1602916 "message filters have stopped working.") +1 |
| weekly | 2.4× | 2026-08-31 | v155 × feat:junk | 5 | 100% answered, 4.4h | [1601955](https://support.mozilla.org/questions/1601955 "Are you aware of a bug since yesterday to handling of spam filters?") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder (bug2068847)") [1602105](https://support.mozilla.org/questions/1602105 "Why do ALL my new emails all go to a spam folder ?") [1602303](https://support.mozilla.org/questions/1602303 "All messages ending in spam folder thunderbird after update to snap ubuntu") [1602574](https://support.mozilla.org/questions/1602574 "can't find Junk folder") |
| monthly | 2.3× | 2026-09 | v155 × feat:junk | 8 | 88% answered, 4.4h | [1601955](https://support.mozilla.org/questions/1601955 "Are you aware of a bug since yesterday to handling of spam filters?") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder (bug2068847)") [1602105](https://support.mozilla.org/questions/1602105 "Why do ALL my new emails all go to a spam folder ?") [1602303](https://support.mozilla.org/questions/1602303 "All messages ending in spam folder thunderbird after update to snap ubuntu") [1602574](https://support.mozilla.org/questions/1602574 "can't find Junk folder") [1602839](https://support.mozilla.org/questions/1602839 "Suddenly all my emails are going to spam.") +2 |

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.3× | 2026-09-07 | feat:filters | 8 | 50% answered (below 60%), 0.8h | 3.5 | [1602761](https://support.mozilla.org/questions/1602761 "Version 155.0 64 bit -- filters now totally non selective.  Fires on all message") [1602768](https://support.mozilla.org/questions/1602768 "Can't get rid of an email (junk/spam) ever with the filter.  Keeps reocurring. B") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602835](https://support.mozilla.org/questions/1602835 "Lost all email filters circa Aug. 4 (approx.) - emails impossible to use/control") [1602847](https://support.mozilla.org/questions/1602847 "Sharing Thunderbird Message filters across multiple computers") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") +2 |


</details>

---

## All September 2026 detail {#all-september-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 6 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | 17.2× | 2026-09-01 | v154 × feat:printing | 4 | 100% answered, 13.8h | recurring | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") |
| weekly | 10.4× | 2026-08-31 | v154 × feat:printing | 8 | 100% answered, 4.7h | recurring | [1601286](https://support.mozilla.org/questions/1601286 "Ik kan niet meer printen vanuit Thunderbird. Is er een storing?") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") [1601367](https://support.mozilla.org/questions/1601367 "PDF se vytiskne prázdné.") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") +2 |
| monthly | 9.6× | 2026-09 | v154 × feat:printing | 5 | 100% answered, 5.0h | recurring | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") [1602826](https://support.mozilla.org/questions/1602826 "When printing from Thunderbird, a white sheet is produced.") |
| daily | 4.1× | 2026-09-07 | v155 × proto:pop | 4 | 75% answered, 5.2h | spreading | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |
| weekly | 3.9× | 2026-09-07 | v155 × feat:filters | 4 | 50% answered (below 60%), 2.4h | spreading | [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") [1602916](https://support.mozilla.org/questions/1602916 "message filters have stopped working.") [1603094](https://support.mozilla.org/questions/1603094 "Cuando bajo los correos estos no respetan la regla de filtro de mensaje y la may") |
| weekly | 3.8× | 2026-08-31 | v154 × feat:attachments | 5 | 100% answered, 3.5h | spreading | [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") [1601835](https://support.mozilla.org/questions/1601835 "I have problems as I can not send attachments") |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 3 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 8.7× | 2026-08-31 | feat:printing | 13 | 100% answered, 4.3h | 1.5 | [1601286](https://support.mozilla.org/questions/1601286 "Ik kan niet meer printen vanuit Thunderbird. Is er een storing?") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") [1601321](https://support.mozilla.org/questions/1601321 "Printing PDF attachment comes out blank") [1601367](https://support.mozilla.org/questions/1601367 "PDF se vytiskne prázdné.") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") +7 |
| weekly | 3.6× | 2026-08-31 | m:spectrum | 9 | 78% answered, 37.2h | 2.5 | [1601375](https://support.mozilla.org/questions/1601375 "my spectrum password wont log me in to thunderbird why") [1601442](https://support.mozilla.org/questions/1601442 "Correct Outgoing SMPT settings for IMAP") [1601623](https://support.mozilla.org/questions/1601623 "no access to Thunderbird email through Spectrum") [1601790](https://support.mozilla.org/questions/1601790 "Charter + pop, all new messages are going to the trash folder, not my inbox, and") [1601822](https://support.mozilla.org/questions/1601822 "trouble sending and receiving messages interfacing with Spectrum (locked duplica") [1602003](https://support.mozilla.org/questions/1602003 "Spectrum Emails are disappearing from my Thunderbird Inbox after downloading. Th") +3 |
| weekly | 3.4× | 2026-08-31 | feat:attachments | 17 | 88% answered, 3.5h | 5.0 | [1601321](https://support.mozilla.org/questions/1601321 "Printing PDF attachment comes out blank") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601493](https://support.mozilla.org/questions/1601493 "CANNOT SEND ATTACHMENTS OVER 36 MB") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") +11 |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 15 rows</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | 11.3× | 2026-09-01 | tb_version_major | 154 | 17 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 1.5 |
| daily | new | 2026-09-02 | tb_version_major | 155 | 13 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| daily | new | 2026-09-03 | tb_version_major | 155 | 19 [1601859](https://support.mozilla.org/questions/1601859 "My latest Thunderbird upgrade on Kubuntu 26.04 is marked as BETA 155.0") [1601864](https://support.mozilla.org/questions/1601864 "Thunderbird impazzito") | 0.0 |
| daily | new | 2026-09-04 | tb_version_major | 155 | 20 [1602082](https://support.mozilla.org/questions/1602082 "I did not receive all my folders when installing Thunderbird") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder (bug2068847)") | 0.0 |
| daily | new | 2026-09-05 | tb_version_major | 155 | 11 [1602267](https://support.mozilla.org/questions/1602267 "Problems with incoming new mail") [1602271](https://support.mozilla.org/questions/1602271 "Mail coming to inbox is automatically rerouted to trash folder") | 0.0 |
| daily | new | 2026-09-06 | tb_version_major | 155 | 14 [1602429](https://support.mozilla.org/questions/1602429 "Cannot connect Thunderbird to Spectrum") [1602438](https://support.mozilla.org/questions/1602438 "Can I move my entire Mozilla Thunderbird from my old DELL PC to my new DELL PC?") | 0.0 |
| daily | new | 2026-09-07 | tb_version_major | 155 | 18 [1602611](https://support.mozilla.org/questions/1602611 "yahoo not populating email after password change") [1602653](https://support.mozilla.org/questions/1602653 "skupiny kontaktů Google") | 0.0 |
| daily | new | 2026-09-08 | tb_version_major | 155 | 14 [1602807](https://support.mozilla.org/questions/1602807 "Thunderbird sending all inbox messages to deleted (bug2068847)") [1602817](https://support.mozilla.org/questions/1602817 "I'm getting this message:   Unable to write the email to the mailbox. Make sure ") | 0.0 |
| daily | new | 2026-09-09 | tb_version_major | 155 | 17 [1602995](https://support.mozilla.org/questions/1602995 "All delete methods not working nor is new folder created") [1603051](https://support.mozilla.org/questions/1603051 "Da qualche giorno su windows 11 Thunderbird non si avvia e .＂non risponde＂. Ho p") | 0.0 |
| monthly | new | 2026-09 | tb_version_major | 154 | 38 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 0.0 |
| monthly | new | 2026-09 | tb_version_major | 155 | 127 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| monthly | 20.0× | 2026-09 | tb_version_major | 153 | 50 [1601441](https://support.mozilla.org/questions/1601441 "Emails not downloading") [1601614](https://support.mozilla.org/questions/1601614 "How do I change my user name in the login in for Thunderbird?") | 2.5 |
| weekly | new | 2026-08-31 | tb_version_major | 155 | 77 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| weekly | 112.0× | 2026-08-31 | tb_version_major | 154 | 56 [1601271](https://support.mozilla.org/questions/1601271 "Se stampo dal Thunderbird esce il foglio bianco") [1601273](https://support.mozilla.org/questions/1601273 "Al iniciar Thunderbird se bloquea") | 0.5 |
| weekly | new | 2026-09-07 | tb_version_major | 155 | 50 [1602611](https://support.mozilla.org/questions/1602611 "yahoo not populating email after password change") [1602653](https://support.mozilla.org/questions/1602653 "skupiny kontaktů Google") | 0.0 |

</details>

<details markdown="1">
<summary>September 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v155 | 127 | `▁▆██▅▆▇▆▇▁` |
| v153 | 50 | `▃▇▇▄▂▄▆▆█▁` |
| v154 | 38 | `█▄▃▂▁▁▂▂▁▁` |
| v140 | 21 | `██▆▅▃▁▅▅▆▁` |
| v115 | 11 | `▁▁▁▃▃▃█▅▅▁` |
| v150 | 5 | `▁▁▁▅█▁▁▅▅▁` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 27 | `▃▄▄▆▁▃▂█▅▁` |
| m:yahooemail | 16 | `▁▃▆█▁▃███▁` |
| m:microsoftemail | 14 | `▃▆▃▁▁▁▃██▁` |
| m:spectrum | 10 | `██▅▁▅█▁▅▅▁` |
| m:virginmedia | 4 | `▃▁▁▁▁▁█▁▁▁` |
| m:att | 3 | `██▁▁▁▁█▁▁▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:attachments | 14 | `▇█▂▄▄▁▁▁▁▁` |
| feat:filters | 11 | `▁▂▂▁▂▁▄█▂▁` |
| feat:junk | 11 | `▁▅▅█▅▅██▅▁` |
| feat:printing | 8 | `█▃▁▃▃▁▁▃▁▁` |
| feat:import_export | 5 | `▁█▁▁▁▃▃▁▁▁` |
| feat:search | 3 | `██▁▁▁▁▁█▁▁` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 32 | `▆▆▅▂▂▅█▂▅▁` |
| proto:smtp | 17 | `▃█▆█▁▆▃▆█▁` |
| proto:pop | 15 | `▂▅▁▂▂▂█▃▁▁` |
| proto:oauth | 10 | `▃▃▁█▃▁▁▃▅▁` |
| proto:carddav | 1 | `▁▁█▁▁▁▁▁▁▁` |
| proto:caldav | 1 | `▁▁█▁▁▁▁▁▁▁` |

The antivirus products named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| av:norton | 2 | `█▁▁█▁▁▁▁▁▁` |
| av:bitdefender | 2 | `▁▁▁█▁▁█▁▁▁` |
| av:defender | 2 | `▁▁▁█▁▁▁▁▁▁` |
| av:avast | 1 | `█▁▁▁▁▁▁▁▁▁` |
| av:malwarebytes | 1 | `█▁▁▁▁▁▁▁▁▁` |
| av:surfshark | 1 | `▁▁▁▁▁▁█▁▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 274 | `▆██▆▄▅█▆▅▁` |
| os:linux | 20 | `▁▂▄█▂▁▄▇█▁` |
| os:macos | 19 | `▅▃▃▅▃▅▆▆█▁` |
| os:other | 4 | `█▁▁▁▁▁▃▁▁▁` |
| os:android | 2 | `▁█▁▁▁▁▁▁▁▁` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:tahoe | 3 | `█▅▁▁▁▁▁▁▁▁` |
| macos:sequoia | 2 | `▁▁▁▁▁▁█▁█▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward September 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
