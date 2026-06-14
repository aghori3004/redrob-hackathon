"""Zero-shot cross-encoder re-ranker (the data's "LLM re-ranker on the top-50").

A bi-encoder (our shipped MiniLM blend) embeds the JD and each candidate
independently, then takes a cosine. A *cross*-encoder instead feeds the
(JD, candidate) pair jointly through the transformer, so query and document
attend to each other — strictly more expressive, at the cost of one model call
per candidate (hence: only ever run on a rules top-K).

Stays inside the existing offline ONNX stack (fastembed, CPU) — no torch — and
loads from the repo-local ./models/ cache exactly like src/embedding.py, so an
adopted version would run network-free at ranking time.
"""

import os
from pathlib import Path

from src.embedding import MODEL_CACHE  # reuse the same ./models/ cache dir

MODEL_NAME = "Xenova/ms-marco-MiniLM-L-6-v2"

_model = None


def is_available():
    try:
        import fastembed  # noqa: F401
    except ImportError:
        return False
    if _cache_populated():
        return True
    return os.environ.get("REDROB_ALLOW_MODEL_FETCH") == "1"


def _cache_populated():
    # The cross-encoder caches under a model-name-derived dir; look for its onnx.
    return MODEL_CACHE.exists() and any(
        "ms-marco" in str(p).lower() for p in MODEL_CACHE.rglob("*.onnx")
    )


def _get_model():
    global _model
    if _model is not None:
        return _model
    from fastembed.rerank.cross_encoder import TextCrossEncoder

    if _cache_populated():
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
        os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    MODEL_CACHE.mkdir(exist_ok=True)
    _model = TextCrossEncoder(MODEL_NAME, cache_dir=str(MODEL_CACHE))
    return _model


def rerank_scores(query, texts, batch_size=64):
    """Return a raw cross-encoder relevance score per text (higher = better).

    Scores are unbounded logits; callers normalize before blending. Raises if
    the model is unavailable — guard with is_available() first.
    """
    model = _get_model()
    return list(model.rerank(query, list(texts), batch_size=batch_size))
