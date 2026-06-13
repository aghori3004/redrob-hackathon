"""JD-fit scoring for shortlisted candidates.

Additive fit components (weights sum to 1.0), then multiplicative JD
disqualifier penalties, then the behavioral availability multiplier:

    score = fit * disqualifier_multiplier * availability_multiplier

Severity of disqualifiers mirrors the JD's own language: "we will not
move forward" items crush the score; "we will probably not move forward"
and "things we do NOT want" items dent it but leave room for offsetting
strengths elsewhere in the profile.

The skills array is never scored for relevance — measured on the real
pool it is uniformly random noise (every skill ~12.1K occurrences).
Relevance evidence comes from titles, summaries, and career descriptions.
"""

import re
from .behavioral import availability_multiplier

# --- Relevance evidence ------------------------------------------------------

# Direct hits on what the JD's "absolutely need" list describes: production
# ranking / retrieval / recommendation / search systems and their evaluation.
TIER_A_PHRASES = {
    "learning_to_rank": re.compile(r"learning.to.rank|\bLTR\b", re.I),
    "ranking": re.compile(r"ranking (?:model|layer|system|pipeline)|re.rank", re.I),
    "recommendation": re.compile(r"recommendation|recommender|collaborative filtering|two.tower", re.I),
    "retrieval": re.compile(r"retrieval|semantic search|hybrid search|search relevance|relevance model", re.I),
    "embeddings": re.compile(r"embedding", re.I),
    "vector_search": re.compile(r"vector (?:search|database|index)|FAISS|Pinecone|Weaviate|Qdrant|Milvus|OpenSearch|Elasticsearch|BM25", re.I),
    "ranking_eval": re.compile(r"NDCG|\bMRR\b|\bMAP@|offline.online|A/B test|click.through|relevance label", re.I),
}

# Adjacent ML/NLP production evidence the JD likes but doesn't require.
TIER_B_PHRASES = {
    "nlp": re.compile(r"\bNLP\b|natural language", re.I),
    "ml_systems": re.compile(r"machine.learning|ML (?:model|pipeline|system|stack|infra)", re.I),
    "llm_work": re.compile(r"fine.tun|\bLoRA\b|\bPEFT\b|transformer|\bLLM\b|\bRAG\b", re.I),
    "ltr_models": re.compile(r"XGBoost|LightGBM|gradient boost", re.I),
    "features": re.compile(r"feature (?:engineering|pipeline|store)", re.I),
}

# The JD's "absolutely need" heart: production ranking / retrieval /
# recommendation / search and their evaluation. Depth across these distinct
# capabilities is what separates a tier-5 (ideal) from a tier-3 (relevant)
# in the labeling rubric, so core_relevance grades the *count* of these,
# not mere presence. `embeddings` is supporting evidence, not core IR.
CORE_IR_KEYS = {
    "learning_to_rank", "ranking", "recommendation",
    "retrieval", "ranking_eval", "vector_search",
}

ML_TITLE_RE = re.compile(
    r"machine learning|ml engineer|\bml\b|ai engineer|ai research|ai specialist"
    r"|data scien|nlp|recommendation|search engineer|applied scientist|deep learning",
    re.I,
)
ADJACENT_TITLE_RE = re.compile(
    r"data engineer|analytics engineer|backend|software engineer|full stack|platform engineer",
    re.I,
)

# JD: people whose primary expertise is CV/speech/robotics without NLP/IR.
CV_SPEECH_RE = re.compile(
    r"computer vision|image (?:classification|segmentation|recognition)|object detection"
    r"|speech (?:recognition|synthesis)|robotics|autonomous",
    re.I,
)
# JD: "<12 months LangChain calling OpenAI" archetype.
WRAPPER_RE = re.compile(r"LangChain|OpenAI API|GPT.4 (?:API|wrapper)|prompt engineering", re.I)
# JD: research-only careers without production deployment.
RESEARCH_TITLE_RE = re.compile(r"research (?:scientist|fellow|assistant|associate)|professor|postdoc|phd", re.I)
PRODUCTION_RE = re.compile(r"production|deploy|shipped|launched|real users|at scale|serving", re.I)
# JD: seniors who stopped writing code ("architecture"/"tech lead" drift).
NONCODING_TITLE_RE = re.compile(r"architect|head of|director|vp |manager", re.I)

