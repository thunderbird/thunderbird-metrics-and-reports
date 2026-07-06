"""Project "LLM Insights" — Stage 1 (map): per-question classification.

Reads one settled month of desktop questions and asks Claude to label each with
a structured record: a FREELY-DISCOVERED theme (not a fixed regex dictionary —
this is what Project 1 can't do), a coarse category, a 1-5 severity, a one-line
root-cause hypothesis, a short supporting quote, and whether it looks new/notable.

Design choices (see plan):
  - Structured outputs (output_config.format json_schema) → guaranteed-valid JSON.
  - Prompt caching on the shared instruction+schema system prefix → the ~700-tok
    prefix is billed once, then read at ~0.1x on every later batch.
  - Questions are sent in batches (default 10/call) to amortize the prefix and
    cut call count; each record echoes its `id` so results re-key safely.
  - Thinking omitted + effort=low: this is cheap classification, not reasoning.
  - Cost is ESTIMATED via the free count_tokens endpoint and GATED at $50 BEFORE
    any spend; actual cost is printed afterward from usage.

Usage:
  uv run scripts/llm_insights_classify.py 2026-06 --sample 20      # cheap validation
  uv run scripts/llm_insights_classify.py 2026-06                  # full month
"""
import sys
import os
import json
import argparse

sys.path.insert(0, "scripts")
from llm_insights_cost import build_enriched, dollars, gate, PRICING

MODEL = "claude-opus-4-8"
OUT = "LLM_INSIGHTS/{month}-{product}-labels.csv"

CATEGORIES = [
    "account-login", "send-receive", "calendar-tasks", "addons-extensions",
    "ui-ux", "migration-import", "performance-crash", "encryption-security",
    "settings-config", "spam-filters", "search-folders", "attachments",
    "sync-oauth", "other",
]

# The shared, stable prefix — cached. Keep it byte-identical across runs so the
# cache actually hits (no timestamps / per-run ids in here).
SYSTEM_PROMPT = """You are a support-data analyst for Thunderbird (the desktop \
email client). You read real user support questions from Mozilla SUMO and label \
each one so engineering management can see what to investigate.

For EACH question you are given (identified by `id`), produce one record:

- discovered_theme: a short, specific noun phrase naming the concrete problem \
(e.g. "Gmail OAuth re-authentication loop", "IMAP folders missing after 140 \
upgrade", "calendar invites not showing"). This is the most important field: \
name the ACTUAL problem in the user's words, do NOT fall back to a generic \
bucket. Group-able wording is good (reuse the same phrasing for the same \
problem across questions).
- category: the single closest coarse bucket from the allowed list.
- severity: integer 1-5 for user impact (1 = trivial/cosmetic or a how-to \
question, 3 = a feature is broken for this user, 5 = data loss, cannot send/\
receive at all, or a security exposure).
- root_cause_hypothesis: ONE sentence proposing the most likely underlying \
technical cause. If genuinely unclear, say what you'd need to know.
- supporting_quote: a short verbatim snippet (<= 200 chars) from the question \
that best evidences the theme. Copy exactly; do not paraphrase.
- is_new_or_notable: true if this reads like a fresh/emerging problem or an \
unusually acute case worth engineering attention, false for routine/how-to.

Write discovered_theme and root_cause_hypothesis in ENGLISH so the same problem \
groups across languages (the corpus is ~16% non-English); keep supporting_quote \
verbatim in the original language.

Base every judgment only on the text provided. Return all records for the \
batch."""

# JSON schema for the structured output. Wrapper object with a `results` array
# (top-level array + additionalProperties:false is the safest structured-output
# shape). No length/number constraints (unsupported by structured outputs) —
# severity is an enum of 1-5 instead.
SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "string"},
                    "discovered_theme": {"type": "string"},
                    "category": {"type": "string", "enum": CATEGORIES},
                    "severity": {"type": "integer", "enum": [1, 2, 3, 4, 5]},
                    "root_cause_hypothesis": {"type": "string"},
                    "supporting_quote": {"type": "string"},
                    "is_new_or_notable": {"type": "boolean"},
                },
                "required": ["id", "discovered_theme", "category", "severity",
                             "root_cause_hypothesis", "supporting_quote",
                             "is_new_or_notable"],
            },
        }
    },
    "required": ["results"],
}

# LLM-produced fields, then the carried value-signal fields (from build_enriched).
LABEL_FIELDS = ["id", "discovered_theme", "category", "severity",
                "root_cause_hypothesis", "supporting_quote", "is_new_or_notable"]
SIGNAL_FIELDS = ["created_date", "is_solved", "solved_by", "has_solution",
                 "last_answer_trusted", "has_trusted_answer",
                 "n_answers", "n_creator_answers"]
FIELDS = LABEL_FIELDS + SIGNAL_FIELDS


def build_batch_message(rows):
    """One user message carrying a batch of enriched questions as a JSON array.
    `text` is already the enriched question (question + creator follow-ups +
    accepted solution + trusted replies), assembled in build_enriched()."""
    items = [{"id": r["id"], "text": r["text"][:8000]} for r in rows]
    return ("Classify these questions. Return one record per id.\n\n"
            + json.dumps(items, ensure_ascii=False))


