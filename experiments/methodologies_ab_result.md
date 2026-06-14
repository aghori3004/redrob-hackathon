# Methodology A/B result (all-against-all)

Labeled set: 200 candidates (103 gate-passing). Bootstrap B=1000. Metric: contest composite (0.50 NDCG@10 + 0.30 NDCG@50 + 0.15 MAP + 0.05 P@10), relevant = tier>=3.

Anchors: `current`=0.8911 (expect ~0.8911), `rules_only`=0.8429 (expect ~0.8429).

## Leaderboard

| variant | composite | 95% CI | NDCG@10 | NDCG@50 | MAP | P@10 | vs current |
|---|---|---|---|---|---|---|---|
| stack_rules_bgeMQ_then_ce | 0.9090 | [0.7153, 0.9852] | 0.8959 | 0.9510 | 0.8386 | 1.000 | +0.0180 |
| rules+bge_base_0.10 | 0.9086 | [0.7168, 0.9851] | 0.8959 | 0.9503 | 0.8371 | 1.000 | +0.0175 |
| rules+minilm_mq_max_0.10 | 0.9056 | [0.7081, 0.9828] | 0.8947 | 0.9480 | 0.8260 | 1.000 | +0.0146 |
| rules+bge_small_mq_max_0.10 | 0.8944 | [0.7094, 0.9830] | 0.8749 | 0.9360 | 0.8410 | 1.000 | +0.0033 |
| rules+bge_small_0.10 | 0.8937 | [0.7110, 0.9816] | 0.8749 | 0.9357 | 0.8367 | 1.000 | +0.0026 |
| rules+bge_small_mq_mean_0.10 | 0.8935 | [0.7105, 0.9816] | 0.8749 | 0.9352 | 0.8365 | 1.000 | +0.0024 |
| rules+ce_0.10 | 0.8927 | [0.7140, 0.9794] | 0.8749 | 0.9358 | 0.8298 | 1.000 | +0.0016 |
| rules+ce_0.20 | 0.8921 | [0.7127, 0.9790] | 0.8749 | 0.9359 | 0.8258 | 1.000 | +0.0010 |
| current | 0.8911 | [0.7026, 0.9799] | 0.8737 | 0.9335 | 0.8277 | 1.000 | +0.0000 |
| rules+ce_0.30 | 0.8899 | [0.7085, 0.9772] | 0.8749 | 0.9329 | 0.8170 | 1.000 | -0.0012 |
| rules+bm25_0.10 | 0.8851 | [0.7097, 0.9795] | 0.8638 | 0.9285 | 0.8313 | 1.000 | -0.0060 |
| rules+minilm_mq_mean_0.10 | 0.8850 | [0.7111, 0.9794] | 0.8638 | 0.9281 | 0.8308 | 1.000 | -0.0061 |
| rules+bm25_0.20 | 0.8795 | [0.7022, 0.9770] | 0.8568 | 0.9242 | 0.8257 | 1.000 | -0.0116 |
| rrf_rules_dense | 0.8743 | [0.6772, 0.9680] | 0.8784 | 0.9097 | 0.7815 | 0.900 | -0.0167 |
| bm25_only | 0.8670 | [0.7590, 0.9399] | 0.8908 | 0.8933 | 0.7239 | 0.900 | -0.0241 |
| rules+bm25_0.30 | 0.8663 | [0.7000, 0.9706] | 0.8440 | 0.9250 | 0.8121 | 0.900 | -0.0247 |
| rrf_rules_bm25_dense | 0.8584 | [0.6751, 0.9642] | 0.8522 | 0.9016 | 0.7786 | 0.900 | -0.0327 |
| rules_then_ce | 0.8511 | [0.7090, 0.9787] | 0.8158 | 0.8940 | 0.8331 | 1.000 | -0.0400 |
| rules_only | 0.8429 | [0.7052, 0.9727] | 0.8035 | 0.8855 | 0.8364 | 1.000 | -0.0482 |
| rrf_rules_ce | 0.8329 | [0.6909, 0.9619] | 0.8047 | 0.8738 | 0.7896 | 1.000 | -0.0582 |
| ce_only | 0.7740 | [0.6401, 0.8832] | 0.8338 | 0.7596 | 0.5615 | 0.900 | -0.1171 |
| ltr_lambdamart | 0.7477 | [0.6160, 0.8962] | 0.7157 | 0.8098 | 0.7126 | 0.800 | -0.1434 |
| ltr_logreg | 0.7396 | [0.5763, 0.9153] | 0.6640 | 0.8277 | 0.7620 | 0.900 | -0.1515 |

