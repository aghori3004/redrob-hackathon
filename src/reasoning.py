"""Evidence-based reasoning generation (Phase 5).

Composes a short justification for each ranked candidate strictly from the
fields the scorer actually read and the evidence it produced — never from
anything else — so the reasoning cannot hallucinate facts the ranking did
not use. Tone is matched to rank (glowing at the top, measured lower down)
and concerns surfaced from the same evidence that shaped the score.

    reasoning_for(cand, evidence, rank) -> str
"""

# Readable phrasings for the core-IR evidence keys (src/scoring.py).
IR_PHRASES = {
    "learning_to_rank": "learning-to-rank",
    "ranking": "ranking systems",
    "recommendation": "recommendation systems",
    "retrieval": "retrieval",
    "ranking_eval": "ranking evaluation (NDCG/A-B testing)",
    "vector_search": "vector search",
}
SUPPORT_PHRASES = {
    "nlp": "NLP",
    "llm_work": "LLMs/fine-tuning",
    "ml_systems": "production ML systems",
    "ltr_models": "gradient-boosted models",
    "features": "feature engineering",
}

# Rank-banded openers (a small rotation per band keeps the column varied).
OPENERS = {
    "elite": ["Exceptional match", "Top-tier fit", "Standout candidate"],
    "strong": ["Strong match", "Strong fit", "Highly relevant"],
    "solid": ["Solid match", "Good fit", "Relevant candidate"],
    "qualified": ["Qualified match", "Reasonable fit", "Meets the bar"],
}


def _band(rank):
    if rank <= 10:
        return "elite"
    if rank <= 30:
        return "strong"
    if rank <= 60:
        return "solid"
    return "qualified"


def _join(items):
    items = list(items)
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + f", and {items[-1]}"


def reasoning_for(cand, evidence, rank):
    profile = cand.get("profile", {})
    core = evidence.get("core", {})
    logi = evidence.get("logistics", {})
    beh = evidence.get("behavioral", {})

    opener = OPENERS[_band(rank)][rank % 3]

    # --- sentence 1: who + the core relevance evidence ---------------------
    title = profile.get("current_title")
    company = profile.get("current_company")
    yoe = profile.get("years_of_experience")
    who = title or "Candidate"
    if company:
        who += f" at {company}"
    if isinstance(yoe, (int, float)):
        who += f" ({yoe:g}y experience)"

    ir = [IR_PHRASES[k] for k in core.get("ir", []) if k in IR_PHRASES]
    if ir:
        evidence_clause = f"with demonstrated {_join(ir[:4])} experience"
    else:
        support = [SUPPORT_PHRASES[k] for k in core.get("tier_b", []) if k in SUPPORT_PHRASES]
        evidence_clause = (
            f"with {_join(support[:3])} experience" if support
            else "with adjacent ML/engineering experience"
        )

    prod = evidence.get("product", {})
    total_m = prod.get("total_months", 0) or 0
    if total_m and prod.get("product_months", 0) / total_m >= 0.6:
        evidence_clause += " at product companies"

    s1 = f"{opener}: {who} {evidence_clause}."

    # --- sentence 2: supporting strengths + concerns -----------------------
    strengths = []
    support = [SUPPORT_PHRASES[k] for k in core.get("tier_b", []) if k in SUPPORT_PHRASES]
    if ir and support:
        strengths.append(_join(support[:2]) + " depth")
    gh = evidence.get("external", {}).get("github")
    if isinstance(gh, (int, float)) and gh >= 50:
        strengths.append("an active public code footprint")
    loc = logi.get("location")
    if logi.get("country") == "India" and loc:
        strengths.append(f"based in {loc}")
    elif logi.get("relocate"):
        strengths.append("open to relocation")
    if beh.get("open_to_work"):
        strengths.append("open to work")

    concerns = []
    for dq in evidence.get("disqualifiers", []):
        concerns.append({
            "research_only": "a research-leaning background with limited production signal",
            "consulting_only": "an all-services career history",
            "llm_wrapper_profile": "mostly LLM-wrapper rather than core IR work",
            "cv_speech_only": "a CV/speech focus with thin NLP/IR exposure",
            "non_coding_senior": "a recent management/architect tilt",
            "geo_ineligible": "located outside India without a relocation signal",
            "title_chaser_tenure": "short tenures across roles",
        }.get(dq, dq))
    notice = logi.get("notice_days")
    if isinstance(notice, int) and notice > 60:
        concerns.append(f"a {notice}-day notice period")
    if isinstance(yoe, (int, float)) and not (5 <= yoe <= 9):
        side = "below" if yoe < 5 else "above"
        concerns.append(f"experience {side} the 5-9y band")
    days = beh.get("last_active_days")
    if isinstance(days, int) and days > 180:
        concerns.append("limited recent platform activity")

    parts = []
    if strengths:
        parts.append("Strengths: " + _join(strengths[:3]) + ".")
    if concerns:
        parts.append("Watch: " + _join(concerns[:2]) + ".")
    s2 = " ".join(parts)

    return (s1 + (" " + s2 if s2 else "")).strip()
