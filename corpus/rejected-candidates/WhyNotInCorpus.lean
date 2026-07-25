/-
# Near-misses that could NOT become corpus entries — and the proof of why

A red-team corpus for an **open** conjecture has a boundary that a corpus for a
settled theorem does not: a statement adjacent to `F` may be false, true, or
*exactly as open as `F` itself*. Only the first kind can be an entry. This file
holds the machine-checked reasons three attractive candidates were dropped.

Recording them matters as much as the entries do. A corpus that quietly omits
its rejects looks more complete than it is, and the next author re-derives the
same three dead ends.

Every declaration here **compiles with no `sorry`** — these are proofs *about*
the candidates, not attempts *at* them.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RejectedCandidates

open Firoozbakht

/-! ## Candidate R1 — `Conjecture` with the `1 ≤ n` guard dropped

    ∀ n : ℕ, F3 n

The obvious dropped-hypothesis attack, and it does not work: `F3` is **true** at
the junk index too. At `n = 0` it reads `(p 1)^0 < (p 0)^1`, i.e. `1 < 2`.

So the unguarded form is *equivalent* to `Conjecture` — refuting it would settle
Firoozbakht. Not an entry. -/
theorem R1_holds_at_zero : F3 0 := by
  simp only [F3, Nat.zero_add, pow_zero, pow_one, p_zero_eq_p_one, p_one]
  omega

/-- And therefore the unguarded form is equivalent to the guarded one: the
"attack" changes nothing at all. -/
theorem R1_equivalent_to_conjecture : (∀ n : ℕ, F3 n) ↔ Conjecture := by
  constructor
  · intro h n _; exact h n
  · intro h n
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · exact R1_holds_at_zero
    · exact h n hn

/-! ## Candidate R2 — `strict_iff_nonstrict` with the guard dropped

    ∀ n : ℕ, ((p (n+1))^n < (p n)^(n+1)) ↔ ((p (n+1))^n ≤ (p n)^(n+1))

Also not an entry, and for a sharper reason: it is **true**, provable, and the
guard in `Statement.lean` is not needed for it. At `n = 0` the two sides are
`1 < 2` and `1 ≤ 2`. Below is the proof, so the claim "the guard is decorative
here" is checked rather than asserted.

The guard on `p_pow_ne` *is* needed — its proof uses `p n < p (n+1)`. The guard
on this corollary is inherited, not required. -/
theorem R2_true_unguarded (n : ℕ) :
    ((p (n + 1)) ^ n < (p n) ^ (n + 1)) ↔ ((p (n + 1)) ^ n ≤ (p n) ^ (n + 1)) := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp only [pow_zero, p_zero_eq_p_one, p_one]
    omega
  · exact strict_iff_nonstrict n hn

/-! ## Candidate R3 — the negation-scope error

    (∃ n ≥ 1, ¬ F3 n)  ↔  (∀ n ≥ 1, ¬ F3 n)

"the conjecture fails somewhere" confused with "the conjecture fails
everywhere". The right-hand side is **provably false** (`F3 1` holds, proven
below by citing `FiniteCheck`), so the biconditional is equivalent to
`¬ (∃ n ≥ 1, ¬ F3 n)`, which is `Conjecture` in classical logic.

**Refuting this near-miss is therefore exactly as hard as proving Firoozbakht.**
It is the cleanest illustration of the boundary: quantifier-scope errors whose
subject is the open conjecture itself cannot be corpus entries. The corpus's
quantifier-order coverage (`F15`, `F16`, `F19`) is deliberately aimed at
statements whose subject is *decidable* — boundedness of the primes, the limit
of `p_n^(1/n)`, the position of a guard — never at `F` itself. -/
theorem R3_rhs_is_false : ¬ (∀ n : ℕ, 1 ≤ n → ¬ F3 n) := by
  intro h
  exact h 1 (by omega) F3_one

/-- And the biconditional collapses to the conjecture. Stated as an implication
*from* the near-miss, which is all that is needed to show refuting it is at
least as hard as proving `Conjecture` — and the implication itself is proven,
with no `sorry`. -/
theorem R3_implies_conjecture
    (h : (∃ n : ℕ, 1 ≤ n ∧ ¬ F3 n) ↔ (∀ n : ℕ, 1 ≤ n → ¬ F3 n)) : Conjecture := by
  intro n hn
  by_contra hc
  exact R3_rhs_is_false (h.mp ⟨n, hn, hc⟩)

/-! ## Candidate R4 — the 0-indexed weakening, claimed pointwise-equivalent

    ∀ m ≥ 1, ((nth Prime (m+1))^m < (nth Prime m)^(m+1)) ↔ F3 m

Card `D1` already says why this cannot be an entry, and says it better than a
Lean file could: **both families hold at every index anyone has checked**, so no
truth-value check distinguishes them. Refuting the pointwise equivalence would
require exhibiting an index where exactly one side fails — which means settling
`F` on at least one branch.

This is why `F02` exists and why it is the load-bearing entry: the separation
that *is* available is at the level of **numerals** (`nth Prime 1 = 3`,
`p 1 = 2`), not propositions. No declaration is needed here; the point is the
absence of one. -/

end Firoozbakht.RejectedCandidates
