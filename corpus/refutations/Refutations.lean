/-
# Red-team corpus — refutations

For every entry `Fxx` in `../manifest.json` whose `evidence` is `"refuted"`,
this file contains a theorem `Fxx_refuted : ¬ (statement)`, **proven**, no
`sorry`.

This is the strong half of the corpus. A file in `../attempts/` that fails to
compile only shows that *one* proof attempt failed; a proof of `¬ S` here shows
that `S` is false and that no attempt can ever succeed.

Everything below is about the definitions of the `Firoozbakht` namespace as they
stand in `../../lean/Firoozbakht/`. If a downstream leg changes those
definitions in a way that makes any theorem here fail to compile, that is the
alarm firing, not a bug in this file.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace Firoozbakht.RedTeam

open Firoozbakht

/-! ## Indexing and fidelity (cards `D1`, `T4`) -/

/-- **F01** — `p 1 = 3`, the 0-indexed reading of "the first prime". -/
theorem F01_refuted : ¬ (p 1 = 3) := by
  intro h; rw [p_one] at h; omega

/-- **F02** — the missing `-1`: `Nat.nth Nat.Prime k = p k`.

This is the load-bearing entry of the whole corpus. Card `D1` says the two
indexing families cannot be told apart by truth value — every case of both holds
in any range anyone can check. They *can* be told apart at the level of
numerals, and this is that separation, machine-checked. -/
theorem F02_refuted : ¬ (∀ k : ℕ, Nat.nth Nat.Prime k = p k) := by
  intro h
  have h1 := h 1
  rw [Nat.nth_prime_one_eq_three, p_one] at h1
  omega

/-- **F03** — `p` is injective. False: `p 0 = p 1 = 2` is the junk value that
truncated subtraction in `p`'s definition creates. -/
theorem F03_refuted : ¬ Function.Injective p := by
  intro h
  have h01 : (0 : ℕ) = 1 := h p_zero_eq_p_one
  omega

/-- **F04** — `p` is strictly increasing, with the `1 ≤ n` guard dropped. -/
theorem F04_refuted : ¬ (∀ n : ℕ, p n < p (n + 1)) := by
  intro h
  have h0 : p 0 < p 1 := by simpa using h 0
  rw [p_zero_eq_p_one] at h0
  exact lt_irrefl _ h0

/-- **F08** — the guard replaced by a shift: `p (n-1) < p n`. At `n = 0`
truncated subtraction gives `p 0 < p 0`. -/
theorem F08_refuted : ¬ (∀ n : ℕ, p (n - 1) < p n) := by
  intro h
  have h0 : p 0 < p 0 := by simpa using h 0
  exact lt_irrefl _ h0

/-- **F19** — the hypothesis moved to the wrong side of the arrow. At `n = 0`
the antecedent is vacuously true and the conclusion is false. -/
theorem F19_refuted : ¬ (∀ n : ℕ, (1 ≤ n → p n < p (n + 1)) → 1 ≤ n) := by
  intro h
  have : (1 : ℕ) ≤ 0 := h 0 (by intro hc; omega)
  omega

/-! ## Gaps and ℕ-subtraction (card `D2`) -/

/-- **F05** — `0 < g n` with the `1 ≤ n` guard dropped. `g 0 = p 1 - p 0 = 0`. -/
theorem F05_refuted : ¬ (∀ n : ℕ, 0 < g n) := by
  intro h
  have h0 : (0 : ℕ) < g 0 := h 0
  have hg : g 0 = 0 := by simp [g, p_zero_eq_p_one]
  omega

/-- **F06** — truncated subtraction treated as invertible in ℕ. At `n = 1`:
`(2 - 3) + 3 = 3 ≠ 2`. -/
theorem F06_refuted : ¬ (∀ n : ℕ, (p n - p (n + 1)) + p (n + 1) = p n) := by
  intro h
  have h1 := h 1
  simp only [show (1 : ℕ) + 1 = 2 from rfl, p_one, p_two] at h1
  omega

/-- **F07** — the cast of a truncated difference read as a genuine difference in
ℤ. At `n = 1`: `((2 - 3 : ℕ) : ℤ) = 0`, not `-1`. Card `L1`'s `cast_g` needs
`1 ≤ n` *and* the inequality in the right direction; this drops both. -/
theorem F07_refuted :
    ¬ (∀ n : ℕ, ((p n - p (n + 1) : ℕ) : ℤ) = (p n : ℤ) - (p (n + 1) : ℤ)) := by
  intro h
  have h1 := h 1
  simp only [show (1 : ℕ) + 1 = 2 from rfl, p_one, p_two] at h1
  norm_num at h1

/-- **F11** — a false gap bound: every gap is at most `2`. Refuted at `n = 4`,
`g 4 = 11 - 7 = 4`. -/
theorem F11_refuted : ¬ (∀ n : ℕ, 1 ≤ n → g n ≤ 2) := by
  intro h
  have h4 := h 4 (by omega)
  simp only [show (4 : ℕ) + 1 = 5 from rfl, g, p_four, p_five] at h4
  omega

/-! ## Direction and strictness (card `D4`) -/

/-- **F09** — Visser's `≤` form differs from the strict form because the
equality case occurs somewhere. Refuted by `p_pow_ne`, which is proven in the
anchor: the two sides have disjoint prime supports. -/
theorem F09_refuted : ¬ (∃ n : ℕ, 1 ≤ n ∧ (p (n + 1)) ^ n = (p n) ^ (n + 1)) := by
  rintro ⟨n, hn, h⟩
  exact p_pow_ne n hn h

/-- **F10** — the inequality with the sides swapped. At `n = 1`: `2^2 = 4 < 3 = 3^1`
is false. -/
theorem F10_refuted : ¬ (∀ n : ℕ, 1 ≤ n → (p n) ^ (n + 1) < (p (n + 1)) ^ n) := by
  intro h
  have h1 := h 1 (by omega)
  simp only [show (1 : ℕ) + 1 = 2 from rfl, p_one, p_two] at h1
  omega

/-! ## Quantifier order -/

/-- **F15** — `∃ largest ∀` in place of `∀ ∃ larger`: the primes have a maximum. -/
theorem F15_refuted : ¬ (∃ n : ℕ, 1 ≤ n ∧ ∀ m : ℕ, 1 ≤ m → p m ≤ p n) := by
  rintro ⟨n, hn, h⟩
  have h1 : p (n + 1) ≤ p n := h (n + 1) (by omega)
  have h2 : p n < p (n + 1) := p_lt_p_succ hn
  omega

/-! ## Universes and impredicativity -/

/-- **F17** — `∀ α : Prop, α`, "every proposition holds". Impredicative `Prop`
makes this a well-formed `Prop`, so it elaborates; it is simply false.

An entry that *elaborates and is refuted*, in deliberate contrast with **F20**
(`∀ α : Type, α`), which does not even elaborate under `¬`: it lives in `Type 1`,
not `Prop`. Drafting this corpus hit that error, which is the point — the two
failure modes are different and the manifest records which is which. -/
theorem F17_refuted : ¬ (∀ α : Prop, α) := by
  intro h
  exact h False

end Firoozbakht.RedTeam
