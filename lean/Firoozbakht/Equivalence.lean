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

The paper proof is elementary and complete (card `L1` is marked PROVEN). As of
the `lean-probe` leg all four steps are **discharged with real proof terms** —
no `sorry` remains in this file, and none of them uses `native_decide`, an
`axiom`, or any hypothesis beyond `1 ≤ n`.

The shape of every proof is the same, and it is worth naming once: each form is
an inequality between two *positive* reals (or, for `F3`, between two positive
naturals), and `Real.log` is a strictly monotone bijection on the positives. So
each step is (i) cast into ℝ if needed, (ii) apply `Real.log_lt_log_iff`, (iii)
push the logarithm through `^` (`Real.log_pow` for ℕ-powers, `Real.log_rpow` for
`rpow`), (iv) clear the denominators `1/n`, `1/(n+1)` — legal because `n ≥ 1`.
Only `F1' ↔ F4` is different: it is pure algebra on `sub_lt_sub_iff_right`, once
`cast_g` has said that the ℕ-subtraction in `g` is genuine.
-/

import Firoozbakht.Statement

namespace Firoozbakht

/-! ## Positivity — the side conditions every step below needs

`Real.log` is only monotone on the positives, and `1/n` is only invertible for
`n ≥ 1`. These two lemmas carry those facts so that the proofs below read as
algebra rather than as bookkeeping.

Note that `positivity` is *not* usable for `p_pos_real`: it sees only a ℕ-cast
and so yields `0 ≤ (p n : ℝ)`, not `0 <` (it says so — "failed to prove strict
positivity, but it would be possible to prove nonnegativity"). The strict bound
has to be routed through `two_le_p` by hand. -/

/-- `0 < p n` as a real. Follows from `2 ≤ p n` (`Statement.two_le_p`). -/
theorem p_pos_real (n : ℕ) : (0 : ℝ) < (p n : ℝ) := by
  have : 0 < p n := lt_of_lt_of_le (by norm_num) (two_le_p n)
  exact_mod_cast this

/-- `0 < n` as a real, from `1 ≤ n`. -/
theorem n_pos_real {n : ℕ} (hn : 1 ≤ n) : (0 : ℝ) < (n : ℝ) := by
  exact_mod_cast hn

/-- `F3 ↔ F2`: take logarithms. Both sides are positive since `p n ≥ 2`, so
`Real.log_lt_log_iff` applies; `Real.log_pow` turns each ℕ-power into a product.
The `1 ≤ n` hypothesis is genuinely **not needed** for this step (both powers are
positive at every `n`, including `n = 0`), so the binder is named `_hn`: it is
kept only so the whole chain has one uniform shape at `n ≥ 1`. Do not read the
hypothesis as load-bearing here — it is not. -/
theorem F3_iff_F2 (n : ℕ) (_hn : 1 ≤ n) : F3 n ↔ F2 n := by
  have hA := p_pos_real (n + 1)
  have hB := p_pos_real n
  rw [F3, F2, ← Nat.cast_lt (α := ℝ)]
  push_cast
  rw [← Real.log_lt_log_iff (pow_pos hA n) (pow_pos hB (n + 1)), Real.log_pow,
    Real.log_pow]
  push_cast
  constructor <;> intro h <;> linarith

/-- `F1 ↔ F3`: `F1` says `A ^ (1/(n+1)) < B ^ (1/n)` with `A, B > 0`. Taking
logarithms turns it into `(1/(n+1)) log A < (1/n) log B`; multiplying by the
positive `n(n+1)` gives `n log A < (n+1) log B`, which is `F2`, which is `F3` by
the step above. This is the "raise to the power `n(n+1)`" argument of card `L1`,
carried out on the log side where the monotonicity lemma is a bijection. -/
theorem F1_iff_F3 (n : ℕ) (hn : 1 ≤ n) : F1 n ↔ F3 n := by
  have hA := p_pos_real (n + 1)
  have hB := p_pos_real n
  have hn0 := n_pos_real hn
  have hn1 : (0 : ℝ) < (n : ℝ) + 1 := by linarith
  rw [F3_iff_F2 n hn, F1, F2,
    ← Real.log_lt_log_iff (Real.rpow_pos_of_pos hA _) (Real.rpow_pos_of_pos hB _),
    Real.log_rpow hA, Real.log_rpow hB, div_mul_eq_mul_div, div_mul_eq_mul_div,
    one_mul, one_mul, div_lt_div_iff₀ hn1 hn0]
  constructor <;> intro h <;> linarith

/-- `F2 ↔ F1'`: divide by `n` and exponentiate. On the log side, `F1'` reads
`log A < (1 + 1/n) log B`; multiplying by `n > 0` gives `n log A < (n+1) log B`,
which is `F2`. -/
theorem F2_iff_F1' (n : ℕ) (hn : 1 ≤ n) : F2 n ↔ F1' n := by
  have hA := p_pos_real (n + 1)
  have hB := p_pos_real n
  have hn0 := n_pos_real hn
  rw [F2, F1', ← Real.log_lt_log_iff hA (Real.rpow_pos_of_pos hB _), Real.log_rpow hB,
    show (1 + 1 / (n : ℝ)) * Real.log (p n) = ((n : ℝ) + 1) * Real.log (p n) / n by
      field_simp,
    lt_div_iff₀ hn0]
  constructor <;> intro h <;> linarith

/-- The cast of the gap is a genuine real subtraction for `n ≥ 1`. It is the one
step of `F1'_iff_F4` that is about `ℕ`-subtraction rather than `rpow`, and getting
it wrong would silently break the gap form. -/
theorem cast_g (n : ℕ) (hn : 1 ≤ n) : (g n : ℝ) = (p (n + 1) : ℝ) - (p n : ℝ) := by
  have h : p n ≤ p (n + 1) := (p_lt_p_succ hn).le
  simp [g, Nat.cast_sub h]

/-- `F1' ↔ F4`: `p_{n+1} < p_n ^ (1 + 1/n) = p_n + T n`, i.e. `g n < T n`.

This is the highest-risk node of the Lean plan (card `T4`, node N5): it
re-imports `Real.rpow` and the natural-subtraction in `g` into a statement the
anchor was designed to keep in `ℕ`. The `1 ≤ n` hypothesis is what makes
`(g n : ℝ) = (p (n+1) : ℝ) - (p n : ℝ)` — truncated subtraction is genuine
subtraction only because `p n < p (n+1)` there.

The proof turns out to be the shortest of the four: once `cast_g` has replaced
`(g n : ℝ)` by `p_{n+1} - p_n`, both sides of `F4` carry the same `- p_n`, and
`sub_lt_sub_iff_right` cancels it. No `rpow` lemma is used at all — `p_n ^ (1+1/n)`
is carried through as an opaque real. -/
theorem F1'_iff_F4 (n : ℕ) (hn : 1 ≤ n) : F1' n ↔ F4 n := by
  rw [F1', F4, T, cast_g n hn, sub_lt_sub_iff_right]

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
