# Redrob Ranker

Candidate ranking system for the **Redrob Intelligent Candidate Discovery & Ranking
Challenge**. Ranks the 100,000-candidate pool against the *Senior AI Engineer —
Founding Team* job description and produces the top-100 submission CSV
(`candidate_id, rank, score, reasoning`).

An interpretable **rules-first** scorer, refined by a small, A/B-validated
**embedding blend**. Runs CPU-only, offline, in ~140 s on the full pool.

## Reproduce

```bash
# 1. install (numpy + fastembed; see Fallback note below)
pip install -r requirements.txt

# 2. fetch the embedding model once (build-time network; ranking stays offline)
python scripts/fetch_model.py

# 3. rank
python rank.py --candidates ./candidates.jsonl --out ./submission.csv
```

Accepts `candidates.jsonl` or `candidates.jsonl.gz`. The ranking step makes **no
network calls** (the model loads from the local `./models/` cache with the
HuggingFace hub forced offline).

### Reproduce in Docker (canonical, fully offline ranking)

```bash
docker build -t redrob-ranker .                      # downloads the model at build
docker run --rm --network none \
    -v "$PWD/data:/data" -v "$PWD/out:/out" redrob-ranker \
    python rank.py --candidates /data/candidates.jsonl --out /out/submission.csv
```

### Fallback

The core ranker (loader, filters, scoring, behavioral, reasoning) is **pure
stdlib**. If `numpy`/`fastembed` or the model are absent, `rank.py`
automatically ranks rules-only and still produces a valid submission — so the
repo always runs. The embedding blend (worth ~+0.05 local composite) is the
only thing lost.

## Approach

Single streaming pass over the pool:

1. **Honeypot filter** (`src/filters.py`) — drops profiles with internally
   impossible facts (expert skills claimed with near-zero duration, stated vs
   summed experience mismatch, impossible job dates). Exactly 60 in the pool.
2. **Relevance gate** — recall-oriented; removes only candidates with no
   plausible ML/IR connection. Precision is the scorer's job.
3. **JD-fit scoring** (`src/scoring.py`) — six additive components:
   - **core relevance** (0.62) — graded by *depth* across the core-IR
     capabilities {learning-to-rank, ranking, recommendation, retrieval,
     ranking-eval, vector-search}; this is what separates a tier-5 from a
     tier-3. Leans on career-text evidence over title.
   - product-company fraction, experience fit (5–9y), location/notice
     logistics, education, external validation.
   - **× JD-severity disqualifier multipliers** (consulting-only, research-only,
     LLM-wrapper, CV/speech-only, non-coding senior, geo-ineligible,
     title-chaser) and a **behavioral availability multiplier**.
4. **Embedding blend** (`src/embedding.py`) — a local MiniLM JD-cosine feature
   blended at weight 0.10, applied to the rules top-3000 only (budget guard).
5. **Reasoning** (`src/reasoning.py`) — 1–2 sentences per candidate composed
   *only* from fields the scorer read, so it cannot hallucinate.

The `skills` array is uniform random noise in this dataset and is used **only**
for honeypot detection, never for relevance.

### Why embeddings (documented experiment)

We hypothesized embeddings would be redundant (career text is drawn from a
finite template pool). The A/B test (`experiments/embeddings_ab.py`,
result in `experiments/embeddings_ab_result.md`) disproved this: the JD-cosine
is monotonic in label tier and a 0.10 blend lifts the local composite
**0.8429 → 0.8911**, concentrated in NDCG@10 (0.8035 → 0.8737) — so it was
adopted. See `eval/runs.md` for the full regression log.

## Evaluation

- `eval/rubric.md` — JD-derived tier 0–5 labeling rubric (written before any
  scorer output, to keep labels independent).
- `eval/labels.jsonl` — 200 hand-labeled candidates across strata.
- `eval/evaluate.py` — contest-exact metrics (0.50·NDCG@10 + 0.30·NDCG@50 +
  0.15·MAP + 0.05·P@10) over the labeled set; `--log` appends to `eval/runs.md`.
- `eval/invariants.py` — label-free checks on the actual submission (zero
  honeypots / stuffers / geo-ineligible in top-100; perturbation tests).
- `eval/diagnose.py` — per-component inspection of labeled candidates.

```bash
python eval/evaluate.py
python eval/invariants.py --candidates ./candidates.jsonl --submission ./submission.csv
```

## Sandbox

`app.py` is a Gradio app (HuggingFace Spaces) that runs the full pipeline on a
small sample — upload a `candidates.jsonl` or run the bundled sample.

```bash
pip install -r requirements-app.txt
python scripts/fetch_model.py
python app.py
```

## Layout

```
rank.py                 entry point — end-to-end pipeline
src/loader.py           streaming JSONL reader
src/filters.py          honeypot consistency checks + relevance gate
src/scoring.py          JD-fit component scorers + disqualifier multipliers
src/behavioral.py       availability multiplier from redrob_signals
src/embedding.py        optional MiniLM JD-cosine blend (Phase 4)
src/reasoning.py        evidence-based reasoning text per candidate
scripts/fetch_model.py  one-time embedding-model fetch into ./models/
experiments/            the embedding A/B test + its written result
eval/                   rubric, labels, metrics, invariants, regression log
app.py                  Gradio sandbox
Dockerfile              reproducible offline build
```
