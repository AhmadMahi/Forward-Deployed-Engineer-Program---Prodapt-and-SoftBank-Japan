#!/usr/bin/env bash
# Run the tests of every SmartDesk step in offline mode (no API key, no calls to an LLM).
# Python steps: pytest. JavaScript steps: node --test (Node 22, no npm install needed).
# Usage: bash shared/SmartDesk/run_all_tests.sh [stepNN-... ...]
set -u
cd "$(dirname "$0")"
export OFFLINE=1
unset OPENAI_API_KEY
log=$(mktemp)
pass=0; fail=0; failed=()
steps=("$@"); [ ${#steps[@]} -eq 0 ] && steps=(step*/)
for d in "${steps[@]}"; do
  d=${d%/}
  ran=0
  if compgen -G "$d/test_*.py" >/dev/null || [ -d "$d/tests" ]; then
    ran=1
    if (cd "$d" && python3 -m pytest -q -p no:cacheprovider >"$log" 2>&1); then
      echo "PASS  $d (pytest: $(tail -1 "$log"))"; pass=$((pass+1))
    else
      echo "FAIL  $d (pytest)"; tail -15 "$log"; fail=$((fail+1)); failed+=("$d")
    fi
  fi
  if compgen -G "$d/*.test.js" >/dev/null; then
    ran=1
    if (cd "$d" && node --test >"$log" 2>&1); then
      echo "PASS  $d (node: $(grep -E '^# pass' "$log"))"; pass=$((pass+1))
    else
      echo "FAIL  $d (node)"; tail -15 "$log"; fail=$((fail+1)); failed+=("$d")
    fi
  fi
  [ $ran -eq 0 ] && echo "SKIP  $d (no automated tests)"
done
rm -f "$log"
find . -name "__pycache__" -type d -prune -exec rm -rf {} + 2>/dev/null
echo
echo "$pass test suite(s) passed, $fail failed."
[ $fail -eq 0 ] || { printf 'Failed: %s\n' "${failed[@]}"; exit 1; }
