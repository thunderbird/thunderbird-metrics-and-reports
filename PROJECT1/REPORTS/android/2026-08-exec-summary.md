---
layout: base
title: "2026-08 exec summary: Thunderbird Android support spikes"
---

# August 2026: Thunderbird Android support spikes

Executive summary for 2026-08. It covers 40 Thunderbird Android support questions. The tool wrote this page on 2026-09-10 04:50 UTC. No AI read the questions. The tool uses regular expressions and standard statistics only.

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

## August 2026: no spike cleared the threshold

No spike cleared the threshold at any grain. The tool found no mail host outage, no protocol surge, no antivirus breakage and no release regression in August 2026.

| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| version×cause (a release caused the problem) | 0 | 0 | 0 |
| cause-level (mail host, protocol, antivirus, feature) | 0 | 0 | 0 |

August 2026 holds 40 questions, about 1 a day. The detectors need 8 questions of one kind in a day, 6 in a week or 8 in a month before they call a spike. At this volume most real clusters cannot clear those floors, so read a zero as "nothing large enough to fire", not as "nothing happened".

Only 2% of the August 2026 questions carry a Thunderbird version. The version×cause detector therefore cannot fire. Read its zero as missing data, not as a clean result.

Three more numbers for context:

- Volume: 40 questions. 18 of them (45%) carry a cause tag. The count per day was `▁▆▃▅▆▁▃█▅▃▅▁▃▅▁▃▁▆▁▃▃▁▃▅▆▃▃▃▁▃▅`, one block per day from August 1 to August 31.
- Answers: 36 of the 40 questions (90%) got an answer from somebody other than the person who asked. The middle time to the first answer was 5.3 hours.
- Release-adoption version spikes: 0. Users move to a new release, so the bare counts rise. These are not incidents.

Every spike row, with its example questions, is in [All August 2026 detail](#all-august-2026-detail) below.

## Two limits of these dates

Read the date of a spike as the day users came to the support site, not as the day the problem started. Users retry and wait before they post, so a spike usually dates days after the start of a problem, often close to the fix. Use this page to find clusters of pain, not to detect a live incident.

A closed month can also change its verdict later. The tool measures each rise against the rate of that cause across all history. Questions that arrive later therefore move the expected count for a past month. Rows can cross the threshold in both directions, and the answered percentage rises as late answers land. This page regenerates every day, and each day's version is committed, so `git log -p` on this file shows how the verdict moved.

<details markdown="1">
<summary>Near misses (within about 25% of the threshold), 0 rows</summary>

The tool runs the same detectors a second time at 0.75 times the thresholds. The rows below came out of that second run and did not clear the real thresholds. They are not incidents. They are context, so that a quiet month is not read as a clean month.

None. Nothing came within about 25% of the threshold either.

</details>

---

## All August 2026 detail {#all-august-2026-detail}

<details markdown="1">
<summary>Version × cause spikes, 0 rows</summary>

None.

</details>

<details markdown="1">
<summary>Cause-level spikes (mail host, protocol, antivirus, feature), 0 rows</summary>

None.

</details>

<details markdown="1">
<summary>Release-adoption version and operating-system spikes (not incidents), 0 rows</summary>

None.

</details>

<details markdown="1">
<summary>August 2026 trends, 7 rows</summary>

The Thunderbird versions named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| v140 | 1 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

The mail hosts named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| m:yahooemail | 4 | `▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁█▁▁█▁▁▁▁▁▁▁▁▁▁` |
| m:gmail | 2 | `▁▁▁██▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:telus | 1 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:btinternet | 1 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:thundermail | 1 | `▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| m:icloud | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |

The Thunderbird features named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| feat:import_export | 2 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:encryption | 2 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |
| feat:junk | 2 | `▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁` |
| feat:printing | 1 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| feat:filters | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁` |
| feat:attachments | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁` |

The protocols named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| proto:smtp | 1 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:imap | 1 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| proto:pop | 1 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

The operating systems named most often were:

| Value | Questions | Count per day |
|:--|--:|:--|
| os:android | 32 | `▁▃▃▆█▁▃▆▆▃▆▁▁▆▁▃▁▆▁▃▃▁▁▆█▃▃▃▁▁▆` |
| os:other | 2 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| os:windows | 2 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |


</details>

---

The tool ran its detectors at daily, weekly and monthly grain. A weekly period counts toward August 2026 when its week overlaps the month. Version×cause needs a known Thunderbird version, which the data carries only from 2026-02 onward. Cause-level uses all history. The full spike tables are in `PROJECT1/android-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`.
