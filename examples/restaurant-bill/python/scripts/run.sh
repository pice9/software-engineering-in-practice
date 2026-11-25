#!usr/bin/env bash
set -eou pipefail
cd "$(dirname "$0")/.."

uv run python main.py