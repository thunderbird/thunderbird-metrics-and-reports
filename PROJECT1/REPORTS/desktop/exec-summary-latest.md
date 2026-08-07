---
layout: base
title: "2026-07 exec summary: Thunderbird Desktop support spikes"
---

# July 2026 — Thunderbird Desktop support spikes

_Executive summary · **2026-07** · 731 questions · regenerated 2026-08-07 05:57 UTC · no AI (regex + traditional stats)_

## ✅ July 2026 was clean

**No spike cleared threshold at any grain.** No provider outage, no protocol surge, no AV breakage, and no release regression in July 2026.


| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| **version×cause** (release regressions) | 0 | 0 | 0 |
| **cause-level** (provider · protocol · AV) | 0 | 0 | 0 |

- **Volume:** 731 questions (`▆▇▅▆▄▇▇▆▇▆▄▃▇▇▄▅▄▅▄▇▆▅█▆▃▇▇▆▆▅▇` by day), 226 (31%) carry a cause tag
- **Answered (non-creator):** 600/731 (82%) · median first answer 3.6h
- **Release-adoption version spikes:** 15 (expected after a release — not incidents; collapsed below)

> ⏱ **Spike timing lags the incident.** A spike dates when users *piled in*, typically days after onset and often near resolution. Treat these as pain-cluster / triage signals, not real-time detection.

> 🔄 **This verdict is not frozen when the month ends.** Lift is measured against each cause's rate across all history, so later questions shift a closed month's expected values and rows can cross the threshold in either direction; answered-% keeps firming up as late answers land. That is why this page regenerates daily — and because each day's version is committed, `git log -p` on this file shows exactly how the verdict evolved.

<details markdown="1">
<summary><strong>🔍 Near misses (within ~25% of threshold)</strong> — 4 rows</summary>

Clusters the same detectors flag at **0.75× the thresholds** (i.e. within ~25% of firing) but which did NOT clear the real ones. Not incidents — context, so that “clean” is not confused with “quiet”.

**Version × cause**

