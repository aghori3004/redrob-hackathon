"""Populate the repo-local embedding model cache (./models/).

Run once at build/setup time WITH network access. After this, the ranking
step (rank.py) loads the model from ./models/ with HF hub offline, making
no network calls — the Stage-3 constraint.

    python scripts/fetch_model.py
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

os.environ["REDROB_ALLOW_MODEL_FETCH"] = "1"

from src.embedding import MODEL_CACHE, _get_model, embed_features

if __name__ == "__main__":
    print(f"fetching {os.path.basename(str(MODEL_CACHE))} model into {MODEL_CACHE} ...")
    _get_model()
    feats = embed_features(["production learning-to-rank and retrieval systems"])
    print(f"OK — model cached, smoke-test feature = {feats[0]:.3f}")