# Consulting / pure-services firms the JD treats as a negative when the
# entire career is spent there.
CONSULTING_COMPANY_RE = re.compile(
    r"TCS|Tata Consultancy|Infosys|Wipro|Accenture|Cognizant|Capgemini|Mindtree"
    r"|HCL|Tech Mahindra|LTI|Mphasis|Birlasoft|Hexaware|NIIT|Zensar",
    re.I,
)
SERVICES_INDUSTRIES = {"IT Services", "Consulting"}

PRODUCT_INDUSTRIES = {
    "AI/ML", "SaaS", "E-commerce", "Fintech", "Food Delivery", "AdTech",
    "EdTech", "Software", "Insurance Tech", "Transportation",
}

TIER1_PREFERRED = ("noida", "pune")
TIER1_CITIES = ("hyderabad", "mumbai", "delhi", "gurgaon", "gurugram", "bangalore", "bengaluru", "chennai", "kolkata")


def _career_text(cand):
    parts = [cand.get("profile", {}).get("summary", ""), cand.get("profile", {}).get("headline", "")]
    for job in cand.get("career_history", []):
        parts.append(job.get("title", ""))
        parts.append(job.get("description", ""))
    return " ".join(p for p in parts if p)


# --- Fit components (each returns score in [0,1] + evidence) ----------------

def core_relevance(cand, text):
    a_hits = sorted(k for k, rx in TIER_A_PHRASES.items() if rx.search(text))
    b_hits = sorted(k for k, rx in TIER_B_PHRASES.items() if rx.search(text))
    # Distinct evidence types matter, not occurrence counts — descriptions
    # repeat verbatim from a template pool, so counting occurrences would
    # reward long histories, not breadth of experience.
    ir_hits = [k for k in a_hits if k in CORE_IR_KEYS]
    # Depth of distinct core-IR capabilities is the dominant relevance
    # signal: 5+ of {LTR, ranking, recommendation, retrieval, ranking_eval,
    # vector_search} = ideal/tier-5 territory; 2-3 = merely relevant. This
    # no longer saturates at 4 generic tier-A hits the way the old formula
    # did (which scored tier-5s and tier-3s identically at ~1.0).
    ir_score = min(1.0, len(ir_hits) / 5.0)
    # Supporting ML/NLP/embedding evidence — useful but not differentiating.
    support_n = len(b_hits) + (1 if "embeddings" in a_hits else 0)
    support_score = min(1.0, support_n / 4.0)
    text_score = 0.8 * ir_score + 0.2 * support_score

    current = cand.get("profile", {}).get("current_title", "")
    past = " | ".join(j.get("title", "") for j in cand.get("career_history", []))
    if ML_TITLE_RE.search(current):
        title_score = 1.0
    elif ML_TITLE_RE.search(past):
        title_score = 0.7
    elif ADJACENT_TITLE_RE.search(current) or ADJACENT_TITLE_RE.search(past):
        title_score = 0.35
    else:
        title_score = 0.1

    # Lean on text evidence over title: every ML-titled candidate scores
    # title=1.0, so title alone can't order the top — depth of IR evidence
    # must drive the separation.
    return 0.3 * title_score + 0.7 * text_score, {
        "tier_a": a_hits, "tier_b": b_hits, "ir": ir_hits, "title_score": title_score,
    }


