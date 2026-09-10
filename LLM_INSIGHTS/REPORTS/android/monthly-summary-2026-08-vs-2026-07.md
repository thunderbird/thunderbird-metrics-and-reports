---
layout: base
title: Android LLM Insights — August 2026
---

# Thunderbird Android — LLM Insights (Engineering)

## August 2026 against July 2026

## TL;DR: the five issues to look at first {#tldr}

| # | Issue | July 2026 | August 2026 | Severity | Resolved | Known status |
|--:|:--|--:|--:|--:|--:|:--|
| [1](#issue-1) | [Stored password reverts or cannot be updated on Android](#issue-1), new this month | 0 | 2 | 4.0 | 100% | — |
| [2](#issue-2) | [Crash opening downloaded email on Android](#issue-2), new this month | 0 | 2 | 4.0 | 100% | — |
| [3](#issue-3) | [AOL/Yahoo account repeatedly prompts for login and stops receiving](#issue-3), new this month | 0 | 2 | 3.5 | 100% | — |
| [4](#issue-4) | [Contact autocomplete not suggesting addresses in To field](#issue-4), new this month | 0 | 2 | 2.0 | 50% | — |
| [5](#issue-5) | [No OpenPGP/S-MIME encryption support on Android](#issue-5), new this month | 0 | 2 | 3.0 | 100% | — |

Each number links to the same issue in [Issues to investigate](#issues-to-investigate) below, which carries the reason, what to look at, and the example questions.

Read this page as a list of the month's problems, not as a trend. August 2026 holds 40 questions in 33 clusters, so most clusters hold one or two questions. A change of one question is noise, and "new this month" often means only that nobody worded the problem that way last month. The severity and the resolved figures carry the signal here.

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
| Support questions (load) | 44 | 40 | ▼ -4 (-9%) |
| Distinct issue clusters | 34 | 33 | ▼ -1 |
| New issue clusters this month | — | 5 | |

Android account and crash reports drive five new issue clusters while overall volume falls slightly

Support volume dropped from 44 questions in July to 40 in August. But five of the six top issues are new this month. Four of those five point at Thunderbird for Android. Engineering must treat the Android client as the focus for this month.

Account and login problems grew from 4 to 6 questions. Three separate clusters describe the same shape of failure. Stored passwords revert or refuse to update on Android. AOL and Yahoo accounts loop on login prompts and stop receiving mail. Imported accounts arrive with no password and show only an Outbox. A shared credential storage or migration path is the likely root cause.

Crash reports rose from 1 to 3. Two of those are one new cluster: the Android app crashes when a user opens a downloaded email. Encryption questions went from 0 to 3, and users are asking for OpenPGP and S/MIME on Android, which the client does not offer.

One issue is served badly. Contact autocomplete failures in the To field resolved at 50 percent. Every other top cluster resolved at 100 percent. That gap means support has no working answer for autocomplete. This reading comes from an automated pass over free-text support questions. Treat it as a triage pointer, not proof.

## Issues to investigate {#issues-to-investigate}

The order comes from a Python score. It weights new clusters, badly served clusters, severity and volume, in that order. Resolved means the question has an accepted solution, or a trusted contributor gave the last answer. A resolved figure under 50% is marked.

### 1. Stored password reverts or cannot be updated on Android, new this month {#issue-1}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Stored password reverts or cannot be updated on Android (account-login) | 0 | 2 | ▲ +2 | 4.0 (2) | 100% | 0% |

- Why it matters: Users on Android cannot change a stored password, and the old value returns, which locks them out of mail.
- What to look at: Engineering must trace the Android credential store write path and check whether account settings save silently fails or gets overwritten on sync.
- Example questions: [1597727](https://support.mozilla.org/questions/1597727 "Password for email accounts in Thunderbird for Android are frequently reverting ") [1601249](https://support.mozilla.org/questions/1601249 "Can't get into my main email account")

### 2. Crash opening downloaded email on Android, new this month {#issue-2}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Crash opening downloaded email on Android (performance-crash) | 0 | 2 | ▲ +2 | 4.0 (2) | 100% | 0% |

- Why it matters: The Android app crashes when a user opens a downloaded message, and mean severity is 4.0, the highest in the set.
- What to look at: Engineering must pull crash traces for the message viewer on downloaded mail and test large or unusual MIME bodies.
- Example questions: [1596786](https://support.mozilla.org/questions/1596786 "Email downloads but cannot be opened") [1596787](https://support.mozilla.org/questions/1596787 "Email downloads but cannot be opened")

### 3. AOL/Yahoo account repeatedly prompts for login and stops receiving, new this month {#issue-3}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| AOL/Yahoo account repeatedly prompts for login and stops receiving (account-login) | 0 | 2 | ▲ +2 | 3.5 (1) | 100% | 0% |

- Why it matters: AOL and Yahoo accounts prompt for login in a loop and then stop receiving mail entirely.
- What to look at: Engineering must check OAuth token refresh against current AOL and Yahoo endpoints, since both providers share one backend.
- Example questions: [1598131](https://support.mozilla.org/questions/1598131 "JE NE PEUX PLUS LIRE MES MAILS AVEC THUNDERBIRD? Quand je veux voir Thunderbird ") [1599009](https://support.mozilla.org/questions/1599009 "no email access on Android phone")

### 4. Contact autocomplete not suggesting addresses in To field, new this month {#issue-4}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Contact autocomplete not suggesting addresses in To field (other) | 0 | 2 | ▲ +2 | 2.0 (0) | 50% | 0% |

- Why it matters: Only half of these users got a resolution, the worst rate in the set, so support has no known fix for missing contact autocomplete.
- What to look at: Engineering must reproduce autocomplete against local address book and directory sources, then publish a diagnostic path support can follow.
- Example questions: [1597532](https://support.mozilla.org/questions/1597532 "How do you save a regular email sender in Thundermail, I've looked everywhere!") [1599008](https://support.mozilla.org/questions/1599008 "No longer see list of possible email addresses when I start typing a name in TO ")

### 5. No OpenPGP/S-MIME encryption support on Android, new this month {#issue-5}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| No OpenPGP/S-MIME encryption support on Android (encryption-security) | 0 | 2 | ▲ +2 | 3.0 (0) | 100% | 0% |

- Why it matters: Users expect OpenPGP and S/MIME encryption on Android and file support tickets when they cannot find it.
- What to look at: Engineering must confirm the roadmap position for Android encryption and give support a clear public statement to link.
- Example questions: [1599880](https://support.mozilla.org/questions/1599880 "Support for s/mime certificates and encryption") [1600129](https://support.mozilla.org/questions/1600129 "OpenKeychain s no longer actively developed, replacement?")

### 6. Imported account shows only Outbox / missing passwords after import {#issue-6}

| Cluster | July 2026 | August 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Imported account shows only Outbox / missing passwords after import (account-login) | 1 | 3 | ▲ +2 | 3.3 (1) | 100% | 0% |

- Why it matters: This grew from 1 to 3 questions, and imported accounts land with no password and only an Outbox visible, which looks like total data loss to the user.
- What to look at: Engineering must audit the import routine for password carry-over and folder subscription, and connect it to the credential bugs in ranks 1 and 3.
- Example questions: [1601095](https://support.mozilla.org/questions/1601095 "携帯でメールアカウントを二つにすると片方が送信トレイしか表示されない") [1596244](https://support.mozilla.org/questions/1596244 "After installing Thunderbird for android it only show the outbox for all my acco") [1598503](https://support.mozilla.org/questions/1598503 "after import, how to enter passwords")

## Category mix, month over month

| Category | July 2026 | August 2026 | Change |
|:--|--:|--:|:--|
| ui-ux | 7 | 8 | ▲ +1 |
| account-login | 4 | 6 | ▲ +2 |
| send-receive | 11 | 5 | ▼ -6 (-55%) |
| other | 5 | 4 | ▼ -1 |
| encryption-security | 0 | 3 | ▲ +3 |
| settings-config | 3 | 3 | ▬ 0 |
| sync-oauth | 1 | 3 | ▲ +2 |
| performance-crash | 1 | 3 | ▲ +2 |
| attachments | 0 | 2 | ▲ +2 |
| spam-filters | 0 | 1 | ▲ +1 |
| migration-import | 7 | 1 | ▼ -6 |
| search-folders | 5 | 1 | ▼ -4 |

---

This is a prototype. Claude claude-opus-5 wrote the labels for each question, and this run of the report cost $0.00. The page covers August 2026 against July 2026. Facts the corpus cannot know, such as a shipped fix, come from `LLM_INSIGHTS/known-status.csv` and appear as Known status.

Last updated: 2026-09-10 07:54 UTC
