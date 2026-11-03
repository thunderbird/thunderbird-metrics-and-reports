---
layout: base
title: Android LLM Insights — October 2026
---

# Thunderbird Android — LLM Insights (Engineering)

## October 2026 against September 2026

## TL;DR: the five issues to look at first {#tldr}

| # | Issue | September 2026 | October 2026 | Severity | Resolved | Known status |
|--:|:--|--:|--:|--:|--:|:--|
| [1](#issue-1) | [Outlook/Hotmail 'authenticated but not connected' error](#issue-1), new this month | 0 | 3 | 3.7 | 0% (below 50%) | — |
| [2](#issue-2) | [Android credentials rejected though valid on desktop](#issue-2), new this month | 0 | 3 | 3.3 | 67% | — |
| [3](#issue-3) | [Deleted messages disappear instead of moving to Trash](#issue-3), new this month | 0 | 2 | 4.0 | 0% (below 50%) | — |
| [4](#issue-4) | [QR import leaves accounts unauthenticated / passwords not transferred](#issue-4), new this month | 0 | 3 | 2.7 | 100% | — |
| [5](#issue-5) | [Desktop/Android account and subfolder sync guidance](#issue-5), new this month | 0 | 2 | 2.5 | 0% (below 50%) | — |

Each number links to the same issue in [Issues to investigate](#issues-to-investigate) below, which carries the reason, what to look at, and the example questions.

Read this page as a list of the month's problems, not as a trend. October 2026 holds 56 questions in 43 clusters, so most clusters hold one or two questions. A change of one question is noise, and "new this month" often means only that nobody worded the problem that way last month. The severity and the resolved figures carry the signal here.

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
| Support questions (load) | 41 | 56 | ▲ +15 (+37%) |
| Distinct issue clusters | 30 | 43 | ▲ +13 |
| New issue clusters this month | — | 8 | |

Eight brand-new issue clusters this month, led by Outlook login failures and deleted mail vanishing instead of going to Trash

Support volume rose from 41 questions in September to 56 in October. Every one of this month's top eight clusters is new. Nothing carried over from September. That pattern points at a recent release or a recent change at a mail provider.

Two clusters have zero resolved rate and high severity. Users hitting the Outlook and Hotmail "authenticated but not connected" error get no working fix. Users who delete a message and watch it disappear instead of landing in Trash also get no fix. Data loss reports carry the highest severity scores in the set.

Android is the common thread. Five of the eight clusters involve the Android app: credential rejection, QR import, subfolder sync, threaded view, and vanishing inbox contents. Engineering should consider treating Android account setup and folder state as one investigation, not five.

Category totals back this up. UI and UX doubled from 6 to 12. Attachments went from 0 to 3. Account and login went from 5 to 7. These counts come from an automated read of free-text support questions. Treat them as a place to start looking, not as proof.

## Issues to investigate {#issues-to-investigate}

The order comes from a Python score. It weights new clusters, badly served clusters, severity and volume, in that order. Resolved means the question has an accepted solution, or a trusted contributor gave the last answer. A resolved figure under 50% is marked.

### 1. Outlook/Hotmail 'authenticated but not connected' error, new this month {#issue-1}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Outlook/Hotmail 'authenticated but not connected' error (account-login) | 0 | 3 | ▲ +3 | 3.7 (2) | 0% (below 50%) | 0% |

- Reviewer note: Roland Tanglao: Same comment as for the desktop Gmail cluster: There wasn't enough troubleshooting details provided by Thunderbird for Android users to diagnose. Problem cause could have been anti-virus, network issues, add-ons, an issue specific to POP3, a Thunderbird bug, etc. Engineering should consider adding troubleshooting features to Thunderbird for Android, especially for popular providers like Outlook/Hotmail and Gmail.
- Why it matters: Three users report Outlook or Hotmail accounts that pass sign-in but never connect, and zero of them got a fix.
- What to look at: Engineering should consider tracing the Microsoft OAuth token exchange after consent, and checking whether a scope or endpoint change broke the follow-up IMAP connection.
- Example questions: [1609449](https://support.mozilla.org/questions/1609449 "Authentication and connection drops with Outlook accounts (User is authenticated") [1612980](https://support.mozilla.org/questions/1612980 "UNABLE TO CONNECT TO THUNDERBIRD ON ANDROID SAMSUN S25. ＂User is authenticared b") [1609460](https://support.mozilla.org/questions/1609460 "Connection issue")

### 2. Android credentials rejected though valid on desktop, new this month {#issue-2}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Android credentials rejected though valid on desktop (account-login) | 0 | 3 | ▲ +3 | 3.3 (2) | 67% | 33% |

- Reviewer note: Roland Tanglao: Engineering could fix this with Sync, which is on the roadmap with no timeline. If Thunderbird Desktop synced with Thunderbird for Android like Firefox desktop syncs with Firefox Android, these issues could be reduced.
- Why it matters: Three users had credentials rejected on Android while the same credentials worked on desktop, which points at a client-side auth difference.
- What to look at: Engineering should consider comparing the OAuth client identifiers and token storage used by Android against desktop for the same provider.
- Example questions: [1611891](https://support.mozilla.org/questions/1611891 "Login hurdle using desktop user and password into mobile app on Android") [1614628](https://support.mozilla.org/questions/1614628 "не могу зайти на почту v_polyakova@alcopack.ru") [1614921](https://support.mozilla.org/questions/1614921 "Email address primary Account not accepted, as it should be!")

### 3. Deleted messages disappear instead of moving to Trash, new this month {#issue-3}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Deleted messages disappear instead of moving to Trash (send-receive) | 0 | 2 | ▲ +2 | 4.0 (2) | 0% (below 50%) | 0% |

- Why it matters: Deleted mail vanishes instead of moving to Trash, the highest-severity kind of report, and neither case was resolved.
- What to look at: Engineering should consider checking Trash folder mapping and the expunge-on-delete path for the affected IMAP accounts.
- Example questions: [1610658](https://support.mozilla.org/questions/1610658 "Deleted emails disappear - not in 'deleted mail' folder") [1611184](https://support.mozilla.org/questions/1611184 "I want messages i delete to go to deleted messages in side panel")

### 4. QR import leaves accounts unauthenticated / passwords not transferred, new this month {#issue-4}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| QR import leaves accounts unauthenticated / passwords not transferred (migration-import) | 0 | 3 | ▲ +3 | 2.7 (0) | 100% | 0% |

- Why it matters: QR import, the feature that copies desktop accounts to Android by scanning a code, leaves accounts without working passwords.
- What to look at: Engineering should consider confirming whether the QR payload carries stored secrets and OAuth refresh tokens, or only server settings.
- Example questions: [1609183](https://support.mozilla.org/questions/1609183 "[Import] No Settings menu to use QR code") [1610685](https://support.mozilla.org/questions/1610685 "Opens with outbox") [1609814](https://support.mozilla.org/questions/1609814 "Beta: after QR import, Google accounts show ＂restore apps＂ screen, blank account")

### 5. Desktop/Android account and subfolder sync guidance, new this month {#issue-5}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Desktop/Android account and subfolder sync guidance (sync-oauth) | 0 | 2 | ▲ +2 | 2.5 (0) | 0% (below 50%) | 100% |

- Why it matters: Both reports about syncing accounts and subfolders between desktop and Android went unanswered, so users got nothing.
- What to look at: Engineering should consider checking default IMAP folder subscription behaviour on Android and writing down the expected behaviour for support staff.
- Example questions: [1615150](https://support.mozilla.org/questions/1615150 "How to synchronise adresses and mail folders with Thunderbird for windows") [1609233](https://support.mozilla.org/questions/1609233 "Following a bereavement I need help with all the technology that my partner mana")

### 6. Threaded/conversation view missing or incomplete on Android, new this month {#issue-6}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Threaded/conversation view missing or incomplete on Android (ui-ux) | 0 | 2 | ▲ +2 | 2.5 (0) | 0% (below 50%) | 50% |

- Why it matters: Users expect grouped conversation view on Android and report it as missing or partial, and half the reports got no reply.
- What to look at: Engineering should consider confirming the current state of threading on Android and stating clearly whether it is a bug or an unshipped feature.
- Example questions: [1615121](https://support.mozilla.org/questions/1615121 "Conversation view doesn't work") [1608898](https://support.mozilla.org/questions/1608898 "Ser email threads on Thunderbird mobile")

### 7. Inbox contents disappeared on Android, new this month {#issue-7}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Inbox contents disappeared on Android (send-receive) | 0 | 2 | ▲ +2 | 4.5 (2) | 100% | 0% |

- Why it matters: Inbox contents disappeared on Android with the highest mean severity in the set, even though both cases eventually got resolved.
- What to look at: Engineering should consider looking at local message database resets and folder resync after app or account updates.
- Example questions: [1614927](https://support.mozilla.org/questions/1614927 "lost emails") [1612939](https://support.mozilla.org/questions/1612939 "Email Messages not Loading, on both my laptop and cell phone")

### 8. Sending fails silently with no error detail, new this month {#issue-8}

| Cluster | September 2026 | October 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Sending fails silently with no error detail (attachments) | 0 | 2 | ▲ +2 | 4.0 (2) | 100% | 0% |

- Why it matters: Sending fails with no error text, so users cannot tell whether the message left or what blocked it.
- What to look at: Engineering should consider surfacing the underlying SMTP response in the compose window, including attachment size rejections.
- Example questions: [1611844](https://support.mozilla.org/questions/1611844 "Thunderbird for Android troubleshooting outbound mail") [1612913](https://support.mozilla.org/questions/1612913 "sending attachments in Thunderbird android")

## Category mix, month over month

| Category | September 2026 | October 2026 | Change |
|:--|--:|--:|:--|
| ui-ux | 6 | 12 | ▲ +6 |
| send-receive | 7 | 9 | ▲ +2 |
| account-login | 5 | 7 | ▲ +2 |
| settings-config | 6 | 6 | ▬ 0 |
| other | 2 | 5 | ▲ +3 |
| sync-oauth | 5 | 4 | ▼ -1 |
| migration-import | 3 | 3 | ▬ 0 |
| search-folders | 2 | 3 | ▲ +1 |
| attachments | 0 | 3 | ▲ +3 |
| spam-filters | 1 | 2 | ▲ +1 |
| performance-crash | 2 | 1 | ▼ -1 |
| encryption-security | 2 | 1 | ▼ -1 |

---

This is a prototype. Claude claude-opus-5 wrote the labels for each question, and this run reused the cached LLM output and cost $0.00 (the full cost is in `LLM_INSIGHTS/COSTS.md`). The page covers October 2026 against September 2026. Facts the corpus cannot know, such as a shipped fix, come from `LLM_INSIGHTS/known-status.csv` and appear as Known status.

Last updated: 2026-11-03 14:46 UTC
