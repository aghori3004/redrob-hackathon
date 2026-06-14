"""Supervised learning-to-rank — out-of-fold only.

The dataset's profiles lean heavily on LambdaMART / gradient-boosted rankers
(XGBoost, LightGBM) over engineered features. We test that here, but with a
hard statistical guardrail: with only ~30 relevant and ~9 top-tier labels, a
model fit and scored on the same 200 candidates would memorize them. So every
prediction used in the leaderboard is **out-of-fold** — produced by a model
that never saw that candidate's label (grouped k-fold). Even so, treat these
numbers as suggestive, not decisive.

Two learners:
  * oof_xgb_ranker — XGBoost rank:pairwise (LambdaMART family), gain = tier.
  * oof_logreg     — numpy logistic regression on relevant(tier>=3); a
                     lower-variance comparison point that can't be installed
                     away and won't overfit as hard as boosted trees on 200 rows.
"""

import numpy as np


def kfold_indices(n, k, seed=42):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(n)
    folds = np.array_split(idx, k)
    for i in range(k):
        test = folds[i]
        train = np.concatenate([folds[j] for j in range(k) if j != i])
        yield np.sort(train), np.sort(test)


def standardize(train_X, X):
    mu = train_X.mean(axis=0)
    sd = train_X.std(axis=0)
    sd[sd == 0] = 1.0
    return (X - mu) / sd


def oof_logreg(X, rel, k=5, seed=42, iters=500, lr=0.3, l2=1.0):
    """Out-of-fold logistic-regression probabilities for relevant(tier>=3)."""
    n, d = X.shape
    oof = np.zeros(n)
    rel = rel.astype(np.float64)
    for train, test in kfold_indices(n, k, seed):
        Xtr = standardize(X[train], X[train])
        Xte = standardize(X[train], X[test])
        w = np.zeros(d)
        b = 0.0
        ytr = rel[train]
        for _ in range(iters):
            z = Xtr @ w + b
            p = 1.0 / (1.0 + np.exp(-z))
            g = p - ytr
            gw = Xtr.T @ g / len(train) + l2 * w / len(train)
            gb = g.mean()
            w -= lr * gw
            b -= lr * gb
        oof[test] = 1.0 / (1.0 + np.exp(-(Xte @ w + b)))
    return oof


def oof_xgb_ranker(X, tiers, k=5, seed=42):
    """Out-of-fold XGBoost rank:pairwise scores. Returns None if xgboost absent.

    Uses the native Booster API (xgb.train + DMatrix) so it needs only xgboost,
    not the scikit-learn wrapper dependency.
    """
    try:
        import xgboost as xgb
    except ImportError:
        return None
    n = X.shape[0]
    oof = np.zeros(n)
    tiers = np.asarray(tiers)
    params = {
        "objective": "rank:pairwise",
        "eta": 0.1,
        "max_depth": 3,
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "lambda": 2.0,
        "tree_method": "hist",
        "seed": seed,
    }
    for train, test in kfold_indices(n, k, seed):
        dtrain = xgb.DMatrix(X[train], label=tiers[train])
        # Single query per fold: the whole training set is one ranking group.
        dtrain.set_group([len(train)])
        bst = xgb.train(params, dtrain, num_boost_round=200)
        oof[test] = bst.predict(xgb.DMatrix(X[test]))
    return oof
