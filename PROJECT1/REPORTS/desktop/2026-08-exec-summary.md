---
layout: base
title: "2026-08 exec summary: Thunderbird Desktop support spikes"
---

# August 2026: Thunderbird Desktop support spikes

Executive summary for 2026-08. It covers 941 Thunderbird Desktop support questions. The tool wrote this page on 2026-09-10 05:32 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## August 2026: 27 spikes to investigate

17 of them tie to a Thunderbird version. 10 of them are cause-level. Every row is in the collapsed blocks below.

In short: Printing and Spectrum. Both are in [What stands out](#what-stands-out), with 5 smaller clusters.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 7 | 8 | 2 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 8 | 2 |

Three more numbers for context:

- Volume: 941 questions. 419 of them (45%) carry a cause tag. The count per day was `▄▃▅▅▅▅▆▆▃▅▃▅▅▅▄▅▅▆▄▅▆▅▄▆▅█▆▅▄▄▇`, one block per day from August 1 to August 31.
- Answers: 708 of the 941 questions (75%) got an answer from somebody other than the person who asked. The middle time to the first answer was 2.8 hours.
- Release-adoption version spikes: 31. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All August 2026 detail](#all-august-2026-detail) below.

## What stands out {#what-stands-out}

1. Printing ([`feat:printing`](explorer.html#grain=monthly&cause=feat:printing&period=2026-08), 11 spikes): 36 questions in August, 8.0 times the baseline of 4.5. It peaked on 2026-08-20 at 24.3 times expected, on Thunderbird 154.
2. Spectrum ([`m:spectrum`](explorer.html#grain=monthly&cause=m:spectrum&period=2026-08), 8 spikes): 34 questions in August, 3.2 times the baseline of 10.5. It peaked in the week of 2026-08-17 at 11.0 times its baseline.
3. Attachments ([`feat:attachments`](explorer.html#grain=monthly&cause=feat:attachments&period=2026-08), 2 spikes): 27 questions in August, under the monthly bar. It peaked in the week of 2026-08-31 at 3.8 times expected, on Thunderbird 154.
4. POP ([`proto:pop`](explorer.html#grain=monthly&cause=proto:pop&period=2026-08), 3 spikes): 46 questions in August, under the monthly bar. It peaked on 2026-08-14 at 3.5 times expected, on Thunderbird 153.
5. Yahoo Mail ([`m:yahooemail`](explorer.html#grain=monthly&cause=m:yahooemail&period=2026-08), 1 spike): 55 questions in August, under the monthly bar. It peaked in the week of 2026-08-10 at 3.5 times its baseline.

2 more clusters fired: [`m:microsoftemail`](explorer.html#grain=monthly&cause=m:microsoftemail&period=2026-08), [`m:comcast`](explorer.html#grain=monthly&cause=m:comcast&period=2026-08). They are in the detail below.

In 2 clusters, fewer than 60% of the questions got an answer: `v154 × feat:printing` in the week of 2026-08-17 (43% answered), `feat:printing` in the week of 2026-08-17 (38% answered).

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 11 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Version and cause together:

| Grain | Lift | When | Version × Cause | Questions | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| daily | 2.7× | 2026-08-18 | v153 × m:gmail | 6 | 17% answered (below 60%), 0.7h | [1598887](https://support.mozilla.org/questions/1598887 "＂Authentification Failure while connecting to server imap.gmail.com＂ How do I re") [1598903](https://support.mozilla.org/questions/1598903 "emails from senders with gmail accounts not being downloaded") [1598918](https://support.mozilla.org/questions/1598918 "Thunderbird has stopped receiving email") [1598928](https://support.mozilla.org/questions/1598928 "Thunderbird PC app and Android both loading and syncing incoming email and all f") [1598949](https://support.mozilla.org/questions/1598949 "Unable to sync address book with Gmail") [1598950](https://support.mozilla.org/questions/1598950 "Unable to sync address book with Gmail (locked duplicate)") |
| weekly | 2.7× | 2026-08-17 | v153 × m:spectrum | 5 | 100% answered, 11.8h | [1598964](https://support.mozilla.org/questions/1598964 "Thunderbird connection resets when using Mozilla VPN.") [1599516](https://support.mozilla.org/questions/1599516 "When trying to send an email it will not go") [1599553](https://support.mozilla.org/questions/1599553 "I can't receive or send Charter emails in thunderbird.") [1599823](https://support.mozilla.org/questions/1599823 "After latest update can't connect to spectrum Charter email") [1599836](https://support.mozilla.org/questions/1599836 "all INBOX emails disappeared--no luck repairing folder or deleting INBOX.msf but") |
| weekly | 2.7× | 2026-08-17 | v154 × feat:attachments | 4 | 50% answered (below 60%), 3.2h | [1599261](https://support.mozilla.org/questions/1599261 "Perchè non si riesce a stampare diretta mente da Thunderbird un allegato ad un m") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") [1599333](https://support.mozilla.org/questions/1599333 "can not print attachments") [1599691](https://support.mozilla.org/questions/1599691 "dopo relese 154.0 del 18 Agosto 2026 se cerco di stampare file allegati in pdf o") |
| daily | 2.5× | 2026-08-03 | v153 × m:microsoftemail | 4 | 100% answered, 15.7h | [1596378](https://support.mozilla.org/questions/1596378 "cartelle cscomparse account posta hotmail") [1596433](https://support.mozilla.org/questions/1596433 "Mijn agenda op Thunderbird.") [1596442](https://support.mozilla.org/questions/1596442 "Aanmelden bij outlook met mailadres dat hoofdletters bevat is niet meer mogelijk") [1596497](https://support.mozilla.org/questions/1596497 "Thunderbird cannot log-in to my mail accounts") |
| weekly | 2.5× | 2026-08-24 | v154 × feat:attachments | 7 | 86% answered, 3.7h | [1600228](https://support.mozilla.org/questions/1600228 "kan ineens een PDF bijlage bij een Thunderbird mailtje niet meer direct printen.") [1600600](https://support.mozilla.org/questions/1600600 "In de mail worden de bijlages blanco (zonder tekst) geprint. Printer werkt naar ") [1600639](https://support.mozilla.org/questions/1600639 "cartelle degli allegati che rimangono aperte quando il mittente riutilizza la st") [1600770](https://support.mozilla.org/questions/1600770 "I can't highlight words on attachments") [1600880](https://support.mozilla.org/questions/1600880 "email attachments are printing blank page") [1600976](https://support.mozilla.org/questions/1600976 "versione 154.0 ho un problema di stampa da allegato PDF") +1 |
| monthly | 2.5× | 2026-08 | v154 × feat:attachments | 12 | 75% answered, 3.2h | [1599261](https://support.mozilla.org/questions/1599261 "Perchè non si riesce a stampare diretta mente da Thunderbird un allegato ad un m") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") [1599333](https://support.mozilla.org/questions/1599333 "can not print attachments") [1599691](https://support.mozilla.org/questions/1599691 "dopo relese 154.0 del 18 Agosto 2026 se cerco di stampare file allegati in pdf o") [1600228](https://support.mozilla.org/questions/1600228 "kan ineens een PDF bijlage bij een Thunderbird mailtje niet meer direct printen.") [1600600](https://support.mozilla.org/questions/1600600 "In de mail worden de bijlages blanco (zonder tekst) geprint. Printer werkt naar ") +6 |
| weekly | 2.4× | 2026-08-31 | v155 × feat:junk | 5 | 100% answered, 4.4h | [1601955](https://support.mozilla.org/questions/1601955 "Are you aware of a bug since yesterday to handling of spam filters?") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder (bug2068847)") [1602105](https://support.mozilla.org/questions/1602105 "Why do ALL my new emails all go to a spam folder ?") [1602303](https://support.mozilla.org/questions/1602303 "All messages ending in spam folder thunderbird after update to snap ubuntu") [1602574](https://support.mozilla.org/questions/1602574 "can't find Junk folder") |

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.7× | 2026-08-17 | feat:attachments | 8 | 50% answered (below 60%), 3.2h | 3.0 | [1598660](https://support.mozilla.org/questions/1598660 "I am getting a mail server fault MFRM53  Relay denied when sending an attachment") [1598688](https://support.mozilla.org/questions/1598688 "Bijlage agenda-afspraak") [1598740](https://support.mozilla.org/questions/1598740 "I want a reliable method of deleting attachments, while keeping the original ema") [1599155](https://support.mozilla.org/questions/1599155 "Can't drag and drop attachments from Thunderbird into file manager.") [1599261](https://support.mozilla.org/questions/1599261 "Perchè non si riesce a stampare diretta mente da Thunderbird un allegato ad un m") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") +2 |
| weekly | 2.5× | 2026-08-03 | m:yahooemail | 14 | 79% answered, 3.3h | 5.5 | [1596455](https://support.mozilla.org/questions/1596455 "Recuprar la carpeta Bulk") [1596495](https://support.mozilla.org/questions/1596495 "Are thunderbird's saved logins the same logins Yahoo recognizes and accepts? Tbi") [1596497](https://support.mozilla.org/questions/1596497 "Thunderbird cannot log-in to my mail accounts") [1596560](https://support.mozilla.org/questions/1596560 "Thunderbirdサーバーにログインできなくなりました。") [1596676](https://support.mozilla.org/questions/1596676 "preventing a 2nd email  address from popping up in thunderbird") [1596708](https://support.mozilla.org/questions/1596708 "TB doesn't like to connect to my Comcast internet provider sometime.") +8 |
| weekly | 2.2× | 2026-08-24 | feat:attachments | 9 | 67% answered, 3.7h | 4.0 | [1600003](https://support.mozilla.org/questions/1600003 "I can not create and email and send attachments") [1600228](https://support.mozilla.org/questions/1600228 "kan ineens een PDF bijlage bij een Thunderbird mailtje niet meer direct printen.") [1600404](https://support.mozilla.org/questions/1600404 "attachments from sent emails are blank upon printing") [1600600](https://support.mozilla.org/questions/1600600 "In de mail worden de bijlages blanco (zonder tekst) geprint. Printer werkt naar ") [1600639](https://support.mozilla.org/questions/1600639 "cartelle degli allegati che rimangono aperte quando il mittente riutilizza la st") [1600770](https://support.mozilla.org/questions/1600770 "I can't highlight words on attachments") +3 |
| monthly | 2.2× | 2026-08 | feat:notifications | 9 | 78% answered, 5.7h | 4.0 | [1596436](https://support.mozilla.org/questions/1596436 "Unified Inboxes and New Mail Notifications") [1596608](https://support.mozilla.org/questions/1596608 "Notification: What Does ＂Inotify initialization error＂ Mean?") [1596659](https://support.mozilla.org/questions/1596659 "Ich bekomme keine Benachrichtigungen über email Eingänge auf meinem einen email ") [1597115](https://support.mozilla.org/questions/1597115 "Notification area and activate main window") [1599280](https://support.mozilla.org/questions/1599280 "melding dat het aantal toegestane verzenders is overschreden.") [1599527](https://support.mozilla.org/questions/1599527 "T-bird gives po-up notification when messages arrive, but they do not appear in ") +3 |


</details>

---

## All August 2026 detail {#all-august-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 17 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | 24.3× | 2026-08-20 | v154 × feat:printing | 4 | 75% answered, 3.2h | new | [1599257](https://support.mozilla.org/questions/1599257 "Print emails") [1599261](https://support.mozilla.org/questions/1599261 "Perchè non si riesce a stampare diretta mente da Thunderbird un allegato ad un m") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") [1599333](https://support.mozilla.org/questions/1599333 "can not print attachments") |
| daily | 13.5× | 2026-08-26 | v154 × feat:printing | 5 | 80% answered, 9.1h | recurring | [1600392](https://support.mozilla.org/questions/1600392 "Printing from Thunderbird since version 154.0 on Windows 11 produces only blank ") [1600397](https://support.mozilla.org/questions/1600397 "Problema anteprima di stampa") [1600407](https://support.mozilla.org/questions/1600407 "PDF direct print from mozilla wil print an blanc page") [1600408](https://support.mozilla.org/questions/1600408 "Problem printing PDF files from Thunderbird.") [1600481](https://support.mozilla.org/questions/1600481 "Print Preview Printing Blanks") |
| daily | 13.3× | 2026-08-31 | v154 × feat:printing | 4 | 100% answered, 2.9h | recurring | [1601286](https://support.mozilla.org/questions/1601286 "Ik kan niet meer printen vanuit Thunderbird. Is er een storing?") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") [1601367](https://support.mozilla.org/questions/1601367 "PDF se vytiskne prázdné.") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") |
| weekly | 10.7× | 2026-08-24 | v154 × feat:printing | 17 | 88% answered, 10.7h | recurring | [1599969](https://support.mozilla.org/questions/1599969 "[Known Issue] Thunderbird printing empty PDF files.") [1600094](https://support.mozilla.org/questions/1600094 "nejde tisk z thunderbirdu") [1600149](https://support.mozilla.org/questions/1600149 "Thunderbird 154 PDF preview prints blank pages") [1600228](https://support.mozilla.org/questions/1600228 "kan ineens een PDF bijlage bij een Thunderbird mailtje niet meer direct printen.") [1600392](https://support.mozilla.org/questions/1600392 "Printing from Thunderbird since version 154.0 on Windows 11 produces only blank ") [1600397](https://support.mozilla.org/questions/1600397 "Problema anteprima di stampa") +11 |
| monthly | 10.5× | 2026-08 | v154 × feat:printing | 29 | 76% answered, 4.1h | new | [1596686](https://support.mozilla.org/questions/1596686 "Cannot print Pdf files from within Thunderbird") [1599257](https://support.mozilla.org/questions/1599257 "Print emails") [1599261](https://support.mozilla.org/questions/1599261 "Perchè non si riesce a stampare diretta mente da Thunderbird un allegato ad un m") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") [1599333](https://support.mozilla.org/questions/1599333 "can not print attachments") [1599495](https://support.mozilla.org/questions/1599495 "Thunderbird can't print files") +23 |
| weekly | 10.4× | 2026-08-31 | v154 × feat:printing | 8 | 100% answered, 4.7h | recurring | [1601286](https://support.mozilla.org/questions/1601286 "Ik kan niet meer printen vanuit Thunderbird. Is er een storing?") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") [1601367](https://support.mozilla.org/questions/1601367 "PDF se vytiskne prázdné.") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") +2 |
| weekly | 8.1× | 2026-08-17 | v154 × feat:printing | 7 | 43% answered (below 60%), 3.2h | new | [1599257](https://support.mozilla.org/questions/1599257 "Print emails") [1599261](https://support.mozilla.org/questions/1599261 "Perchè non si riesce a stampare diretta mente da Thunderbird un allegato ad un m") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") [1599333](https://support.mozilla.org/questions/1599333 "can not print attachments") [1599495](https://support.mozilla.org/questions/1599495 "Thunderbird can't print files") [1599560](https://support.mozilla.org/questions/1599560 "PDF Files not printing from Thunderbird since last update") +1 |
| weekly | 4.0× | 2026-08-24 | v153 × m:spectrum | 4 | 75% answered, 3.7h | spreading | [1600000](https://support.mozilla.org/questions/1600000 "Suddenly can't send/receive emails") [1600041](https://support.mozilla.org/questions/1600041 "I can receive but not send emails") [1600103](https://support.mozilla.org/questions/1600103 "Cannot send or receive email. (locked duplicate)") [1601143](https://support.mozilla.org/questions/1601143 "IMAP accounts no longer update - Charter/Spectrum email hosting") |
| weekly | 3.8× | 2026-08-31 | v154 × feat:attachments | 5 | 100% answered, 3.5h | spreading | [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") [1601835](https://support.mozilla.org/questions/1601835 "I have problems as I can not send attachments") |
| daily | 3.5× | 2026-08-14 | v153 × proto:pop | 4 | 100% answered, 8.0h | recurring | [1598311](https://support.mozilla.org/questions/1598311 "Thunderbird went goofy for multiple gmail accounts - deleted email does not show") [1598314](https://support.mozilla.org/questions/1598314 "Email from Roadrunner.com does not show but server test works") [1598327](https://support.mozilla.org/questions/1598327 "Unable to receive e-mail") [1598357](https://support.mozilla.org/questions/1598357 "Recently Unable to send (SMTP) from Thunderbird from Cox.com (now thru Yahoo).") |
| daily | 3.3× | 2026-08-13 | v153 × proto:pop | 4 | 100% answered, 1.2h | recurring | [1598091](https://support.mozilla.org/questions/1598091 "thunderbird has stopped receiving emails from century link") [1598146](https://support.mozilla.org/questions/1598146 "Can't access my account") [1598151](https://support.mozilla.org/questions/1598151 "How to set up automatic email forwarding from Thunderbird to Gmail") [1598175](https://support.mozilla.org/questions/1598175 "Thunderbird won't download email messages from Yahoo (formerly Cox) account") |
| daily | 3.3× | 2026-08-04 | v153 × m:microsoftemail | 5 | 100% answered, 0.8h | spreading | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") |
| daily | 3.3× | 2026-08-10 | v153 × proto:pop | 4 | 75% answered, 1.1h | spreading | [1597551](https://support.mozilla.org/questions/1597551 "Thunderbird POP stopped retrieving email from one mail box, No error message") [1597571](https://support.mozilla.org/questions/1597571 "Email collection over pop failed on one account, server settings rejected when I") [1597638](https://support.mozilla.org/questions/1597638 "How logging onto wowway with old password?") [1597683](https://support.mozilla.org/questions/1597683 "Hotmail personal account: IMAP OAuth2 works but SMTP OAuth2 fails with message: ") |
| weekly | 3.3× | 2026-08-24 | v154 × m:spectrum | 8 | 88% answered, 13.7h | recurring | [1600052](https://support.mozilla.org/questions/1600052 "Trouble connecting to my email provider Time Warner Corporation to send emails u") [1600872](https://support.mozilla.org/questions/1600872 "I can send email but can not receive.") [1600919](https://support.mozilla.org/questions/1600919 "how Can i get help when my email doesn't work?") [1600982](https://support.mozilla.org/questions/1600982 "Thunderbird not working again with Spectrum emails.") [1601056](https://support.mozilla.org/questions/1601056 "Thunderbird 154.0 is causing extremem issues with Spectrum email. HELP Please") [1601071](https://support.mozilla.org/questions/1601071 "After update I cant send or receive Charter emails") +2 |
| weekly | 3.1× | 2026-08-17 | v154 × m:spectrum | 4 | 100% answered, 4.2h | spreading | [1599683](https://support.mozilla.org/questions/1599683 "Suddenly not receiving email") [1599738](https://support.mozilla.org/questions/1599738 "Thunderbird is not receiving in coming mail from Charter") [1599818](https://support.mozilla.org/questions/1599818 "Thunderbird not connecting to server.  Cannot send or receive emails.") [1599874](https://support.mozilla.org/questions/1599874 "Ability to send emails using roadrunner (mail.twc.com) account") |
| weekly | 3.1× | 2026-07-27 | v153 × m:comcast | 4 | 75% answered, 5.4h | spreading | [1595937](https://support.mozilla.org/questions/1595937 "Need help recovering my profile from a zip file") [1595941](https://support.mozilla.org/questions/1595941 "Why can't Thunderbird use new yahoo email platform for Comcast on MacBook Air?") [1596164](https://support.mozilla.org/questions/1596164 "With version 153: Unable to send from gmail account.  And cannot create a new gm") [1596297](https://support.mozilla.org/questions/1596297 "Trying to set APP Password to connect with Yahoo Mail conversion at Comcast.") |
| monthly | 3.1× | 2026-08 | v154 × m:spectrum | 13 | 92% answered, 4.2h | spreading | [1599683](https://support.mozilla.org/questions/1599683 "Suddenly not receiving email") [1599738](https://support.mozilla.org/questions/1599738 "Thunderbird is not receiving in coming mail from Charter") [1599818](https://support.mozilla.org/questions/1599818 "Thunderbird not connecting to server.  Cannot send or receive emails.") [1599874](https://support.mozilla.org/questions/1599874 "Ability to send emails using roadrunner (mail.twc.com) account") [1600052](https://support.mozilla.org/questions/1600052 "Trouble connecting to my email provider Time Warner Corporation to send emails u") [1600872](https://support.mozilla.org/questions/1600872 "I can send email but can not receive.") +7 |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 10 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 12.7× | 2026-08-24 | feat:printing | 19 | 84% answered, 7.5h | 1.5 | [1599969](https://support.mozilla.org/questions/1599969 "[Known Issue] Thunderbird printing empty PDF files.") [1600094](https://support.mozilla.org/questions/1600094 "nejde tisk z thunderbirdu") [1600149](https://support.mozilla.org/questions/1600149 "Thunderbird 154 PDF preview prints blank pages") [1600152](https://support.mozilla.org/questions/1600152 "URGENT: Thunderbird 154.0 is unable to print emails and is producing blank pages") [1600228](https://support.mozilla.org/questions/1600228 "kan ineens een PDF bijlage bij een Thunderbird mailtje niet meer direct printen.") [1600392](https://support.mozilla.org/questions/1600392 "Printing from Thunderbird since version 154.0 on Windows 11 produces only blank ") +13 |
| weekly | 11.0× | 2026-08-17 | m:spectrum | 11 | 100% answered, 8.0h | 1.0 | [1598964](https://support.mozilla.org/questions/1598964 "Thunderbird connection resets when using Mozilla VPN.") [1599516](https://support.mozilla.org/questions/1599516 "When trying to send an email it will not go") [1599553](https://support.mozilla.org/questions/1599553 "I can't receive or send Charter emails in thunderbird.") [1599681](https://support.mozilla.org/questions/1599681 "I am unable to send and receive emails on two of my computers. I can do that onl") [1599683](https://support.mozilla.org/questions/1599683 "Suddenly not receiving email") [1599711](https://support.mozilla.org/questions/1599711 "I use to be able to get my email messages from Spectrum on Thunderbird, but now ") +5 |
| weekly | 10.0× | 2026-08-24 | m:spectrum | 15 | 87% answered, 3.7h | 1.5 | [1600000](https://support.mozilla.org/questions/1600000 "Suddenly can't send/receive emails") [1600041](https://support.mozilla.org/questions/1600041 "I can receive but not send emails") [1600052](https://support.mozilla.org/questions/1600052 "Trouble connecting to my email provider Time Warner Corporation to send emails u") [1600103](https://support.mozilla.org/questions/1600103 "Cannot send or receive email. (locked duplicate)") [1600207](https://support.mozilla.org/questions/1600207 "Can't get into my Spectrum email account through Thunderbird") [1600663](https://support.mozilla.org/questions/1600663 "can no longer get my e-mail") +9 |
| weekly | 8.7× | 2026-08-31 | feat:printing | 13 | 100% answered, 4.3h | 1.5 | [1601286](https://support.mozilla.org/questions/1601286 "Ik kan niet meer printen vanuit Thunderbird. Is er een storing?") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") [1601321](https://support.mozilla.org/questions/1601321 "Printing PDF attachment comes out blank") [1601367](https://support.mozilla.org/questions/1601367 "PDF se vytiskne prázdné.") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") +7 |
| weekly | 8.0× | 2026-08-17 | feat:printing | 8 | 38% answered (below 60%), 3.2h | 1.0 | [1599257](https://support.mozilla.org/questions/1599257 "Print emails") [1599261](https://support.mozilla.org/questions/1599261 "Perchè non si riesce a stampare diretta mente da Thunderbird un allegato ad un m") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") [1599333](https://support.mozilla.org/questions/1599333 "can not print attachments") [1599382](https://support.mozilla.org/questions/1599382 "Can I change the print font size for calendar?") [1599495](https://support.mozilla.org/questions/1599495 "Thunderbird can't print files") +2 |
| monthly | 8.0× | 2026-08 | feat:printing | 36 | 75% answered, 3.9h | 4.5 | [1596620](https://support.mozilla.org/questions/1596620 "How do I export/print/backup the contents of one folder?") [1596686](https://support.mozilla.org/questions/1596686 "Cannot print Pdf files from within Thunderbird") [1596958](https://support.mozilla.org/questions/1596958 "How do I change the standard number of copies in printing from Thunderbird?") [1599257](https://support.mozilla.org/questions/1599257 "Print emails") [1599261](https://support.mozilla.org/questions/1599261 "Perchè non si riesce a stampare diretta mente da Thunderbird un allegato ad un m") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") +30 |
| weekly | 3.6× | 2026-08-31 | m:spectrum | 9 | 78% answered, 37.2h | 2.5 | [1601375](https://support.mozilla.org/questions/1601375 "my spectrum password wont log me in to thunderbird why") [1601442](https://support.mozilla.org/questions/1601442 "Correct Outgoing SMPT settings for IMAP") [1601623](https://support.mozilla.org/questions/1601623 "no access to Thunderbird email through Spectrum") [1601790](https://support.mozilla.org/questions/1601790 "Charter + pop, all new messages are going to the trash folder, not my inbox, and") [1601822](https://support.mozilla.org/questions/1601822 "trouble sending and receiving messages interfacing with Spectrum (locked duplica") [1602003](https://support.mozilla.org/questions/1602003 "Spectrum Emails are disappearing from my Thunderbird Inbox after downloading. Th") +3 |
| weekly | 3.5× | 2026-08-10 | m:yahooemail | 19 | 63% answered, 3.4h | 5.5 | [1597571](https://support.mozilla.org/questions/1597571 "Email collection over pop failed on one account, server settings rejected when I") [1597605](https://support.mozilla.org/questions/1597605 "I am still canot open my yahoo.co.uk email account? I have deleted the account f") [1597650](https://support.mozilla.org/questions/1597650 "why am i getting a pop-up window demanding that I agree to allow thunderbird mai") [1597665](https://support.mozilla.org/questions/1597665 "Yahoo IMAP Mailbox Reserved Loop: Bulk folder stuck inside Trash") [1597759](https://support.mozilla.org/questions/1597759 "Why is Yahoo_mail not updatuing in Thunderbird since two weeks?") [1597789](https://support.mozilla.org/questions/1597789 "Yahoo mail authentication failure after the newest update") +13 |
| weekly | 3.4× | 2026-08-31 | feat:attachments | 17 | 88% answered, 3.5h | 5.0 | [1601321](https://support.mozilla.org/questions/1601321 "Printing PDF attachment comes out blank") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601493](https://support.mozilla.org/questions/1601493 "CANNOT SEND ATTACHMENTS OVER 36 MB") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") +11 |
| monthly | 3.2× | 2026-08 | m:spectrum | 34 | 82% answered, 4.4h | 10.5 | [1596316](https://support.mozilla.org/questions/1596316 "Thunderbird 1 of 7  email account stopped working from the Provider Spectrum and") [1596807](https://support.mozilla.org/questions/1596807 "Receiving, deleting, and sending messages is extremely slow for 1 of 2 users on ") [1597319](https://support.mozilla.org/questions/1597319 "thunderbird not able to access mail.twc.com") [1597495](https://support.mozilla.org/questions/1597495 "NO longer have Spectrum as email provider but need to preserve emails .") [1597964](https://support.mozilla.org/questions/1597964 "Roadrunner / TWC IMAP settings") [1597972](https://support.mozilla.org/questions/1597972 "Thunderbird tells me that the spectrum servers won't accept my password") +28 |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 31 rows</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | new | 2026-08-01 | tb_version_major | 153 | 13 [1596031](https://support.mozilla.org/questions/1596031 "why is thunderbird not working") [1596048](https://support.mozilla.org/questions/1596048 "thunderbrd version 153.0.1 64bit: some registered adress get filtered as spam th") | 0.0 |
| daily | new | 2026-08-02 | tb_version_major | 153 | 10 [1596185](https://support.mozilla.org/questions/1596185 "I can't send or receive emails using wifi") [1596191](https://support.mozilla.org/questions/1596191 "Events shift one hour earlier in calendar") | 0.0 |
| daily | new | 2026-08-03 | tb_version_major | 153 | 21 [1596331](https://support.mozilla.org/questions/1596331 "When a message must be Sent Later, where is the draft stored???") [1596345](https://support.mozilla.org/questions/1596345 "InsertSignature button moved from formatting toolbar to top toolbar after Thunde") | 0.0 |
| daily | new | 2026-08-04 | tb_version_major | 153 | 20 [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") | 0.0 |
| daily | 7.5× | 2026-08-05 | tb_version_major | 153 | 15 [1596705](https://support.mozilla.org/questions/1596705 "Can't create or rename Inbox subfolders in Thunderbird") [1596708](https://support.mozilla.org/questions/1596708 "TB doesn't like to connect to my Comcast internet provider sometime.") | 2.0 |
| daily | 4.9× | 2026-08-06 | tb_version_major | 153 | 22 [1596881](https://support.mozilla.org/questions/1596881 "Can no longer drag and drop email attachments from emails to folders after 153es") [1596896](https://support.mozilla.org/questions/1596896 "gmail linkage") | 4.5 |
| daily | 5.0× | 2026-08-07 | os | os:linux | 10 [1597113](https://support.mozilla.org/questions/1597113 "i just need account to identify online access to verify my online social media d") [1597136](https://support.mozilla.org/questions/1597136 "Jak spravne nastavit thunderbird pro pop3?") | 2.0 |
| daily | 3.7× | 2026-08-07 | tb_version_major | 153 | 22 [1597076](https://support.mozilla.org/questions/1597076 "Update to Thunderbird 153.0.2esr (32-bit) freezes up and locks.  SOLVED by 153.1") [1597080](https://support.mozilla.org/questions/1597080 "how many adresses can I have in a single Thunderbird email?") | 6.0 |
| daily | new | 2026-08-19 | tb_version_major | 154 | 8 [1599072](https://support.mozilla.org/questions/1599072 "Nelze zadat přihlašovací heslo") [1599085](https://support.mozilla.org/questions/1599085 "Unable to log in to my email account through the Thunderbird desktop application") | 0.0 |
| daily | new | 2026-08-20 | tb_version_major | 154 | 12 [1599228](https://support.mozilla.org/questions/1599228 "Asking for authorisation after deleting account") [1599257](https://support.mozilla.org/questions/1599257 "Print emails") | 0.0 |
| daily | new | 2026-08-21 | tb_version_major | 154 | 18 [1599422](https://support.mozilla.org/questions/1599422 "Sending e-mails does not work") [1599433](https://support.mozilla.org/questions/1599433 "Very slow to download and synchronize") | 0.0 |
| daily | new | 2026-08-22 | tb_version_major | 154 | 13 [1599566](https://support.mozilla.org/questions/1599566 "My Thunderbird is freezing up") [1599568](https://support.mozilla.org/questions/1599568 "Thunderbird is freezing up after a few minutes or when I try to select a folder.") | 0.0 |
| daily | new | 2026-08-23 | tb_version_major | 154 | 10 [1599762](https://support.mozilla.org/questions/1599762 "How do I  add my Outlook Calendar to TB 154 using Owl") [1599777](https://support.mozilla.org/questions/1599777 "mail indirmeyi çok yavaş yapıyor.nedeni nedir ? 1000 mb internet hızım var.") | 0.0 |
| daily | new | 2026-08-24 | tb_version_major | 154 | 19 [1599916](https://support.mozilla.org/questions/1599916 "Are you having problems with the program right now?") [1599944](https://support.mozilla.org/questions/1599944 "Transfer Thunderbird from PC to Laptop") | 0.0 |
| daily | new | 2026-08-25 | tb_version_major | 154 | 9 [1600116](https://support.mozilla.org/questions/1600116 "Account Passwords need frequent updating") [1600119](https://support.mozilla.org/questions/1600119 "Every time Thunderbird queries gmail, it starts downloading my hundreds of thous") | 0.0 |
| daily | new | 2026-08-26 | tb_version_major | 154 | 27 [1600375](https://support.mozilla.org/questions/1600375 "Varför är det så svårt att sortera mapparna i bokstavordning.") [1600387](https://support.mozilla.org/questions/1600387 "thunderbird pdf viewer") | 0.0 |
| daily | new | 2026-08-27 | tb_version_major | 154 | 17 [1600526](https://support.mozilla.org/questions/1600526 "Reply with Template option missing") [1600549](https://support.mozilla.org/questions/1600549 "I want to delete my account from the thunderbird server so that I can start fres") | 0.0 |
| daily | new | 2026-08-28 | tb_version_major | 154 | 17 [1600770](https://support.mozilla.org/questions/1600770 "I can't highlight words on attachments") [1600772](https://support.mozilla.org/questions/1600772 "thunderbird mail") | 0.0 |
| daily | new | 2026-08-29 | tb_version_major | 154 | 14 [1600904](https://support.mozilla.org/questions/1600904 "Trouble reading emails with a screenreader (JAWS)") [1600919](https://support.mozilla.org/questions/1600919 "how Can i get help when my email doesn't work?") | 0.0 |
| daily | new | 2026-08-30 | tb_version_major | 154 | 13 [1601071](https://support.mozilla.org/questions/1601071 "After update I cant send or receive Charter emails") [1601074](https://support.mozilla.org/questions/1601074 "I can't print attachments.") | 0.0 |
| daily | 44.0× | 2026-08-31 | tb_version_major | 154 | 22 [1601271](https://support.mozilla.org/questions/1601271 "Se stampo dal Thunderbird esce il foglio bianco") [1601273](https://support.mozilla.org/questions/1601273 "Al iniciar Thunderbird se bloquea") | 0.5 |
| monthly | new | 2026-08 | tb_version_major | 154 | 202 [1596686](https://support.mozilla.org/questions/1596686 "Cannot print Pdf files from within Thunderbird") [1598813](https://support.mozilla.org/questions/1598813 "Missing SENT messages. Folder ＂greyed out＂") | 0.0 |
| monthly | 882.0× | 2026-08 | tb_version_major | 153 | 441 [1596031](https://support.mozilla.org/questions/1596031 "why is thunderbird not working") [1596048](https://support.mozilla.org/questions/1596048 "thunderbrd version 153.0.1 64bit: some registered adress get filtered as spam th") | 0.5 |
| weekly | new | 2026-07-27 | tb_version_major | 153 | 79 [1595089](https://support.mozilla.org/questions/1595089 "add a yohoo email account") [1595090](https://support.mozilla.org/questions/1595090 "backup zip ,841mb ,will not import into thunderbird") | 0.0 |
| weekly | 137.0× | 2026-08-03 | tb_version_major | 153 | 137 [1596331](https://support.mozilla.org/questions/1596331 "When a message must be Sent Later, where is the draft stored???") [1596345](https://support.mozilla.org/questions/1596345 "InsertSignature button moved from formatting toolbar to top toolbar after Thunde") | 1.0 |
| weekly | 43.3× | 2026-08-10 | tb_version_major | 153 | 130 [1597513](https://support.mozilla.org/questions/1597513 "Migrate emails to another provider") [1597551](https://support.mozilla.org/questions/1597551 "Thunderbird POP stopped retrieving email from one mail box, No error message") | 3.0 |
| weekly | new | 2026-08-17 | tb_version_major | 154 | 63 [1598813](https://support.mozilla.org/questions/1598813 "Missing SENT messages. Folder ＂greyed out＂") [1598989](https://support.mozilla.org/questions/1598989 "Over the weekend Thuderbird stopped allowing me to send emails and will not set ") | 0.0 |
| weekly | 3.8× | 2026-08-17 | tb_version_major | 153 | 89 [1598650](https://support.mozilla.org/questions/1598650 "I am trying to restore a backed up profile for use in thunderbird.") [1598659](https://support.mozilla.org/questions/1598659 "Please remover the annpying Yahoo signip splash screen") | 23.5 |
| weekly | new | 2026-08-24 | tb_version_major | 154 | 116 [1599916](https://support.mozilla.org/questions/1599916 "Are you having problems with the program right now?") [1599944](https://support.mozilla.org/questions/1599944 "Transfer Thunderbird from PC to Laptop") | 0.0 |
| weekly | new | 2026-08-31 | tb_version_major | 155 | 77 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| weekly | 112.0× | 2026-08-31 | tb_version_major | 154 | 56 [1601271](https://support.mozilla.org/questions/1601271 "Se stampo dal Thunderbird esce il foglio bianco") [1601273](https://support.mozilla.org/questions/1601273 "Al iniciar Thunderbird se bloquea") | 0.5 |

</details>

<details markdown="1">
<summary>August 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v153 | 441 | `▅▄▇▇▅▇▇▇▅▇▄▇▇▇▅▇▇█▄▄▅▃▃▄▂▄▅▃▂▂▅` |
| v154 | 202 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▃▄▆▄▄▆▃█▅▅▅▄▇` |
| v140 | 67 | `▃▃▅▆█▅▆█▃▆█▅▁▅▆▅▅▅▁▆▅▆▆▅▅▅▅▃▃▃█` |
| v150 | 25 | `▁▁▅▁▃▆▃█▁▃▁▁▁▃▃▃▃▁▃▃▁▁▁▃▁▃▁▃▃▃▅` |
| v115 | 24 | `▃▁▃▃▆▁▃▃▁█▁▁▁▁▃▆▆▁▁▁▁▆▁▆▃█▁▁▃▁▁` |
| v151 | 7 | `▁█▁▁▁█▁▁▁▁▁█▁█▁█▁▁▁▁▁▁▁█▁▁▁▁█▁▁` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 75 | `▂▁▆▅▂▅▂▅▁▄▂▃▄▃▄▁▄█▃▅▃▄▄▁▄▄▂▁▄▄▅` |
| m:yahooemail | 55 | `▃▅▆▅▃▅▃▆▅██▅▃▆▃█▃▅▁▅▅▃▁▁▅▃▁▅▃▃█` |
| m:microsoftemail | 53 | `▄▂▇█▄▁▄▂▁▅▂▄▅▄▁▂▂▂▂▄▅▄▂▂▄▂▂▄▁▄▇` |
| m:spectrum | 34 | `▁▃▁▁▃▁▁▃▃▁▁▅▁▃▁▁▁▃▁▁▅███▃▁▃▃██▃` |
| m:comcast | 12 | `▃▃▁▁▃▁▁▁▁▁▁▁▁▁▃█▁▃▁▁▃▃▁▁▁▃▃▁▁▁▁` |
| m:att | 5 | `▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁█` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:printing | 36 | `▁▁▁▂▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▆▅▂▁▃▅█▅▂▅▂█` |
| feat:attachments | 27 | `▃▁▁▁▁▃▁▃▃▃▁▃▁▃▁▁█▁▃█▁▃▁▃▃▃▆▆▃▃█` |
| feat:junk | 24 | `▂▁█▁▁▁▁▂▄▂▁▁▂▂▁▂▂▁▂▄▄▁▁▂▂▁▁▂▄▁▁` |
| feat:addressbook | 24 | `▁▁▃▃▁▃▁█▃▃▃▃▁▃▁▆▃▆▁▁▁▃▃▃▁▃▁▆▃▁▃` |
| feat:import_export | 22 | `▁▃▁█▁▁▃█▁▃▆▁▁▁▁▁▁▁▁▃▁▃▁▃▁█▁▆▁▁█` |
| feat:calendar | 16 | `▁▅█▁▁▁▁▁▁▅▁▁▁▁▅▅█▁▁▅█▁▅▁▁█▁▁▁▅▅` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 71 | `▃▁▇▃▅▁▁▃▃█▂▂▅▆▃▂▅▆▃▁▃▅▃▆▂▇▃▂▅▃▅` |
| proto:pop | 46 | `▃▃▅▆▃▅▅▆▅█▁▁██▁▁▅▅▁▃▃▃▁▃▁▁▆▃▃▃▆` |
| proto:smtp | 44 | `▁▃█▁▃▁▃▃▃▆▁▆▆▆▃▁▃▃▃▆█▆▃▆▃█▃▆█▃█` |
| proto:oauth | 19 | `▁▁▃▁▁▁▁▆▁█▃▁▃▁▃▁▃▁▃▁▁▃▁▁▃▁▁▆▃▃▆` |
| proto:ews | 3 | `█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁` |
| proto:carddav | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁█` |

The antivirus products named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| av:bitdefender | 3 | `▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |
| av:avast | 2 | `▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁` |
| av:defender | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁` |
| av:mcafee | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁▁▁` |
| av:kaspersky | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁▁▁` |
| av:norton | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 750 | `▃▂▅▅▃▄▄▅▃▅▂▅▅▅▃▃▅▅▄▅▆▅▄▆▄█▆▅▄▃▇` |
| os:linux | 93 | `▄▃▃▂▃▄█▅▁▃▄▂▂▃▄▅▂▃▂▂▂▃▂▂▄▂▂▂▁▄▅` |
| os:macos | 59 | `▂▂▂▅█▅▃▃▃▂▅▂▂▁▅█▂▆▂▁▃▃▂▅▂▂▃▁▂▃▃` |
| os:android | 10 | `▁▃▁▁▁▃▁▆▁▁▃▃▁▁▁▁▁█▁▁▁▁▁▁▁▃▁▁▁▁▁` |
| os:other | 6 | `▁▅▁▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁▁▁` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:tahoe | 4 | `▁▁▁▁█▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁` |
| macos:monterey | 2 | `▁▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sequoia | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁█▁▁` |
| macos:sonoma | 1 | `▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sierra | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:ventura | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward August 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
