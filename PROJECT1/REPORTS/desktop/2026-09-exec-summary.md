---
layout: base
title: "2026-09 exec summary: Thunderbird Desktop support spikes"
---

# September 2026 — Thunderbird Desktop support spikes

_Executive summary · **2026-09** · 327 questions · regenerated 2026-09-10 00:20 UTC · no AI (regex + traditional stats)_

## 🚨 September 2026: 9 spikes to investigate

**6 version×cause** (release regressions) and **3 cause-level** (provider / protocol / AV / feature) spike(s) cleared threshold. Detail is collapsed below.

> ⏳ **September 2026 is still in progress** — counts will grow.


| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| **version×cause** (release regressions) | 2 | 3 | 1 |
| **cause-level** (provider · protocol · AV · feature) | 0 | 3 | 0 |

- **Volume:** 327 questions (`▆█▇▆▄▄█▆▆` by day), 157 (48%) carry a cause tag
- **Answered (non-creator):** 236/327 (72%) · median first answer 3.5h
- **Release-adoption version spikes:** 15 (expected after a release — not incidents; collapsed below)

> ⏱ **Spike timing lags the incident.** A spike dates when users *piled in*, typically days after onset and often near resolution. Treat these as pain-cluster / triage signals, not real-time detection.

> 🔄 **This verdict is not frozen when the month ends.** Lift is measured against each cause's rate across all history, so later questions shift a closed month's expected values and rows can cross the threshold in either direction; answered-% keeps firming up as late answers land. That is why this page regenerates daily — and because each day's version is committed, `git log -p` on this file shows exactly how the verdict evolved.

<details markdown="1">
<summary><strong>🔍 Near misses (within ~25% of threshold)</strong> — 6 rows</summary>

Clusters the same detectors flag at **0.75× the thresholds** (i.e. within ~25% of firing) but which did NOT clear the real ones. Not incidents — context, so that “clean” is not confused with “quiet”.

**Version × cause**

