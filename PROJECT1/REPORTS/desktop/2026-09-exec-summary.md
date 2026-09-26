---
layout: base
title: "2026-09 exec summary: Thunderbird Desktop support spikes"
---

# September 2026: Thunderbird Desktop support spikes

Executive summary for 2026-09. It covers 837 Thunderbird Desktop support questions. The tool wrote this page on 2026-09-26 05:33 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## September 2026: 25 spikes to investigate

17 of them tie to a Thunderbird version. 8 of them are cause-level. Every row is in the collapsed blocks below.

September 2026 is still in progress. The counts will grow.

In short: Alice it and Printing. Both are in [What stands out](#what-stands-out), with 7 smaller clusters.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 5 | 9 | 3 |
| cause-level (mail host, protocol, antivirus, feature) | 2 | 5 | 1 |

Three more numbers for context:

- Volume: 837 questions. 385 of them (46%) carry a cause tag. The count per day was `▅▇▇▅▄▄▇▆▆▅▆▃▄▅▆▆▅▄▃▃▅▆█▆▄▁`, one block per day from September 1 to September 26.
- Answers: 612 of the 837 questions (73%) got an answer from somebody other than the person who asked. The middle time to the first answer was 3.6 hours.
- Release-adoption version spikes: 35. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All September 2026 detail](#all-september-2026-detail) below.

## What stands out {#what-stands-out}

1. Alice it ([`m:alice_it`](explorer.html#grain=monthly&cause=m:alice_it&period=2026-09), 8 spikes): 20 questions in September, 20.0 times the baseline of 1.0. It peaked on 2026-09-23 with 9 questions, where earlier periods had none.
2. Printing ([`feat:printing`](explorer.html#grain=monthly&cause=feat:printing&period=2026-09), 4 spikes): 8 questions in September, under the monthly bar. It peaked on 2026-09-01 at 18.6 times expected, on Thunderbird 154.
3. Virgin Media ([`m:virginmedia`](explorer.html#grain=monthly&cause=m:virginmedia&period=2026-09), 1 spike): 6 questions in September, under the monthly bar. It peaked in the week of 2026-09-07 at 17.3 times expected, on Thunderbird 155.
4. Microsoft mail ([`m:microsoftemail`](explorer.html#grain=monthly&cause=m:microsoftemail&period=2026-09), 2 spikes): 51 questions in September, under the monthly bar. It peaked on 2026-09-16 at 8.0 times its baseline.
5. Yahoo Mail ([`m:yahooemail`](explorer.html#grain=monthly&cause=m:yahooemail&period=2026-09), 3 spikes): 49 questions in September, under the monthly bar. It peaked on 2026-09-16 at 7.2 times expected, on Thunderbird 153.

4 more clusters fired: [`feat:attachments`](explorer.html#grain=monthly&cause=feat:attachments&period=2026-09), [`proto:pop`](explorer.html#grain=monthly&cause=proto:pop&period=2026-09), [`m:spectrum`](explorer.html#grain=monthly&cause=m:spectrum&period=2026-09), [`feat:filters`](explorer.html#grain=monthly&cause=feat:filters&period=2026-09). They are in the detail below.

In 2 clusters, fewer than 60% of the questions got an answer: `v155 × m:virginmedia` in the week of 2026-09-07 (25% answered), `v153 × m:yahooemail` in the week of 2026-09-07 (50% answered).

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 6 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Version and cause together:

| Grain | Lift | When | Version × Cause | Questions | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| daily | 2.7× | 2026-09-01 | v154 × proto:imap | 4 | 25% answered (below 60%), 7.2h | [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601534](https://support.mozilla.org/questions/1601534 "Thunderbird on Win11 will not send or receive emails") [1601629](https://support.mozilla.org/questions/1601629 "Login to inbound server fails") [1601635](https://support.mozilla.org/questions/1601635 "missing email from flders") |
| weekly | 2.7× | 2026-09-14 | v153 × proto:pop | 7 | 43% answered (below 60%), 3.1h | [1603956](https://support.mozilla.org/questions/1603956 "authentication problem yahoo mail cannot access OAuth dialog box") [1604479](https://support.mozilla.org/questions/1604479 "I stared to get message ＂ Connection to server Pop.mail.yahoo.com timedout＂. wha") [1604799](https://support.mozilla.org/questions/1604799 "thunderbird deleting my emails from the POP server") [1604953](https://support.mozilla.org/questions/1604953 "Thunderbird won't send emails between  2 AOL accounts") [1605422](https://support.mozilla.org/questions/1605422 "I have one POP3 email account which does not download while other POP3 email acc") [1605471](https://support.mozilla.org/questions/1605471 "Thunderbird Unable to receive or send emails from CenturyLink") +1 |
| weekly | 2.5× | 2026-08-31 | v155 × feat:junk | 5 | 100% answered, 4.4h | [1601955](https://support.mozilla.org/questions/1601955 "Are you aware of a bug since yesterday to handling of spam filters?") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder (bug2068847)") [1602105](https://support.mozilla.org/questions/1602105 "Why do ALL my new emails all go to a spam folder ?") [1602303](https://support.mozilla.org/questions/1602303 "All messages ending in spam folder thunderbird after update to snap ubuntu") [1602574](https://support.mozilla.org/questions/1602574 "can't find Junk folder") |
| daily | 2.4× | 2026-09-15 | v155 × m:microsoftemail | 4 | 75% answered, 67.3h | [1604263](https://support.mozilla.org/questions/1604263 "More lines in Title of Thunderbird appointments") [1604373](https://support.mozilla.org/questions/1604373 "Trying to get TB 155 to link with microsoft exchange account and failing - what ") [1604399](https://support.mozilla.org/questions/1604399 "SMTP blokkeert met outlook bij -mail.live.nl") [1604480](https://support.mozilla.org/questions/1604480 "Thunderbird adds a fix for quoted styles, then its own filter throws the fix awa") |

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.3× | 2026-09-07 | m:spectrum | 7 | 57% answered (below 60%), 8.8h | 3.0 | [1602946](https://support.mozilla.org/questions/1602946 "How can i access my Thunderbird  email? It stopped recognizing my password") [1603164](https://support.mozilla.org/questions/1603164 "mobile.charter.net  times out?") [1603258](https://support.mozilla.org/questions/1603258 "The server access you are using is no longer functional!!!  I have had little ac") [1603335](https://support.mozilla.org/questions/1603335 "can't get email on laptop. I can get it on phone; have Spectrum") [1603361](https://support.mozilla.org/questions/1603361 "Thunderbird is not sending or receiving e mail from Charter.net") [1603380](https://support.mozilla.org/questions/1603380 "in the last 10 days, my spectrum/charter email works only sporadically, like may") +1 |
| weekly | 2.3× | 2026-09-14 | m:microsoftemail | 23 | 65% answered, 13.0h | 10.0 | [1603932](https://support.mozilla.org/questions/1603932 "Authentication error when trying to load outlook.365.com emails to Thunderbird") [1604054](https://support.mozilla.org/questions/1604054 "Save email messages so they can be read in MS Outlook") [1604079](https://support.mozilla.org/questions/1604079 "Thunderbird emails archive") [1604105](https://support.mozilla.org/questions/1604105 "Lost emails") [1604263](https://support.mozilla.org/questions/1604263 "More lines in Title of Thunderbird appointments") [1604342](https://support.mozilla.org/questions/1604342 "Fails to connect to Outlook primary account") +17 |


</details>

---

## All September 2026 detail {#all-september-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 17 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | 76.6× | 2026-09-23 | v153 × m:alice_it | 5 | 100% answered, 3.1h | new | [1606888](https://support.mozilla.org/questions/1606888 "non mi funziona la mail alice.it") [1606928](https://support.mozilla.org/questions/1606928 "non ricevo le mail di Alicemail") [1606938](https://support.mozilla.org/questions/1606938 "Alice mail") [1607000](https://support.mozilla.org/questions/1607000 "non scarico messaggi") [1607026](https://support.mozilla.org/questions/1607026 "Non riesco a scaricare posta alice su thunderbid, mi da errore di collegamento..") |
| weekly | 45.2× | 2026-09-21 | v153 × m:alice_it | 8 | 100% answered, 2.1h | new | [1606403](https://support.mozilla.org/questions/1606403 "non ricevo posta su pino.[RIMOSSO]@alice.it, sono con starlink, nè riesco a invi") [1606888](https://support.mozilla.org/questions/1606888 "non mi funziona la mail alice.it") [1606928](https://support.mozilla.org/questions/1606928 "non ricevo le mail di Alicemail") [1606938](https://support.mozilla.org/questions/1606938 "Alice mail") [1607000](https://support.mozilla.org/questions/1607000 "non scarico messaggi") [1607026](https://support.mozilla.org/questions/1607026 "Non riesco a scaricare posta alice su thunderbid, mi da errore di collegamento..") +2 |
| daily | 18.6× | 2026-09-01 | v154 × feat:printing | 4 | 100% answered, 13.8h | recurring | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") |
| weekly | 17.3× | 2026-09-07 | v155 × m:virginmedia | 4 | 25% answered (below 60%), 5.2h | new | [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602701](https://support.mozilla.org/questions/1602701 "read emails for dryborough@ntlworld.com") [1602752](https://support.mozilla.org/questions/1602752 "Thunderbird says no new messages") [1603241](https://support.mozilla.org/questions/1603241 "lost all  virgin media and gmail account settings") |
| weekly | 16.3× | 2026-09-21 | v156 × m:alice_it | 6 | 100% answered, 0.5h | new | [1606677](https://support.mozilla.org/questions/1606677 "Uso Thunderbird e non ricevo più la posta dal server in.alice.it") [1606766](https://support.mozilla.org/questions/1606766 "problemi all'accesso e ricezione delle mail con @alice") [1606943](https://support.mozilla.org/questions/1606943 "Non riesco più a scaricare la posta in arrivo.") [1607001](https://support.mozilla.org/questions/1607001 "da alcuni giorni non scarica la posta da alice.it") [1607008](https://support.mozilla.org/questions/1607008 "sul server di alice non ricevo la posta, posso inviare ma in arrivo connessione ") [1607177](https://support.mozilla.org/questions/1607177 "Non è possibile connettersi al server in.alice.it; la connessione è stata rifiut") |
| monthly | 12.2× | 2026-09 | v153 × m:alice_it | 9 | 100% answered, 3.1h | new | [1605600](https://support.mozilla.org/questions/1605600 "Risposta alle mail diversa da prima") [1606403](https://support.mozilla.org/questions/1606403 "non ricevo posta su pino.[RIMOSSO]@alice.it, sono con starlink, nè riesco a invi") [1606888](https://support.mozilla.org/questions/1606888 "non mi funziona la mail alice.it") [1606928](https://support.mozilla.org/questions/1606928 "non ricevo le mail di Alicemail") [1606938](https://support.mozilla.org/questions/1606938 "Alice mail") [1607000](https://support.mozilla.org/questions/1607000 "non scarico messaggi") +3 |
| weekly | 11.3× | 2026-08-31 | v154 × feat:printing | 8 | 100% answered, 4.7h | recurring | [1601286](https://support.mozilla.org/questions/1601286 "Ik kan niet meer printen vanuit Thunderbird. Is er een storing?") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") [1601367](https://support.mozilla.org/questions/1601367 "PDF se vytiskne prázdné.") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") +2 |
| monthly | 9.4× | 2026-09 | v154 × feat:printing | 5 | 100% answered, 5.0h | recurring | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") [1602826](https://support.mozilla.org/questions/1602826 "When printing from Thunderbird, a white sheet is produced.") |
| monthly | 9.4× | 2026-09 | v156 × m:alice_it | 6 | 100% answered, 0.5h | new | [1606677](https://support.mozilla.org/questions/1606677 "Uso Thunderbird e non ricevo più la posta dal server in.alice.it") [1606766](https://support.mozilla.org/questions/1606766 "problemi all'accesso e ricezione delle mail con @alice") [1606943](https://support.mozilla.org/questions/1606943 "Non riesco più a scaricare la posta in arrivo.") [1607001](https://support.mozilla.org/questions/1607001 "da alcuni giorni non scarica la posta da alice.it") [1607008](https://support.mozilla.org/questions/1607008 "sul server di alice non ricevo la posta, posso inviare ma in arrivo connessione ") [1607177](https://support.mozilla.org/questions/1607177 "Non è possibile connettersi al server in.alice.it; la connessione è stata rifiut") |
| daily | 7.2× | 2026-09-16 | v153 × m:yahooemail | 4 | 75% answered, 0.8h | new | [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604699](https://support.mozilla.org/questions/1604699 "I messaggi di un account vanno anche in un secondo account") [1604799](https://support.mozilla.org/questions/1604799 "thunderbird deleting my emails from the POP server") [1604953](https://support.mozilla.org/questions/1604953 "Thunderbird won't send emails between  2 AOL accounts") |
| daily | 4.1× | 2026-09-16 | v156 × m:microsoftemail | 4 | 75% answered, 50.5h | spreading | [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") [1604697](https://support.mozilla.org/questions/1604697 "Authentication Failure outlook.office365.com only on startup") [1604835](https://support.mozilla.org/questions/1604835 "ERROR AL AÑADIR CUENTA DE OUTLOOK") [1604859](https://support.mozilla.org/questions/1604859 "autenticazione non riuscita durante la connessione al server outlook su thunderb") |
| weekly | 3.9× | 2026-08-31 | v154 × feat:attachments | 5 | 100% answered, 3.5h | spreading | [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") [1601835](https://support.mozilla.org/questions/1601835 "I have problems as I can not send attachments") |
| daily | 3.7× | 2026-09-07 | v155 × proto:pop | 4 | 75% answered, 5.2h | spreading | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |
| weekly | 3.2× | 2026-09-21 | v153 × proto:pop | 7 | 86% answered, 5.9h | new | [1606580](https://support.mozilla.org/questions/1606580 "Messages Count in Local Folder Went To Zero When  I  Changed That Folders Title") [1606920](https://support.mozilla.org/questions/1606920 "Thunderbird  již druhý den nepřijímá poštu, odesílání pošty ale funguje.") [1606928](https://support.mozilla.org/questions/1606928 "non ricevo le mail di Alicemail") [1607103](https://support.mozilla.org/questions/1607103 "On September 16, 2026, just before midnight,  my Thunderbird received its last e") [1607192](https://support.mozilla.org/questions/1607192 "Problemi con Account Alice mail") [1607243](https://support.mozilla.org/questions/1607243 "Non riesco a scaricare la posta da uno dei miei account dopo l'ultimo aggiorname") +1 |
| weekly | 3.2× | 2026-09-07 | v155 × feat:filters | 7 | 86% answered, 8.4h | spreading | [1602761](https://support.mozilla.org/questions/1602761 "Version 155.0 64 bit -- filters now totally non selective.  Fires on all message") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") [1602916](https://support.mozilla.org/questions/1602916 "message filters have stopped working.") [1603094](https://support.mozilla.org/questions/1603094 "Cuando bajo los correos estos no respetan la regla de filtro de mensaje y la may") [1603242](https://support.mozilla.org/questions/1603242 "For every filter I get a message saying that the filter could not be applied.") +1 |
| weekly | 3.1× | 2026-09-07 | v153 × m:yahooemail | 8 | 50% answered (below 60%), 7.3h | spreading | [1602816](https://support.mozilla.org/questions/1602816 "How can I get emails coming into the correct account and be able to send respons") [1602845](https://support.mozilla.org/questions/1602845 "pCENT error for Yahoo when using OAuth2") [1603033](https://support.mozilla.org/questions/1603033 "authentication errors") [1603355](https://support.mozilla.org/questions/1603355 "Update: @rocketmail.com address not recognized") [1603404](https://support.mozilla.org/questions/1603404 "Unable to write the email to the mailbox error message") [1603516](https://support.mozilla.org/questions/1603516 "I cannot send emails from my aol accounts in thunderbird, but I am still receivi") +2 |
| weekly | 3.1× | 2026-09-14 | v153 × m:yahooemail | 8 | 62% answered, 2.1h | recurring | [1603956](https://support.mozilla.org/questions/1603956 "authentication problem yahoo mail cannot access OAuth dialog box") [1604479](https://support.mozilla.org/questions/1604479 "I stared to get message ＂ Connection to server Pop.mail.yahoo.com timedout＂. wha") [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604699](https://support.mozilla.org/questions/1604699 "I messaggi di un account vanno anche in un secondo account") [1604799](https://support.mozilla.org/questions/1604799 "thunderbird deleting my emails from the POP server") [1604953](https://support.mozilla.org/questions/1604953 "Thunderbird won't send emails between  2 AOL accounts") +2 |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 8 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| daily | new | 2026-09-23 | m:alice_it | 9 | 100% answered, 0.8h | 0.0 | [1606888](https://support.mozilla.org/questions/1606888 "non mi funziona la mail alice.it") [1606928](https://support.mozilla.org/questions/1606928 "non ricevo le mail di Alicemail") [1606938](https://support.mozilla.org/questions/1606938 "Alice mail") [1606943](https://support.mozilla.org/questions/1606943 "Non riesco più a scaricare la posta in arrivo.") [1606967](https://support.mozilla.org/questions/1606967 "non mi scarica più i messaggi") [1607000](https://support.mozilla.org/questions/1607000 "non scarico messaggi") +3 |
| weekly | new | 2026-09-21 | m:alice_it | 18 | 100% answered, 1.7h | 0.0 | [1606403](https://support.mozilla.org/questions/1606403 "non ricevo posta su pino.[RIMOSSO]@alice.it, sono con starlink, nè riesco a invi") [1606677](https://support.mozilla.org/questions/1606677 "Uso Thunderbird e non ricevo più la posta dal server in.alice.it") [1606715](https://support.mozilla.org/questions/1606715 "Non ricevo i messaggi nella mia e.mail centrosaggi@alice.it") [1606766](https://support.mozilla.org/questions/1606766 "problemi all'accesso e ricezione delle mail con @alice") [1606888](https://support.mozilla.org/questions/1606888 "non mi funziona la mail alice.it") [1606928](https://support.mozilla.org/questions/1606928 "non ricevo le mail di Alicemail") +12 |
| monthly | 20.0× | 2026-09 | m:alice_it | 20 | 100% answered, 1.7h | 1.0 | [1602510](https://support.mozilla.org/questions/1602510 "Connessione rifiutata con alice.it") [1605600](https://support.mozilla.org/questions/1605600 "Risposta alle mail diversa da prima") [1606403](https://support.mozilla.org/questions/1606403 "non ricevo posta su pino.[RIMOSSO]@alice.it, sono con starlink, nè riesco a invi") [1606677](https://support.mozilla.org/questions/1606677 "Uso Thunderbird e non ricevo più la posta dal server in.alice.it") [1606715](https://support.mozilla.org/questions/1606715 "Non ricevo i messaggi nella mia e.mail centrosaggi@alice.it") [1606766](https://support.mozilla.org/questions/1606766 "problemi all'accesso e ricezione delle mail con @alice") +14 |
| daily | 8.0× | 2026-09-16 | m:microsoftemail | 8 | 62% answered, 35.0h | 1.0 | [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") [1604613](https://support.mozilla.org/questions/1604613 "Error messages.  t-bird Linux Mint ＂.p＂ and ＂UID Fetch＂") [1604697](https://support.mozilla.org/questions/1604697 "Authentication Failure outlook.office365.com only on startup") [1604774](https://support.mozilla.org/questions/1604774 "I receive this reply when launching email:   ＂Looks like there’s a problem with ") [1604835](https://support.mozilla.org/questions/1604835 "ERROR AL AÑADIR CUENTA DE OUTLOOK") [1604859](https://support.mozilla.org/questions/1604859 "autenticazione non riuscita durante la connessione al server outlook su thunderb") +2 |
| weekly | 6.5× | 2026-08-31 | feat:printing | 13 | 100% answered, 4.3h | 2.0 | [1601286](https://support.mozilla.org/questions/1601286 "Ik kan niet meer printen vanuit Thunderbird. Is er een storing?") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") [1601321](https://support.mozilla.org/questions/1601321 "Printing PDF attachment comes out blank") [1601367](https://support.mozilla.org/questions/1601367 "PDF se vytiskne prázdné.") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") +7 |
| weekly | 3.6× | 2026-08-31 | m:spectrum | 9 | 78% answered, 37.2h | 2.5 | [1601375](https://support.mozilla.org/questions/1601375 "my spectrum password wont log me in to thunderbird why") [1601442](https://support.mozilla.org/questions/1601442 "Correct Outgoing SMPT settings for IMAP") [1601623](https://support.mozilla.org/questions/1601623 "no access to Thunderbird email through Spectrum") [1601790](https://support.mozilla.org/questions/1601790 "Charter + pop, all new messages are going to the trash folder, not my inbox, and") [1601822](https://support.mozilla.org/questions/1601822 "trouble sending and receiving messages interfacing with Spectrum (locked duplica") [1602003](https://support.mozilla.org/questions/1602003 "Spectrum Emails are disappearing from my Thunderbird Inbox after downloading. Th") +3 |
| weekly | 3.4× | 2026-09-07 | feat:filters | 12 | 67% answered, 3.9h | 3.5 | [1602761](https://support.mozilla.org/questions/1602761 "Version 155.0 64 bit -- filters now totally non selective.  Fires on all message") [1602768](https://support.mozilla.org/questions/1602768 "Can't get rid of an email (junk/spam) ever with the filter.  Keeps reocurring. B") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602835](https://support.mozilla.org/questions/1602835 "Lost all email filters circa Aug. 4 (approx.) - emails impossible to use/control") [1602847](https://support.mozilla.org/questions/1602847 "Sharing Thunderbird Message filters across multiple computers") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") +6 |
| weekly | 3.4× | 2026-08-31 | feat:attachments | 17 | 88% answered, 3.5h | 5.0 | [1601321](https://support.mozilla.org/questions/1601321 "Printing PDF attachment comes out blank") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1601493](https://support.mozilla.org/questions/1601493 "CANNOT SEND ATTACHMENTS OVER 36 MB") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") +11 |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 35 rows</summary>

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
| daily | new | 2026-09-17 | tb_version_major | 156 | 15 [1605097](https://support.mozilla.org/questions/1605097 "Why is Thunderbird not always getting each SMTP (if STD) server to deliver to ra") [1605190](https://support.mozilla.org/questions/1605190 "Unified Folders - Wrond ＂Sent＂") | 0.0 |
| daily | new | 2026-09-18 | tb_version_major | 156 | 13 [1605512](https://support.mozilla.org/questions/1605512 "Inline PNG in HTML - Unable to Save Image") [1605563](https://support.mozilla.org/questions/1605563 "I have been told by OZ lotteries that your emails are being soft bounced with th") | 0.0 |
| daily | new | 2026-09-20 | tb_version_major | 156 | 11 [1606066](https://support.mozilla.org/questions/1606066 "Cannot save photos sent from iPhone as jpg on our hard drive. Have done this for") [1606067](https://support.mozilla.org/questions/1606067 "Thunderbird intermittently fails to download certain POP emails that are visible") | 0.0 |
| daily | new | 2026-09-21 | tb_version_major | 156 | 13 [1606312](https://support.mozilla.org/questions/1606312 "Thunderbird intermittently fails to download certain POP emails that are visible") [1606364](https://support.mozilla.org/questions/1606364 "Ogni volta che ravvio il pc Thunderbird perde le password.") | 0.0 |
| daily | new | 2026-09-22 | tb_version_major | 156 | 14 [1606601](https://support.mozilla.org/questions/1606601 "I can't open links in my email by simply clicking on it. Why?") [1606663](https://support.mozilla.org/questions/1606663 "Авторизация на домене @inbox.ru") | 0.0 |
| daily | new | 2026-09-23 | tb_version_major | 156 | 23 [1606863](https://support.mozilla.org/questions/1606863 "I cannot send return emails") [1606885](https://support.mozilla.org/questions/1606885 "Biglobeというプロバイダ業者のメールアカウントを設定したいがサーバーに接続できない") | 0.0 |
| daily | new | 2026-09-24 | tb_version_major | 156 | 17 [1607151](https://support.mozilla.org/questions/1607151 "Expected popup for Gmail login is missing") [1607155](https://support.mozilla.org/questions/1607155 "senders in my address book keep getting put in my spam box") | 0.0 |
| daily | new | 2026-09-25 | tb_version_major | 156 | 11 [1607411](https://support.mozilla.org/questions/1607411 "How can I hide the yellow “Your privacy is protected” bar while keeping the priv") [1607452](https://support.mozilla.org/questions/1607452 "PDF, non ecidenzia il testo") | 0.0 |
| monthly | new | 2026-09 | tb_version_major | 154 | 42 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 0.0 |
| monthly | new | 2026-09 | tb_version_major | 155 | 234 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| monthly | new | 2026-09 | tb_version_major | 156 | 137 [1603530](https://support.mozilla.org/questions/1603530 "Strange things happening with TB 156.0b3 (32-bit)  and Yahoo") [1603857](https://support.mozilla.org/questions/1603857 "beta 3 is stopped getting mails") | 0.0 |
| monthly | 63.2× | 2026-09 | tb_version_major | 153 | 158 [1601441](https://support.mozilla.org/questions/1601441 "Emails not downloading") [1601614](https://support.mozilla.org/questions/1601614 "How do I change my user name in the login in for Thunderbird?") | 2.5 |
| weekly | new | 2026-08-31 | tb_version_major | 155 | 77 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| weekly | 112.0× | 2026-08-31 | tb_version_major | 154 | 56 [1601271](https://support.mozilla.org/questions/1601271 "Se stampo dal Thunderbird esce il foglio bianco") [1601273](https://support.mozilla.org/questions/1601273 "Al iniciar Thunderbird se bloquea") | 0.5 |
| weekly | new | 2026-09-07 | tb_version_major | 155 | 104 [1602611](https://support.mozilla.org/questions/1602611 "yahoo not populating email after password change") [1602653](https://support.mozilla.org/questions/1602653 "skupiny kontaktů Google") | 0.0 |
| weekly | new | 2026-09-14 | tb_version_major | 155 | 47 [1603932](https://support.mozilla.org/questions/1603932 "Authentication error when trying to load outlook.365.com emails to Thunderbird") [1603934](https://support.mozilla.org/questions/1603934 "Thunderbird and junk mail") | 0.0 |
| weekly | new | 2026-09-14 | tb_version_major | 156 | 56 [1604559](https://support.mozilla.org/questions/1604559 "Mail sent to me as cc: and/or bcc:  (but not as To:) is received at ISP mail ser") [1604594](https://support.mozilla.org/questions/1604594 "Still can't sync outlook outgoing mail with thunderbird, i receive emails just f") | 0.0 |
| weekly | new | 2026-09-21 | tb_version_major | 155 | 6 [1606478](https://support.mozilla.org/questions/1606478 "REinstalled TB on a new PC, TB does not recognize my previous password. How to p") [1606653](https://support.mozilla.org/questions/1606653 "Thunderbird hangs while sending an email. How do I resolve issue?") | 0.0 |
| weekly | new | 2026-09-21 | tb_version_major | 156 | 79 [1606312](https://support.mozilla.org/questions/1606312 "Thunderbird intermittently fails to download certain POP emails that are visible") [1606364](https://support.mozilla.org/questions/1606364 "Ogni volta che ravvio il pc Thunderbird perde le password.") | 0.0 |

</details>

<details markdown="1">
<summary>September 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v155 | 234 | `▁▅▇▇▅▅▇▅▆▅▇▅▄▅█▃▂▂▁▁▁▂▁▁▁▁` |
| v153 | 158 | `▃▅▅▃▁▃▄▅▅▅▄▂▅▆▅▆▄▃▃▃▄▃█▅▃▁` |
| v156 | 137 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▆▅▂▄▅▅█▆▄▁` |
| v154 | 42 | `█▄▃▂▁▁▂▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| v140 | 41 | `██▆▅▃▁▅▅▆▅▅▁▅▃▁▆▁▃▁▁▃▃▅█▁▃` |
| v115 | 22 | `▁▁▁▃▃▃█▅▅▅▁▁▃▃▃▁▅▃▁▁▃▃▁▃▁▁` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 60 | `▃▄▄▆▁▃▂█▄▅▄▂▃▅▁▆▃▂▂▂▂▆▃▂▂▁` |
| m:microsoftemail | 51 | `▂▄▂▁▁▁▂▅▅▂▂▁▃▅▅█▃▃▁▃▂▅▂▃▃▁` |
| m:yahooemail | 49 | `▁▂▃▅▁▂▅▅▅▃▇▂▅▂▂█▂▃▂▃▁▅▁▆▂▁` |
| m:spectrum | 21 | `▅▅▃▁▃▅▁▃▃█▃▁▁▁▃▁▃▁▁▁▁▅▃▁▃▁` |
| m:alice_it | 20 | `▁▁▁▁▁▂▁▁▁▁▁▁▁▁▁▁▁▂▁▁▂▃█▅▁▁` |
| m:btinternet | 8 | `▁▁▁▅▁█▁▁▁▁▁▅▅▁▅▁▅▅▁▁▁▁▁▁▁▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:filters | 21 | `▁▂▂▁▂▁▄█▂▄▂▁▂▂▂▂▁▁▁▅▁▁▁▁▁▁` |
| feat:attachments | 20 | `▇█▂▄▄▁▁▁▁▄▁▁▂▁▁▂▂▁▁▁▂▁▁▁▁▁` |
| feat:junk | 19 | `▁▅▅█▅▅██▅▅█▁▅█▁▁▁▁▁▁▅▁▁▅▁▁` |
| feat:import_export | 13 | `▁█▁▁▁▃▃▁▁▁▃▃▁▆▁▃▁▁▁▁▃▃▁▃▁▁` |
| feat:addressbook | 11 | `▅▁▁▅▅▁▁▁▁▁▁▁█▁▅▅▁▁▁▁▅▅▁█▁▁` |
| feat:search | 8 | `██▁▁▁▁▁█▁▁▁▁█▁▁██▁▁▁█▁█▁▁▁` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 66 | `▆▆▅▂▂▅█▂▅▂▆▂▁▇▃▅▄▃▁▃▃▂▂▂▄▁` |
| proto:pop | 50 | `▂▅▁▂▂▂█▃▁▃▇▂▁▃▃▃▃▃▂▃▃▃▆▇▂▁` |
| proto:smtp | 48 | `▃▆▅▆▁▅▃▅▆▃▅▃▃▅▆█▆▆▁▁▆▅▅▁█▁` |
| proto:oauth | 21 | `▃▃▁█▃▁▁▃▅▁▃▁▃▅▁▅▁▃▁▁▃▃▁▁▅▁` |
| proto:caldav | 3 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁█▁` |
| proto:ews | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁` |

The antivirus products named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| av:norton | 5 | `█▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁█▁▁` |
| av:bitdefender | 4 | `▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁` |
| av:mcafee | 3 | `▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁██▁▁▁` |
| av:avast | 2 | `█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁` |
| av:defender | 2 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:surfshark | 2 | `▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 711 | `▅▇▇▅▃▄▇▅▄▅▅▃▄▅▆▆▅▄▂▃▅▅█▅▄▁` |
| os:macos | 49 | `▃▂▂▃▂▃▅▅▆▂▆▂▁▂█▂▂▁▂▃▂▅▅▆▁▂` |
| os:linux | 46 | `▁▂▄█▂▁▄▇█▄▄▂▄▂▁▇▂▂▄▁▂▇▁▅▂▂` |
| os:other | 5 | `█▁▁▁▁▁▃▁▁▁▁▁▁▁▁▃▁▁▁▁▁▁▁▁▁▁` |
| os:android | 5 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▅▁▁▁▁▁▅▁` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:tahoe | 4 | `█▅▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sequoia | 4 | `▁▁▁▁▁▁█▁█▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁` |
| macos:golden_gate | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁█▁▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward September 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
