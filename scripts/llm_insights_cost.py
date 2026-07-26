"""Project "LLM Insights" — shared cost harness + data loader.

Cost discipline is a first-class requirement for this project (see the plan):
every LLM step must PRINT an estimated cost BEFORE spending, and ABORT if the
estimate exceeds a hard ceiling ($50/run). This module is the single place that
knows model pricing, estimates token cost, and enforces the ceiling. It also
holds the reusable desktop-question loader (reusing Project 1's read idiom:
`csv.field_size_limit(sys.maxsize)`, `dtype=str, keep_default_na=False`, spam
filter) so every bucket loads data the same way.

Run directly for a $0 cost preview (Bucket 0 — no LLM calls):

  uv run scripts/llm_insights_cost.py 2026-05 2026-06

Token counting: if an Anthropic client + API key is available, uses the FREE
`messages.count_tokens` endpoint for accuracy; otherwise falls back to a
char-based heuristic (labeled as such). Either way, no billable tokens.
"""
import sys
import csv
import pandas as pd

csv.field_size_limit(sys.maxsize)

CONCAT_DIR = "CONCATENATED_FILES/{PRODUCT}"

# Hard circuit-breaker: no single run may exceed this estimated cost.
COST_CEILING_USD = 50.0

# Pricing per 1M tokens (input, output). Source: Claude API skill, cached
# 2026-06-24. Update if pricing changes. Batch API is 50% off both columns.
PRICING = {
    "claude-opus-5": (5.00, 25.00),     # same rates as opus-4-8 — see COSTS.md
    "claude-opus-4-8": (5.00, 25.00),
    "claude-sonnet-5": (3.00, 15.00),   # standard; intro $2/$10 through 2026-08-31
    "claude-haiku-4-5": (1.00, 5.00),
}

# Heuristic tokens-per-char for the Opus 4.7+ tokenizer when count_tokens is
# unavailable. ~1 token per 3.5 chars is deliberately conservative (over- rather
# than under-estimates) for English support text; empirically char/4 matched the
# measured corpus, so /3.5 leaves headroom.
_CHARS_PER_TOKEN = 3.5


def heuristic_tokens(text: str) -> int:
    """Rough token count from characters. Conservative (slightly high)."""
    return int(len(text or "") / _CHARS_PER_TOKEN)


def dollars(input_tokens: int, output_tokens: int, model: str,
            batch: bool = False) -> float:
    """Cost in USD for a given token split on a given model."""
    if model not in PRICING:
        raise ValueError(f"Unknown model {model!r}; add it to PRICING.")
    in_rate, out_rate = PRICING[model]
    cost = input_tokens / 1e6 * in_rate + output_tokens / 1e6 * out_rate
    return cost * 0.5 if batch else cost


def gate(estimate_usd: float, ceiling: float = COST_CEILING_USD,
         label: str = "run") -> None:
    """Abort hard if an estimate exceeds the ceiling. Call BEFORE any spend."""
    if estimate_usd > ceiling:
        print(f"\n🛑 ABORT: estimated cost for {label} is "
              f"${estimate_usd:,.2f}, over the ${ceiling:,.2f} ceiling.\n"
              f"   Stop and reconsider (smaller batch, cheaper model, or "
              f"sampling) before proceeding.", file=sys.stderr)
        sys.exit(1)
    print(f"✅ Estimate for {label}: ${estimate_usd:,.2f} "
          f"(under ${ceiling:,.0f} ceiling) — OK to proceed.")


class Refusal(RuntimeError):
    """The model declined the request (`stop_reason == "refusal"`)."""


def response_text(resp, label: str = "request") -> str:
    """The response's text block, failing loudly instead of with StopIteration.

    Opus 5's safety classifiers can decline a request: HTTP 200, `stop_reason
    "refusal"`, and an EMPTY content array. A bare
    `next(b.text for b in resp.content if b.type == "text")` raises
    StopIteration there — killing a run mid-way after every earlier batch has
    already been paid for. Callers that can skip one unit of work should catch
    RuntimeError and continue; single-call stages should let it propagate.
    """
    if getattr(resp, "stop_reason", None) == "refusal":
        cat = getattr(getattr(resp, "stop_details", None), "category", None)
        raise Refusal(f"{label}: declined by safety classifiers (category={cat})")
    for block in resp.content:
        if block.type == "text":
            return block.text
    raise RuntimeError(f"{label}: no text block in response "
                       f"(stop_reason={getattr(resp, 'stop_reason', None)})")


