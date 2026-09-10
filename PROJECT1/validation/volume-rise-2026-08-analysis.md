# Why did desktop support volume rise in August 2026?

August 2026 logged **941** desktop questions against July's **731** — **+210
(+29%)**. This is an analysis of possible causes, with the hypotheses I could test
from the corpus marked as tested and the ones needing external data left open.
Companion to issue #67 (the long-run volume decline).

## First: it is not an "August bump"

Framing it as one month misses the shape. Per-day rates (month-length neutral):

| Month | Questions | Per day |
|:--|--:|--:|
| 2026-04 | 759 | 25.3 |
| 2026-05 | 812 | 26.2 |
| 2026-06 | 725 | 24.2 |
| **2026-07** | **731** | **23.6** |
| **2026-08** | **941** | **30.4** |
| 2026-09 (9 days) | 327 | **36.3** |

**September is running higher than August.** The rise is ongoing and accelerating,
and the trailing-3-month rate bottomed out at 24.6/day in July and has turned up
to 30.1/day.

The changepoint is the **week of Aug 3**, not the v154 release. Weekly counts:
Jun–Jul sit in a 148–183 band, then 213 (wk 08-03), 188, 215, 239, 256 (wk 08-31).
Splitting August around the v154 rollout (Aug 18–19):

| Window | Per day | vs July |
|:--|--:|--:|
| Jul 1–31 | 23.6 | — |
| Aug 1–17 (pre-v154) | 27.5 | **1.16×** |
| Aug 18–31 (v154 out) | 33.9 | **1.44×** |

So roughly a third of the lift predates v154 entirely.

## Second: it is still a decline year-over-year

| Month | 2025 /day | 2026 /day | YoY |
|:--|--:|--:|--:|
| Jun | 34.9 | 24.2 | −31% |
| **Jul** | 46.3 | 23.6 | **−49%** |
| **Aug** | 49.2 | 30.4 | **−38%** |
| **Sep** | 43.2 | 36.3 | **−16%** |

August 2026 is 38% *below* August 2025, so this is a **rebound inside a longer
decline, not a reversal of it**. But the YoY gap is closing fast — −49% → −38% →
−16% over three months — which is the part #67 should probably revisit.

## Decomposition of the +210

Four clusters are individually identifiable. Counted as a **union** (a question
matching two clusters is counted once), they explain a bit over half the rise:

| Component | Jul | Aug | Δ |
|:--|--:|--:|--:|
| `feat:printing` (v154 regression, Bugzilla 2065922) | 4 | 36 | **+32** |
| `m:spectrum` (provider incident from Aug 21) | 5 | 34 | **+29** |
| `m:yahooemail` (wk 08-10 cluster, 3.45×, 63% answered) | 30 | 55 | **+25** |
| crashes (title-verified — see the provenance note below) | 18 | 28 | **+10** |
| **Union of the four** | **56** | **152** | **+96 (46% of the rise)** |
| **Residual — everything else** | **675** | **789** | **+114 (54% of the rise)** |

The residual is not flat noise: it runs 21.8/day in July → 25.5/day in August →
**31.4/day in September**. Whatever is lifting the floor is still lifting it, and
it is bigger than every identified incident combined.

### Provenance note on the crash figure (corrected 2026-09-10)

An earlier version of this table put the crash component at **+37**, taken from
the SUMO **`topic`** column — questions filed under `app-crash` or
`crashing-and-slow-performance`. That is topic metadata carried verbatim from the
scraper's questions CSV (44 possible values, exactly one per question); it is
**not** crash-stats, not telemetry, and not a regex over the question text.

Checked against the titles, it is a poor proxy. Of August's 29
`crashing-and-slow-performance` questions, **2 are crash-worded, 5 are
slow-worded, and 22 are neither** — the bucket also holds "Print Preview Printing
Blanks" (part of the printing cluster), "Thunderbird Mail does not display the
body of the email msg" and "Profile Manager". `app-crash` holds up better (15 of
35 crash-worded, and several of the rest describe a crash in other words: "non si
apre più", "my email froze").