| Grain | Lift | When | Version × Cause | Qs | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| weekly | 2.9× | 2026-09-07 | v153 × m:gmail | 6 | ⚠️ 33% ans · 5.7h | [1602816](https://support.mozilla.org/questions/1602816 "How can I get emails coming into the correct account and be able to send respons") [1602865](https://support.mozilla.org/questions/1602865 "I am being asked for ＂new password＂ when sending email and it doesn't recognise ") [1602984](https://support.mozilla.org/questions/1602984 "Emails not appearing in Thunderbird for days but appear in Outlook without delay") [1603033](https://support.mozilla.org/questions/1603033 "authentication errors") [1603075](https://support.mozilla.org/questions/1603075 "Inability to transfer Emails from one account in Thunderbird to another account ") [1603103](https://support.mozilla.org/questions/1603103 "Thunderbird Mail has 'stopped working'") |
| daily | 2.7× | 2026-09-01 | v154 × proto:imap | 4 | ⚠️ 25% ans · 7.2h | [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601534](https://support.mozilla.org/questions/1601534 "Thunderbird on Win11 will not send or receive emails") [1601629](https://support.mozilla.org/questions/1601629 "Login to inbound server fails") [1601635](https://support.mozilla.org/questions/1601635 "missing email from flders") |
| monthly | 2.7× | 2026-09 | v155 × feat:filters | 7 | 71% ans · 4.3h | [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") [1601955](https://support.mozilla.org/questions/1601955 "Are you aware of a bug since yesterday to handling of spam filters?") [1602361](https://support.mozilla.org/questions/1602361 "Message filters has gone crazy for last 2 days") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") [1602916](https://support.mozilla.org/questions/1602916 "message filters have stopped working.") +1 |
| weekly | 2.4× | 2026-08-31 | v155 × feat:junk | 5 | 100% ans · 4.4h | [1601955](https://support.mozilla.org/questions/1601955 "Are you aware of a bug since yesterday to handling of spam filters?") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder (bug2068847)") [1602105](https://support.mozilla.org/questions/1602105 "Why do ALL my new emails all go to a spam folder ?") [1602303](https://support.mozilla.org/questions/1602303 "All messages ending in spam folder thunderbird after update to snap ubuntu") [1602574](https://support.mozilla.org/questions/1602574 "can't find Junk folder") |
| monthly | 2.3× | 2026-09 | v155 × feat:junk | 8 | 88% ans · 4.4h | [1601955](https://support.mozilla.org/questions/1601955 "Are you aware of a bug since yesterday to handling of spam filters?") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder (bug2068847)") [1602105](https://support.mozilla.org/questions/1602105 "Why do ALL my new emails all go to a spam folder ?") [1602303](https://support.mozilla.org/questions/1602303 "All messages ending in spam folder thunderbird after update to snap ubuntu") [1602574](https://support.mozilla.org/questions/1602574 "can't find Junk folder") [1602839](https://support.mozilla.org/questions/1602839 "Suddenly all my emails are going to spam.") +2 |

**Cause-level**

| Grain | Rise | When | Cause | Qs | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.3× | 2026-09-07 | feat:filters | 8 | ⚠️ 50% ans · 0.8h | 3.5 | [1602761](https://support.mozilla.org/questions/1602761 "Version 155.0 64 bit -- filters now totally non selective.  Fires on all message") [1602768](https://support.mozilla.org/questions/1602768 "Can't get rid of an email (junk/spam) ever with the filter.  Keeps reocurring. B") [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602835](https://support.mozilla.org/questions/1602835 "Lost all email filters circa Aug. 4 (approx.) - emails impossible to use/control") [1602847](https://support.mozilla.org/questions/1602847 "Sharing Thunderbird Message filters across multiple computers") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") +2 |


</details>

---

## All September 2026 detail

<details markdown="1">
<summary><strong>🚨 Version × cause spikes</strong> — 6 rows</summary>

| Grain | Lift | When | Version × Cause | Qs | Served | Signal | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | **17.2×** | 2026-09-01 | v154 × feat:printing | 4 | 100% ans · 13.8h | recurring | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") |
| weekly | **10.4×** | 2026-08-31 | v154 × feat:printing | 8 | 100% ans · 4.7h | recurring | [1601286](https://support.mozilla.org/questions/1601286 "") [1601306](https://support.mozilla.org/questions/1601306 "") [1601367](https://support.mozilla.org/questions/1601367 "") [1601404](https://support.mozilla.org/questions/1601404 "") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") +2 |
| monthly | **9.6×** | 2026-09 | v154 × feat:printing | 5 | 100% ans · 5.0h | recurring | [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601564](https://support.mozilla.org/questions/1601564 "Can no longer highlight text in a .pdf being previewed in Thunderbird and Printi") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") [1602826](https://support.mozilla.org/questions/1602826 "When printing from Thunderbird, a white sheet is produced.") |
| daily | **4.1×** | 2026-09-07 | v155 × proto:pop | 4 | 75% ans · 5.2h | spreading | [1602660](https://support.mozilla.org/questions/1602660 "pop3 account creation error") [1602682](https://support.mozilla.org/questions/1602682 "Login to server pop3.virginmedia.com with username ******* failed") [1602703](https://support.mozilla.org/questions/1602703 "Thunderbird freezes downloading messages when it reaches a message from aliexpre") [1602714](https://support.mozilla.org/questions/1602714 "Is syncronization bidirectional with IMAP accounts?") |
| weekly | **4.0×** | 2026-09-07 | v155 × feat:filters | 4 | ⚠️ 50% ans · 2.4h | spreading | [1602820](https://support.mozilla.org/questions/1602820 "Email filter problem after update") [1602914](https://support.mozilla.org/questions/1602914 "Message filters screwed up in Thuderbird 155") [1602916](https://support.mozilla.org/questions/1602916 "message filters have stopped working.") [1603094](https://support.mozilla.org/questions/1603094 "Cuando bajo los correos estos no respetan la regla de filtro de mensaje y la may") |
| weekly | **3.8×** | 2026-08-31 | v154 × feat:attachments | 5 | 100% ans · 3.5h | spreading | [1601404](https://support.mozilla.org/questions/1601404 "") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") [1601583](https://support.mozilla.org/questions/1601583 "Kan bijlage niet meer printen in thunderbird") [1601835](https://support.mozilla.org/questions/1601835 "I have problems as I can not send attachments") |

</details>

<details markdown="1">
<summary><strong>📮 Cause-level spikes (provider · protocol · AV · feature)</strong> — 3 rows</summary>

| Grain | Rise | When | Cause | Qs | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | **8.7×** | 2026-08-31 | feat:printing | 13 | 100% ans · 4.3h | 1.5 | [1601286](https://support.mozilla.org/questions/1601286 "") [1601306](https://support.mozilla.org/questions/1601306 "") [1601321](https://support.mozilla.org/questions/1601321 "") [1601367](https://support.mozilla.org/questions/1601367 "") [1601387](https://support.mozilla.org/questions/1601387 "") [1601404](https://support.mozilla.org/questions/1601404 "") +7 |
| weekly | **3.6×** | 2026-08-31 | m:spectrum | 9 | 78% ans · 37.2h | 2.5 | [1601375](https://support.mozilla.org/questions/1601375 "") [1601442](https://support.mozilla.org/questions/1601442 "Correct Outgoing SMPT settings for IMAP") [1601623](https://support.mozilla.org/questions/1601623 "no access to Thunderbird email through Spectrum") [1601790](https://support.mozilla.org/questions/1601790 "Charter + pop, all new messages are going to the trash folder, not my inbox, and") [1601822](https://support.mozilla.org/questions/1601822 "trouble sending and receiving messages interfacing with Spectrum (locked duplica") [1602003](https://support.mozilla.org/questions/1602003 "Spectrum Emails are disappearing from my Thunderbird Inbox after downloading. Th") +3 |
| weekly | **3.4×** | 2026-08-31 | feat:attachments | 17 | 88% ans · 3.5h | 5.0 | [1601321](https://support.mozilla.org/questions/1601321 "") [1601387](https://support.mozilla.org/questions/1601387 "") [1601404](https://support.mozilla.org/questions/1601404 "") [1601493](https://support.mozilla.org/questions/1601493 "CANNOT SEND ATTACHMENTS OVER 36 MB") [1601512](https://support.mozilla.org/questions/1601512 "Stampa fogli bianchi gli allegati delle mail") [1601528](https://support.mozilla.org/questions/1601528 "Printen van bijlage in thunderbird lukt me niet meer") +11 |

</details>

<details markdown="1">
<summary><strong>📦 Release-adoption version/OS spikes (not incidents)</strong> — 15 rows</summary>

Version and OS are **filters, not causes** — a bare version spike is release adoption, not a regression. Listed for manual checking only.

| Grain | Rise | When | Dimension | Value | Qs | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | **11.3×** | 2026-09-01 | tb_version_major | 154 | 17 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 1.5 |
| daily | **new** | 2026-09-02 | tb_version_major | 155 | 13 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| daily | **new** | 2026-09-03 | tb_version_major | 155 | 19 [1601859](https://support.mozilla.org/questions/1601859 "My latest Thunderbird upgrade on Kubuntu 26.04 is marked as BETA 155.0") [1601864](https://support.mozilla.org/questions/1601864 "Thunderbird impazzito") | 0.0 |
| daily | **new** | 2026-09-04 | tb_version_major | 155 | 20 [1602082](https://support.mozilla.org/questions/1602082 "I did not receive all my folders when installing Thunderbird") [1602091](https://support.mozilla.org/questions/1602091 "All received emails are going to spam folder (bug2068847)") | 0.0 |
| daily | **new** | 2026-09-05 | tb_version_major | 155 | 11 [1602267](https://support.mozilla.org/questions/1602267 "Problems with incoming new mail") [1602271](https://support.mozilla.org/questions/1602271 "Mail coming to inbox is automatically rerouted to trash folder") | 0.0 |
| daily | **new** | 2026-09-06 | tb_version_major | 155 | 14 [1602429](https://support.mozilla.org/questions/1602429 "Cannot connect Thunderbird to Spectrum") [1602438](https://support.mozilla.org/questions/1602438 "Can I move my entire Mozilla Thunderbird from my old DELL PC to my new DELL PC?") | 0.0 |
| daily | **new** | 2026-09-07 | tb_version_major | 155 | 18 [1602611](https://support.mozilla.org/questions/1602611 "yahoo not populating email after password change") [1602653](https://support.mozilla.org/questions/1602653 "skupiny kontaktů Google") | 0.0 |
| daily | **new** | 2026-09-08 | tb_version_major | 155 | 14 [1602807](https://support.mozilla.org/questions/1602807 "Thunderbird sending all inbox messages to deleted (bug2068847)") [1602817](https://support.mozilla.org/questions/1602817 "I'm getting this message:   Unable to write the email to the mailbox. Make sure ") | 0.0 |
| daily | **new** | 2026-09-09 | tb_version_major | 155 | 17 [1602995](https://support.mozilla.org/questions/1602995 "All delete methods not working nor is new folder created") [1603051](https://support.mozilla.org/questions/1603051 "Da qualche giorno su windows 11 Thunderbird non si avvia e .＂non risponde＂. Ho p") | 0.0 |
| monthly | **new** | 2026-09 | tb_version_major | 154 | 38 [1601433](https://support.mozilla.org/questions/1601433 "Uable to add new account over one that's been hacked.") [1601478](https://support.mozilla.org/questions/1601478 "Thunderbird non si carica su Apple Tahoe 26.6.2") | 0.0 |
| monthly | **new** | 2026-09 | tb_version_major | 155 | 126 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| monthly | **20.0×** | 2026-09 | tb_version_major | 153 | 50 [1601441](https://support.mozilla.org/questions/1601441 "Emails not downloading") [1601614](https://support.mozilla.org/questions/1601614 "How do I change my user name in the login in for Thunderbird?") | 2.5 |
| weekly | **new** | 2026-08-31 | tb_version_major | 155 | 77 [1601641](https://support.mozilla.org/questions/1601641 "no recibos los correos") [1601684](https://support.mozilla.org/questions/1601684 "Problemi filtro  ricerca mail") | 0.0 |
| weekly | **112.0×** | 2026-08-31 | tb_version_major | 154 | 56 [1601271](https://support.mozilla.org/questions/1601271 "") [1601273](https://support.mozilla.org/questions/1601273 "") | 0.5 |
| weekly | **new** | 2026-09-07 | tb_version_major | 155 | 49 [1602611](https://support.mozilla.org/questions/1602611 "yahoo not populating email after password change") [1602653](https://support.mozilla.org/questions/1602653 "skupiny kontaktů Google") | 0.0 |

</details>

<details markdown="1">
<summary><strong>📈 September 2026 trends</strong> — 7 rows</summary>

**Top versions**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| v155 | 126 | `▁▆██▅▆▇▆▇` |
| v153 | 50 | `▃▇▇▄▂▄▆▆█` |
| v154 | 38 | `█▄▃▂▁▁▂▂▁` |
| v140 | 21 | `██▆▅▃▁▅▅▆` |
| v115 | 11 | `▁▁▁▃▃▃█▅▅` |
| v150 | 5 | `▁▁▁▅█▁▁▅▅` |

**Top mail providers**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| m:gmail | 27 | `▃▄▄▆▁▃▂█▅` |
| m:yahooemail | 16 | `▁▃▆█▁▃███` |
| m:microsoftemail | 14 | `▃▆▃▁▁▁▃██` |
| m:spectrum | 10 | `██▅▁▅█▁▅▅` |
| m:virginmedia | 4 | `▃▁▁▁▁▁█▁▁` |
| m:att | 3 | `██▁▁▁▁█▁▁` |

**Top feature areas**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| feat:attachments | 14 | `▇█▂▄▄▁▁▁▁` |
| feat:filters | 11 | `▁▂▂▁▂▁▄█▂` |
| feat:junk | 11 | `▁▅▅█▅▅██▅` |
| feat:printing | 8 | `█▃▁▃▃▁▁▃▁` |
| feat:import_export | 5 | `▁█▁▁▁▃▃▁▁` |
| feat:search | 3 | `██▁▁▁▁▁█▁` |

**Top protocols**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| proto:imap | 32 | `▆▆▅▂▂▅█▂▅` |
| proto:smtp | 17 | `▃█▆█▁▆▃▆█` |
| proto:pop | 15 | `▂▅▁▂▂▂█▃▁` |
| proto:oauth | 10 | `▃▃▁█▃▁▁▃▅` |
| proto:carddav | 1 | `▁▁█▁▁▁▁▁▁` |
| proto:caldav | 1 | `▁▁█▁▁▁▁▁▁` |

**Top antivirus**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| av:norton | 2 | `█▁▁█▁▁▁▁▁` |
| av:bitdefender | 2 | `▁▁▁█▁▁█▁▁` |
| av:defender | 2 | `▁▁▁█▁▁▁▁▁` |
| av:avast | 1 | `█▁▁▁▁▁▁▁▁` |
| av:malwarebytes | 1 | `█▁▁▁▁▁▁▁▁` |
| av:surfshark | 1 | `▁▁▁▁▁▁█▁▁` |

**OS mix (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| os:windows | 273 | `▆██▆▄▅█▆▅` |
| os:linux | 20 | `▁▂▄█▂▁▄▇█` |
| os:macos | 19 | `▅▃▃▅▃▅▆▆█` |
| os:other | 4 | `█▁▁▁▁▁▃▁▁` |
| os:android | 2 | `▁█▁▁▁▁▁▁▁` |

**macOS releases (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| macos:tahoe | 3 | `█▅▁▁▁▁▁▁▁` |
| macos:sequoia | 2 | `▁▁▁▁▁▁█▁█` |


</details>

---

_Detectors run at daily / weekly / monthly grain; a weekly period is included when its week overlaps September 2026. Version×cause requires a known version, which is only populated from 2026-02 onward; cause-level uses all history. Full spike CSVs: `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`._
