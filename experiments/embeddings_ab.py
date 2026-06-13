"""Phase 4 — embedding A/B test.

Hypothesis: a sentence-embedding cosine similarity between each candidate's
career text and the JD adds relevance signal the rules scorer misses, and
should be added to the pipeline only if it improves the contest composite
on the local labeled set (the agreed "embeddings only if proven" decision).

We deliberately expect this to add little: the dataset's career descriptions
are drawn from a finite template pool, so a dense embedding largely recovers
the same phrase-presence signal the rules already capture. This script
measures whether that intuition holds.

Setup (dev-time only — the core ranker stays stdlib-only and network-free):
    pip install fastembed numpy
Then:
    python experiments/embeddings_ab.py

Reports composite + components for: rules-only, embed-only, and several
rules/embed blends, plus a rules-gated rerank. Prints a verdict and the
recommended action. Results are written to experiments/embeddings_ab_result.md.
"""

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.filters import honeypot_flags, passes_relevance_gate
from src.scoring import score_candidate, _career_text
from eval.evaluate import ndcg_at, average_precision

EVAL_DIR = Path(__file__).parent.parent / "eval"
OUT = Path(__file__).parent / "embeddings_ab_result.md"

# Focused JD query: the must-haves distilled from job_description.docx.
# Kept short so it fits the MiniLM context and isn't diluted by the JD's
# long narrative passages.
JD_QUERY = (
    "Senior AI engineer owning production ranking, retrieval and recommendation "
    "systems that decide what recruiters and candidates see. Deep ML systems "
    "depth: embeddings, hybrid retrieval, learning-to-rank, LLM-based re-ranking, "
    "fine-tuning, semantic and vector search, BM25, evaluation with NDCG and "
    "offline/online A/B tests. Scrappy product engineering: ship a working ranker "
    "fast at a product company. 5 to 9 years experience, India based."
)


def composite(scored, labels):
    """scored: list of (score, cid) ; returns metric dict (contest mix)."""
    scored = sorted(scored, key=lambda x: (-x[0], x[1]))
    tiers = [labels[c] for _, c in scored]
    rel = [1 if t >= 3 else 0 for t in tiers]
    m = {
        "NDCG@10": ndcg_at(tiers, 10),
        "NDCG@50": ndcg_at(tiers, 50),
        "MAP": average_precision(rel),
        "P@10": sum(rel[:10]) / 10,
    }
    m["composite"] = 0.50 * m["NDCG@10"] + 0.30 * m["NDCG@50"] + 0.15 * m["MAP"] + 0.05 * m["P@10"]
    return m


def fmt(m):
    return (f"composite={m['composite']:.4f}  NDCG@10={m['NDCG@10']:.4f}  "
            f"NDCG@50={m['NDCG@50']:.4f}  MAP={m['MAP']:.4f}  P@10={m['P@10']:.3f}")