def product_company_score(cand):
    """Fraction of career months spent at product companies."""
    product_m = services_m = total_m = 0
    for job in cand.get("career_history", []):
        m = job.get("duration_months", 0) or 0
        total_m += m
        industry = job.get("industry", "")
        if industry in SERVICES_INDUSTRIES or CONSULTING_COMPANY_RE.search(job.get("company", "")):
            services_m += m
        elif industry in PRODUCT_INDUSTRIES:
            product_m += m
    if total_m == 0:
        return 0.3, {"product_months": 0}
    frac = product_m / total_m
    return 0.2 + 0.8 * frac, {"product_months": product_m, "services_months": services_m, "total_months": total_m}


def experience_fit(cand):
    yoe = cand.get("profile", {}).get("years_of_experience")
    if not isinstance(yoe, (int, float)):
        return 0.3, {"yoe": None}
    if 6 <= yoe <= 8:        # JD's "ideal candidate" sketch
        s = 1.0
    elif 5 <= yoe <= 9:      # the stated band
        s = 0.85
    elif 4 <= yoe <= 10:     # "seriously consider outside the band"
        s = 0.55
    elif 3 <= yoe <= 12:
        s = 0.3
    else:
        s = 0.1
    return s, {"yoe": yoe}


def logistics_fit(cand):
    profile = cand.get("profile", {})
    sig = cand.get("redrob_signals", {})
    country = profile.get("country", "")
    location = (profile.get("location") or "").lower()
    relocate = bool(sig.get("willing_to_relocate"))

    if country == "India":
        if any(c in location for c in TIER1_PREFERRED):
            loc = 1.0
        elif any(c in location for c in TIER1_CITIES):
            loc = 0.9
        else:
            loc = 0.8 if relocate else 0.6
    else:
        # JD: outside India case-by-case, no visa sponsorship.
        loc = 0.35 if relocate else 0.05

    notice = sig.get("notice_period_days")
    if not isinstance(notice, int):
        n = 0.6
    elif notice <= 30:       # JD: sub-30 loved, can buy out 30
        n = 1.0
    elif notice <= 60:       # "bar gets higher" but in scope
        n = 0.7
    elif notice <= 90:
        n = 0.5
    else:
        n = 0.3

    return 0.75 * loc + 0.25 * n, {"country": country, "location": profile.get("location"), "relocate": relocate, "notice_days": notice}


def education_fit(cand):
    best = 0.45  # no/unknown education: mild neutral, JD never requires a degree
    field_bonus = 0.0
    for edu in cand.get("education", []):
        tier = {"tier_1": 1.0, "tier_2": 0.8, "tier_3": 0.6, "tier_4": 0.5}.get(edu.get("tier"), 0.5)
        best = max(best, tier)
        if re.search(r"computer|machine learning|artificial|data", edu.get("field_of_study", ""), re.I):
            field_bonus = 0.1
    return min(1.0, best + field_bonus), {}


def external_validation(cand):
    # JD: closed-source-only careers without external validation are a concern.
    gh = cand.get("redrob_signals", {}).get("github_activity_score")
    if not isinstance(gh, (int, float)) or gh < 0:  # -1 sentinel = no GitHub linked
        return 0.5, {"github": None}
    return (0.5 + 0.5 * min(gh, 100) / 100), {"github": gh}


# Weights lean hard on core relevance: the labeling rubric tiers candidates
# primarily on depth of production ranking/retrieval evidence, and
# product-company fraction proved weakly correlated with the hand labels
# (tier-5s appear at 0.32 and 0.84; a tier-2 at 1.0), so it is down-weighted.
FIT_WEIGHTS = {
    "core_relevance": 0.62,
    "product_company": 0.06,
    "experience": 0.14,
    "logistics": 0.10,
    "education": 0.04,
    "external_validation": 0.04,
}


# --- JD disqualifier multipliers ---------------------------------------------

