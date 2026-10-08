---
layout: base
title: Desktop LLM Insights — September 2026
---

# Thunderbird Desktop — LLM Insights (Engineering)

## September 2026 against August 2026

## TL;DR: the five issues to look at first {#tldr}

| # | Issue | August 2026 | September 2026 | Severity | Resolved | Known status |
|--:|:--|--:|--:|--:|--:|:--|
| [1](#issue-1) | [Generic 'cannot receive mail' / mail stopped arriving](#issue-1) | 29 | 50 | 4.1 | 50% | — |
| [2](#issue-2) | [TB 155 message filters with blank conditions match everything and misroute mail](#issue-2) | 2 | 35 | 4.3 | 80% | Fixed in Thunderbird 155.0.1, released 2026-09-09 (Bugzilla 2068847, duplicate 2068955). ESR 153 was never affected. 27 of the 37 September reports came before the release, and the last one arrived on 2026-09-14. |
| [3](#issue-3) | [Alice.it/TIM POP/IMAP server connection refused (m:alice_it)](#issue-3) | 1 | 21 | 4.2 | 14% (below 50%) | — |
| [4](#issue-4) | [Microsoft/Outlook OAuth2 authentication failures (m:microsoftemail)](#issue-4) | 14 | 22 | 3.8 | 18% (below 50%) | — |
| [5](#issue-5) | [AOL/Yahoo account cannot send or receive](#issue-5) | 12 | 21 | 4.1 | 33% (below 50%) | — |

Each number links to the same issue in [Issues to investigate](#issues-to-investigate) below, which carries the reason, what to look at, and the example questions.

Claude read every support question of both months. For each question it named the concrete problem, guessed a root cause and rated how much the problem hurts the user. It also read the answers: the follow-ups from the person who asked, the accepted solution, and the replies from trusted contributors.

Python did the counting and the ranking. Claude grouped the named problems and wrote the prose. Read this page as a pointer for triage, not as proof.

<details markdown="1">
<summary>Glossary</summary>

| Term | Meaning |
|:--|:--|
| question | One post by a user on the Thunderbird support site. |
| cluster | A group of questions that describe the same concrete problem. Claude reads each question and names the problem, and questions with the same named problem form one cluster. |
| new cluster | A cluster with no questions in the previous month. |
| severity | How much the problem hurts the user, from 1 (cosmetic or a how-to) to 5 (data loss or no mail at all). Claude rates each question. |
| resolved | The question has an accepted solution, or a trusted contributor gave the last answer. |
| unanswered | Nobody except the person who asked has replied. |
| rank | A Python score, not a Claude opinion. It weights new clusters, badly served clusters, severity and volume, in that order. |

</details>

## Headline

| | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 940 | 976 | ▲ +36 (+4%) |
| Distinct issue clusters | 175 | 161 | ▼ -14 |
| New issue clusters this month | — | 1 | |

Mail delivery failures drove support up in September, and three connection clusters got almost no working answers

Support volume rose from 940 to 976 questions. Send and receive problems grew most, from 169 to 233. Engineering must treat mail transport as the September focus, not the interface.

The worst user pain sits in three clusters with very low resolved rates. Resolved rate means the share of questions where the user got a fix. Alice.it and TIM users (rank 3) resolved at 14 percent. Microsoft OAuth2 failures (rank 4) resolved at 18 percent, with 55 percent of questions never answered. AOL and Yahoo failures (rank 5) resolved at 33 percent. These look like provider side changes to servers, ports or token rules that Thunderbird does not detect or explain.

One regression is clear and already well handled. The Thunderbird 155 filter bug (rank 2) jumped from 2 to 35 questions and resolves at 80 percent. Blank filter conditions match every message and misroute mail. The fix belongs in code, not in support text.

One cluster is new this month. POP downloads fail with "Unable to write the email to the mailbox" (rank 11), at 7 questions. Volume is small. Severity is high because mail can be lost on download.

## Issues to investigate {#issues-to-investigate}

The order comes from a Python score. It weights new clusters, badly served clusters, severity and volume, in that order. Resolved means the question has an accepted solution, or a trusted contributor gave the last answer. A resolved figure under 50% is marked.

### 1. Generic 'cannot receive mail' / mail stopped arriving {#issue-1}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Generic 'cannot receive mail' / mail stopped arriving (send-receive) | 29 | 50 | ▲ +21 (+72%) | 4.1 (39) | 50% | 30% |

- Why it matters: This is the largest cluster at 50 questions, up 21, and 30 percent of users got no answer at all.
- What to look at: Engineering must add clearer failure reasons to the receive path so users and helpers can tell server refusal apart from local index or profile faults.
- Example questions: [1604822](https://support.mozilla.org/questions/1604822 "Ik ontvang geen e-mails meer") [1603856](https://support.mozilla.org/questions/1603856 "Not getting my emails with Thunerbird") [1604365](https://support.mozilla.org/questions/1604365 "Connection to my email supplier has suddenly stopped showing  ＂could not connect") [1605528](https://support.mozilla.org/questions/1605528 "Can't download email via thunderbird") [1602919](https://support.mozilla.org/questions/1602919 "Why does my Thunderbird account not download new emails to my Inbox since Septem") +1

### 2. TB 155 message filters with blank conditions match everything and misroute mail {#issue-2}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| TB 155 message filters with blank conditions match everything and misroute mail (spam-filters) | 2 | 35 | ▲ +33 | 4.3 (33) | 80% | 9% |

- Known status: Fixed in Thunderbird 155.0.1, released 2026-09-09 (Bugzilla 2068847, duplicate 2068955). ESR 153 was never affected. 27 of the 37 September reports came before the release, and the last one arrived on 2026-09-14.
- Why it matters: A Thunderbird 155 regression makes filters with blank conditions match every message and misroute mail, and it grew from 2 to 35 questions.
- What to look at: Engineering must block or ignore empty filter conditions at save and at run time, and ship the fix in the next point release.
- Example questions: [1602807](https://support.mozilla.org/questions/1602807 "Thunderbird sending all inbox messages to deleted (bug2068847)") [1603340](https://support.mozilla.org/questions/1603340 "Incoming messages routed to Trash (bug2068847?)") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1603074](https://support.mozilla.org/questions/1603074 "How do I get rid of 155.0 Beta version") [1602453](https://support.mozilla.org/questions/1602453 "All of my new emails go to Trash with Thunderbird 155.0 (bug2068847)") +1

### 3. Alice.it/TIM POP/IMAP server connection refused (m:alice_it) {#issue-3}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Alice.it/TIM POP/IMAP server connection refused (m:alice_it) (send-receive) | 1 | 21 | ▲ +20 | 4.2 (21) | 14% (below 50%) | 0% |

- Why it matters: Alice.it and TIM users jumped from 1 to 21 questions and only 14 percent got a fix, the worst rate on the board.
- What to look at: Engineering must test current Alice.it and TIM server settings, then update the autoconfiguration entry for that provider.
- Example questions: [1606928](https://support.mozilla.org/questions/1606928 "non ricevo le mail di Alicemail") [1606939](https://support.mozilla.org/questions/1606939 "Da ieri 22-09-2026 non si scarica più la posta in arrivo da Alice") [1606943](https://support.mozilla.org/questions/1606943 "Non riesco più a scaricare la posta in arrivo.") [1606403](https://support.mozilla.org/questions/1606403 "non ricevo posta su pino.[RIMOSSO]@alice.it, sono con starlink, nè riesco a invi") [1602510](https://support.mozilla.org/questions/1602510 "Connessione rifiutata con alice.it") +1

### 4. Microsoft/Outlook OAuth2 authentication failures (m:microsoftemail) {#issue-4}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Microsoft/Outlook OAuth2 authentication failures (m:microsoftemail) (sync-oauth) | 14 | 22 | ▲ +8 (+57%) | 3.8 (16) | 18% (below 50%) | 55% |

- Why it matters: Microsoft OAuth2 sign in fails for 22 users, 18 percent get a fix, and 55 percent get no reply at all.
- What to look at: Engineering must capture the exact Microsoft token error in the account setup log and check tenant and consent policy changes on the Microsoft side.
- Example questions: [1602968](https://support.mozilla.org/questions/1602968 "My live.com email is neither sending or receiving using Mozilla on my desktop, b") [1608482](https://support.mozilla.org/questions/1608482 "I can't get Thunderbird to connect to Outlook") [1603527](https://support.mozilla.org/questions/1603527 "Authentication failures with new Outlook email account") [1603811](https://support.mozilla.org/questions/1603811 "All of a sudden, SMTP authentication failure to (all my) Outlook accounts") [1604859](https://support.mozilla.org/questions/1604859 "autenticazione non riuscita durante la connessione al server outlook su thunderb") +1

### 5. AOL/Yahoo account cannot send or receive {#issue-5}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| AOL/Yahoo account cannot send or receive (send-receive) | 12 | 21 | ▲ +9 (+75%) | 4.1 (18) | 33% (below 50%) | 43% |

- Why it matters: AOL and Yahoo accounts stopped sending and receiving for 21 users, with 43 percent unanswered and only 33 percent resolved.
- What to look at: Engineering must verify whether Yahoo now requires app passwords or OAuth for these accounts and surface that requirement in the error dialog.
- Example questions: [1601864](https://support.mozilla.org/questions/1601864 "Thunderbird impazzito") [1603516](https://support.mozilla.org/questions/1603516 "I cannot send emails from my aol accounts in thunderbird, but I am still receivi") [1608356](https://support.mozilla.org/questions/1608356 "Canot receive or send aol mail") [1602068](https://support.mozilla.org/questions/1602068 "thundesbird startet nicht und ich habe keinen zugriff auf das Menü, also auch ke") [1608595](https://support.mozilla.org/questions/1608595 "can't receive emails. authentication error while connecting to server. imap.mail") +1

### 6. Generic SMTP send failure while receiving works {#issue-6}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Generic SMTP send failure while receiving works (send-receive) | 22 | 28 | ▲ +6 (+27%) | 4.0 (21) | 61% | 25% |

- Why it matters: Outbound sending fails while receiving works for 28 users, which points at SMTP settings or provider port and authentication changes.
- What to look at: Engineering must review SMTP error reporting so the dialog names the rejecting server and the reason.
- Example questions: [1607890](https://support.mozilla.org/questions/1607890 "Es werten keine Mails nicht gesendet") [1602038](https://support.mozilla.org/questions/1602038 "Cannot snde out emails anymore") [1605272](https://support.mozilla.org/questions/1605272 "outgoing mail") [1602958](https://support.mozilla.org/questions/1602958 "Can not send email") [1603485](https://support.mozilla.org/questions/1603485 "Openreach recently installed fibre broadband to my home and since then I'm able ") +1

### 7. Account Settings panel unresponsive — cannot save or delete accounts (bug 2069949) {#issue-7}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Account Settings panel unresponsive — cannot save or delete accounts (bug 2069949) (settings-config) | 3 | 18 | ▲ +15 | 3.6 (10) | 67% | 11% |

- Why it matters: The Account Settings panel stops responding and users cannot save or delete accounts, growing from 3 to 18 questions under bug 2069949.
- What to look at: Engineering must prioritise bug 2069949 and check for a blocking call in the settings save path.
- Example questions: [1606631](https://support.mozilla.org/questions/1606631 "Thunderbird does not save account settings – missing prefs.js") [1606755](https://support.mozilla.org/questions/1606755 "Email Account corrupted. And unable to delete the account.") [1608317](https://support.mozilla.org/questions/1608317 "Configurazione server in uscita") [1608142](https://support.mozilla.org/questions/1608142 "Cannot delete an email address added to T'bird") [1602823](https://support.mozilla.org/questions/1602823 "Issue with settings - Acocunt details") +1

### 8. Thunderbird hangs/freezes at startup {#issue-8}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Thunderbird hangs/freezes at startup (performance-crash) | 34 | 24 | ▼ -10 (-29%) | 4.4 (21) | 38% (below 50%) | 8% |

- Why it matters: Startup hangs fell to 24 questions but carry the highest mean severity at 4.4 and resolve at only 38 percent.
- What to look at: Engineering must collect startup profiles from affected users and check folder index and add-on loading at launch.
- Example questions: [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") [1603126](https://support.mozilla.org/questions/1603126 "Thunderbird 155.0 crashes when launching on macOS macOS 15.0.1, even in Safe Mod") [1607222](https://support.mozilla.org/questions/1607222 "Thunderbird si blocca all'avvio") [1605586](https://support.mozilla.org/questions/1605586 "CON L'ULTIMO AGGIORNAMENTO MI HA PERSO MOLTE MAIL E MOLTE NON SONO PIU' VISIBILI") [1604320](https://support.mozilla.org/questions/1604320 "Thunderbird will not open on iMac - the wheel of death keeps spinning on all are") +1

### 9. Profile migration to new computer fails or loses data {#issue-9}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Profile migration to new computer fails or loses data (migration-import) | 34 | 32 | ▼ -2 (-6%) | 3.5 (16) | 69% | 12% |

- Why it matters: Profile moves to a new computer still fail or lose data for 32 users, and data loss is permanent.
- What to look at: Engineering must review the profile copy guidance and build a supported export and import path.
- Example questions: [1608722](https://support.mozilla.org/questions/1608722 "Incomplete Import From Windows to Mac") [1603977](https://support.mozilla.org/questions/1603977 "Urgently need help transferring Thunderbird...") [1606916](https://support.mozilla.org/questions/1606916 "Updating from v68 to v78 deleted all data in Thuderbird.") [1605933](https://support.mozilla.org/questions/1605933 "Thunderbird reinstall, cannot connect to recent profile. Appears to have install") [1603149](https://support.mozilla.org/questions/1603149 "email accounts disabled") +1

### 10. Missing folders after update or re-created profile {#issue-10}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Missing folders after update or re-created profile (search-folders) | 11 | 15 | ▲ +4 (+36%) | 4.0 (11) | 40% (below 50%) | 27% |

- Why it matters: Folders vanish after updates or profile rebuilds for 15 users, and only 40 percent recover them.
- What to look at: Engineering must check folder subscription and index rebuild behaviour after version upgrades.
- Example questions: [1602124](https://support.mozilla.org/questions/1602124 "Error ultima actualizacion thunderbird") [1603999](https://support.mozilla.org/questions/1603999 "ho l'account ma non trovo piu la cartella") [1604337](https://support.mozilla.org/questions/1604337 "cartelle sparite") [1606542](https://support.mozilla.org/questions/1606542 "Thunderbird 115.18.0 (64-bit update) lost all my folders and screwed up my email") [1602657](https://support.mozilla.org/questions/1602657 "Thunderbird IMAP – brak tematu i nadawcy po „Porządkuj folder”") +1

### 11. 'Unable to write the email to the mailbox' POP download failure, new this month {#issue-11}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| 'Unable to write the email to the mailbox' POP download failure (send-receive) | 0 | 7 | ▲ +7 | 4.3 (7) | 71% | 29% |

- Why it matters: This cluster is new this month and the error stops POP mail from being written to local storage, which risks message loss.
- What to look at: Engineering must check disk permissions, mailbox file locking and antivirus interference on the POP download path.
- Example questions: [1601755](https://support.mozilla.org/questions/1601755 "Thunderbird hangs due to POP3 server error right at the start.  ＂An error occurr") [1608144](https://support.mozilla.org/questions/1608144 "Thunderbird won't download messages from grandecom.net") [1602817](https://support.mozilla.org/questions/1602817 "I'm getting this message:   Unable to write the email to the mailbox. Make sure ") [1603404](https://support.mozilla.org/questions/1603404 "Unable to write the email to the mailbox error message") [1603972](https://support.mozilla.org/questions/1603972 "Unable to download emails from gmail.") +1

### 12. Spectrum/Charter/Roadrunner mail connectivity failures {#issue-12}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Spectrum/Charter/Roadrunner mail connectivity failures (send-receive) | 33 | 18 | ▼ -15 (-45%) | 4.4 (16) | 50% | 33% |

- Why it matters: Spectrum and Charter failures dropped from 33 to 18 questions but still resolve at only 50 percent with severity 4.4.
- What to look at: Engineering must confirm the current Spectrum server settings and close out the stale autoconfiguration entry.
- Example questions: [1601442](https://support.mozilla.org/questions/1601442 "Correct Outgoing SMPT settings for IMAP") [1603380](https://support.mozilla.org/questions/1603380 "in the last 10 days, my spectrum/charter email works only sporadically, like may") [1601822](https://support.mozilla.org/questions/1601822 "trouble sending and receiving messages interfacing with Spectrum (locked duplica") [1602003](https://support.mozilla.org/questions/1602003 "Spectrum Emails are disappearing from my Thunderbird Inbox after downloading. Th") [1602429](https://support.mozilla.org/questions/1602429 "Cannot connect Thunderbird to Spectrum") +1

## Category mix, month over month

| Category | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-receive | 169 | 233 | ▲ +64 (+38%) |
| account-login | 141 | 164 | ▲ +23 (+16%) |
| ui-ux | 118 | 92 | ▼ -26 (-22%) |
| settings-config | 75 | 91 | ▲ +16 (+21%) |
| migration-import | 49 | 56 | ▲ +7 (+14%) |
| performance-crash | 69 | 54 | ▼ -15 (-22%) |
| sync-oauth | 55 | 51 | ▼ -4 (-7%) |
| search-folders | 56 | 50 | ▼ -6 (-11%) |
| other | 72 | 50 | ▼ -22 (-31%) |
| spam-filters | 28 | 39 | ▲ +11 (+39%) |
| attachments | 55 | 29 | ▼ -26 (-47%) |
| encryption-security | 17 | 25 | ▲ +8 (+47%) |
| calendar-tasks | 20 | 22 | ▲ +2 (+10%) |
| addons-extensions | 16 | 20 | ▲ +4 (+25%) |

---

This is a prototype. Claude claude-opus-5 wrote the labels for each question, and this run reused the cached LLM output and cost $0.00 (the full cost is in `LLM_INSIGHTS/COSTS.md`). The page covers September 2026 against August 2026. Facts the corpus cannot know, such as a shipped fix, come from `LLM_INSIGHTS/known-status.csv` and appear as Known status.

Last updated: 2026-10-08 04:07 UTC
