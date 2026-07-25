# Lean probe — report

Leg: `lean-probe` (probe-engineer), molecule `task-20260725-9975`, germ
`germ-20260725-791a7c45`. **Backend: `lean`** — not skipped.

Input: the `lean-skeleton` tree (molecule `task-20260725-5fd9`), which declared
**five** `sorry`s. Job: discharge as many as possible with real proof terms and
let `lake build` be the only judge.

## Headline

**Four of the five `sorry`s are discharged. The fifth is Firoozbakht's
conjecture itself and was not attempted — it is the open problem.**

The development now contains exactly one `sorryAx` dependency, and it is the
declared target.

## Build — the verdict

The LLM emitted proof terms only; the toolchain decided. Reproduce with:

```
$ lake exe cache get          # Mathlib v4.29.0 from the shared cache
$ lake build                  # ← the verdict
$ lake env lean audit.lean              # per-declaration axiom dependencies
$ lake env lean audit_exhaustive.lean   # list-free: every sorryAx in the namespace
```

Observed, verbatim:

```
⚠ [1979/1984] Replayed Firoozbakht.Statement
warning: Firoozbakht/Statement.lean:185:8: declaration uses `sorry`
Build completed successfully (1984 jobs).
```

(The bracketed job index varies with what the build cache replays; the three
lines that matter — one warning, the line it points at, `Build completed
successfully` — do not.)

| gate | result |
|---|---|
| `lake build` exit code | **0** |
| build warnings | **1** — `Statement.lean:185`, the open target, and nothing else |
| `lake env lean audit.lean` exit code | **0** |
| `lake env lean audit_exhaustive.lean` exit code | **0** |
| declarations scanned by the exhaustive audit | **60** |
| declarations depending on `sorryAx` | **1** — `Firoozbakht.firoozbakht` |
| live `sorry` tokens in `.lean` sources | **1** — `Statement.lean:186`, the tactic block of the `theorem` on line 185 |
| `native_decide` / `axiom` / `@[implemented_by]` / `unsafe` in sources | **none** (grep-clean) |

- Toolchain: `leanprover/lean4:v4.29.0` (`lean-toolchain`).
- Mathlib: tag `v4.29.0`, rev `8a178386ffc0f5fef0b77738bb5449d50efeea95`
  (`lake-manifest.json`, unchanged from the skeleton — verified identical).

### The audit was made exhaustive, and then tested

`audit.lean` prints `#print axioms` for a **hand-maintained list**. That is a
hazard dressed as a check: a `sorry` in a declaration nobody remembered to add to
the list is invisible. `audit_exhaustive.lean` (new) removes the list — it walks
the environment, keeps every non-internal declaration under `Firoozbakht`, and
reports the ones depending on `sorryAx`:

```
declarations scanned: 60
depending on sorryAx: [Firoozbakht.firoozbakht]
```

And the detector was checked against a planted failure, because an audit that
cannot fail is worth nothing. Adding one `theorem planted_sorry_selftest : (1:Nat) = 1 := by sorry`
to the `Firoozbakht` namespace and re-running gives:

```
declarations scanned: 61
depending on sorryAx: [Firoozbakht.firoozbakht, Firoozbakht.planted_sorry_selftest]
```

The planted declaration was then deleted; it is not in the tree. This is the same
discipline the skeleton's own verification pass applied to its fidelity checks
(finding 1: a `simp` that closed both `F3 1 ↔ 3 < 4` *and*
`F3 1 ↔ 999999 < 1000000`).


## Per-theorem verdict

| # | Declaration | Skeleton | Verdict | Evidence |
|---|---|---|---|---|
| 1 | `firoozbakht : Conjecture` | `sorry` | **UNPROVABLE_IN_BUDGET** | Open problem since 1982. Not attempted. See the note below — this is *not* a claim that it is false. |
| 2 | `F3_iff_F2` | `sorry` | **PROVED** | build exit 0; audit shows `[propext, Classical.choice, Quot.sound]` |
| 3 | `F1_iff_F3` | `sorry` | **PROVED** | idem |
| 4 | `F2_iff_F1'` | `sorry` | **PROVED** | idem |
| 5 | `F1'_iff_F4` | `sorry` | **PROVED** | idem |

