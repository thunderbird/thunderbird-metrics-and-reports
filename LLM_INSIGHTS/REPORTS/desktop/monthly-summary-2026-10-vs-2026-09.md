---
layout: base
title: Desktop LLM Insights — October 2026
---

# Thunderbird Desktop — LLM Insights (Engineering)

## October 2026 against September 2026

## TL;DR: the five issues to look at first {#tldr}

| # | Issue | September 2026 | October 2026 | Severity | Resolved | Known status |
|--:|:--|--:|--:|--:|--:|:--|
| [1](#issue-1) | [Attach button does nothing / file picker never opens (stale mail.compose.attach.dir, bug 2077526/2077590)](#issue-1), new this month | 0 | 169 | 4.0 | 62% | Fixed in Thunderbird 158.0.1, 159 and ESR 153.5.0 (Bugzilla [2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590), duplicate [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526)). [More](#issue-1). |
| [2](#issue-2) | [Mail problem that cannot be diagnosed without troubleshooting tools (m:gmail)](#issue-2) | 13 | 29 | 3.9 | 34% (below 50%) | A recurring problem with no fix in sight. [More](#issue-2). Reviewer: Users give too few details to diagnose. Engineering should consider self-diagnosis and repair tools, also for providers like Gmail. |
| [3](#issue-3) | [Cannot receive new mail (generic, no error)](#issue-3) | 53 | 22 | 4.2 | 27% (below 50%) | — |
| [4](#issue-4) | [AT&T inbound.att.net certificate revoked/untrusted blocking mail download (m:att)](#issue-4) | 1 | 15 | 4.2 | 87% | Fixed by AT&T. [More](#issue-4). |
| [5](#issue-5) | [Generic account setup wizard failures (hostname, ports, credentials)](#issue-5) | 39 | 28 | 3.9 | 54% | — |

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
| Spike Detector signal | A spike that the Spike Detector, a separate tool with no AI, found for a mail host, antivirus, protocol or feature tag that this issue's questions carry. |

</details>

## Headline

| | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 977 | 1030 | ▲ +53 (+5%) |
| Distinct issue clusters | 166 | 168 | ▲ +2 |
| New issue clusters this month | — | 1 | |

A new Attach button failure drove 169 reports in one month, while Outlook.com sign-in stayed the worst-served pain at 12 percent resolved.

One new problem explains almost all of this month's growth. Support questions rose from 977 to 1030. The attachments category jumped from 29 to 190. Behind that sits a single new cluster: the Attach button does nothing and the file picker never opens. It accounts for 169 questions, with an average severity of 4.0 out of 5. The suspected cause is a stale value in the mail.compose.attach.dir setting, which stores the last folder used for attachments. Bugs [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526) and [2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590) track it.

Volume is not the only signal. Two older clusters serve users badly. Microsoft and Outlook.com OAuth2 failures (OAuth2 is a sign-in method that uses tokens instead of a password) resolve only 12 percent of the time. Half of those questions get no answer at all. Generic "cannot receive new mail" reports resolve 27 percent of the time, with 41 percent unanswered. Both carry high severity. Helpers appear to lack the information needed to diagnose them.

Some areas improved. Send and receive questions fell from 233 to 160. Account and login fell from 165 to 135. The AT&T certificate problem grew but resolves at 87 percent, so helpers have a working answer. Startup hangs and broken calendar add-ons also resolve well.

This signal comes from a language model reading free-text support questions. Treat it as a triage pointer, not proof.

## Issues to investigate {#issues-to-investigate}

The order comes from a Python score. It weights new clusters, badly served clusters, severity and volume, in that order. Resolved means the question has an accepted solution, or a trusted contributor gave the last answer. A resolved figure under 50% is marked.

<a id="p1-feat-attachments"></a>

### 1. Attach button does nothing / file picker never opens (stale mail.compose.attach.dir, bug [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526)/[2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590)), new this month {#issue-1}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Attach button does nothing / file picker never opens (stale mail.compose.attach.dir, bug [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526)/[2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590)) (attachments) | 0 | 169 | ▲ +169 | 4.0 (161) | 62% | 5% |

- Known status: Fixed in Thunderbird 158.0.1, 159 and ESR 153.5.0 (Bugzilla [2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590), duplicate [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526)). Before the fix, the workaround was to reset mail.compose.attach.dir in the Config Editor. Reports peaked at 20 to 25 a day from 2026-10-06 to 2026-10-09, and only three arrived in the last two weeks of October.
- Spike Detector signal: `feat:attachments`, daily spike on 2026-10-09: 12 questions where earlier periods had none. 91 of this issue's 169 questions carry the tag. [explore ↗](../../../PROJECT1/REPORTS/desktop/explorer.html#grain=daily&cause=feat:attachments&period=2026-10-09)
- Why it matters: This cluster is new, it produced 169 questions in one month, and 161 of them scored severity 4 or higher.
- What to look at: Engineering should consider looking at how mail.compose.attach.dir is read at compose time, and adding a fallback when the stored folder no longer exists.
- Example questions: [1610213](https://support.mozilla.org/questions/1610213 "Thunderbird is onbruikbaar geworden") [1610928](https://support.mozilla.org/questions/1610928 "Attaching files no longer works in the current version of Thunderbird—what shoul") [1610829](https://support.mozilla.org/questions/1610829 "impossibile inserire allegati") [1610832](https://support.mozilla.org/questions/1610832 "No attachment possible") [1610834](https://support.mozilla.org/questions/1610834 "Keien Aänge weren geöffnet") +1

<a id="p1-m-gmail"></a>

### 2. Mail problem that cannot be diagnosed without troubleshooting tools (m:gmail) {#issue-2}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Mail problem that cannot be diagnosed without troubleshooting tools (m:gmail) (send-receive) | 13 | 29 | ▲ +16 (+123%) | 3.9 (21) | 34% (below 50%) | 28% |

- Known status: A recurring problem with no fix in sight. These users give too few details to find the cause, which can be antivirus, the network, an add-on, POP3, a Thunderbird bug or the provider. Thunderbird has no self-diagnosis or repair tools that would collect those details for them.
- Reviewer note: Roland Tanglao: There wasn't enough troubleshooting details provided by Thunderbird Desktop users to diagnose. Problem cause could have been anti-virus, network issues, add-ons, an issue specific to POP3, a Thunderbird bug, etc. Some ideas for engineering to consider: adding self diagnostic and repair facilities to Thunderbird, perhaps even specific troubleshooting features for popular providers like gmail.
- Spike Detector signal: `m:gmail`, daily spike on 2026-10-21: 11 questions against a baseline of 2.0. 29 of this issue's 29 questions carry the tag. [explore ↗](../../../PROJECT1/REPORTS/desktop/explorer.html#grain=daily&cause=m:gmail&period=2026-10-21)
- Why it matters: Gmail users report a mail problem that no one can diagnose, and only 34 percent of these questions reach a resolution.
- What to look at: Engineering should consider adding a one-click diagnostic export that captures protocol logs and account settings for Gmail accounts.
- Example questions: [1609137](https://support.mozilla.org/questions/1609137 "Accesso server smtp.gmail.com con nome utente pasquale.cristillo@gmail.com non r") [1613725](https://support.mozilla.org/questions/1613725 "da ieri Mozzilla Thunderbird non riceve più posta al mio indirizzo mail [RIMOSSO") [1613451](https://support.mozilla.org/questions/1613451 "Thunderbird is asking for a password") [1610604](https://support.mozilla.org/questions/1610604 "My gmail account has stopped synchronising with Thunderbird") [1613215](https://support.mozilla.org/questions/1613215 "Can't Receive Emails") +1

### 3. Cannot receive new mail (generic, no error) {#issue-3}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot receive new mail (generic, no error) (send-receive) | 53 | 22 | ▼ -31 (-58%) | 4.2 (19) | 27% (below 50%) | 41% |

- Why it matters: Mail simply stops arriving with no error shown, 41 percent of reports get no reply, and only 27 percent resolve.
- What to look at: Engineering should consider surfacing fetch failures in the interface instead of failing silently, so users can report an actual error code.
- Example questions: [1609063](https://support.mozilla.org/questions/1609063 "I am no longer getting emails on my thunderbird account") [1609960](https://support.mozilla.org/questions/1609960 "Get Messages button quit working") [1610435](https://support.mozilla.org/questions/1610435 "Get Messages not working in the latest version 157.1") [1610234](https://support.mozilla.org/questions/1610234 "i can't receive inbound") [1610324](https://support.mozilla.org/questions/1610324 "Emails in my inbox have disappeared on my Surface Pro.  I can still see them on ") +1

<a id="p1-m-att"></a>

### 4. AT&T inbound.att.net certificate revoked/untrusted blocking mail download (m:att) {#issue-4}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| AT&T inbound.att.net certificate revoked/untrusted blocking mail download (m:att) (encryption-security) | 1 | 15 | ▲ +14 | 4.2 (14) | 87% | 13% |

- Known status: Fixed by AT&T. DigiCert revoked the POP certificate for inbound.att.net on 2026-10-05, and some error messages called it expired. Only POP failed: IMAP and SMTP were not affected. AT&T served a new certificate from 2026-10-06, and the last certificate question arrived on 2026-10-08. Antivirus such as Norton, AVG and Avast showed the error but did not cause it. See the [incident page](https://thunderbird.github.io/thunderbird-metrics-and-reports/PROJECT1/validation/incident-att-2026-10.html) and [issue 85](https://github.com/thunderbird/thunderbird-metrics-and-reports/issues/85).
- Spike Detector signal: `m:att`, daily spike on 2026-10-06: 11 questions where earlier periods had none. 15 of this issue's 15 questions carry the tag. [explore ↗](../../../PROJECT1/REPORTS/desktop/explorer.html#grain=daily&cause=m:att&period=2026-10-06)
- Why it matters: A revoked certificate on inbound.att.net blocked mail downloads for AT&T users, though helpers resolved 87 percent of cases.
- What to look at: Engineering should consider a clearer certificate error dialog that names the server and the reason, and tracking provider certificate changes.
- Example questions: [1610297](https://support.mozilla.org/questions/1610297 "Unable to receive messages due to certificate problem") [1610321](https://support.mozilla.org/questions/1610321 "I can't recieve emails but can send the certification is revoked for inbound.att") [1610322](https://support.mozilla.org/questions/1610322 "No E-mail because of ＂The certificate for inbound.att.net:995 does not come from") [1610523](https://support.mozilla.org/questions/1610523 "Thunderbird could not connect to server inbound.att.net. The connection was refu") [1610002](https://support.mozilla.org/questions/1610002 "'Digicert Global G2' revoked Oct 5, 2026") +1

### 5. Generic account setup wizard failures (hostname, ports, credentials) {#issue-5}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Generic account setup wizard failures (hostname, ports, credentials) (account-login) | 39 | 28 | ▼ -11 (-28%) | 3.9 (22) | 54% | 25% |

- Why it matters: Setup wizard failures over hostname, ports and credentials still produce 28 questions, and a quarter get no answer.
- What to look at: Engineering should consider logging which autoconfiguration step failed and showing that step to the user in the wizard.
- Example questions: [1615005](https://support.mozilla.org/questions/1615005 "My e-mail stopped working a week ago. I get to ＂connecting to IMAP but then get ") [1608967](https://support.mozilla.org/questions/1608967 "I lost the ability to sync thunderbird to shaw rmail6") [1614795](https://support.mozilla.org/questions/1614795 "nmeldung auf dem Server secureimap.t-online.de fehlgeschlagen＂") [1610662](https://support.mozilla.org/questions/1610662 "HO INSTALLATO WINDOWS 11 non ricevo la posta mi chiede la password e non vene ac") [1614068](https://support.mozilla.org/questions/1614068 "I am unable to download my emails from Greenby") +1

### 6. Profile migration to new computer loses mail/address books {#issue-6}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Profile migration to new computer loses mail/address books (migration-import) | 35 | 31 | ▼ -4 (-11%) | 3.6 (18) | 68% | 6% |

- Why it matters: Users move to a new computer and lose mail and address books, which is unrecoverable data loss from the user point of view.
- What to look at: Engineering should consider a guided profile export and import flow that verifies the copy before the old machine is retired.
- Example questions: [1609108](https://support.mozilla.org/questions/1609108 "HELP PLEASE. Need to recover 2 yrs of emails after fresh install of Ubuntu") [1611383](https://support.mozilla.org/questions/1611383 "How can I restore missing Local Folders and emails after Thunderbird re-install?") [1612938](https://support.mozilla.org/questions/1612938 "Thunderbird update destroyed my email organization") [1612793](https://support.mozilla.org/questions/1612793 "Meine Festplatte ging kaputt. Auf der neuen Festplatte können meine in den dorti") [1609531](https://support.mozilla.org/questions/1609531 "Lost my emails on upgrade to 153.4.0 esr") +1

### 7. Junk filter not catching spam / legitimate mail marked as junk {#issue-7}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Junk filter not catching spam / legitimate mail marked as junk (spam-filters) | 8 | 19 | ▲ +11 | 2.4 (2) | 58% | 16% |

- Why it matters: Junk filter complaints more than doubled, from 8 to 19, although severity stays low at 2.4.
- What to look at: Engineering should consider checking whether a recent change reset junk training data or altered the adaptive filter thresholds.
- Example questions: [1610731](https://support.mozilla.org/questions/1610731 "Piratage de mon compte Thunderbird") [1613576](https://support.mozilla.org/questions/1613576 "Still want to see ALL messages sent my TB -- including spam / junk (the worst of") [1614990](https://support.mozilla.org/questions/1614990 "My spam has disappeared") [1614669](https://support.mozilla.org/questions/1614669 "How can I whitelist email senders using message filters?") [1614077](https://support.mozilla.org/questions/1614077 "Something is blocking one of my contacts from appearing in my firefox mail:    a") +1

<a id="p1-proto-oauth"></a>

### 8. Microsoft/Outlook.com OAuth2 authentication failures (IMAP/SMTP) {#issue-8}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Microsoft/Outlook.com OAuth2 authentication failures (IMAP/SMTP) (sync-oauth) | 16 | 16 | ▬ 0 (+0%) | 4.3 (15) | 12% (below 50%) | 50% |

- Spike Detector signal: `v158 × proto:oauth`, weekly spike in the week of 2026-10-26: 5 questions, 7.0 times the expected 0.7. 9 of this issue's 16 questions carry the tag. [explore ↗](../../../PROJECT1/REPORTS/desktop/explorer.html#grain=weekly&version=158&cause=proto:oauth&period=2026-10-26)
- Why it matters: This is the worst-served cluster in the data, with 12 percent resolved, 50 percent unanswered and severity 4.3.
- What to look at: Engineering should consider reproducing Outlook.com OAuth2 token refresh against current Microsoft endpoints and publishing a known-good configuration.
- Example questions: [1612144](https://support.mozilla.org/questions/1612144 "Popup non si aprono dopo aggiornamento windows di 2gg fa, non si riesce ad utili") [1612885](https://support.mozilla.org/questions/1612885 "Thunderbird 158 fails OAuth2 authentication when adding a new Outlook.com accoun") [1613480](https://support.mozilla.org/questions/1613480 "Thunderbird IMAP (OAuth 2.0) - Microsoft Hesaplarında ＂User is authenticated but") [1614222](https://support.mozilla.org/questions/1614222 "Outlook.de receives mail but cannot send with OAuth2: “SmtpClientAuthentication ") [1614513](https://support.mozilla.org/questions/1614513 "Thunderbird 158.1 receives emails from my new Outlook.com account but cannot sen") +1

### 9. Thunderbird hangs/freezes at startup (session.json, loading messages, profile lock) {#issue-9}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Thunderbird hangs/freezes at startup (session.json, loading messages, profile lock) (performance-crash) | 30 | 25 | ▼ -5 (-17%) | 4.2 (21) | 80% | 8% |

- Why it matters: Startup hangs tied to session.json, message loading and profile locks remain high severity but resolve at 80 percent.
- What to look at: Engineering should consider making a corrupt session.json recoverable at startup rather than requiring manual file deletion.
- Example questions: [1612463](https://support.mozilla.org/questions/1612463 "Unable to load Thunderbird") [1612917](https://support.mozilla.org/questions/1612917 "After the update to version 158  it opens and shortly afterwards freezes.") [1610394](https://support.mozilla.org/questions/1610394 "Thunderbird fails to start after update on Ubuntu") [1614055](https://support.mozilla.org/questions/1614055 "Hello, ik heb problemen met thunderbird op windows 11 . Bij het opstarten krijg ") [1613838](https://support.mozilla.org/questions/1613838 "Thunderbird non risponde dopo l'installazione") +1

<a id="p1-feat-calendar"></a>

### 10. Calendar add-ons (CardBook, Provider for Google Calendar, TbSync) broken by TB updates {#issue-10}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Calendar add-ons (CardBook, Provider for Google Calendar, TbSync) broken by TB updates (addons-extensions) | 5 | 14 | ▲ +9 | 3.6 (10) | 86% | 0% |

- Spike Detector signal: `v159 × feat:calendar`, weekly spike in the week of 2026-10-26: 10 questions, 5.2 times the expected 1.9. 7 of this issue's 14 questions carry the tag. [explore ↗](../../../PROJECT1/REPORTS/desktop/explorer.html#grain=weekly&version=159&cause=feat:calendar&period=2026-10-26)
- Why it matters: CardBook, Provider for Google Calendar and TbSync broke after Thunderbird updates, nearly tripling reports from 5 to 14.
- What to look at: Engineering should consider testing these three add-ons against release candidates and warning users before an update disables them.
- Example questions: [1610169](https://support.mozilla.org/questions/1610169 "Calendari disattivati") [1608944](https://support.mozilla.org/questions/1608944 "Thunderbird 157 breaks google calendar add-on") [1608983](https://support.mozilla.org/questions/1608983 "Google Calendar & Tasks suddenly fail in Thunderbird 157 64bit") [1609292](https://support.mozilla.org/questions/1609292 "thunderbird 157 update deactivated all my calendars") [1614739](https://support.mozilla.org/questions/1614739 "PLEASE STOP RELEASING UNTESTED UPDATES") +1

### 11. Out-of-office, return receipts and reply prefix configuration {#issue-11}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Out-of-office, return receipts and reply prefix configuration (ui-ux) | 16 | 23 | ▲ +7 (+44%) | 2.2 (1) | 70% | 22% |

- Why it matters: Questions about out-of-office replies, return receipts and reply prefixes grew to 23, and 22 percent get no answer.
- What to look at: Engineering should consider whether these settings are hard to find, and grouping them in one place in the settings interface.
- Example questions: [1613475](https://support.mozilla.org/questions/1613475 "my emails won't open") [1608951](https://support.mozilla.org/questions/1608951 "default actions http/s not working unless use open in Browser as a link..") [1609795](https://support.mozilla.org/questions/1609795 "Thunderbird  send copy to a folder") [1614685](https://support.mozilla.org/questions/1614685 "Beérkezett üzenetre kattintva nem az üzenet nyílik meg egy új ablakban, hanem eg") [1610415](https://support.mozilla.org/questions/1610415 "Annoying unsilencable dialogs for internet connection problems") +1

### 12. Folders missing/disappeared from folder pane after update {#issue-12}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Folders missing/disappeared from folder pane after update (search-folders) | 13 | 14 | ▲ +1 (+8%) | 4.4 (12) | 43% (below 50%) | 29% |

- Why it matters: Folders vanish from the folder pane after an update, severity averages 4.4, and only 43 percent of reports resolve.
- What to look at: Engineering should consider checking whether update-time folder database rebuilds drop subscriptions or orphan local folder entries.
- Example questions: [1609211](https://support.mozilla.org/questions/1609211 "Пропажа отправленных сообщений") [1609927](https://support.mozilla.org/questions/1609927 "i have lost all my emails") [1610432](https://support.mozilla.org/questions/1610432 "Disparition de sous-dossiers (.sbd) après un glisser-déposer vers un compte IMAP") [1611881](https://support.mozilla.org/questions/1611881 "FOLDERS in my thunderbox email have disappeared how do i recover them") [1611890](https://support.mozilla.org/questions/1611890 "Loss of all my filed emails") +1

## Seen by one side only {#seen-by-one-side-only}

The Spike Detector is a separate tool with no AI. It flags a spike when a mail host, antivirus, protocol or feature tag rises well above its usual level. Where a spike and an issue on this page share questions, the issue carries a Spike Detector signal line. The [Spike Detector executive summary for October 2026](../../../PROJECT1/REPORTS/desktop/2026-10-exec-summary.html) has the numbers.

Spikes from the Spike Detector that have no issue on this page. Their questions are too few, or they spread over clusters below the featured list:

- `m:shaw`, weekly spike in the week of 2026-09-28: 9 questions against a baseline of 0.5
- `v158 × proto:pop`, daily spike on 2026-10-24: 4 questions, 7.8 times the expected 0.5
- `v158 × m:thundermail`, monthly spike in October 2026: 5 questions, 7.8 times the expected 0.6
- `v158 × feat:addressbook`, weekly spike in the week of 2026-10-12: 6 questions, 5.8 times the expected 1.0
- `v156 × feat:import_export`, weekly spike in the week of 2026-09-28: 5 questions, 3.1 times the expected 1.6

Issues with 10 or more questions and no Spike Detector spike. No spiking tag covers a quarter of their questions, so the Spike Detector does not flag them:

- [Issue 3](#issue-3), Cannot receive new mail (generic, no error), 22 questions
- [Issue 5](#issue-5), Generic account setup wizard failures (hostname, ports, credentials), 28 questions
- [Issue 6](#issue-6), Profile migration to new computer loses mail/address books, 31 questions
- [Issue 7](#issue-7), Junk filter not catching spam / legitimate mail marked as junk, 19 questions
- [Issue 9](#issue-9), Thunderbird hangs/freezes at startup (session.json, loading messages, profile lock), 25 questions
- [Issue 11](#issue-11), Out-of-office, return receipts and reply prefix configuration, 23 questions
- [Issue 12](#issue-12), Folders missing/disappeared from folder pane after update, 14 questions

## Category mix, month over month

| Category | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| attachments | 29 | 190 | ▲ +161 (+555%) |
| send-receive | 233 | 160 | ▼ -73 (-31%) |
| account-login | 165 | 135 | ▼ -30 (-18%) |
| ui-ux | 92 | 111 | ▲ +19 (+21%) |
| settings-config | 91 | 70 | ▼ -21 (-23%) |
| search-folders | 50 | 55 | ▲ +5 (+10%) |
| other | 50 | 54 | ▲ +4 (+8%) |
| sync-oauth | 51 | 50 | ▼ -1 (-2%) |
| performance-crash | 54 | 46 | ▼ -8 (-15%) |
| migration-import | 56 | 43 | ▼ -13 (-23%) |
| calendar-tasks | 22 | 37 | ▲ +15 (+68%) |
| encryption-security | 25 | 31 | ▲ +6 (+24%) |
| spam-filters | 39 | 28 | ▼ -11 (-28%) |
| addons-extensions | 20 | 20 | ▬ 0 (+0%) |

---

This is a prototype. Claude claude-opus-5 wrote the labels for each question, and this run reused the cached LLM output and cost $0.00 (the full cost is in `LLM_INSIGHTS/COSTS.md`). The page covers October 2026 against September 2026. Facts the corpus cannot know, such as a shipped fix, come from `LLM_INSIGHTS/known-status.csv` and appear as Known status.

Last updated: 2026-11-03 18:22 UTC
