"""Redrob ranker entry point.

Usage:
    python rank.py --candidates ./candidates.jsonl --out ./submission.csv

Single streaming pass over the pool: honeypot checks -> relevance gate ->
scoring -> top-100 CSV. Stdlib only, CPU only, no network.
"""

import argparse
import csv
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.loader import iter_candidates
from src.filters import honeypot_flags, passes_relevance_gate
from src.scoring import score_candidate, _career_text
from src.reasoning import reasoning_for
from src import embedding

TOP_N = 100


def run(candidates_path, out_path, verbose=True):
    t0 = time.time()
    total = 0
    honeypots = 0
    gated_out = 0
    scored = []

    for cand in iter_candidates(candidates_path):
        total += 1
        if honeypot_flags(cand):
            honeypots += 1
            continue
        if not passes_relevance_gate(cand):
            gated_out += 1
            continue
        score, evidence = score_candidate(cand)
        scored.append((score, cand["candidate_id"], cand, evidence))

    # Highest rules score first; equal scores ordered by candidate_id ascending
    # (the validator enforces exactly this tie-break).
    scored.sort(key=lambda x: (-x[0], x[1]))

    # Embedding blend (Phase 4, adopted): refine the ordering with a MiniLM
    # JD-cosine feature. Only the rules top-K are embedded — the blend adds at
    # most EMBED_WEIGHT, so nothing outside the rules top-K can reach the
    # top-100 (keeps us inside the 5-min budget). Degrades to rules-only if the
    # model/deps are absent, so the repo always runs.
    use_embed = embedding.is_available()
    if use_embed:
        k = min(embedding.EMBED_TOPK, len(scored))
        feats = embedding.embed_features(_career_text(row[2]) for row in scored[:k])
        for i, f in enumerate(feats):
            s, cid, cand, ev = scored[i]
            ev["embed_feature"] = round(f, 4)
            scored[i] = (embedding.blend(s, f), cid, cand, ev)
        scored.sort(key=lambda x: (-x[0], x[1]))

    top = scored[:TOP_N]

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["candidate_id", "rank", "score", "reasoning"])
        for rank, (score, cid, cand, evidence) in enumerate(top, start=1):
            writer.writerow([cid, rank, f"{score:.6f}", reasoning_for(cand, evidence, rank)])

    if verbose:
        elapsed = time.time() - t0
        mode = "rules+embed blend" if use_embed else "rules-only (no embed model)"
        print(f"pool: {total} | honeypots: {honeypots} | gated out: {gated_out} | scored: {len(scored)} | {mode}")
        print(f"wrote top {len(top)} to {out_path} in {elapsed:.1f}s")
        print("\ntop 10 preview:")
        for rank, (score, cid, cand, evidence) in enumerate(top[:10], start=1):
            p = cand["profile"]
            print(
                f"{rank:3d} {score:.4f} {cid} | {p['current_title']} @ {p['current_company']}"
                f" | {p['years_of_experience']}y | {p['location']}"
                f" | A:{evidence['core']['tier_a']} dq:{evidence['disqualifiers']}"
                f" avail:{evidence['behavioral']['availability_multiplier']}"
            )

    return top


def main():
    parser = argparse.ArgumentParser(description="Rank candidates against the Redrob JD.")
    parser.add_argument("--candidates", required=True, help="Path to candidates.jsonl(.gz)")
    parser.add_argument("--out", required=True, help="Path for the submission CSV")
    args = parser.parse_args()
    run(args.candidates, args.out)


if __name__ == "__main__":
    main()
