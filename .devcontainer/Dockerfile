FROM python:3.11.3-slim-bullseye

RUN apt update \
    && apt install -y --no-install-recommends \
    apt-utils \
    gcc \
    build-essential \
    && pip install --no-cache-dir \
    autopep8 \
    flake8 \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*
