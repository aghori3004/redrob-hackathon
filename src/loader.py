"""Streaming candidate loader.

Yields one parsed candidate dict at a time so the full 100K pool
(~465 MB raw) never has to be resident in memory at once.
"""

import gzip
import json


def iter_candidates(path):
    """Yield candidate dicts from a .jsonl or .jsonl.gz file."""
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)
