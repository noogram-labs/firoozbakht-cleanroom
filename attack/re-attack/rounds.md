# Re-attack round ledger — reattack-20260725-4db5

## Preflight (Step 1)

- `cs wait --help` — **present** (exit 0, full help printed). Driver-capable check 1/2 PASS.
- `cs run --help` — **advertises `--resident`** (ADR-095 Resident Runtime). Driver-capable check 2/2 PASS.
- Executor verdict: **driver-capable**. No collapse; the loop is not refused.

## Bound check

- `${rounds}` = `1` (from molecule variables, matches formula default). Parses as a positive integer. PASS.
- Sealed `[spore.node.bounds].max_instances` ceiling: the binding `math-attack` spore's `re-attack` node
  (`kind = "emergent"`) declares this ceiling; `cs spore validate` enforces it at germination time
  (defence layer 1). This molecule's germination already occurred (see `cs --json observe
  reattack-20260725-4db5` → `variables.rounds = "1"`), so layer-1 validation already passed for this
  exact value. Layer 2 (this check): `rounds=1` is the floor of the parameter's domain (a positive
  integer), which is `<=` any ceiling `>= 1` the spore could sanely declare — a ceiling of 0 would make
  the parameter itself ungerminatable, so `rounds=1 <= max_instances` holds unconditionally here.
  PASS (defence-in-depth confirmed, not merely assumed).

## EARLY EXIT AT rounds=1

`${rounds}` = 1 → **no re-attack round is nucleated**. Round 1 is the spore's pinned v3.x
informal (`proof-attempt` × subquestions, `notebooks`) + formal (`lean-skeleton`, `lean-probe`,
`red-team-corpus`) branches, already run upstream by the spore germination. This IS the whole
attack for `rounds=1` — it is the exact v3.x graph, unmodified.

Per the formula, this early exit jumps straight to `emit-verdict` (Step 4), folding round 1's own
`skeptic` (upstream `faults.md`) and `lean-probe` (upstream `lean-probe-report.md`) verdicts. Step 2
reads those two files verbatim (never re-run) to populate the row below.

| round | attempt ids | probe id | skeptic id | kernel | skeptic | converged? |
|-------|-------------|----------|------------|--------|---------|------------|
| 1     | proof-attempt×3 (`first-failure-maximality`, `RH-conditional-bound`, `unconditional-verified-range`) + notebooks×3, molecule `task-20250725-488f` lineage (upstream, pinned) | `task-20260725-9975` (lean-probe) | `task-20260725-488f` (skeptic) | **UNPROVABLE_IN_BUDGET** | **blockers** | **NO** |

`rounds_target` = 1. `rounds_run` (this molecule) = 0 (no NEW round nucleated). Row above is
round 1's pre-existing verdict, read not produced.

## Step 2 — round 1 verdicts, read verbatim from upstream (never re-run)

**Source files (both present, both well-formed — no fail-closed trigger):**
- `.cosmon/state/spore-runs/germ-20260725-791a7c45/skeptic/faults.md` (444 lines)
- `.cosmon/state/spore-runs/germ-20260725-791a7c45/lean-probe/lean-probe-report.md` (280 lines)

**kernel[1] = UNPROVABLE_IN_BUDGET** (not PROVED, not DEGRADED — `formal_backend = lean` so the
leg genuinely ran). `lake build` exit 0, grep-clean of `axiom`/`native_decide`/`unsafe`, but the
target theorem `Firoozbakht.firoozbakht` (`Statement.lean:186`) still carries exactly one live
`sorry` — the conjecture itself, correctly never attempted (open problem, not a budget failure).
4 of 5 skeleton `sorry`s were discharged (equivalence-form transfers), 0 of those touch the
conjecture's truth.

**skeptic[1] = blockers** (NOT clean). `faults.md` reports **2 BLOCKER + 4 MAJOR + 8 MINOR**,
non-empty BLOCKER set:
- **F1** (BLOCKER): `m(n)` / "governing record index" carries three inequivalent definitions
  across `notebook-0`, `notebook-2`, card `L15`; two sibling legs publish opposite trends
  ("weakens" vs "does not decay") for what are, under audit, two different quantities sharing one
  name. Repairable, does not touch `F` itself.
- **F2** (BLOCKER): `proof-attempt-0.md` Theorem C(b)'s cited bound (A-high) does not follow from
  its stated justification (`v(1+v/x) ≤ v(1+ℓ⁴/x)` does not follow from `v<ℓ²`); as printed the
  theorem is false by a factor ≈38 over part of its range. The skeptic independently confirms the
  theorem's *conclusion* is nonetheless true under the correct (tight) form of the bound — a
  derivation defect, not a truth defect, but a BLOCKER as printed.
- 4 MAJOR (F3–F6): premature "unconditional"/"retire" framing on an unopened citation (F3);
  false "no other index whatsoever" headline dropping a load-bearing `n≥3` restriction (F4);
  three incompatible fractions for the headline `55.92%` statistic (F5); a self-contradictory
  definition of `p*(C)` in `notebook-1` (F6).
- 8 MINOR (F7–F14): transcription/labelling slips, none load-bearing on `F`.

**converged[1] = NO.** kernel is UNPROVABLE_IN_BUDGET (not PROVED) AND skeptic carries 2 BLOCKERs
(not clean) — neither half of the strict stop condition holds, so convergence fails on both legs
independently. The conjecture `F` itself is explicitly stated OPEN throughout (never assumed,
never refuted) — round 1 is honest, disciplined, structurally-flawed-but-repairable, and NOT a
proof or a disproof.

`unproved-1` = { `Firoozbakht.firoozbakht` (`Conjecture`) — the sole remaining `sorry`,
`Statement.lean:186` }. This is the ONLY still-`sorry`'d theorem; all four reduction lemmas are
discharged.

`faults-1` = { F1 (BLOCKER, vocabulary collision on `m(n)`), F2 (BLOCKER, mis-derived bound in
Theorem C(b)), F3–F6 (MAJOR) }.

## Step 3 — loop body: NOT ENTERED

`${rounds}` = 1, so the `while round < 1` condition is false at round = 1 from the start (the loop
variable initializes at round 1, the target is 1) — the loop body never executes per the
EARLY EXIT AT rounds=1 discipline mandated in Step 1/README. No `attack-round-2/` directory was
created, no molecules were nucleated, no `--decayed-from`/`--blocked-by` edges were drawn. This is
the exact v3.x single-shot graph, confirmed by inspection: round 1 is the totality of the attack.
