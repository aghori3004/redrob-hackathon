"""Build a labeling queue from the submission's top-N candidates.

The submission CSV only carries candidate_ids, not full profiles. This script
pulls the full records for the top-N ids out of the 100K pool (one streaming
pass), writes them to:

  eval/label_queue.jsonl      — full records (+ _rank, _model_score) for label_cli.py
  eval/submission_digests.md  — human-readable digests, in rank order

and merges those records into eval/sample_candidates.jsonl (deduped) so that
eval/evaluate.py can actually score them against your new labels — it only
scores candidates present in that file.

The worksheet deliberately shows the model's RANK (you already know these are
the top picks) but NOT any suggested tier — you assign the tier yourself from
the rubric, which is the whole point of independent human ground truth.

Usage:
    python eval/make_worksheet.py \
        --candidates "../[PUB] India_runs_data_and_ai_challenge/India_runs_data_and_ai_challenge/candidates.jsonl" \
        --top 50
"""

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.loader import iter_candidates
from eval.label_tool import digest

EVAL_DIR = Path(__file__).parent
REPO_ROOT = EVAL_DIR.parent


def read_submission(path, top_n):
    rows = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append((row["candidate_id"], int(row["rank"]), row["score"]))
    rows.sort(key=lambda r: r[1])
    return rows[:top_n]


def merge_into_sample(records):
    """Append records to sample_candidates.jsonl, deduped by candidate_id."""
    sample_path = EVAL_DIR / "sample_candidates.jsonl"
    existing_ids = set()
    if sample_path.exists():
        with open(sample_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    existing_ids.add(json.loads(line)["candidate_id"])
    added = 0
    with open(sample_path, "a", encoding="utf-8") as f:
        for cand in records:
            if cand["candidate_id"] in existing_ids:
                continue
            rec = dict(cand)
            rec["_stratum"] = "submission_top"
            f.write(json.dumps(rec) + "\n")
            added += 1
    return added


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates", required=True, help="path to candidates.jsonl(.gz)")
    parser.add_argument("--submission", default=str(REPO_ROOT / "submission.csv"))
    parser.add_argument("--top", type=int, default=50, help="how many top-ranked candidates to queue")
    parser.add_argument("--no-merge", action="store_true", help="don't merge into sample_candidates.jsonl")
    args = parser.parse_args()

    targets = read_submission(args.submission, args.top)
    want = {cid: (rank, score) for cid, rank, score in targets}
    print(f"looking for {len(want)} candidates from {args.submission} (top {args.top})...")

    found = {}
    for cand in iter_candidates(args.candidates):
        cid = cand["candidate_id"]
        if cid in want:
            found[cid] = cand
            if len(found) == len(want):
                break

    missing = set(want) - set(found)
    if missing:
        print(f"WARNING: {len(missing)} ids not found in pool: {sorted(missing)[:5]}...")

    # Ordered by model rank.
    ordered = [found[cid] for cid, _, _ in targets if cid in found]

    queue_path = EVAL_DIR / "label_queue.jsonl"
    with open(queue_path, "w", encoding="utf-8") as f:
        for cand in ordered:
            rank, score = want[cand["candidate_id"]]
            rec = dict(cand)
            rec["_rank"] = rank
            rec["_model_score"] = score
            f.write(json.dumps(rec) + "\n")

    digests_path = EVAL_DIR / "submission_digests.md"
    with open(digests_path, "w", encoding="utf-8") as f:
        f.write("# Submission top-N — labeling worksheet\n\n")
        f.write("Assign a tier 0–5 per eval/rubric.md. Rank shown for context only; "
                "judge the profile, not the rank.\n\n")
        for cand in ordered:
            rank, _ = want[cand["candidate_id"]]
            f.write(f"\n---\n\n**model rank #{rank}**\n\n")
            f.write(digest(cand, "submission_top") + "\n\n")
            f.write("`tier: ___`  notes: \n\n")

    print(f"wrote {len(ordered)} records to {queue_path}")
    print(f"wrote worksheet to {digests_path}")
    if not args.no_merge:
        added = merge_into_sample(ordered)
        print(f"merged {added} new records into eval/sample_candidates.jsonl (so evaluate.py can score them)")
    print("\nNow label them fast with:  python eval/label_cli.py")


if __name__ == "__main__":
    main()
