FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

ENV MNEMONIC=""

COPY . .

RUN uv venv
RUN uv pip install -e .

EXPOSE 8080
CMD ["uv", "run", "farcaster.py"]