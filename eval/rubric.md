# Labeling Rubric — Relevance Tiers 0–5

Derived **only** from `job_description.docx` (including its hackathon section), written
before reading any model rankings, so labels stay independent of the scorer's logic.
"Relevant" for P@10 purposes = tier 3+, matching the contest's stated semantics.

## How to label a profile

Read the raw profile top to bottom: summary, career history (titles, companies,
industries, descriptions, dates), education, behavioral signals. **Ignore the skills
array entirely for relevance** (it is uniform random noise in this dataset); it counts
only as honeypot evidence (expert proficiency with near-zero duration).

Assign the base tier first, then apply caps/demotions.

## Base tiers

**Tier 5 — Ideal.** Production ranking / retrieval / recommendation / search / NLP
systems evidenced in career descriptions (not just titles), predominantly at product
companies, ~5–9 yrs (ideally 6–8), India Tier-1 (or clearly relocating), behaviorally
reachable. No disqualifiers, no significant concerns. The JD expects only a handful
of these to exist.

**Tier 4 — Strong.** Meets the must-haves (production ML/IR evidence at product
companies) with one or two minor concerns: notice period 60–90d, slightly outside the
experience band, non-Tier-1 India city, moderate activity staleness, or a softer
evidence trail (e.g., clear ML production work but ranking/retrieval specifically is
thin).

**Tier 3 — Relevant.** Real production ML/IR connection but a significant gap:
strong adjacent profile transitioning into ML with concrete production-ML exposure
(the "plain-language Tier 5" archetype reads higher — judge the evidence, not the
title); ML engineer whose career is services-heavy but has product stints; CV/speech
specialist WITH genuine NLP/IR work.

**Tier 2 — Adjacent.** Competent technical profile without production ML/IR evidence:
backend/data/analytics engineers whose descriptions show pipelines and infra but no
ranking/retrieval/ML modeling; self-described ML hobbyists (Kaggle, side projects)
on a solid engineering career.

**Tier 1 — Weak.** Wrong-specialty tech with no ML/IR evidence (pure Java/.NET/QA/
mobile/frontend careers); or profiles whose only "AI" is keywords with no career
corroboration.

**Tier 0 — Irrelevant / honeypot.** Non-tech careers (HR, sales, accounting,
marketing, mechanical/civil) regardless of listed skills; internally impossible
profiles (honeypots).

## Hard caps (JD: "we will not move forward")

- Research-only career, no production deployment ever → cap at tier 1.
- Outside India and not willing to relocate → cap at tier 1 (no visa sponsorship).
- AI experience that is only recent LLM-wrapper work (LangChain/OpenAI calls) with
  no pre-LLM production ML → cap at tier 2.
- No hands-on code in the last ~18 months (pure architect/manager recent roles with
  no built/shipped evidence) → cap at tier 2.

## Demotions (JD: "probably not" / "do NOT want") — drop 1–2 tiers

- Entire career at consulting/IT-services firms (a current services job with prior
  product experience is explicitly fine).
- Title-chaser pattern: 3+ jobs with median stint < ~18 months.
- CV/speech/robotics specialty without NLP/IR exposure.
- 5+ closed-source years with no external validation signal (no GitHub, no
  open-source/talks evidence anywhere in the profile) — mild, −1 at most.

## Behavioral cap (JD hackathon section: "down-weight them appropriately")

- Effectively unreachable — last active 6+ months ago AND recruiter response rate
  ≤ ~0.10 → cap at tier 2 regardless of paper strength.
- Moderately stale/unresponsive → −1 tier from base.

## Tie-style guidance

When torn between two tiers, ask: "would the hiring manager who wrote this JD spend
an interview slot on this person?" Clearly yes → at least tier 3. Only if nothing
better exists → tier 2. No → tier 0–1.
