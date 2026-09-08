---
layout: base
title: "2026-09 exec summary: Thunderbird Desktop support spikes"
---

# September 2026 — Thunderbird Desktop support spikes

_Executive summary · **2026-09** · 260 questions · regenerated 2026-09-08 05:34 UTC · no AI (regex + traditional stats)_

## 🚨 September 2026: 4 spikes to investigate

**3 version×cause** (release regressions) and **1 cause-level** (provider / protocol / AV) spike(s) cleared threshold. Detail is collapsed below.

> ⏳ **September 2026 is still in progress** — counts will grow.


| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| **version×cause** (release regressions) | 1 | 2 | 0 |
| **cause-level** (provider · protocol · AV) | 0 | 1 | 0 |

- **Volume:** 260 questions (`▆█▇▆▄▄█▂` by day), 83 (32%) carry a cause tag
- **Answered (non-creator):** 195/260 (75%) · median first answer 3.5h
- **Release-adoption version spikes:** 13 (expected after a release — not incidents; collapsed below)

> ⏱ **Spike timing lags the incident.** A spike dates when users *piled in*, typically days after onset and often near resolution. Treat these as pain-cluster / triage signals, not real-time detection.

> 🔄 **This verdict is not frozen when the month ends.** Lift is measured against each cause's rate across all history, so later questions shift a closed month's expected values and rows can cross the threshold in either direction; answered-% keeps firming up as late answers land. That is why this page regenerates daily — and because each day's version is committed, `git log -p` on this file shows exactly how the verdict evolved.

<details markdown="1">
<summary><strong>🔍 Near misses (within ~25% of threshold)</strong> — 1 row</summary>

Clusters the same detectors flag at **0.75× the thresholds** (i.e. within ~25% of firing) but which did NOT clear the real ones. Not incidents — context, so that “clean” is not confused with “quiet”.

**Version × cause**

