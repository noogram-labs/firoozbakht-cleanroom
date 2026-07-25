# D6 — The normalized ratio `ρ_n := g_n / T_n`

**Kind:** definition (the correct search objective)
**Verdict:** **PROVEN** — definitional; that `ρ_n ≥ 1` is *exactly* equivalent to a failure of `F`
at `n` follows from **L1**, with no error term and no index restriction.
**Rests on:** **D5** and **L1**; the ledger row behind the equivalence is
`visser2019verifying` (L0) Conjecture 3 eq. (2.4).

---

## Statement

```
ρ_n  :=  g_n / T_n                      (T_n as in D5)

F fails at n   ⟺   ρ_n ≥ 1.
```

This is an **exact** biconditional at every `n ≥ 1`. Contrast **D7**.

## Role in the proof-obligation tree

`ρ_n` is the objective function of the only computationally live route (counterexample search).
It is also the unit in which every "how close does the conjecture come to failing?" statement
should be expressed, because it is the unit in which the failure threshold is exactly `1`.

## Dependencies

**D2**, **D5**, **L1**.

## Used by

**T2** (search design), **L7** (the record, converted into this unit), **L15**.

## Why `ρ`, and not gap size, and not `g_n/L²`

- **Not gap size.** `ρ` weights by roughly `log²p`, so a moderate gap at a small prime can beat a
  huge gap at a large prime. In-run, the maximum is `ρ = 0.76047` at `p_217 = 1327` (gap 34),
  narrowly ahead of `ρ = 0.75910` at `p_149689 = 2 010 733` (gap 148) — three orders of magnitude
  apart in `p`, essentially tied in `ρ`.
- **Not `g_n/L²`.** That is **D7**, and it sets the bar too high by `O(L)`. Using it as the search
  objective can step straight over a genuine counterexample.

## Verified in-run

Sieve to `3·10⁶` (216 816 primes, 216 815 consecutive pairs):

| Quantity | Value |
|---|---|
| Violations of `F` (`ρ_n ≥ 1`) | **none**, `1 ≤ n ≤ 216 815` |
| `max ρ_n` for `n ≥ 10` | **0.7604709** at `n = 217`, `p_n = 1327`, `g = 34` |
| runner-up | `0.759` at `n = 149 689`, `p_n = 2 010 733`, `g = 148` |

Independently reproduced in this leg (not merely copied from `decompose` §5.1).

## Hazards

1. **The `F2`-margin statistic is not a substitute.** `decompose` §5.1 reports
   `max n·log p_{n+1} / ((n+1)·log p_n) = 0.9999984`. That quantity's distance from 1 scales like
   `(1−ρ_n)/n`, so it approaches 1 for *arithmetic* reasons as the sieve extends — it would read
   `0.9999984` in a universe where every gap were 2. A leg that extends the sieve and reports
   `0.9999999…` as "the conjecture tightening" has measured `1/n`. `ρ_n` has `O(1)` operands and
   no such artifact. (`synthesis.md` §2 C10.)
2. **Double precision.** `ρ_n` is safe far past `3·10⁶`, but the `F2` margin above dies at
   `p ≈ 2·10¹⁵` — *below* the published frontier of `2⁶⁴` (**L6**). The failure is silent in the
   verification direction. See **T2**.

## Declared gap

None.
