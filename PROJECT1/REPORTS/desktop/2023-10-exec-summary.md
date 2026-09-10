---
layout: base
title: "2023-10 exec summary: Thunderbird Desktop support spikes"
---

# October 2023: Thunderbird Desktop support spikes

Executive summary for 2023-10. It covers 1977 Thunderbird Desktop support questions. The tool wrote this page on 2026-09-10 04:44 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## October 2023: 11 spikes to investigate

None of them tie to a Thunderbird version. All 11 are cause-level. Every row is in the collapsed blocks below.

In short: Frontier and Search. Both are in [What stands out](#what-stands-out), with 4 smaller clusters.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 0 | 0 | 0 |
| cause-level (mail host, protocol, antivirus, feature) | 1 | 7 | 3 |

Almost no October 2023 question carries a Thunderbird version. The version×cause detector therefore cannot fire. Read its zero as missing data, not as a clean result.

Three more numbers for context:

- Volume: 1977 questions. 685 of them (35%) carry a cause tag. The count per day was `▄▆██▆▇▅▄▆▆▇▆▅▅▃▆▆▅▆▄▄▃▄▄▄▅▅▃▃▅▄`, one block per day from October 1 to October 31.
- Answers: 1212 of the 1977 questions (61%) got an answer from somebody other than the person who asked. The middle time to the first answer was 4.4 hours.
- Release-adoption version spikes: 1. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All October 2023 detail](#all-october-2023-detail) below.

## What stands out {#what-stands-out}

1. Frontier ([`m:frontier`](explorer.html#grain=monthly&cause=m:frontier&period=2023-10), 3 spikes): 15 questions in October, 30.0 times the baseline of 0.5. It peaked in the week of 2023-10-09 with 6 questions, where earlier periods had none.
2. Search ([`feat:search`](explorer.html#grain=monthly&cause=feat:search&period=2023-10), 1 spike): 34 questions in October, 4.5 times the baseline of 7.5.
3. Add-ons ([`feat:addons`](explorer.html#grain=monthly&cause=feat:addons&period=2023-10), 1 spike): 16 questions in October, 4.0 times the baseline of 4.0.
4. Spectrum ([`m:spectrum`](explorer.html#grain=monthly&cause=m:spectrum&period=2023-10), 3 spikes): 21 questions in October, under the monthly bar. It peaked in the week of 2023-10-16 at 4.0 times its baseline.
5. IMAP ([`proto:imap`](explorer.html#grain=monthly&cause=proto:imap&period=2023-10), 1 spike): 113 questions in October, under the monthly bar. It peaked on 2023-10-11 at 3.7 times its baseline.

1 more cluster fired: [`feat:attachments`](explorer.html#grain=monthly&cause=feat:attachments&period=2023-10). It is in the detail below.

In 6 clusters, fewer than 60% of the questions got an answer: `proto:imap` on 2023-10-11 (36% answered), `m:spectrum` in the week of 2023-10-16 (38% answered), `feat:attachments` in the week of 2023-10-16 (45% answered), `m:frontier` in the week of 2023-10-09 (33% answered), and 2 more.

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 15 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.8× | 2023-10-02 | feat:junk | 11 | 64% answered, 2.5h | 4.0 | [1425933](https://support.mozilla.org/questions/1425933 "No Junk folder on new, single-account Thunderbird installation") [1425977](https://support.mozilla.org/questions/1425977 "sistema di posta bloccato a causa di attività di spam") [1426159](https://support.mozilla.org/questions/1426159 "Thunderbird 115 has no junk removal tool") [1426281](https://support.mozilla.org/questions/1426281 "Spam isn't removed from Spam filter in Mozilla Thunderbird") [1426306](https://support.mozilla.org/questions/1426306 "Help needed troubleshooting automatic junk filter") [1426388](https://support.mozilla.org/questions/1426388 "Msgs marked as junk are not moved to ＂Junk＂ folder") +5 |
| daily | 2.7× | 2023-10-27 | m:microsoftemail | 8 | 88% answered, 8.5h | 3.0 | [1429015](https://support.mozilla.org/questions/1429015 "Synchronizing multiple calendars - automatically copy events from one calendar t") [1429030](https://support.mozilla.org/questions/1429030 "Account on Thunderbird not receiving emails") [1429044](https://support.mozilla.org/questions/1429044 "All address books gone this morning") [1429089](https://support.mozilla.org/questions/1429089 "Freeze Favorites in the Inbox Left Pane") [1429106](https://support.mozilla.org/questions/1429106 "Can't send or receive messages on new Thunderbird 115.4.1") [1429108](https://support.mozilla.org/questions/1429108 "This latest upgrade to 115.4.1 ＂SUPERNOVA＂ lives up to its name - it blew up my ") +2 |
| daily | 2.7× | 2023-10-03 | proto:imap | 8 | 38% answered (below 60%), 3.4h | 3.0 | [1425973](https://support.mozilla.org/questions/1425973 "Find default profile in profiles.ini") [1425997](https://support.mozilla.org/questions/1425997 "Problema TLS con Thunderbird dopo trasferimento profilo - SOLUZIONE") [1426017](https://support.mozilla.org/questions/1426017 "No SMTP authentication method works with Synology Mail Server (SSL, port 465)") [1426028](https://support.mozilla.org/questions/1426028 "Transfer 400k email from 3 gmail accounts to 1 new account") [1426035](https://support.mozilla.org/questions/1426035 "Blank message display tabs when opening inbox and sent mails") [1426062](https://support.mozilla.org/questions/1426062 "Passwort prompt comes up for deleted account") +2 |
| weekly | 2.7× | 2023-10-09 | feat:search | 8 | 50% answered (below 60%), 11.9h | 3.0 | [1426874](https://support.mozilla.org/questions/1426874 "Can I Resize the Search Bar in Supernova?") [1427372](https://support.mozilla.org/questions/1427372 "Search bar function opens waaaaay too many emails") [1427447](https://support.mozilla.org/questions/1427447 "After the update search finds but does not open an individual email") [1427514](https://support.mozilla.org/questions/1427514 "unifed inbox searches in 802 (sub-)folders") [1427521](https://support.mozilla.org/questions/1427521 "Folder colors in search folders, or: Automatically set tags based on folder name") [1427582](https://support.mozilla.org/questions/1427582 "Turning off threading in Ctrl+Shift+F method of Search") +2 |
| weekly | 2.7× | 2023-10-02 | proto:oauth | 12 | 58% answered (below 60%), 11.1h | 4.5 | [1425833](https://support.mozilla.org/questions/1425833 "Sending emails from O365 account not working") [1426035](https://support.mozilla.org/questions/1426035 "Blank message display tabs when opening inbox and sent mails") [1426060](https://support.mozilla.org/questions/1426060 "Problems with 102 -> 115 Upgrade") [1426229](https://support.mozilla.org/questions/1426229 "Can't connect to Gmail") [1426352](https://support.mozilla.org/questions/1426352 "Cant send email from an office 365 email") [1426506](https://support.mozilla.org/questions/1426506 "I have answered my own question") +6 |
| weekly | 2.6× | 2023-10-02 | feat:attachments | 9 | 56% answered (below 60%), 12.7h | 3.5 | [1425880](https://support.mozilla.org/questions/1425880 "Can only intermittently drag and drop file attachments into email") [1426248](https://support.mozilla.org/questions/1426248 "Opening attachments from email") [1426265](https://support.mozilla.org/questions/1426265 "Email attachments disappeared after update to Version  115.2.3 Build ID  2023091") [1426330](https://support.mozilla.org/questions/1426330 "Attaching a photo to an email") [1426338](https://support.mozilla.org/questions/1426338 "Receiving emails with unwanted image attachments") [1426405](https://support.mozilla.org/questions/1426405 "Remove Attachments?") +3 |
| weekly | 2.4× | 2023-10-09 | feat:addons | 6 | 67% answered, 11.5h | 2.5 | [1426866](https://support.mozilla.org/questions/1426866 "Thunderbird 115 and up with IMAP ACL Extension") [1427086](https://support.mozilla.org/questions/1427086 "System theme auto is enabled but does not reflect system theme") [1427199](https://support.mozilla.org/questions/1427199 "Upgrade from 115.3.1 to 115.3.2 breaks Owl extension - can I downgrade to 115.3.") [1427314](https://support.mozilla.org/questions/1427314 "Thunderbird: Revert to Old Theme - new theme has too much color, blue circles fo") [1427377](https://support.mozilla.org/questions/1427377 "An Exchange account is not saved in Thunderbird (I'm using Exquilla plugin)") [1427634](https://support.mozilla.org/questions/1427634 "Why does my Thunderbird light screen AddOn keep changing to a dark screen") |
| weekly | 2.4× | 2023-10-02 | feat:search | 6 | 83% answered, 4.9h | 2.5 | [1426165](https://support.mozilla.org/questions/1426165 "Ricerca messaggi funziona male") [1426197](https://support.mozilla.org/questions/1426197 "Global Search in Thunderbird 115.3 shows wrong sender and recipient in the resul") [1426395](https://support.mozilla.org/questions/1426395 "＂C＂ key creates new email, I can't type C on search (win10)") [1426476](https://support.mozilla.org/questions/1426476 "Problemi ricerca e posizionamento cursore, dopo aggiornamento.") [1426483](https://support.mozilla.org/questions/1426483 "Search feature still doesn't work") [1426530](https://support.mozilla.org/questions/1426530 "Add-on questions regarding search engines?") |
| weekly | 2.4× | 2023-10-02 | m:yahooemail | 13 | 54% answered (below 60%), 4.9h | 5.5 | [1425912](https://support.mozilla.org/questions/1425912 "Set IMAP so that local copy does NOT get deleted when it's deleted from the serv") [1425961](https://support.mozilla.org/questions/1425961 "Mancato invio email") [1425969](https://support.mozilla.org/questions/1425969 "cannot send emails") [1425972](https://support.mozilla.org/questions/1425972 "Outgoing server error after upgrade to Thunderbird 115.3.1") [1426004](https://support.mozilla.org/questions/1426004 "Yahoo mail won't send messages from Thunderbird 115.3.1 (64-bit)") [1426018](https://support.mozilla.org/questions/1426018 "Unable to log in at server. Probably wrong configuration, username, or password'") +7 |
| weekly | 2.3× | 2023-09-25 | feat:import_export | 14 | 50% answered (below 60%), 8.2h | 6.0 | [1425043](https://support.mozilla.org/questions/1425043 "migrate email archive (+10y) to Thunderbird Linux?") [1425071](https://support.mozilla.org/questions/1425071 "Importing Outlook messages") [1425093](https://support.mozilla.org/questions/1425093 "Just installed TB: import-export-tools-ng : incompatible?") [1425193](https://support.mozilla.org/questions/1425193 "STARTED SETTING UP EMAIL ACCOUNT BUT DIDN'T HAVE BACKUP EMAIL. I HAVE ONE NOW") [1425359](https://support.mozilla.org/questions/1425359 "Reverse Migration") [1425399](https://support.mozilla.org/questions/1425399 "Migrating Thunderbird 115") +8 |
| monthly | 2.3× | 2023-10 | m:spectrum | 21 | 71% answered, 7.0h | 9.0 | [1426534](https://support.mozilla.org/questions/1426534 "Sending & Receiving Emails") [1426655](https://support.mozilla.org/questions/1426655 "Thunderbird E-Mail Behavior since latest update") [1427444](https://support.mozilla.org/questions/1427444 "Can't send email after update") [1427470](https://support.mozilla.org/questions/1427470 "twc.com account ＂junkmail＂ folder not identifiable as ＂junk＂ folder") [1427756](https://support.mozilla.org/questions/1427756 "Problem after update to 115.3.2 32 bit") [1427862](https://support.mozilla.org/questions/1427862 "unable to send emails, unable to print incoming documents") +15 |
| monthly | 2.3× | 2023-10 | m:att | 15 | 80% answered, 4.2h | 6.5 | [1425745](https://support.mozilla.org/questions/1425745 "Messages won't download on one email account since 115 update") [1426839](https://support.mozilla.org/questions/1426839 "Where are my Lost emails and pass word unrecognized after installing 115.") [1427052](https://support.mozilla.org/questions/1427052 "Thunderbird stopped downloading POP3 AT&T/Yahoo emails") [1427059](https://support.mozilla.org/questions/1427059 "Why can't I sign in after update115") [1427654](https://support.mozilla.org/questions/1427654 "Suddenly I cannot send or receive emails") [1427757](https://support.mozilla.org/questions/1427757 "Thunderbird") +9 |
| daily | 2.2× | 2023-10-12 | m:microsoftemail | 9 | 44% answered (below 60%), 1.4h | 4.0 | [1427224](https://support.mozilla.org/questions/1427224 "Account office 365 non si installa dopo ultima versione") [1427227](https://support.mozilla.org/questions/1427227 "microsoft outlook accounts, all lost from Thunderbird interface") [1427232](https://support.mozilla.org/questions/1427232 "Problem: ＂A unique identity matching the From address was not found＂") [1427240](https://support.mozilla.org/questions/1427240 "Problema con configurazione account Oulook su Thunderbird") [1427265](https://support.mozilla.org/questions/1427265 "SMTP Password not an option") [1427270](https://support.mozilla.org/questions/1427270 "Microsoft Exchange - odchozí pošta") +3 |
| daily | 2.2× | 2023-10-11 | m:microsoftemail | 9 | 44% answered (below 60%), 4.9h | 4.0 | [1427108](https://support.mozilla.org/questions/1427108 "Problemi con la nuova release di Thunderbird") [1427114](https://support.mozilla.org/questions/1427114 "Account disappeared and unable to add back again") [1427138](https://support.mozilla.org/questions/1427138 "Thunderbird update automatically merged two accounts???") [1427143](https://support.mozilla.org/questions/1427143 "missing mail") [1427155](https://support.mozilla.org/questions/1427155 "Thunderbird looses Email account when closed") [1427171](https://support.mozilla.org/questions/1427171 "Using Thunderbird email with new oauth2 and Microsoft 365") +3 |
| daily | 2.2× | 2023-10-03 | m:gmail | 9 | 78% answered, 11.6h | 4.0 | [1425997](https://support.mozilla.org/questions/1425997 "Problema TLS con Thunderbird dopo trasferimento profilo - SOLUZIONE") [1426003](https://support.mozilla.org/questions/1426003 "Outlook email missing from Unified Archives in Thunderbird.") [1426028](https://support.mozilla.org/questions/1426028 "Transfer 400k email from 3 gmail accounts to 1 new account") [1426033](https://support.mozilla.org/questions/1426033 "Disappointing release, Thunderbird Team") [1426035](https://support.mozilla.org/questions/1426035 "Blank message display tabs when opening inbox and sent mails") [1426067](https://support.mozilla.org/questions/1426067 "thunderbird - mancato reindirizzamento a siti internet") +3 |


</details>

---

## All October 2023 detail {#all-october-2023-detail}

<details markdown="1">
<summary>Version × cause spikes, 0 rows</summary>

None.

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 11 rows</summary>

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | new | 2023-10-02 | m:frontier | 9 | 67% answered, 10.5h | 0.0 | [1426135](https://support.mozilla.org/questions/1426135 "Email not working after update to SuperNova?  Multiple - gmail, dreamhost, front") [1426500](https://support.mozilla.org/questions/1426500 "Thunderbird Version	119.0b3 - hangs") [1426532](https://support.mozilla.org/questions/1426532 "Thunderbird downloading messages from frontier.com") [1426537](https://support.mozilla.org/questions/1426537 "using Frontier.com for email.  TB v 102 stopped working yesterday.  Updated to v") [1426556](https://support.mozilla.org/questions/1426556 "Tbird 115.2.1 stopped downloading emails on all accounts.") [1426687](https://support.mozilla.org/questions/1426687 "URGENT REQUEST FOR 'basic' HELP - My Email-setting has been changed by 'SKYPE'..") +3 |
| weekly | new | 2023-10-09 | m:frontier | 6 | 33% answered (below 60%), 1.0h | 0.0 | [1426814](https://support.mozilla.org/questions/1426814 "Lost download of e-mails with version 115.3.1") [1426860](https://support.mozilla.org/questions/1426860 "Cannot login") [1426996](https://support.mozilla.org/questions/1426996 "E-Mails") [1427039](https://support.mozilla.org/questions/1427039 "on log in I get to <connected to server...> and no further action.") [1427191](https://support.mozilla.org/questions/1427191 "Lost email") [1427196](https://support.mozilla.org/questions/1427196 "Thunderbird stopped logging into Frontier communications to get my email. Help") |
| monthly | 30.0× | 2023-10 | m:frontier | 15 | 53% answered (below 60%), 7.9h | 0.5 | [1426135](https://support.mozilla.org/questions/1426135 "Email not working after update to SuperNova?  Multiple - gmail, dreamhost, front") [1426500](https://support.mozilla.org/questions/1426500 "Thunderbird Version	119.0b3 - hangs") [1426532](https://support.mozilla.org/questions/1426532 "Thunderbird downloading messages from frontier.com") [1426537](https://support.mozilla.org/questions/1426537 "using Frontier.com for email.  TB v 102 stopped working yesterday.  Updated to v") [1426556](https://support.mozilla.org/questions/1426556 "Tbird 115.2.1 stopped downloading emails on all accounts.") [1426687](https://support.mozilla.org/questions/1426687 "URGENT REQUEST FOR 'basic' HELP - My Email-setting has been changed by 'SKYPE'..") +9 |
| monthly | 4.5× | 2023-10 | feat:search | 34 | 68% answered, 4.3h | 7.5 | [1426165](https://support.mozilla.org/questions/1426165 "Ricerca messaggi funziona male") [1426197](https://support.mozilla.org/questions/1426197 "Global Search in Thunderbird 115.3 shows wrong sender and recipient in the resul") [1426395](https://support.mozilla.org/questions/1426395 "＂C＂ key creates new email, I can't type C on search (win10)") [1426476](https://support.mozilla.org/questions/1426476 "Problemi ricerca e posizionamento cursore, dopo aggiornamento.") [1426483](https://support.mozilla.org/questions/1426483 "Search feature still doesn't work") [1426530](https://support.mozilla.org/questions/1426530 "Add-on questions regarding search engines?") +28 |
| weekly | 4.0× | 2023-10-16 | m:spectrum | 8 | 38% answered (below 60%), 7.0h | 2.0 | [1427756](https://support.mozilla.org/questions/1427756 "Problem after update to 115.3.2 32 bit") [1427862](https://support.mozilla.org/questions/1427862 "unable to send emails, unable to print incoming documents") [1427863](https://support.mozilla.org/questions/1427863 "unable to send emails, unable to print incoming documents") [1427897](https://support.mozilla.org/questions/1427897 "115.3.1 Will Not Allow Me To Send Emails") [1427993](https://support.mozilla.org/questions/1427993 "Sending and now receiving mail via Brighthouse.com") [1428138](https://support.mozilla.org/questions/1428138 "SMTP Server User Name across multiple email accounts") +2 |
| monthly | 4.0× | 2023-10 | feat:addons | 16 | 69% answered, 4.4h | 4.0 | [1426361](https://support.mozilla.org/questions/1426361 "GTK (Linux Mint) Theme Broken After Thunderbird Update") [1426374](https://support.mozilla.org/questions/1426374 "Deselect on Delete TB78 add-on not working") [1426530](https://support.mozilla.org/questions/1426530 "Add-on questions regarding search engines?") [1426717](https://support.mozilla.org/questions/1426717 "Temporary extension location") [1426866](https://support.mozilla.org/questions/1426866 "Thunderbird 115 and up with IMAP ACL Extension") [1427086](https://support.mozilla.org/questions/1427086 "System theme auto is enabled but does not reflect system theme") +10 |
| daily | 3.7× | 2023-10-11 | proto:imap | 11 | 36% answered (below 60%), 3.7h | 3.0 | [1427077](https://support.mozilla.org/questions/1427077 "Selecting multiple IMAP folders on Supernova running on MacOS Big Sur (11.7.10)") [1427101](https://support.mozilla.org/questions/1427101 "Thunderbird 155.3.2 past update storage grow too much") [1427104](https://support.mozilla.org/questions/1427104 "Update 15.3.2 (64-bit) broke Thunderbird") [1427127](https://support.mozilla.org/questions/1427127 "How to restore tags from a profile backup?") [1427138](https://support.mozilla.org/questions/1427138 "Thunderbird update automatically merged two accounts???") [1427163](https://support.mozilla.org/questions/1427163 "Thunderbird fails to download new mails (POP & IMAP)") +5 |
| weekly | 3.6× | 2023-10-30 | m:spectrum | 9 | 89% answered, 3.3h | 2.5 | [1429422](https://support.mozilla.org/questions/1429422 "No Incoming EMail Only Outgoing On My TWC Emai Account") [1429596](https://support.mozilla.org/questions/1429596 "Sending messages has started failing") [1429597](https://support.mozilla.org/questions/1429597 "Filtered Messages Not Syncing with IMAP Server") [1429663](https://support.mozilla.org/questions/1429663 "As of 2 days ago I am unable to send emails using my Thunderbird client.") [1429664](https://support.mozilla.org/questions/1429664 "Can't Send Emails") [1429681](https://support.mozilla.org/questions/1429681 "Can't remove email account from Thunderbird") +3 |
| weekly | 3.1× | 2023-10-16 | feat:attachments | 11 | 45% answered (below 60%), 3.1h | 3.5 | [1427710](https://support.mozilla.org/questions/1427710 "Cannot open attachments from Flatpak on Linux Mint 21") [1427763](https://support.mozilla.org/questions/1427763 "Attached photos do not display") [1427764](https://support.mozilla.org/questions/1427764 "Attached photos do not display") [1427911](https://support.mozilla.org/questions/1427911 "115.3.2 (64-bit) Thunderbird- can I set a default folder for sending attachments") [1428170](https://support.mozilla.org/questions/1428170 "email attachments") [1428179](https://support.mozilla.org/questions/1428179 "When opening attachments they are not readable") +5 |
| weekly | 3.0× | 2023-09-25 | feat:attachments | 9 | 11% answered (below 60%), 6.5h | 3.0 | [1425047](https://support.mozilla.org/questions/1425047 "Visualizzazione allegati con estensione *.jpg") [1425254](https://support.mozilla.org/questions/1425254 "Message selection moves to next message after deleting attached file") [1425486](https://support.mozilla.org/questions/1425486 "Lately, when I receive an email attachment that has a video in Thunderbird, the ") [1425576](https://support.mozilla.org/questions/1425576 "Thunderbird attachments problem.") [1425578](https://support.mozilla.org/questions/1425578 "Thunderbird not displaying SMIME signed email, but attach smime.p7m") [1425618](https://support.mozilla.org/questions/1425618 "thunderbird attachments problem") +3 |
| weekly | 3.0× | 2023-10-23 | m:spectrum | 6 | 100% answered, 8.1h | 2.0 | [1428950](https://support.mozilla.org/questions/1428950 "115.4.1 is terribly slow downloading and filtering messages.  (win10, spectrum, ") [1429003](https://support.mozilla.org/questions/1429003 "unable to send email after update to 115 10/2023") [1429052](https://support.mozilla.org/questions/1429052 "Outgoing email has stopped since Thunderbird update") [1429069](https://support.mozilla.org/questions/1429069 "email error") [1429086](https://support.mozilla.org/questions/1429086 "Newest Thunderbird version doesn't work with my internet provider") [1429098](https://support.mozilla.org/questions/1429098 "Sending email") |

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 1 row</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | 5.3× | 2023-10-04 | os | os:linux | 8 [1426156](https://support.mozilla.org/questions/1426156 "Unable to copy HTML-formatted table from Firefox on Linux") [1426159](https://support.mozilla.org/questions/1426159 "Thunderbird 115 has no junk removal tool") | 1.5 |

</details>

<details markdown="1">
<summary>October 2023 trends, 7 rows</summary>

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:gmail | 146 | `▃▆█▆▃▄▆▂▄▅▅█▇▅▄▆▄▅▃▃▅▃▃▄▆▅▃▃▃▆▅` |
| m:microsoftemail | 130 | `▆▃▃▅▅▆▃▁▆▆██▃▆▂▆▆▃▇▃▃▂▃▃▃▃▇▃▃▂▂` |
| m:yahooemail | 36 | `▃▂█▃▁▂▅▁▂▃▁▂▂▃▃▁▁▃▂▃▃▁▂▂▃▁▂▁▁▁▁` |
| m:spectrum | 21 | `▁▁▁▁▁▃▃▁▁▁▁▁▅▁▁▃▆▃▅▁▃▁▁▁▁▅█▁▁▃▅` |
| m:att | 15 | `▅▁▁▁▁▁▁▁▅█▁▁▁▁▅▅▅▅█▁▁▁▁▅▅▁█▁▁▅▁` |
| m:frontier | 15 | `▁▁▃▁▁█▆▃▅▅▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:calendar | 48 | `▂▄▇▇▇▁▁▅▂▅█▅▂▂▂▇▁▁▂▁▁▁▁▄▂▂▅▁▁▅▁` |
| feat:search | 34 | `▁▁▁▅▃▆▁▁▃▁▁▃▃▆▅▅▁▅▃▅▅▁▁▃▁▁▆▅▁█▃` |
| feat:junk | 32 | `▁▃▃█▃▃▆▆▁█▁▃▆▁▁▁▃▆▃█▃▆▁▁▁▁▆▁▁█▁` |
| feat:import_export | 31 | `█▁▃▅▁▃▅▃▁▁▃▃▁▁▃▅▆▃▅▃▅▁▃▁▁▁▃▁▃▃▅` |
| feat:attachments | 30 | `▃▃▁▆█▆▃▁▁▃▃▁▁▁▁█▃▁▆█▃▃▁▆▃█▁▁▃▁▁` |
| feat:filters | 29 | `▃▆▅█▁▃▁▅▃▃▁▁▅▅▁▃▃▃▃▁▁▁▁▁▃▃▁▁▃▅▃` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:imap | 113 | `▃▃▆▃▂▄▄▂▃▅█▃▅▄▂▄▅▄▄▂▄▃▄▁▂▂▃▁▂▃▃` |
| proto:pop | 81 | `▃▇▄█▂▁▃▄▇▅▆▃▁▁▂▆▅▄▄▂▂▂▄▃▄▂▂▁▅▅▄` |
| proto:smtp | 75 | `▃▂▇▅▂▅▂▁▁▅▂█▅▂▂▃▇▆▇▂▂▅▃▃▆▁▇▃▇▃▂` |
| proto:oauth | 28 | `▃▃▆▃▃██▃▃▆▃▆▁▁▁▆▆▁▁▁▆▁▃▁▁▁▃▁▃▁▁` |
| proto:caldav | 5 | `▁█▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁` |
| proto:carddav | 3 | `▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁` |

The antivirus products named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| av:avast | 7 | `▁▁▁▁▁█▁▁▁▁▁▁██▁▁▁▁▁▁█▁█▁█▁▁▁▁█▁` |
| av:kaspersky | 4 | `▁▅▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:eset | 4 | `▁▁█▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁` |
| av:norton | 3 | `▁▁█▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:defender | 3 | `▁▁▁▁▁▁▁▁▁▁▁▁▁██▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁` |
| av:comodo | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 198 | `▃▆█▅▇▇▃▄▆▆▆▄▅▃▄▅▆█▅▆▃▃▃▃▅▄▅▃▃▃▄` |
| os:linux | 87 | `▄▂▆█▅▄▃▅▄▅▄▃▅▂▁▄▅▃▃▂▅▃▅▂▁▃▂▄▃▄▃` |
| os:macos | 49 | `▃▁█▂▆▇▂▁▂▃▆▂▂▂▁▂▃▁▆▂▁▃▂▃▂▁▂▃▂▂▂` |

The macOS releases named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| macos:ventura | 15 | `▁▁▃▃█▁▃▁▃▆▃▁▁▁▁▁▁▁▃▁▁▆▁▁▁▁▃▁▃▁▁` |
| macos:big_sur | 6 | `▁▁█▁▁█▁▁▁▁██▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█▁▁▁` |
| macos:sonoma | 5 | `▁▁█▁▁▅▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:monterey | 4 | `█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁█▁` |
| macos:high_sierra | 2 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:mojave | 1 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward October 2023 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
