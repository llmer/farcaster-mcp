FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:${PATH}"

ENV MNEMONIC=""
ENV TRANSPORT="sse"

COPY . .

RUN uv venv --clear
RUN uv pip install --force-reinstall -e .

EXPOSE 8080
CMD ["uv", "run", "farcaster_mcp.py"]
