"""Stratified sampler for the hand-labeled eval set.

Streams the full pool once, classifies every candidate into a stratum, and
reservoir-samples a fixed quota per stratum (seeded, so the sample is
reproducible). Emits:

  eval/sample_candidates.jsonl  — full records + stratum tag (input to evaluate.py)
  eval/sample_digests.md        — compact human-readable digests for labeling

Strata are chosen so every failure mode the dataset plants is represented.
"""

import argparse
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.loader import iter_candidates
from src.filters import honeypot_flags, passes_relevance_gate
from src.scoring import ML_TITLE_RE

QUOTAS = {
    "ml_titled": 50,        # the gold pockets: direct competition pool
    "adjacent_in": 50,      # passed gate without ML title (plain-language Tier 5s hide here)
    "tech_out": 30,         # gated-out tech titles (gate false-negative check)
    "nontech_out": 30,      # gated-out non-tech (keyword stuffer territory)
    "honeypot": 20,         # of the ~60 flagged (honeypot check verification)
    "random": 20,           # unconditioned slice of the pool
}
SEED = 42


def classify(cand):
    if honeypot_flags(cand):
        return "honeypot"
    titles = " | ".join(
        [cand.get("profile", {}).get("current_title", "")]
        + [j.get("title", "") for j in cand.get("career_history", [])]
    )
    gated_in = passes_relevance_gate(cand)
    if gated_in:
        return "ml_titled" if ML_TITLE_RE.search(titles) else "adjacent_in"
    tech_markers = (
        "Engineer", "Developer", "Analyst", "Architect", "DevOps", "QA",
        "Scientist", "Programmer",
    )
    if any(m in titles for m in tech_markers):
        return "tech_out"
    return "nontech_out"


def digest(cand, stratum):
    p = cand["profile"]
    sig = cand["redrob_signals"]
    lines = [
        f"### {cand['candidate_id']}  [{stratum}]",
        f"**{p['current_title']}** @ {p['current_company']} ({p['current_industry']}, "
        f"{p['current_company_size']}) | {p['years_of_experience']}y | {p['location']}, {p['country']}",
        f"_Summary:_ {p['summary']}",
        "_Career:_",
    ]
    for j in cand["career_history"]:
        lines.append(
            f"- {j['title']} @ {j['company']} ({j['industry']}, {j['company_size']}, "
            f"{j['duration_months']}mo{', current' if j.get('is_current') else ''}): {j['description']}"
        )
    for e in cand.get("education", []):
        lines.append(
            f"_Edu:_ {e['degree']} {e['field_of_study']}, {e['institution']} ({e.get('tier', '?')})"
        )
    expert_short = [
        f"{s['name']}({s.get('duration_months')}mo)"
        for s in cand.get("skills", [])
        if s.get("proficiency") == "expert" and isinstance(s.get("duration_months"), int) and s["duration_months"] <= 6
    ]
    lines.append(
        f"_Signals:_ last_active {sig['last_active_date']}, response_rate {sig['recruiter_response_rate']}, "
        f"open_to_work {sig['open_to_work_flag']}, notice {sig['notice_period_days']}d, "
        f"relocate {sig['willing_to_relocate']}, interview_completion {sig['interview_completion_rate']}, "
        f"github {sig['github_activity_score']}"
    )
    if expert_short:
        lines.append(f"_Suspect expert skills (<=6mo):_ {', '.join(expert_short)}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True)
    args = parser.parse_args()

    rng = random.Random(SEED)
    reservoirs = {k: [] for k in QUOTAS}
    seen = {k: 0 for k in QUOTAS}
    rand_seen = 0

    for cand in iter_candidates(args.candidates):
        # Independent reservoir for the unconditioned slice.
        rand_seen += 1
        if len(reservoirs["random"]) < QUOTAS["random"]:
            reservoirs["random"].append(cand)
        else:
            j = rng.randrange(rand_seen)
            if j < QUOTAS["random"]:
                reservoirs["random"][j] = cand

        stratum = classify(cand)
        seen[stratum] += 1
        quota = QUOTAS[stratum]
        if len(reservoirs[stratum]) < quota:
            reservoirs[stratum].append(cand)
        else:
            j = rng.randrange(seen[stratum])
            if j < quota:
                reservoirs[stratum][j] = cand

    out_dir = Path(__file__).parent
    picked_ids = set()
    with open(out_dir / "sample_candidates.jsonl", "w", encoding="utf-8") as f_jsonl, open(
        out_dir / "sample_digests.md", "w", encoding="utf-8"
    ) as f_md:
        f_md.write("# Labeling digests (label per eval/rubric.md)\n\n")
        for stratum in QUOTAS:
            f_md.write(f"\n## Stratum: {stratum} ({len(reservoirs[stratum])})\n\n")
            for cand in reservoirs[stratum]:
                if cand["candidate_id"] in picked_ids:
                    continue  # random slice may duplicate a stratified pick
                picked_ids.add(cand["candidate_id"])
                rec = dict(cand)
                rec["_stratum"] = stratum
                f_jsonl.write(json.dumps(rec) + "\n")
                f_md.write(digest(cand, stratum) + "\n\n")

    print(f"strata seen: {seen}")
    print(f"sampled {len(picked_ids)} unique candidates")


if __name__ == "__main__":
    main()
