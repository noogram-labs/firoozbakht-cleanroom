# Re-attack delivery — reattack-20260726-57d1 (round 2)

**Supersedes** the prior delivery here (`reattack-20260725-4db5`, `rounds=1`, early-exit — no
`attack-round-K/` was ever nucleated). This molecule is the re-germination that earlier run
recommended: `rounds=2`, and this loop actually ran a round 2.

- **`rounds.md`** — the full round ledger: round 1 (upstream, pinned spore nodes, read not
  re-run) and round 2 (nucleated forward by this loop: 3 proof-attempts, 1 lean-probe, 1
  skeptic).
- **`reattack-verdict.json`** — the fail-closed machine-readable verdict the evidence-gate reads.
  `final_round.artifacts` points into `attack-round-2/` below.
- **`synthesis.md`** — the round-by-round trajectory in prose: what round 2 fixed (both round-1
  BLOCKERs, confirmed by independent re-derivation), what it could not (3 new BLOCKERs — all
  cross-artifact reconciliation seams, none mathematical errors, none touching the conjecture),
  and the named escalation for a hypothetical round 3.
- **`attack-round-2/`** — the final round's own artifacts, copied verbatim from the molecule
  state dir per the formula's delivery spec (v5.2): 3 `proof-attempt-*.md`, `lean-probe-report.md`,
  `unproved.md`, `faults.md`, plus the verification scripts each leg used
  (`skeptic-round2-checks/`, `verify-*-round2.py`, `r2_*.py`).

**Verdict: BLOCKED** (`rounds-exhausted`, `rounds_target=2`, `rounds_run=2`). Kernel
`UNPROVABLE_IN_BUDGET` (one live `sorry` — the conjecture itself, honestly attempted this round
and correctly not discharged). Skeptic carries 3 live BLOCKERs (up from round 1's 2 — a different
species: reconciliation failures across a widened fan-out, not mathematical defects). **The
conjecture remains OPEN.** What changed versus round 1: both round-1 BLOCKERs (F1, F2) are
genuinely fixed as mathematics; what did not change: the loop never reached its fixpoint (kernel
PROVED and skeptic clean in the same round), and the `sorry` count is unchanged at one.
