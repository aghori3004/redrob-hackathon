"""Gradio sandbox for the Redrob ranker (HuggingFace Spaces / local).

Runs the exact ranking pipeline from rank.py on a small candidate sample so
reviewers can see honeypot filtering, JD-fit scoring, the embedding blend, and
evidence-based reasoning end to end. Upload a candidates .jsonl (one JSON
object per line) or click "Run bundled sample".

    pip install -r requirements-app.txt
    python scripts/fetch_model.py     # once, to enable the embedding blend
    python app.py
"""

import json
import sys
import tempfile
from pathlib import Path

import gradio as gr

sys.path.insert(0, str(Path(__file__).parent))

from src.loader import iter_candidates
from src.filters import honeypot_flags, passes_relevance_gate
from src.scoring import score_candidate, _career_text
from src.reasoning import reasoning_for
from src import embedding

SAMPLE = Path(__file__).parent / "eval" / "sample_candidates.jsonl"
TOP_N = 100


def rank_file(path, top_n=TOP_N):
    """Run the full pipeline on a JSONL path; return (rows, status)."""
    total = honeypots = gated = 0
    scored = []
    for cand in iter_candidates(path):
        total += 1
        if honeypot_flags(cand):
            honeypots += 1
            continue
        if not passes_relevance_gate(cand):
            gated += 1
            continue
        score, ev = score_candidate(cand)
        scored.append([score, cand["candidate_id"], cand, ev])

    scored.sort(key=lambda x: (-x[0], x[1]))
    mode = "rules-only"
    if embedding.is_available() and scored:
        k = min(embedding.EMBED_TOPK, len(scored))
        feats = embedding.embed_features(_career_text(r[2]) for r in scored[:k])
        for i, f in enumerate(feats):
            scored[i][3]["embed_feature"] = round(f, 4)
            scored[i][0] = embedding.blend(scored[i][0], f)
        scored.sort(key=lambda x: (-x[0], x[1]))
        mode = "rules + embedding blend"

    top = scored[:top_n]
    rows = [
        [rank, cid, round(score, 6), reasoning_for(cand, ev, rank)]
        for rank, (score, cid, cand, ev) in enumerate(top, start=1)
    ]
    status = (
        f"Pool: {total}  |  honeypots filtered: {honeypots}  |  gated out: {gated}  "
        f"|  scored: {len(scored)}  |  scoring mode: {mode}"
    )
    return rows, status


def _write_csv(rows):
    import csv
    f = tempfile.NamedTemporaryFile("w", delete=False, suffix=".csv", newline="", encoding="utf-8")
    w = csv.writer(f)
    w.writerow(["candidate_id", "rank", "score", "reasoning"])
    for rank, cid, score, reason in rows:
        w.writerow([cid, rank, f"{score:.6f}", reason])
    f.close()
    return f.name


def run_upload(file):
    if file is None:
        return [], "Upload a candidates .jsonl or click 'Run bundled sample'.", None
    rows, status = rank_file(file.name)
    return rows, status, _write_csv(rows)


def run_sample():
    if not SAMPLE.exists():
        return [], f"Bundled sample not found at {SAMPLE}", None
    rows, status = rank_file(str(SAMPLE))
    return rows, status, _write_csv(rows)


with gr.Blocks(title="Redrob Ranker") as demo:
    gr.Markdown(
        "# Redrob Ranker — sandbox\n"
        "Ranks candidates against the **Senior AI Engineer — Founding Team** JD: "
        "honeypot filtering → JD-fit scoring → embedding blend → evidence-based "
        "reasoning. Upload a `candidates.jsonl` (one JSON object per line) or run "
        "the bundled sample."
    )
    with gr.Row():
        up = gr.File(label="candidates.jsonl", file_types=[".jsonl", ".json", ".txt"])
        with gr.Column():
            run_btn = gr.Button("Rank uploaded file", variant="primary")
            sample_btn = gr.Button("Run bundled sample")
    status = gr.Textbox(label="Run summary", interactive=False)
    table = gr.Dataframe(
        headers=["rank", "candidate_id", "score", "reasoning"],
        wrap=True, label="Top candidates",
    )
    download = gr.File(label="Download submission CSV")

    run_btn.click(run_upload, inputs=up, outputs=[table, status, download])
    sample_btn.click(run_sample, inputs=None, outputs=[table, status, download])


if __name__ == "__main__":
    demo.launch()
