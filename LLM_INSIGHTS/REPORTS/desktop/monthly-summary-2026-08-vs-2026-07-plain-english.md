---
layout: base
title: Desktop LLM Insights — August 2026
---

# Thunderbird Desktop — LLM Insights (Engineering)

## August 2026 against July 2026

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
| Distinct issue clusters | 87 | 98 | ▲ +11 |
| New issue clusters this month | — | 0 | |

Attachment printing and Spectrum mail stalls jumped from near zero to 75 reports, and startup crashes doubled.

Support volume rose from 731 questions in July to 940 in August. Three problems drove most of the jump. Attachments that print as blank pages went from 2 reports to 39. Spectrum, Charter and Roadrunner mail that stops downloading went from 2 to 36. Startup hangs and crashes went from 18 to 41. The attachments category more than tripled, and performance-crash more than doubled.

Engineering must treat the blank-page printing reports as a probable regression in the 153 and 154 releases. Only 38 percent of those users got a resolution. The Spectrum family of reports looks like a provider-side change in connection or TLS handling that Thunderbird handles badly. Mean severity there is 4.4 out of 5, so users lose mail access completely.

The worst-served group is Microsoft and Office 365 OAuth login failures. OAuth is the token-based sign-in flow used instead of a password. Only 29 percent of those reports resolved, and 53 percent got no reply at all. Volume is small at 17, but the pain per user is high and nobody is answering.

These numbers come from a language model reading free-text support questions. Treat them as a triage pointer, not as proof of a defect.

## Issues to investigate

The order comes from a Python score. It weights new clusters, badly served clusters, severity and volume, in that order. Resolved means the question has an accepted solution, or a trusted contributor gave the last answer. A resolved figure under 50% is marked.

### 1. PDF/email attachments print as blank pages

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| PDF/email attachments print as blank pages (attachments) | 2 | 39 | ▲ +37 | 3.3 (12) | 38% (below 50%) | 21% |

