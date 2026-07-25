# Lean skeleton — status

Leg: `lean-skeleton` (kernel-engineer), molecule `task-20260725-5fd9`,
germ `germ-20260725-791a7c45`. Backend: **lean** (not skipped).

## Build

```
$ lake build
Build completed successfully (1984 jobs).
```

- Toolchain: `leanprover/lean4:v4.29.0` (pinned in `lean-toolchain`).
- Mathlib: `leanprover-community/mathlib4` tag `v4.29.0`,
  rev `8a178386ffc0f5fef0b77738bb5449d50efeea95` (pinned in `lake-manifest.json`).
- The build is **green with warnings only** — the warnings are the five declared
  `sorry`s listed below and nothing else.

This closes card `T4` hazard 1, which flagged that the run's Lean facts were
documentation snapshots rather than a pinned-toolchain check. They are now a
pinned-toolchain check: `Nat.nth`, `Nat.nth_lt_nth`, `Nat.nth_mem_of_infinite`,
`Nat.infinite_setOf_prime` and the five `nth_prime_*` base lemmas all resolved
against the toolchain above.

## Axiom audit

`lake env lean audit.lean` prints the dependency of each declaration. Reproduced
verbatim:

| Declaration | `sorryAx`? |
|---|---|
| `p_one`, `p_five`, `p_succ` | no |
| `prime_p`, `p_lt_p_succ` | no |
| `refuted_of_witness` | no |
| `cast_g` | no |
| `p_pow_ne`, `strict_iff_nonstrict` | no |
| `F3_one`, `F3_four`, `firoozbakht_le_four` | no |
| `firoozbakht` | **yes** — the open target |
| `F3_iff_F2`, `F1_iff_F3`, `F2_iff_F1'`, `F1'_iff_F4` | **yes** — L1 steps, skeleton |
| `conjecture_iff_real`, `conjecture_iff_gap` | **yes** — inherited from the four above |

Everything else is `[propext, Classical.choice, Quot.sound]` only.

## The five `sorry`s, and why each is there

| # | Declaration | File:line | Status |
|---|---|---|---|
| 1 | `firoozbakht : Conjecture` | `Statement.lean:182` | **Open problem.** This is the point. Never to be discharged by anything but mathematics. |
| 2 | `F3_iff_F2` | `Equivalence.lean:28` | Card `L1`, PROVEN on paper; Lean proof is `Real.log` API work, budgeted to the proof leg (card `T4`, node N2). |
| 3 | `F1_iff_F3` | `Equivalence.lean:33` | idem, `Real.rpow` monotonicity. |
| 4 | `F2_iff_F1'` | `Equivalence.lean:37` | idem. |
| 5 | `F1'_iff_F4` | `Equivalence.lean:47` | idem — and card `T4` names this the **highest-risk node** (N5): it re-imports `rpow` and ℕ-subtraction into a statement the anchor keeps in ℕ. Its one ℕ-subtraction step, `cast_g`, is proven. |

Sorries 2–5 correspond to a card (`L1`) whose paper proof is complete and
corroborated at two L0 locators. They are *unformalized*, not *unproven*. Sorry 1
is genuinely unproven by anybody.

## What is actually proven here (no `sorry`)

- `p 1 = 2` … `p 5 = 11` — the 1-indexed sequence agrees with the paper convention.
- `prime_p : ∀ n, Nat.Prime (p n)`.
- `p_lt_p_succ : 1 ≤ n → p n < p (n+1)`.
- `p_succ : p (k+1) = Nat.nth Nat.Prime k` — the 0↔1 index bridge, in one place.
- `p_pow_ne` / `strict_iff_nonstrict` — Visser's `≤` form and Kourbatov's `<`
  form define the same conjecture, at every `n ≥ 1` (card `D4` hazard 1, which
  the cards asserted from unique factorisation; now machine-checked, via
  `p_{n+1} ∣ p_n^{n+1} → p_{n+1} = p_n`).
- `cast_g : 1 ≤ n → (g n : ℝ) = p (n+1) - p n` — truncated subtraction is genuine.
- `refuted_of_witness` — the `Σ₁` refutation shape (card `L16`).
- `firoozbakht_le_four` — the conjecture holds for `1 ≤ n ≤ 4`.

## Deliberate non-deliveries, stated plainly

**Verified range is `n ≤ 4`, not `n ≤ 10⁴`.** Card `T4` Fact 1: `Nat.nth` is
`noncomputable` and has *no* kernel reduction, so `decide` cannot produce `p n`;
card `T4` Fact 2: Mathlib's prime-specific `nth` API is exactly five `@[simp]`
base lemmas, `nth Prime 0 = 2` through `nth Prime 4 = 11`. Four is therefore the
entire reach of this project without new machinery (`Nat.count`↔`Nat.nth`
bridging, cost linear in `p_N`). The limit is not integer size — `p_51^52` has
124 digits. Extending the range is a separate, budgeted leg; claiming a larger
`N` here would be a fabrication.

**Node N4 (the smooth model, card `L14`) is not formalized.** Out of scope for a
statement leg, and the panel demoted it from primary (card `T4`, node table).

