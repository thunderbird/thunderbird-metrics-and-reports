# Incident analysis — Spectrum / Charter, from 2026-08-21 (ongoing)

Companion to the detector back-tests in this directory. Unlike those, this one
analyses a **live, still-open** cluster rather than a closed incident. Brands
treated as one entity throughout: **Spectrum, Charter, Time Warner Cable / TWC,
Roadrunner (`*.rr.com`, `mail.twc.com`, `mobile.charter.net`)** — all the same
company, all tagged `m:spectrum`.

## When it started: 2026-08-21, 18:47 UTC

The first question of the cluster is **[1599516](https://support.mozilla.org/questions/1599516) at 2026-08-21 18:47Z** ("When
trying to send an email it will not go"), followed by [1599553](https://support.mozilla.org/questions/1599553) at 22:19Z ("I can't
receive or send Charter emails in thunderbird"). Before it there is a **2.9-day
quiet gap** — the previous `m:spectrum` question ([1598964](https://support.mozilla.org/questions/1598964), Aug 18 18:58Z) is an
unrelated Mozilla-VPN connection-reset report, and the one before that
([1598314](https://support.mozilla.org/questions/1598314), Aug 14) an unrelated Roadrunner display issue.

The rate change is unambiguous, against a long-run baseline of **11–12
questions/month (0.39/day)** measured over 2023-01→2026-06:

| Window | Questions | Per day | vs baseline |
|:--|--:|--:|--:|
| Aug 1–20 | 8 | 0.40 | **1.0×** (exactly baseline) |
| **Aug 21–31** | **26** | **2.4** | **6×** |
| Sep 1–9 | 10 | 1.1 | 2.8× |

⏱ **Aug 21 is a lower bound, not the provider-side onset.** Per Project 1's
lagging-indicator property, this is when users piled in; the underlying change
plausibly precedes it by a day or more. 18:47Z is ~2:47pm US Eastern, mid-afternoon
in Spectrum's core service area.

## Shape: two peaks, then an elevated plateau — it has NOT ended

Daily counts: `21:2 22:4 23:4 24:4 25:1 26:0 27:1 28:1 `**`29:4 30:4`**` 31:1`,
then September at 1–2/day through 09-09. A **second peak on Aug 29–30 as large as
the first**, separated by a four-day lull.

Weekly detector view: wk 08-17 → 11 questions (**11×**), wk 08-24 → 15 (**10×**),
wk 08-31 → 9 (3.6×). Note the `2026-08-31` week is mostly *September* days
(Aug 31–Sep 6) — do not read it as an August signal.

September is running at essentially August's rate (3.06% of monthly volume vs
3.61%), still ~2.8× baseline, most recent 2026-09-09. **So the correct
description is "started Aug 21, decayed to an elevated plateau", not "started and
ended".**

## Attribution: provider-side, not Thunderbird-side

10 of the 36 questions blame a Thunderbird update ("After latest update can't
connect to spectrum Charter email", [1599823](https://support.mozilla.org/questions/1599823)), and one names v154 directly
("Thunderbird 154.0 is causing extreme issues with Spectrum email", [1601056](https://support.mozilla.org/questions/1601056)). The timing invites that
reading — v154 rolled out Aug 18–19, two days before onset.

**The cross-provider control test rejects it.** If a Thunderbird release had
broken mail connections, other providers would move too. Over Aug 21–31 vs a
Jun 1–Aug 20 baseline:

| Provider | Window | /day | Baseline /day | Ratio |
|:--|--:|--:|--:|--:|
| **m:spectrum** | 26 | 2.36 | 0.41 | **5.8×** |
| m:gmail | 25 | 2.27 | 2.16 | 1.1× |
| m:microsoftemail | 19 | 1.73 | 1.53 | 1.1× |
| m:yahooemail | 14 | 1.27 | 1.21 | 1.1× |
| m:comcast | 4 | 0.36 | 0.43 | 0.8× |

Every other major provider is flat. The cluster also **spans six Thunderbird
majors** — v154 (14), v153 (10), unknown (6), v155 (4), v140 (2), v150 (1) —
including v155 users *after* the Sep 1 release. A version-specific regression
cannot produce that distribution.

**Consequence for reading the reports:** the `v154 × m:spectrum` version×cause row
(13 questions, 3.1× lift, `spreading`) is **an artefact of v154 being the dominant
version in the period**, not evidence of a release regression. This is the same
shape as the March 2026 GMX outage already documented in `CLAUDE.md`: a
**cause-level** incident that the joint detector also reports against whichever
version happens to dominate. Trust the cause-level row here; treat the joint row
as coincidental.

## This is the third distinct Spectrum episode of 2026

`m:spectrum` questions per month, 2026: Jan 8 · Feb 14 · Mar 7 · Apr 6 ·
**May 19** · **Jun 20** · Jul 5 · **Aug 34** · Sep 10 (9 days). Symptom mix
separates them into three unrelated root causes:

| Episode | n | Dominant symptom | Signature |
|:--|--:|:--|:--|
| **May 9–27** | 19 | connect / send-receive (46%) + auth (44%) | "Lost Thunderbird connectivity on Spectrum today 5/9/26" ([1580867](https://support.mozilla.org/questions/1580867)) |
| **Jun 9–16** | 20 | **cert/SSL (18% overall, 7 clustered on Jun 9–10)** | "The certificate for `mobile.charter.net:993` does not come from a trusted source" ([1586504](https://support.mozilla.org/questions/1586504)) |
| **Aug 21 → ongoing** | 36 | connect / send-receive (53%) + auth (19%), cert ~0 | "Cannot send or receive email" ([1600103](https://support.mozilla.org/questions/1600103)), "not connecting to server" ([1599818](https://support.mozilla.org/questions/1599818)) |

So August is **not** a recurrence of the June certificate incident (that one was a
specific untrusted-cert failure on `mobile.charter.net:993`, and is the episode
`CLAUDE.md` refers to as the validated `v151 × m:spectrum` cert spike). It most
resembles the **May** connectivity/auth episode. July (5 questions) is a clean
control month between them.

The picture is **chronic provider instability**: a Spectrum cluster every two to
three months with a *different* root cause each time, on a 11–12/month floor. That
is what the detector's `recurring` novelty tag is describing, and it is the reason
`novelty` exists — so a genuinely new regression (v154 printing, tagged `new`)
floats above chronic provider load.

## Possibly a distinct sub-cluster in September

Two v155 users report Charter/POP mail being routed to **Trash instead of Inbox**
(Sep 2, [1601790](https://support.mozilla.org/questions/1601790); Sep 5, [1602271](https://support.mozilla.org/questions/1602271)) — a different symptom on a new
version, and one that `m:spectrum` absorbs rather than surfacing separately. Worth checking on its own.

## Served

84% answered (31/37 since Aug 15), median first answer 8.5h. The wk-08-31 slice is
the worst-served of the month at 37.2h median.

## Every question in the cluster

All 36 `m:spectrum` questions from 2026-08-21 to 2026-09-09, oldest
first. Titles are shortened to 80 characters. The Answered column is yes when
a person other than the person who asked replied. The Solved column is the
SUMO `is_solved` flag, which the person who asked sets. A trusted contributor
is a person on
`CONCATENATED_FILES/DESKTOP/thunderbird-desktop-trusted-contributors.csv`, and
the last column is yes when that person wrote the most recent answer.

<details markdown="1">
<summary>The 36 questions</summary>

| Date | Question | Version | Title | Answered | Solved | Last answer by a trusted contributor |
|:--|:--|:--|:--|:--|:--|:--|
| 2026-08-21 | [1599516](https://support.mozilla.org/questions/1599516) | 153 | When trying to send an email it will not go | yes | no | no |
| 2026-08-21 | [1599553](https://support.mozilla.org/questions/1599553) | 153 | I can't receive or send Charter emails in thunderbird. | yes | no | yes |
| 2026-08-22 | [1599681](https://support.mozilla.org/questions/1599681) | 140 | I am unable to send and receive emails on two of my computers. I can do that on… | yes | no | yes |
| 2026-08-22 | [1599683](https://support.mozilla.org/questions/1599683) | 154 | Suddenly not receiving email | yes | no | yes |
| 2026-08-22 | [1599711](https://support.mozilla.org/questions/1599711) | unknown | I use to be able to get my email messages from Spectrum on Thunderbird, but now… | yes | no | yes |
| 2026-08-22 | [1599738](https://support.mozilla.org/questions/1599738) | 154 | Thunderbird is not receiving in coming mail from Charter | yes | no | yes |
| 2026-08-23 | [1599818](https://support.mozilla.org/questions/1599818) | 154 | Thunderbird not connecting to server.  Cannot send or receive emails. | yes | no | no |
| 2026-08-23 | [1599823](https://support.mozilla.org/questions/1599823) | 153 | After latest update can't connect to spectrum Charter email | yes | no | yes |
| 2026-08-23 | [1599836](https://support.mozilla.org/questions/1599836) | 153 | all INBOX emails disappeared--no luck repairing folder or deleting INBOX.msf bu… | yes | yes | no |
| 2026-08-23 | [1599874](https://support.mozilla.org/questions/1599874) | 154 | Ability to send emails using roadrunner (mail.twc.com) account | yes | no | yes |
| 2026-08-24 | [1600000](https://support.mozilla.org/questions/1600000) | 153 | Suddenly can't send/receive emails | no | no | no |
| 2026-08-24 | [1600041](https://support.mozilla.org/questions/1600041) | 153 | I can receive but not send emails | yes | yes | yes |
| 2026-08-24 | [1600052](https://support.mozilla.org/questions/1600052) | 154 | Trouble connecting to my email provider Time Warner Corporation to send emails … | no | no | no |
| 2026-08-24 | [1600103](https://support.mozilla.org/questions/1600103) | 153 | Cannot send or receive email. (locked duplicate) | yes | no | yes |
| 2026-08-25 | [1600207](https://support.mozilla.org/questions/1600207) | unknown | Can't get into my Spectrum email account through Thunderbird | yes | no | no |
| 2026-08-27 | [1600663](https://support.mozilla.org/questions/1600663) | unknown | can no longer get my e-mail | yes | no | yes |
| 2026-08-28 | [1600872](https://support.mozilla.org/questions/1600872) | 154 | I can send email but can not receive. | yes | no | yes |
| 2026-08-29 | [1600919](https://support.mozilla.org/questions/1600919) | 154 | how Can i get help when my email doesn't work? | yes | no | yes |
| 2026-08-29 | [1600982](https://support.mozilla.org/questions/1600982) | 154 | Thunderbird not working again with Spectrum emails. | yes | no | yes |
| 2026-08-29 | [1600985](https://support.mozilla.org/questions/1600985) | 150 | Again no email using Spectrum | yes | no | yes |
| 2026-08-29 | [1601056](https://support.mozilla.org/questions/1601056) | 154 | Thunderbird 154.0 is causing extremem issues with Spectrum email. HELP Please | yes | no | yes |
| 2026-08-30 | [1601071](https://support.mozilla.org/questions/1601071) | 154 | After update I cant send or receive Charter emails | yes | no | no |
| 2026-08-30 | [1601143](https://support.mozilla.org/questions/1601143) | 153 | IMAP accounts no longer update - Charter/Spectrum email hosting | yes | yes | no |
| 2026-08-30 | [1601159](https://support.mozilla.org/questions/1601159) | 154 | thunderbird has stopped downloading email from charter. it will work if i have … | yes | no | no |
| 2026-08-30 | [1601196](https://support.mozilla.org/questions/1601196) | 154 | Problems Sending and Receiving - Unable to Connect to Server | yes | no | no |
| 2026-08-31 | [1601375](https://support.mozilla.org/questions/1601375) | 154 | my spectrum password wont log me in to thunderbird why | yes | no | yes |
| 2026-09-01 | [1601442](https://support.mozilla.org/questions/1601442) | 140 | Correct Outgoing SMPT settings for IMAP | no | no | no |
| 2026-09-01 | [1601623](https://support.mozilla.org/questions/1601623) | unknown | no access to Thunderbird email through Spectrum | yes | no | yes |
| 2026-09-02 | [1601790](https://support.mozilla.org/questions/1601790) | 155 | Charter + pop, all new messages are going to the trash folder, not my inbox, an… | yes | no | yes |
| 2026-09-02 | [1601822](https://support.mozilla.org/questions/1601822) | unknown | trouble sending and receiving messages interfacing with Spectrum (locked duplic… | no | no | no |
| 2026-09-03 | [1602003](https://support.mozilla.org/questions/1602003) | 153 | Spectrum Emails are disappearing from my Thunderbird Inbox after downloading. T… | yes | no | yes |
| 2026-09-05 | [1602271](https://support.mozilla.org/questions/1602271) | 155 | Mail coming to inbox is automatically rerouted to trash folder | yes | no | yes |
| 2026-09-06 | [1602429](https://support.mozilla.org/questions/1602429) | 155 | Cannot connect Thunderbird to Spectrum | yes | no | no |
| 2026-09-06 | [1602561](https://support.mozilla.org/questions/1602561) | 154 | Emails without content | yes | no | no |
| 2026-09-08 | [1602946](https://support.mozilla.org/questions/1602946) | unknown | How can i access my Thunderbird  email? It stopped recognizing my password | no | no | no |
| 2026-09-09 | [1603164](https://support.mozilla.org/questions/1603164) | 155 | mobile.charter.net  times out? | no | no | no |

</details>
