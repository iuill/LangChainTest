#FROM python:3.11.3-slim-bullseye
ARG VARIANT=3.10-bullseye
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

RUN apt update \
    && apt install -y --no-install-recommends \
    apt-utils \
    gcc \
    build-essential \
    locales-all \
    && apt autoremove -y \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ=Asia/Tokyo
