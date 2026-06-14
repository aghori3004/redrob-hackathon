"""Turn the rules scorer's evidence into a suggested label tier (0-5) plus a
short plain-language reason, applying the same rubric the human uses.

This is a *suggestion to challenge*, not ground truth — it is derived from the
same scorer the labels are meant to audit, so accepting it blindly would defeat
the purpose. It exists to make labeling fast: agree with one keypress, or
override when your read of the profile differs.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.scoring import score_candidate


def suggest_tier(cand):
    """Return (tier, reason_str, model_score)."""
    score, ev = score_candidate(cand)
    core = ev["core"]
    ir = core["ir"]
    n_ir = len(ir)
    title = core["title_score"]
    tier_b = core["tier_b"]
    dq = ev["disqualifiers"]
    yoe = ev["experience"]["yoe"]
    logi = ev["logistics"]
    beh = ev["behavioral"]
    notes = []

    # --- base tier from depth of production IR evidence + title ---
    if n_ir >= 4 and title >= 0.7:
        base = 5
        notes.append(f"deep IR: {n_ir} core capabilities ({', '.join(ir)}) + ML title")
    elif n_ir >= 2 and title >= 0.7:
        base = 4
        notes.append(f"solid IR: {n_ir} capabilities ({', '.join(ir)}) + ML title")
    elif n_ir >= 1:
        base = 3
        notes.append(f"real but thin IR: {n_ir} capability ({', '.join(ir)})")
    elif tier_b and title >= 0.35:
        base = 2
        notes.append("ML/NLP evidence but no core ranking/retrieval/recsys")
    elif title >= 0.35:
        base = 2
        notes.append("adjacent tech, no production ML/IR evidence")
    else:
        base = 1
        notes.append("little ML/IR evidence in descriptions")

    tier = base

    # --- minor concerns nudge the top tiers down by one ---
    if base >= 4:
        if isinstance(yoe, (int, float)) and not (6 <= yoe <= 8):
            if not (5 <= yoe <= 9):
                tier = min(tier, 4)
                notes.append(f"{yoe}y outside 5-9 band")
            else:
                notes.append(f"{yoe}y (band edge)")
        nd = logi.get("notice_days")
        if isinstance(nd, int) and nd >= 90:
            tier = min(tier, 4)
            notes.append(f"{nd}d notice period")

    # --- hard caps (JD "will not move forward") ---
    if "research_only" in dq:
        tier = min(tier, 1); notes.append("CAP->1: research-only, no production")
    if "geo_ineligible" in dq:
        tier = min(tier, 1); notes.append("CAP->1: outside India, won't relocate")
    if "llm_wrapper_profile" in dq:
        tier = min(tier, 2); notes.append("CAP->2: LLM-wrapper-only AI")
    if "non_coding_senior" in dq:
        tier = min(tier, 2); notes.append("CAP->2: no hands-on code (architect/mgr)")

    # --- demotions (drop one tier) ---
    for key, label in (
        ("consulting_only", "consulting-only career"),
        ("title_chaser_tenure", "title-chaser tenure (median <18mo)"),
        ("cv_speech_only", "CV/speech specialty, no NLP/IR"),
    ):
        if key in dq:
            tier = max(0, tier - 1); notes.append(f"DEMOTE: {label}")

    # --- behavioral cap ---
    la = beh.get("last_active_days")
    rr = beh.get("response_rate")
    if isinstance(la, int) and la > 180 and isinstance(rr, (int, float)) and rr <= 0.10:
        tier = min(tier, 2); notes.append("CAP->2: effectively unreachable")
    elif beh.get("availability_multiplier", 1.0) < 0.7:
        notes.append("availability concern (stale/unresponsive)")

    return tier, "; ".join(notes), round(score, 4)
