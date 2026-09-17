---
layout: base
title: "2026-09 exec summary: Thunderbird Desktop support spikes"
---

# September 2026: Thunderbird Desktop support spikes

Executive summary for 2026-09. It covers 558 Thunderbird Desktop support questions. The tool wrote this page on 2026-09-17 05:34 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## September 2026: 17 spikes to investigate

12 of them tie to a Thunderbird version. 5 of them are cause-level. Every row is in the collapsed blocks below.

September 2026 is still in progress. The counts will grow.

In short: Printing and Virgin Media. Both are in [What stands out](#what-stands-out), with 6 smaller clusters.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 4 | 7 | 1 |
| cause-level (mail host, protocol, antivirus, feature) | 1 | 4 | 0 |

Three more numbers for context:

- Volume: 558 questions. 267 of them (48%) carry a cause tag. The count per day was `▆█▇▆▄▄█▆▆▆▆▃▅▆▇▇▁`, one block per day from September 1 to September 17.
- Answers: 385 of the 558 questions (69%) got an answer from somebody other than the person who asked. The middle time to the first answer was 3.6 hours.
- Release-adoption version spikes: 25. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All September 2026 detail](#all-september-2026-detail) below.

## What stands out {#what-stands-out}

1. Printing ([`feat:printing`](explorer.html#grain=monthly&cause=feat:printing&period=2026-09), 4 spikes): 8 questions in September, under the monthly bar. It peaked on 2026-09-01 at 18.0 times expected, on Thunderbird 154.
2. Virgin Media ([`m:virginmedia`](explorer.html#grain=monthly&cause=m:virginmedia&period=2026-09), 1 spike): 6 questions in September, under the monthly bar. It peaked in the week of 2026-09-07 at 16.5 times expected, on Thunderbird 155.
3. Microsoft mail ([`m:microsoftemail`](explorer.html#grain=monthly&cause=m:microsoftemail&period=2026-09), 3 spikes): 35 questions in September, under the monthly bar. It peaked on 2026-09-16 at 8.0 times its baseline.
4. Yahoo Mail ([`m:yahooemail`](explorer.html#grain=monthly&cause=m:yahooemail&period=2026-09), 3 spikes): 35 questions in September, under the monthly bar. It peaked on 2026-09-16 at 7.2 times expected, on Thunderbird 153.
5. Attachments ([`feat:attachments`](explorer.html#grain=monthly&cause=feat:attachments&period=2026-09), 2 spikes): 18 questions in September, under the monthly bar. It peaked in the week of 2026-08-31 at 3.8 times expected, on Thunderbird 154.

3 more clusters fired: [`proto:pop`](explorer.html#grain=monthly&cause=proto:pop&period=2026-09), [`m:spectrum`](explorer.html#grain=monthly&cause=m:spectrum&period=2026-09), [`feat:filters`](explorer.html#grain=monthly&cause=feat:filters&period=2026-09). They are in the detail below.

In 6 clusters, fewer than 60% of the questions got an answer: `v156 × m:microsoftemail` on 2026-09-16 (25% answered), `v155 × m:virginmedia` in the week of 2026-09-07 (25% answered), `v156 × m:microsoftemail` in the week of 2026-09-14 (25% answered), `v153 × m:yahooemail` in the week of 2026-09-07 (50% answered), and 2 more.

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 9 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Version and cause together:

| Grain | Lift | When | Version × Cause | Questions | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| monthly | 2.8× | 2026-09 | v153 × m:yahooemail | 16 | 56% answered (below 60%), 5.1h | [1602160](https://support.mozilla.org/questions/1602160 "Unable to add AOL account") [1602571](https://support.mozilla.org/questions/1602571 "T-bird connect to yahoo mail works on one laptop, not the other") [1602816](https://support.mozilla.org/questions/1602816 "How can I get emails coming into the correct account and be able to send respons") [1602845](https://support.mozilla.org/questions/1602845 "pCENT error for Yahoo when using OAuth2") [1603033](https://support.mozilla.org/questions/1603033 "authentication errors") [1603355](https://support.mozilla.org/questions/1603355 "Update: @rocketmail.com address not recognized") +10 |
| daily | 2.7× | 2026-09-01 | v154 × proto:imap | 4 | 25% answered (below 60%), 7.2h | [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601534](https://support.mozilla.org/questions/1601534 "Thunderbird on Win11 will not send or receive emails") [1601629](https://support.mozilla.org/questions/1601629 "Login to inbound server fails") [1601635](https://support.mozilla.org/questions/1601635 "missing email from flders") |
| weekly | 2.6× | 2026-09-14 | v153 × m:microsoftemail | 6 | 33% answered (below 60%), 2.8h | [1604054](https://support.mozilla.org/questions/1604054 "Save email messages so they can be read in MS Outlook") [1604079](https://support.mozilla.org/questions/1604079 "Thunderbird emails archive") [1604342](https://support.mozilla.org/questions/1604342 "Fails to connect to Outlook primary account") [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604774](https://support.mozilla.org/questions/1604774 "I receive this reply when launching email:   ＂Looks like there’s a problem with ") [1604861](https://support.mozilla.org/questions/1604861 "Microsoft account team messge in correspondents") |
| daily | 2.4× | 2026-09-15 | v155 × m:microsoftemail | 4 | 25% answered (below 60%), 7.1h | [1604263](https://support.mozilla.org/questions/1604263 "More lines in Title of Thunderbird appointments") [1604373](https://support.mozilla.org/questions/1604373 "Trying to get TB 155 to link with microsoft exchange account and failing - what ") [1604399](https://support.mozilla.org/questions/1604399 "SMTP blokkeert met outlook bij -mail.live.nl") [1604480](https://support.mozilla.org/questions/1604480 "Thunderbird adds a fix for quoted styles, then its own filter throws the fix awa") |
| weekly | 2.4× | 2026-09-14 | v153 × proto:pop | 4 | 50% answered (below 60%), 2.8h | [1603956](https://support.mozilla.org/questions/1603956 "authentication problem yahoo mail cannot access OAuth dialog box") [1604479](https://support.mozilla.org/questions/1604479 "I stared to get message ＂ Connection to server Pop.mail.yahoo.com timedout＂. wha") [1604799](https://support.mozilla.org/questions/1604799 "thunderbird deleting my emails from the POP server") [1604953](https://support.mozilla.org/questions/1604953 "Thunderbird won't send emails between  2 AOL accounts") |
| weekly | 2.4× | 2026-08-31 | v155 × feat:junk | 5 | 100% answered, 4.4h | [1601955](https://support.mozilla.org/questions/1601955 "Are you aware of a bug since yesterday to handling of spam filters?") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder (bug2068847)") [1602105](https://support.mozilla.org/questions/1602105 "Why do ALL my new emails all go to a spam folder ?") [1602303](https://support.mozilla.org/questions/1602303 "All messages ending in spam folder thunderbird after update to snap ubuntu") [1602574](https://support.mozilla.org/questions/1602574 "can't find Junk folder") |
| monthly | 2.4× | 2026-09 | v153 × proto:oauth | 7 | 29% answered (below 60%), 7.1h | [1601815](https://support.mozilla.org/questions/1601815 "cannot send emails anymore") [1602845](https://support.mozilla.org/questions/1602845 "pCENT error for Yahoo when using OAuth2") [1603097](https://support.mozilla.org/questions/1603097 "Thunderbird Stopped being able to send mail through office365") [1603754](https://support.mozilla.org/questions/1603754 "OAuth Authentication and Thunderbird in 2026 using an AOL email.") [1603956](https://support.mozilla.org/questions/1603956 "authentication problem yahoo mail cannot access OAuth dialog box") [1604117](https://support.mozilla.org/questions/1604117 "Can't send emails since about 8/23/26; still receive emails") +1 |
| monthly | 2.3× | 2026-09 | v155 × feat:filters | 11 | 82% answered, 5.1h | [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") [1601955](https://support.mozilla.org/questions/1601955 "Are you aware of a bug since yesterday to handling of spam filters?") [1602361](https://support.mozilla.org/questions/1602361 "Message filters has gone crazy for last 2 days") [1602761](https://support.mozilla.org/questions/1602761 "Version 155.0 64 bit -- filters now totally non selective.  Fires on all message") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") +5 |

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.3× | 2026-09-07 | m:spectrum | 7 | 57% answered (below 60%), 8.8h | 3.0 | [1602946](https://support.mozilla.org/questions/1602946 "How can i access my Thunderbird  email? It stopped recognizing my password") [1603164](https://support.mozilla.org/questions/1603164 "mobile.charter.net  times out?") [1603258](https://support.mozilla.org/questions/1603258 "The server access you are using is no longer functional!!!  I have had little ac") [1603335](https://support.mozilla.org/questions/1603335 "can't get email on laptop. I can get it on phone; have Spectrum") [1603361](https://support.mozilla.org/questions/1603361 "Thunderbird is not sending or receiving e mail from Charter.net") [1603380](https://support.mozilla.org/questions/1603380 "in the last 10 days, my spectrum/charter email works only sporadically, like may") +1 |


</details>

---

## All September 2026 detail {#all-september-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 12 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | 18.0× | 2026-09-01 | v154 × feat:printing | 4 | 100% answered, 13.8h | recurring | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") |
| weekly | 16.5× | 2026-09-07 | v155 × m:virginmedia | 4 | 25% answered (below 60%), 5.2h | new | [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602701](https://support.mozilla.org/questions/1602701 "read emails for dryborough@ntlworld.com") [1602752](https://support.mozilla.org/questions/1602752 "Thunderbird says no new messages") [1603241](https://support.mozilla.org/questions/1603241 "lost all  virgin media and gmail account settings") |
| weekly | 10.9× | 2026-08-31 | v154 × feat:printing | 8 | 100% answered, 4.7h | recurring | [1601286](https://support.mozilla.org/questions/1601286 "Ik kan niet meer printen vanuit Thunderbird. Is er een storing?") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") [1601367](https://support.mozilla.org/questions/1601367 "PDF se vytiskne prázdné.") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") +2 |
| monthly | 9.6× | 2026-09 | v154 × feat:printing | 5 | 100% answered, 5.0h | recurring | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") [1602826](https://support.mozilla.org/questions/1602826 "When printing from Thunderbird, a white sheet is produced.") |
| daily | 7.2× | 2026-09-16 | v153 × m:yahooemail | 4 | 75% answered, 0.8h | new | [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604699](https://support.mozilla.org/questions/1604699 "I messaggi di un account vanno anche in un secondo account") [1604799](https://support.mozilla.org/questions/1604799 "thunderbird deleting my emails from the POP server") [1604953](https://support.mozilla.org/questions/1604953 "Thunderbird won't send emails between  2 AOL accounts") |
| daily | 4.0× | 2026-09-16 | v156 × m:microsoftemail | 4 | 25% answered (below 60%), 0.8h | spreading | [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") [1604697](https://support.mozilla.org/questions/1604697 "Authentication Failure outlook.office365.com only on startup") [1604835](https://support.mozilla.org/questions/1604835 "ERROR AL AÑADIR CUENTA DE OUTLOOK") [1604859](https://support.mozilla.org/questions/1604859 "autenticazione non riuscita durante la connessione al server outlook su thunderb") |
| daily | 3.8× | 2026-09-07 | v155 × proto:pop | 4 | 75% answered, 5.2h | spreading | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |
| weekly | 3.8× | 2026-08-31 | v154 × feat:attachments | 5 | 100% answered, 3.5h | spreading | [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") [1601835](https://support.mozilla.org/questions/1601835 "I have problems as I can not send attachments") |
| weekly | 3.7× | 2026-09-14 | v156 × m:microsoftemail | 4 | 25% answered (below 60%), 0.8h | new | [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") [1604697](https://support.mozilla.org/questions/1604697 "Authentication Failure outlook.office365.com only on startup") [1604835](https://support.mozilla.org/questions/1604835 "ERROR AL AÑADIR CUENTA DE OUTLOOK") [1604859](https://support.mozilla.org/questions/1604859 "autenticazione non riuscita durante la connessione al server outlook su thunderb") |
| weekly | 3.6× | 2026-09-14 | v153 × m:yahooemail | 6 | 50% answered (below 60%), 0.8h | recurring | [1603956](https://support.mozilla.org/questions/1603956 "authentication problem yahoo mail cannot access OAuth dialog box") [1604479](https://support.mozilla.org/questions/1604479 "I stared to get message ＂ Connection to server Pop.mail.yahoo.com timedout＂. wha") [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604699](https://support.mozilla.org/questions/1604699 "I messaggi di un account vanno anche in un secondo account") [1604799](https://support.mozilla.org/questions/1604799 "thunderbird deleting my emails from the POP server") [1604953](https://support.mozilla.org/questions/1604953 "Thunderbird won't send emails between  2 AOL accounts") |
| weekly | 3.1× | 2026-09-07 | v153 × m:yahooemail | 8 | 50% answered (below 60%), 7.3h | spreading | [1602816](https://support.mozilla.org/questions/1602816 "How can I get emails coming into the correct account and be able to send respons") [1602845](https://support.mozilla.org/questions/1602845 "pCENT error for Yahoo when using OAuth2") [1603033](https://support.mozilla.org/questions/1603033 "authentication errors") [1603355](https://support.mozilla.org/questions/1603355 "Update: @rocketmail.com address not recognized") [1603404](https://support.mozilla.org/questions/1603404 "Unable to write the email to the mailbox error message") [1603516](https://support.mozilla.org/questions/1603516 "I cannot send emails from my aol accounts in thunderbird, but I am still receivi") +2 |
| weekly | 3.1× | 2026-09-07 | v155 × feat:filters | 7 | 86% answered, 8.4h | spreading | [1602761](https://support.mozilla.org/questions/1602761 "Version 155.0 64 bit -- filters now totally non selective.  Fires on all message") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") [1602916](https://support.mozilla.org/questions/1602916 "message filters have stopped working.") [1603094](https://support.mozilla.org/questions/1603094 "Cuando bajo los correos estos no respetan la regla de filtro de mensaje y la may") [1603242](https://support.mozilla.org/questions/1603242 "For every filter I get a message saying that the filter could not be applied.") +1 |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 5 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 8.7× | 2026-08-31 | feat:printing | 13 | 100% answered, 4.3h | 1.5 | [1601286](https://support.mozilla.org/questions/1601286 "Ik kan niet meer printen vanuit Thunderbird. Is er een storing?") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") [1601321](https://support.mozilla.org/questions/1601321 "Printing PDF attachment comes out blank") [1601367](https://support.mozilla.org/questions/1601367 "PDF se vytiskne prázdné.") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") +7 |
| daily | 8.0× | 2026-09-16 | m:microsoftemail | 8 | 12% answered (below 60%), 0.8h | 1.0 | [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604697](https://support.mozilla.org/questions/1604697 "Authentication Failure outlook.office365.com only on startup") [1604774](https://support.mozilla.org/questions/1604774 "I receive this reply when launching email:   ＂Looks like there’s a problem with ") [1604835](https://support.mozilla.org/questions/1604835 "ERROR AL AÑADIR CUENTA DE OUTLOOK") [1604859](https://support.mozilla.org/questions/1604859 "autenticazione non riuscita durante la connessione al server outlook su thunderb") +2 |
| weekly | 3.6× | 2026-08-31 | m:spectrum | 9 | 78% answered, 37.2h | 2.5 | [1601375](https://support.mozilla.org/questions/1601375 "my spectrum password wont log me in to thunderbird why") [1601442](https://support.mozilla.org/questions/1601442 "Correct Outgoing SMPT settings for IMAP") [1601623](https://support.mozilla.org/questions/1601623 "no access to Thunderbird email through Spectrum") [1601790](https://support.mozilla.org/questions/1601790 "Charter + pop, all new messages are going to the trash folder, not my inbox, and") [1601822](https://support.mozilla.org/questions/1601822 "trouble sending and receiving messages interfacing with Spectrum (locked duplica") [1602003](https://support.mozilla.org/questions/1602003 "Spectrum Emails are disappearing from my Thunderbird Inbox after downloading. Th") +3 |
| weekly | 3.4× | 2026-09-07 | feat:filters | 12 | 67% answered, 3.9h | 3.5 | [1602761](https://support.mozilla.org/questions/1602761 "Version 155.0 64 bit -- filters now totally non selective.  Fires on all message") [1602768](https://support.mozilla.org/questions/1602768 "Can't get rid of an email (junk/spam) ever with the filter.  Keeps reocurring. B") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602835](https://support.mozilla.org/questions/1602835 "Lost all email filters circa Aug. 4 (approx.) - emails impossible to use/control") [1602847](https://support.mozilla.org/questions/1602847 "Sharing Thunderbird Message filters across multiple computers") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") +6 |
| weekly | 3.4× | 2026-08-31 | feat:attachments | 17 | 88% answered, 3.5h | 5.0 | [1601321](https://support.mozilla.org/questions/1601321 "Printing PDF attachment comes out blank") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601493](https://support.mozilla.org/questions/1601493 "CANNOT SEND ATTACHMENTS OVER 36 MB") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") +11 |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 25 rows</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | 11.3× | 2026-09-01 | tb_version_major | 154 | 17 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 1.5 |
| daily | new | 2026-09-02 | tb_version_major | 155 | 13 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| daily | new | 2026-09-03 | tb_version_major | 155 | 19 [1601859](https://support.mozilla.org/questions/1601859 "My latest Thunderbird upgrade on Kubuntu 26.04 is marked as BETA 155.0") [1601864](https://support.mozilla.org/questions/1601864 "Thunderbird impazzito") | 0.0 |
| daily | new | 2026-09-04 | tb_version_major | 155 | 20 [1602082](https://support.mozilla.org/questions/1602082 "I did not receive all my folders when installing Thunderbird") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder (bug2068847)") | 0.0 |
| daily | new | 2026-09-05 | tb_version_major | 155 | 11 [1602267](https://support.mozilla.org/questions/1602267 "Problems with incoming new mail") [1602271](https://support.mozilla.org/questions/1602271 "Mail coming to inbox is automatically rerouted to trash folder") | 0.0 |
| daily | new | 2026-09-06 | tb_version_major | 155 | 14 [1602429](https://support.mozilla.org/questions/1602429 "Cannot connect Thunderbird to Spectrum") [1602438](https://support.mozilla.org/questions/1602438 "Can I move my entire Mozilla Thunderbird from my old DELL PC to my new DELL PC?") | 0.0 |
| daily | new | 2026-09-07 | tb_version_major | 155 | 19 [1602611](https://support.mozilla.org/questions/1602611 "yahoo not populating email after password change") [1602653](https://support.mozilla.org/questions/1602653 "skupiny kontaktů Google") | 0.0 |
| daily | new | 2026-09-08 | tb_version_major | 155 | 14 [1602807](https://support.mozilla.org/questions/1602807 "Thunderbird sending all inbox messages to deleted (bug2068847)") [1602817](https://support.mozilla.org/questions/1602817 "I'm getting this message:   Unable to write the email to the mailbox. Make sure ") | 0.0 |
| daily | new | 2026-09-09 | tb_version_major | 155 | 17 [1602995](https://support.mozilla.org/questions/1602995 "All delete methods not working nor is new folder created") [1603051](https://support.mozilla.org/questions/1603051 "Da qualche giorno su windows 11 Thunderbird non si avvia e .＂non risponde＂. Ho p") | 0.0 |
| daily | new | 2026-09-10 | tb_version_major | 155 | 13 [1603189](https://support.mozilla.org/questions/1603189 "Thunderbird not responding, reinstall/safe mode not helping (win11)") [1603227](https://support.mozilla.org/questions/1603227 "I can't install Thunderbird on my new laptop") | 0.0 |
| daily | new | 2026-09-11 | tb_version_major | 155 | 18 [1603410](https://support.mozilla.org/questions/1603410 "Delete Account button doesn't work. (bug2069949)") [1603414](https://support.mozilla.org/questions/1603414 "Thunderbird 155.0 outbound error") | 0.0 |
| daily | new | 2026-09-12 | tb_version_major | 155 | 14 [1603587](https://support.mozilla.org/questions/1603587 "'Advance to next unread message' Toggle?") [1603613](https://support.mozilla.org/questions/1603613 "I have (mis)managed to acquire thhree ＂stgilb@optusnet.com.au＂ accounts/profiles") | 0.0 |
| daily | new | 2026-09-13 | tb_version_major | 155 | 9 [1603765](https://support.mozilla.org/questions/1603765 "Top level of Account Levels ＂doesn't take＂ (bug2069949)") [1603769](https://support.mozilla.org/questions/1603769 "Gmail Emails are going into Deleted rather than Inbox. (bug2068847)") | 0.0 |
| daily | new | 2026-09-14 | tb_version_major | 155 | 13 [1603932](https://support.mozilla.org/questions/1603932 "Authentication error when trying to load outlook.365.com emails to Thunderbird") [1603934](https://support.mozilla.org/questions/1603934 "Thunderbird and junk mail") | 0.0 |
| daily | new | 2026-09-15 | tb_version_major | 155 | 22 [1604201](https://support.mozilla.org/questions/1604201 "Wrong correspondent listed in correspondent column. ie Shows Progressive when it") [1604236](https://support.mozilla.org/questions/1604236 "unable to send mail using Thunderbird") | 0.0 |
| daily | new | 2026-09-16 | tb_version_major | 156 | 13 [1604559](https://support.mozilla.org/questions/1604559 "Mail sent to me as cc: and/or bcc:  (but not as To:) is received at ISP mail ser") [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") | 0.0 |
| monthly | new | 2026-09 | tb_version_major | 154 | 40 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 0.0 |
| monthly | new | 2026-09 | tb_version_major | 155 | 223 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| monthly | new | 2026-09 | tb_version_major | 156 | 16 [1603530](https://support.mozilla.org/questions/1603530 "Strange things happening with TB 156.0b3 (32-bit)  and Yahoo") [1603857](https://support.mozilla.org/questions/1603857 "beta 3 is stopped getting mails") | 0.0 |
| monthly | 41.6× | 2026-09 | tb_version_major | 153 | 104 [1601441](https://support.mozilla.org/questions/1601441 "Emails not downloading") [1601614](https://support.mozilla.org/questions/1601614 "How do I change my user name in the login in for Thunderbird?") | 2.5 |
| weekly | new | 2026-08-31 | tb_version_major | 155 | 77 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| weekly | 112.0× | 2026-08-31 | tb_version_major | 154 | 56 [1601271](https://support.mozilla.org/questions/1601271 "Se stampo dal Thunderbird esce il foglio bianco") [1601273](https://support.mozilla.org/questions/1601273 "Al iniciar Thunderbird se bloquea") | 0.5 |
| weekly | new | 2026-09-07 | tb_version_major | 155 | 104 [1602611](https://support.mozilla.org/questions/1602611 "yahoo not populating email after password change") [1602653](https://support.mozilla.org/questions/1602653 "skupiny kontaktů Google") | 0.0 |
| weekly | new | 2026-09-14 | tb_version_major | 155 | 42 [1603932](https://support.mozilla.org/questions/1603932 "Authentication error when trying to load outlook.365.com emails to Thunderbird") [1603934](https://support.mozilla.org/questions/1603934 "Thunderbird and junk mail") | 0.0 |
| weekly | new | 2026-09-14 | tb_version_major | 156 | 14 [1604559](https://support.mozilla.org/questions/1604559 "Mail sent to me as cc: and/or bcc:  (but not as To:) is received at ISP mail ser") [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") | 0.0 |

</details>

<details markdown="1">
<summary>September 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v155 | 223 | `▁▅▇▇▅▅▇▅▆▅▇▅▄▅█▃▁` |
| v153 | 104 | `▃▇▇▄▂▄▅▆▇▇▅▂▇█▇█▂` |
| v154 | 40 | `█▄▃▂▁▁▂▂▁▁▁▁▁▁▁▁▁` |
| v140 | 31 | `██▆▅▃▁▅▅▆▅▅▁▅▃▁▆▁` |
| v115 | 16 | `▁▁▁▃▃▃█▅▅▅▁▁▃▃▃▁▁` |
| v156 | 16 | `▁▁▁▁▁▁▁▁▁▁▂▁▂▁▁█▂` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 45 | `▃▄▄▆▁▃▂█▄▅▄▂▃▅▁▆▁` |
| m:microsoftemail | 35 | `▂▄▂▁▁▁▂▅▅▂▂▁▃▅▅█▁` |
| m:yahooemail | 35 | `▁▂▃▅▁▂▅▅▅▃▇▂▅▂▂█▁` |
| m:spectrum | 17 | `▅▅▃▁▃▅▁▃▃█▃▁▁▁▃▁▃` |
| m:virginmedia | 6 | `▃▁▁▁▁▁█▁▁▃▁▃▁▁▁▁▁` |
| m:btinternet | 6 | `▁▁▁▅▁█▁▁▁▁▁▅▅▁▅▁▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:attachments | 18 | `▇█▂▄▄▁▁▁▁▄▁▁▂▁▁▂▁` |
| feat:filters | 18 | `▁▂▂▁▂▁▄█▂▄▂▁▂▂▂▂▁` |
| feat:junk | 17 | `▁▅▅█▅▅██▅▅█▁▅█▁▁▁` |
| feat:import_export | 10 | `▁█▁▁▁▃▃▁▁▁▃▃▁▆▁▃▁` |
| feat:printing | 8 | `█▃▁▃▃▁▁▃▁▁▁▁▁▁▁▁▁` |
| feat:addressbook | 7 | `▅▁▁▅▅▁▁▁▁▁▁▁█▁▅▅▁` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 51 | `▆▆▅▂▂▅█▂▅▂▆▂▁▇▃▅▁` |
| proto:smtp | 33 | `▃▆▅▆▁▅▃▅▆▃▅▃▃▅▆█▅` |
| proto:pop | 29 | `▂▅▁▂▂▂█▃▁▃▇▂▁▃▃▃▁` |
| proto:oauth | 16 | `▃▃▁█▃▁▁▃▅▁▃▁▃▅▁▅▁` |
| proto:carddav | 1 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:caldav | 1 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

The antivirus products named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| av:norton | 3 | `█▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁` |
| av:avast | 2 | `█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁` |
| av:bitdefender | 2 | `▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁` |
| av:defender | 2 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:zonealarm | 2 | `▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁` |
| av:malwarebytes | 1 | `█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 474 | `▆██▆▄▅█▆▅▆▆▃▅▆▇▇▁` |
| os:macos | 33 | `▃▂▂▃▂▃▅▅▆▂▆▂▁▂█▂▁` |
| os:linux | 32 | `▁▂▄█▂▁▄▇█▄▄▂▄▂▁▇▁` |
| os:other | 5 | `█▁▁▁▁▁▃▁▁▁▁▁▁▁▁▃▁` |
| os:android | 3 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:tahoe | 4 | `█▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁` |
| macos:sequoia | 3 | `▁▁▁▁▁▁█▁█▁▁▁▁▁▁█▁` |
| macos:golden_gate | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward September 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