def load_questions(month: str, product: str = "desktop") -> pd.DataFrame:
    """Load one settled month of questions from the committed concat file,
    spam-filtered. Returns columns: id, created, title, content (+ the native
    operating_system / thunderbird_version, handy later).

    Reuses Project 1's read idiom. `month` is 'YYYY-MM'; `product` is
    desktop/android.
    """
    path = (f"{CONCAT_DIR.format(PRODUCT=product.upper())}/"
            f"{month}-sumo-{product}-questions.csv")
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    is_spam = df["is_spam"].str.strip().str.lower().isin(["true", "1", "yes"])
    df = df[~is_spam].copy()
    keep = ["id", "created", "title", "content",
            "operating_system", "thunderbird_version"]
    return df[[c for c in keep if c in df.columns]].reset_index(drop=True)


def question_text(row) -> str:
    """The text we send to the LLM per question (title + body)."""
    return f"{row.get('title', '')}\n{row.get('content', '')}"


# --- Enriched "question" model --------------------------------------------- #
# Per the user's definition, a "question" = the question body PLUS all answers by
# the question's own creator (their clarifications / "I tried X" / "turns out it
# was Y"). Two answer kinds are treated as HIGHER VALUE and fed to the LLM as
# authoritative context: (a) the accepted solution, and (b) trusted-contributor
# answers (especially the last answer in the thread). We also carry these as
# per-question signals so the reduce/ranking stage can weight them.

def _norm_id(s: str) -> str:
    """SUMO's `solution` column stores answer ids float-formatted ('1822588.0');
    answer `id`s are bare ints. Strip a trailing '.0' so they join."""
    s = (s or "").strip()
    return s[:-2] if s.endswith(".0") else s


def load_trusted_contributors(product: str = "desktop") -> set:
    """Set of trusted-contributor usernames for the product."""
    path = (f"{CONCAT_DIR.format(PRODUCT=product.upper())}/"
            f"thunderbird-{product}-trusted-contributors.csv")
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    return {c.strip() for c in df["creator"] if c.strip()}


import re as _re
import html as _html


def _strip_html(s: str) -> str:
    """SUMO content is HTML; strip tags + unescape entities to plain text
    (cheaper tokens, cleaner quotes)."""
    s = _re.sub(r"<[^>]+>", " ", s or "")
    s = _html.unescape(s)
    return _re.sub(r"[ \t]*\n[ \t]*", "\n", _re.sub(r"[ \t]+", " ", s)).strip()


def _clip(s: str, n: int) -> str:
    s = _strip_html(s)
    return s if len(s) <= n else s[:n] + "…"


def build_enriched(month: str, product: str = "desktop"):
    """Return a list of per-question dicts for one settled month. Each
    dict has:
      id, created, created_date, title, creator, os, tb_version,
      text          -- enriched text sent to the LLM (question + creator
                       follow-ups + accepted solution + trusted replies)
      is_solved, solved_by, has_solution,
      n_answers, n_creator_answers, has_trusted_answer, last_answer_trusted
    Spam is filtered from both questions and answers.
    """
    base = CONCAT_DIR.format(PRODUCT=product.upper())
    q = pd.read_csv(f"{base}/{month}-sumo-{product}-questions.csv",
                    dtype=str, keep_default_na=False)
    a = pd.read_csv(f"{base}/{month}-sumo-{product}-answers.csv",
                    dtype=str, keep_default_na=False)
    trusted = load_trusted_contributors(product)

    q = q[~q["is_spam"].str.strip().str.lower().isin(["true", "1", "yes"])].copy()
    a = a[~a["is_spam"].str.strip().str.lower().isin(["true", "1", "yes"])].copy()
    a["created_dt"] = pd.to_datetime(a["created"], utc=True, format="mixed",
                                     errors="coerce")

    # answers grouped per question, chronological
    ans_by_q = {}
    for _, r in a.sort_values("created_dt").iterrows():
        ans_by_q.setdefault(r["question_id"], []).append(r)
    ans_by_id = dict(zip(a["id"].map(str), a["content"]))

    out = []
    for _, r in q.iterrows():
        qid = r["id"]
        creator = r.get("creator", "").strip()
        ans = ans_by_q.get(qid, [])
        creator_ans = [x for x in ans if x["creator"].strip() == creator]
        trusted_ans = [x for x in ans if x["creator"].strip() in trusted]
        sol_id = _norm_id(r.get("solution", ""))
        sol_text = ans_by_id.get(sol_id, "")
        last = ans[-1] if ans else None
        last_trusted = bool(last is not None and last["creator"].strip() in trusted)

        # --- assemble the text the LLM reads ---
        parts = [f"[TITLE] {r.get('title', '')}",
                 f"\n[QUESTION]\n{_clip(r.get('content', ''), 6000)}"]
        if creator_ans:
            parts.append("\n[CREATOR FOLLOW-UPS] (same user adding detail)")
            for x in creator_ans:
                parts.append(f"- {_clip(x['content'], 1500)}")
        if sol_text:
            parts.append(f"\n[ACCEPTED SOLUTION by {r.get('solved_by','')}] "
                         f"(authoritative — reveals the fix/root cause)\n"
                         f"{_clip(sol_text, 2000)}")
        # trusted replies that aren't already the creator or the solution
        shown = {id(x) for x in creator_ans}
        trust_lines = []
        for x in trusted_ans:
            if id(x) in shown or _norm_id(x["id"]) == sol_id:
                continue
            tag = " (LAST IN THREAD)" if last is not None and x is last else ""
            trust_lines.append(f"- by {x['creator'].strip()}{tag}: "
                               f"{_clip(x['content'], 1200)}")
        if trust_lines:
            parts.append("\n[TRUSTED CONTRIBUTOR REPLIES] (higher value)")
            parts.extend(trust_lines)

        created_dt = pd.to_datetime(r.get("created", ""), utc=True,
                                    format="mixed", errors="coerce")
        out.append({
            "id": qid,
            "created": r.get("created", ""),
            "created_date": created_dt.date().isoformat()
                            if pd.notna(created_dt) else "",
            "title": (r.get("title", "") or "")[:120],
            "creator": creator,
            "os": r.get("operating_system", ""),
            "tb_version": r.get("thunderbird_version", ""),
            "text": "\n".join(parts),
            "is_solved": r.get("is_solved", ""),
            "solved_by": r.get("solved_by", ""),
            "has_solution": bool(sol_text),
            "n_answers": len(ans),
            "n_creator_answers": len(creator_ans),
            "has_trusted_answer": bool(trusted_ans),
            "last_answer_trusted": last_trusted,
        })
    return out


