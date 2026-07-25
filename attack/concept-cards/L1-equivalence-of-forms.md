# L1 — Equivalence of the four forms of `F`

**Kind:** lemma (elementary)
**Verdict:** **PROVEN.** Derived in full below; independently corroborated at two L0 locators.
**Rests on:**
- `kourbatov2015bounds` (L0) §1 eq. (1) — states `F ⟺ p_{k+1} < (p_k)^{1+1/k}`, i.e. the
  (F1) ⟺ (F1′) step.
- `visser2019verifying` (L0) Conjecture 1 eq. (1.1) — states (F1) ⟺ (F2) explicitly
  ("`(p_{n+1})^{1/(n+1)} ≤ (p_n)^{1/n}`; equivalently `ln p_{n+1}/(n+1) ≤ ln p_n/n`").
- `visser2019verifying` (L0) Conjecture 3 eq. (2.4) — states the gap form (F4).

---

## Statement

For every `n ≥ 1` the following are equivalent:

| | Form |
|---|---|
| **F1** | `p_{n+1}^{1/(n+1)} < p_n^{1/n}` |
| **F1′** | `p_{n+1} < p_n^{1+1/n}` |
| **F2** | `n · log p_{n+1} < (n+1) · log p_n` |
| **F3** | `p_{n+1}^{\,n} < p_n^{\,n+1}` |
| **F4** | `g_n < T_n` |

## Proof

All quantities are real and `> 1`.

- **F1 ⟺ F3.** `t ↦ t^{n(n+1)}` is strictly increasing on `(0,∞)`. Raising F1 to that power gives
  `p_{n+1}^{n} < p_n^{n+1}`; the map is a bijection of `(0,∞)` onto itself, so the step is
  reversible.
- **F3 ⟺ F2.** `log` is strictly increasing and both sides are positive; take logs.
- **F2 ⟺ F1′.** Divide F2 by `n`: `log p_{n+1} < (1 + 1/n) log p_n`, then exponentiate.
- **F1′ ⟺ F4.** `p_{n+1} < p_n^{1+1/n} = p_n + (p_n^{1+1/n} − p_n) = p_n + T_n`, i.e.
  `g_n = p_{n+1} − p_n < T_n`. ∎

## Role in the proof-obligation tree

This is the hinge of the entire attack. Without it, Firoozbakht is a curiosity about `n`-th
roots; with it, Firoozbakht **is a prime-gap bound**, and the whole analytic-number-theory
literature on gaps becomes admissible. Every obstruction card (**L11**, **L12**) and every
heuristic card (**L9**, **L10**) reaches the conjecture only through this equivalence.

## Dependencies

**D1**, **D2**, **D4**, **D5**.

## Used by

Every lemma card. In particular **L3**, **L4**, **L13**, **T2**, **T4** (Lean L2 node).

## Hazards

1. **F3 is the right *statement* and the wrong *bulk computation*.** At `n = 10⁵` both sides
   carry more than `6·10⁵` decimal digits. Large-range verification must use F2 with certified
   interval arithmetic on logarithms, or exact rational bounds on `log`. (Small `n` is fine:
   `p_51^52` has only 124 digits.)
2. **The equivalence is unconditional and index-free.** No `n ≥ n₀` appears anywhere in the
   proof. Any downstream statement that attaches a threshold to the *equivalence* (rather than to
   an asymptotic surrogate for `T_n`) has confused **L1** with **L2**.
3. Strict vs non-strict: see **D4** hazard 1. Equality never occurs, so the point is cosmetic.

## Declared gap

None. This card is fully discharged.
