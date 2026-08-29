---
layout: base
title: "2026-08 exec summary: Thunderbird Desktop support spikes"
---

# August 2026 — Thunderbird Desktop support spikes

_Executive summary · **2026-08** · 845 questions · regenerated 2026-08-29 05:31 UTC · no AI (regex + traditional stats)_

## 🚨 August 2026: 9 spikes to investigate

**6 version×cause** (release regressions) and **3 cause-level** (provider / protocol / AV) spike(s) cleared threshold. Detail is collapsed below.

> ⏳ **August 2026 is still in progress** — counts will grow.


| Detector | daily | weekly | monthly |
|:--|--:|--:|--:|
| **version×cause** (release regressions) | 4 | 2 | 0 |
| **cause-level** (provider · protocol · AV) | 0 | 3 | 0 |

- **Volume:** 845 questions (`▄▃▅▅▅▅▆▆▄▅▄▅▅▅▄▅▅▆▄▅▆▅▄▆▅█▆▅▁` by day), 255 (30%) carry a cause tag
- **Answered (non-creator):** 613/845 (73%) · median first answer 2.6h
- **Release-adoption version spikes:** 26 (expected after a release — not incidents; collapsed below)

> ⏱ **Spike timing lags the incident.** A spike dates when users *piled in*, typically days after onset and often near resolution. Treat these as pain-cluster / triage signals, not real-time detection.

> 🔄 **This verdict is not frozen when the month ends.** Lift is measured against each cause's rate across all history, so later questions shift a closed month's expected values and rows can cross the threshold in either direction; answered-% keeps firming up as late answers land. That is why this page regenerates daily — and because each day's version is committed, `git log -p` on this file shows exactly how the verdict evolved.

<details markdown="1">
<summary><strong>🔍 Near misses (within ~25% of threshold)</strong> — 5 rows</summary>

Clusters the same detectors flag at **0.75× the thresholds** (i.e. within ~25% of firing) but which did NOT clear the real ones. Not incidents — context, so that “clean” is not confused with “quiet”.

**Version × cause**

