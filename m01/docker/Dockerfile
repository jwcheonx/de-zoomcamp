# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim-bookworm

# hadolint ignore=DL3008
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends \
  wget
rm -rf /var/lib/apt/lists/*
EOF

WORKDIR /app

# hadolint ignore=DL3042
RUN --mount=type=cache,target=/root/.cache/pip \
  --mount=type=bind,source=requirements.txt,target=requirements.txt \
  python -m pip install -r requirements.txt

COPY ingest_data.py .

ENTRYPOINT ["python", "ingest_data.py"]
