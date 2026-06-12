# Redrob Ranker — Project Context

Hackathon entry: rank 100K synthetic candidates against the "Senior AI Engineer —
Founding Team" JD; submit top-100 CSV + this repo + a HuggingFace Spaces sandbox.

## Commands

```bash
# Reproduce the submission (the Stage-3-audited command):
python rank.py --candidates ./candidates.jsonl --out ./submission.csv

# Validate before submitting (bundle's validator):
python "../[PUB] India_runs_data_and_ai_challenge/India_runs_data_and_ai_challenge/validate_submission.py" submission.csv

# Local evaluation (Phase 3+):
python eval/evaluate.py
```

Data lives in `../[PUB] India_runs_data_and_ai_challenge/India_runs_data_and_ai_challenge/`
(candidates.jsonl, job_description.docx, submission_spec.docx, etc. — .docx text is
extractable via zipfile → word/document.xml).

## Hard constraints (Stage 3 reproduces in Docker and disqualifies violations)

- Ranking step: ≤5 min wall-clock, ≤16 GB RAM, CPU only, NO network (no LLM APIs).
- Contest score: 0.50·NDCG@10 + 0.30·NDCG@50 + 0.15·MAP + 0.05·P@10 (hidden ground truth).
- Honeypot rate >10% in top 100 = disqualified. 3 submissions max; last valid counts.
- CSV: ranks 1–100 unique, scores non-increasing; tied scores MUST be ordered by
  candidate_id ascending (validator enforces this).

## Agreed decisions (with user, 2026-06)

1. Rules-first interpretable scorer; embeddings only if the local eval proves a gain
   (experiments/embeddings_ab.py), documented either way.
2. Sandbox: HuggingFace Spaces (Gradio) + Dockerfile here for Stage 3.
3. Solo developer, iterative git history (Stage 4 checks history authenticity).
4. Core ranker stays stdlib-only.

## Data gotchas (measured on the real pool — do not re-derive)

- The `skills` array is RANDOM NOISE: every skill name appears ~12.1K times uniformly.
  Use only for honeypot detection (expert proficiency + low duration_months), never
  for relevance. Career descriptions/titles/summaries carry the real signal and are
  drawn from a finite template pool.
- Honeypots: exactly 60 candidates trip the three valid checks (expert-skill-no-duration,
  YoE overclaim, YoE underclaim) — see src/filters.py. Date-based checks
  (active-before-signup: 7,496 hits; job-before-edu: 3,457 hits) are generator
  artifacts, NOT honeypots — do not reinstate them.
- `github_activity_score` and `offer_acceptance_rate` use -1 = "missing", not "bad".
- Pool: 75% India; ~726 ML/AI-titled candidates are the real competition; gold pockets:
  Recommendation Systems Engineer ×26, Search Engineer ×23, ML Engineer ×167.

## Status

- Phase 1 done (commit bf3810f): loader + filters; funnel = 60 honeypots / 80,915
  gated / 19,025 shortlisted in ~58s.
- Phase 2 done: scoring.py (6 fit components + JD-severity disqualifier multipliers)
  + behavioral.py (availability multiplier [0.5,1.0], fixed REFERENCE_DATE 2026-06-01).
  Full run 91s; top 10 = India-based RecSys/Search/ML engineers at product companies,
  zero disqualifier hits. submission.csv has empty reasoning until Phase 5.
- Next: Phase 3 eval framework (rubric, labeled set, gold pool, invariants, runs.md
  regression log) → embeddings A/B → reasoning → packaging.
  Full plan: C:\Users\divya\.claude\plans\read-the-readme-docx-inside-wise-crescent.md
