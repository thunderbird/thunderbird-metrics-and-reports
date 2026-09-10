# Why did desktop support volume rise in August 2026?

August 2026 logged **941** desktop questions against July's **731** — **+210
(+29%)**. This is an analysis of possible causes, with the hypotheses I could test
from the corpus marked as tested and the ones needing external data left open.
Companion to issue #67 (the long-run volume decline).

## Confirmed in ground truth (2026-09-09)

The BigQuery ground truth now runs through August 2026 and the rise is real:

| Month | BigQuery | This repo | Match |
|:--|--:|--:|--:|
| 2026-05 | 812 | 812 | 100.0% |
| 2026-06 | 724 | 725 | 100.1% |
| 2026-07 | 732 | 731 | 99.9% |
| **2026-08** | **943** | **941** | **99.8%** |
| 2026-09 (Sep 1–8) | 291 | 291 | 100.0% |

Across all 44 complete months the two agree to 100.0% (49,419 against 49,422),
and the old 2023-11 scraper gap is closed. So the +29% is not a scraper artefact.
See `README.md` in this directory.

The September figure is a partial export. BigQuery gives 291, and this repo's
cumulative count through 2026-09-08 is 291 exactly, so the export ends with
September 8 and the two agree to the question. That puts the September run rate
at **36.4/day in ground truth**, against 30.4/day in August.

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
| Seasonality (Jul→Aug is normally up) | **CONFIRMED, and it is most of the rise** | Raw ratios read as inconsistent (2023 −3%, 2024 +34%, 2025 +6%, 2026 +29%), but raw ratios mix the seasonal step with the year's trend. Detrended against a centred 12-month mean, August is a high month every year. See the section below. |

## Seasonality explains about 60% of the rise

Dividing each month by a centred 12-month mean removes the decline and leaves the
calendar effect. Averaged over 2023–2026 (BigQuery):

| Month | J | F | M | A | M | J | J | A | S | O | N | D |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Index | 1.03 | 0.94 | 0.93 | 0.81 | 0.80 | 0.76 | 0.98 | 1.16 | 1.19 | 1.41 | 1.11 | 0.97 |

June is the floor of the year and August, September and October are the peak.
The seasonal step from July to August is 1.16 / 0.98 = **1.18×**.

Applied to July 2026 (732 questions), the expected August is **860**. The actual
is 943, which is **1.10× the seasonal expectation, or +83 questions**. So of the
+211 rise, roughly **128 is the normal August step and 83 is genuine excess**.

That reframes the decomposition above. The named clusters (printing +32, Spectrum
+29, Yahoo Mail +25, crashes +10, union **+96**) do not cover half of +211; they
cover **more than all of the +83 excess**. The residual is largely the calendar.

September behaves the same way. The index says September runs 1.19 / 1.16 = 1.03×
August, which from a 30.4/day August predicts **31.2/day**. Ground truth gives
**36.4/day** through September 8, so September carries about **+5.2/day of excess**,
larger than August's +2.7/day. The excess is growing even though the rise itself
is mostly seasonal, and that is the part worth watching.

Two cautions. The index rests on three Augusts, and 2023 does not fit it (index
0.86, the year Supernova pushed the peak to October). And eight days is a short
window: one busy Monday moves it.

## Hypotheses that need EXTERNAL data (cannot be settled from the corpus)

1. ~~**Is the rise real in ground truth?**~~ **SETTLED 2026-09-09: yes, for both
   months.** BigQuery gives 943 for August against this repo's 941, and 291 for
   September 1–8 against 291 here. All 44 complete months agree to 100.0%.
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
