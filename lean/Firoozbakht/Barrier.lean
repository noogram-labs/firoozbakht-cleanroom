/-
# The Bertrand barrier — why the substrate cannot reach the target

This file is the **negative** half of the round-2 lean probe (molecule
`task-20260726-8ba0`). The probe's job was to attempt `Firoozbakht.firoozbakht`.
It did not prove it — the conjecture is open since 1982 and the honest verdict
is `UNPROVABLE_IN_BUDGET`. What *can* be machine-checked, and is checked here,
is a precise statement of **how far the available tools fall short**, so that
"no proof was found" is backed by a theorem rather than by a paragraph.

Nothing in this file asserts or denies Firoozbakht's conjecture. It contains no
`sorry`, no `axiom`, no `native_decide`.

## What is proven here

Mathlib's strongest prime-gap result is **Bertrand's postulate**
(`Nat.exists_prime_lt_and_le_two_mul`): there is a prime in `(m, 2m]`. Ported to
this file's 1-indexed `p` (`bertrand_gap`), it gives

    p_{n+1} ≤ 2 * p_n .

Firoozbakht in Kourbatov's form (`F1'`) needs

    p_{n+1} < p_n ^ (1 + 1/n) .

So Bertrand can decide `F1' n` only if its ceiling `2 * p_n` sits at or below the
threshold `p_n ^ (1 + 1/n)`, i.e. only if `2 ^ n ≤ p_n`. Theorem
`bertrand_ceiling_above_threshold` shows the opposite holds at **every** `n ≥ 2`:
the ceiling is strictly *above* the threshold. The route is therefore closed at
every index but the first, not merely "hard" — and this is a theorem, not an
impression.

The mechanism is `p_lt_two_pow`: `p_n < 2 ^ n` for `n ≥ 2`, itself an induction
on Bertrand. The primes grow like `n log n`; the bound a constant-factor gap
theorem would need grows like `2 ^ n`. The required multiplicative slack
`p_n ^ (1/n) = exp((log p_n)/n) → 1`, while Bertrand supplies the constant `2`.

## What this does *not* say

- It does **not** say Firoozbakht is false, nor unprovable in principle. It says
  one specific route — the only prime-gap input Mathlib currently carries — cannot
  reach it.
- It says nothing about routes through bounds Mathlib does **not** have
  (Baker–Harman–Pintz `p^0.525`, RH-conditional `√p log p`, Cramér-type
  `(log p)²`). Those are unavailable in this substrate; the sibling analytic legs
  of round 2 examine them on paper and find the first two insufficient as well.
-/

import Firoozbakht.Statement
import Mathlib.NumberTheory.Bertrand

namespace Firoozbakht

/-- **Bertrand's postulate, in this file's 1-indexed convention.**
`p_{n+1} ≤ 2 * p_n`. This is the strongest prime-gap bound available in
Mathlib. -/
theorem bertrand_gap (n : ℕ) (hn : 1 ≤ n) : p (n + 1) ≤ 2 * p n := by
  obtain ⟨q, hq_prime, hq_lo, hq_hi⟩ :=
    Nat.exists_prime_lt_and_le_two_mul (p n) (by have := two_le_p n; omega)
  by_contra hcon
  simp only [Nat.not_le] at hcon
  -- `q` is a prime with `p n < q ≤ 2 * p n`, so `q` sits at index ≥ n, hence
  -- `p (n+1) = nth Prime n ≤ q ≤ 2 * p n`.
  have hlt : Nat.nth Nat.Prime (n - 1) < q := by simpa [p] using hq_lo
  have hidx : n - 1 < Nat.count Nat.Prime q :=
    (Nat.lt_nth_iff_count_lt infinite_setOf_prime).2 hlt
  have heq : Nat.nth Nat.Prime (Nat.count Nat.Prime q) = q := Nat.nth_count hq_prime
  have hmono : Nat.nth Nat.Prime n ≤ Nat.nth Nat.Prime (Nat.count Nat.Prime q) :=
    (Nat.nth_le_nth infinite_setOf_prime).2 (by omega)
  have hnth : p (n + 1) ≤ q := by rw [p_succ]; omega
  omega

/-- `p_n < 2 ^ n` for `n ≥ 2` — the primes never catch the exponential that a
constant-factor gap bound would need them to. Induction on `bertrand_gap`, base
case `p_2 = 3 < 4`. -/
theorem p_lt_two_pow (n : ℕ) (hn : 2 ≤ n) : p n < 2 ^ n := by
  induction n with
  | zero => omega
  | succ k ih =>
    rcases Nat.lt_or_ge k 2 with hk | hk
    · interval_cases k
      · omega
      · show p 2 < 2 ^ 2
        norm_num
    · have h1 : p (k + 1) ≤ 2 * p k := bertrand_gap k (by omega)
      have h2 : p k < 2 ^ k := ih hk
      calc p (k + 1) ≤ 2 * p k := h1
        _ < 2 * 2 ^ k := by omega
        _ = 2 ^ (k + 1) := by ring

/-- **The barrier.** At every `n ≥ 2`, the ceiling Bertrand's postulate provides
(`2 * p_n`) is strictly *above* the Firoozbakht threshold `p_n ^ (1 + 1/n)`. So
`bertrand_gap` cannot discharge `F1' n` — hence cannot discharge `Conjecture` —
at any index past the first.

This is the machine-checked content of the round-2 probe's
`UNPROVABLE_IN_BUDGET` verdict on the substrate side. -/
theorem bertrand_ceiling_above_threshold (n : ℕ) (hn : 2 ≤ n) :
    (p n : ℝ) ^ (1 + 1 / (n : ℝ)) < 2 * (p n : ℝ) := by
  have hp0 : (0 : ℝ) < (p n : ℝ) := by
    have := two_le_p n; exact_mod_cast lt_of_lt_of_le (by norm_num) this
  have hn0 : (0 : ℝ) < (n : ℝ) := by
    have : (0 : ℕ) < n := by omega
    exact_mod_cast this
  have hlt : (p n : ℝ) < (2 : ℝ) ^ (n : ℝ) := by
    have h := p_lt_two_pow n hn
    have hcast : ((p n : ℕ) : ℝ) < ((2 ^ n : ℕ) : ℝ) := by exact_mod_cast h
    simpa [Nat.cast_pow, Real.rpow_natCast] using hcast
  have hroot : (p n : ℝ) ^ (1 / (n : ℝ)) < 2 := by
    have hmono : (p n : ℝ) ^ (1 / (n : ℝ)) < ((2 : ℝ) ^ (n : ℝ)) ^ (1 / (n : ℝ)) :=
      Real.rpow_lt_rpow (le_of_lt hp0) hlt (by positivity)
    have hsimp : ((2 : ℝ) ^ (n : ℝ)) ^ (1 / (n : ℝ)) = 2 := by
      rw [← Real.rpow_mul (by norm_num : (0 : ℝ) ≤ 2), mul_one_div,
        div_self (ne_of_gt hn0), Real.rpow_one]
    rwa [hsimp] at hmono
  calc (p n : ℝ) ^ (1 + 1 / (n : ℝ))
      = (p n : ℝ) ^ (1 : ℝ) * (p n : ℝ) ^ (1 / (n : ℝ)) := by rw [← Real.rpow_add hp0]
    _ = (p n : ℝ) * (p n : ℝ) ^ (1 / (n : ℝ)) := by rw [Real.rpow_one]
    _ < (p n : ℝ) * 2 := by nlinarith [hroot, hp0]
    _ = 2 * (p n : ℝ) := by ring

end Firoozbakht