| Grain | Lift | When | Version × Cause | Qs | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| daily | 2.8× | 2026-07-02 | v152 × proto:imap | 4 | ⚠️ 50% ans · 7.6h | [1590718](https://support.mozilla.org/questions/1590718 "Accidentally moved IMAP Gmail label to Local Folders - Emails disappeared, Local") [1590790](https://support.mozilla.org/questions/1590790 "Thunderbird and GoDaddy account") [1590808](https://support.mozilla.org/questions/1590808 "Forwarded attachments disappear after first IMAP draft save and subsequent saves") [1590848](https://support.mozilla.org/questions/1590848 "Continue to have ＂Authentication Required＂ POPup errors at startup.") |
| weekly | 2.8× | 2026-07-27 | v153 × m:comcast | 4 | 75% ans · 5.4h | [1595937](https://support.mozilla.org/questions/1595937 "Need help recovering my profile from a zip file") [1595941](https://support.mozilla.org/questions/1595941 "Why can't Thunderbird use new yahoo email platform for Comcast on MacBook Air?") [1596164](https://support.mozilla.org/questions/1596164 "") [1596297](https://support.mozilla.org/questions/1596297 "") |
| weekly | 2.8× | 2026-07-06 | v152 × proto:oauth | 5 | 80% ans · 5.4h | [1591762](https://support.mozilla.org/questions/1591762 "Even with verions 152.01, Oauth for smtp through Yahoo.com is not an available c") [1591813](https://support.mozilla.org/questions/1591813 "Oauth challenge never appears") [1591979](https://support.mozilla.org/questions/1591979 "Outlook: OAuth Authentication failure with IMAP") [1592379](https://support.mozilla.org/questions/1592379 "Gmail oauth gives Authentication failure after restarting Thunderbird") [1592479](https://support.mozilla.org/questions/1592479 "cannot set OAuth authentication method in Thunderbird 152.0.1") |
| weekly | 2.6× | 2026-07-06 | v140 × proto:smtp | 5 | 100% ans · 6.1h | [1591795](https://support.mozilla.org/questions/1591795 "Impossibile inviare messaggi") [1591885](https://support.mozilla.org/questions/1591885 "Can't find outgoing server after login following Win 11 sleeps") [1591986](https://support.mozilla.org/questions/1591986 "After the last Thunderbird update I cannot send e-mails but still receive emails") [1592019](https://support.mozilla.org/questions/1592019 "IMAP, SMTP и POP3") [1592468](https://support.mozilla.org/questions/1592468 "I have problems with my Orcon emails and they say it is Thunderbird.") |


</details>

---

## All July 2026 detail

<details markdown="1">
<summary><strong>🚨 Version × cause spikes</strong> — 0 rows</summary>

_None._

</details>

<details markdown="1">
<summary><strong>📮 Cause-level spikes (provider · protocol · AV)</strong> — 0 rows</summary>

_None._

</details>

<details markdown="1">
<summary><strong>📦 Release-adoption version/OS spikes (not incidents)</strong> — 15 rows</summary>

Version and OS are **filters, not causes** — a bare version spike is release adoption, not a regression. Listed for manual checking only.

| Grain | Rise | When | Dimension | Value | Qs | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | **3.1×** | 2026-07-01 | tb_version_major | 152 | 11 [1590558](https://support.mozilla.org/questions/1590558 "Chyba editoru při přeposílání (inline): Uzamčení dočasných souborů v Tempu při u") [1590593](https://support.mozilla.org/questions/1590593 "Too much disk space used by Thunderbird") | 3.5 |
| daily | **new** | 2026-07-23 | tb_version_major | 153 | 11 [1594355](https://support.mozilla.org/questions/1594355 "not sure i  lke the new version") [1594359](https://support.mozilla.org/questions/1594359 "How do I remove the English (US) dictionary from Thunderbird") | 0.0 |
| daily | **new** | 2026-07-24 | tb_version_major | 153 | 8 [1594604](https://support.mozilla.org/questions/1594604 "＂Current operation on Inbox did not succeed for yahoo account") [1594673](https://support.mozilla.org/questions/1594673 "Can't get back to inbox from local folders") | 0.0 |
| daily | **new** | 2026-07-26 | tb_version_major | 153 | 15 [1594896](https://support.mozilla.org/questions/1594896 "Lost my password") [1594901](https://support.mozilla.org/questions/1594901 "When opening Tbird 153.0, several servers give authentication errors") | 0.0 |
| daily | **new** | 2026-07-27 | tb_version_major | 153 | 11 [1595089](https://support.mozilla.org/questions/1595089 "add a yohoo email account") [1595090](https://support.mozilla.org/questions/1595090 "backup zip ,841mb ,will not import into thunderbird") | 0.0 |
| daily | **new** | 2026-07-28 | tb_version_major | 153 | 11 [1595265](https://support.mozilla.org/questions/1595265 "How to delete duplicate folders in three email acounts?") [1595273](https://support.mozilla.org/questions/1595273 "Adding a hotmail email account to Thunderbird 153.0 (64-bit) on Windows 11 Home ") | 0.0 |
| daily | **new** | 2026-07-30 | tb_version_major | 153 | 9 [1595713](https://support.mozilla.org/questions/1595713 "Why do deleted emails remain in my All Mail box?") [1595723](https://support.mozilla.org/questions/1595723 "Thunderbird editor line spacing") | 0.0 |
| daily | **new** | 2026-07-31 | tb_version_major | 153 | 18 [1595834](https://support.mozilla.org/questions/1595834 "Compacting folders progress bar") [1595845](https://support.mozilla.org/questions/1595845 "are you able to use thunderbird email without primary password") | 0.0 |
| monthly | **new** | 2026-07 | tb_version_major | 153 | 101 [1590618](https://support.mozilla.org/questions/1590618 "When a proper repository for .deb packages will be available?") [1590771](https://support.mozilla.org/questions/1590771 "Can't sign in to Thunderbird") | 0.0 |
| monthly | **422.0×** | 2026-07 | tb_version_major | 152 | 211 [1590558](https://support.mozilla.org/questions/1590558 "Chyba editoru při přeposílání (inline): Uzamčení dočasných souborů v Tempu při u") [1590593](https://support.mozilla.org/questions/1590593 "Too much disk space used by Thunderbird") | 0.5 |
| monthly | **3.1×** | 2026-07 | tb_version_major | 150 | 26 [1590853](https://support.mozilla.org/questions/1590853 "Have difficulty deleting emails") [1591057](https://support.mozilla.org/questions/1591057 "Thunderbird Error Message : Authentication Error :  Unable To Log in at Server. ") | 8.5 |
| weekly | **52.0×** | 2026-06-29 | tb_version_major | 152 | 78 [1590162](https://support.mozilla.org/questions/1590162 "") [1590178](https://support.mozilla.org/questions/1590178 "") | 1.5 |
| weekly | **26.0×** | 2026-07-06 | tb_version_major | 152 | 65 [1591418](https://support.mozilla.org/questions/1591418 "Pulsante ＂Esegui ora＂ del filtro messaggi non disponibile") [1591432](https://support.mozilla.org/questions/1591432 "code-uitvoering kan niet worden voortgezet") | 2.5 |
| weekly | **new** | 2026-07-20 | tb_version_major | 153 | 43 [1594201](https://support.mozilla.org/questions/1594201 "LỖi đăng nhập hotmail, email") [1594241](https://support.mozilla.org/questions/1594241 "Connection reset errors for CalDAV calendars when staritng Thunderbird") | 0.0 |
| weekly | **new** | 2026-07-27 | tb_version_major | 153 | 79 [1595089](https://support.mozilla.org/questions/1595089 "add a yohoo email account") [1595090](https://support.mozilla.org/questions/1595090 "backup zip ,841mb ,will not import into thunderbird") | 0.0 |

</details>

<details markdown="1">
<summary><strong>📈 July 2026 trends</strong> — 6 rows</summary>

**Top versions**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| v152 | 211 | `▆█▄▆▃▆▇▆▆▄▂▃▆█▄▃▁▆▃▅▆▂▂▁▁▂▁▂▂▁▁` |
| v140 | 186 | `▅▆▆▇▆▇▅▅█▅▄▂▅▅▅▅▆▄▅▇▅▅▅█▂▇▅▄▇▃▅` |
| v153 | 101 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▃▅▄▃▇▅▅▄▅█` |
| v150 | 26 | `▁▃▃▁▁▃█▁▆▃▆▁▃▁▁▃▁█▆▆▆▃▁▁▁▃▁▃▃▁▁` |
| v115 | 16 | `▆▃▁▁▁▃▁▁▆▁▁▃▁▃▁▁▆▁▁▁▁▁▆▁▁▁▁▁█▁▃` |
| v149 | 6 | `█▁█▁▁▁▁▁▁▁▁▁█▁▁█▁▁█▁▁▁▁▁▁▁█▁▁▁▁` |

**Top mail providers**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| m:gmail | 73 | `▃▅▅▅▆▂▃▅▅▆▅▁▁▆▁▃▅▅▂▁▁▅▂█▂█▃▅▂▆▃` |
| m:microsoftemail | 36 | `▁▅▃▂▂▁▁▃█▁▁▅▁▅▁▃▂▁▁▃▂▃▂▁▁▂▃▂▂▂▁` |
| m:yahooemail | 30 | `▃▅▃▁▆▃▃▃▃▃▁▃▃▁▁▁▁▃▃▁▃▁▁▅▁▅▃█▅▁▅` |
| m:comcast | 13 | `▁▅▁▅▁▁▁▅█▁▁▁▁▅▅▁▁▅▁▁▁▁▅▁▁▅▁▁▅▁█` |
| m:icloud | 6 | `▁▅▁▁▁▁▁█▁▁▁▁▅▁▁▁▁▁▅▁▁▁▁▁▁▅▁▁▁▁▁` |
| m:btinternet | 6 | `▁▁▁▁▁▁█▁▁█▁▁▁▁▁█▁▁▁▁█▁█▁▁▁▁▁▁█▁` |

**Top protocols**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| proto:imap | 56 | `▂▇▄▄▂▅▄▄█▁▁▄▂▄▂▂▂█▁▄▄▄▇▁▁▅▅▂▄▁▄` |
| proto:pop | 42 | `▁▃▃▅█▅█▅▅▁▁▃▅▁▃▁▁█▅▁▃▃▃▅▃▁▃▆▁▃▆` |
| proto:smtp | 35 | `▂▂▂▁▂▁▄▇█▁▁▂▁▂▄▂▁▁▂▂█▄▁▁▂▂▂▁▂▂▂` |
| proto:oauth | 20 | `▁▅▁▅▁▁▁██▁▅▅▅▅▁▅▅▁▁▁█▁▁▁▅█▅█▁▁▁` |
| proto:caldav | 3 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁█▁█▁▁▁▁▁▁▁▁▁` |
| proto:ews | 1 | `▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

**Top antivirus**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| av:norton | 3 | `▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁█` |
| av:bitdefender | 2 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:eset | 2 | `▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |
| av:avast | 2 | `▁▁▁▁▁▁▁█▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| av:defender | 2 | `▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█` |
| av:mcafee | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |

**OS mix (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| os:windows | 589 | `▅▆▅▅▄▆▇▆▇▅▄▃▇▇▄▅▄▅▄▇▇▅█▆▂▆▇▆▆▄█` |
| os:linux | 61 | `▇▅▆▁▁▁▃▃▂▂▁▁▅▂▁▃▅▂▂▃▁▅▇▁▃█▅▆▃▅▃` |
| os:macos | 45 | `▂█▁▄▁█▁▅▂▄▂▄▄▄▄▁▂▅▁▄▁▂▄▄▁▁▂▁▅▂▂` |
| os:other | 11 | `▅▅█▅▁▁▁▁▁▅▁▁▁▅▁▅▁▁▁▁▁▅▁▅▁▁▅▁▁▁▁` |
| os:android | 7 | `█▁▁▁█▁█▁██▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |

**macOS releases (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| macos:tahoe | 5 | `▁█▁▁▁▁▁▁▁▁▁▁▁▁▅▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁` |
| macos:sequoia | 2 | `▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁` |
| macos:sonoma | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sierra | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |
| macos:monterey | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁` |


</details>

---

_Detectors run at daily / weekly / monthly grain; a weekly period is included when its week overlaps July 2026. Version×cause requires a known version, which is only populated from 2026-02 onward; cause-level uses all history. Full spike CSVs: `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`._