def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("month", help="YYYY-MM, e.g. 2026-06")
    ap.add_argument("--product", default="desktop", choices=["desktop", "android"])
    ap.add_argument("--sample", type=int, default=0,
                    help="classify only the first N questions (cheap validation)")
    ap.add_argument("--batch-size", type=int, default=10)
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    if not os.getenv("ANTHROPIC_API_KEY"):
        print("🛑 ANTHROPIC_API_KEY is not set. Export it before running "
              "(this is the first bucket that spends).", file=sys.stderr)
        sys.exit(2)
    from anthropic import Anthropic
    client = Anthropic()

    rows = build_enriched(args.month, args.product)
    if args.sample:
        rows = rows[:args.sample]
    signals_by_id = {r["id"]: {k: r[k] for k in SIGNAL_FIELDS} for r in rows}
    batches = list(chunk(rows, args.batch_size))
    print(f"{args.month} {args.product}: {len(rows)} questions in {len(batches)} "
          f"batch(es) of up to {args.batch_size} (model: {args.model})")

    system = [{"type": "text", "text": SYSTEM_PROMPT,
               "cache_control": {"type": "ephemeral"}}]

    # --- estimate BEFORE spending, then gate ---------------------------------
    est_in = 0
    for b in batches:
        msg = build_batch_message(b)
        try:
            ct = client.messages.count_tokens(
                model=args.model, system=system,
                messages=[{"role": "user", "content": msg}])
            est_in += ct.input_tokens
        except Exception:
            est_in += len(msg) // 3  # heuristic fallback
    est_out = len(rows) * 200  # ~200 out tok/question (high-ish)
    est = dollars(est_in, est_out, args.model)
    label = f"Stage-1 map: {args.month} {args.product} ({len(rows)} q, {args.model})"
    print(f"   estimated input ~{est_in:,} tok, output ~{est_out:,} tok")
    gate(est, label=label)

    # --- run -----------------------------------------------------------------
    results, usage = [], {"in": 0, "out": 0, "cache_read": 0, "cache_write": 0}
    for i, b in enumerate(batches, 1):
        msg = build_batch_message(b)
        resp = client.messages.create(
            model=args.model,
            max_tokens=8000,
            system=system,
            output_config={"format": {"type": "json_schema", "schema": SCHEMA},
                           "effort": "low"},
            messages=[{"role": "user", "content": msg}],
        )
        u = resp.usage
        usage["in"] += u.input_tokens
        usage["out"] += u.output_tokens
        usage["cache_read"] += getattr(u, "cache_read_input_tokens", 0) or 0
        usage["cache_write"] += getattr(u, "cache_creation_input_tokens", 0) or 0
        text = next(bl.text for bl in resp.content if bl.type == "text")
        recs = json.loads(text)["results"]
        results.extend(recs)
        print(f"   batch {i}/{len(batches)}: {len(recs)} records "
              f"(in {u.input_tokens}, out {u.output_tokens}, "
              f"cache_read {usage['cache_read']})")

    # --- actual cost (accounts for the cheap cache-read tier) ----------------
    in_rate, out_rate = PRICING[args.model]
    actual = (usage["in"] / 1e6 * in_rate
              + usage["cache_write"] / 1e6 * in_rate * 1.25
              + usage["cache_read"] / 1e6 * in_rate * 0.10
              + usage["out"] / 1e6 * out_rate)
    print(f"\n💵 ACTUAL cost: ${actual:.4f}  "
          f"(in {usage['in']:,} | cache_write {usage['cache_write']:,} | "
          f"cache_read {usage['cache_read']:,} | out {usage['out']:,})")
    if results:
        per_q = actual / len(results)
        print(f"   ${per_q:.5f}/question")

    # --- write ---------------------------------------------------------------
    # merge the carried value signals (created_date, solved, trusted-last, …)
    for rec in results:
        rec.update(signals_by_id.get(rec["id"], {k: "" for k in SIGNAL_FIELDS}))
    got = {rec["id"] for rec in results}
    missing = [qid for qid in signals_by_id if qid not in got]
    if missing:
        print(f"   ⚠️  {len(missing)} question(s) returned no label "
              f"(ids: {missing[:5]}{'…' if len(missing) > 5 else ''})")

    import pandas as pd
    out_path = args.out or OUT.format(month=args.month, product=args.product)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    odf = pd.DataFrame(results)[FIELDS]
    odf.to_csv(out_path, index=False)
    print(f"   wrote {len(odf)} rows → {out_path}")

    # sample preview for the checkpoint
    print("\n--- sample labels ---")
    for r in results[:5]:
        print(f"  [{r['id']}] sev{r['severity']} {r['category']:<16} "
              f"{r['discovered_theme']}")
        print(f"        why: {r['root_cause_hypothesis']}")


if __name__ == "__main__":
    main()
