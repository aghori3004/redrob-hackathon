# Scorer sensitivity / ablation result

## 1. Full-pool top-100 churn (what determines the ranking)

Gate-passing pool: 19025. Each row = how many of the top-100 change when the assumption is removed (penalty dropped, or component signal neutralized to its mean).

| ablation | top-100 changed | (fires on N gate-passing) |
|---|---|---|
| drop penalty `geo_ineligible` | 5 | 3157 |
| drop penalty `consulting_only` | 0 | 2112 |
| drop penalty `title_chaser_tenure` | 10 | 1068 |
| drop penalty `non_coding_senior` | 0 | 204 |
| drop penalty `research_only` | 0 | 0 |
| drop penalty `llm_wrapper_profile` | 0 | 0 |
| drop penalty `cv_speech_only` | 0 | 0 |
| neutralize component `core` (w=0.62) | 60 | — |
| neutralize component `experience` (w=0.14) | 10 | — |
| neutralize component `logistics` (w=0.1) | 2 | — |
| neutralize component `product` (w=0.06) | 6 | — |
| neutralize component `education` (w=0.04) | 1 | — |
| neutralize component `external` (w=0.04) | 1 | — |

## 2. Labeled-composite ablation (what the 200 labels support)

Rules-only baseline composite = 0.8429. `delta` = change when the assumption is REMOVED; **positive delta = the assumption was HURTING the labeled composite**. Caveat: 200 noisy labels (30 relevant) — directional only, all within bootstrap noise.

| ablation | delta composite |
|---|---|
| drop penalty `geo_ineligible` (fires 14x) | +0.0000 |
| drop penalty `title_chaser_tenure` (fires 9x) | -0.0043 |
| drop penalty `consulting_only` (fires 7x) | -0.0027 |
| neutralize component `core` | -0.2141 |
| neutralize component `experience` | +0.0417 |
| neutralize component `logistics` | +0.0632 |
| neutralize component `product` | +0.0075 |
| neutralize component `education` | -0.0009 |
| neutralize component `external` | +0.0405 |

## 3. Top-100 honeypot margin (hard >10% disqualifier)

| submission | hard honeypots in top-100 | near-tolerance soft signals |
|---|---|---|
| submission.csv | 0 | 2 |
| submission_mq.csv | 0 | 2 |

## Reading

- **The ranking rests on `core_relevance`** (60/100 top-100 churn when neutralized; neutralizing it craters the labeled composite -0.21). That is the most JD-aligned, label-validated signal (IR/ranking depth) — the ranking is fundamentally sound.

- **Disqualifiers are low-risk.** Only `geo_ineligible` (5) and `title_chaser_tenure` (10) move the top-100 at all; `consulting_only`, `research_only`, `cv_speech_only`, `llm_wrapper`, `non_coding` move 0. All have <=0.004 labeled-composite effect. Leave them.

- **The real calibration tension:** neutralizing `logistics` (+0.063), `experience` (+0.042) and `external` (+0.040) each *improves* the labeled composite — i.e. as weighted they pull the ranking away from the labels. BUT `experience` (5-9y band) and `logistics` (India / notice) encode *explicit* JD must-haves, so they are likely right for the hidden ground truth even where the noisy local labels under-credit them. `external_validation` (GitHub) is the least JD-central and the clearest down-weight candidate.

- **Honeypot margin is safe** (0/100 in the top-100; the >10% rule is a hard DQ).

- **Action now: change nothing.** Every delta here is inside the +/-0.14 bootstrap band of the 200-label set. These are directional flags to re-test *after* the labeled set expands; priority to re-examine then: `logistics` >= `experience` >= `external` weighting.

