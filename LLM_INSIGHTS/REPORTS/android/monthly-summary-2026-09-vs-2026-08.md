---
layout: base
title: Android LLM Insights — September 2026
---

# Thunderbird Android — LLM Insights (Engineering)

## September 2026 against August 2026

## TL;DR: the five issues to look at first {#tldr}

| # | Issue | August 2026 | September 2026 | Severity | Resolved | Known status |
|--:|:--|--:|--:|--:|--:|:--|
| [1](#issue-1) | [Background sync and push notifications not working unless app opened](#issue-1), new this month | 0 | 3 | 3.7 | 33% (below 50%) | — |
| [2](#issue-2) | [Message body renders empty in Android message viewer](#issue-2), new this month | 0 | 3 | 3.3 | 33% (below 50%) | — |
| [3](#issue-3) | [QR code import button missing or non-functional at setup](#issue-3), new this month | 0 | 3 | 3.3 | 67% | — |
| [4](#issue-4) | [Push notification delays and re-enabling disabled notifications](#issue-4), new this month | 0 | 2 | 3.0 | 50% | — |
| [5](#issue-5) | [Remote images: no 'always show' setting on Android](#issue-5), new this month | 0 | 2 | 2.0 | 100% | — |

Each number links to the same issue in [Issues to investigate](#issues-to-investigate) below, which carries the reason, what to look at, and the example questions.

Read this page as a list of the month's problems, not as a trend. September 2026 holds 41 questions in 29 clusters, so most clusters hold one or two questions. A change of one question is noise, and "new this month" often means only that nobody worded the problem that way last month. The severity and the resolved figures carry the signal here.

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
| Support questions (load) | 40 | 41 | ▲ +1 (+2%) |
| Distinct issue clusters | 31 | 29 | ▼ -2 |
| New issue clusters this month | — | 6 | |

Android background sync and empty message bodies lead six new issue clusters in September 2026

Total support questions held flat. August had 40, September has 41. But six new issue clusters appeared, and all six point at Thunderbird for Android. Engineering must treat the mobile client as this month's hot spot.

Two new clusters carry real user pain. Background sync and push notifications fail unless the user opens the app. Only 33 percent of those reports got resolved. Message bodies render blank in the Android viewer. That cluster also sits at 33 percent resolved, and 67 percent of the reports got no answer at all. Unanswered means no support reply was recorded.

Category shifts match the story. Sync and OAuth rose from 3 to 5. Settings and config rose from 3 to 6. Migration and import rose from 1 to 3. Send and receive rose from 5 to 7. UI and UX fell from 8 to 6, and attachments dropped to zero.

This signal comes from a language model reading free-text support questions. Use it to pick where to dig, not as proof of a defect.

## Issues to investigate {#issues-to-investigate}

The order comes from a Python score. It weights new clusters, badly served clusters, severity and volume, in that order. Resolved means the question has an accepted solution, or a trusted contributor gave the last answer. A resolved figure under 50% is marked.

### 1. Background sync and push notifications not working unless app opened, new this month {#issue-1}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Background sync and push notifications not working unless app opened (sync-oauth) | 0 | 3 | ▲ +3 | 3.7 (2) | 33% (below 50%) | 33% |

- Why it matters: Three users report that mail only arrives when they open the app, and support resolved just one of the three.
- What to look at: Engineering must check Firebase push delivery, Android background work scheduling, and battery optimisation exemptions on recent Android versions.
- Example questions: [1602435](https://support.mozilla.org/questions/1602435 "incoming emails don't display in Inbox on android") [1608763](https://support.mozilla.org/questions/1608763 "Thunderbird Android not pushing new notifications") [1606852](https://support.mozilla.org/questions/1606852 "Getting notifications on android?")

### 2. Message body renders empty in Android message viewer, new this month {#issue-2}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Message body renders empty in Android message viewer (send-receive) | 0 | 3 | ▲ +3 | 3.3 (1) | 33% (below 50%) | 67% |

- Why it matters: Three users see blank message bodies in the Android viewer, and two of the three reports got no reply at all.
- What to look at: Engineering must reproduce blank rendering against HTML and multipart messages, and inspect the WebView rendering path and MIME body selection.
- Example questions: [1602183](https://support.mozilla.org/questions/1602183 "All emails are empty") [1601432](https://support.mozilla.org/questions/1601432 "Message body of certain email is empty") [1604037](https://support.mozilla.org/questions/1604037 "Some emails opened in thunderbird for android immediately blank out and only rea")

### 3. QR code import button missing or non-functional at setup, new this month {#issue-3}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| QR code import button missing or non-functional at setup (migration-import) | 0 | 3 | ▲ +3 | 3.3 (1) | 67% | 0% |

- Why it matters: Three users cannot finish desktop-to-mobile setup because the QR code import button is missing or dead.
- What to look at: Engineering must test the QR import entry point across fresh installs and check camera permission handling and the account transfer build flag.
- Example questions: [1605621](https://support.mozilla.org/questions/1605621 "“Scan QR code” button does nothing in Thunderbird for Android 23.0") [1604782](https://support.mozilla.org/questions/1604782 "Unable to set up Thunderbird Mobile on my Android phone") [1604884](https://support.mozilla.org/questions/1604884 "Unable to set up Thunderbird Mobile on my Android phone.")

### 4. Push notification delays and re-enabling disabled notifications, new this month {#issue-4}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Push notification delays and re-enabling disabled notifications (settings-config) | 0 | 2 | ▲ +2 | 3.0 (0) | 50% | 50% |

- Why it matters: Two users report late notifications and no clear way to turn notifications back on after Android disables them.
- What to look at: Engineering must measure notification latency end to end and add an in-app path to restore a disabled notification channel.
- Example questions: [1601974](https://support.mozilla.org/questions/1601974 "Push notifications delayed when inboxes are unified.") [1607794](https://support.mozilla.org/questions/1607794 "how to re-enable push notifications, notifications?")

### 5. Remote images: no 'always show' setting on Android, new this month {#issue-5}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Remote images: no 'always show' setting on Android (settings-config) | 0 | 2 | ▲ +2 | 2.0 (0) | 100% | 0% |

- Why it matters: Two users want remote images to load by default and found no setting, which is a small gap but a repeated one.
- What to look at: Engineering must decide whether to add a per-account always-show-remote-images preference on Android, matching desktop behaviour.
- Example questions: [1602040](https://support.mozilla.org/questions/1602040 "Show remote images automatically") [1608374](https://support.mozilla.org/questions/1608374 "如何让App每次打开邮件都自动显示图片？")

### 6. Cannot create folders or manage contacts in Thunderbird for Android, new this month {#issue-6}

| Cluster | August 2026 | September 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Cannot create folders or manage contacts in Thunderbird for Android (search-folders) | 0 | 2 | ▲ +2 | 2.0 (0) | 100% | 0% |

- Why it matters: Two users expect folder creation and contact management on Android and did not find them.
- What to look at: Engineering must confirm these are known gaps and publish the roadmap position so support can answer in one line.
- Example questions: [1606251](https://support.mozilla.org/questions/1606251 "I cannot find contact on Thunderbird for Android") [1607408](https://support.mozilla.org/questions/1607408 "How do I add new folders?")

## Category mix, month over month

| Category | August 2026 | September 2026 | Change |
|:--|--:|--:|:--|
| send-receive | 5 | 7 | ▲ +2 |
| ui-ux | 8 | 6 | ▼ -2 |
| settings-config | 3 | 6 | ▲ +3 |
| account-login | 6 | 5 | ▼ -1 |
| sync-oauth | 3 | 5 | ▲ +2 |
| migration-import | 1 | 3 | ▲ +2 |
| encryption-security | 3 | 2 | ▼ -1 |
| other | 4 | 2 | ▼ -2 |
| performance-crash | 3 | 2 | ▼ -1 |
| search-folders | 1 | 2 | ▲ +1 |
| spam-filters | 1 | 1 | ▬ 0 |
| attachments | 2 | 0 | ▼ -2 |

---

This is a prototype. Claude claude-opus-5 wrote the labels for each question, and this run reused the cached LLM output and cost $0.00 (the full cost is in `LLM_INSIGHTS/COSTS.md`). The page covers September 2026 against August 2026. Facts the corpus cannot know, such as a shipped fix, come from `LLM_INSIGHTS/known-status.csv` and appear as Known status.

Last updated: 2026-10-08 03:57 UTC