| Grain | Lift | When | Version × Cause | Qs | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| daily | 2.7× | 2026-09-01 | v154 × proto:imap | 4 | ⚠️ 25% ans · 7.2h | [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601534](https://support.mozilla.org/questions/1601534 "Thunderbird on Win11 will not send or receive emails") [1601629](https://support.mozilla.org/questions/1601629 "Login to inbound server fails") [1601635](https://support.mozilla.org/questions/1601635 "missing email from flders") |


</details>

---

## All September 2026 detail

<details markdown="1">
<summary><strong>🚨 Version × cause spikes</strong> — 3 rows</summary>

| Grain | Lift | When | Version × Cause | Qs | Served | Signal | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | **4.0×** | 2026-09-07 | v155 × proto:pop | 4 | 75% ans · 5.2h | spreading | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |
| weekly | **3.6×** | 2026-09-07 | v155 × m:yahooemail | 4 | ⚠️ 50% ans · 7.3h | spreading | [1602611](https://support.mozilla.org/questions/1602611 "yahoo not populating email after password change") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") |
| weekly | **3.4×** | 2026-09-07 | v155 × proto:pop | 4 | 75% ans · 5.2h | new | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |

</details>

<details markdown="1">
<summary><strong>📮 Cause-level spikes (provider · protocol · AV)</strong> — 1 row</summary>

| Grain | Rise | When | Cause | Qs | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | **3.6×** | 2026-08-31 | m:spectrum | 9 | 78% ans · 37.2h | 2.5 | [1601375](https://support.mozilla.org/questions/1601375 "") [1601442](https://support.mozilla.org/questions/1601442 "Correct Outgoing SMPT settings for IMAP") [1601623](https://support.mozilla.org/questions/1601623 "no access to Thunderbird email through Spectrum") [1601790](https://support.mozilla.org/questions/1601790 "Charter + pop, all new messages are going to the trash folder, not my inbox, and") [1601822](https://support.mozilla.org/questions/1601822 "trouble sending and receiving messages interfacing with Spectrum (locked duplica") [1602003](https://support.mozilla.org/questions/1602003 "Spectrum Emails are disappearing from my Thunderbird Inbox after downloading. Th") +3 |

</details>

<details markdown="1">
<summary><strong>📦 Release-adoption version/OS spikes (not incidents)</strong> — 13 rows</summary>

Version and OS are **filters, not causes** — a bare version spike is release adoption, not a regression. Listed for manual checking only.

| Grain | Rise | When | Dimension | Value | Qs | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | **11.3×** | 2026-09-01 | tb_version_major | 154 | 17 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 1.5 |
| daily | **new** | 2026-09-02 | tb_version_major | 155 | 13 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| daily | **new** | 2026-09-03 | tb_version_major | 155 | 19 [1601859](https://support.mozilla.org/questions/1601859 "My latest Thunderbird upgrade on Kubuntu 26.04 is marked as BETA 155.0") [1601864](https://support.mozilla.org/questions/1601864 "Thunderbird impazzito") | 0.0 |
| daily | **new** | 2026-09-04 | tb_version_major | 155 | 20 [1602082](https://support.mozilla.org/questions/1602082 "I did not receive all my folders when installing Thunderbird") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder") | 0.0 |
| daily | **new** | 2026-09-05 | tb_version_major | 155 | 11 [1602267](https://support.mozilla.org/questions/1602267 "Problems with incoming new mail") [1602271](https://support.mozilla.org/questions/1602271 "Mail coming to inbox is automatically rerouted to trash folder") | 0.0 |
| daily | **new** | 2026-09-06 | tb_version_major | 155 | 14 [1602429](https://support.mozilla.org/questions/1602429 "Cannot connect Thunderbird to Spectrum") [1602438](https://support.mozilla.org/questions/1602438 "Can I move my entire Mozilla Thunderbird from my old DELL PC to my new DELL PC?") | 0.0 |
| daily | **new** | 2026-09-07 | tb_version_major | 155 | 18 [1602611](https://support.mozilla.org/questions/1602611 "yahoo not populating email after password change") [1602653](https://support.mozilla.org/questions/1602653 "skupiny kontaktů Google") | 0.0 |
| monthly | **new** | 2026-09 | tb_version_major | 154 | 36 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 0.0 |
| monthly | **new** | 2026-09 | tb_version_major | 155 | 98 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| monthly | **18.0×** | 2026-09 | tb_version_major | 153 | 36 [1601441](https://support.mozilla.org/questions/1601441 "Emails not downloading") [1601614](https://support.mozilla.org/questions/1601614 "How do I change my user name in the login in for Thunderbird?") | 2.0 |
| weekly | **new** | 2026-08-31 | tb_version_major | 155 | 77 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| weekly | **112.0×** | 2026-08-31 | tb_version_major | 154 | 56 [1601271](https://support.mozilla.org/questions/1601271 "") [1601273](https://support.mozilla.org/questions/1601273 "") | 0.5 |
| weekly | **new** | 2026-09-07 | tb_version_major | 155 | 21 [1602611](https://support.mozilla.org/questions/1602611 "yahoo not populating email after password change") [1602653](https://support.mozilla.org/questions/1602653 "skupiny kontaktů Google") | 0.0 |

</details>

<details markdown="1">
<summary><strong>📈 September 2026 trends</strong> — 6 rows</summary>

**Top versions**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| v155 | 98 | `▁▆██▅▆▇▂` |
| v154 | 36 | `█▄▃▂▁▁▂▁` |
| v153 | 36 | `▄██▅▂▅▆▃` |
| v140 | 16 | `██▆▅▃▁▅▁` |
| v115 | 7 | `▁▁▁▃▃▃█▁` |
| v128 | 3 | `▁███▁▁▁▁` |

**Top mail providers**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| m:gmail | 17 | `▄▅▅█▁▄▂▂` |
| m:yahooemail | 12 | `▁▃▆█▁▃█▆` |
| m:spectrum | 8 | `██▅▁▅█▁▁` |
| m:microsoftemail | 6 | `▃█▃▁▁▁▃▁` |
| m:virginmedia | 4 | `▃▁▁▁▁▁█▁` |
| m:att | 3 | `██▁▁▁▁█▁` |

**Top protocols**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| proto:imap | 27 | `▆▆▅▂▂▅█▁` |
| proto:pop | 13 | `▂▅▁▂▂▂█▁` |
| proto:smtp | 12 | `▃█▆█▁▆▃▁` |
| proto:oauth | 7 | `▃▃▁█▃▁▁▁` |
| proto:carddav | 1 | `▁▁█▁▁▁▁▁` |
| proto:caldav | 1 | `▁▁█▁▁▁▁▁` |

**Top antivirus**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| av:bitdefender | 2 | `▁▁▁█▁▁█▁` |
| av:defender | 2 | `▁▁▁█▁▁▁▁` |
| av:avast | 1 | `█▁▁▁▁▁▁▁` |
| av:malwarebytes | 1 | `█▁▁▁▁▁▁▁` |
| av:norton | 1 | `█▁▁▁▁▁▁▁` |
| av:surfshark | 1 | `▁▁▁▁▁▁█▁` |

**OS mix (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| os:windows | 225 | `▆██▆▄▅█▂` |
| os:macos | 12 | `▆▃▃▆▃▆█▁` |
| os:linux | 11 | `▁▂▄█▂▁▄▁` |
| os:other | 4 | `█▁▁▁▁▁▃▁` |
| os:android | 2 | `▁█▁▁▁▁▁▁` |

**macOS releases (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| macos:tahoe | 3 | `█▅▁▁▁▁▁▁` |
| macos:sequoia | 1 | `▁▁▁▁▁▁█▁` |


</details>

---

_Detectors run at daily / weekly / monthly grain; a weekly period is included when its week overlaps September 2026. Version×cause requires a known version, which is only populated from 2026-02 onward; cause-level uses all history. Full spike CSVs: `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`._
