# Synthesis — reattack-20260725-4db5 (converge-math-attack, rounds=1)

## Trajectory

Round 1 is the ONLY round in this run, by construction: `rounds=1` triggers the formula's
EARLY EXIT — the loop never nucleates a round 2, because round 1 (the `math-attack` spore's
pinned v3.x informal + formal branches, run upstream of this molecule) already IS the whole
attack for this target. This molecule's job was purely to read round 1's two verdicts honestly,
check the strict stop condition, and — since it does not hold — emit a fail-closed BLOCKED
verdict rather than a silent pass.

**Round 1, what it fixed / what it could not:**

- **Formal (kernel) leg**: `lean-probe` discharged 4 of the skeleton's 5 `sorry`s (all four
  equivalence-form reductions `F1↔F2↔F3↔F4`), promoting 6 further downstream declarations from
  "contaminated" to clean, and mechanically re-verified the fidelity anchor (`Statement.lean`
  signatures unchanged, diffed against the skeleton). It correctly did **not** attempt the fifth
  `sorry` — `Firoozbakht.firoozbakht` itself — because that IS the open conjecture. Kernel verdict:
  **UNPROVABLE_IN_BUDGET**, honestly distinguished from "false" or "disproved". This is not
  progress toward a *specific* proof strategy; it is infrastructure (the reduction chain is now
  machine-checked rather than asserted) that any future round would inherit for free.

- **Informal (skeptic) leg**: found the corpus structurally disciplined — no assumed conclusions,
  no circular reasoning, no scale-limited computation dressed as a theorem (18 items independently
  re-derived and confirmed clean, §5 of `faults.md`). But it surfaced **2 BLOCKERs**: a three-way
  vocabulary collision on `m(n)` across two notebooks and a concept card (F1), and a genuinely
  mis-derived bound in `proof-attempt-0.md` Theorem C(b) whose *conclusion* the skeptic
  independently reconfirms true under the corrected form (F2). Both are named as repairable and
  neither is a mathematical error about the conjecture `F` itself — but per the strict
  fail-closed discipline, "repairable" is not "clean", and the BLOCKER set is non-empty.

**Did the unproved list shrink or churn?** It shrank sharply on the formal side — 5 sorries down
to 1, with the sole survivor being the conjecture itself, which by definition cannot shrink
further within this run. There is no round-over-round comparison possible for `rounds=1`: this is
the first and only measurement, not a trend.

## Verdict

**BLOCKED**, `exit_reason = rounds-exhausted` (trivially, since `rounds_target = 1` and
`rounds_run = 0` — the cap was never available to spend). This is the honest fixpoint check
applied once: kernel is UNPROVABLE_IN_BUDGET (not PROVED) and skeptic carries 2 live BLOCKERs (not
clean), so the strict stop condition fails on both legs independently — never a silent pass.

**The conjecture `p_{n+1}^{1/(n+1)} < p_n^{1/n}` (Firoozbakht's conjecture) remains OPEN.**
Nothing in round 1 — kernel or skeptic — proves or refutes it. The run is disciplined (every
artifact states `F` open and none uses it as a hypothesis, per `faults.md` §5 items 17–18) but
incomplete: two BLOCKER-level defects in the informal corpus and one irreducible `sorry` in the
formal development.

## Escalation (named, per the fail-closed discipline)

1. **F1 (BLOCKER)** — `m(n)`/"governing record index" means three different things across
   `notebook-0`, `notebook-2`, and card `L15`. Repair: name the three predicates explicitly
   (P6′-pair, P6′-gov, P6′-min) and state which measurement used which.
2. **F2 (BLOCKER)** — `proof-attempt-0.md` Theorem C(b)'s cited bound (A-high) does not follow
   from its stated justification (off by a factor ≈ℓ²); the theorem's conclusion is true under the
   corrected (tight) bound but the printed derivation is not. Repair: restate (A-high) as
   `v(1+v/x)` with `v := ℓ²-ℓ-1-1/ℓ`, replace `ℓ⁴/p_m` by `v²/p_m` in §6.2's criterion.
3. **`Firoozbakht.firoozbakht : Conjecture`** (`Statement.lean:186`) remains `sorry` — the
   conjecture itself, open since 1982, correctly never attempted by this run.

To make further progress, re-germinate with `rounds >= 2` (subject to the sealed `max_instances`
ceiling) so a re-attack round can apply the two named repairs before the skeptic re-runs. That
round is OUT OF SCOPE for this molecule (`rounds=1` by explicit configuration) and is not
nucleated here.
