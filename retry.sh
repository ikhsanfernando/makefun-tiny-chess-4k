#!/bin/bash
set -u
cd /tmp/chess-kit/tiny-chess-01-kit || exit 1
export PATH=$HOME/.local/bin:$HOME/.hermes/node/bin:$PATH
export LD_LIBRARY_PATH=/tmp/atomic/root/usr/lib/x86_64-linux-gnu:$HOME/lib
export MAKEFUN_API_KEY=$(python3 -c "import json;print(json.load(open('/home/ikhsanwahyuribowo01/.hermes/secrets/makefun_account.json'))['key'])")
for i in $(seq 1 60); do
  out=$(node cli/makefun.mjs submit --competition tiny-chess-01 \
    --repo-url "https://github.com/ikhsanfernando/makefun-tiny-chess-4k" \
    --commit e3a71b9dcfd1fdb9417f53faac5144221dfd9f44 \
    --title "4087-byte chess engine, perft-clean, alpha-beta search" \
    --bundle /tmp/chess4/tr.tar.gz 2>&1)
  if echo "$out" | grep -q accepted; then
    echo "$out" | grep -E "accepted|claim"
    SID=$(echo "$out" | grep -oE '01[0-9a-f]{6}-[0-9a-f-]{20,}' | head -1)
    sleep 45
    node cli/makefun.mjs status --submission "$SID" 2>&1 | grep -E "pass  |fail  |stage" | head -30
    exit 0
  fi
  echo "attempt $i: $(echo "$out" | tail -1 | cut -c1-90)"
  sleep 600
done
