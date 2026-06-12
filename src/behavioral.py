"""Behavioral availability multiplier from redrob_signals.

The signals doc frames these as "a multiplier or modifier on top of
skill-match scoring": a perfect-on-paper candidate who is unreachable is
not hireable. The multiplier is bounded to [0.5, 1.0] so availability can
halve a fit score but never zero out genuinely strong candidates.

-1 sentinel values (github_activity_score, offer_acceptance_rate) mean
"no data", not "bad" — they must map to neutral, never to a penalty.
"""

from datetime import date

# Fixed reference point for recency so the ranking is reproducible on any
# run date. The dataset's last_active dates extend through 2026-05.
REFERENCE_DATE = date(2026, 6, 1)


def _days_since(date_str):
    try:
        return (REFERENCE_DATE - date.fromisoformat(date_str)).days
    except (TypeError, ValueError):
        return None


def _recency_score(days):
    if days is None:
        return 0.5
    if days <= 30:
        return 1.0
    if days <= 90:
        return 0.8
    if days <= 180:
        return 0.55
    return 0.25  # the JD's "hasn't logged in for 6 months" case


def _response_time_score(hours):
    if not isinstance(hours, (int, float)) or hours < 0:
        return 0.5
    if hours <= 24:
        return 1.0
    if hours <= 72:
        return 0.7
    return 0.4


def availability_multiplier(cand):
    """Return (multiplier in [0.5, 1.0], evidence dict)."""
    sig = cand.get("redrob_signals", {})

    recency_days = _days_since(sig.get("last_active_date"))
    response_rate = sig.get("recruiter_response_rate")
    response_rate = response_rate if isinstance(response_rate, (int, float)) else 0.5
    interview_rate = sig.get("interview_completion_rate")
    interview_rate = interview_rate if isinstance(interview_rate, (int, float)) else 0.5

    components = {
        "recency": (_recency_score(recency_days), 0.30),
        "response_rate": (max(0.0, min(1.0, response_rate)), 0.30),
        "interview_completion": (max(0.0, min(1.0, interview_rate)), 0.15),
        "open_to_work": (1.0 if sig.get("open_to_work_flag") else 0.55, 0.15),
        "response_time": (_response_time_score(sig.get("avg_response_time_hours")), 0.05),
        "verified": (
            (bool(sig.get("verified_email")) + bool(sig.get("verified_phone"))) / 2.0,
            0.05,
        ),
    }
    availability = sum(score * w for score, w in components.values())
    multiplier = 0.5 + 0.5 * availability

    evidence = {
        "last_active_days": recency_days,
        "response_rate": response_rate,
        "interview_completion": interview_rate,
        "open_to_work": bool(sig.get("open_to_work_flag")),
        "availability_multiplier": round(multiplier, 3),
    }
    return multiplier, evidence
