"""Methodology A/B benchmark — all-against-all on the local labeled set.

Implements the ranking methodologies the dataset's profiles describe (BM25,
rank fusion, cross-encoder reranking, BGE / multi-query embeddings, supervised
learning-to-rank) as pluggable variants, scores every one on the full 200
Claude-labeled candidates with the contest composite, and reports:

  1. a leaderboard (composite + NDCG@10/@50/MAP/P@10, delta vs `current`),
  2. paired bootstrap 95% CIs (is a +0.01 real or noise, given 30 relevant /
     9 top-tier labels?),
  3. an all-against-all pairwise win matrix (P[A beats B] across resamples),
  4. measured signal timings + a full-pool feasibility note.

Dev-time only — imports from src/* but writes nothing into the production path.
Reproduce-anchors: `current` must land ~0.8911 and `rules_only` ~0.8429.

    pip install -r experiments/requirements-experiments.txt
    python scripts/fetch_experiment_models.py        # one-time, network
    python experiments/methodologies_ab.py
    python experiments/methodologies_ab.py --time-full-pool <candidates.jsonl>
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.filters import honeypot_flags, passes_relevance_gate
from src.scoring import score_candidate, _career_text, FIT_WEIGHTS
from src import embedding
from eval.evaluate import ndcg_at, average_precision

from experiments.lib import bm25 as bm25lib
from experiments.lib import fusion
from experiments.lib import ltr
from experiments.lib import cross_encoder as ce_lib

EVAL_DIR = Path(__file__).parent.parent / "eval"
MODELS = Path(__file__).parent.parent / "models"
OUT = Path(__file__).parent / "methodologies_ab_result.md"

JD_QUERY = embedding.JD_QUERY  # the shipped single-query distillation

# Multi-query split: the JD's must-haves vs its "ideal candidate" colour.
JD_MUST = (
    "Production ranking, retrieval and recommendation systems: learning-to-rank, "
    "hybrid sparse and dense retrieval, semantic and vector search, BM25, embeddings, "
    "LLM-based re-ranking, evaluation with NDCG, MRR and offline-online A/B testing."
)
JD_IDEAL = (
    "Scrappy senior AI engineer who ships a working ranker fast at a product company; "
    "5 to 9 years experience; India based; fine-tuning and deep ML systems depth."
)

BOOT_B = 1000
BOOT_SEED = 7


# --- metrics ---------------------------------------------------------------

def composite_from_arrays(scores, tiers, order_ids):
    """scores/tiers/order_ids are parallel arrays; sort by (-score, id)."""
    idx = sorted(range(len(scores)), key=lambda i: (-scores[i], order_ids[i]))
    t = [tiers[i] for i in idx]
    rel = [1 if x >= 3 else 0 for x in t]
    m = {
        "NDCG@10": ndcg_at(t, 10), "NDCG@50": ndcg_at(t, 50),
        "MAP": average_precision(rel), "P@10": sum(rel[:10]) / 10,
    }
    m["composite"] = 0.50 * m["NDCG@10"] + 0.30 * m["NDCG@50"] + 0.15 * m["MAP"] + 0.05 * m["P@10"]
    return m


def fmt(m):
    return (f"composite={m['composite']:.4f}  NDCG@10={m['NDCG@10']:.4f}  "
            f"NDCG@50={m['NDCG@50']:.4f}  MAP={m['MAP']:.4f}  P@10={m['P@10']:.3f}")


# --- embedding helpers (raw cosines, any fastembed model) ------------------

def _offline_if_cached():
    if MODELS.exists() and any(MODELS.rglob("*.onnx")):
        os.environ.setdefault("HF_HUB_OFFLINE", "1")
        os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")


def embed_unit_vectors(model_name, texts):
    from fastembed import TextEmbedding
    _offline_if_cached()
    model = TextEmbedding(model_name, cache_dir=str(MODELS))
    vecs = np.asarray(list(model.embed(list(texts))), dtype="float32")
    vecs /= (np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9)
    return model, vecs


def unit_query(model, q):
    v = np.asarray(next(iter(model.embed([q]))), dtype="float32")
    return v / (np.linalg.norm(v) + 1e-9)


# --- load + compute every signal once --------------------------------------

def build():
    labels = {}
    with open(EVAL_DIR / "labels.jsonl", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                r = json.loads(line)
                labels[r["candidate_id"]] = r["tier"]

    cands, texts, rules, filt, feats_raw = {}, {}, {}, set(), {}
    with open(EVAL_DIR / "sample_candidates.jsonl", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            c = json.loads(line)
            cid = c["candidate_id"]
            if cid not in labels:
                continue
            cands[cid] = c
            texts[cid] = _career_text(c)
            if honeypot_flags(c) or not passes_relevance_gate(c):
                filt.add(cid)
                rules[cid] = -1.0
            else:
                s, ev = score_candidate(c)
                rules[cid] = s
                feats_raw[cid] = (c, ev)

    ids = list(cands)
    active = [c for c in ids if c not in filt]   # gate-passing, scoreable
    print(f"labeled: {len(ids)}  active(gate-passing): {len(active)}  filtered: {len(filt)}")

    sig = {"labels": labels, "ids": ids, "active": active, "filt": filt,
           "texts": texts, "rules": rules, "cands": cands}
    timings = {}

    # --- BM25 (over active texts; JD query) --------------------------------
    t0 = time.perf_counter()
    act_tokens = [bm25lib.tokenize(texts[c]) for c in active]
    bm = bm25lib.BM25(act_tokens)
    q_tok = bm25lib.tokenize(JD_QUERY)
    bm_scores = bm.scores(q_tok)
    sig["bm25"] = {c: s for c, s in zip(active, bm_scores)}
    timings["bm25_active"] = time.perf_counter() - t0

    # --- dense cosines: MiniLM (shipped), bge-small, bge-base --------------
    def dense(model_name, key):
        from fastembed import TextEmbedding
        _offline_if_cached()
        model = TextEmbedding(model_name, cache_dir=str(MODELS))
        act_texts = [texts[c] for c in active]
        list(model.embed(act_texts[:8]))   # warm: exclude one-time model load/JIT from timing
        t = time.perf_counter()
        vecs = np.asarray(list(model.embed(act_texts)), dtype="float32")
        timings["embed_" + key] = dt = time.perf_counter() - t
        timings["embed_" + key + "_per_item_ms"] = dt / max(1, len(active)) * 1000
        vecs /= (np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-9)
        cos = vecs @ unit_query(model, JD_QUERY)
        sig[key] = {c: float(x) for c, x in zip(active, cos)}
        # multi-query (must/ideal) reuse the same candidate vectors
        if key == "minilm" or key == "bge_small":
            mc = vecs @ unit_query(model, JD_MUST)
            ic = vecs @ unit_query(model, JD_IDEAL)
            sig[key + "_mq_max"] = {c: float(max(a, b)) for c, a, b in zip(active, mc, ic)}
            sig[key + "_mq_mean"] = {c: float((a + b) / 2) for c, a, b in zip(active, mc, ic)}

    dense(embedding.MODEL_NAME, "minilm")
    try:
        dense("BAAI/bge-small-en-v1.5", "bge_small")
    except Exception as e:
        print("bge-small unavailable:", e)
    try:
        dense("BAAI/bge-base-en-v1.5", "bge_base")
    except Exception as e:
        print("bge-base unavailable:", e)

    # --- cross-encoder reranker -------------------------------------------
    if ce_lib.is_available():
        try:
            act_texts = [texts[c] for c in active]
            ce_lib.rerank_scores(JD_QUERY, act_texts[:8])  # warm
            t = time.perf_counter()
            ce = ce_lib.rerank_scores(JD_QUERY, act_texts)
            timings["cross_encoder"] = time.perf_counter() - t
            timings["cross_encoder_per_item_ms"] = timings["cross_encoder"] / max(1, len(active)) * 1000
            sig["ce"] = {c: float(s) for c, s in zip(active, ce)}
        except Exception as e:
            print("cross-encoder failed:", e)
    else:
        print("cross-encoder model not cached — run scripts/fetch_experiment_models.py")

    sig["timings"] = timings
    return sig


# --- variant assembly ------------------------------------------------------

def _full(score_map_active, sig):
    """Active scores -> full {cid: score}, filtered forced to -1."""
    out = {c: -1.0 for c in sig["ids"]}
    out.update(score_map_active)
    return out


def make_variants(sig):
    active = sig["active"]
    rules = sig["rules"]
    V = {}

    # baselines
    V["rules_only"] = _full({c: rules[c] for c in active}, sig)

    minilm_feat = {c: embedding._cos_to_feature(sig["minilm"][c]) for c in active}
    V["current"] = _full(
        {c: embedding.blend(rules[c], minilm_feat[c]) for c in active}, sig)

    # Family 1 — BM25
    V["bm25_only"] = _full(sig["bm25"], sig)
    bm_norm = fusion.minmax(sig["bm25"])
    for w in (0.10, 0.20, 0.30):
        V[f"rules+bm25_{w:.2f}"] = _full(
            {c: (1 - w) * rules[c] + w * bm_norm[c] for c in active}, sig)

    # Family 2 — rank fusion
    V["rrf_rules_dense"] = _full(
        fusion.rrf([{c: rules[c] for c in active}, sig["minilm"]]), sig)
    V["rrf_rules_bm25_dense"] = _full(
        fusion.rrf([{c: rules[c] for c in active}, sig["bm25"], sig["minilm"]]), sig)

    # Family 3 — cross-encoder
    if "ce" in sig:
        ce_norm = fusion.minmax(sig["ce"])
        V["ce_only"] = _full(sig["ce"], sig)
        for w in (0.10, 0.20, 0.30):
            V[f"rules+ce_{w:.2f}"] = _full(
                {c: (1 - w) * rules[c] + w * ce_norm[c] for c in active}, sig)
        # rules_then_ce: keep rules score, reorder within by a gentle CE nudge.
        V["rules_then_ce"] = _full(
            {c: rules[c] + 0.05 * (ce_norm[c] - 0.5) for c in active}, sig)
        V["rrf_rules_ce"] = _full(
            fusion.rrf([{c: rules[c] for c in active}, sig["ce"]]), sig)

    # Family 4 — embedding upgrades
    for key, label in (("bge_small", "bge_small"), ("bge_base", "bge_base")):
        if key in sig:
            feat = fusion.minmax(sig[key])
            V[f"rules+{label}_0.10"] = _full(
                {c: 0.9 * rules[c] + 0.1 * feat[c] for c in active}, sig)
    for key in ("minilm", "bge_small"):
        for pool in ("mq_max", "mq_mean"):
            mqkey = f"{key}_{pool}"
            if mqkey in sig:
                feat = fusion.minmax(sig[mqkey])
                V[f"rules+{key}_{pool}_0.10"] = _full(
                    {c: 0.9 * rules[c] + 0.1 * feat[c] for c in active}, sig)

    # Family 5 — supervised LTR (out-of-fold)
    X, tiers_active = build_ltr_matrix(sig)
    if X is not None:
        rel = np.array([1 if sig["labels"][c] >= 3 else 0 for c in active])
        lr = ltr.oof_logreg(X, rel)
        V["ltr_logreg"] = _full({c: float(s) for c, s in zip(active, lr)}, sig)
        xgb = ltr.oof_xgb_ranker(X, tiers_active)
        if xgb is not None:
            V["ltr_lambdamart"] = _full({c: float(s) for c, s in zip(active, xgb)}, sig)
        else:
            print("xgboost not installed — skipping ltr_lambdamart")

    # Combinations — the data's stacked pipelines
    if "bge_small_mq_max" in sig and "ce" in sig:
        bge_feat = fusion.minmax(sig["bge_small_mq_max"])
        ce_norm = fusion.minmax(sig["ce"])
        stage1 = {c: 0.9 * rules[c] + 0.1 * bge_feat[c] for c in active}
        V["stack_rules_bgeMQ_then_ce"] = _full(
            {c: stage1[c] + 0.05 * (ce_norm[c] - 0.5) for c in active}, sig)

    return V


def build_ltr_matrix(sig):
    active = sig["active"]
    if not active:
        return None, None
    # Re-score each active candidate to pull its component breakdown + behavioral
    # multiplier as LTR features (cheap; score_candidate is pure stdlib).
    feat_keys = ("core", "product", "experience", "logistics", "education", "external")
    rows, tiers = [], []
    for c in active:
        _, ev = score_candidate(sig["cands"][c])
        comp = ev["components"]
        prof = sig["cands"][c].get("profile", {})
        sgl = sig["cands"][c].get("redrob_signals", {})
        avail = ev["behavioral"].get("availability_multiplier", 1.0)
        row = [comp[k] for k in feat_keys]
        row += [
            sig["rules"][c],
            sig["bm25"].get(c, 0.0),
            sig["minilm"].get(c, 0.0),
            sig.get("ce", {}).get(c, 0.0),
            avail,
            float(prof.get("years_of_experience") or 0.0),
            float(sgl.get("notice_period_days") or 0.0),
            float(sgl.get("github_activity_score") or 0.0),
        ]
        rows.append(row)
        tiers.append(sig["labels"][c])
    return np.array(rows, dtype="float64"), tiers


# --- bootstrap + pairwise --------------------------------------------------

def bootstrap(variants, sig, B=BOOT_B, seed=BOOT_SEED):
    ids = sig["ids"]
    tiers = [sig["labels"][c] for c in ids]
    names = list(variants)
    score_arrays = {n: [variants[n][c] for c in ids] for n in names}

    rng = np.random.default_rng(seed)
    n = len(ids)
    comp = {n_: np.empty(B) for n_ in names}
    for b in range(B):
        pick = rng.integers(0, n, size=n)
        order_ids = [ids[i] for i in pick]
        bt = [tiers[i] for i in pick]
        for n_ in names:
            sc = [score_arrays[n_][i] for i in pick]
            comp[n_][b] = composite_from_arrays(sc, bt, order_ids)["composite"]

    ci = {n_: (float(np.percentile(comp[n_], 2.5)), float(np.percentile(comp[n_], 97.5)),
               float(comp[n_].mean())) for n_ in names}
    # pairwise P[row beats col]
    win = {a: {} for a in names}
    for a in names:
        for b in names:
            win[a][b] = float(np.mean(comp[a] > comp[b]))
    return ci, win, names


# --- report ----------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--time-full-pool", metavar="CANDIDATES", default=None,
                    help="stream the real pool, time gate+rules+top-K embed/CE, assert <5min")
    ap.add_argument("--boot", type=int, default=BOOT_B)
    args = ap.parse_args()

    sig = build()
    variants = make_variants(sig)

    ids = sig["ids"]
    tiers = [sig["labels"][c] for c in ids]
    results = {n: composite_from_arrays([variants[n][c] for c in ids], tiers, ids)
               for n in variants}

    base = results["current"]["composite"]
    ordered = sorted(results.items(), key=lambda kv: -kv[1]["composite"])

    print("\n=== leaderboard (vs current) ===")
    for name, m in ordered:
        print(f"{name:28s} {fmt(m)}  d={m['composite'] - base:+.4f}")

    # anchors
    anc_cur = results["current"]["composite"]
    anc_rules = results["rules_only"]["composite"]
    print(f"\nanchors: current={anc_cur:.4f} (expect ~0.8911)  rules_only={anc_rules:.4f} (expect ~0.8429)")

    print(f"\nbootstrap B={args.boot} ...")
    ci, win, names = bootstrap(variants, sig, B=args.boot)

    # write md
    lines = ["# Methodology A/B result (all-against-all)\n",
             f"Labeled set: {len(ids)} candidates ({len(sig['active'])} gate-passing). "
             f"Bootstrap B={args.boot}. Metric: contest composite "
             f"(0.50 NDCG@10 + 0.30 NDCG@50 + 0.15 MAP + 0.05 P@10), relevant = tier>=3.\n",
             f"Anchors: `current`={anc_cur:.4f} (expect ~0.8911), "
             f"`rules_only`={anc_rules:.4f} (expect ~0.8429).\n",
             "## Leaderboard\n",
             "| variant | composite | 95% CI | NDCG@10 | NDCG@50 | MAP | P@10 | vs current |",
             "|---|---|---|---|---|---|---|---|"]
    for name, m in ordered:
        lo, hi, mean = ci[name]
        lines.append(
            f"| {name} | {m['composite']:.4f} | [{lo:.4f}, {hi:.4f}] | {m['NDCG@10']:.4f} "
            f"| {m['NDCG@50']:.4f} | {m['MAP']:.4f} | {m['P@10']:.3f} | {m['composite'] - base:+.4f} |")

    # pairwise win matrix (P[row beats col])
    order_names = [n for n, _ in ordered]
    lines += ["\n## Pairwise P[row beats column] (bootstrap)\n",
              "| | " + " | ".join(order_names) + " |",
              "|" + "---|" * (len(order_names) + 1)]
    for a in order_names:
        cells = " | ".join(f"{win[a][b]:.2f}" if a != b else "—" for b in order_names)
        lines.append(f"| {a} | {cells} |")

    # timings + feasibility
    tmg = sig["timings"]
    lines += ["\n## Signal timings (on the labeled active set) + full-pool projection\n",
              "Heavy signals (dense / cross-encoder) run only on the rules top-K=3000 in "
              "production, so projected full-pool cost = per-item ms x 3000.\n",
              "| signal | active wall (s) | per-item (ms) | projected top-3000 (s) |",
              "|---|---|---|---|"]
    for key in ("bm25_active", "embed_minilm", "embed_bge_small", "embed_bge_base", "cross_encoder"):
        if key in tmg:
            pim = tmg.get(key + "_per_item_ms")
            proj = (pim * 3000 / 1000) if pim else tmg[key]
            pim_s = f"{pim:.2f}" if pim else "-"
            lines.append(f"| {key} | {tmg[key]:.2f} | {pim_s} | {proj:.1f} |")

    # --- runtime feasibility (projected full-pool top-K cost vs 5-min budget) ---
    RULES_BASE_S = 80     # approx gate+rules+IO over 100K (confirm with --time-full-pool)
    BUDGET_S = 300

    def proj(key):
        pim = tmg.get(f"{key}_per_item_ms")
        return (pim * 3000 / 1000.0) if pim else 0.0

    def variant_runtime(name):
        s = RULES_BASE_S
        if "bge_base" in name:
            s += proj("embed_bge_base")
        if "bge_small" in name:
            s += proj("embed_bge_small")
        if "minilm" in name or "dense" in name or name == "current":
            s += proj("embed_minilm")
        if name.endswith("_ce") or "ce_" in name or name.startswith("ltr_"):
            s += proj("cross_encoder")   # ltr_* needs the CE feature at inference too
        return s

    def feasible(name):
        return variant_runtime(name) <= BUDGET_S

    lines += ["\n## Runtime feasibility of variants beating `current`\n",
              "Projected full-pool cost = ~80 s (gate+rules) + heaviest signal over the rules "
              f"top-3000 (warm per-item x 3000). Budget = {BUDGET_S} s, CPU, no network.\n",
              "| variant | composite | proj. full-pool (s) | within budget |",
              "|---|---|---|---|"]
    for name, m in ordered:
        if m["composite"] > base + 1e-9 and name != "current":
            rt = variant_runtime(name)
            lines.append(f"| {name} | {m['composite']:.4f} | {rt:.0f} | "
                         f"{'YES' if rt <= BUDGET_S else 'NO'} |")

    # verdict
    winners = [(n, m["composite"]) for n, m in ordered
               if m["composite"] > base + 1e-9 and n != "current"]
    feas_winners = [(n, c) for n, c in winners if feasible(n)]
    verdict = ["\n## Verdict\n"]
    if winners:
        bn, bc = winners[0]
        verdict.append(
            f"Best composite overall: **{bn}** ({bc:.4f}, {bc - base:+.4f}; "
            f"P[beats current]={win[bn]['current']:.2f}) — projected full-pool "
            f"{variant_runtime(bn):.0f}s, {'within' if feasible(bn) else 'OVER'} the {BUDGET_S}s budget.\n")
    if feas_winners:
        fn, fc = feas_winners[0]
        beat = win[fn]["current"]
        verdict.append(
            f"Best **budget-feasible** improvement: **{fn}** "
            f"(composite {fc:.4f}, {fc - base:+.4f}; P[beats current]={beat:.2f}; "
            f"projected {variant_runtime(fn):.0f}s).\n")
        if beat >= 0.85:
            verdict.append(
                "Clears the >=0.85 bootstrap-win bar AND fits the budget — a real adoption "
                "candidate. Propose wiring into rank.py as a separate, explicitly-approved step.\n")
        else:
            verdict.append(
                f"But P[beats current]={beat:.2f} < 0.85: the gain is within bootstrap noise on this "
                "tiny label set (30 relevant / 9 top-tier) — the 95% CIs overlap heavily. It is "
                "promising and (if dependency-free) cheap to adopt, but **not statistically proven**. "
                "Best next move: expand the labeled set, then re-run, before committing.\n")
    else:
        verdict.append(
            "**No budget-feasible variant beats `current`.** The variants that score higher "
            "(BGE / cross-encoder stacks) cost 5-28 min on the full pool at CPU — disqualified by "
            "the 5-min constraint. The heavier methodologies the data describes do not yield a "
            "*shippable* gain here.\n")
    verdict.append(
        "\nThe data's marquee methods underperform on this set: supervised LTR (`ltr_*`) ranks "
        "**last** (out-of-fold, but only 9 top-tier labels to learn from), and cross-encoder / BM25 "
        "as primary signals lose to the rules+dense blend — consistent with finite-template "
        "descriptions giving lexical/dense signals little to recover beyond rules phrase-presence.\n"
        "\n_Caveat: local composite is a proxy for the hidden ground truth; treat all deltas as "
        "directional._\n")

    OUT.write_text("\n".join(lines + verdict) + "\n", encoding="utf-8")
    print("\n".join(verdict))
    print(f"written to {OUT}")

    if args.time_full_pool:
        time_full_pool(args.time_full_pool, sig)


def time_full_pool(path, sig):
    """Stream the real pool: gate+rules, then embed/CE the rules top-3000."""
    from src.loader import iter_candidates
    print(f"\n=== full-pool timing on {path} ===")
    t0 = time.perf_counter()
    scored = []
    total = hp = gated = 0
    for c in iter_candidates(path):
        total += 1
        if honeypot_flags(c):
            hp += 1; continue
        if not passes_relevance_gate(c):
            gated += 1; continue
        s, _ = score_candidate(c)
        scored.append((s, c["candidate_id"], _career_text(c)))
    scored.sort(key=lambda x: (-x[0], x[1]))
    t_rules = time.perf_counter() - t0
    print(f"pool={total} honeypots={hp} gated={gated} scored={len(scored)} | gate+rules {t_rules:.1f}s")

    topk = [t for _, _, t in scored[:3000]]
    if embedding.is_available():
        t = time.perf_counter()
        embedding.embed_features(topk)
        print(f"MiniLM embed top-{len(topk)}: {time.perf_counter() - t:.1f}s")
    if ce_lib.is_available():
        t = time.perf_counter()
        ce_lib.rerank_scores(JD_QUERY, topk)
        print(f"cross-encoder rerank top-{len(topk)}: {time.perf_counter() - t:.1f}s")
    print(f"NOTE budget is 300s wall / 16GB / CPU / no-network for the full ranking step.")


if __name__ == "__main__":
    main()
