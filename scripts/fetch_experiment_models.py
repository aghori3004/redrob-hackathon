"""Populate ./models/ with the extra models the methodology benchmark needs.

Run once at setup time WITH network access. After this, experiments/
methodologies_ab.py (and any future adoption) loads these from ./models/ with
HF hub offline — no network at ranking time.

Fetches:
  * BAAI/bge-small-en-v1.5, BAAI/bge-base-en-v1.5   (embedding upgrades)
  * Xenova/ms-marco-MiniLM-L-6-v2                    (cross-encoder reranker)

The MiniLM bi-encoder is fetched separately by scripts/fetch_model.py.

    python scripts/fetch_experiment_models.py
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

os.environ["REDROB_ALLOW_MODEL_FETCH"] = "1"

from src.embedding import MODEL_CACHE

EMBED_MODELS = ["BAAI/bge-small-en-v1.5", "BAAI/bge-base-en-v1.5"]
CROSS_ENCODER = "Xenova/ms-marco-MiniLM-L-6-v2"


def main():
    MODEL_CACHE.mkdir(exist_ok=True)
    from fastembed import TextEmbedding

    for name in EMBED_MODELS:
        print(f"fetching embedding model {name} ...")
        m = TextEmbedding(name, cache_dir=str(MODEL_CACHE))
        vec = next(iter(m.embed(["production learning-to-rank and retrieval"])))
        print(f"  OK — dim {len(vec)}")

    print(f"fetching cross-encoder {CROSS_ENCODER} ...")
    from fastembed.rerank.cross_encoder import TextCrossEncoder

    ce = TextCrossEncoder(CROSS_ENCODER, cache_dir=str(MODEL_CACHE))
    s = list(ce.rerank("senior AI ranking engineer", ["built a learning-to-rank system", "sold insurance"]))
    print(f"  OK — sample scores {[round(x, 3) for x in s]}")
    print(f"\nall models cached under {MODEL_CACHE}")


if __name__ == "__main__":
    main()
