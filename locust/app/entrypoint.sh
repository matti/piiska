#!/usr/bin/env bash
set -euo pipefail

exec locust -f "piiska.py" -P 8080