| Grain | Lift | When | Version × Cause | Qs | Served | Example questions |
|:--|--:|:--|:--|--:|:--|:--|
| weekly | 2.9× | 2026-07-27 | v153 × m:comcast | 4 | 75% ans · 5.4h | [1595937](https://support.mozilla.org/questions/1595937 "") [1595941](https://support.mozilla.org/questions/1595941 "") [1596164](https://support.mozilla.org/questions/1596164 "With version 153: Unable to send from gmail account.  And cannot create a new gm") [1596297](https://support.mozilla.org/questions/1596297 "Trying to set APP Password to connect with Yahoo Mail conversion at Comcast.") |
| daily | 2.7× | 2026-08-18 | v153 × m:gmail | 6 | ⚠️ 17% ans · 0.7h | [1598887](https://support.mozilla.org/questions/1598887 "＂Authentification Failure while connecting to server imap.gmail.com＂ How do I re") [1598903](https://support.mozilla.org/questions/1598903 "emails from senders with gmail accounts not being downloaded") [1598918](https://support.mozilla.org/questions/1598918 "Thunderbird has stopped receiving email") [1598928](https://support.mozilla.org/questions/1598928 "Thunderbird PC app and Android both loading and syncing incoming email and all f") [1598949](https://support.mozilla.org/questions/1598949 "Unable to sync address book with Gmail") [1598950](https://support.mozilla.org/questions/1598950 "Unable to sync address book with Gmail (locked duplicate)") |
| daily | 2.4× | 2026-08-03 | v153 × m:microsoftemail | 4 | 100% ans · 15.7h | [1596378](https://support.mozilla.org/questions/1596378 "cartelle cscomparse account posta hotmail") [1596433](https://support.mozilla.org/questions/1596433 "Mijn agenda op Thunderbird.") [1596442](https://support.mozilla.org/questions/1596442 "Aanmelden bij outlook met mailadres dat hoofdletters bevat is niet meer mogelijk") [1596497](https://support.mozilla.org/questions/1596497 "Thunderbird cannot log-in to my mail accounts") |

**Cause-level**

| Grain | Rise | When | Cause | Qs | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | 2.5× | 2026-08-03 | m:yahooemail | 14 | 79% ans · 3.3h | 5.5 | [1596455](https://support.mozilla.org/questions/1596455 "Recuprar la carpeta Bulk") [1596495](https://support.mozilla.org/questions/1596495 "Are thunderbird's saved logins the same logins Yahoo recognizes and accepts? Tbi") [1596497](https://support.mozilla.org/questions/1596497 "Thunderbird cannot log-in to my mail accounts") [1596560](https://support.mozilla.org/questions/1596560 "Thunderbirdサーバーにログインできなくなりました。") [1596676](https://support.mozilla.org/questions/1596676 "preventing a 2nd email  address from popping up in thunderbird") [1596708](https://support.mozilla.org/questions/1596708 "TB doesn't like to connect to my Comcast internet provider sometime.") +8 |
| monthly | 2.4× | 2026-08 | m:spectrum | 25 | 68% ans · 3.7h | 10.5 | [1596316](https://support.mozilla.org/questions/1596316 "Thunderbird 1 of 7  email account stopped working from the Provider Spectrum and") [1596807](https://support.mozilla.org/questions/1596807 "Receiving, deleting, and sending messages is extremely slow for 1 of 2 users on ") [1597319](https://support.mozilla.org/questions/1597319 "thunderbird not able to access mail.twc.com") [1597495](https://support.mozilla.org/questions/1597495 "NO longer have Spectrum as email provider but need to preserve emails .") [1597964](https://support.mozilla.org/questions/1597964 "Roadrunner / TWC IMAP settings") [1597972](https://support.mozilla.org/questions/1597972 "Thunderbird tells me that the spectrum servers won't accept my password") +19 |


</details>

---

## All August 2026 detail

<details markdown="1">
<summary><strong>🚨 Version × cause spikes</strong> — 6 rows</summary>

| Grain | Lift | When | Version × Cause | Qs | Served | Signal | Example questions |
|:--|--:|:--|:--|--:|:--|:--|:--|
| daily | **3.5×** | 2026-08-14 | v153 × proto:pop | 4 | 100% ans · 8.0h | recurring | [1598311](https://support.mozilla.org/questions/1598311 "Thunderbird went goofy for multiple gmail accounts - deleted email does not show") [1598314](https://support.mozilla.org/questions/1598314 "Email from Roadrunner.com does not show but server test works") [1598327](https://support.mozilla.org/questions/1598327 "Unable to receive e-mail") [1598357](https://support.mozilla.org/questions/1598357 "Recently Unable to send (SMTP) from Thunderbird from Cox.com (now thru Yahoo).") |
| weekly | **3.4×** | 2026-08-17 | v154 × m:spectrum | 4 | 100% ans · 4.2h | spreading | [1599683](https://support.mozilla.org/questions/1599683 "Suddenly not receiving email") [1599738](https://support.mozilla.org/questions/1599738 "Thunderbird is not receiving in coming mail from Charter") [1599818](https://support.mozilla.org/questions/1599818 "Thunderbird not connecting to server.  Cannot send or receive emails.") [1599874](https://support.mozilla.org/questions/1599874 "Ability to send emails using roadrunner (mail.twc.com) account") |
| daily | **3.3×** | 2026-08-13 | v153 × proto:pop | 4 | 100% ans · 1.2h | recurring | [1598091](https://support.mozilla.org/questions/1598091 "thunderbird has stopped receiving emails from century link") [1598146](https://support.mozilla.org/questions/1598146 "Can't access my account") [1598151](https://support.mozilla.org/questions/1598151 "How to set up automatic email forwarding from Thunderbird to Gmail") [1598175](https://support.mozilla.org/questions/1598175 "Thunderbird won't download email messages from Yahoo (formerly Cox) account") |
| daily | **3.3×** | 2026-08-10 | v153 × proto:pop | 4 | 75% ans · 1.1h | spreading | [1597551](https://support.mozilla.org/questions/1597551 "Thunderbird POP stopped retrieving email from one mail box, No error message") [1597571](https://support.mozilla.org/questions/1597571 "Email collection over pop failed on one account, server settings rejected when I") [1597638](https://support.mozilla.org/questions/1597638 "How logging onto wowway with old password?") [1597683](https://support.mozilla.org/questions/1597683 "Hotmail personal account: IMAP OAuth2 works but SMTP OAuth2 fails with message: ") |
| daily | **3.2×** | 2026-08-04 | v153 × m:microsoftemail | 5 | 100% ans · 0.8h | spreading | [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") [1596591](https://support.mozilla.org/questions/1596591 "email not collegament to app thunderbird pc (email outlook)") [1596602](https://support.mozilla.org/questions/1596602 "Import from Outlook (M365) Mac OS to Thunderbird?") [1596606](https://support.mozilla.org/questions/1596606 "Cannot import contacts from outlook 2016") |
| weekly | **3.0×** | 2026-08-17 | v153 × m:spectrum | 5 | 80% ans · 10.1h | spreading | [1598964](https://support.mozilla.org/questions/1598964 "Thunderbird connection resets when using Mozilla VPN.") [1599516](https://support.mozilla.org/questions/1599516 "When trying to send an email it will not go") [1599553](https://support.mozilla.org/questions/1599553 "I can't receive or send emails in thunderbird.") [1599823](https://support.mozilla.org/questions/1599823 "After latest update can't connect to spectrum email") [1599836](https://support.mozilla.org/questions/1599836 "all INBOX emails disappeared--no luck repairing folder or deleting INBOX.msf but") |

</details>

<details markdown="1">
<summary><strong>📮 Cause-level spikes (provider · protocol · AV)</strong> — 3 rows</summary>

| Grain | Rise | When | Cause | Qs | Served | Baseline | Example questions |
|:--|--:|:--|:--|--:|:--|--:|:--|
| weekly | **11.0×** | 2026-08-17 | m:spectrum | 11 | 91% ans · 6.5h | 1.0 | [1598964](https://support.mozilla.org/questions/1598964 "Thunderbird connection resets when using Mozilla VPN.") [1599516](https://support.mozilla.org/questions/1599516 "When trying to send an email it will not go") [1599553](https://support.mozilla.org/questions/1599553 "I can't receive or send emails in thunderbird.") [1599681](https://support.mozilla.org/questions/1599681 "I am unable to send and receive emails on two of my computers. I can do that onl") [1599683](https://support.mozilla.org/questions/1599683 "Suddenly not receiving email") [1599711](https://support.mozilla.org/questions/1599711 "I use to be able to get my email messages from Spectrum on Thunderbird, but now ") +5 |
| weekly | **4.7×** | 2026-08-24 | m:spectrum | 7 | ⚠️ 57% ans · 0.4h | 1.5 | [1600000](https://support.mozilla.org/questions/1600000 "Suddenly can't send/receive emails") [1600041](https://support.mozilla.org/questions/1600041 "I can receive but not send emails") [1600052](https://support.mozilla.org/questions/1600052 "Trouble connecting to my email provider Time Warner Corporation to send emails u") [1600103](https://support.mozilla.org/questions/1600103 "Cannot send or receive email.") [1600207](https://support.mozilla.org/questions/1600207 "Can't get into my Spectrum email account through Thunderbird") [1600663](https://support.mozilla.org/questions/1600663 "can no longer get my e-mail") +1 |
| weekly | **3.5×** | 2026-08-10 | m:yahooemail | 19 | 63% ans · 3.4h | 5.5 | [1597571](https://support.mozilla.org/questions/1597571 "Email collection over pop failed on one account, server settings rejected when I") [1597605](https://support.mozilla.org/questions/1597605 "I am still canot open my yahoo.co.uk email account? I have deleted the account f") [1597650](https://support.mozilla.org/questions/1597650 "why am i getting a pop-up window demanding that I agree to allow thunderbird mai") [1597665](https://support.mozilla.org/questions/1597665 "Yahoo IMAP Mailbox Reserved Loop: Bulk folder stuck inside Trash") [1597759](https://support.mozilla.org/questions/1597759 "Why is Yahoo_mail not updatuing in Thunderbird since two weeks?") [1597789](https://support.mozilla.org/questions/1597789 "Yahoo mail authentication failure after the newest update") +13 |

</details>

<details markdown="1">
<summary><strong>📦 Release-adoption version/OS spikes (not incidents)</strong> — 26 rows</summary>

Version and OS are **filters, not causes** — a bare version spike is release adoption, not a regression. Listed for manual checking only.

| Grain | Rise | When | Dimension | Value | Qs | Baseline |
|:--|--:|:--|:--|:--|:--|--:|
| daily | **new** | 2026-08-01 | tb_version_major | 153 | 13 [1596031](https://support.mozilla.org/questions/1596031 "why is thunderbird not working") [1596048](https://support.mozilla.org/questions/1596048 "thunderbrd version 153.0.1 64bit: some registered adress get filtered as spam th") | 0.0 |
| daily | **new** | 2026-08-02 | tb_version_major | 153 | 10 [1596185](https://support.mozilla.org/questions/1596185 "I can't send or receive emails using wifi") [1596191](https://support.mozilla.org/questions/1596191 "Events shift one hour earlier in calendar") | 0.0 |
| daily | **new** | 2026-08-03 | tb_version_major | 153 | 21 [1596331](https://support.mozilla.org/questions/1596331 "When a message must be Sent Later, where is the draft stored???") [1596345](https://support.mozilla.org/questions/1596345 "InsertSignature button moved from formatting toolbar to top toolbar after Thunde") | 0.0 |
| daily | **new** | 2026-08-04 | tb_version_major | 153 | 20 [1596545](https://support.mozilla.org/questions/1596545 "Microsoft Outlook authentication failure.") [1596547](https://support.mozilla.org/questions/1596547 "I just had a fake prompt to add a password to a website mimicking Thunderbird") | 0.0 |
| daily | **7.5×** | 2026-08-05 | tb_version_major | 153 | 15 [1596705](https://support.mozilla.org/questions/1596705 "Can't create or rename Inbox subfolders in Thunderbird") [1596708](https://support.mozilla.org/questions/1596708 "TB doesn't like to connect to my Comcast internet provider sometime.") | 2.0 |
| daily | **4.9×** | 2026-08-06 | tb_version_major | 153 | 22 [1596881](https://support.mozilla.org/questions/1596881 "Can no longer drag and drop email attachments from emails to folders after 153es") [1596896](https://support.mozilla.org/questions/1596896 "gmail linkage") | 4.5 |
| daily | **5.0×** | 2026-08-07 | os | os:linux | 10 [1597113](https://support.mozilla.org/questions/1597113 "i just need account to identify online access to verify my online social media d") [1597136](https://support.mozilla.org/questions/1597136 "Jak spravne nastavit thunderbird pro pop3?") | 2.0 |
| daily | **3.7×** | 2026-08-07 | tb_version_major | 153 | 22 [1597076](https://support.mozilla.org/questions/1597076 "Update to Thunderbird 153.0.2esr (32-bit) freezes up and locks.  SOLVED by 153.1") [1597080](https://support.mozilla.org/questions/1597080 "how many adresses can I have in a single Thunderbird email?") | 6.0 |
| daily | **new** | 2026-08-19 | tb_version_major | 154 | 8 [1599072](https://support.mozilla.org/questions/1599072 "Nelze zadat přihlašovací heslo") [1599085](https://support.mozilla.org/questions/1599085 "Unable to log in to my email account through the Thunderbird desktop application") | 0.0 |
| daily | **new** | 2026-08-20 | tb_version_major | 154 | 12 [1599228](https://support.mozilla.org/questions/1599228 "Asking for authorisation after deleting account") [1599257](https://support.mozilla.org/questions/1599257 "Print emails") | 0.0 |
| daily | **new** | 2026-08-21 | tb_version_major | 154 | 18 [1599422](https://support.mozilla.org/questions/1599422 "Sending e-mails does not work") [1599433](https://support.mozilla.org/questions/1599433 "Very slow to download and synchronize") | 0.0 |
| daily | **new** | 2026-08-22 | tb_version_major | 154 | 13 [1599566](https://support.mozilla.org/questions/1599566 "My Thunderbird is freezing up") [1599568](https://support.mozilla.org/questions/1599568 "Thunderbird is freezing up after a few minutes or when I try to select a folder.") | 0.0 |
| daily | **new** | 2026-08-23 | tb_version_major | 154 | 10 [1599762](https://support.mozilla.org/questions/1599762 "How do I  add my Outlook Calendar to TB 154 using Owl") [1599777](https://support.mozilla.org/questions/1599777 "mail indirmeyi çok yavaş yapıyor.nedeni nedir ? 1000 mb internet hızım var.") | 0.0 |
| daily | **new** | 2026-08-24 | tb_version_major | 154 | 19 [1599916](https://support.mozilla.org/questions/1599916 "Are you having problems with the program right now?") [1599944](https://support.mozilla.org/questions/1599944 "Transfer Thunderbird from PC to Laptop") | 0.0 |
| daily | **new** | 2026-08-25 | tb_version_major | 154 | 9 [1600116](https://support.mozilla.org/questions/1600116 "Account Passwords need frequent updating") [1600119](https://support.mozilla.org/questions/1600119 "Every time Thunderbird queries gmail, it starts downloading my hundreds of thous") | 0.0 |
| daily | **new** | 2026-08-26 | tb_version_major | 154 | 27 [1600375](https://support.mozilla.org/questions/1600375 "Varför är det så svårt att sortera mapparna i bokstavordning.") [1600387](https://support.mozilla.org/questions/1600387 "thunderbird pdf viewer") | 0.0 |
| daily | **new** | 2026-08-27 | tb_version_major | 154 | 17 [1600526](https://support.mozilla.org/questions/1600526 "Reply with Template option missing") [1600549](https://support.mozilla.org/questions/1600549 "I want to delete my account from the thunderbird server so that I can start fres") | 0.0 |
| daily | **new** | 2026-08-28 | tb_version_major | 154 | 17 [1600770](https://support.mozilla.org/questions/1600770 "I can't highlight words on attachments") [1600772](https://support.mozilla.org/questions/1600772 "thunderbird mail") | 0.0 |
| monthly | **new** | 2026-08 | tb_version_major | 154 | 154 [1596686](https://support.mozilla.org/questions/1596686 "Cannot print Pdf files from within Thunderbird") [1598813](https://support.mozilla.org/questions/1598813 "Missing SENT messages. Folder ＂greyed out＂") | 0.0 |
| monthly | **840.0×** | 2026-08 | tb_version_major | 153 | 420 [1596031](https://support.mozilla.org/questions/1596031 "why is thunderbird not working") [1596048](https://support.mozilla.org/questions/1596048 "thunderbrd version 153.0.1 64bit: some registered adress get filtered as spam th") | 0.5 |
| weekly | **new** | 2026-07-27 | tb_version_major | 153 | 79 [1595089](https://support.mozilla.org/questions/1595089 "") [1595090](https://support.mozilla.org/questions/1595090 "") | 0.0 |
| weekly | **274.0×** | 2026-08-03 | tb_version_major | 153 | 137 [1596331](https://support.mozilla.org/questions/1596331 "When a message must be Sent Later, where is the draft stored???") [1596345](https://support.mozilla.org/questions/1596345 "InsertSignature button moved from formatting toolbar to top toolbar after Thunde") | 0.5 |
| weekly | **52.0×** | 2026-08-10 | tb_version_major | 153 | 130 [1597513](https://support.mozilla.org/questions/1597513 "Migrate emails to another provider") [1597551](https://support.mozilla.org/questions/1597551 "Thunderbird POP stopped retrieving email from one mail box, No error message") | 2.5 |
| weekly | **new** | 2026-08-17 | tb_version_major | 154 | 63 [1598813](https://support.mozilla.org/questions/1598813 "Missing SENT messages. Folder ＂greyed out＂") [1598989](https://support.mozilla.org/questions/1598989 "Over the weekend Thuderbird stopped allowing me to send emails and will not set ") | 0.0 |
| weekly | **3.8×** | 2026-08-17 | tb_version_major | 153 | 89 [1598650](https://support.mozilla.org/questions/1598650 "I am trying to restore a backed up profile for use in thunderbird.") [1598659](https://support.mozilla.org/questions/1598659 "Please remover the annpying Yahoo signip splash screen") | 23.5 |
| weekly | **new** | 2026-08-24 | tb_version_major | 154 | 90 [1599916](https://support.mozilla.org/questions/1599916 "Are you having problems with the program right now?") [1599944](https://support.mozilla.org/questions/1599944 "Transfer Thunderbird from PC to Laptop") | 0.0 |

</details>

<details markdown="1">
<summary><strong>📈 August 2026 trends</strong> — 6 rows</summary>

**Top versions**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| v153 | 420 | `▅▄▇▇▅▇▇▇▅▇▄▇▇▇▅▇▇█▄▄▅▃▃▄▂▃▅▃▁` |
| v154 | 154 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▃▄▆▄▄▆▃█▅▅▁` |
| v140 | 61 | `▃▃▅▆█▅▆█▃▆█▅▁▅▆▅▅▅▁▆▅▆▆▅▅▅▅▃▁` |
| v115 | 23 | `▃▁▃▃▆▁▃▃▁█▁▁▁▁▃▆▆▁▁▁▁▆▁▆▃█▁▁▁` |
| v150 | 21 | `▁▁▅▁▃▆▃█▁▃▁▁▁▃▃▃▃▁▃▃▁▁▁▃▁▃▁▃▁` |
| v152 | 6 | `█▁█▁█▁█▁█▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |

**Top mail providers**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| m:gmail | 65 | `▂▁▆▅▂▅▂▅▁▄▂▃▄▃▄▁▄█▃▅▃▄▄▁▄▄▂▁▁` |
| m:yahooemail | 49 | `▃▅▆▅▃▅▃▆▅██▅▃▆▃█▃▅▁▅▅▃▁▁▅▃▁▅▁` |
| m:microsoftemail | 47 | `▄▂▇█▄▁▄▂▁▅▂▄▅▄▁▂▂▂▂▄▅▄▂▂▄▂▂▄▁` |
| m:spectrum | 25 | `▁▃▁▁▃▁▁▃▃▁▁▅▁▃▁▁▁▃▁▁▅███▃▁▃▃▁` |
| m:comcast | 12 | `▃▃▁▁▃▁▁▁▁▁▁▁▁▁▃█▁▃▁▁▃▃▁▁▁▃▃▁▁` |
| m:cox | 5 | `▁▁▁▁▁▁▁█▁▁▁███▁▁▁▁▁▁▁█▁▁▁▁▁▁▁` |

**Top protocols**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| proto:imap | 64 | `▃▁▇▃▅▁▁▃▃█▂▂▅▆▃▂▅▆▃▁▃▅▃▅▂▇▃▂▃` |
| proto:pop | 41 | `▃▃▅▆▃▅▅▆▅█▁▁██▁▁▅▅▁▃▃▃▁▃▁▁▆▃▁` |
| proto:smtp | 38 | `▁▃█▁▃▁▃▃▃▆▁▆▆▆▃▁▃▃▃▆█▆▃▆▃█▃▆▃` |
| proto:oauth | 15 | `▁▁▃▁▁▁▁▆▁█▃▁▃▁▃▁▃▁▃▁▁▃▁▁▃▁▁▆▁` |
| proto:ews | 3 | `█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁` |
| proto:carddav | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁` |

**Top antivirus**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| av:bitdefender | 3 | `▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁` |
| av:avast | 2 | `▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁` |
| av:defender | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁` |
| av:mcafee | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁█▁▁▁` |
| av:kaspersky | 2 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁█▁▁` |
| av:norton | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁` |

**OS mix (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| os:windows | 674 | `▃▂▅▅▃▄▄▅▃▅▂▅▅▅▃▃▅▅▄▅▆▅▄▆▄█▆▅▁` |
| os:linux | 83 | `▄▃▃▂▃▄█▅▁▃▄▂▂▃▄▅▂▃▂▂▂▃▂▂▄▂▂▂▁` |
| os:macos | 54 | `▂▂▂▅█▅▃▃▃▂▅▂▂▁▅█▂▆▂▁▃▃▂▅▂▂▃▁▁` |
| os:android | 10 | `▁▃▁▁▁▃▁▆▁▁▃▃▁▁▁▁▁█▁▁▁▁▁▁▁▃▁▁▁` |
| os:other | 6 | `▁▅▁▅▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▅▅▁▁` |

**macOS releases (filter dimension)**

| Value | Questions | Trend (by day) |
|:--|--:|:--|
| macos:tahoe | 3 | `▁▁▁▁█▁█▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:monterey | 2 | `▁▁▁█▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sonoma | 1 | `▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sierra | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁▁` |
| macos:sequoia | 1 | `▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁█▁▁▁▁▁` |


</details>

---

_Detectors run at daily / weekly / monthly grain; a weekly period is included when its week overlaps August 2026. Version×cause requires a known version, which is only populated from 2026-02 onward; cause-level uses all history. Full spike CSVs: `PROJECT1/desktop-{daily,weekly,monthly}-{single,version-cause}-spikes.csv`._
