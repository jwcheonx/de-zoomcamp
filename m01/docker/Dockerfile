# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim-bookworm

RUN python -m pip install --no-cache-dir polars

WORKDIR /app

COPY foo.py .

ENTRYPOINT ["python", "foo.py"]
