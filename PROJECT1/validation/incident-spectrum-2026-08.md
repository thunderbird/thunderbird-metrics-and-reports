# Incident analysis — Spectrum / Charter, from 2026-08-21 (ongoing)

Companion to the detector back-tests in this directory. Unlike those, this one
analyses a **live, still-open** cluster rather than a closed incident. Brands
treated as one entity throughout: **Spectrum, Charter, Time Warner Cable / TWC,
Roadrunner (`*.rr.com`, `mail.twc.com`, `mobile.charter.net`)** — all the same
company, all tagged `m:spectrum`.

## When it started: 2026-08-21, 18:47 UTC

The first question of the cluster is **1599516 at 2026-08-21 18:47Z** ("When
trying to send an email it will not go"), followed by 1599553 at 22:19Z ("I can't
receive or send Charter emails in thunderbird"). Before it there is a **2.9-day
quiet gap** — the previous `m:spectrum` question (Aug 18 18:58Z) is an unrelated
Mozilla-VPN connection-reset report, and the one before that (Aug 14) an unrelated
Roadrunner display issue.

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
connect to spectrum Charter email"), and one names v154 directly ("Thunderbird
154.0 is causing extreme issues with Spectrum email"). The timing invites that
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
| **May 9–27** | 19 | connect / send-receive (46%) + auth (44%) | "Lost Thunderbird connectivity on Spectrum today 5/9/26" |
| **Jun 9–16** | 20 | **cert/SSL (18% overall, 7 clustered on Jun 9–10)** | "The certificate for `mobile.charter.net:993` does not come from a trusted source" |
| **Aug 21 → ongoing** | 36 | connect / send-receive (53%) + auth (19%), cert ~0 | "Cannot send or receive email", "not connecting to server" |

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
(Sep 2, Sep 5) — a different symptom on a new version, and one that
`m:spectrum` absorbs rather than surfacing separately. Worth checking on its own.

## Served

84% answered (31/37 since Aug 15), median first answer 8.5h. The wk-08-31 slice is
the worst-served of the month at 37.2h median.