## Pairwise P[row beats column] (bootstrap)

| | stack_rules_bgeMQ_then_ce | rules+bge_base_0.10 | rules+minilm_mq_max_0.10 | rules+bge_small_mq_max_0.10 | rules+bge_small_0.10 | rules+bge_small_mq_mean_0.10 | rules+ce_0.10 | rules+ce_0.20 | current | rules+ce_0.30 | rules+bm25_0.10 | rules+minilm_mq_mean_0.10 | rules+bm25_0.20 | rrf_rules_dense | bm25_only | rules+bm25_0.30 | rrf_rules_bm25_dense | rules_then_ce | rules_only | rrf_rules_ce | ce_only | ltr_lambdamart | ltr_logreg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| stack_rules_bgeMQ_then_ce | — | 0.58 | 0.86 | 0.62 | 0.72 | 0.76 | 0.87 | 0.91 | 0.92 | 0.96 | 0.89 | 0.86 | 0.94 | 0.99 | 0.75 | 0.97 | 1.00 | 0.86 | 0.91 | 0.99 | 0.99 | 1.00 | 1.00 |
| rules+bge_base_0.10 | 0.42 | — | 0.87 | 0.60 | 0.68 | 0.71 | 0.87 | 0.86 | 0.91 | 0.95 | 0.87 | 0.85 | 0.92 | 0.99 | 0.75 | 0.97 | 0.99 | 0.88 | 0.90 | 0.99 | 0.99 | 1.00 | 1.00 |
| rules+minilm_mq_max_0.10 | 0.14 | 0.13 | — | 0.47 | 0.43 | 0.45 | 0.48 | 0.56 | 0.62 | 0.69 | 0.62 | 0.56 | 0.73 | 0.98 | 0.73 | 0.88 | 0.96 | 0.59 | 0.72 | 0.95 | 0.98 | 1.00 | 0.99 |
| rules+bge_small_mq_max_0.10 | 0.37 | 0.40 | 0.53 | — | 0.57 | 0.60 | 0.61 | 0.63 | 0.88 | 0.68 | 0.74 | 0.69 | 0.76 | 0.80 | 0.65 | 0.79 | 0.83 | 0.73 | 0.89 | 0.89 | 0.95 | 1.00 | 1.00 |
| rules+bge_small_0.10 | 0.27 | 0.30 | 0.57 | 0.42 | — | 0.64 | 0.73 | 0.72 | 0.76 | 0.73 | 0.71 | 0.71 | 0.76 | 0.79 | 0.67 | 0.79 | 0.81 | 0.93 | 0.92 | 0.99 | 0.95 | 1.00 | 1.00 |
| rules+bge_small_mq_mean_0.10 | 0.23 | 0.29 | 0.55 | 0.40 | 0.34 | — | 0.66 | 0.68 | 0.73 | 0.72 | 0.68 | 0.68 | 0.74 | 0.79 | 0.66 | 0.79 | 0.81 | 0.85 | 0.90 | 0.99 | 0.95 | 1.00 | 1.00 |
| rules+ce_0.10 | 0.12 | 0.13 | 0.52 | 0.39 | 0.27 | 0.34 | — | 0.72 | 0.64 | 0.86 | 0.64 | 0.67 | 0.83 | 0.79 | 0.72 | 0.93 | 0.94 | 0.61 | 0.77 | 0.98 | 0.99 | 1.00 | 0.99 |
| rules+ce_0.20 | 0.09 | 0.14 | 0.44 | 0.37 | 0.28 | 0.32 | 0.28 | — | 0.56 | 0.81 | 0.59 | 0.60 | 0.76 | 0.78 | 0.70 | 0.91 | 0.94 | 0.56 | 0.73 | 0.98 | 0.98 | 1.00 | 0.99 |
| current | 0.09 | 0.09 | 0.37 | 0.12 | 0.24 | 0.27 | 0.36 | 0.44 | — | 0.52 | 0.50 | 0.44 | 0.61 | 0.76 | 0.63 | 0.72 | 0.79 | 0.51 | 0.59 | 0.83 | 0.93 | 1.00 | 0.99 |
| rules+ce_0.30 | 0.04 | 0.05 | 0.31 | 0.32 | 0.27 | 0.28 | 0.14 | 0.19 | 0.48 | — | 0.47 | 0.50 | 0.66 | 0.77 | 0.69 | 0.86 | 0.93 | 0.50 | 0.68 | 0.98 | 0.98 | 1.00 | 0.99 |
| rules+bm25_0.10 | 0.11 | 0.13 | 0.38 | 0.26 | 0.29 | 0.31 | 0.36 | 0.41 | 0.50 | 0.53 | — | 0.57 | 0.83 | 0.68 | 0.67 | 0.92 | 0.92 | 0.56 | 0.68 | 0.97 | 0.98 | 1.00 | 0.95 |
| rules+minilm_mq_mean_0.10 | 0.14 | 0.15 | 0.44 | 0.30 | 0.29 | 0.32 | 0.33 | 0.40 | 0.55 | 0.50 | 0.43 | — | 0.76 | 0.68 | 0.67 | 0.89 | 0.92 | 0.56 | 0.67 | 0.97 | 0.98 | 1.00 | 0.96 |
| rules+bm25_0.20 | 0.06 | 0.08 | 0.27 | 0.24 | 0.24 | 0.26 | 0.17 | 0.24 | 0.39 | 0.34 | 0.17 | 0.24 | — | 0.60 | 0.62 | 0.87 | 0.87 | 0.47 | 0.59 | 0.84 | 0.98 | 1.00 | 0.92 |
| rrf_rules_dense | 0.01 | 0.01 | 0.02 | 0.20 | 0.21 | 0.21 | 0.21 | 0.22 | 0.24 | 0.23 | 0.32 | 0.32 | 0.40 | — | 0.57 | 0.48 | 0.58 | 0.51 | 0.59 | 0.68 | 0.95 | 0.98 | 0.94 |
| bm25_only | 0.25 | 0.25 | 0.27 | 0.35 | 0.33 | 0.34 | 0.28 | 0.29 | 0.37 | 0.31 | 0.33 | 0.33 | 0.38 | 0.43 | — | 0.45 | 0.48 | 0.48 | 0.55 | 0.61 | 1.00 | 0.91 | 0.82 |
| rules+bm25_0.30 | 0.03 | 0.03 | 0.12 | 0.21 | 0.21 | 0.21 | 0.07 | 0.09 | 0.28 | 0.14 | 0.09 | 0.11 | 0.13 | 0.52 | 0.55 | — | 0.69 | 0.43 | 0.52 | 0.69 | 0.97 | 1.00 | 0.88 |
| rrf_rules_bm25_dense | 0.00 | 0.01 | 0.04 | 0.17 | 0.19 | 0.19 | 0.06 | 0.06 | 0.21 | 0.07 | 0.08 | 0.08 | 0.13 | 0.41 | 0.52 | 0.30 | — | 0.41 | 0.50 | 0.53 | 0.96 | 0.98 | 0.86 |
| rules_then_ce | 0.14 | 0.12 | 0.41 | 0.27 | 0.05 | 0.14 | 0.39 | 0.43 | 0.49 | 0.50 | 0.43 | 0.44 | 0.53 | 0.49 | 0.52 | 0.57 | 0.59 | — | 0.70 | 0.97 | 0.94 | 1.00 | 1.00 |
| rules_only | 0.09 | 0.10 | 0.28 | 0.12 | 0.08 | 0.10 | 0.23 | 0.27 | 0.41 | 0.32 | 0.32 | 0.33 | 0.41 | 0.41 | 0.45 | 0.48 | 0.50 | 0.24 | — | 0.76 | 0.89 | 1.00 | 1.00 |
| rrf_rules_ce | 0.01 | 0.01 | 0.05 | 0.11 | 0.01 | 0.01 | 0.02 | 0.01 | 0.17 | 0.02 | 0.03 | 0.03 | 0.16 | 0.32 | 0.39 | 0.31 | 0.47 | 0.03 | 0.24 | — | 0.91 | 1.00 | 0.90 |
| ce_only | 0.01 | 0.01 | 0.02 | 0.05 | 0.05 | 0.05 | 0.01 | 0.02 | 0.07 | 0.02 | 0.02 | 0.02 | 0.02 | 0.04 | 0.00 | 0.03 | 0.04 | 0.06 | 0.11 | 0.10 | — | 0.56 | 0.58 |
| ltr_lambdamart | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.02 | 0.09 | 0.00 | 0.02 | 0.00 | 0.00 | 0.00 | 0.44 | — | 0.59 |
| ltr_logreg | 0.00 | 0.00 | 0.01 | 0.00 | 0.00 | 0.00 | 0.01 | 0.01 | 0.01 | 0.01 | 0.05 | 0.04 | 0.08 | 0.06 | 0.18 | 0.12 | 0.14 | 0.00 | 0.00 | 0.10 | 0.42 | 0.41 | — |

