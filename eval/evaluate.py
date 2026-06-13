"""Local evaluation: contest metrics over the hand-labeled sample.

Scores every labeled candidate with the current pipeline (honeypot-flagged
candidates are forced to the bottom, mirroring rank.py), ranks them, and
computes the contest's exact metric mix against the hand labels:

    composite = 0.50*NDCG@10 + 0.30*NDCG@50 + 0.15*MAP + 0.05*P@10

"Relevant" = tier >= 3. With --log, appends a row (with git commit) to
eval/runs.md so every scorer change has a recorded before/after.
"""

import argparse
import json
import math
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.filters import honeypot_flags, passes_relevance_gate
from src.scoring import score_candidate, _career_text
from src import embedding

EVAL_DIR = Path(__file__).parent


def ndcg_at(ranked_tiers, k):
    dcg = sum((2 ** t - 1) / math.log2(i + 2) for i, t in enumerate(ranked_tiers[:k]))
    ideal = sorted(ranked_tiers, reverse=True)
    idcg = sum((2 ** t - 1) / math.log2(i + 2) for i, t in enumerate(ideal[:k]))
    return dcg / idcg if idcg > 0 else 0.0


def average_precision(ranked_rel):
    hits = 0
    total = 0.0
    for i, rel in enumerate(ranked_rel, start=1):
        if rel:
            hits += 1
            total += hits / i
    n_rel = sum(ranked_rel)
    return total / n_rel if n_rel else 0.0


def evaluate():
    labels = {}
    with open(EVAL_DIR / "labels.jsonl", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                labels[rec["candidate_id"]] = rec["tier"]

    scored = []
    with open(EVAL_DIR / "sample_candidates.jsonl", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            cand = json.loads(line)
            cid = cand["candidate_id"]
            if cid not in labels:
                continue
            if honeypot_flags(cand) or not passes_relevance_gate(cand):
                score = -1.0  # filtered out = ranked below everything scored
                cand = None
            else:
                score, _ = score_candidate(cand)
            scored.append((score, cid, cand))

    # Mirror rank.py's embedding blend so local metrics reflect the shipped
    # pipeline. Gated/honeypot rows (cand is None) stay rules-only at -1.
    scored.sort(key=lambda x: (-x[0], x[1]))
    if embedding.is_available():
        k = min(embedding.EMBED_TOPK, len(scored))
        embeddable = [(i, row[2]) for i, row in enumerate(scored[:k]) if row[2] is not None]
        if embeddable:
            feats = embedding.embed_features(_career_text(c) for _, c in embeddable)
            for (i, _), f in zip(embeddable, feats):
                s, cid, cand = scored[i]
                scored[i] = (embedding.blend(s, f), cid, cand)
        scored.sort(key=lambda x: (-x[0], x[1]))

    scored = [(s, cid) for s, cid, _ in scored]
    ranked_tiers = [labels[cid] for _, cid in scored]
    ranked_rel = [1 if t >= 3 else 0 for t in ranked_tiers]

    metrics = {
        "n": len(scored),
        "NDCG@10": round(ndcg_at(ranked_tiers, 10), 4),
        "NDCG@50": round(ndcg_at(ranked_tiers, 50), 4),
        "MAP": round(average_precision(ranked_rel), 4),
        "P@10": round(sum(ranked_rel[:10]) / 10, 4),
    }
    metrics["composite"] = round(
        0.50 * metrics["NDCG@10"] + 0.30 * metrics["NDCG@50"]
        + 0.15 * metrics["MAP"] + 0.05 * metrics["P@10"], 4,
    )
    return metrics, scored, labels


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", action="store_true", help="append result to eval/runs.md")
    parser.add_argument("--note", default="", help="short description of the change being evaluated")
    args = parser.parse_args()

    metrics, scored, labels = evaluate()
    print(json.dumps(metrics, indent=1))

    print("\ntop 15 of labeled set (model order vs label):")
    for i, (score, cid) in enumerate(scored[:15], start=1):
        print(f"{i:3d} {score:7.4f} {cid} tier={labels[cid]}")

    misranked = [(s, c) for s, c in scored[:10] if labels[c] < 3]
    if misranked:
        print(f"\nWARNING: {len(misranked)} sub-relevant candidates in local top 10: {[c for _, c in misranked]}")

    if args.log:
        commit = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
            cwd=Path(__file__).parent.parent,
        ).stdout.strip()
        row = (
            f"| {datetime.now():%Y-%m-%d %H:%M} | {commit} | {metrics['composite']} "
            f"| {metrics['NDCG@10']} | {metrics['NDCG@50']} | {metrics['MAP']} "
            f"| {metrics['P@10']} | {args.note} |\n"
        )
        runs = EVAL_DIR / "runs.md"
        if not runs.exists():
            runs.write_text(
                "# Evaluation runs (local labeled set)\n\n"
                "| when | commit | composite | NDCG@10 | NDCG@50 | MAP | P@10 | note |\n"
                "|---|---|---|---|---|---|---|---|\n",
                encoding="utf-8",
            )
        with open(runs, "a", encoding="utf-8") as f:
            f.write(row)
        print(f"\nlogged to {runs}")


if __name__ == "__main__":
    main()
