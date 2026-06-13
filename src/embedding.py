"""Optional embedding relevance feature (Phase 4, adopted).

A sentence-embedding cosine between each candidate's career text and a
focused JD query, blended into the rules score at a small fixed weight.
The A/B test (experiments/embeddings_ab.py) measured this blend lifting the
local composite 0.8429 -> 0.8911 (+0.048), concentrated in NDCG@10/@50.

Design constraints honored:
  * CPU-only, no network at ranking time. The model is loaded from a
    repo-local cache (./models/), populated at build time (see Dockerfile /
    scripts/fetch_model.py). HF hub calls are disabled at runtime.
  * 5-min budget: we only embed the rules top-K candidates (EMBED_TOPK).
    The blend adds at most EMBED_WEIGHT, so a candidate can only be lifted
    into the top-100 if it is already within the rules top-K — embedding
    the rest is wasted work.
  * Graceful degradation: if fastembed or the cached model is unavailable,
    is_available() returns False and callers rank rules-only, so the repo
    always runs even with a stdlib-only install.

The cosine -> feature transform is a FIXED, set-independent map (no
normalization over the scored set), so the score is identical in eval and
on the full pool — the measured A/B gain carries over without leakage.
"""

import os
from pathlib import Path

# --- shared constants (also referenced by the A/B experiment) ---------------

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
MODEL_CACHE = Path(__file__).parent.parent / "models"

# Distilled from job_description.docx — the must-haves only, kept short so it
# fits MiniLM's context and isn't diluted by the JD's long narrative.
JD_QUERY = (
    "Senior AI engineer owning production ranking, retrieval and recommendation "
    "systems that decide what recruiters and candidates see. Deep ML systems "
    "depth: embeddings, hybrid retrieval, learning-to-rank, LLM-based re-ranking, "
    "fine-tuning, semantic and vector search, BM25, evaluation with NDCG and "
    "offline/online A/B tests. Scrappy product engineering: ship a working ranker "
    "fast at a product company. 5 to 9 years experience, India based."
)

EMBED_WEIGHT = 0.10          # blend weight chosen by the A/B test
EMBED_TOPK = 3000            # only embed the rules top-K (budget guard)
EMBED_COS_FLOOR = 0.45       # cosine->feature transform, from JD-cosine geometry
EMBED_COS_SPAN = 0.32

_model = None
_jd_vec = None


def is_available():
    """True if fastembed imports and the model is present in the local cache."""
    try:
        import fastembed  # noqa: F401
        import numpy  # noqa: F401
    except ImportError:
        return False
    # A populated cache means we can run with HF offline. If empty, we only
    # proceed when a network fetch is explicitly allowed (dev/build time).
    if _cache_populated():
        return True
    return os.environ.get("REDROB_ALLOW_MODEL_FETCH") == "1"


def _cache_populated():
    return MODEL_CACHE.exists() and any(MODEL_CACHE.rglob("*.onnx"))


def _get_model():
    global _model, _jd_vec
    if _model is not None:
        return _model
    import numpy as np
    from fastembed import TextEmbedding

    # Force offline once the cache is populated so the ranking step makes no
    # network calls (the Stage-3 hard constraint).
    if _cache_populated():
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
        os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    MODEL_CACHE.mkdir(exist_ok=True)
    _model = TextEmbedding(MODEL_NAME, cache_dir=str(MODEL_CACHE))
    v = np.asarray(list(_model.embed([JD_QUERY]))[0], dtype="float32")
    _jd_vec = v / (np.linalg.norm(v) + 1e-9)
    return _model


def _cos_to_feature(cos):
    f = (cos - EMBED_COS_FLOOR) / EMBED_COS_SPAN
    return 0.0 if f < 0 else 1.0 if f > 1 else float(f)


def embed_features(texts, batch_size=256):
    """Return a list of embed features in [0,1], one per input text.

    Cosine of each text's MiniLM embedding to the JD query, passed through
    the fixed transform. Raises if the model is unavailable — callers should
    guard with is_available() first.
    """
    import numpy as np
    model = _get_model()
    vecs = np.asarray(list(model.embed(list(texts), batch_size=batch_size)), dtype="float32")
    if vecs.ndim == 1:  # single text edge case
        vecs = vecs[None, :]
    vecs /= (np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9)
    cosims = vecs @ _jd_vec
    return [_cos_to_feature(c) for c in cosims]


def blend(rules_score, embed_feature):
    """Blend a rules score with an embed feature at the A/B-chosen weight."""
    return (1.0 - EMBED_WEIGHT) * rules_score + EMBED_WEIGHT * embed_feature