**Node N6 (the `limsup` corollary, card `L3`) is not formalized.** It needs
effective `π(x)` bounds (card `T1`) which are not assumed present in Mathlib
(card `T4` hazard 4); it would have to enter as an explicit flagged hypothesis.

**`Nat.bertrand` was neither used nor confirmed.** Card `L17` establishes it is
useless for `F` anyway.

## Verification pass (step 2) — what it found and changed

The artifact was re-audited against its own brief. Four findings, all fixed.

**1. The original fidelity checks were vacuous.** They were written as
`example : F3 1 ↔ (3:ℕ)^1 < 2^2 := by simp [F3]`. `simp` closes that by
evaluating *both sides to `True`* — and it closes
`F3 1 ↔ (999999:ℕ) < 1000000` just as happily (checked). An `Iff` between two
true propositions says nothing about which primes the statement names, so the
central claim of this leg was resting on a check that could not fail.
**Fixed:** the positive checks are now propositional *equalities* discharged by
`simp only [F3, p_one, p_two]` — rewriting only, no `decide`, no `norm_num`. The
goal closes because `p 2` rewrites to `3`; under the 0-indexed reading it would
rewrite to `5` and the goal would not close.

**2. A negative control cannot live at the level of propositions at all.** The
first draft's `¬ (F3 1 = (5^1 < 3^2))` is *false* — `propext` identifies any two
true propositions. Lean says so. **Fixed:** the negative control moved to the
level of natural numbers, where `propext` has no purchase:
`p_ne_nth_same_index : p 1 ≠ Nat.nth Nat.Prime 1` (i.e. `2 ≠ 3`), plus
`nth_eq_p_succ : Nat.nth Nat.Prime k = p (k+1)`, which states the off-by-one as
an identity.

**3. One `sorry` was avoidable and was removed.** `strict_iff_nonstrict` (card
`D4` hazard 1 — Visser's `≤` versus Kourbatov's `<`) was `sorry`-ed on the
grounds of being off the critical path. It is now proven, via
`p_pow_ne : p_{n+1}^n ≠ p_n^{n+1}` (if they were equal then
`p_{n+1} ∣ p_n^{n+1}`, so `p_{n+1} = p_n`, contradicting `p_n < p_{n+1}`).
The sorry count went 6 → 5.

**4. A numeric claim in a docstring was wrong.** `n = 4` was called "the
tightest of the small cases" on the strength of its absolute margin `2166`.
By ratio it is the *loosest* of the four: `16807/14641 = 1.15` against
`27/25 = 1.08` at `n = 2`. **Fixed** — `n = 2` is now named as the tightest in
range, with both ratios stated.

### Independent cross-check (outside Lean)

The transcribed statement was evaluated in Python over the first `25996`
primes, in log form (`n·log p_{n+1} < (n+1)·log p_n`): **zero** violations,
tightest margin `0.0770` nats at `n = 2` (primes `3, 5`) — consistent with the
Lean range and with the literature's picture. The `n = 1..4` cases were also
checked in exact integer arithmetic and agree with the four numerals in
`FiniteCheck.lean`. This is a cross-check of the transcription, **not** evidence
about the conjecture: the conjecture is verified far past `2.6·10⁴` in the
literature, and no finite range bears on a `Π₁` sentence.

The "strictly weaker" claim about the 0-indexed variant (card `D1`) was also
re-derived by hand rather than taken on trust. With `a = p_m`, `b = p_{m+1}`,
the true form is `b^(1/(m+1)) < a^(1/m)` and the mis-transcription is
`b^(1/m) < a^(1/(m-1))`. From the former, `b^(1/m) < a^((m+1)/m²)`, and
`(m+1)/m² ≤ 1/(m-1)` since `(m+1)(m-1) = m²-1 ≤ m²`. So the true statement
implies the mis-transcription and not conversely: **strictly weaker**, as
claimed.

### Checked and clean

- No `native_decide`, no `axiom`, no `@[implemented_by]`, no `unsafe` anywhere.
- `Real.rpow` really is what `F1`, `F1'` and `T` use (confirmed by `rfl` against
  `Real.rpow` explicitly, not by reading the pretty-printer).
- Every definition re-read against its card: `F1`/`F1'` vs `D4`+Kourbatov §1
  eq. (1); `F2` vs `D4` F2; `F3` vs `D4` F3; `T` vs `D5`; `F4` vs `D5`/`L1` F4;
  `g`, `L` vs `D2`. All match.
- `L n = Real.log (p n)` is defined but currently unused. Kept because `D2`
  defines it and the asymptotic cards (`L2`, `L3`, `L4`) are stated in terms of
  it; flagged here so it is not mistaken for dead code left by accident.

## The refutation branch is not a second `sorry`

Two contradictory `sorry`-ed theorems (`firoozbakht` and `not_firoozbakht`) in
one namespace would let any later file close any goal via
`absurd firoozbakht not_firoozbakht`, silently voiding every other proof in the
development. The refutation branch is therefore `def Refuted : Prop := ¬ Conjecture`
plus `refuted_of_witness`, which is **proven**.
