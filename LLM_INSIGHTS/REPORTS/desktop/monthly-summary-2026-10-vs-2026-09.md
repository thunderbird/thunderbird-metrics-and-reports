---
layout: base
title: Desktop LLM Insights — October 2026
---

# Thunderbird Desktop — LLM Insights (Engineering)

## October 2026 against September 2026

## TL;DR: the five issues to look at first {#tldr}

| # | Issue | September 2026 | October 2026 | Severity | Resolved | Known status |
|--:|:--|--:|--:|--:|--:|:--|
| [1](#issue-1) | [Attach button does nothing / file picker never opens (stale mail.compose.attach.dir, bug 2077526/2077590)](#issue-1), new this month | 0 | 169 | 4.0 | 62% | Fixed in Thunderbird 158.0.1, 159 and ESR 153.5.0 (Bugzilla [2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590), duplicate [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526)). Before the fix, the workaround was to reset mail.compose.attach.dir in the Config Editor. Reports peaked at 20 to 25 a day from 2026-10-06 to 2026-10-09, and only three arrived in the last two weeks of October. |
| [2](#issue-2) | [Cannot receive new mail (generic, no error)](#issue-2) | 55 | 24 | 4.2 | 25% (below 50%) | — |
| [3](#issue-3) | [Gmail mail not downloading / Inbox empty while All Mail has messages (m:gmail)](#issue-3) | 6 | 16 | 3.9 | 31% (below 50%) | — |
| [4](#issue-4) | [Microsoft/Outlook.com OAuth2 authentication failures (IMAP/SMTP)](#issue-4) | 23 | 21 | 4.2 | 14% (below 50%) | — |
| [5](#issue-5) | [AT&T inbound.att.net certificate revoked/untrusted blocking mail download (m:att)](#issue-5) | 1 | 15 | 4.2 | 87% | — |

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

| | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 977 | 1030 | ▲ +53 (+5%) |
| Distinct issue clusters | 167 | 174 | ▲ +7 |
| New issue clusters this month | — | 1 | |

A new attachment bug drove 169 reports in October, while Microsoft OAuth2 failures stay the worst-served pain at 14 percent resolved.

Engineering should consider looking at two things this month. First, a brand new cluster: the Attach button does nothing and the file picker never opens. It went from zero reports in September to 169 in October. Users link it to a stale `mail.compose.attach.dir` value, tracked in bugs [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526) and [2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590). Average severity is 4.0 and 161 reports sit at severity 4 or higher. This single cluster lifted the attachments category from 29 to 190 reports.

Second, the worst-served pain is Microsoft and Outlook.com OAuth2 login failures. OAuth2 is the token-based sign-in flow that replaced passwords. Only 14 percent of those reports reach a resolution. 57 percent get no reply at all. The volume is flat at 21 reports, so this is a quality problem, not a growth problem. Generic "cannot receive new mail" reports are the second worst served at 25 percent resolved and 38 percent unanswered.

Total volume rose from 977 to 1030 questions. Send and receive dropped from 233 to 160. Two provider-specific clusters grew: Gmail Inbox staying empty while All Mail holds messages, and a revoked AT&T certificate on inbound.att.net. Support answers the AT&T case well at 87 percent resolved, so that one needs a documented workaround more than code.

These clusters come from a language model reading free-text support questions. Treat the numbers as a triage pointer, not as bug confirmation.

## Issues to investigate {#issues-to-investigate}

The order comes from a Python score. It weights new clusters, badly served clusters, severity and volume, in that order. Resolved means the question has an accepted solution, or a trusted contributor gave the last answer. A resolved figure under 50% is marked.

### 1. Attach button does nothing / file picker never opens (stale mail.compose.attach.dir, bug [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526)/[2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590)), new this month {#issue-1}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Attach button does nothing / file picker never opens (stale mail.compose.attach.dir, bug [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526)/[2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590)) (attachments) | 0 | 169 | ▲ +169 | 4.0 (161) | 62% | 5% |

- Known status: Fixed in Thunderbird 158.0.1, 159 and ESR 153.5.0 (Bugzilla [2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590), duplicate [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526)). Before the fix, the workaround was to reset mail.compose.attach.dir in the Config Editor. Reports peaked at 20 to 25 a day from 2026-10-06 to 2026-10-09, and only three arrived in the last two weeks of October.
- Why it matters: Rank 1 is new this month and went from 0 to 169 reports, with 161 at severity 4 or higher, so composing mail with files is broken for many users.
- What to look at: Engineering should consider confirming whether a stale or invalid `mail.compose.attach.dir` path blocks the file picker, and ship a fallback that ignores unreachable directories, per bugs [2077526](https://bugzilla.mozilla.org/show_bug.cgi?id=2077526) and [2077590](https://bugzilla.mozilla.org/show_bug.cgi?id=2077590).
- Example questions: [1610213](https://support.mozilla.org/questions/1610213 "Thunderbird is onbruikbaar geworden") [1610928](https://support.mozilla.org/questions/1610928 "Attaching files no longer works in the current version of Thunderbird—what shoul") [1610829](https://support.mozilla.org/questions/1610829 "impossibile inserire allegati") [1610832](https://support.mozilla.org/questions/1610832 "No attachment possible") [1610834](https://support.mozilla.org/questions/1610834 "Keien Aänge weren geöffnet") +1

### 2. Cannot receive new mail (generic, no error) {#issue-2}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot receive new mail (generic, no error) (send-receive) | 55 | 24 | ▼ -31 (-56%) | 4.2 (21) | 25% (below 50%) | 38% |

- Why it matters: Rank 2 reports give no error text, only 25 percent reach a resolution and 38 percent get no reply, so users hit a dead end.
- What to look at: Engineering should consider adding a visible, specific failure reason when a mail fetch returns nothing, so helpers can tell a server timeout from an auth failure.
- Example questions: [1609063](https://support.mozilla.org/questions/1609063 "I am no longer getting emails on my thunderbird account") [1609609](https://support.mozilla.org/questions/1609609 "Non scarica la posta dopo aggiornamento") [1610435](https://support.mozilla.org/questions/1610435 "Get Messages not working in the latest version 157.1") [1610234](https://support.mozilla.org/questions/1610234 "i can't receive inbound") [1609960](https://support.mozilla.org/questions/1609960 "Get Messages button quit working") +1

### 3. Gmail mail not downloading / Inbox empty while All Mail has messages (m:gmail) {#issue-3}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Gmail mail not downloading / Inbox empty while All Mail has messages (m:gmail) (send-receive) | 6 | 16 | ▲ +10 | 3.9 (12) | 31% (below 50%) | 25% |

- Why it matters: Rank 3 nearly tripled to 16 reports and only 31 percent resolve, which points at Gmail IMAP folder mapping rather than user error.
- What to look at: Engineering should consider testing how Thunderbird maps Gmail labels and the All Mail folder to a local Inbox after account setup and after upgrades.
- Example questions: [1610604](https://support.mozilla.org/questions/1610604 "My gmail account has stopped synchronising with Thunderbird") [1612765](https://support.mozilla.org/questions/1612765 "Non ricevo le mail da gmail") [1613215](https://support.mozilla.org/questions/1613215 "Can't Receive Emails") [1613725](https://support.mozilla.org/questions/1613725 "da ieri Mozzilla Thunderbird non riceve più posta al mio indirizzo mail [RIMOSSO") [1609176](https://support.mozilla.org/questions/1609176 "multiple problems with thunderbird handling gmail accounts") +1

### 4. Microsoft/Outlook.com OAuth2 authentication failures (IMAP/SMTP) {#issue-4}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Microsoft/Outlook.com OAuth2 authentication failures (IMAP/SMTP) (sync-oauth) | 23 | 21 | ▼ -2 (-9%) | 4.2 (19) | 14% (below 50%) | 57% |

- Why it matters: Rank 4 has the worst service in the whole set at 14 percent resolved and 57 percent unanswered, with severity 4.2.
- What to look at: Engineering should consider capturing and logging the exact Microsoft token error codes and publishing a decision tree so support can answer these at all.
- Example questions: [1613480](https://support.mozilla.org/questions/1613480 "Thunderbird IMAP (OAuth 2.0) - Microsoft Hesaplarında ＂User is authenticated but") [1614875](https://support.mozilla.org/questions/1614875 "Thunderbird says ＂login failed＂ when trying to send an email") [1614513](https://support.mozilla.org/questions/1614513 "Thunderbird 158.1 receives emails from my new Outlook.com account but cannot sen") [1614222](https://support.mozilla.org/questions/1614222 "Outlook.de receives mail but cannot send with OAuth2: “SmtpClientAuthentication ") [1612144](https://support.mozilla.org/questions/1612144 "Popup non si aprono dopo aggiornamento windows di 2gg fa, non si riesce ad utili") +1

### 5. AT&T inbound.att.net certificate revoked/untrusted blocking mail download (m:att) {#issue-5}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| AT&T inbound.att.net certificate revoked/untrusted blocking mail download (m:att) (encryption-security) | 1 | 15 | ▲ +14 | 4.2 (14) | 87% | 13% |

- Why it matters: Rank 5 grew from 1 to 15 reports because AT&T served a revoked or untrusted certificate, which stops mail download outright.
- What to look at: Engineering should consider checking how Thunderbird presents a revoked server certificate and making the dialog name the provider and the safe next step.
- Example questions: [1610297](https://support.mozilla.org/questions/1610297 "Unable to receive messages due to certificate problem") [1610321](https://support.mozilla.org/questions/1610321 "I can't recieve emails but can send the certification is revoked for inbound.att") [1610322](https://support.mozilla.org/questions/1610322 "No E-mail because of ＂The certificate for inbound.att.net:995 does not come from") [1610523](https://support.mozilla.org/questions/1610523 "Thunderbird could not connect to server inbound.att.net. The connection was refu") [1610002](https://support.mozilla.org/questions/1610002 "'Digicert Global G2' revoked Oct 5, 2026") +1

### 6. Generic account setup wizard failures (hostname, ports, credentials) {#issue-6}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Generic account setup wizard failures (hostname, ports, credentials) (account-login) | 41 | 28 | ▼ -13 (-32%) | 3.9 (22) | 54% | 25% |

- Why it matters: Rank 6 fell to 28 reports but still leaves 25 percent of askers with no reply, so wizard autoconfiguration keeps failing silently.
- What to look at: Engineering should consider reviewing which hostname and port guesses the setup wizard tries, and showing the attempted values when every guess fails.
- Example questions: [1615005](https://support.mozilla.org/questions/1615005 "My e-mail stopped working a week ago. I get to ＂connecting to IMAP but then get ") [1608967](https://support.mozilla.org/questions/1608967 "I lost the ability to sync thunderbird to shaw rmail6") [1614795](https://support.mozilla.org/questions/1614795 "nmeldung auf dem Server secureimap.t-online.de fehlgeschlagen＂") [1610662](https://support.mozilla.org/questions/1610662 "HO INSTALLATO WINDOWS 11 non ricevo la posta mi chiede la password e non vene ac") [1614068](https://support.mozilla.org/questions/1614068 "I am unable to download my emails from Greenby") +1

### 7. Profile migration to new computer loses mail/address books {#issue-7}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Profile migration to new computer loses mail/address books (migration-import) | 35 | 31 | ▼ -4 (-11%) | 3.6 (18) | 68% | 6% |

- Why it matters: Rank 7 holds steady at 31 reports and resolves at 68 percent, so this is a known, answerable problem rather than a regression.
- What to look at: Engineering should consider reducing the manual steps in moving a profile folder between computers, since the volume persists month after month.
- Example questions: [1609108](https://support.mozilla.org/questions/1609108 "HELP PLEASE. Need to recover 2 yrs of emails after fresh install of Ubuntu") [1611383](https://support.mozilla.org/questions/1611383 "How can I restore missing Local Folders and emails after Thunderbird re-install?") [1612938](https://support.mozilla.org/questions/1612938 "Thunderbird update destroyed my email organization") [1612793](https://support.mozilla.org/questions/1612793 "Meine Festplatte ging kaputt. Auf der neuen Festplatte können meine in den dorti") [1609531](https://support.mozilla.org/questions/1609531 "Lost my emails on upgrade to 153.4.0 esr") +1

### 8. Junk filter not catching spam / legitimate mail marked as junk {#issue-8}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Junk filter not catching spam / legitimate mail marked as junk (spam-filters) | 8 | 19 | ▲ +11 | 2.4 (2) | 58% | 16% |

- Why it matters: Rank 8 more than doubled to 19 reports but sits at mean severity 2.4, so the pain is annoyance, not blockage.
- What to look at: Engineering should consider checking whether the adaptive junk filter training data survives recent upgrades before spending more effort here.
- Example questions: [1610731](https://support.mozilla.org/questions/1610731 "Piratage de mon compte Thunderbird") [1613576](https://support.mozilla.org/questions/1613576 "Still want to see ALL messages sent my TB -- including spam / junk (the worst of") [1614990](https://support.mozilla.org/questions/1614990 "My spam has disappeared") [1614669](https://support.mozilla.org/questions/1614669 "How can I whitelist email senders using message filters?") [1614077](https://support.mozilla.org/questions/1614077 "Something is blocking one of my contacts from appearing in my firefox mail:    a") +1

### 9. Thunderbird hangs/freezes at startup (session.json, loading messages, profile lock) {#issue-9}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Thunderbird hangs/freezes at startup (session.json, loading messages, profile lock) (performance-crash) | 30 | 25 | ▼ -5 (-17%) | 4.2 (21) | 80% | 8% |

- Why it matters: Rank 9 is high severity at 4.2 but support resolves 80 percent of startup hangs, so the existing guidance works.
- What to look at: Engineering should consider keeping the known fixes for session.json and profile lock files, and watch for any rise after the next release.
- Example questions: [1612463](https://support.mozilla.org/questions/1612463 "Unable to load Thunderbird") [1612917](https://support.mozilla.org/questions/1612917 "After the update to version 158  it opens and shortly afterwards freezes.") [1610394](https://support.mozilla.org/questions/1610394 "Thunderbird fails to start after update on Ubuntu") [1614055](https://support.mozilla.org/questions/1614055 "Hello, ik heb problemen met thunderbird op windows 11 . Bij het opstarten krijg ") [1613838](https://support.mozilla.org/questions/1613838 "Thunderbird non risponde dopo l'installazione") +1

### 10. Folders missing/disappeared from folder pane after update {#issue-10}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Folders missing/disappeared from folder pane after update (search-folders) | 13 | 15 | ▲ +2 (+15%) | 4.4 (13) | 40% (below 50%) | 27% |

- Why it matters: Rank 10 carries the highest mean severity at 4.4 and resolves only 40 percent, and users tie missing folders to an update.
- What to look at: Engineering should consider tracing folder pane state loss across upgrades, including whether folder subscription or cache files get rewritten on first run.
- Example questions: [1609211](https://support.mozilla.org/questions/1609211 "Пропажа отправленных сообщений") [1609927](https://support.mozilla.org/questions/1609927 "i have lost all my emails") [1610432](https://support.mozilla.org/questions/1610432 "Disparition de sous-dossiers (.sbd) après un glisser-déposer vers un compte IMAP") [1611881](https://support.mozilla.org/questions/1611881 "FOLDERS in my thunderbox email have disappeared how do i recover them") [1611890](https://support.mozilla.org/questions/1611890 "Loss of all my filed emails") +1

### 11. Gmail OAuth2 authentication/login failures and re-auth loops (m:gmail) {#issue-11}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Gmail OAuth2 authentication/login failures and re-auth loops (m:gmail) (sync-oauth) | 8 | 13 | ▲ +5 | 3.6 (8) | 31% (below 50%) | 15% |

- Why it matters: Rank 11 grew to 13 reports and resolves at 31 percent, which shows Gmail re-authentication loops repeat without a working fix.
- What to look at: Engineering should consider looking at why a refresh token gets rejected and the login prompt reappears, and adding a clean token reset path.
- Example questions: [1613156](https://support.mozilla.org/questions/1613156 "Unable to send emails") [1608938](https://support.mozilla.org/questions/1608938 "Thunderbird non riceve i miei indirizzi maxs21r@hotmail-it e maxs21r  ò   gmail.") [1610127](https://support.mozilla.org/questions/1610127 "Thunderbird does not recognise password email account password in linux on chrom") [1611880](https://support.mozilla.org/questions/1611880 "Unable to Add a Gmail Account to Thunderbird Despite Successful Authentication") [1612677](https://support.mozilla.org/questions/1612677 "Gmail authentification dialog does not open when setting up new account") +1

### 12. Calendar add-ons (CardBook, Provider for Google Calendar, TbSync) broken by TB updates {#issue-12}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Calendar add-ons (CardBook, Provider for Google Calendar, TbSync) broken by TB updates (addons-extensions) | 5 | 14 | ▲ +9 | 3.6 (10) | 86% | 0% |

- Why it matters: Rank 12 nearly tripled to 14 reports but resolves at 86 percent with zero unanswered, so the fix path is already clear.
- What to look at: Engineering should consider warning add-on authors earlier when calendar and contact APIs change, since CardBook, TbSync and the Google Calendar provider keep breaking on update.
- Example questions: [1610169](https://support.mozilla.org/questions/1610169 "Calendari disattivati") [1608944](https://support.mozilla.org/questions/1608944 "Thunderbird 157 breaks google calendar add-on") [1608983](https://support.mozilla.org/questions/1608983 "Google Calendar & Tasks suddenly fail in Thunderbird 157 64bit") [1609292](https://support.mozilla.org/questions/1609292 "thunderbird 157 update deactivated all my calendars") [1614739](https://support.mozilla.org/questions/1614739 "PLEASE STOP RELEASING UNTESTED UPDATES") +1

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

Last updated: 2026-11-03 13:45 UTC
