# Reproducible build for the Redrob ranker.
#
# The embedding model is downloaded ONCE at build time (network allowed during
# build). At run time the ranking step loads it from the baked-in ./models/
# cache with the HF hub forced offline — no network calls, per the Stage-3
# constraint.
#
#   docker build -t redrob-ranker .
#   # mount the data and reproduce the submission (CPU, offline):
#   docker run --rm --network none \
#       -v "$PWD/data:/data" -v "$PWD/out:/out" redrob-ranker \
#       python rank.py --candidates /data/candidates.jsonl --out /out/submission.csv

FROM python:3.11-slim

WORKDIR /app

# Install reproduction deps first (better layer caching).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project.
COPY . .

# Bake the embedding model into the image (build-time network only).
RUN REDROB_ALLOW_MODEL_FETCH=1 python scripts/fetch_model.py

# Force the HF hub offline at run time so ranking makes no network calls.
ENV HF_HUB_OFFLINE=1 \
    TRANSFORMERS_OFFLINE=1

# Default: print usage. Override with the reproduce command (see header).
CMD ["python", "rank.py", "--help"]
