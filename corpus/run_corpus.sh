#!/usr/bin/env bash
# Red-team corpus runner.
#
# Four checks, in order of evidential strength:
#
#   1. REFUTED   — ../corpus/refutations/*.lean must COMPILE. Each theorem there
#                  proves `¬ S` for a corpus statement S. Strongest evidence:
#                  not "an attempt failed" but "no attempt can succeed".
#   2. REJECTED  — attempts/*.lean must FAIL to compile (non-zero exit, and at
#                  least one line matching `error`). One file per entry, so a
#                  failure cannot be masked by a neighbour.
#   3. ACCEPTED-BUT-UNSOUND — audit/*.lean must COMPILE (that is the finding),
#                  and the appended `#print axioms` must show a non-standard
#                  axiom or `sorryAx`. These are the entries `lake build` alone
#                  does not catch.
#   5. REJECTED-CANDIDATE — rejected-candidates/*.lean must COMPILE. Proofs
#                  about near-misses that could NOT be entries because their
#                  falsity is itself as open as the conjecture.
#   4. UNDETECTED — undetected/*.lean must COMPILE with a *clean* axiom audit.
#                  These are false-in-spirit claims that no gate in this run
#                  catches; the file itself documents what would catch them.
#
# Usage:  bash corpus/run_corpus.sh          (from the repo root)
# Output: corpus/results.tsv and a summary on stdout. Exit 0 iff every entry
#         behaved as its manifest says it must.

set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LEANDIR="$ROOT/lean"
CORPUS="$ROOT/corpus"
OUT="$CORPUS/results.tsv"
LOGDIR="$CORPUS/.logs"
mkdir -p "$LOGDIR"

printf 'id\tkind\texpected\tobserved\tstatus\tdetail\n' > "$OUT"
fail=0

run_lean() { (cd "$LEANDIR" && lake env lean "$1") > "$2" 2>&1; echo $?; }

record() { printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4" "$5" "$6" >> "$OUT"; }

echo "== 1. refutations (must compile) =="
for f in "$CORPUS"/refutations/*.lean; do
  id="$(basename "$f" .lean)"
  log="$LOGDIR/ref-$id.log"
  rc=$(run_lean "$f" "$log")
  if [ "$rc" = "0" ] && ! grep -q "declaration uses 'sorry'" "$log"; then
    record "$id" refutation compiles compiles PASS "no sorry, no error"
    echo "  PASS $id"
  else
    record "$id" refutation compiles "exit=$rc" FAIL "$(head -1 "$log" | tr '\t' ' ')"
    echo "  FAIL $id (exit $rc)"; fail=1
  fi
done

echo "== 2. attempts (must be rejected) =="
for f in "$CORPUS"/attempts/*.lean; do
  id="$(basename "$f" .lean)"
  log="$LOGDIR/att-$id.log"
  rc=$(run_lean "$f" "$log")
  err="$(grep -m1 -o 'error[^,]*' "$log" | head -1 | tr '\t' ' ')"
  if [ "$rc" != "0" ] && grep -qi 'error' "$log"; then
    record "$id" attempt rejected rejected PASS "${err:-error}"
    echo "  PASS $id — rejected: ${err:-error}"
  else
    record "$id" attempt rejected "ACCEPTED(exit=$rc)" FAIL "checker did not reject"
    echo "  FAIL $id — THE CHECKER ACCEPTED A FALSE CLAIM"; fail=1
  fi
done

echo "== 3. audit-evasion (must compile; audit must flag) =="
for f in "$CORPUS"/audit/*.lean; do
  id="$(basename "$f" .lean)"
  log="$LOGDIR/aud-$id.log"
  rc=$(run_lean "$f" "$log")
  # Re-run with `#print axioms` appended to every theorem in the file.
  tmp="$LOGDIR/$id.axioms.lean"
  cp "$f" "$tmp"
  ns="$(grep -m1 '^namespace ' "$f" | awk '{print $2}')"
  grep -oE '^theorem [A-Za-z_0-9]+' "$f" | awk -v ns="$ns" '{print "#print axioms " ns "." $2}' >> "$tmp"
  alog="$LOGDIR/aud-$id.axioms.log"
  run_lean "$tmp" "$alog" > /dev/null
  if [ "$rc" = "0" ] && grep -qE 'sorryAx|_axiom' "$alog"; then
    flagged="$(grep -oE 'sorryAx|[A-Za-z_.0-9]*_axiom' "$alog" | sort -u | tr '\n' ' ')"
    record "$id" audit-evasion "compiles+flagged" "compiles+flagged" PASS "audit sees: $flagged"
    echo "  PASS $id — build green (exit 0); audit sees: $flagged"
  else
    record "$id" audit-evasion "compiles+flagged" "exit=$rc" FAIL "audit did not flag it"
    echo "  FAIL $id (exit $rc; audit silent)"; fail=1
  fi
done

echo "== 5. rejected candidates (documentation; must compile) =="
for f in "$CORPUS"/rejected-candidates/*.lean; do
  id="$(basename "$f" .lean)"
  log="$LOGDIR/rej-$id.log"
  rc=$(run_lean "$f" "$log")
  if [ "$rc" = "0" ] && ! grep -q "declaration uses 'sorry'" "$log"; then
    record "$id" rejected-candidate compiles compiles PASS "proofs about near-misses that could not be entries"
    echo "  PASS $id"
  else
    record "$id" rejected-candidate compiles "exit=$rc" FAIL "$(head -1 "$log" | tr '\t' ' ')"
    echo "  FAIL $id (exit $rc)"; fail=1
  fi
done

echo "== 4. undetected-by-any-gate (must compile AND have a clean axiom audit) =="
for f in "$CORPUS"/undetected/*.lean; do
  id="$(basename "$f" .lean)"
  log="$LOGDIR/und-$id.log"
  rc=$(run_lean "$f" "$log")
  tmp="$LOGDIR/$id.axioms.lean"
  cp "$f" "$tmp"
  ns="$(grep -m1 '^namespace ' "$f" | awk '{print $2}')"
  grep -oE '^theorem [A-Za-z_0-9]+' "$f" | awk -v ns="$ns" '{print "#print axioms " ns "." $2}' >> "$tmp"
  alog="$LOGDIR/und-$id.axioms.log"
  run_lean "$tmp" "$alog" > /dev/null
  if [ "$rc" = "0" ] && ! grep -qE 'sorryAx|_axiom' "$alog" && ! grep -q "uses 'sorry'" "$log"; then
    record "$id" undetected "compiles+clean-audit" "compiles+clean-audit" PASS "no gate in this run fires; hazard is documented in the file"
    echo "  PASS $id — compiles, audit clean, no gate fires (that IS the finding)"
  else
    record "$id" undetected "compiles+clean-audit" "exit=$rc" FAIL "expected a silent pass"
    echo "  FAIL $id (exit $rc)"; fail=1
  fi
done

echo
if [ "$fail" = "0" ]; then echo "CORPUS GREEN — every entry behaved as specified. See $OUT";
else echo "CORPUS RED — at least one entry misbehaved. See $OUT"; fi
exit "$fail"
