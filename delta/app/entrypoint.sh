#!/usr/bin/env sh
set -eu

_term() {
  >&2 echo "TERM"
  exit 0
}
trap "_term" TERM

_err() {
  >&2 echo "err: $*"
  exit 1
}

echo "waiting for deltas..."
while true; do
  set +e
    delta=$(redis-cli -h redis --raw get delta)
  set -e
  if [ "$delta" != "" ]; then
    echo $delta
  fi

  sleep 1
done