Downstream declarations that merely *inherited* `sorryAx` from 2–5 are therefore
now clean as well, without being touched: `F1_iff_F2`, `F1_iff_F1'`, `F1_iff_F4`,
`F3_iff_F4`, `conjecture_iff_real`, `conjecture_iff_gap`. That is six additional
declarations promoted from "contaminated" to `[propext, Classical.choice,
Quot.sound]`, and it is the substantive gain of this leg: **the statement
`Conjecture ↔ ConjectureReal ↔ (∀ n ≥ 1, g_n < T_n)` is now machine-checked**, so
the run's central move — *Firoozbakht is a prime-gap bound, therefore the
analytic gap literature is admissible* — no longer rests on a paper argument.

### Verdict 1, stated carefully

`UNPROVABLE_IN_BUDGET` here means **no proof was found**, and in this case none
was sought: Firoozbakht's conjecture is open, and the skeleton's own instruction
is that `firoozbakht` may never be discharged by anything but mathematics. This
is not evidence that the conjecture is false. It is `Π₁`; refuting it needs one
certified counterexample index, and the shape such a witness must take is
`refuted_of_witness`, which *is* proven (no `sorry`).

## How the four were proven

One idea, applied four times. Each form of the conjecture is an inequality
between two **positive** quantities, and `Real.log` is a strictly monotone
bijection on the positives (`Real.log_lt_log_iff`). So every step is: cast into
ℝ, take logarithms, push the log through the exponent (`Real.log_pow` for
ℕ-powers, `Real.log_rpow` for `rpow`), then clear the denominators `1/n` and
`1/(n+1)` — legal exactly because `n ≥ 1`.

| step | mechanism |
|---|---|
| `F3 ↔ F2` | `Nat.cast_lt` → `log_lt_log_iff (pow_pos …)` → `log_pow` twice → `linarith` |
| `F1 ↔ F3` | reduce to `F1 ↔ F2` via step 1, then `log_rpow` twice → `div_lt_div_iff₀` (needs `n > 0` and `n+1 > 0`) → `linarith` |
| `F2 ↔ F1'` | `log_rpow`, rewrite `(1 + 1/n)·log p_n` as `((n+1)·log p_n)/n` by `field_simp`, then `lt_div_iff₀ (n > 0)` |
| `F1' ↔ F4` | one `rw`: `cast_g` turns `(g n : ℝ)` into `p_{n+1} - p_n`, then `sub_lt_sub_iff_right` cancels the shared `- p_n`. No `rpow` lemma at all — `p_n^(1+1/n)` is carried through opaquely. |

Two positivity helpers were added, `p_pos_real` and `n_pos_real`, both proven
from the skeleton's `two_le_p`. `positivity` cannot be used on `(p n : ℝ)`
directly — it sees only a ℕ-cast, so it yields `0 ≤`, not `0 <`. That claim was
checked rather than assumed; Lean's exact words on
`example (n : ℕ) : (0:ℝ) < (p n : ℝ) := by positivity` are *"failed to prove
strict positivity, but it would be possible to prove nonnegativity if desired"*.
Hence the strict bound is routed through `two_le_p` by hand.

The high-risk node the skeleton flagged (`F1' ↔ F4`, card `T4` node N5 — the one
that re-imports `rpow` *and* ℕ-subtraction) turned out to be the **cheapest** of
the four, precisely because the skeleton had already isolated its one hazardous
step into `cast_g`. The risk assessment was right about *where* the danger was
and wrong about *how much* was left after the isolation.

## The equivalences are not vacuous — and this was checked

`A ↔ B` is provable whenever `A` and `B` are both false. So four green `Iff`s are
not, by themselves, evidence that the chain *carries* anything. Three new
theorems in `FiniteCheck.lean` close that hole by pushing content through it:

- `F1_le_four`, `F1'_le_four`, `F4_le_four` — the real-analytic, Kourbatov and
  gap forms at `1 ≤ n ≤ 4`, obtained **only** by transferring
  `firoozbakht_le_four` (a ℕ-power statement `norm_num`-proven on four numerals)
  through the chain. No new arithmetic.

The input is true, so the outputs are true statements about `Real.rpow` and about
`g n` — objects the ℕ form never mentions. All three are `sorry`-free in the audit.

That still leaves one gap, and it is the one the skeleton's own verification pass
got caught by: a true-but-uninformative inequality hides a wrong definition.
`F4_le_four` is only as meaningful as `g` and `T` are. So both are pinned to
numerals, in the tree, by rewriting only:

- `g_one : g 1 = 1` — i.e. `p_2 - p_1 = 3 - 2`.
- `T_one : T 1 = (2:ℝ) ^ (2:ℝ) - 2` — the exponent is a **real** exponent, which
  is the point of writing it `(2:ℝ)`.

So `F4 1` is `1 < 2^2 - 2`, i.e. `1 < 2`. A wrong `g` or a wrong `T` now fails to
compile instead of passing quietly.

## Changed files

| File | Change |
|---|---|
| `lean/Firoozbakht/Equivalence.lean` | four `sorry`s → proof terms; two positivity helpers; `cast_g` moved above its first use |
| `lean/Firoozbakht/FiniteCheck.lean` | imports `Equivalence`; three non-vacuity transfer theorems; `g_one` / `T_one` pinning the gap form to numerals |
| `lean/Firoozbakht/Statement.lean` | **docstring only** — the header claimed *every* target theorem is `sorry`-ed, which is no longer true. No definition was touched. |
| `lean/audit.lean` | audits every declaration the leg touched, plus the transfers |
| `lean/audit_exhaustive.lean` | **new** — list-free audit: enumerates the namespace, reports every `sorryAx` dependency |
| `lean/STATUS.md` | updated to the post-probe state |

### The fidelity anchor is unchanged — and this was verified mechanically

This matters more than the four proofs. Had the probe "closed" a `sorry` by
quietly weakening the statement it was attached to, `lake build` would still be
green and the leg would be a fabrication. So every declaration *signature* was
diffed against the skeleton tree
(`…/spore-runs/germ-20260725-791a7c45/lean-skeleton/lean`):

```
$ diff <(grep -E '^(noncomputable )?(@\[simp\] )?(theorem|def|lemma|example)' SKEL/Statement.lean) \
       <(grep -E '^(noncomputable )?(@\[simp\] )?(theorem|def|lemma|example)' Statement.lean)
   → no output (exit 0)
$ diff SKEL/lean-toolchain lean-toolchain            → identical
$ diff SKEL/lake-manifest.json lake-manifest.json    → identical
```

`Statement.lean` — the anchor — has **zero** signature changes: `p`, `g`, `L`,
`T`, `F1`, `F1'`, `F2`, `F3`, `F4`, `Conjecture`, `ConjectureReal`, `Refuted`,
`p_pow_ne`, `strict_iff_nonstrict`, `refuted_of_witness` all identical. Only a
prose block in the module docstring changed.

`Equivalence.lean` and `FiniteCheck.lean` differ only by **additions**, a
**reordering** (`cast_g` moved above `F1'_iff_F4`, which now uses it), and one
binder rename, stated plainly because it *is* a signature change: `F3_iff_F2`'s
hypothesis `(hn : 1 ≤ n)` became `(_hn : 1 ≤ n)`. The proposition is identical;
the underscore records that the proof never uses it, which was verified by
re-running the same script with no hypothesis (see the verification pass, item 2)
— `F3 ↔ F2` holds at every `n`, `n = 0` included. Nothing calls it by named
argument.

## What this leg did *not* do

