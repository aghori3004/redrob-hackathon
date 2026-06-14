"""Fast interactive labeler — RANDOM across the full quality spectrum.

Run in YOUR terminal:

    python eval/label_cli.py

Instead of marching down the submission top-50 in rank order (which biases you
toward saying "yes, strong" again and again), this draws candidates in RANDOM
order from eval/sample_candidates.jsonl — a stratified mix deliberately built to
span the whole spectrum: gold ML-titled pros, plain-language strong profiles
hiding without an ML title, gated-out tech, non-tech keyword-stuffers,
honeypots, and an unconditioned random slice of the pool. Good and bad come
shuffled together, so each judgment stands on its own and you stay unbiased.

You are NOT shown the model's rank or which stratum a profile came from — that
is the point: judge the profile cold. You ARE shown the model's suggested tier
with its reasoning (a suggestion to challenge, not ground truth — it comes from
the same scorer these labels audit) and the job's judging criteria, so labeling
stays fast.

Controls:
    [Enter]    ACCEPT the model's suggested tier
    0-5        OVERRIDE with your own tier (optionally add a note:  3 too junior)
    s          skip for now (stays unlabeled)
    b          go back to the previous candidate
    q          save and quit

Every label is written to eval/labels.jsonl immediately (a human label overrides
any prior Claude label for the same candidate), so it is always safe to quit.
Re-running resumes where you left off — already human-labeled candidates are
skipped unless you pass --relabel. The random order is seeded (--seed, default
42) so the sequence is stable across sessions; pass a different seed to reshuffle.

Use --queue to fall back to the old top-50 submission queue (label_queue.jsonl).
"""

import argparse
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from eval.label_tool import digest
from eval.suggest import suggest_tier

EVAL_DIR = Path(__file__).parent
LABELS = EVAL_DIR / "labels.jsonl"
QUEUE = EVAL_DIR / "label_queue.jsonl"
SAMPLE = EVAL_DIR / "sample_candidates.jsonl"

JOB_WANTS = """WHAT THIS JOB WANTS (judge career DESCRIPTIONS, not titles, never the skills list):
  - Has actually BUILT ranking / search / recommendation / retrieval systems for real users
  - At a PRODUCT company (not pure consulting: TCS/Infosys/Wipro/Accenture...)
  - ~6-8 years experience, based in India (or clearly willing to relocate there)
  - Still REACHABLE: logs in, responds to recruiters

INSTANT DOWNGRADES (apply regardless of how strong the rest looks):
  - Pure academic/research career, never shipped to production .......... -> tier 1
  - Outside India and won't relocate (no visa sponsorship) .............. -> tier 1
  - "AI" is only recent LangChain/OpenAI-wrapper work, no real prior ML .. -> tier 2
  - Senior who stopped coding (architect/manager, nothing built ~18mo) ... -> tier 2
  - Effectively unreachable (no login 6mo+ AND ignores recruiters) ....... -> tier 2
  - Consulting-only career / title-chaser / CV-speech-no-NLP ............ -> drop a tier

NOTE: career descriptions are drawn from a shared template pool — the same
paragraphs recur across many profiles (sometimes with the company swapped).
That is the data generator, NOT a fake-profile signal: do not downgrade for it.

TIER LADDER (ask: would the hiring manager spend an interview slot on them?):
  5 ideal   4 strong (1-2 minor worries)   3 relevant but real gap
  2 competent tech, no production ML/IR    1 wrong specialty / keyword-only    0 non-tech / honeypot"""


