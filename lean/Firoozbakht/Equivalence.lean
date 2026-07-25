/-
# L1 — Equivalence of the four forms

Card `L1`: for every `n ≥ 1`,  `F1 ↔ F1' ↔ F2 ↔ F3 ↔ F4`.

Corroborated at two L0 locators: Kourbatov (2015) §1 eq. (1) states the
`F1 ↔ F1'` step; Visser (2019) Conjecture 1 eq. (1.1) states `F1 ↔ F2` and
Conjecture 3 eq. (2.4) states the gap form `F4`.

This is the hinge of the whole attack: without it Firoozbakht is a curiosity
about `n`-th roots; with it, Firoozbakht **is a prime-gap bound**, and the
analytic literature on gaps becomes admissible. The equivalence is
**unconditional and index-free** — no `n ≥ n₀` appears anywhere in it (card
`L1`, hazard 2).

The paper proof is elementary and complete (card `L1` is marked PROVEN). The
Lean proofs below are `sorry`-ed: this leg is the *skeleton*, and closing them is
pure `Real.rpow`/`Real.log` API work budgeted to the downstream proof leg
(card `T4`, node N2). What is established here is the **statement** of each
equivalence and the fact that they typecheck against the anchor definitions.
-/

import Firoozbakht.Statement

namespace Firoozbakht

/-- `F3 ↔ F2`: take logarithms. Both sides are positive since `p n ≥ 2`. -/
theorem F3_iff_F2 (n : ℕ) (hn : 1 ≤ n) : F3 n ↔ F2 n := by
  sorry

/-- `F1 ↔ F3`: raise to the power `n(n+1)`, which is a strictly monotone
bijection of `(0, ∞)`. -/
theorem F1_iff_F3 (n : ℕ) (hn : 1 ≤ n) : F1 n ↔ F3 n := by
  sorry

/-- `F2 ↔ F1'`: divide by `n` and exponentiate. -/
theorem F2_iff_F1' (n : ℕ) (hn : 1 ≤ n) : F2 n ↔ F1' n := by
  sorry

/-- `F1' ↔ F4`: `p_{n+1} < p_n ^ (1 + 1/n) = p_n + T n`, i.e. `g n < T n`.

This is the highest-risk node of the Lean plan (card `T4`, node N5): it
re-imports `Real.rpow` and the natural-subtraction in `g` into a statement the
anchor was designed to keep in `ℕ`. The `1 ≤ n` hypothesis is what makes
`(g n : ℝ) = (p (n+1) : ℝ) - (p n : ℝ)` — truncated subtraction is genuine
subtraction only because `p n < p (n+1)` there. -/
theorem F1'_iff_F4 (n : ℕ) (hn : 1 ≤ n) : F1' n ↔ F4 n := by
  sorry

/-- The cast of the gap is a genuine real subtraction for `n ≥ 1`. Proven — it
is the one step of `F1'_iff_F4` that is about `ℕ`-subtraction rather than
`rpow`, and getting it wrong would silently break the gap form. -/
theorem cast_g (n : ℕ) (hn : 1 ≤ n) : (g n : ℝ) = (p (n + 1) : ℝ) - (p n : ℝ) := by
  have h : p n ≤ p (n + 1) := (p_lt_p_succ hn).le
  simp [g, Nat.cast_sub h]

/-! ## The chain, assembled -/

theorem F1_iff_F2 (n : ℕ) (hn : 1 ≤ n) : F1 n ↔ F2 n :=
  (F1_iff_F3 n hn).trans (F3_iff_F2 n hn)

theorem F1_iff_F1' (n : ℕ) (hn : 1 ≤ n) : F1 n ↔ F1' n :=
  (F1_iff_F2 n hn).trans (F2_iff_F1' n hn)

theorem F1_iff_F4 (n : ℕ) (hn : 1 ≤ n) : F1 n ↔ F4 n :=
  (F1_iff_F1' n hn).trans (F1'_iff_F4 n hn)

theorem F3_iff_F4 (n : ℕ) (hn : 1 ≤ n) : F3 n ↔ F4 n :=
  ((F1_iff_F3 n hn).symm).trans (F1_iff_F4 n hn)

/-- The primary arithmetic form and the originally-posed real form state the
same conjecture. -/
theorem conjecture_iff_real : Conjecture ↔ ConjectureReal :=
  ⟨fun h n hn => (F1_iff_F3 n hn).mpr (h n hn),
   fun h n hn => (F1_iff_F3 n hn).mp (h n hn)⟩

/-- The gap form of the conjecture: `∀ n ≥ 1, g_n < T_n` (card `D5`). -/
theorem conjecture_iff_gap : Conjecture ↔ ∀ n : ℕ, 1 ≤ n → F4 n :=
  ⟨fun h n hn => (F3_iff_F4 n hn).mp (h n hn),
   fun h n hn => (F3_iff_F4 n hn).mpr (h n hn)⟩

end Firoozbakht
