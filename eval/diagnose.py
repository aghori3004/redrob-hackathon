"""Throwaway diagnostic: dump component breakdown for labeled candidates,
ordered by model score, so we can see what blurs tier-5/4/3 separation.

    python eval/diagnose.py            # top 25 by model score
    python eval/diagnose.py --tier 5   # only labeled tier-5 candidates
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.filters import honeypot_flags, passes_relevance_gate
from src.scoring import score_candidate

EVAL_DIR = Path(__file__).parent


def load():
    labels = {}
    with open(EVAL_DIR / "labels.jsonl", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                labels[rec["candidate_id"]] = rec["tier"]
    cands = {}
    with open(EVAL_DIR / "sample_candidates.jsonl", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                c = json.loads(line)
                cands[c["candidate_id"]] = c
    return labels, cands


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", type=int, default=None)
    ap.add_argument("--n", type=int, default=25)
    args = ap.parse_args()

    labels, cands = load()
    rows = []
    for cid, tier in labels.items():
        c = cands.get(cid)
        if c is None:
            continue
        if honeypot_flags(c):
            rows.append((-1.0, cid, tier, {"filtered": "honeypot"}))
            continue
        if not passes_relevance_gate(c):
            rows.append((-1.0, cid, tier, {"filtered": "gate"}))
            continue
        score, ev = score_candidate(c)
        rows.append((score, cid, tier, ev))

    rows.sort(key=lambda x: (-x[0], x[1]))
    if args.tier is not None:
        rows = [r for r in rows if r[2] == args.tier]
    rows = rows[: args.n]

    for rank, (score, cid, tier, ev) in enumerate(rows, 1):
        c = cands[cid]
        p = c["profile"]
        comp = ev.get("components", {})
        core = ev.get("core", {})
        print(
            f"#{rank:2d} s={score:.4f} T{tier} {cid} | {p.get('current_title','?')} | "
            f"{p.get('years_of_experience')}y | {p.get('location')}"
        )
        if "filtered" in ev:
            print(f"      FILTERED: {ev['filtered']}")
            continue
        print(
            f"      comp={comp} dq={ev.get('disqualifiers')} "
            f"avail={ev['behavioral']['availability_multiplier']}"
        )
        print(f"      A={core.get('tier_a')} B={core.get('tier_b')} title={core.get('title_score')}")


if __name__ == "__main__":
    main()