def disqualifier_multiplier(cand, text, evidence):
    """Multiplicative penalties mirroring the JD's stated severities."""
    mult = 1.0
    hits = []
    career = cand.get("career_history", [])
    titles = [j.get("title", "") for j in career]

    # "We will not move forward": research-only career, no production signal.
    if titles and all(RESEARCH_TITLE_RE.search(t) for t in titles) and not PRODUCTION_RE.search(text):
        mult *= 0.05
        hits.append("research_only")

    # Consulting-only entire career (current consulting job + prior product
    # experience is explicitly fine, so only the all-services case counts).
    if career:
        all_services = all(
            j.get("industry", "") in SERVICES_INDUSTRIES
            or CONSULTING_COMPANY_RE.search(j.get("company", ""))
            for j in career
        )
        if all_services:
            mult *= 0.3
            hits.append("consulting_only")

    # "Probably not": LLM-wrapper experience without real IR/ranking depth.
    if WRAPPER_RE.search(text) and not evidence["core"]["tier_a"]:
        mult *= 0.4
        hits.append("llm_wrapper_profile")

    # "Probably not": CV/speech/robotics specialty without NLP/IR exposure.
    if CV_SPEECH_RE.search(text) and not evidence["core"]["tier_a"] and "nlp" not in evidence["core"]["tier_b"]:
        mult *= 0.4
        hits.append("cv_speech_only")

    # "Probably not": senior who stopped coding — recent role is pure
    # architect/manager and the current description shows no hands-on signal.
    current = next((j for j in career if j.get("is_current")), None)
    if current and NONCODING_TITLE_RE.search(current.get("title", "")):
        if not re.search(r"\b(?:built|wrote|coded|implemented|developed|trained|shipped)\b", current.get("description", ""), re.I):
            mult *= 0.4
            hits.append("non_coding_senior")

    # Outside India and not willing to relocate: the JD offers no visa
    # sponsorship and sketches an in-India ideal. With 75K India-based
    # candidates available this is effectively disqualifying for a top-100,
    # so it must be multiplicative — as a weighted component it was provably
    # outweighed by core strength (caught by eval/invariants.py).
    profile = cand.get("profile", {})
    if profile.get("country") != "India" and not cand.get("redrob_signals", {}).get("willing_to_relocate"):
        mult *= 0.2
        hits.append("geo_ineligible")

    # "Do NOT want": title-chaser hopping pattern (3+ jobs, median stint <18mo).
    stints = sorted(j.get("duration_months", 0) or 0 for j in career)
    if len(stints) >= 3:
        median = stints[len(stints) // 2]
        if median < 18:
            mult *= 0.6
            hits.append("title_chaser_tenure")

    return mult, hits


# --- Main entry --------------------------------------------------------------

def score_candidate(cand):
    """Return (final_score, evidence) for a gate-passing candidate."""
    text = _career_text(cand)
    evidence = {}

    core, ev = core_relevance(cand, text)
    evidence["core"] = ev
    product, ev = product_company_score(cand)
    evidence["product"] = ev
    exp, ev = experience_fit(cand)
    evidence["experience"] = ev
    logi, ev = logistics_fit(cand)
    evidence["logistics"] = ev
    edu, _ = education_fit(cand)
    ext, ev = external_validation(cand)
    evidence["external"] = ev

    fit = (
        FIT_WEIGHTS["core_relevance"] * core
        + FIT_WEIGHTS["product_company"] * product
        + FIT_WEIGHTS["experience"] * exp
        + FIT_WEIGHTS["logistics"] * logi
        + FIT_WEIGHTS["education"] * edu
        + FIT_WEIGHTS["external_validation"] * ext
    )

    dq_mult, dq_hits = disqualifier_multiplier(cand, text, evidence)
    avail_mult, avail_ev = availability_multiplier(cand)

    evidence["components"] = {
        "core": round(core, 3), "product": round(product, 3), "experience": round(exp, 3),
        "logistics": round(logi, 3), "education": round(edu, 3), "external": round(ext, 3),
    }
    evidence["disqualifiers"] = dq_hits
    evidence["behavioral"] = avail_ev

    return fit * dq_mult * avail_mult, evidence
