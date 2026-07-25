/-
# Firoozbakht's conjecture — the statement (fidelity anchor)

This file is the **fidelity anchor** of the whole formal leg. Nothing downstream
means anything if the definitions here are wrong, so every choice is justified
inline and cross-checked against a machine-checked sanity block at the bottom.

Concept cards: `D1` (indexing), `D2` (gap and log), `D4` (the conjecture),
`D5` (the threshold `T n`), `L1` (equivalence of the forms), `T4` (Lean substrate).

## The conjecture

Firoozbakht (1982, unpublished; first printed in Ribenboim, *The Little Book of
Bigger Primes*, 2nd ed., p. 185) conjectured that the sequence `n ↦ p_n ^ (1/n)`
is **strictly decreasing**, i.e.

    p_{n+1} ^ (1/(n+1))  <  p_n ^ (1/n)      for all n ≥ 1.

It is **OPEN**: not proven, not refuted. Every target theorem in this
development is therefore `sorry`-ed and explicitly tagged, and no file in this
project may ever discharge `firoozbakht` by any means other than a real proof.

## Indexing — the highest-severity hazard in this attack (card `D1`)

The conjecture and *every* index threshold in the literature (`k > 9`, `n ≥ 10`,
`n ≥ 5`, `n > 4`, `n ≥ 3645`) are stated **1-indexed**: `p_1 = 2`, `p_2 = 3`, …

Mathlib's primitive is **0-indexed**: `Nat.nth Nat.Prime 0 = 2`.

Writing the conjecture directly against `Nat.nth Nat.Prime n` — as an earlier
draft of the attack plan did — yields `p_{m+1}^{m-1} < p_m^{m}`, which is a
*strictly weaker* statement (exponent ratio `1 + 1/(m-1)` instead of `1 + 1/m`)
and additionally drops the case `m = 1`. A development could go fully green
having formalized a different conjecture. The offset is corrected **once**,
here, in the definition of `p`, and nowhere else.
-/

import Mathlib.Data.Nat.Prime.Nth
import Mathlib.Data.Nat.Nth
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace Firoozbakht

open Nat

/-! ## The prime sequence, 1-indexed (card `D1`) -/

/-- The `n`-th prime under the **1-indexed** convention of this attack:
`p 1 = 2`, `p 2 = 3`, `p 3 = 5`, …

Implemented as `Nat.nth Nat.Prime (n - 1)` with truncated subtraction, so
`p 0 = p 1 = 2` is a junk value. Every statement below guards on `1 ≤ n`, so the
junk value is never reachable from a target theorem; `p_zero_eq_p_one` records
it explicitly rather than leaving it as a trap.

`Nat.nth` is `noncomputable` (card `T4`, Fact 1): there is no kernel reduction
at all, so `decide`/`native_decide` cannot evaluate `p n`. Finite checks must go
through prime literals and the base `@[simp]` lemmas — see `FiniteCheck.lean`. -/
noncomputable def p (n : ℕ) : ℕ := Nat.nth Nat.Prime (n - 1)

/-- The primes are infinite; this hypothesis is required by essentially every
`Nat.nth` monotonicity lemma (card `T4`, hazard 2). -/
theorem infinite_setOf_prime : (setOf Nat.Prime).Infinite := Nat.infinite_setOf_prime

@[simp] theorem p_one : p 1 = 2 := Nat.nth_prime_zero_eq_two
@[simp] theorem p_two : p 2 = 3 := Nat.nth_prime_one_eq_three
@[simp] theorem p_three : p 3 = 5 := Nat.nth_prime_two_eq_five
@[simp] theorem p_four : p 4 = 7 := Nat.nth_prime_three_eq_seven
@[simp] theorem p_five : p 5 = 11 := Nat.nth_prime_four_eq_eleven

/-- The junk value at `0`, recorded so nobody trips over it. -/
theorem p_zero_eq_p_one : p 0 = p 1 := rfl