Using a **title regex** for crash/freeze/hang/not-responding wording instead gives
Jul 18 → Aug 28, i.e. **+10**, at 2.5% → 3.0% of volume — well inside the normal
oscillation (May 2.5%, June 3.9%, September 3.7%). **So "crashes roughly doubled"
is not supported.** The revision moves ~27 questions out of an identified cluster
and into the residual, which *raises* the unexplained share of the rise from 43%
to 54%.

## Hypotheses TESTED against the corpus

| Hypothesis | Verdict | Evidence |
|:--|:--|:--|
| Duplicate/bot/spam inflation | **Rejected** | Unique creators scale with volume: 676 (Jul) → 845 (Aug); questions per creator flat at 1.08 → 1.11. Top August asker filed 7. ~169 more *distinct people*. |
| A new locale / traffic source | **Rejected** | Locale mix stable: en-US 85.2% → 86.9%; it/nl/es all within a point. |
| SUMO-funnel or scraper-wide change | **Rejected** | **Android went the other way: −11% Jul→Aug** while desktop went +29%. A funnel or scraper cause would hit both. (Caveat: android is only ~2/day, so its noise is wide.) |
| v154 caused it | **Partly — a third at most** | The changepoint is wk Aug 3; Aug 1–17 already ran 1.16× July before v154 shipped. v154 does coincide with the steeper second half (1.44×). |
| The crash rise is a v154 regression | **Rejected — and the rise itself is mostly an artefact** | Cohort rates over the SUMO crash/perf topics, Aug 18–Sep 9: v154 7.1%, v153 5.5%, v155 6.3%, **v140 10.2%**, unknown 10.7% — no version specificity (contrast printing: v154 13.4% vs v153 0.0%). And title-verified crashes only rose +10 (2.5% → 3.0%), within normal oscillation. See the provenance note above. |
| Seasonality (Jul→Aug is normally up) | **Weak / inconsistent** | 2023: −3%. **2024: +34%.** 2025: +6%. 2026: +29%. August *can* jump, but two of three prior years did not. |

## Hypotheses that need EXTERNAL data (cannot be settled from the corpus)

1. **Is the rise real in ground truth?** Cross-check August and September against
   BigQuery using the #67 method (`PROJECT1/validation/bq-desktop-questions-by-month.sql`).
   This is the cheapest decisive check and should come first — the whole analysis
   rests on scraper counts.
2. **Did SUMO change the ask-a-question funnel in early August?** A more prominent
   AAQ entry point, a changed help-article CTA, or a support-routing change would
   raise *every* topic at once — which is exactly the residual's signature.
3. **Release cadence and user base.** Three releases in six weeks (v153 ~Jul 25–26,
   v154 Aug 18–19, v155 Sep 1) versus a quieter July. More releases → more
   "after the update" questions. Independently, did the desktop install base grow?
4. **The crash question (+10, not +37).** Small and within historical oscillation,
   so it is no longer a leading candidate — but a crash-stats / telemetry
   cross-check would settle whether even the +10 is real, since the support
   corpus cannot distinguish a crash from a hang or a failed launch.
5. **September's send-and-receive-email doubling.** The single biggest mover:
   5.97/day (Jul) → **12.44/day** (Sep). It is diffuse — 68% of those questions
   carry no provider tag, versus 64% in July — so it is not one unnamed provider
   incident. This may be the most important open thread.

## Detector gap this exposes

`project1_spike_detect.py` does carry a `total` dimension, but it has produced
**zero** spikes in 3.5 years of history at any grain — because `single_mult=3.0`
means aggregate volume would have to treble. A +29% month, or a sustained
+54% climb over six weeks, is invisible to the detectors **by construction**.
If aggregate-volume changepoints are worth alerting on, that needs a different
statistic (e.g. a trend/changepoint test on the `total` series), not a lower
multiplier — dropping the multiplier would flood every cause dimension.
