# `unproved-2` — the still-`sorry`'d theorems after round 2

**Molecule:** `task-20260726-8ba0` (leg `lean-probe`, round 2)
**Source of truth:** `lake env lean audit_exhaustive.lean`, run on the committed
tree. Not a hand-maintained list — the audit walks the environment.

```
declarations scanned: 63
depending on sorryAx: [Firoozbakht.firoozbakht]
```

## The list — one entry

| Declaration | Location | Status | Attempted this round? |
|---|---|---|---|
| `Firoozbakht.firoozbakht : Conjecture` | `lean/Firoozbakht/Statement.lean:186` (theorem on line 185) | **UNPROVABLE_IN_BUDGET** — open problem since 1982 | **Yes.** Round 1 declined to attempt it; round 2 attempted it and failed. |

`Conjecture` unfolds to `∀ n : ℕ, 1 ≤ n → p (n+1) ^ n < p n ^ (n+1)` (form `F3`,
the primary arithmetic form; equivalent to the three other forms by the
kernel-checked chain in `Equivalence.lean`).

## Statement of what "unproved" means here

`UNPROVABLE_IN_BUDGET` = **no proof was found**. It is not a claim that the
conjecture is false, and not a claim that it is unprovable in principle.
Firoozbakht's conjecture is `Π₁`: a proof must cover all `n`, whereas a single
certified counterexample index refutes it. The refutation shape is
`refuted_of_witness`, which *is* proven (no `sorry`) — so the development can
express a refutation without a second `sorry`-ed theorem.

## What was tried, and what stopped it

| Route | Stopped by |
|---|---|
| `exact?` on the target | no matching lemma in Mathlib (`could not close the goal`) |
| `aesop` on the target | `made no progress` |
| `decide` on the single case `F3 1` | `Nat.nth` is `noncomputable` — no kernel reduction (card `T4` Fact 1) |
| Bertrand's postulate (`p_{n+1} ≤ 2 p_n`) | **provably insufficient at every `n ≥ 2`** — `Firoozbakht.bertrand_ceiling_above_threshold` proves Bertrand's ceiling sits strictly *above* the Firoozbakht threshold `p_n^(1+1/n)` |
| BHP `p^0.525`, RH-conditional `√p log p`, Cramér `(log p)²` | not formalized in Mathlib; and the first two are shown insufficient on paper by this round's `proof-attempt-RH-conditional-bound.md` (Theorems B, C) |

## The missing input, named precisely

A Cramér-strength prime-gap bound: `g_n < p_n^{1+1/n} - p_n ≈ (log p_n)²`. No
such unconditional theorem exists in the literature — this is exactly the content
of the open problem, not a formalization shortfall. **Even a complete
formalization of every published prime-gap bound, unconditional or
RH-conditional, would not discharge this `sorry`.**

## Not on this list, and why

Round 1's `unproved-1` had the same single entry. Nothing regressed and nothing
new became `sorry`'d: the three theorems round 2 added
(`bertrand_gap`, `p_lt_two_pow`, `bertrand_ceiling_above_threshold`, in the new
`Firoozbakht/Barrier.lean`) are all `sorry`-free, confirmed by
`lake env lean audit.lean` showing `[propext, Classical.choice, Quot.sound]` for
each.

The audit detector was re-tested against a planted `sorry` in the enlarged tree
(scanned 64, two names reported), then the plant was deleted — the list above is
produced by a detector demonstrated to fire.
