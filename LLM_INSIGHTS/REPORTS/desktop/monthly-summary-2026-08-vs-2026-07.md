---
layout: base
title: Desktop LLM Insights — August 2026
---

# Thunderbird Desktop — LLM Insights (Engineering)

## August 2026 against July 2026

## TL;DR: the five issues to look at first {#tldr}

| # | Issue | July 2026 | August 2026 | Severity | Resolved | Known status |
|--:|:--|--:|--:|--:|--:|:--|
| [1](#issue-1) | [PDF/email attachments print as blank pages (154 regression)](#issue-1) | 1 | 38 | 3.3 | 37% (below 50%) | Fixed in Thunderbird 155, released 2026-09-01 (Bugzilla 2065922). The reports that arrive after that date come from users still on 154. |
| [2](#issue-2) | [Spectrum/Charter/Roadrunner mail download and connection failures (m:spectrum)](#issue-2) | 3 | 34 | 4.3 | 62% | — |
| [3](#issue-3) | [Compose window Send button / composition toolbar missing (bug 1989214)](#issue-3) | 8 | 28 | 3.1 | 89% | — |
| [4](#issue-4) | [Thunderbird hangs or freezes at startup (System Integration dialog)](#issue-4) | 8 | 22 | 4.2 | 59% | — |
| [5](#issue-5) | [Thunderbird freezes/crashes during use or on message load](#issue-5) | 14 | 25 | 4.1 | 60% | — |

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

| | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 731 | 940 | ▲ +209 (+29%) |
| Distinct issue clusters | 119 | 117 | ▼ -2 |
| New issue clusters this month | — | 0 | |

Attachment printing and Spectrum mail failures drive an August support surge that Thunderbird engineering must triage first

Support volume rose from 731 questions in July to 940 in August, a jump of 209. No brand new problem clusters appeared. The growth came from existing clusters getting much worse after the 153 and 154 releases. Attachments questions more than tripled, from 17 to 55. Performance and crash questions more than doubled, from 29 to 69.

The sharpest new pain is rank 1, blank pages when printing PDF and email attachments. It went from 1 question to 38 in one month. Only 37 percent of those threads reached a resolution, meaning support had no working fix to give. This pattern points at a print or PDF rendering regression, that is a bug introduced by the 154 release. Rank 7, broken drag and drop of messages and attachments to the file system after 153, points at the same release window and likely shares a file handling root cause.

The most severe pain sits with one provider. Rank 2 covers Spectrum, Charter and Roadrunner mail download and connection failures. Thirty one of its 34 questions scored severity 4 or higher, so users lost mail access entirely. This looks like a server side authentication or TLS change at the provider, not a Thunderbird build issue, but Thunderbird must confirm and publish guidance.

Two credential clusters are served worst. Rank 11, Yahoo, AT&T and AOL password rejections, resolved only 29 percent of the time. Rank 9, repeated password prompts, left 42 percent of users with no reply at all. Both suggest gaps in app specific password handling and in stored credential renewal.

## Issues to investigate {#issues-to-investigate}

The order comes from a Python score. It weights new clusters, badly served clusters, severity and volume, in that order. Resolved means the question has an accepted solution, or a trusted contributor gave the last answer. A resolved figure under 50% is marked.

### 1. PDF/email attachments print as blank pages (154 regression) {#issue-1}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| PDF/email attachments print as blank pages (154 regression) (attachments) | 1 | 38 | ▲ +37 | 3.3 (12) | 37% (below 50%) | 21% |

- Known status: Fixed in Thunderbird 155, released 2026-09-01 (Bugzilla 2065922). The reports that arrive after that date come from users still on 154.
- Why it matters: Printing attachments as blank pages jumped from 1 to 38 questions and only 37 percent of users got a fix.
- What to look at: Engineering must bisect print and PDF viewer changes in the 154 release and reproduce blank output across Windows print drivers.
- Example questions: [1600414](https://support.mozilla.org/questions/1600414 "Puste strony i brak podglądu przy drukowaniu załączników PDF (Canon MF450, Windo") [1600149](https://support.mozilla.org/questions/1600149 "Thunderbird 154 PDF preview prints blank pages") [1601389](https://support.mozilla.org/questions/1601389 "Problema  con ultimo  aggiornamento") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") +1

### 2. Spectrum/Charter/Roadrunner mail download and connection failures (m:spectrum) {#issue-2}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Spectrum/Charter/Roadrunner mail download and connection failures (m:spectrum) (send-receive) | 3 | 34 | ▲ +31 | 4.3 (31) | 62% | 15% |

- Why it matters: Spectrum, Charter and Roadrunner users lost mail access outright, with 31 of 34 reports at the top severity band.
- What to look at: Engineering must capture connection logs from affected accounts and check for a provider side authentication, port or TLS change.
- Example questions: [1599681](https://support.mozilla.org/questions/1599681 "I am unable to send and receive emails on two of my computers. I can do that onl") [1599818](https://support.mozilla.org/questions/1599818 "Thunderbird not connecting to server.  Cannot send or receive emails.") [1600663](https://support.mozilla.org/questions/1600663 "can no longer get my e-mail") [1600000](https://support.mozilla.org/questions/1600000 "Suddenly can't send/receive emails") [1601143](https://support.mozilla.org/questions/1601143 "IMAP accounts no longer update - Charter/Spectrum email hosting") +1

### 3. Compose window Send button / composition toolbar missing (bug 1989214) {#issue-3}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Compose window Send button / composition toolbar missing (bug 1989214) (ui-ux) | 8 | 28 | ▲ +20 | 3.1 (9) | 89% | 4% |

- Why it matters: The missing Send button and compose toolbar hit 28 users, up from 8, though 89 percent got a workaround.
- What to look at: x
- Example questions: [1596605](https://support.mozilla.org/questions/1596605 "SEND button vanished after update (bug1989214)") [1597835](https://support.mozilla.org/questions/1597835 "No button to send my emails (bug1989214)") [1596368](https://support.mozilla.org/questions/1596368 "Verzendknop ontbreekt sinds update naar 153.0.1") [1596407](https://support.mozilla.org/questions/1596407 "Errors in compose menu after Update to 153.0.1esr (Menus gone)") [1597318](https://support.mozilla.org/questions/1597318 "THe Send button has vanished in T'bird (bug1989214)") +1

### 4. Thunderbird hangs or freezes at startup (System Integration dialog) {#issue-4}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Thunderbird hangs or freezes at startup (System Integration dialog) (performance-crash) | 8 | 22 | ▲ +14 | 4.2 (19) | 59% | 23% |

- Why it matters: Startup hangs tied to the System Integration dialog reached 22 reports at 4.2 mean severity, and 23 percent of askers got no reply.
- What to look at: Engineering must review the default mail client check on startup for a blocking call and add a timeout.
- Example questions: [1596205](https://support.mozilla.org/questions/1596205 "Lost my accounts in Mozilla Thunderbird") [1598140](https://support.mozilla.org/questions/1598140 "8/12/26 update cleared icon and TB files from program folders.") [1600335](https://support.mozilla.org/questions/1600335 "Thunderbird freezes after startup. I tried restarting, Troubleshoot Mode, and bo") [1598917](https://support.mozilla.org/questions/1598917 "System integration not responding, preventing access to Thunderbird") [1596317](https://support.mozilla.org/questions/1596317 "Dal 17/07 Thunderbird si avvia in background ma non mostra la finestra (funziona") +1

### 5. Thunderbird freezes/crashes during use or on message load {#issue-5}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Thunderbird freezes/crashes during use or on message load (performance-crash) | 14 | 25 | ▲ +11 (+79%) | 4.1 (20) | 60% | 20% |

- Why it matters: Freezes and crashes during normal use grew to 25 reports with 20 at high severity.
- What to look at: Engineering must pull crash and hang signatures from 153 and 154 telemetry and compare against message load paths.
- Example questions: [1601279](https://support.mozilla.org/questions/1601279 "Thunderbird va in crasi alla connessione") [1599740](https://support.mozilla.org/questions/1599740 "I have a Win 11 mozilla app which has had several experiments to overcome sudden") [1601277](https://support.mozilla.org/questions/1601277 "Thundrbird va in crash all'accesso") [1601273](https://support.mozilla.org/questions/1601273 "Al iniciar Thunderbird se bloquea") [1598340](https://support.mozilla.org/questions/1598340 "I was deleting old emails a few days ago and my email froze. It hasn’t responded") +1

### 6. Cannot send or receive at all / no connection to mail server {#issue-6}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot send or receive at all / no connection to mail server (send-receive) | 11 | 21 | ▲ +10 (+91%) | 4.5 (19) | 52% | 29% |

- Why it matters: Total send and receive failure carries the highest mean severity at 4.5 and leaves 29 percent of askers unanswered.
- What to look at: Engineering must check whether these reports overlap with rank 2 or form a separate connection stack regression.
- Example questions: [1601287](https://support.mozilla.org/questions/1601287 "Buongiorno, non riesco ad inviare e ricevere mail") [1600053](https://support.mozilla.org/questions/1600053 "My email will not connect to the server, cannot get messages") [1597006](https://support.mozilla.org/questions/1597006 "Although I use the right Password I cannot get any connection to my postbox nor ") [1601282](https://support.mozilla.org/questions/1601282 "Na installatie nwe versie komt er geen mail meer binnen en kan ik geen mail verz") [1598269](https://support.mozilla.org/questions/1598269 "IMAP/SMTP server connected, but receives and send fails") +1

### 7. Drag-and-drop of messages/attachments to filesystem broken after 153 {#issue-7}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Drag-and-drop of messages/attachments to filesystem broken after 153 (attachments) | 1 | 16 | ▲ +15 | 3.2 (3) | 56% | 19% |

- Why it matters: Drag and drop of messages and attachments to the file system broke after 153, moving from 1 report to 16.
- What to look at: Engineering must test file drag targets on all three desktop platforms against the 153 file handling changes.
- Example questions: [1597011](https://support.mozilla.org/questions/1597011 "trascinamento fallisce con tutti i PDF") [1597120](https://support.mozilla.org/questions/1597120 "Drag-and-drop email export to Windows Explorer no longer works in Thunderbird 15") [1601351](https://support.mozilla.org/questions/1601351 "Thunderbird shuts down when I try to drag items to a different folder.") [1596881](https://support.mozilla.org/questions/1596881 "Can no longer drag and drop email attachments from emails to folders after 153es") [1596923](https://support.mozilla.org/questions/1596923 "Errore durante lo spostamento del file o della cartella") +1

### 8. Password forgotten / cannot recover stored account password {#issue-8}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Password forgotten / cannot recover stored account password (account-login) | 17 | 26 | ▲ +9 (+53%) | 2.9 (11) | 50% | 31% |

- Why it matters: Stored password recovery requests rose to 26 and 31 percent of those users received no answer.
- What to look at: Engineering must review whether the password manager exposes saved credentials clearly enough after recent profile changes.
- Example questions: [1601104](https://support.mozilla.org/questions/1601104 "retrouver messagerie de Thunderbird car mots de passe non reconnus") [1599457](https://support.mozilla.org/questions/1599457 "Login to server with account / password fails suddenly") [1599085](https://support.mozilla.org/questions/1599085 "Unable to log in to my email account through the Thunderbird desktop application") [1600066](https://support.mozilla.org/questions/1600066 "I can't sign into my thunderbird email account because I dont have a passord tha") [1599916](https://support.mozilla.org/questions/1599916 "Are you having problems with the program right now?") +1

### 9. Repeated password prompts despite saved credentials {#issue-9}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Repeated password prompts despite saved credentials (account-login) | 19 | 24 | ▲ +5 (+26%) | 3.5 (11) | 42% (below 50%) | 42% |

- Why it matters: Repeated password prompts despite saved credentials resolved only 42 percent of the time and left 42 percent unanswered, the worst reply rate on the list.
- What to look at: Engineering must trace token refresh and credential store reads when a saved password exists but the server rejects it.
- Example questions: [1599070](https://support.mozilla.org/questions/1599070 "impossible to connect to my mail serveur; ask always same question about pass wo") [1599359](https://support.mozilla.org/questions/1599359 "thunderbird is no longer syncing with my server") [1600807](https://support.mozilla.org/questions/1600807 "Thunderbird won't accept correct password") [1597195](https://support.mozilla.org/questions/1597195 "thunderbird keeps forgetting my email account passwords") [1600726](https://support.mozilla.org/questions/1600726 "New problem last 2 months! email login(s) not being remembered on all 8 emails?") +1

### 10. Message body blank / not rendering {#issue-10}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Message body blank / not rendering (send-receive) | 12 | 19 | ▲ +7 (+58%) | 3.7 (13) | 47% (below 50%) | 32% |

- Why it matters: Blank message bodies reached 19 reports with 13 at high severity and only 47 percent resolved.
- What to look at: Engineering must check message rendering and remote content handling for a regression that empties the reading pane.
- Example questions: [1601048](https://support.mozilla.org/questions/1601048 "8.29.2026 Once again I am having same problem with email content not loading. No") [1600007](https://support.mozilla.org/questions/1600007 "My emails won't open, none show up in sent or delete files, it is very slow to l") [1600073](https://support.mozilla.org/questions/1600073 "Inbox email shows only sender and subject line.  Content not available,") [1600049](https://support.mozilla.org/questions/1600049 "8.24.2026 As of yesterday, Thunderbird Inbox messages are being received and old") [1600832](https://support.mozilla.org/questions/1600832 "Emails have down loaded without headings and sometimes without text") +1

### 11. Yahoo/AT&T/AOL account password rejected; app-specific password required (m:yahooemail) {#issue-11}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Yahoo/AT&T/AOL account password rejected; app-specific password required (m:yahooemail) (account-login) | 6 | 14 | ▲ +8 | 4.0 (11) | 29% (below 50%) | 36% |

- Why it matters: Yahoo, AT&T and AOL password rejections resolved just 29 percent of the time, the worst outcome of any cluster.
- What to look at: Engineering must add an in product prompt that detects these providers and guides users to create an app specific password.
- Example questions: [1597317](https://support.mozilla.org/questions/1597317 "As of yesterday, only one of my email accounts is functioning in thunderbird.  c") [1597789](https://support.mozilla.org/questions/1597789 "Yahoo mail authentication failure after the newest update") [1598357](https://support.mozilla.org/questions/1598357 "Recently Unable to send (SMTP) from Thunderbird from Cox.com (now thru Yahoo).") [1600856](https://support.mozilla.org/questions/1600856 "How can I reinstall and save emails in three email accounts?") [1601420](https://support.mozilla.org/questions/1601420 "Thunderbird can't login to my incoming mail server.") +1

### 12. Folders or messages disappeared from folder pane {#issue-12}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Folders or messages disappeared from folder pane (search-folders) | 35 | 28 | ▼ -7 (-20%) | 3.4 (13) | 50% | 29% |

- Why it matters: Disappearing folders and messages fell from 35 to 28 reports but still leaves half of users unresolved and 29 percent unanswered.
- What to look at: Engineering must review local folder index rebuilds and IMAP subscription state for silent folder loss.
- Example questions: [1596378](https://support.mozilla.org/questions/1596378 "cartelle cscomparse account posta hotmail") [1598431](https://support.mozilla.org/questions/1598431 "Disparition. des mails") [1599320](https://support.mozilla.org/questions/1599320 "WHERE ARE MY FOLDERS") [1598837](https://support.mozilla.org/questions/1598837 "Lost subfolders and emails within") [1601281](https://support.mozilla.org/questions/1601281 "sono scomparse la sottocartelle e email da ＂cartelle locali＂, come rimediare?") +1

## Category mix, month over month

| Category | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| send-receive | 122 | 169 | ▲ +47 (+39%) |
| account-login | 117 | 141 | ▲ +24 (+21%) |
| ui-ux | 94 | 118 | ▲ +24 (+26%) |
| settings-config | 60 | 75 | ▲ +15 (+25%) |
| other | 64 | 72 | ▲ +8 (+12%) |
| performance-crash | 29 | 69 | ▲ +40 (+138%) |
| search-folders | 58 | 56 | ▼ -2 (-3%) |
| sync-oauth | 38 | 55 | ▲ +17 (+45%) |
| attachments | 17 | 55 | ▲ +38 (+224%) |
| migration-import | 58 | 49 | ▼ -9 (-16%) |
| spam-filters | 24 | 28 | ▲ +4 (+17%) |
| calendar-tasks | 20 | 20 | ▬ 0 (+0%) |
| encryption-security | 16 | 17 | ▲ +1 (+6%) |
| addons-extensions | 14 | 16 | ▲ +2 (+14%) |

---

This is a prototype. Claude claude-opus-5 wrote the labels for each question, and this run of the report cost $0.06. The page covers August 2026 against July 2026. Facts the corpus cannot know, such as a shipped fix, come from `LLM_INSIGHTS/known-status.csv` and appear as Known status.

Last updated: 2026-09-10 07:38 UTC
