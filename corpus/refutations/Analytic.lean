/-
# Red-team corpus — refutations, analytic half

The entries whose refutation needs `Real.rpow` / `Real.log` rather than `omega`.
Same contract as `Refutations.lean`: every theorem here is a **proof that the
corpus statement is false**, with no `sorry`.

These are the entries that matter most for the downstream proof leg, because
they live in exactly the API (`rpow`, `log`, the threshold `T`) that card `T4`
names as node N5, the highest-risk node of the Lean plan.
-/

import Firoozbakht.Statement
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Complex.ExponentialBounds

namespace Firoozbakht.RedTeam

open Firoozbakht

/-! ## Numeric facts about `rpow` used below, proven once -/

/-- `2 ^ (3/2) < 3`, by squaring: `8 < 9`. -/
theorem two_rpow_three_halves_lt_three : (2 : ℝ) ^ ((3 : ℝ) / 2) < 3 := by
  have hnn : (0 : ℝ) ≤ (2 : ℝ) ^ ((3 : ℝ) / 2) := Real.rpow_nonneg (by norm_num) _
  have hsq : ((2 : ℝ) ^ ((3 : ℝ) / 2)) ^ (2 : ℕ) = 8 := by
    rw [← Real.rpow_natCast ((2 : ℝ) ^ ((3 : ℝ) / 2)) 2, ← Real.rpow_mul (by norm_num)]
    norm_num
  nlinarith [hsq, hnn]

/-- `5 < 3 ^ (3/2)`, by squaring: `25 < 27`. -/
theorem five_lt_three_rpow_three_halves : (5 : ℝ) < (3 : ℝ) ^ ((3 : ℝ) / 2) := by
  have hnn : (0 : ℝ) ≤ (3 : ℝ) ^ ((3 : ℝ) / 2) := Real.rpow_nonneg (by norm_num) _
  have hsq : ((3 : ℝ) ^ ((3 : ℝ) / 2)) ^ (2 : ℕ) = 27 := by
    rw [← Real.rpow_natCast ((3 : ℝ) ^ ((3 : ℝ) / 2)) 2, ← Real.rpow_mul (by norm_num)]
    norm_num
  nlinarith [hsq, hnn]

/-- `T 1 = 2`. The threshold at the first index: `2 ^ (1 + 1/1) - 2 = 4 - 2`. -/
theorem T_one : T 1 = 2 := by
  have e : (1 : ℝ) + 1 / ((1 : ℕ) : ℝ) = ((2 : ℕ) : ℝ) := by norm_num
  simp only [T, p_one, e, Real.rpow_natCast]
  norm_num

/-- `T 2 = 3 ^ (3/2) - 3`. -/
theorem T_two : T 2 = (3 : ℝ) ^ ((3 : ℝ) / 2) - 3 := by
  have e : (1 : ℝ) + 1 / ((2 : ℕ) : ℝ) = (3 : ℝ) / 2 := by norm_num
  simp only [T, p_two, e]
  norm_num

/-! ## The entries -/

/-- **F13** — the gap form of the conjecture with the inequality reversed:
`T n < g n` in place of card `D5`'s `g n < T n`. At `n = 1`: `T 1 = 2` and
`g 1 = 1`, so the reversed form fails at the very first index. -/
theorem F13_refuted : ¬ (∀ n : ℕ, 1 ≤ n → T n < (g n : ℝ)) := by
  intro h
  have h1 := h 1 (by omega)
  have hg : g 1 = 1 := by simp [g]
  rw [T_one, hg] at h1
  norm_num at h1

/-- **F14** — Kourbatov's form `p_{k+1} < p_k ^ (1 + 1/k)` with the exponent's
denominator shifted to `k + 1`, a *strengthening* of the conjecture. At `n = 1`
it asserts `3 < 2 ^ (3/2) = 2.828…`, which is false. -/
theorem F14_refuted :
    ¬ (∀ n : ℕ, 1 ≤ n → (p (n + 1) : ℝ) < (p n : ℝ) ^ (1 + 1 / ((n : ℝ) + 1))) := by
  intro h
  have h1 := h 1 (by omega)
  have e : (1 : ℝ) + 1 / (((1 : ℕ) : ℝ) + 1) = (3 : ℝ) / 2 := by norm_num
  rw [e] at h1
  simp only [show (1 : ℕ) + 1 = 2 from rfl, p_one, p_two] at h1
  have := two_rpow_three_halves_lt_three
  norm_num at h1
  linarith

