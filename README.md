# Redrob Ranker

Candidate ranking system for the Redrob Intelligent Candidate Discovery & Ranking Challenge.

Ranks the 100,000-candidate pool against the "Senior AI Engineer — Founding Team" JD and
produces the top-100 submission CSV.

## Reproduce

```bash
python rank.py --candidates ./candidates.jsonl --out ./submission.csv
```

Accepts both `candidates.jsonl` and `candidates.jsonl.gz`.

Runs CPU-only, single pass, no network, no external dependencies (stdlib only).

## Layout

- `rank.py` — entry point, end-to-end pipeline
- `src/loader.py` — streaming JSONL reader
- `src/filters.py` — honeypot consistency checks + relevance gate
- `src/scoring.py` — JD-fit component scorers
- `src/behavioral.py` — availability multiplier from redrob_signals
- `src/reasoning.py` — evidence-based reasoning text per ranked candidate
- `eval/` — local evaluation harness (hand-labeled sample + metrics)
