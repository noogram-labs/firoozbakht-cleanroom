# T3 — Technique: certifying the index `n` of a candidate counterexample

**Kind:** technique
**Verdict:** **PROVEN** that a *lower* bound suffices (**L16** (c)); the cost model below is
standard and **not sourced in this run**.
**Rests on:** **L16**, **T1**, **D3**, **D5**. `dusart2010estimates` (L0) Thm 6.9 is the concrete
tool.

---

## The problem

A refutation of `F` at `n` needs `π(p_n) = n` (**D3**). Primality has succinct certificates;
primality **rank** does not. Three ways to get the rank, in increasing order of cleverness:

| method | cost | gives |
|---|---|---|
| exhaustive sieve to `p_n` | `Õ(p_n)` time, segmented for memory | exact `n` |
| Meissel–Lehmer / Lagarias–Miller–Odlyzko combinatorial `π(x)` | `Õ(x^{2/3})` | exact `n` |
| **effective `π(x)` lower bound (T1)** | `O(1)` arithmetic | **a certified `N ≤ n`** |

## Why the third row is enough

`T_n` is strictly decreasing in `n` at fixed `p_n` (**D5**), so understating the index *raises*
the bar:

```
N ≤ π(p_n)   ⟹   T_N ≥ T_n   ⟹   [ g_n ≥ T_N  ⟹  F fails at n ].
```

**A candidate that clears the bar computed from a certified lower bound on its rank is a genuine
refutation**, with no sieve and no `π(x)` computation at all. Concretely, from Dusart Thm 6.9
eq. (6.5), for `p_n ≥ 599`:

```
N := ⌈ (p_n/L)(1 + 1/L) ⌉   satisfies   N ≤ π(p_n) = n.
```

This is a one-line, fully rigorous certificate. It is *conservative* — the bar it produces is
slightly higher than the true bar — which is exactly the right direction for a refutation claim.

## The symmetric warning

**Verification needs the opposite bound.** To *confirm* `F` at `n` one must show `g_n < T_n`, and
`T_n` shrinks as `n` grows — so a certified **upper** bound `M ≥ π(p_n)` is what is needed, giving
`T_M ≤ T_n` and hence `g_n < T_M ⟹ g_n < T_n`. Dusart's upper bounds on `π(x)` supply that (eq.
(6.5) upper half, `x > 1`; eq. (6.6) upper half, `x ≥ 60184`).

So: **refutation consumes a lower bound on the rank; verification consumes an upper bound.** They
are different inequalities with different validity ranges, and interchanging them silently
produces a claim in the unsafe direction. This is the same asymmetry that **L16** identifies, seen
from the computational side.

*(Note that `π(x)` is an integer, so a real lower bound `B` may be rounded **up**: `π(x) ≥ ⌈B⌉`.
Symmetrically an upper bound may be rounded **down**. Rounding the wrong way loses the
certificate.)*

## Role in the proof-obligation tree

`T3` is the edge from the refutation branch to the effective-`π` node (**T1**) that the upstream
tree does not draw. It is also what makes the Lean finite-verification node expensive (**T4**).

## Dependencies

**D3**, **D5**, **L16**, **T1**.

## Used by

**T2** (this is what makes a targeted search rigorous rather than suggestive), **T4**.

## Hazards

1. **Validity ranges.** The lower-bound formula above is valid for `p_n ≥ 599` only. Below that,
   enumerate.
2. **Do not report a candidate with an *estimated* index.** An overstated index lowers the bar and
   can manufacture an apparent counterexample. State which bound was used and in which direction.
3. **The cost figures in the table are unsourced.** `Õ(x^{2/3})` for combinatorial prime counting
   is standard, and this run has **no ledger row** for it. If the paper quotes a complexity, fetch
   a source.

## Declared gap

No source-ledger row for the prime-counting complexity results. The *mathematical* content of this
card (the direction argument) is self-contained and rests on **D5**, which is sourced.