/-- **F18** — card `L16`(c) says `T n` is strictly decreasing in `n` **at fixed
`p_n`**. Drop the "at fixed `p_n`" and the claim becomes `T (n+1) < T n`, which
is false immediately: `T 1 = 2` and `T 2 = 3^(3/2) - 3 = 2.196…`.

This is the sharpest dropped-hypothesis entry in the corpus. The dropped clause
is not decorative: the whole repair in `L16`(c) — that a *lower* bound on the
rank suffices for a refutation certificate — rests on it, and reading the card's
monotonicity as monotonicity in `n` alone inverts the direction of the bound. -/
theorem F18_refuted : ¬ (∀ n : ℕ, 1 ≤ n → T (n + 1) < T n) := by
  intro h
  have h1 := h 1 (by omega)
  rw [show (1 : ℕ) + 1 = 2 from rfl, T_one, T_two] at h1
  have := five_lt_three_rpow_three_halves
  linarith

/-- **F12** — a gap bound that is far too strong: `g n < log p_n` for all
`n ≥ 1`. At `n = 1` it asserts `1 < log 2 = 0.693…`. -/
theorem F12_refuted : ¬ (∀ n : ℕ, 1 ≤ n → (g n : ℝ) < Real.log (p n)) := by
  intro h
  have h1 := h 1 (by omega)
  have hg : g 1 = 1 := by simp [g]
  rw [hg] at h1
  simp only [p_one] at h1
  have hlog : Real.log 2 < 0.6931471808 := Real.log_two_lt_d9
  norm_num at h1
  linarith

/-- **F16** — quantifier order: `∃ N, ∀ n ≥ N, p_n ^ (1/n) < 1`. The true
statement in this neighbourhood is that `p_n ^ (1/n) → 1` *from above*; the
sequence is bounded **below** by `1`, never under it, since `p_n ≥ 2` and
`1/n > 0`. -/
theorem F16_refuted : ¬ (∃ N : ℕ, ∀ n : ℕ, N ≤ n → (p n : ℝ) ^ (1 / (n : ℝ)) < 1) := by
  rintro ⟨N, h⟩
  have hN := h (N + 1) (by omega)
  have hp : (2 : ℝ) ≤ (p (N + 1) : ℝ) := by exact_mod_cast two_le_p (N + 1)
  have hx : (0 : ℝ) < (p (N + 1) : ℝ) := by linarith
  have hcast : (((N + 1 : ℕ) : ℝ)) = (N : ℝ) + 1 := by push_cast; ring
  have hy : (0 : ℝ) < 1 / (((N + 1 : ℕ) : ℝ)) := by
    rw [hcast]; positivity
  have hgt : (1 : ℝ) < (p (N + 1) : ℝ) ^ (1 / (((N + 1 : ℕ) : ℝ))) :=
    Real.one_lt_rpow_iff_of_pos hx |>.mpr (Or.inl ⟨by linarith, hy⟩)
  linarith

/-- **F21** — the ℝ-valued twin of `F07`, and the exact shape of `cast_g`
(`Equivalence.lean`) with the subtraction reversed and the `1 ≤ n` guard
dropped. At `n = 1`: `((2 - 3 : ℕ) : ℝ) = 0`, while `(2 : ℝ) - 3 = -1`.

Card `T4` names `F1'_iff_F4` the highest-risk node precisely because it moves
`ℕ`-subtraction across a cast. This entry is the failure that node is exposed
to, isolated. -/
theorem F21_refuted :
    ¬ (∀ n : ℕ, ((p n - p (n + 1) : ℕ) : ℝ) = (p n : ℝ) - (p (n + 1) : ℝ)) := by
  intro h
  have h1 := h 1
  simp only [show (1 : ℕ) + 1 = 2 from rfl, p_one, p_two] at h1
  norm_num at h1

end Firoozbakht.RedTeam