- **Did not attempt `firoozbakht`.** By instruction, and because it is open.
- **Did not extend the verified range past `n ≤ 4`.** Still card `T4` Fact 1:
  `Nat.nth` is `noncomputable` with no kernel reduction, and Mathlib's
  prime-specific `nth` API is exactly five `@[simp]` base lemmas
  (`nth Prime 0 = 2` … `nth Prime 4 = 11`). Extending needs
  `Nat.count`↔`Nat.nth` bridging machinery — a separate budgeted leg. Reporting
  a larger `N` without it would be a fabrication.
- **Did not formalize node N4** (the smooth model, card `L14`) or **node N6**
  (the `limsup` corollary, card `L3`). N6 needs effective `π(x)` bounds that are
  not assumed present in Mathlib (card `T4` hazard 4).
- **Did not touch the refutation branch.** `Refuted` stays a `def` plus the
  proven `refuted_of_witness`; two contradictory `sorry`-ed theorems in one
  namespace would let any later file prove anything.

## Verification pass (step 2) — what it checked and changed

The artifact was re-audited against its own brief. Four claims in the first draft
were load-bearing and unverified; each was turned into a test.

**1. "`positivity` cannot get a strict bound on a ℕ-cast."** Asserted from
memory. **Checked** — `example (n : ℕ) : (0:ℝ) < (p n : ℝ) := by positivity`
fails with *"failed to prove strict positivity, but it would be possible to prove
nonnegativity if desired"*. Claim stands, now with Lean's own words behind it.

**2. "`F3_iff_F2` does not need `1 ≤ n`."** Asserted from reading the proof —
which is exactly the kind of reading that is wrong. **Checked** by re-running the
identical tactic script on `theorem (n : ℕ) : F3 n ↔ F2 n` with no hypothesis at
all: compiles. So the `_hn` underscore in the signature is accurate, not a
guess.

**3. "The transfers are real terms."** An `Iff` chain can be green and the
transferred instances can still fail to elaborate. **Checked** — `F1 1`, `F1' 1`,
`F4 1` and `F4 4` were each exhibited as closed terms built only from
`F*_le_four`.

**4. The gap form was un-pinned.** `F4_le_four` was reported as evidence that the
chain carries content, but nothing tied `g` or `T` to a number, and the skeleton's
own step-2 pass had already been burned once by exactly this (a `simp` that closed
`F3 1 ↔ 3 < 4` *and* `F3 1 ↔ 999999 < 1000000`). **Fixed** — `g_one` and `T_one`
are now in `FiniteCheck.lean`, so `F4 1` is visibly `1 < 2^2 - 2`.

Two smaller corrections, stated because they were in the first draft:

- `one_lt_p_real` was added and never used. **Removed** rather than left as dead
  code with a note. Two positivity helpers remain and both are used.
- The exhaustive-audit count was reported as 59, taken from a run made before
  `g_one`/`T_one` existed. It is **60**. The table above is the corrected figure,
  and the numbers in this report were re-read against a final run rather than
  carried forward.

### Gaps left open, named

- **The four equivalence proofs are believed correct because the kernel accepted
  them; they were not independently re-derived on paper in this leg.** The paper
  proof lives in card `L1` and was corroborated at two L0 locators by an earlier
  leg. The kernel check and the paper proof are two independent witnesses; neither
  was produced by the other.
- **No claim is made about `n > 4`.** See the non-deliveries below.
- **The `sorry` count went 5 → 1, not 5 → 0, and cannot go to 0.** That is the
  honest state of an open problem.

## Honest reading of the gain

Four `sorry`s went away and none of them was hard — they were `Real.log` API
work, correctly budgeted by the skeleton as such. Nothing here bears on whether
Firoozbakht's conjecture is true. What changed is that a load-bearing *reduction*
used by the rest of the run is now kernel-checked rather than asserted, and the
axiom audit now has a single `sorryAx` whose presence is the honest statement of
the run's position: the conjecture is open.