def main():
    labels = {}
    with open(EVAL_DIR / "labels.jsonl", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                labels[rec["candidate_id"]] = rec["tier"]

    cands, texts, rules = {}, {}, {}
    filtered = set()
    with open(EVAL_DIR / "sample_candidates.jsonl", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            c = json.loads(line)
            cid = c["candidate_id"]
            if cid not in labels:
                continue
            cands[cid] = c
            texts[cid] = _career_text(c)
            if honeypot_flags(c) or not passes_relevance_gate(c):
                filtered.add(cid)
                rules[cid] = -1.0
            else:
                rules[cid], _ = score_candidate(c)

    ids = list(cands)
    print(f"labeled candidates: {len(ids)} ({len(filtered)} filtered by gate/honeypot)")

    # --- embeddings ---------------------------------------------------------
    from fastembed import TextEmbedding
    model = TextEmbedding("sentence-transformers/all-MiniLM-L6-v2")
    print("embedding JD + career texts (MiniLM, CPU)...")
    jd_vec = np.array(list(model.embed([JD_QUERY]))[0], dtype=np.float32)
    jd_vec /= np.linalg.norm(jd_vec) + 1e-9

    cand_vecs = np.array(list(model.embed([texts[c] for c in ids])), dtype=np.float32)
    cand_vecs /= (np.linalg.norm(cand_vecs, axis=1, keepdims=True) + 1e-9)
    cos = cand_vecs @ jd_vec  # cosine in [-1, 1], typically [0, 0.7] here
    cos_by_id = dict(zip(ids, cos))

    # Fixed, set-INDEPENDENT cosine -> feature transform. The bounds come from
    # the JD-cosine geometry (observed range ~[0.46, 0.76] across the pool),
    # NOT from optimizing on labels, so this is identical in production on the
    # full pool — no normalization leakage. clip keeps it in [0,1].
    EMBED_COS_FLOOR, EMBED_COS_SPAN = 0.45, 0.32
    embed_norm = {
        c: max(0.0, min(1.0, (float(cos_by_id[c]) - EMBED_COS_FLOOR) / EMBED_COS_SPAN))
        for c in ids
    }

    # --- variants -----------------------------------------------------------
    results = {}

    results["rules_only"] = composite([(rules[c], c) for c in ids], labels)
    # Embed-only: filtered candidates still forced to the bottom (the gate is
    # a hard honeypot/relevance guard regardless of the relevance signal used).
    results["embed_only"] = composite(
        [(-1.0 if c in filtered else float(cos_by_id[c]), c) for c in ids], labels
    )

    for a in (0.10, 0.20, 0.30, 0.40, 0.50):
        blended = []
        for c in ids:
            if c in filtered:
                blended.append((-1.0, c))
            else:
                blended.append(((1 - a) * rules[c] + a * embed_norm[c], c))
        results[f"blend_a{a:.2f}"] = composite(blended, labels)

    # Rules-gated rerank: keep the rules top-K, reorder only within it by a
    # gentle embed nudge. Tests whether embeddings help ORDER the top without
    # disturbing the rules gate. (K covers the contest's scored window.)
    for a in (0.10, 0.20):
        nudged = []
        for c in ids:
            if c in filtered:
                nudged.append((-1.0, c))
            else:
                nudged.append((rules[c] + a * (embed_norm[c] - 0.5) * 0.2, c))
        results[f"rerank_a{a:.2f}"] = composite(nudged, labels)

    # --- report -------------------------------------------------------------
    base = results["rules_only"]["composite"]
    lines = ["# Embedding A/B result (Phase 4)\n",
             f"Model: all-MiniLM-L6-v2 (fastembed/ONNX, CPU). Labeled set: {len(ids)} candidates.\n",
             f"JD query: {JD_QUERY}\n",
             "| variant | composite | NDCG@10 | NDCG@50 | MAP | P@10 | vs rules |",
             "|---|---|---|---|---|---|---|"]
    print()
    for name, m in results.items():
        delta = m["composite"] - base
        print(f"{name:14s} {fmt(m)}  d={delta:+.4f}")
        lines.append(
            f"| {name} | {m['composite']:.4f} | {m['NDCG@10']:.4f} | {m['NDCG@50']:.4f} "
            f"| {m['MAP']:.4f} | {m['P@10']:.3f} | {delta:+.4f} |"
        )

    best = max(results.items(), key=lambda kv: kv[1]["composite"])
    improved = best[1]["composite"] > base + 1e-4 and best[0] != "rules_only"
    verdict = (
        f"\nBest variant: **{best[0]}** (composite {best[1]['composite']:.4f}, "
        f"{best[1]['composite'] - base:+.4f} vs rules-only {base:.4f}).\n\n"
    )
    if improved:
        verdict += (
            "**Verdict: embeddings help on the labeled set.** Consider adding the "
            "embedding cosine as a feature — but weigh the operational cost: shipping "
            "it means bundling model weights and an ONNX/torch runtime into the "
            "no-network ranking step, breaking the stdlib-only core. Re-run on the "
            "full pool and confirm the 5-min/16-GB budget before adopting.\n"
        )
    else:
        verdict += (
            "**Verdict: embeddings do NOT improve the composite over the rules "
            "scorer.** As hypothesized, the finite-template career descriptions mean "
            "a dense embedding mostly re-encodes the same phrase-presence signal the "
            "rules already capture. Decision: keep the stdlib-only rules scorer; do "
            "not add an embedding dependency to the ranking pipeline. This experiment "
            "is retained as methodology evidence.\n"
        )
    print(verdict)
    OUT.write_text("\n".join(lines) + "\n" + verdict, encoding="utf-8")
    print(f"written to {OUT}")


if __name__ == "__main__":
    main()
