/-
# Finite verification — and the fidelity check on the indexing

Two jobs, in order of importance.

**Job 1 (the real one): prove the statement in `Statement.lean` is the
conjecture and not its 0-indexed weakening.** A wrong statement makes every
downstream proof meaningless (card `D1`). The check is that the *first* case,
`n = 1`, reads `p_2 ^ 1 < p_1 ^ 2` i.e. `3 < 4` — the case the mis-transcription
silently drops — and that the numerals at `n = 1..4` are exactly the ones the
paper conjecture predicts. These are `example`s with the numerals written out,
so a reader can check them by eye and Lean checks them by kernel.

**Job 2: a genuine (tiny) finite verification.** `Firoozbakht` holds for
`1 ≤ n ≤ 4`.

The range is `4`, not `10⁴`, and that is not modesty — it is card `T4` Fact 1.
`Nat.nth` is `noncomputable`; there is **no kernel reduction at all**, so
`decide` cannot produce `p n`. The only values of `p n` this project can name
are the ones Mathlib's five `@[simp]` base lemmas give: `p 1 .. p 5`. Extending
the range requires building `Nat.count`/`Nat.nth` bridging machinery with
per-`n` cost linear in `p_n` — real work, budgeted to a later leg, not done
here. Reporting a larger `N` without that machinery would be a fabrication.
-/

import Firoozbakht.Statement
import Mathlib.Tactic.IntervalCases

namespace Firoozbakht

/-! ## Job 1 — the indexing fidelity check

Each `example` states the case with the *numerals* on both sides, so the
transcription can be verified by eye against the paper conjecture. -/

/-- `n = 1`: `p_2 ^ 1 < p_1 ^ 2`, i.e. `3 < 4`. **This is the case the
0-indexed mis-transcription drops entirely.** -/
example : F3 1 ↔ (3 : ℕ) ^ 1 < 2 ^ 2 := by simp [F3]

/-- `n = 2`: `p_3 ^ 2 < p_2 ^ 3`, i.e. `25 < 27`. -/
example : F3 2 ↔ (5 : ℕ) ^ 2 < 3 ^ 3 := by simp [F3]

/-- `n = 3`: `p_4 ^ 3 < p_3 ^ 4`, i.e. `343 < 625`. -/
example : F3 3 ↔ (7 : ℕ) ^ 3 < 5 ^ 4 := by simp [F3]

/-- `n = 4`: `p_5 ^ 4 < p_4 ^ 5`, i.e. `14641 < 16807`. This is the tightest of
the small cases — margin `2166`, about 13%. -/
example : F3 4 ↔ (11 : ℕ) ^ 4 < 7 ^ 5 := by simp [F3]

/-! ### The negative control

If the statement had been written 0-indexed against `Nat.nth Nat.Prime n`
directly, its `n = 1` case would have been `p_3 ^ 1 < p_2 ^ 2`, i.e. `5 < 9`:
a different inequality, between a different pair of primes, with a different
exponent ratio (`1 + 1/(m-1)` instead of `1 + 1/m`).

**The two cannot be told apart by truth value** — `3 < 4` and `5 < 9` are both
true, and so is every case of both families in the verified range. That is
exactly why the off-by-one is silent and must be caught at the level of the
*statement*, by naming the primes and exponents, rather than by any amount of
green output. The two `example`s below pin the two families to their numerals so
the difference is visible and kernel-checked. -/

/-- What this development's `n = 1` case actually says: primes `(3, 2)`,
exponents `(1, 2)`. -/
example : F3 1 ↔ (3 : ℕ) ^ 1 < 2 ^ 2 := by simp [F3]

/-- What the 0-indexed mis-transcription's `n = 1` case would have said: primes
`(5, 3)`, exponents `(1, 2)`. Different primes — one index too far along the
sequence. -/
example :
    ((Nat.nth Nat.Prime (1 + 1)) ^ 1 < (Nat.nth Nat.Prime 1) ^ (1 + 1))
      ↔ ((5 : ℕ) ^ 1 < 3 ^ 2) := by
  simp [Nat.nth_prime_two_eq_five, Nat.nth_prime_one_eq_three]

/-- The two families are shifted relative to one another: the mis-transcription
at index `k` speaks about the primes this development calls `p_{k+1}, p_{k+2}`.
Stated as an identity of the underlying primes, which is what the off-by-one
actually is. -/
example (k : ℕ) : Nat.nth Nat.Prime k = p (k + 1) := (p_succ k).symm

/-! ## Job 2 — Firoozbakht holds for `1 ≤ n ≤ 4` -/

theorem F3_one : F3 1 := by norm_num [F3]
theorem F3_two : F3 2 := by norm_num [F3]
theorem F3_three : F3 3 := by norm_num [F3]
theorem F3_four : F3 4 := by norm_num [F3]

/-- **Verified range.** Firoozbakht's conjecture holds for `1 ≤ n ≤ 4`.

Fully proven — no `sorry`. The bound `4` is set by Mathlib's five base
`nth_prime_*` lemmas (card `T4`, Fact 2), not by the size of the integers
(`p_51 ^ 52` has only 124 digits). -/
theorem firoozbakht_le_four : ∀ n : ℕ, 1 ≤ n → n ≤ 4 → F3 n := by
  intro n h1 h4
  interval_cases n <;>
    first
      | exact F3_one
      | exact F3_two
      | exact F3_three
      | exact F3_four

end Firoozbakht
