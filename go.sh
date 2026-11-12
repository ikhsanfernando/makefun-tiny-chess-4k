#!/bin/bash
# Push chess4 clean tree + bundle sesi in-window + audit + submit (+status)
set -u
export PATH=$HOME/.local/bin:$HOME/.hermes/node/bin:$PATH
export LD_LIBRARY_PATH=/tmp/atomic/root/usr/lib/x86_64-linux-gnu:$HOME/lib
export MAKEFUN_API_KEY=$(python3 -c "import json;print(json.load(open('/home/ikhsanwahyuribowo01/.hermes/secrets/makefun_account.json'))['key'])")
PAT=$(python3 -c "import json;print(json.load(open('/home/ikhsanwahyuribowo01/.hermes/secrets/github_pat.json'))['token'])")
S=~/.hermes/skills/operations/makefun-bounties/scripts

cd /tmp/chess4 || exit 1
git remote remove origin 2>/dev/null
git remote add origin "https://${PAT}@github.com/ikhsanfernando/makefun-tiny-chess-4k.git"
git push -q origin HEAD:main --force 2>&1 | tail -1
C=$(git rev-parse HEAD); echo "commit=$C"
echo "tree: $(git ls-files | xargs -r wc -c | tail -1)"

mapfile -t SS < <(grep -l "chess4\|tiny-chess-01" ~/.codex/sessions/2026/11/12/*.jsonl 2>/dev/null)
echo "sesi: ${#SS[@]}"
cd /tmp/chess-kit/tiny-chess-01-kit || exit 1
ARGS=(--repo /tmp/chess4 --no-discover --out /tmp/chess4/tr.tar.gz)
for s in "${SS[@]}"; do ARGS+=(--session "$s"); done
node cli/makefun.mjs bundle "${ARGS[@]}" 2>&1 | grep -E "wrote|refus"
python3 "$S/audit_bundle_lines.py" /tmp/chess4/tr.tar.gz /tmp/chess4/main.py --min 0.3 2>&1 | tail -2

node cli/makefun.mjs submit --competition tiny-chess-01 \
  --repo-url "https://github.com/ikhsanfernando/makefun-tiny-chess-4k" --commit "$C" \
  --title "4087-byte chess engine, perft-clean, alpha-beta search" \
  --bundle /tmp/chess4/tr.tar.gz --keypair /tmp/engine/makefun-keypair.json 2>&1 | tee /tmp/chess4/sub.txt | grep -E "accepted|refused|id\"|claim" | head -4
SID=$(grep -oE '01[0-9a-f]{6}-[0-9a-f-]{20,}' /tmp/chess4/sub.txt | head -1)
if [ -n "$SID" ]; then
  sleep 50
  python3 - "$SID" <<'PY'
import json, os, sys, urllib.request
sid=sys.argv[1]
acc=json.load(open(os.path.expanduser('~/.hermes/secrets/makefun_account.json')))
H={'x-api-key':acc['key'],'Accept':'application/json','User-Agent':'makefun-agent'}
d=json.load(urllib.request.urlopen(urllib.request.Request(f'https://make.fun/api/submissions/{sid}/status',headers=H),timeout=45))
print("stage:", d.get('stage'), "| checks:", len(d['checks']))
for c in d['checks']:
    if c['status']!='pass': print("  FAIL", c['check'], "|", c['reason'][:120])
PY
fi
