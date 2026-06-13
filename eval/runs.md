# Evaluation runs (local labeled set)

| when | commit | composite | NDCG@10 | NDCG@50 | MAP | P@10 | note |
|---|---|---|---|---|---|---|---|
| 2026-06-12 23:52 | 93a51b4 | 0.7107 | 0.5921 | 0.8184 | 0.8274 | 0.9 | baseline: Phase 2 scorer, first eval on completed 200-label set |
| 2026-06-13 08:12 | bd804fd | 0.8429 | 0.8035 | 0.8855 | 0.8364 | 1.0 | regrade core_relevance to IR-depth (graded over distinct core-IR capabilities), reweight core 0.55->0.62 / product 0.12->0.06 |