/-- The bridge to Mathlib's 0-indexed primitive, in the direction one usually
needs it: `Nat.nth Nat.Prime k = p_{k+1}`. -/
theorem p_succ (k : ℕ) : p (k + 1) = Nat.nth Nat.Prime k := by
  simp [p]

/-- `p n` really is prime, for every `n` (including the junk index `0`). -/
theorem prime_p (n : ℕ) : Nat.Prime (p n) :=
  Nat.nth_mem_of_infinite infinite_setOf_prime _

/-- The sequence is strictly increasing from index `1` on. -/
theorem p_lt_p_succ {n : ℕ} (hn : 1 ≤ n) : p n < p (n + 1) := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hn
  have h : Nat.nth Nat.Prime k < Nat.nth Nat.Prime (k + 1) :=
    (Nat.nth_lt_nth infinite_setOf_prime).2 (Nat.lt_succ_self k)
  simpa [p, Nat.add_comm, Nat.add_assoc] using h

/-- Every prime is at least `2`, so `2 ≤ p n`; used throughout to know the bases
of the powers below are `> 1`. -/
theorem two_le_p (n : ℕ) : 2 ≤ p n := (prime_p n).two_le

/-! ## Gap and logarithm (card `D2`) -/

/-- The `n`-th prime gap, `g n = p_{n+1} - p_n`, 1-indexed. Subtraction is over
`ℕ`; it is genuine subtraction for `n ≥ 1` since `p n < p (n+1)` there. -/
noncomputable def g (n : ℕ) : ℕ := p (n + 1) - p n

/-- `L n = log p_n`. -/
noncomputable def L (n : ℕ) : ℝ := Real.log (p n)

/-! ## The threshold (card `D5`) -/

/-- The Firoozbakht threshold `T n = p_n ^ (1 + 1/n) - p_n = p_n * (p_n ^ (1/n) - 1)`.

Kourbatov (2015) writes this `f_k`; Visser (2019, Conjecture 3, eq. (2.4))
writes it inline. Real-valued, via `Real.rpow`. -/
noncomputable def T (n : ℕ) : ℝ := (p n : ℝ) ^ (1 + 1 / (n : ℝ)) - (p n : ℝ)

/-! ## The four forms of the conjecture (card `D4`)

All four are equivalent (card `L1`, formalized in `Equivalence.lean`). `F3` is
taken as the **primary** definition: it is a statement about natural numbers
only — no `rpow`, no `log`, no analysis — and it is the form every downstream
arithmetic argument wants. -/

/-- **(F1)** Real-analytic, as posed: `p_{n+1} ^ (1/(n+1)) < p_n ^ (1/n)`. -/
def F1 (n : ℕ) : Prop :=
  (p (n + 1) : ℝ) ^ (1 / ((n : ℝ) + 1)) < (p n : ℝ) ^ (1 / (n : ℝ))

/-- **(F1′)** Kourbatov's form (2015, §1 eq. (1)): `p_{k+1} < p_k ^ (1 + 1/k)`. -/
def F1' (n : ℕ) : Prop := (p (n + 1) : ℝ) < (p n : ℝ) ^ (1 + 1 / (n : ℝ))

/-- **(F2)** Logarithmic: `n * log p_{n+1} < (n+1) * log p_n`. -/
def F2 (n : ℕ) : Prop := (n : ℝ) * Real.log (p (n + 1)) < ((n : ℝ) + 1) * Real.log (p n)

/-- **(F3)** Purely arithmetic — no reals, no logarithms:
`p_{n+1} ^ n < p_n ^ (n+1)`. This is the primary form. -/
def F3 (n : ℕ) : Prop := (p (n + 1)) ^ n < (p n) ^ (n + 1)

/-- **(F4)** Gap form: `g_n < T_n`. -/
def F4 (n : ℕ) : Prop := (g n : ℝ) < T n

/-! ## The conjecture itself -/

