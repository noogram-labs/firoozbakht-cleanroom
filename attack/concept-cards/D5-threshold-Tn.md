# D5 — The Firoozbakht threshold `T_n`

**Kind:** definition
**Verdict:** **PROVEN** as a definition, and **PROVEN** to be the exact bar (equivalence is **L1**).
Its *asymptotic size* is a separate card (**L2**).
**Rests on:**
- `visser2019verifying` (L0) Conjecture 3, eq. (2.4): Firoozbakht ⟺ `g_n ≤ p_n(p_n^{1/n} − 1)`
  for `n ≥ 1`.
- `kourbatov2015bounds` (L0) §5 Appendix Theorem 5, which names the same quantity
  `f_k := p_k^{1+1/k} − p_k`.

---

## Statement

```
T_n  :=  p_n · ( p_n^{1/n} − 1 )  =  p_n^{1+1/n} − p_n  =  p_n · ( e^{L_n/n} − 1 )
```

Kourbatov writes this `f_k`; Visser writes it inline. It is the same object.

Then (**L1**):  `F  ⟺  ∀ n ≥ 1,  g_n < T_n`.

## Role in the proof-obligation tree

`T_n` is **the bar**. Every strategy on the proof side tries to show `g_n` stays under it; every
strategy on the refutation side tries to push `g_n` over it. Both the necessary condition
(**L3**) and the sufficient condition (**L4**) are statements obtained by replacing `T_n` with an
explicit function of `L_n` alone.

## Dependencies

**D1**, **D2**, **D3** (`T_n` depends on `n = π(p_n)`, not on a free parameter).

## Used by

**D6**, **L1**, **L2**, **L3**, **L4**, **L13**, **L15**, **L16**, **T2**.

## Two structural facts about `T_n`, both verified in-run

1. **`T_n` is strictly decreasing in `n` at fixed `p_n`.** Immediate: `n ↦ p^{1/n}` is decreasing
   for `p > 1`. *Consequence:* understating the index raises the bar; overstating it lowers the
   bar. This is why **L16**'s certificate needs a *lower* bound on `π(p_n)`, and only a lower
   bound.
2. **`T` is not monotone along the sequence `n = 1, 2, 3, …`** — because `p` jumps by `g_n` while
   `n` increments by 1. Verified in this run: **`T_{n+1} < T_n` at 121 238 of 216 805 steps with
   `n ≥ 10` (55.92%)**, sieve to `3·10⁶`. This is a *discreteness* phenomenon and no smooth model
   reproduces it (see the hazard in **L14**). It is the reason **L15** (the maximal-gap
   reduction) is an obligation rather than a triviality.

## Hazards

1. **`T_n` is not `log²p_n`, and it is not `log²p_n − log p_n − 1` either.** Those are its
   asymptotics (**L2**). At small `n` the difference is large. Writing the substitution error as
   `T_n/(L²−L−1) − 1` (recomputed in this leg): **`+16.03%` at `p = 113`, `+2.744%` at
   `p = 1327`, `−0.0872%` at `p = 2 010 733`, `−0.0730%` at `p = 2 999 957`** — the surrogate
   *understates* `T_n` badly at small `p` and overshoots slightly past `~10⁶`. Five of the six
   numerically tightest cases below `3·10⁶` sit at `p < 5·10⁵`, i.e. squarely in the regime where
   the surrogate is wrong by more than the celebrated 5% margin. Any rhetoric about how "close" the conjecture
   comes to failing that is computed at small `p` with the asymptotic surrogate is measuring the
   surrogate.
   (`synthesis.md` §3 D1.)
2. **The 55.92% figure does not bear on the maximal-gap reduction.** It is a statement about
   single steps; the reduction needs `T_m ≤ T_n` for `m` the *governing record index*. See
   **L15** — that quantity has **zero** exceptions in the same range.
3. `decompose` §2.4 derives a rule ("`T` increases exactly when `g_n > L`") by substituting
   `n ≈ p/L` before differencing. The rule is order-dependent and the threshold is not `L`: the
   in-run misclassification rate is 7.07% at threshold `L`, 2.79% at `L−1`, **0.29% at `L−2`**.
   Since `n ≈ p/L` itself carries relative error `1/L ≈ 7%`, the derivation cannot resolve
   `L` from `L−2` at all. **Do not propagate the smooth rule; cite the discrete measurement.**
   (`synthesis.md` §3 D2.)

## Declared gap

None. The definition and the equivalence are settled; the asymptotics are deferred to **L2**,
whose effective form rests on an unopened source.
