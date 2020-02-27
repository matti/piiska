#!/usr/bin/env bash
set -euo pipefail

_term() {
  >&2 echo "TERM"
  exit 0
}
trap "_term" TERM

_err() {
  >&2 echo "err: $*"
  exit 1
}

PIISKA_MODE=${PIISKA_MODE:-master}
PIISKA_CLIENT=${PIISKA_CLIENT:-normal}

echo "starting: $PIISKA_MODE with $PIISKA_CLIENT"

case "$PIISKA_MODE" in
  master)
    exec locust -f "$PIISKA_CLIENT.py" --master --step-load -P 8080
  ;;
  slave)
    exec locust -f "$PIISKA_CLIENT.py" --slave --master-host=master
  ;;
esac