## Signal timings (on the labeled active set) + full-pool projection

Heavy signals (dense / cross-encoder) run only on the rules top-K=3000 in production, so projected full-pool cost = per-item ms x 3000.

| signal | active wall (s) | per-item (ms) | projected top-3000 (s) |
|---|---|---|---|
| bm25_active | 0.02 | - | 0.0 |
| embed_minilm | 1.67 | 16.18 | 48.5 |
| embed_bge_small | 20.08 | 194.97 | 584.9 |
| embed_bge_base | 55.89 | 542.63 | 1627.9 |
| cross_encoder | 10.60 | 102.93 | 308.8 |

## Runtime feasibility of variants beating `current`

Projected full-pool cost = ~80 s (gate+rules) + heaviest signal over the rules top-3000 (warm per-item x 3000). Budget = 300 s, CPU, no network.

| variant | composite | proj. full-pool (s) | within budget |
|---|---|---|---|
| stack_rules_bgeMQ_then_ce | 0.9090 | 389 | NO |
| rules+bge_base_0.10 | 0.9086 | 1708 | NO |
| rules+minilm_mq_max_0.10 | 0.9056 | 129 | YES |
| rules+bge_small_mq_max_0.10 | 0.8944 | 665 | NO |
| rules+bge_small_0.10 | 0.8937 | 665 | NO |
| rules+bge_small_mq_mean_0.10 | 0.8935 | 665 | NO |
| rules+ce_0.10 | 0.8927 | 389 | NO |
| rules+ce_0.20 | 0.8921 | 389 | NO |

## Verdict

Best composite overall: **stack_rules_bgeMQ_then_ce** (0.9090, +0.0180; P[beats current]=0.92) — projected full-pool 389s, OVER the 300s budget.

Best **budget-feasible** improvement: **rules+minilm_mq_max_0.10** (composite 0.9056, +0.0146; P[beats current]=0.62; projected 129s).

But P[beats current]=0.62 < 0.85: the gain is within bootstrap noise on this tiny label set (30 relevant / 9 top-tier) — the 95% CIs overlap heavily. It is promising and (if dependency-free) cheap to adopt, but **not statistically proven**. Best next move: expand the labeled set, then re-run, before committing.


The data's marquee methods underperform on this set: supervised LTR (`ltr_*`) ranks **last** (out-of-fold, but only 9 top-tier labels to learn from), and cross-encoder / BM25 as primary signals lose to the rules+dense blend — consistent with finite-template descriptions giving lexical/dense signals little to recover beyond rules phrase-presence.

_Caveat: local composite is a proxy for the hidden ground truth; treat all deltas as directional._

