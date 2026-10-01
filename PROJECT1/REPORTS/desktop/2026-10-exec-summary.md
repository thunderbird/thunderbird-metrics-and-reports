---
layout: base
title: "2026-10 exec summary: Thunderbird Desktop support spikes"
---

# October 2026: Thunderbird Desktop support spikes

Executive summary for 2026-10. It covers 2 Thunderbird Desktop support questions. The tool wrote this page on 2026-10-01 05:36 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## October 2026: 2 spikes to investigate

All 2 tie to a Thunderbird version. None of them are cause-level. Every row is in the collapsed blocks below.

October 2026 is still in progress. The counts will grow.

In short: Address book and Import and export. [What stands out](#what-stands-out) has the detail.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 0 | 2 | 0 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 0 | 0 |

October 2026 holds 2 questions, about 2 a day. The detectors need 8 questions of one kind in a day, 6 in a week or 8 in a month before they call a spike. At this volume most real clusters cannot clear those floors, so read a zero as "nothing large enough to fire", not as "nothing happened".

Three more numbers for context:

- Volume: 2 questions. 0 of them (0%) carry a cause tag. The count per day was `█`, one block per day from October 1 to October 1.
- Answers: 0 of the 2 questions (0%) got an answer from somebody other than the person who asked.
- Release-adoption version spikes: 1. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All October 2026 detail](#all-october-2026-detail) below.

## What stands out {#what-stands-out}

1. Address book ([`feat:addressbook`](explorer.html#grain=monthly&cause=feat:addressbook&period=2026-10), 1 spike):  It peaked in the week of 2026-09-28 at 3.7 times expected, on Thunderbird 156.
2. Import and export ([`feat:import_export`](explorer.html#grain=monthly&cause=feat:import_export&period=2026-10), 1 spike):  It peaked in the week of 2026-09-28 at 3.5 times expected, on Thunderbird 156.

In 1 cluster, fewer than 60% of the questions got an answer: `v156 × feat:import_export` in the week of 2026-09-28 (40% answered).

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 1 row</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

Cause alone:

| Grain | Rise | When | Cause | Questions | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.6× | 2026-09-28 | feat:import_export | 9 | 44% answered (below 60%), 0.7h | 3.5 | [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") [1608076](https://support.mozilla.org/questions/1608076 "Import from Outlook") [1608137](https://support.mozilla.org/questions/1608137 "Missing Outlook import information") [1608271](https://support.mozilla.org/questions/1608271 "preciso de ajuda para fazer backup no thunderbird.") [1608318](https://support.mozilla.org/questions/1608318 "How do I migrate local folders from Outlook for Mac to Thunderbird") [1608366](https://support.mozilla.org/questions/1608366 "Since thunderbird freezes when I try to import from outlook 2016 (Win 7), how ca") +3 |


</details>

---

## All October 2026 detail {#all-october-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 2 rows</summary>

| Grain | Lift | When | Version × Cause | Questions | Served | Novelty | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| weekly | 3.7× | 2026-09-28 | v156 × feat:addressbook | 4 | 75% answered, 0.1h | new | [1608295](https://support.mozilla.org/questions/1608295 "reloaded Thuderbird but address book .sqlite file not reloading") [1608307](https://support.mozilla.org/questions/1608307 "How to sync iCloud Contacts to Thunderbird") [1608370](https://support.mozilla.org/questions/1608370 "How to import contacts from Thunderbird to Zoho") [1608602](https://support.mozilla.org/questions/1608602 "Remove Personall Address Book and Collected Addresses from Address Book") |
| weekly | 3.5× | 2026-09-28 | v156 × feat:import_export | 5 | 40% answered (below 60%), 1.0h | spreading | [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") [1608076](https://support.mozilla.org/questions/1608076 "Import from Outlook") [1608271](https://support.mozilla.org/questions/1608271 "preciso de ajuda para fazer backup no thunderbird.") [1608370](https://support.mozilla.org/questions/1608370 "How to import contacts from Thunderbird to Zoho") [1608599](https://support.mozilla.org/questions/1608599 "Export/Import accounts only") |

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 0 rows</summary>

None.

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 1 row</summary>

Version and operating system are filters, not causes. A rise in the bare count of one version is release adoption, not a regression. The rows are here for manual checking only.

| Grain | Rise | When | Dimension | Value | Questions | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| weekly | new | 2026-09-28 | tb_version_major | 156 | 51 [1607958](https://support.mozilla.org/questions/1607958 "free large video and large file  sender  to send large files  videos in Thunderb") [1607999](https://support.mozilla.org/questions/1607999 "How do I import Thunderbird profile from Windows 11 to Ubuntu 24.04?") | 0.0 |

</details>

<details markdown="1">
<summary>October 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v157 | 1 | `█` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:windows | 2 | `█` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward October 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
