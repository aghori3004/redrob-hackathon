"""Okapi BM25 — sparse lexical relevance of career text vs the JD query.

The dataset's profiles repeatedly cite "BM25 + dense retrieval". Our shipped
ranker has no lexical/TF-IDF term-weighting signal at all (the rules scorer
uses binary phrase presence; the embedding blend is purely dense). This is a
stdlib implementation (no new dependency) so the benchmark can measure whether
a real term-frequency/IDF signal adds anything over phrase presence + dense.

IDF is fit over the candidate corpus passed in (the labeled set in the eval
harness; in production it would be the gate-passing top-K). The score is a raw
BM25 sum; callers normalize it to [0,1] for blending.
"""

import math
import re

_TOKEN_RE = re.compile(r"[a-z0-9]+")
# A short stoplist — BM25 IDF already down-weights ubiquitous terms, but
# dropping these trims noise from the heavily templated descriptions.
_STOP = {
    "the", "a", "an", "and", "or", "of", "to", "in", "for", "on", "with", "at",
    "by", "from", "as", "is", "was", "were", "are", "be", "been", "that", "this",
    "it", "i", "my", "our", "we", "they", "their", "over", "into", "across",
    "using", "used", "both", "while", "than", "but", "some", "most", "more",
}

K1 = 1.5
B = 0.75


def tokenize(text):
    return [t for t in _TOKEN_RE.findall((text or "").lower()) if t not in _STOP and len(t) > 1]


class BM25:
    """Fit IDF + doc lengths over a corpus; score any query against each doc."""

    def __init__(self, docs_tokens):
        self.docs = docs_tokens
        self.N = len(docs_tokens)
        self.doc_len = [len(d) for d in docs_tokens]
        self.avgdl = (sum(self.doc_len) / self.N) if self.N else 0.0
        df = {}
        for d in docs_tokens:
            for term in set(d):
                df[term] = df.get(term, 0) + 1
        # Okapi IDF with the +1 inside the log to keep it non-negative.
        self.idf = {
            t: math.log(1 + (self.N - n + 0.5) / (n + 0.5)) for t, n in df.items()
        }
        self._tf = [self._term_freqs(d) for d in docs_tokens]

    @staticmethod
    def _term_freqs(tokens):
        tf = {}
        for t in tokens:
            tf[t] = tf.get(t, 0) + 1
        return tf

    def score(self, query_tokens, doc_idx):
        tf = self._tf[doc_idx]
        dl = self.doc_len[doc_idx]
        denom_norm = K1 * (1 - B + B * dl / (self.avgdl or 1.0))
        s = 0.0
        for t in query_tokens:
            f = tf.get(t)
            if not f:
                continue
            s += self.idf.get(t, 0.0) * (f * (K1 + 1)) / (f + denom_norm)
        return s

    def scores(self, query_tokens):
        return [self.score(query_tokens, i) for i in range(self.N)]
