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
| [2](#issue-2) | [Thunderbird hangs or freezes at startup / becomes unresponsive](#issue-2) | 18 | 36 | 4.2 | 64% | — |
| [3](#issue-3) | [Cannot send or receive at all — no server connection](#issue-3) | 14 | 31 | 4.5 | 52% | — |
| [4](#issue-4) | [Mail retrieval silently stops until restart (IMAP/POP polling stalls)](#issue-4) | 30 | 38 | 4.2 | 55% | — |
| [5](#issue-5) | [IMAP/POP login authentication failure with correct credentials](#issue-5) | 18 | 29 | 4.0 | 52% | — |

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
| Distinct issue clusters | 103 | 113 | ▲ +10 |
| New issue clusters this month | — | 0 | |

Printing and attachment regressions in 153.x and 154 drove support volume up 29 percent, and users get the least help on them

Support questions rose from 731 in July to 940 in August, a 29 percent jump. No brand new problem clusters appeared. The growth came from existing clusters getting much worse after the 153.x and 154 releases. The attachments category more than tripled, from 17 to 55 questions. Performance and crash reports went from 29 to 69.

The sharpest new pain is rank 1. PDF and email attachments print as blank pages after the 154 update. This went from 1 question to 38 in one month. Only 37 percent of those users got a resolution, and 21 percent got no reply at all. Rank 11, broken drag and drop of messages to the file system in 153.x, points at the same area. Both suggest a change in how Thunderbird hands file data to the operating system.

The worst-served users are in rank 7, slow mail download. Only 29 percent reach a resolution and 35 percent get no answer. Rank 9, Gmail OAuth2 sign-in failure, leaves 48 percent of askers with no reply. OAuth2 is the token-based login Google requires instead of a password. Helpers appear to lack a working diagnosis for both.

The highest-severity clusters remain connection failures. Ranks 3, 4, 5 and 6 all average above 4 out of 5 on severity, meaning users cannot send or receive mail. Rank 4, where mail retrieval stops silently until a restart, leaves 32 percent unanswered. This is an LLM-derived signal over free-text support text. Treat it as a triage pointer, not proof.

## Issues to investigate {#issues-to-investigate}

The order comes from a Python score. It weights new clusters, badly served clusters, severity and volume, in that order. Resolved means the question has an accepted solution, or a trusted contributor gave the last answer. A resolved figure under 50% is marked.

### 1. PDF/email attachments print as blank pages (154 regression) {#issue-1}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| PDF/email attachments print as blank pages (154 regression) (attachments) | 1 | 38 | ▲ +37 | 3.3 (12) | 37% (below 50%) | 21% |

- Known status: Fixed in Thunderbird 155, released 2026-09-01 (Bugzilla 2065922). The reports that arrive after that date come from users still on 154.
- Why it matters: Attachment printing went from 1 question to 38 after the 154 release, and under four in ten users got a fix.
- What to look at: Engineering must diff the 154 print and attachment rendering path, and confirm whether the blank output depends on the operating system print driver.
- Example questions: [1600414](https://support.mozilla.org/questions/1600414 "Puste strony i brak podglądu przy drukowaniu załączników PDF (Canon MF450, Windo") [1600149](https://support.mozilla.org/questions/1600149 "Thunderbird 154 PDF preview prints blank pages") [1601389](https://support.mozilla.org/questions/1601389 "Problema  con ultimo  aggiornamento") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1601306](https://support.mozilla.org/questions/1601306 "Problemi di stampa") +1

### 2. Thunderbird hangs or freezes at startup / becomes unresponsive {#issue-2}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Thunderbird hangs or freezes at startup / becomes unresponsive (performance-crash) | 18 | 36 | ▲ +18 (+100%) | 4.2 (31) | 64% | 19% |

- Why it matters: Startup hangs doubled to 36 questions and carry a 4.2 mean severity, which means the application is unusable for those users.
- What to look at: Engineering must collect startup profiles and check profile size, folder database rebuild, and add-on load order as triggers.
- Example questions: [1596317](https://support.mozilla.org/questions/1596317 "Dal 17/07 Thunderbird si avvia in background ma non mostra la finestra (funziona") [1598321](https://support.mozilla.org/questions/1598321 "encountering a message of ＂The installation seems to be incomplete.") [1601277](https://support.mozilla.org/questions/1601277 "Thundrbird va in crash all'accesso") [1601273](https://support.mozilla.org/questions/1601273 "Al iniciar Thunderbird se bloquea") [1600948](https://support.mozilla.org/questions/1600948 "Mozilla Thunderbird stopped responding") +1

### 3. Cannot send or receive at all — no server connection {#issue-3}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot send or receive at all — no server connection (send-receive) | 14 | 31 | ▲ +17 (+121%) | 4.5 (30) | 52% | 29% |

- Why it matters: Total loss of server connection more than doubled to 31 questions at the highest severity in the set, 4.5.
- What to look at: Engineering must check whether recent TLS, proxy, or connection-timeout changes shipped in 153.x and 154 explain the increase.
- Example questions: [1599683](https://support.mozilla.org/questions/1599683 "Suddenly not receiving email") [1599839](https://support.mozilla.org/questions/1599839 "Thunderbird will not connect with my server") [1599747](https://support.mozilla.org/questions/1599747 "can not get email after latest update 154.0") [1599843](https://support.mozilla.org/questions/1599843 "I've been w/o email for two days.  How can I get help?") [1599681](https://support.mozilla.org/questions/1599681 "I am unable to send and receive emails on two of my computers. I can do that onl") +1

### 4. Mail retrieval silently stops until restart (IMAP/POP polling stalls) {#issue-4}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Mail retrieval silently stops until restart (IMAP/POP polling stalls) (send-receive) | 30 | 38 | ▲ +8 (+27%) | 4.2 (34) | 55% | 32% |

- Why it matters: Mail retrieval that stops silently until restart hits 38 users and leaves 32 percent with no reply, so the failure is hard to diagnose.
- What to look at: Engineering must add visible logging or a stalled-poll indicator to the IMAP and POP polling loop so helpers can identify the stall.
- Example questions: [1599295](https://support.mozilla.org/questions/1599295 "Thunderbird stopped downloading Yahoo email") [1599738](https://support.mozilla.org/questions/1599738 "Thunderbird is not receiving in coming mail from Charter") [1601143](https://support.mozilla.org/questions/1601143 "IMAP accounts no longer update - Charter/Spectrum email hosting") [1600985](https://support.mozilla.org/questions/1600985 "Again no email using Spectrum") [1600872](https://support.mozilla.org/questions/1600872 "I can send email but can not receive.") +1

### 5. IMAP/POP login authentication failure with correct credentials {#issue-5}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| IMAP/POP login authentication failure with correct credentials (account-login) | 18 | 29 | ▲ +11 (+61%) | 4.0 (25) | 52% | 28% |

- Why it matters: Login failures with correct credentials rose to 29 questions and only half get resolved, which points at a client-side authentication bug.
- What to look at: Engineering must review the authentication method negotiation and stored credential handling for accounts that use plain IMAP and POP login.
- Example questions: [1598989](https://support.mozilla.org/questions/1598989 "Over the weekend Thuderbird stopped allowing me to send emails and will not set ") [1599070](https://support.mozilla.org/questions/1599070 "impossible to connect to my mail serveur; ask always same question about pass wo") [1596931](https://support.mozilla.org/questions/1596931 "Problemi di autenticazione server con account Gmail") [1597026](https://support.mozilla.org/questions/1597026 "Error message login to server pop.wbforme.com with username failed") [1600395](https://support.mozilla.org/questions/1600395 "Kako da popravimo grešku koja izbacuje ,,Greška sa povezivanjem na server,,") +1

### 6. Cannot send outgoing mail — SMTP connection/auth failure {#issue-6}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot send outgoing mail — SMTP connection/auth failure (send-receive) | 30 | 36 | ▲ +6 (+20%) | 4.4 (32) | 75% | 19% |

- Why it matters: SMTP send failures stay high at 36 questions and 4.4 severity, but 75 percent of users get a fix, so the playbook works.
- What to look at: Engineering must keep the existing guidance and check only whether the growth from 30 to 36 tracks a specific provider change.
- Example questions: [1599422](https://support.mozilla.org/questions/1599422 "Sending e-mails does not work") [1598639](https://support.mozilla.org/questions/1598639 "Cannot send emails") [1600308](https://support.mozilla.org/questions/1600308 "unable to send messages after upgrade") [1600281](https://support.mozilla.org/questions/1600281 "unanle to send messages") [1599511](https://support.mozilla.org/questions/1599511 "Falló el envío del mensaje. El mensaje no se ha podido enviar porque ha caducado") +1

### 7. Slow mail download / sluggish performance {#issue-7}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Slow mail download / sluggish performance (performance-crash) | 3 | 17 | ▲ +14 | 3.6 (9) | 29% (below 50%) | 35% |

- Why it matters: Slow mail download is the worst-served cluster, with 29 percent resolved and 35 percent unanswered across 17 questions.
- What to look at: Engineering must define a reproducible slow-download test and publish a diagnosis path, because helpers currently have no answer.
- Example questions: [1600636](https://support.mozilla.org/questions/1600636 "My Thunderbird has stopped working") [1599061](https://support.mozilla.org/questions/1599061 "emails home page open extremely slow, send and receive are extraordinary slow") [1600424](https://support.mozilla.org/questions/1600424 "Why so many problems with 154.0 (aarch64)?") [1596484](https://support.mozilla.org/questions/1596484 "Thunderbird not downloading gmail") [1598092](https://support.mozilla.org/questions/1598092 "Takes forever opening Thunderbird and when selecting account settings it hangs u") +1

### 8. Compose window Send button / composition toolbar missing (bug 1989214) {#issue-8}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Compose window Send button / composition toolbar missing (bug 1989214) (ui-ux) | 9 | 26 | ▲ +17 | 3.2 (9) | 88% | 4% |

- Why it matters: The missing Send button in the compose window hit 26 users, but 88 percent got a resolution and only 4 percent went unanswered.
- What to look at: Engineering must ship the fix for bug 1989214 and then let this cluster close on its own.
- Example questions: [1596605](https://support.mozilla.org/questions/1596605 "SEND button vanished after update (bug1989214)") [1598077](https://support.mozilla.org/questions/1598077 "Send, delete, forward boxes have vanished from my Thunderbird write screen (bug1") [1596407](https://support.mozilla.org/questions/1596407 "Errors in compose menu after Update to 153.0.1esr (Menus gone)") [1597318](https://support.mozilla.org/questions/1597318 "THe Send button has vanished in T'bird (bug1989214)") [1597330](https://support.mozilla.org/questions/1597330 "My ＂Send＂ button has disappeared from my Thunderbird mail client.  Is there a ke") +1

### 9. Gmail OAuth2 sign-in failures (HTTP 400 / localhost redirect / blank popup) {#issue-9}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Gmail OAuth2 sign-in failures (HTTP 400 / localhost redirect / blank popup) (sync-oauth) | 16 | 25 | ▲ +9 (+56%) | 3.5 (13) | 48% (below 50%) | 48% |

- Why it matters: Nearly half of the 25 Gmail OAuth2 questions get no reply at all, which is the highest silence rate in the set.
- What to look at: Engineering must reproduce the HTTP 400 and blank popup cases and check the localhost redirect handler against current Google policy.
- Example questions: [1599099](https://support.mozilla.org/questions/1599099 "I received a large pop up window from Google saying 'malformed' so I've lost Thu") [1600615](https://support.mozilla.org/questions/1600615 "Thunderbird start niet meer op") [1599866](https://support.mozilla.org/questions/1599866 "Sudden block of account by gmail.") [1598376](https://support.mozilla.org/questions/1598376 "＂Authentication failure＂ with Gmail Oauth login (Linux/Nixos)") [1596733](https://support.mozilla.org/questions/1596733 "Cannot setup Gmail in Thunderbird, authentication popup is empty!") +1

### 10. Stored password rejected / lost, cannot recover account password {#issue-10}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Stored password rejected / lost, cannot recover account password (account-login) | 22 | 30 | ▲ +8 (+36%) | 3.2 (14) | 63% | 13% |

- Why it matters: Rejected or lost stored passwords reached 30 questions, and 63 percent get resolved, so the pain is real but manageable.
- What to look at: Engineering must check whether the password store is losing entries on upgrade, which would link this to ranks 5 and 9.
- Example questions: [1601385](https://support.mozilla.org/questions/1601385 "Thunderbird loses passwords") [1597006](https://support.mozilla.org/questions/1597006 "Although I use the right Password I cannot get any connection to my postbox nor ") [1601104](https://support.mozilla.org/questions/1601104 "retrouver messagerie de Thunderbird car mots de passe non reconnus") [1600222](https://support.mozilla.org/questions/1600222 "E-Mail Programm meldet alle Passwörter wären falsch") [1598973](https://support.mozilla.org/questions/1598973 "Changed password on email account not working in Thunderbird") +1

### 11. Drag-and-drop of messages/attachments to filesystem broken in 153.x {#issue-11}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Drag-and-drop of messages/attachments to filesystem broken in 153.x (attachments) | 1 | 16 | ▲ +15 | 3.2 (3) | 56% | 19% |

- Why it matters: Drag and drop of messages to the file system broke in 153.x, moving from 1 question to 16.
- What to look at: Engineering must test the file drop path together with rank 1, since both involve exporting message data out of the application.
- Example questions: [1597011](https://support.mozilla.org/questions/1597011 "trascinamento fallisce con tutti i PDF") [1597120](https://support.mozilla.org/questions/1597120 "Drag-and-drop email export to Windows Explorer no longer works in Thunderbird 15") [1601351](https://support.mozilla.org/questions/1601351 "Thunderbird shuts down when I try to drag items to a different folder.") [1596881](https://support.mozilla.org/questions/1596881 "Can no longer drag and drop email attachments from emails to folders after 153es") [1596923](https://support.mozilla.org/questions/1596923 "Errore durante lo spostamento del file o della cartella") +1

### 12. Message bodies blank / headers only downloaded {#issue-12}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Message bodies blank / headers only downloaded (send-receive) | 5 | 15 | ▲ +10 | 4.1 (12) | 53% | 33% |

- Why it matters: Blank message bodies with headers only tripled to 15 questions at 4.1 severity, and a third of askers got no reply.
- What to look at: Engineering must check message body fetch and local cache invalidation for accounts set to download headers first.
- Example questions: [1600007](https://support.mozilla.org/questions/1600007 "My emails won't open, none show up in sent or delete files, it is very slow to l") [1600049](https://support.mozilla.org/questions/1600049 "8.24.2026 As of yesterday, Thunderbird Inbox messages are being received and old") [1600073](https://support.mozilla.org/questions/1600073 "Inbox email shows only sender and subject line.  Content not available,") [1601048](https://support.mozilla.org/questions/1601048 "8.29.2026 Once again I am having same problem with email content not loading. No") [1599663](https://support.mozilla.org/questions/1599663 "windows thunderbird has stopped displaying message body of my emails") +1

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

This is a prototype. Claude claude-opus-5 wrote the labels for each question, and this run of the report cost $0.55. The page covers August 2026 against July 2026. Facts the corpus cannot know, such as a shipped fix, come from `LLM_INSIGHTS/known-status.csv` and appear as Known status.

Last updated: 2026-09-10 07:25 UTC
