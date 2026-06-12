"""Hard filters: honeypot consistency checks and the JD relevance gate.

Honeypots (~80 in the pool) are profiles with internally impossible facts.
The ground truth forces them to tier 0 and a >10% honeypot rate in the
top 100 disqualifies the submission, so anything flagged here is excluded
from ranking entirely.

The relevance gate is deliberately recall-oriented: it only removes
candidates with no plausible connection to ML/IR work at all. Precision
is the scorer's job, not the gate's.
"""

import re
from datetime import date

# --- Honeypot / consistency checks -----------------------------------------

# "Expert" proficiency claimed with almost no time using the skill.
EXPERT_MIN_MONTHS = 6
# Allowed gap between stated years_of_experience and summed career history.
# Career gaps between jobs are normal, so stated > summed is judged more
# leniently than summed > stated (which means claimed years don't exist).
YOE_OVERCLAIM_TOLERANCE = 3.0
YOE_UNDERCLAIM_TOLERANCE = 5.0


def _parse_date(s):
    try:
        return date.fromisoformat(s)
    except (TypeError, ValueError):
        return None


def honeypot_flags(cand):
    """Return a list of human-readable inconsistency flags (empty = clean)."""
    flags = []
    profile = cand.get("profile", {})
    career = cand.get("career_history", [])
    skills = cand.get("skills", [])

    # Expert skills with near-zero usage time. duration_months is optional
    # in the schema; only judge skills where it is present.
    bogus_experts = [
        s["name"]
        for s in skills
        if s.get("proficiency") == "expert"
        and isinstance(s.get("duration_months"), int)
        and s["duration_months"] <= EXPERT_MIN_MONTHS
    ]
    if len(bogus_experts) >= 2:
        flags.append(
            f"{len(bogus_experts)} 'expert' skills with <= {EXPERT_MIN_MONTHS} months use"
        )

    # Stated experience vs summed career history.
    stated = profile.get("years_of_experience")
    summed = sum(j.get("duration_months", 0) for j in career) / 12.0
    if isinstance(stated, (int, float)):
        if stated - summed > YOE_OVERCLAIM_TOLERANCE:
            flags.append(
                f"claims {stated:.1f} yrs but career history sums to {summed:.1f}"
            )
        elif summed - stated > YOE_UNDERCLAIM_TOLERANCE:
            flags.append(
                f"career history sums to {summed:.1f} yrs but claims only {stated:.1f}"
            )

    # Per-job date sanity: end before start, or duration wildly off the dates.
    for job in career:
        start = _parse_date(job.get("start_date"))
        end = _parse_date(job.get("end_date"))
        months = job.get("duration_months")
        if start and end:
            if end < start:
                flags.append(f"job at {job.get('company')} ends before it starts")
                continue
            span = (end.year - start.year) * 12 + (end.month - start.month)
            if isinstance(months, int) and abs(span - months) > 6:
                flags.append(
                    f"job at {job.get('company')} claims {months} months over a "
                    f"{span}-month date span"
                )

    # NOT checked, despite looking tempting (measured on the real pool):
    # - last_active before signup: fires on 7,496 candidates — the generator
    #   draws these dates independently, so it carries no honeypot signal.
    # - first job predating education: fires on 3,457 and is legitimately
    #   ambiguous (mid-career degrees).
    return flags


# --- Relevance gate ---------------------------------------------------------

# Titles that are direct evidence of ML/IR work.
ML_TITLE_RE = re.compile(
    r"machine learning|ml engineer|\bml\b|ai engineer|ai research|ai specialist"
    r"|data scien|nlp|recommendation|search engineer|computer vision"
    r"|applied scientist|deep learning",
    re.IGNORECASE,
)

# Tech titles adjacent enough that strong text evidence can qualify them
# (the "plain-language Tier 5s" hide here).
ADJACENT_TITLE_RE = re.compile(
    r"data engineer|analytics engineer|backend|software engineer|full stack"
    r"|data analyst|platform engineer",
    re.IGNORECASE,
)

# Free-text evidence of the work the JD actually cares about: production
# ranking / retrieval / recommendation / NLP systems.
ML_EVIDENCE_RE = re.compile(
    r"ranking model|learning.to.rank|recommendation|recommender|retrieval"
    r"|embedding|semantic search|vector (?:search|database|index)|BM25"
    r"|search relevance|relevance model|NDCG|fine.tun|transformer|\bLLM\b"
    r"|\bRAG\b|\bNLP\b|machine.learning|ML (?:model|pipeline|system|stack)"
    r"|XGBoost|LightGBM|feature (?:engineering|pipeline)|A/B test"
    r"|offline.online|click.through|two.tower|collaborative filtering",
    re.IGNORECASE,
)


def _career_text(cand):
    parts = [cand.get("profile", {}).get("summary", "")]
    parts.append(cand.get("profile", {}).get("headline", ""))
    for job in cand.get("career_history", []):
        parts.append(job.get("title", ""))
        parts.append(job.get("description", ""))
    return " ".join(p for p in parts if p)


def passes_relevance_gate(cand):
    """True if the candidate has any plausible ML/IR connection."""
    titles = [j.get("title", "") for j in cand.get("career_history", [])]
    titles.append(cand.get("profile", {}).get("current_title", ""))
    all_titles = " | ".join(titles)

    if ML_TITLE_RE.search(all_titles):
        return True

    text = _career_text(cand)
    evidence = ML_EVIDENCE_RE.findall(text)
    if ADJACENT_TITLE_RE.search(all_titles) and evidence:
        return True
    # No tech title at all: require strong, repeated evidence before letting
    # the candidate through (keyword stuffers put noise in skills, not here,
    # but stay conservative).
    return len(evidence) >= 3
