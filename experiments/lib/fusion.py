"""Rank-fusion + normalization helpers for the methodology benchmark.

Our shipped ranker combines signals with a *linear blend* of normalized
scores. The dataset's profiles instead describe multi-stage *retrieval fusion*.
This module provides:

  * minmax  — set-relative [0,1] normalization (for linear blends).
  * rrf     — Reciprocal Rank Fusion: combine signals by RANK, not score, so a
              signal's raw scale and outliers don't dominate (the standard
              hybrid sparse+dense fusion).

Both operate over dicts keyed by candidate_id. Filtered/honeypot candidates are
the caller's responsibility — pass them in with a sentinel low value, or omit
them and re-append at score -1.0 after fusion.
"""


def minmax(score_by_id):
    """Normalize a {id: score} map to [0,1] (set-relative)."""
    if not score_by_id:
        return {}
    vals = list(score_by_id.values())
    lo, hi = min(vals), max(vals)
    span = hi - lo
    if span <= 0:
        return {k: 0.0 for k in score_by_id}
    return {k: (v - lo) / span for k, v in score_by_id.items()}


def linear_blend(signals, weights):
    """Weighted sum of several {id: score} signals after minmax-normalizing each.

    signals/weights are parallel lists. Returns {id: blended_score}. Assumes all
    signals share the same key set.
    """
    norm = [minmax(s) for s in signals]
    ids = norm[0].keys()
    wsum = sum(weights) or 1.0
    return {
        cid: sum(w * n[cid] for w, n in zip(weights, norm)) / wsum
        for cid in ids
    }


def rrf(signals, k=60):
    """Reciprocal Rank Fusion over several {id: score} signals (higher better).

    Each signal is ranked independently (rank 1 = best); the fused score for a
    candidate is sum_i 1 / (k + rank_i). k=60 is the canonical default. Returns
    {id: fused_score}.
    """
    ids = signals[0].keys()
    fused = {cid: 0.0 for cid in ids}
    for s in signals:
        # rank 1 = highest score; ties broken by id for determinism.
        order = sorted(s.keys(), key=lambda c: (-s[c], c))
        for rank, cid in enumerate(order, start=1):
            fused[cid] += 1.0 / (k + rank)
    return fused