def load_labels():
    labels = {}
    if LABELS.exists():
        with open(LABELS, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    rec = json.loads(line)
                    labels[rec["candidate_id"]] = rec
    return labels


def save_labels(labels):
    with open(LABELS, "w", encoding="utf-8") as f:
        for rec in labels.values():
            f.write(json.dumps(rec) + "\n")


def load_records(path, what):
    if not path.exists():
        sys.exit(f"No {what} found at {path}.")
    recs = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                recs.append(json.loads(line))
    return recs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--relabel", action="store_true", help="re-show already-human-labeled candidates")
    parser.add_argument("--queue", action="store_true",
                        help="use the old top-50 submission queue (label_queue.jsonl) instead of a random draw")
    parser.add_argument("--seed", type=int, default=42, help="shuffle seed for the random draw (change to reshuffle)")
    parser.add_argument("--blind", action="store_true",
                        help="hide the model's suggested tier so your judgment can't anchor to the scorer "
                             "(de-biases the eval; the suggestion is still recorded silently for agreement analysis)")
    parser.add_argument("--order", choices=("random", "model"), default="random",
                        help="random (default) = draw across all strata; model = highest model-score first, "
                             "so you label the TOP of the ranking (where NDCG@10 value and positives concentrate)")
    args = parser.parse_args()

    if args.queue:
        pool = load_records(QUEUE, "queue (run make_worksheet.py first)")
        mode = "submission top-50 (rank order)"
    else:
        pool = load_records(SAMPLE, "sample (run make_worksheet.py / label_tool.py first)")
        if args.order == "model":
            pool.sort(key=lambda c: suggest_tier(c)[2], reverse=True)
            mode = "model-score descending (top of ranking first)"
        else:
            random.Random(args.seed).shuffle(pool)
            mode = f"random draw across all strata (seed {args.seed})"
    if args.blind:
        mode += " | BLIND (suggestion hidden)"

    labels = load_labels()
    human_ids = {cid for cid, r in labels.items() if r.get("source") == "human"}

    todo = [c for c in pool if args.relabel or c["candidate_id"] not in human_ids]
    if not todo:
        print(f"All {len(pool)} candidates already human-labeled. Use --relabel to revisit.")
        return

    print(f"Mode: {mode}")
    print(f"{len(todo)} of {len(pool)} candidates to label "
          f"({len(pool) - len(todo)} already human-labeled).")

    i = 0
    while 0 <= i < len(todo):
        cand = todo[i]
        cid = cand["candidate_id"]
        sug_tier, sug_reason, model_score = suggest_tier(cand)
        prior = labels.get(cid)
        prior_human = prior.get("tier") if prior and prior.get("source") == "human" else None

        print("\n" + "=" * 80)
        print(f"[{i + 1}/{len(todo)}]   {cid}"
              + (f"   (your current label: tier {prior_human})" if prior_human is not None else ""))
        print("=" * 80)
        # Neutral stratum label: do NOT leak rank or stratum, so the judgment is cold.
        print(digest(cand, "profile"))
        print("\n" + "-" * 80)
        print(JOB_WANTS)
        print("-" * 80)
        if args.blind:
            print(">> BLIND: judge cold, then enter your tier (the model's view is hidden).")
            print("-" * 80)
            prompt = "0-5=tier  |  s skip  b back  q quit > "
        else:
            print(f">> MODEL SUGGESTS:  TIER {sug_tier}   (rules score {model_score})")
            print(f"   reasoning: {sug_reason}")
            print("-" * 80)
            prompt = f"[Enter]=accept tier {sug_tier}  |  0-5=override  |  s skip  b back  q quit > "

        raw = input(prompt).strip()

        if raw == "":  # accept the suggestion (disabled in blind mode — nothing shown to accept)
            if args.blind:
                print("  blind mode: type a digit 0-5 (no suggestion to accept)")
                continue
            labels[cid] = {"candidate_id": cid, "tier": sug_tier, "model_tier": sug_tier,
                           "agreed": True, "note": "", "source": "human"}
            save_labels(labels)
            i += 1
            continue

        cmd = raw[0].lower()
        if cmd == "q":
            break
        if cmd == "s":
            i += 1
            continue
        if cmd == "b":
            i = max(0, i - 1)
            continue
        if cmd in "012345":
            tier = int(cmd)
            note = raw[1:].strip()
            labels[cid] = {"candidate_id": cid, "tier": tier, "model_tier": sug_tier,
                           "agreed": tier == sug_tier, "note": note, "source": "human"}
            save_labels(labels)
            if tier != sug_tier:
                print(f"   challenged: you said tier {tier}"
                      + (f" — {note}" if note else " (consider adding a note next time)"))
            i += 1
        else:
            print("  ? press Enter to accept, a digit 0-5 to override, or s / b / q")

    human = [r for r in labels.values() if r.get("source") == "human"]
    challenged = [r for r in human if not r.get("agreed", True)]
    print(f"\nSaved. {len(human)} human labels total ({len(challenged)} where you overrode the model).")
    print("Re-measure with:  python eval/evaluate.py --log --note \"human labels\"")


if __name__ == "__main__":
    main()
