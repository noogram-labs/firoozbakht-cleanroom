# Re-attack delivery — reattack-20260725-4db5

`rounds=1` → no `attack-round-K/` directory was ever created (the EARLY EXIT AT rounds=1
discipline: round 1, already present at `attack/` in this worktree — `faults.md`,
`lean-probe-report.md`, `proof-attempt-{0,1,2}.md`, `notebook-{0,1,2}/` — IS the whole attack).
There is no separate "final round" artifact set to copy; round 1's own files, already tracked at
`attack/`, are the ones `reattack-verdict.json.final_round.artifacts` points at.

This directory carries only the loop's own bookkeeping:

- `rounds.md` — the round ledger (one row: round 1, read not produced).
- `reattack-verdict.json` — the fail-closed machine-readable verdict the evidence-gate reads.
- `synthesis.md` — round-by-round trajectory in prose, and the named escalation.

Verdict: **BLOCKED** (`rounds-exhausted`, trivially — `rounds_target=1`, `rounds_run=0`). Kernel
UNPROVABLE_IN_BUDGET, skeptic carries 2 live BLOCKERs. The conjecture remains OPEN.