- Why it matters: Blank-page printing grew from 2 reports to 39 in one month, and only 38 percent of users got a fix.
- What to look at: Engineering must test printing of PDF and inline attachments on the 153 and 154 builds and check the print path in the PDF viewer.
- Example questions: [1601404](https://support.mozilla.org/questions/1601404 "can not print email attachments") [1600392](https://support.mozilla.org/questions/1600392 "Printing from Thunderbird since version 154.0 on Windows 11 produces only blank ") [1601389](https://support.mozilla.org/questions/1601389 "Problema  con ultimo  aggiornamento") [1601387](https://support.mozilla.org/questions/1601387 "problemi con la stampa degli allegati della posta, stampa e salva tutto bianco,p") [1599285](https://support.mozilla.org/questions/1599285 "PDF attachments now blank when printed.  Worked great til today.") +1

### 2. Spectrum/Charter/Roadrunner IMAP/POP mail stops downloading or times out

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Spectrum/Charter/Roadrunner IMAP/POP mail stops downloading or times out (send-receive) | 2 | 36 | ▲ +34 | 4.4 (35) | 61% | 17% |

- Why it matters: Spectrum, Charter and Roadrunner mail stalls jumped from 2 to 36 reports with mean severity 4.4, so users lose all incoming mail.
- What to look at: Engineering must capture IMAP and POP logs from these accounts and review connection limits, idle timeouts and TLS negotiation against the provider.
- Example questions: [1599683](https://support.mozilla.org/questions/1599683 "Suddenly not receiving email") [1599681](https://support.mozilla.org/questions/1599681 "I am unable to send and receive emails on two of my computers. I can do that onl") [1600103](https://support.mozilla.org/questions/1600103 "Cannot send or receive email. (locked duplicate)") [1600872](https://support.mozilla.org/questions/1600872 "I can send email but can not receive.") [1600000](https://support.mozilla.org/questions/1600000 "Suddenly can't send/receive emails") +1

### 3. Thunderbird hangs/freezes or crashes at startup

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Thunderbird hangs/freezes or crashes at startup (performance-crash) | 18 | 41 | ▲ +23 (+128%) | 4.3 (38) | 56% | 27% |

- Why it matters: Startup hangs and crashes more than doubled to 41 reports, and 27 percent of those users got no reply.
- What to look at: Engineering must pull crash and hang stacks from the 153 and 154 releases and check profile database loading and add-on startup work.
- Example questions: [1596317](https://support.mozilla.org/questions/1596317 "Dal 17/07 Thunderbird si avvia in background ma non mostra la finestra (funziona") [1598340](https://support.mozilla.org/questions/1598340 "I was deleting old emails a few days ago and my email froze. It hasn’t responded") [1601279](https://support.mozilla.org/questions/1601279 "Thunderbird va in crasi alla connessione") [1601277](https://support.mozilla.org/questions/1601277 "Thundrbird va in crash all'accesso") [1601273](https://support.mozilla.org/questions/1601273 "Al iniciar Thunderbird se bloquea") +1

### 4. IMAP/POP mail silently stops downloading until restart

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| IMAP/POP mail silently stops downloading until restart (send-receive) | 27 | 34 | ▲ +7 (+26%) | 4.1 (29) | 47% (below 50%) | 41% |

- Why it matters: Mail silently stops downloading until restart in 34 reports, and 41 percent of those questions went unanswered.
- What to look at: Engineering must look at IMAP connection recovery after a dropped socket and add a visible error when a folder stops polling.
- Example questions: [1601356](https://support.mozilla.org/questions/1601356 "I have not received any emails for 2-3 days???") [1600778](https://support.mozilla.org/questions/1600778 "I can not down load Emails from Yahoo to Thunderbird  tired all listed solutions") [1600220](https://support.mozilla.org/questions/1600220 "Emails won’t show from 2024") [1600092](https://support.mozilla.org/questions/1600092 "Folders Enumerate but do not populate") [1598049](https://support.mozilla.org/questions/1598049 "After update 153.0.3 I can't receive emails but I can send them.") +1

### 5. Cannot send or receive at all / connection refused to mail server

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot send or receive at all / connection refused to mail server (send-receive) | 13 | 25 | ▲ +12 (+92%) | 4.4 (22) | 56% | 24% |

- Why it matters: Complete send and receive failure with connection refused doubled to 25 reports at mean severity 4.4.
- What to look at: Engineering must check whether these accounts share a port, TLS setting or provider with the Spectrum cluster in rank 2.
- Example questions: [1599843](https://support.mozilla.org/questions/1599843 "I've been w/o email for two days.  How can I get help?") [1597006](https://support.mozilla.org/questions/1597006 "Although I use the right Password I cannot get any connection to my postbox nor ") [1601287](https://support.mozilla.org/questions/1601287 "Buongiorno, non riesco ad inviare e ricevere mail") [1601282](https://support.mozilla.org/questions/1601282 "Na installatie nwe versie komt er geen mail meer binnen en kan ik geen mail verz") [1598269](https://support.mozilla.org/questions/1598269 "IMAP/SMTP server connected, but receives and send fails") +1

### 6. Password rejected / cannot log in with correct credentials

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Password rejected / cannot log in with correct credentials (account-login) | 25 | 31 | ▲ +6 (+24%) | 3.9 (25) | 58% | 29% |

- Why it matters: Thirty-one users report rejected passwords that they know are correct, which points at stored credential handling rather than user error.
- What to look at: Engineering must review password manager reads and token fallback when a server switches from basic authentication to OAuth.
- Example questions: [1597026](https://support.mozilla.org/questions/1597026 "Error message login to server pop.wbforme.com with username failed") [1601104](https://support.mozilla.org/questions/1601104 "retrouver messagerie de Thunderbird car mots de passe non reconnus") [1600222](https://support.mozilla.org/questions/1600222 "E-Mail Programm meldet alle Passwörter wären falsch") [1599070](https://support.mozilla.org/questions/1599070 "impossible to connect to my mail serveur; ask always same question about pass wo") [1599264](https://support.mozilla.org/questions/1599264 "this last update completely broke my emails") +1

### 7. Send button / composition toolbar missing in compose window

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Send button / composition toolbar missing in compose window (ui-ux) | 10 | 27 | ▲ +17 (+170%) | 3.1 (9) | 89% | 4% |

- Why it matters: The missing Send button grew from 10 to 27 reports, though support resolves 89 percent of them.
- What to look at: Engineering must find the toolbar state that hides compose controls after update and reset it automatically instead of relying on support advice.
- Example questions: [1596605](https://support.mozilla.org/questions/1596605 "SEND button vanished after update (bug1989214)") [1598077](https://support.mozilla.org/questions/1598077 "Send, delete, forward boxes have vanished from my Thunderbird write screen (bug1") [1596407](https://support.mozilla.org/questions/1596407 "Errors in compose menu after Update to 153.0.1esr (Menus gone)") [1597318](https://support.mozilla.org/questions/1597318 "THe Send button has vanished in T'bird (bug1989214)") [1597330](https://support.mozilla.org/questions/1597330 "My ＂Send＂ button has disappeared from my Thunderbird mail client.  Is there a ke") +1

### 8. UI elements missing after 153/154 update (toolbars, menus, panes)

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| UI elements missing after 153/154 update (toolbars, menus, panes) (ui-ux) | 33 | 44 | ▲ +11 (+33%) | 2.2 (1) | 66% | 14% |

- Why it matters: Missing toolbars and panes after the 153 and 154 update remain the largest single cluster at 44 reports, but severity is low at 2.2.
- What to look at: Engineering must confirm the upgrade path preserves toolbar and pane layout, since this is a repeat of a known update side effect.
- Example questions: [1600361](https://support.mozilla.org/questions/1600361 "thinderbird mail tabs blank, show an X on tab, no content.") [1597229](https://support.mozilla.org/questions/1597229 "Thunderbird, versão 153.0esr: Problema com as Pastas favoritas") [1597563](https://support.mozilla.org/questions/1597563 "today I have a FREDOM pop up from thunderbird and now cannot access any mail") [1600623](https://support.mozilla.org/questions/1600623 "v140.13.0esr on Linux Debian 11: impossible to resize windows") [1596413](https://support.mozilla.org/questions/1596413 "The 'Customise Menu＂ function does nothing in v153.0.1 (64-bit)") +1

### 9. Slow performance: sluggish mail loading, sync, memory leaks

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Slow performance: sluggish mail loading, sync, memory leaks (performance-crash) | 7 | 19 | ▲ +12 | 3.4 (8) | 37% (below 50%) | 37% |

- Why it matters: Slow loading and memory growth grew to 19 reports with only 37 percent resolved and 37 percent unanswered.
- What to look at: Engineering must profile memory use over long sessions and check message list rendering on large folders.
- Example questions: [1600636](https://support.mozilla.org/questions/1600636 "My Thunderbird has stopped working") [1599061](https://support.mozilla.org/questions/1599061 "emails home page open extremely slow, send and receive are extraordinary slow") [1596484](https://support.mozilla.org/questions/1596484 "Thunderbird not downloading gmail") [1598092](https://support.mozilla.org/questions/1598092 "Takes forever opening Thunderbird and when selecting account settings it hangs u") [1598432](https://support.mozilla.org/questions/1598432 "Thunderbird High CPU with status bar on") +1

### 10. Profile migration to new computer loses mail/accounts

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Profile migration to new computer loses mail/accounts (migration-import) | 50 | 44 | ▼ -6 (-12%) | 3.4 (20) | 73% | 7% |

- Why it matters: Profile migration losses fell from 50 to 44 reports and support resolves 73 percent, so this is handled load rather than a new problem.
- What to look at: Engineering must keep the current guidance and consider a built-in profile move tool to cut the volume.
- Example questions: [1598972](https://support.mozilla.org/questions/1598972 "updated to 153.0.3 and no folders.") [1597960](https://support.mozilla.org/questions/1597960 "where are all my emails, sent emails and deleted emails? My last PC died and aft") [1597907](https://support.mozilla.org/questions/1597907 "Lost sub folders") [1597858](https://support.mozilla.org/questions/1597858 "After updateing to a new version of Thunderbird my old profile has disappeared") [1599476](https://support.mozilla.org/questions/1599476 "if i download an older version of thunderbird, will i loose all my current email") +1

### 11. Microsoft/Outlook/Office365 OAuth login and authentication failures

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Microsoft/Outlook/Office365 OAuth login and authentication failures (sync-oauth) | 8 | 17 | ▲ +9 | 4.1 (14) | 29% (below 50%) | 53% |

- Why it matters: Microsoft OAuth failures resolve for only 29 percent of users and 53 percent get no answer, the worst result in the set.
- What to look at: Engineering must reproduce Office 365 token refresh and tenant consent failures and return an error message that names the actual cause.
- Example questions: [1598006](https://support.mozilla.org/questions/1598006 "Hotmail authenticator error") [1598566](https://support.mozilla.org/questions/1598566 "Cant get hotmail to work on thunderbird linux ubuntu") [1597324](https://support.mozilla.org/questions/1597324 "No sync on exchange email account after updating to v153") [1598437](https://support.mozilla.org/questions/1598437 "Unable to Connect MS- Email") [1596314](https://support.mozilla.org/questions/1596314 "Unable to add a personal Outlook email to Thunderbird") +1

### 12. SMTP send fails / timeouts while receiving works

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| SMTP send fails / timeouts while receiving works (send-receive) | 33 | 29 | ▼ -4 (-12%) | 4.6 (28) | 66% | 21% |

- Why it matters: SMTP send failures fell slightly to 29 reports but carry the highest mean severity at 4.6, so affected users cannot send mail.
- What to look at: Engineering must review send timeout values and retry behaviour when the outgoing server accepts the connection but stalls.
- Example questions: [1599327](https://support.mozilla.org/questions/1599327 "＂Sending of the message failed. The message could not be sent because the connec") [1598759](https://support.mozilla.org/questions/1598759 "Unable to send email from Thunderbird after Network Solutions changed SMTP serve") [1600308](https://support.mozilla.org/questions/1600308 "unable to send messages after upgrade") [1600281](https://support.mozilla.org/questions/1600281 "unanle to send messages") [1600197](https://support.mozilla.org/questions/1600197 "Email msgs not received") +1

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

This is a prototype. Claude claude-opus-5 wrote the labels for each question, and this run of the report cost $0.64. The page covers August 2026 against July 2026. The same month is also published in the original format, for comparison.

Last updated: 2026-09-10 07:11 UTC
