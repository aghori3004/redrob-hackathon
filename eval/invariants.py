"""Label-free invariant suite over the actual submission CSV.

These catch regressions no labeled sample can: they verify properties that
must hold for ANY good ranking of this pool. Run after producing
submission.csv from the full pool.

  python eval/invariants.py --candidates <pool.jsonl> --submission submission.csv
"""

import argparse
import copy
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.loader import iter_candidates
from src.filters import honeypot_flags
from src.scoring import score_candidate

# Keyword-stuffer picks from the organizers' sample_submission.csv top 10 —
# non-tech titles with AI skill lists. None may appear in our top 100.
STUFFER_IDS = {
    "CAND_0004989", "CAND_0001195", "CAND_0000339", "CAND_0001082",
    "CAND_0001218", "CAND_0004558", "CAND_0001753", "CAND_0001503", "CAND_0004548",
}


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f" — {detail}" if detail else ""))
    return ok


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--submission", required=True)
    args = parser.parse_args()

    with open(args.submission, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    top_ids = {r["candidate_id"] for r in rows}
    top10_ids = {r["candidate_id"] for r in rows if int(r["rank"]) <= 10}

    needed = {}
    honeypot_hits = []
    for cand in iter_candidates(args.candidates):
        cid = cand["candidate_id"]
        if cid in top_ids:
            needed[cid] = cand
            if honeypot_flags(cand):
                honeypot_hits.append(cid)

    all_ok = True

    all_ok &= check(
        "all top-100 ids exist in pool", len(needed) == len(top_ids),
        f"{len(needed)}/{len(top_ids)} found",
    )
    all_ok &= check(
        "zero honeypot-flagged in top 100", not honeypot_hits, str(honeypot_hits),
    )
    all_ok &= check(
        "no keyword-stuffer picks in top 100", not (top_ids & STUFFER_IDS),
        str(top_ids & STUFFER_IDS),
    )

    bad_geo = [
        cid for cid, c in needed.items()
        if c["profile"].get("country") != "India"
        and not c["redrob_signals"].get("willing_to_relocate")
    ]
    all_ok &= check("no non-India non-relocating in top 100", not bad_geo, str(bad_geo))

    stale = [
        cid for cid in top10_ids
        if needed[cid]["redrob_signals"].get("recruiter_response_rate", 1) <= 0.10
        and str(needed[cid]["redrob_signals"].get("last_active_date", "")) < "2025-12-01"
    ]
    all_ok &= check("top 10 contains no unreachable ghosts", not stale, str(stale))

    # Perturbation: injecting a disqualifier into a top-10 profile must
    # materially drop its score.
    probe = needed[sorted(top10_ids)[0]]
    base_score, _ = score_candidate(probe)

    consulting = copy.deepcopy(probe)
    for job in consulting["career_history"]:
        job["industry"] = "IT Services"
        job["company"] = "TCS"
    c_score, _ = score_candidate(consulting)
    all_ok &= check(
        "perturbation: consulting-only career drops score >30%",
        c_score < base_score * 0.7, f"{base_score:.3f} -> {c_score:.3f}",
    )

    ghost = copy.deepcopy(probe)
    ghost["redrob_signals"]["last_active_date"] = "2025-09-01"
    ghost["redrob_signals"]["recruiter_response_rate"] = 0.05
    ghost["redrob_signals"]["open_to_work_flag"] = False
    g_score, _ = score_candidate(ghost)
    all_ok &= check(
        "perturbation: ghost behavioral signals drop score >15%",
        g_score < base_score * 0.85, f"{base_score:.3f} -> {g_score:.3f}",
    )

    print("\nALL INVARIANTS PASS" if all_ok else "\nINVARIANT FAILURES PRESENT")
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
