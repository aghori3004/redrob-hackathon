# Embedding A/B result (Phase 4)

Model: all-MiniLM-L6-v2 (fastembed/ONNX, CPU). Labeled set: 200 candidates.

JD query: Senior AI engineer owning production ranking, retrieval and recommendation systems that decide what recruiters and candidates see. Deep ML systems depth: embeddings, hybrid retrieval, learning-to-rank, LLM-based re-ranking, fine-tuning, semantic and vector search, BM25, evaluation with NDCG and offline/online A/B tests. Scrappy product engineering: ship a working ranker fast at a product company. 5 to 9 years experience, India based.

| variant | composite | NDCG@10 | NDCG@50 | MAP | P@10 | vs rules |
|---|---|---|---|---|---|---|
| rules_only | 0.8429 | 0.8035 | 0.8855 | 0.8364 | 1.000 | +0.0000 |
| embed_only | 0.7667 | 0.7480 | 0.8410 | 0.6696 | 0.800 | -0.0762 |
| blend_a0.10 | 0.8911 | 0.8737 | 0.9335 | 0.8277 | 1.000 | +0.0482 |
| blend_a0.20 | 0.8905 | 0.8737 | 0.9329 | 0.8249 | 1.000 | +0.0476 |
| blend_a0.30 | 0.8881 | 0.8737 | 0.9320 | 0.8108 | 1.000 | +0.0452 |
| blend_a0.40 | 0.8839 | 0.8737 | 0.9194 | 0.8079 | 1.000 | +0.0410 |
| blend_a0.50 | 0.8785 | 0.8705 | 0.9158 | 0.7905 | 1.000 | +0.0357 |
| rerank_a0.10 | 0.8419 | 0.8035 | 0.8851 | 0.8309 | 1.000 | -0.0010 |
| rerank_a0.20 | 0.8836 | 0.8626 | 0.9259 | 0.8297 | 1.000 | +0.0407 |

Best variant: **blend_a0.10** (composite 0.8911, +0.0482 vs rules-only 0.8429).

**Verdict: embeddings help on the labeled set.** Consider adding the embedding cosine as a feature — but weigh the operational cost: shipping it means bundling model weights and an ONNX/torch runtime into the no-network ranking step, breaking the stdlib-only core. Re-run on the full pool and confirm the 5-min/16-GB budget before adopting.