/-- **Firoozbakht's conjecture** `Conjecture`, in the primary arithmetic form:

    ∀ n ≥ 1,  p_{n+1} ^ n  <  p_n ^ (n+1) .

Index check (card `D1`): at `n = 1` this reads `p 2 ^ 1 < p 1 ^ 2`, i.e.
`3 < 4` — the genuine first case, which the 0-indexed mis-transcription drops.
At `n = 4` it reads `p 5 ^ 4 < p 4 ^ 5`, i.e. `11^4 = 14641 < 16807 = 7^5`. Both
are machine-checked in `FiniteCheck.lean`. -/
def Conjecture : Prop := ∀ n : ℕ, 1 ≤ n → F3 n

/-- The conjecture in its originally-posed real-analytic form: `n ↦ p_n ^ (1/n)`
is strictly decreasing. Equivalent to `Conjecture` by `L1`. -/
def ConjectureReal : Prop := ∀ n : ℕ, 1 ≤ n → F1 n

/-- Visser (2019, Conjecture 1, eq. (1.1)) states the conjecture with `≤` rather
than `<`. The two agree: equality `p_{n+1}^n = p_n^{n+1}` is impossible at every
`n ≥ 1`, since the two sides have disjoint prime supports (card `D4`, hazard 1).
Proven below, so the two literature variants are known to define the same
conjecture rather than merely believed to. -/
theorem p_pow_ne (n : ℕ) (hn : 1 ≤ n) : (p (n + 1)) ^ n ≠ (p n) ^ (n + 1) := by
  intro h
  have hlt := p_lt_p_succ hn
  have hdvd : p (n + 1) ∣ (p n) ^ (n + 1) := by
    rw [← h]; exact dvd_pow_self _ (by omega)
  have h1 := (prime_p (n + 1)).dvd_of_dvd_pow hdvd
  have h2 := (Nat.prime_dvd_prime_iff_eq (prime_p (n + 1)) (prime_p n)).mp h1
  omega

/-- Visser's `≤` form and the strict form coincide, at every `n ≥ 1`. -/
theorem strict_iff_nonstrict (n : ℕ) (hn : 1 ≤ n) :
    ((p (n + 1)) ^ n < (p n) ^ (n + 1)) ↔ ((p (n + 1)) ^ n ≤ (p n) ^ (n + 1)) :=
  ⟨le_of_lt, fun h => lt_of_le_of_ne h (p_pow_ne n hn)⟩

/-! ## The target theorem — OPEN

`Conjecture` is an open problem. The declaration below is the goal of the
attack, stated so that a proof (or, via `refuted_of_witness`, a refutation) has
an unambiguous target. **It must never be discharged by anything but
mathematics.**

`Conjecture` is `Π₁`; its negation is `Σ₁` (card `L16`) — a single certified
counterexample index refutes it, whereas a proof must cover all `n`. -/

/-- **TARGET (open).** Firoozbakht's conjecture holds. -/
theorem firoozbakht : Conjecture := by
  sorry

/-! ### The refutation branch

The refutation target is deliberately **not** stated as a second `sorry`-ed
`theorem`. Two contradictory `sorry`-ed theorems in one namespace let any later
file close any goal by `absurd firoozbakht not_conjecture`, which would silently
void every other proof in the development. The refutation branch is therefore a
`Prop` plus a witness-shaped reduction lemma that is *actually proven*. -/

/-- The refutation branch as a proposition (card `T5`). -/
def Refuted : Prop := ¬ Conjecture

/-- A single index `n ≥ 1` with `p_n ^ (n+1) ≤ p_{n+1} ^ n` refutes the
conjecture. This is the `Σ₁` shape a counterexample search must produce
(card `L16`); it is proven, not assumed. -/
theorem refuted_of_witness {n : ℕ} (hn : 1 ≤ n)
    (h : (p n) ^ (n + 1) ≤ (p (n + 1)) ^ n) : Refuted := fun hF =>
  absurd (hF n hn) (not_lt.mpr h)

end Firoozbakht