# --- Bucket-0 cost preview ------------------------------------------------- #

# Per-question modelling assumptions for the Stage-1 (map) classification pass.
# These are estimates only; Bucket 1 replaces them with a measured per-question
# cost on a 20-question sample.
_FRAMING_TOKENS_PER_Q = 30      # per-question JSON scaffolding around the text
_SYSTEM_PROMPT_TOKENS = 700     # shared instruction+schema prefix (cached once)
_OUT_TOKENS = {"low": 100, "expected": 160, "high": 260}   # structured label size


def preview_map_cost(months, product="desktop", model="claude-opus-4-8"):
    """Print a $0 projected-cost band for the Stage-1 map pass over the given
    months (list of 'YYYY-MM'). Uses count_tokens if a client is available,
    else the char heuristic."""
    client, counting = _maybe_client()
    grand_in = 0
    grand_q = 0
    print(f"\n=== LLM Insights — Bucket 0 cost preview ({product}, model: {model}) ===")
    print("Text per question = question + creator follow-ups + accepted "
          "solution + trusted replies.")
    print(f"Token counting: {'count_tokens (accurate, free)' if counting else 'char heuristic (~len/3.5)'}\n")
    for month in months:
        recs = build_enriched(month, product)
        texts = [r["text"] for r in recs]
        if counting:
            content_tok = sum(_count_tokens(client, model, t) for t in texts)
        else:
            content_tok = sum(heuristic_tokens(t) for t in texts)
        n = len(recs)
        in_tok = content_tok + n * _FRAMING_TOKENS_PER_Q + _SYSTEM_PROMPT_TOKENS
        grand_in += in_tok
        grand_q += n
        print(f"  {month} {product}: {n:>4} questions | "
              f"content ~{content_tok:>7,} tok | input ~{in_tok:>7,} tok")

    print(f"\n  TOTAL: {grand_q} questions | input ~{grand_in:,} tok")
    print(f"\n  Projected Stage-1 (map) cost band — {model}:")
    for band, out_per_q in _OUT_TOKENS.items():
        out_tok = grand_q * out_per_q
        live = dollars(grand_in, out_tok, model)
        batched = dollars(grand_in, out_tok, model, batch=True)
        print(f"    {band:<9} (out ~{out_per_q}/q): "
              f"live ${live:5.2f}  |  batch ${batched:5.2f}")
    # Gate on the high-band live estimate — the worst realistic case.
    worst = dollars(grand_in, grand_q * _OUT_TOKENS["high"], model)
    print()
    gate(worst, label=f"Stage-1 map over {'+'.join(months)} (high-band, live)")


def _maybe_client():
    """Return (client, True) if the Anthropic SDK + credentials are available,
    else (None, False). Never raises — Bucket 0 must run at $0 regardless."""
    import os
    if not os.getenv("ANTHROPIC_API_KEY"):
        return None, False
    try:
        from anthropic import Anthropic
        return Anthropic(), True
    except Exception:
        return None, False


def _count_tokens(client, model, text):
    try:
        r = client.messages.count_tokens(
            model=model, messages=[{"role": "user", "content": text}])
        return r.input_tokens
    except Exception:
        return heuristic_tokens(text)


if __name__ == "__main__":
    argv = sys.argv[1:]
    product = next((a for a in argv if a in ("desktop", "android")), "desktop")
    months = [a for a in argv if a not in ("desktop", "android")] or ["2026-05", "2026-06"]
    preview_map_cost(months, product)
