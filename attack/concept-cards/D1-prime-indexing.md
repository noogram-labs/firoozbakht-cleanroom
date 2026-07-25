# D1 — The prime sequence and its indexing convention

**Kind:** definition (+ one load-bearing bridge lemma)
**Verdict:** **PROVEN** — the definition is a definition; the Mathlib offset is read at an L0 locator.
**Rests on:** `mathlib_nat_prime_nth` (L0) — `Mathlib.Data.Nat.Prime.Nth`, the five `@[simp]` base
lemmas, first of which is `Nat.nth_prime_zero_eq_two : nth Prime 0 = 2`.
Also `mathlib_nat_nth` (L0) for `noncomputable def Nat.nth`.

---

## Statement

Let `p_n` denote the `n`-th prime under the **1-indexed** convention of this attack:

```
p_1 = 2,  p_2 = 3,  p_3 = 5,  p_4 = 7,  …
```

Mathlib's primitive is **0-indexed**: `Nat.nth Nat.Prime 0 = 2`. The bridge is therefore

```
p_n  =  Nat.nth Nat.Prime (n − 1)        for n ≥ 1
```

equivalently `Nat.nth Nat.Prime k = p_{k+1}`.

## Role in the proof-obligation tree

Root-level. Every other card names `p_n`. The card exists as a separate object solely because
the offset is **the single highest-severity defect found in the whole run** and it lives here.

## Dependencies

None. This is a leaf.

## Used by

Every card. Directly and dangerously by **T4** (Lean substrate) and by every card carrying an
index threshold: **L3** (`k > 9`), **L4** (`k > 9`), **L5**, **L8** (`n > 4`), **L13**
(`n ∈ {1..7,10}`), **T5** (`n ≥ 3645`).

## Why it is load-bearing

The upstream `decompose` §6 proposed the Lean statement

```lean
Firoozbakht : Prop := ∀ n ≥ 1, (p (n+1))^n < (p n)^(n+1)   with  p n := Nat.nth Nat.Prime n
```

With `p n = p_{n+1}` in this document's notation, substituting `m := n+1` turns that into
`p_{m+1}^{m−1} < p_m^{m}` — an exponent ratio of `1 + 1/(m−1)` where Firoozbakht needs
`1 + 1/m`. Since `1 + 1/(m−1) > 1 + 1/m`, **the proposition as written is strictly weaker than
Firoozbakht**, and it silently drops the case `m = 1`. A Lean development could go fully green
having formalized a different conjecture.

Two panelists (godel, knuth) found this independently with matching algebra
(`frame-deliberation/synthesis.md` §2 C1); the source ledger reached it a third way, from the
Mathlib docs (`source-ledger.md` §4.8).

## Hazards

1. **Every index threshold in the literature is stated 1-indexed.** `k > 9`, `n ≥ 10`, `n ≥ 5`,
   `n > 4`, `n ≥ 3645`, `p_k ≥ 29`. Fixing the offset once, in the statement file, is the only
   safe discipline; fixing it per-use guarantees a miss.
2. The `[needs-anchor]` tag that `decompose` §6 attached to the Lean plan was scoped to API
   *names*. This is *semantics*. It survives any name check, and `lean-probe` will not catch it
   unless told to look.
3. `Nat.nth` is **`noncomputable`** — see **T4**. That is a separate problem from the offset and
   must not be conflated with it.

## Declared gap

None. Both halves (the convention, the Mathlib offset) are settled.
