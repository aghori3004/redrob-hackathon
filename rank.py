"""Redrob ranker entry point.

Usage:
    python rank.py --candidates ./candidates.jsonl --out ./submission.csv

Single streaming pass over the pool: honeypot checks -> relevance gate ->
scoring -> top-100 CSV. Stdlib only, CPU only, no network.
"""

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from src.loader import iter_candidates
from src.filters import honeypot_flags, passes_relevance_gate


def run(candidates_path, out_path):
    t0 = time.time()
    total = 0
    honeypots = 0
    gated_out = 0
    shortlist = []

    for cand in iter_candidates(candidates_path):
        total += 1
        if honeypot_flags(cand):
            honeypots += 1
            continue
        if not passes_relevance_gate(cand):
            gated_out += 1
            continue
        shortlist.append(cand)

    elapsed = time.time() - t0
    print(f"pool: {total}")
    print(f"honeypot-flagged: {honeypots}")
    print(f"gated out (no ML/IR relevance): {gated_out}")
    print(f"shortlist for scoring: {len(shortlist)}")
    print(f"elapsed: {elapsed:.1f}s")

    # Scoring + CSV emission arrive in the next phase.
    return shortlist


def main():
    parser = argparse.ArgumentParser(description="Rank candidates against the Redrob JD.")
    parser.add_argument("--candidates", required=True, help="Path to candidates.jsonl(.gz)")
    parser.add_argument("--out", required=True, help="Path for the submission CSV")
    args = parser.parse_args()
    run(args.candidates, args.out)


if __name__ == "__main__":
    main()
