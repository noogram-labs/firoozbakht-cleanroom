/-
# Finite verification — and the fidelity check on the indexing

Two jobs, in order of importance.

**Job 1 (the real one): show the statement in `Statement.lean` is the
conjecture and not its 0-indexed weakening.** A wrong statement makes every
downstream proof meaningless (card `D1`).

**Job 2: a genuine (tiny) finite verification.** The conjecture holds for
`1 ≤ n ≤ 4`.

The range is `4`, not `10⁴`, and that is not modesty — it is card `T4` Fact 1.
`Nat.nth` is `noncomputable`; there is **no kernel reduction at all**, so
`decide` cannot produce `p n`. The only values of `p n` this project can name
are the ones Mathlib's five `@[simp]` base lemmas give: `p 1 .. p 5`. Extending
the range requires building `Nat.count`/`Nat.nth` bridging machinery with
per-`n` cost linear in `p_n` — real work, budgeted to a later leg, not done
here. Reporting a larger `N` without that machinery would be a fabrication.

## How *not* to write the fidelity check — two traps, both hit in drafting

**Trap 1: `F3 1 ↔ 3 ^ 1 < 2 ^ 2` proves nothing.** `simp` closes it by
evaluating *both sides to `True`*. The identical tactic closes
`F3 1 ↔ (999999 : ℕ) < 1000000` — checked, and it does. An `Iff` between two
true propositions carries no information about which primes appear.

**Trap 2: a *negative* control cannot live at the level of propositions
either.** `¬ (F3 1 = (5 ^ 1 < 3 ^ 2))` is *false*: both sides are true
propositions, and `propext` makes them equal. Lean says so if you try.

The check that does work has two halves:

- **Positive**, at the level of propositions but discharged by *rewriting only*
  (`simp only` with the `p_*` lemmas — no `decide`, no `norm_num`, no truth
  evaluation): the goal closes by substituting `p 2 ↦ 3`, `p 1 ↦ 2`, so the
  numerals written on the right are forced to be the ones the statement
  actually names. Under the 0-indexed reading the rewrite would produce `5`
  where `3` is written, and the goal would not close.
- **Negative**, at the level of *numbers*, where propositional extensionality
  has no purchase: `p 1 ≠ Nat.nth Nat.Prime 1`.
-/

import Firoozbakht.Statement
import Mathlib.Tactic.IntervalCases

namespace Firoozbakht

/-! ## Job 1a — positive: the cases unfold to the right numerals

Proved by rewriting alone. -/

/-- `n = 1`: `p_2 ^ 1 < p_1 ^ 2`, i.e. `3 ^ 1 < 2 ^ 2`. **This is the case the
0-indexed mis-transcription drops entirely.** -/
example : F3 1 = ((3 : ℕ) ^ 1 < 2 ^ 2) := by
  simp only [F3, show (1 : ℕ) + 1 = 2 from rfl, p_one, p_two]

/-- `n = 2`: `p_3 ^ 2 < p_2 ^ 3`, i.e. `5 ^ 2 < 3 ^ 3` (`25 < 27`). This is the
**tightest** case in the verified range `1 ≤ n ≤ 4` — ratio `27/25 = 1.08`. -/
example : F3 2 = ((5 : ℕ) ^ 2 < 3 ^ 3) := by
  simp only [F3, show (2 : ℕ) + 1 = 3 from rfl, p_two, p_three]

/-- `n = 3`: `p_4 ^ 3 < p_3 ^ 4`, i.e. `7 ^ 3 < 5 ^ 4`. -/
example : F3 3 = ((7 : ℕ) ^ 3 < 5 ^ 4) := by
  simp only [F3, show (3 : ℕ) + 1 = 4 from rfl, p_three, p_four]

/-- `n = 4`: `p_5 ^ 4 < p_4 ^ 5`, i.e. `11 ^ 4 < 7 ^ 5` (`14641 < 16807`).
Absolute margin `2166`, but ratio `1.15` — looser than `n = 2`. -/
example : F3 4 = ((11 : ℕ) ^ 4 < 7 ^ 5) := by
  simp only [F3, show (4 : ℕ) + 1 = 5 from rfl, p_four, p_five]

/-! ## Job 1b — negative: the mis-transcription reads one step ahead -/

/-- The 0-indexed primitive at index `1` is `3`; this development's `p 1` is `2`.
Writing the conjecture against `Nat.nth Nat.Prime n` directly would therefore
have put a different prime in every position. -/
theorem p_ne_nth_same_index : p 1 ≠ Nat.nth Nat.Prime 1 := by
  simp [p_one, Nat.nth_prime_one_eq_three]

/-- The precise shift: the mis-transcription's index `k` is this development's
index `k + 1`. This *is* the off-by-one, stated as an identity. -/
theorem nth_eq_p_succ (k : ℕ) : Nat.nth Nat.Prime k = p (k + 1) := (p_succ k).symm

/-! ### What a truth-value check cannot see

Both families hold at every index anyone has checked, so **no amount of green
output distinguishes them**. That is why the off-by-one had to be caught at the
level of the statement (card `D1`), and why `p` carries the `- 1` once rather
than each use site carrying a correction. -/

/-! ## Job 2 — the conjecture holds for `1 ≤ n ≤ 4` -/

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
