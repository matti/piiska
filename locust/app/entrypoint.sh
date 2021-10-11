#!/usr/bin/env bash
set -euo pipefail

_term() {
  exit 0
}
trap _term TERM INT

case ${1:-web} in
  web)
    exec locust -P 8080
  ;;
  hang)
    echo "hang"
    tail -f /dev/null &
    wait $!
  ;;
esac

