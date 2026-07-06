---
layout: base
title: Android LLM Insights — June 2026
---

# Thunderbird Android — LLM Insights (Engineering)

## June 2026 vs May 2026

_The **AI counterpart to Project 1**: Claude reads every support question (plus the creator's own follow-ups, the accepted solution, and trusted-contributor replies), names the concrete problem, hypothesises a root cause, and rates severity — surfacing emerging / worst-served pain that regex + stats can't. Counts are exact (computed in Python); clustering and prose are LLM-derived. A triage pointer, not proof._

## Headline

| | May 2026 | June 2026 | Change |
|:--|--:|--:|:--|
| Support questions (load) | 47 | 46 | ▼ -1 (-2%) |
| Distinct issue clusters | 36 | 34 | ▼ -2 |
| New issue clusters this month | — | 5 | |

**Android email delivery is the emerging pain point—top issue #6 shows severe, partly-unanswered breakage while five new clusters cluster around mobile parity.**

**Volume was flat month-over-month (46 vs 47 questions), but the composition shifted toward mobile/Android delivery and cross-device parity.** Five brand-new clusters appeared this month, and the single worst-served issue is a returning one: **#6 (stopped receiving new mail on Android)** now carries a mean severity of 4.0 with all three reports at severity 4+, a 67% resolved rate, and a full third of users left with no answer. That combination of high severity and unanswered load is the clearest signal for engineering to act on now.

Category movement backs this up: `search-folders` jumped 1→7 and `migration-import` 3→7, while `send-receive` rose 9→12. Meanwhile `account-login` (10→5) and `ui-ux` (9→4) cooled off. The new clusters (#1–#5) are individually low-volume but thematically consistent—several are Android-side gaps in features desktop users take for granted (local/POP3 folders, notifications, password change, flagged-mail views).

**Attachments went 0→3 as a category**, driven by #3 (Save All producing overwritten/zero-byte files)—well-resolved so far but a concrete data-loss bug worth a quick code look. #7 (QR-code transfer failures) is resolving at 100% but doubled in volume, suggesting a scaling friction in the new device-transfer flow.

Net: prioritize the Android receive/notification path (#6, #2) and the attachment data-loss bug (#3); the remaining new clusters are lower-severity parity requests to track, not firefight.

## 🚨 Issues to investigate

_Ranked by a transparent score weighting new/emerging + worst-served (low resolved %) + severity + volume. **Resolved %** = solved or a trusted contributor gave the last word; ⚠️ marks poorly-served clusters._

### 1. Local folders from desktop / POP3 not accessible on Android · 🆕 new this month

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Local folders from desktop / POP3 not accessible on Android (settings-config) | 0 | 2 | ▲ +2 | 2.5 (0) | 50% | 0% |

- **Why:** New cluster reflecting a cross-device parity gap—desktop local/POP3 folders simply aren't reachable on Android, with only 50% resolved.
- **Look at:** Confirm expected behavior and messaging for POP3/local-folder accounts on Android, and clarify in-app whether server-side sync is required.
- **Examples:** [1589013](https://support.mozilla.org/questions/1589013 "Moving messages around in local folders when using POP") [1585727](https://support.mozilla.org/questions/1585727 "Accessing local folders on android")

### 2. No new-mail notifications despite sync · 🆕 new this month

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| No new-mail notifications despite sync (send-receive) | 0 | 2 | ▲ +2 | 2.5 (0) | 50% | 0% |

- **Why:** New this month and directly compounds #6—users receive mail but get no notification, eroding trust in the client even when sync works.
- **Look at:** Audit the Android notification pipeline (channel registration, per-account notification settings, and post-sync notify triggers) for cases where new-mail events don't surface.
- **Examples:** [1589027](https://support.mozilla.org/questions/1589027 "Notification of incoming email works for one provider but not the other.") [1586400](https://support.mozilla.org/questions/1586400 "Why my email don't sync")

### 3. Save All attachments overwrites / zero-byte files · 🆕 new this month

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Save All attachments overwrites / zero-byte files (attachments) | 0 | 2 | ▲ +2 | 3.0 (0) | 100% | 0% |

- **Why:** A concrete data-loss bug (overwritten or zero-byte files) in Save All attachments, now visible as a new attachments cluster.
- **Look at:** Review the Save-All file-writing path for duplicate-filename collision handling and stream-flush/close on empty or same-named attachments.
- **Examples:** [1588049](https://support.mozilla.org/questions/1588049 "Save all attachments not working") [1589713](https://support.mozilla.org/questions/1589713 "Save all changes documents")

### 4. Change email account password on Android · 🆕 new this month

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Change email account password on Android (account-login) | 0 | 2 | ▲ +2 | 1.0 (0) | 100% | 0% |

- **Why:** New but low-severity (1.0) and fully resolved—a discoverability/UX gap rather than a defect.
- **Look at:** Consider surfacing the account-password change flow more clearly in Android account settings; no code urgency.
- **Examples:** [1588089](https://support.mozilla.org/questions/1588089 "how to change thunderbird  password on samsung phone") [1589539](https://support.mozilla.org/questions/1589539 "password")

### 5. Finding starred/flagged emails and folder · 🆕 new this month

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Finding starred/flagged emails and folder (search-folders) | 0 | 2 | ▲ +2 | 1.0 (0) | 100% | 0% |

- **Why:** New parity request showing users can't easily locate starred/flagged mail on mobile despite the feature existing on desktop.
- **Look at:** Verify a discoverable flagged/starred smart-folder or filter view exists in the Android UI.
- **Examples:** [1585622](https://support.mozilla.org/questions/1585622 "How do I find a letter marked with a star?") [1587771](https://support.mozilla.org/questions/1587771 "Flagged folder")

### 6. Stopped receiving new mail on Android

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| Stopped receiving new mail on Android (send-receive) | 1 | 3 | ▲ +2 | 4.0 (3) | 67% | 33% |

- **Why:** Highest-severity issue on the board (mean 4.0, all three sev4+) with a third of users unanswered—this is active, unresolved user pain around core mail delivery.
- **Look at:** Investigate Android background sync/push and account-fetch reliability, especially IMAP IDLE and battery-optimization/doze interactions that silently halt mail retrieval.
- **Examples:** [1585920](https://support.mozilla.org/questions/1585920 "Thunderbird has stopped receiving emails.  I followed the instructions I found. ") [1587011](https://support.mozilla.org/questions/1587011 "New email not received in android") [1588448](https://support.mozilla.org/questions/1588448 "Thunderbird mobile and on Ubuntu do not fetch Mails anymore")

### 7. QR code not recognised during transfer

| Cluster | May 2026 | June 2026 | Change | Sev (≥4) | Resolved | Unanswered |
|:--|--:|--:|:--|:--|:--|--:|
| QR code not recognised during transfer (migration-import) | 1 | 3 | ▲ +2 | 3.0 (0) | 100% | 0% |

- **Why:** Device-transfer QR failures doubled and, while resolved, indicate friction scaling in a flagship onboarding flow.
- **Look at:** Check QR generation/scanning tolerance (size, contrast, timeout, camera-permission handling) in the account-transfer feature across device models.
- **Examples:** [1588395](https://support.mozilla.org/questions/1588395 "problem with Thunderbird for Android.") [1588606](https://support.mozilla.org/questions/1588606 "QR code not recognised") [1588762](https://support.mozilla.org/questions/1588762 "I can't scan the qr code to transfer my thunderbird settings to my new Fold 7...")

## Category mix — month over month

| Category | May 2026 | June 2026 | Change |
|:--|--:|--:|:--|
| send-receive | 9 | 12 | ▲ +3 |
| search-folders | 1 | 7 | ▲ +6 |
| migration-import | 3 | 7 | ▲ +4 |
| account-login | 10 | 5 | ▼ -5 (-50%) |
| ui-ux | 9 | 4 | ▼ -5 |
| sync-oauth | 7 | 4 | ▼ -3 |
| attachments | 0 | 3 | ▲ +3 |
| encryption-security | 2 | 1 | ▼ -1 |
| performance-crash | 1 | 1 | ▬ 0 |
| settings-config | 2 | 1 | ▼ -1 |
| other | 2 | 1 | ▼ -1 |
| addons-extensions | 1 | 0 | ▼ -1 |

---

_Prototype LLM-insights report · Claude claude-opus-4-8 over Stage-1 per-question labels · June 2026 vs May 2026 · this run cost $0.12._

_Last updated: 2026-07-06 17:27 UTC_
