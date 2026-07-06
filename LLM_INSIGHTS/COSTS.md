# Project "LLM Insights" — API cost tracking

_Last updated: 2026-07-06. Model: `claude-opus-4-8` ($5 / $25 per 1M input/output tokens)._
_Every LLM step estimates cost via the free `count_tokens` endpoint and aborts above a **$50/run** ceiling (`scripts/llm_insights_cost.py`); actual cost is read from `response.usage` (cache-read tier included)._

## Measured unit rate

- **Classification (Stage 1, "map"):** **~$0.0066 per question** (desktop May $0.006652/q, June $0.006528/q — enriched question text = question + creator follow-ups + accepted solution + trusted replies).
- **Report (Stage 2, "reduce" = semantic clustering + narrative):** **~$0.60 per report** (largely fixed; scales with the number of distinct themes, not question count).

## Actual spend to date

### Desktop — $10.85 total this month

| Step | Questions | Cost |
|:--|--:|--:|
| Bucket 1 sample (validation) | 20 | $0.13 |
| May 2026 classify | 812 | $5.40 |
| June 2026 classify | 724 | $4.73 |
| Bucket 3 report (June vs May) | — | $0.60 |
| **Total** | | **$10.85** |

> **One-time double cost:** the first run classified *both* May and June. In steady state only the **new** month is classified (the prior month's labels are reused), so the recurring cost of one monthly desktop report is **~$5**, not $10.85.

### Android — $0.65 total (PoC)

| Step | Questions | Cost |
|:--|--:|--:|
| May 2026 classify | 47 | $0.27 |
| June 2026 classify | 46 | $0.26 |
| Report (June vs May) | — | $0.12 |
| **Total** | | **$0.65** |

## Projected cost per monthly report (steady state)

Recurring = classify the **new** month only + one reduce (prior month already labeled).

| Product | ~Questions/mo | Live API | Batch API (−50% classify) |
|:--|--:|--:|--:|
| Desktop | ~660–720 (declining) | **~$5.0–5.4** | **~$2.9** |
| Android | ~46 | **~$0.38** (classify ~$0.26 + reduce ~$0.12) | **~$0.25** |

### July 2026 desktop report (July vs June)
- June already labeled, so only July needs classifying + the reduce.
- Full month, live: **≈ $5.0–5.4** (128 questions in through day 6; projecting ~660–720 for the month at ~$0.0066/q + ~$0.60 reduce).
- Full month, Batch API: **≈ $2.9**.
- If generated *today* (partial, 128 q so far): **≈ $1.4** — but understates July (month ~20% elapsed).

### July 2026 android report (July vs June)
- June already labeled, so only July needs classifying + the reduce.
- Full month, live: classify ~46 q × ~$0.0057/q ≈ **$0.26** + reduce **~$0.12** = **≈ $0.38**.
- If generated *today* (partial, 7 q so far): **≈ $0.16** — badly understates July (7 of ~46).
- Android stays **live** (see decision below); batching saves ~$0.13, not worth the complexity.

## Batch API — caveats and current decision

**Decision (2026-07-06): stay on the live (synchronous) API for now.** The 50% saving
is real but small in absolute terms (~$2/month desktop), and the added complexity isn't
worth it until the pipeline is automated and stable. Revisit when building Bucket 4.

The Batch API is not "just slower" — it's a different, asynchronous execution model:

- **Asynchronous, up to 24 h SLA** (usually <1 h). You submit, then poll until `ended`.
  Fine for a scheduled report; wrong for anything interactive. Results kept 29 days.
- **Results come back unordered** — must key every request by a `custom_id` and match on
  it, never by position.
- **Per-request outcomes vary within one batch** (`succeeded` / `errored` / `canceled` /
  `expired`) — a batch can partially fail, so the code must handle mixed results and
  re-submit expired/errored items, not assume all-or-nothing.
- **It's a code change, not a flag** — `messages.batches.create` → poll `retrieve` →
  stream `results()`, replacing the current synchronous `messages.create` loop.
- **Prompt caching is less predictable** — the server controls timing/concurrency, so the
  cross-request cache hits on the shared system prompt aren't guaranteed the way they are
  in a sequential run (the 50% batch discount usually dominates anyway).
- **Unchanged / fine for us:** 50% off both input and output; all features supported
  (structured outputs, our schema, thinking); 100k requests / 256 MB per batch limit;
  available on the first-party API (not Bedrock/Vertex/Foundry — irrelevant here); the
  $50 pre-spend `count_tokens` gate still applies.

**When we do adopt it (Bucket 4):** batch the **classify** stage (many calls, latency-
insensitive → biggest saving); keep the **reduce** stage (2 calls) **live** (batching a
couple of calls saves pennies and adds latency); **Android stays live** (saving ~$0.15
isn't worth the complexity at ~46 q/mo).

## Notes
- All figures are well under the $50/run circuit-breaker.
- Cost scales with the enriched text size; if it ever grows, re-baseline the unit rate with the Bucket-0 preview: `uv run scripts/llm_insights_cost.py <month> <month> <product>`.
