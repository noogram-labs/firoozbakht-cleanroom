# L13 — `T_n < L_n²`, with exception set exactly `{1,…,7, 10}`

**Kind:** lemma (proved in-run; the effective input is at L0)
**Verdict:** **PROVEN**, in two halves — an unconditional analytic argument for `p_n ≥ 599`
(i.e. `n ≥ 109`), and an exhaustive finite check for `n < 109`.
**Rests on:** `dusart2010estimates` (L0) **Theorem 6.9**, eq. (6.5):
`(x/ln x)(1 + 1/ln x) ≤ π(x)` for `x ≥ 599`.
Plus an in-run exhaustive computation for `1 ≤ n ≤ 216 815`.

---

## Statement

```
T_n  <  L_n²      for every n ≥ 1  except  n ∈ {1, 2, 3, 4, 5, 6, 7, 10}.
```

At those eight indices, `T_n ≥ L_n²`.

## Proof

**Analytic half (`x = p_n ≥ 599`).** With `L = log x` and `n = π(x)` (**D3**):

`T_n = x(e^{L/n} − 1) < L²` ⟸ `L/n < log(1 + L²/x)`.

Since `log(1+u) ≥ u − u²/2`, it suffices that `L/n < L²/x − L⁴/(2x²)`, i.e.
`n > (x/L)·(1 − L²/(2x))^{-1}`, and a sufficient clean form is

```
π(x)  >  x/L  +  L .
```

Dusart Theorem 6.9 eq. (6.5) gives `π(x) ≥ x/L + x/L²` for `x ≥ 599`, and `x/L² > L` whenever
`x > L³` — which holds at `x = 599` (`L = 6.395`, `L³ = 261.6 < 599`) and, since `x/L³` is
increasing for `x > e³`, for every `x ≥ 599` thereafter. ∎

**Finite half (`n < 109`, i.e. `p_n < 599`).** Direct evaluation. `T_n ≥ L_n²` at exactly
`n ∈ {1,…,7, 10}` and `T_n < L_n²` at every other `n < 109`.

**Recomputed in this leg** (independently of `decompose` and of the panel): exception set
`[1, 2, 3, 4, 5, 6, 7, 10]`, and `p_109 = 599` exactly, so the two halves meet with no gap.

## Role in the proof-obligation tree

This card licenses the **direction** of the CSG implication in **D7**: a breach of `c_n ≥ 1`
implies a breach of `ρ_n ≥ 1` — i.e. the CSG criterion is *sufficient* for refutation, and
*harder to satisfy* than the true bar. Without `L13` that implication is unlicensed, and it is
easy to state backwards.

## Dependencies

**D3**, **D5**, **D7**, **T1**.

## Used by

**D7**, **T2**.

## Hazards — this card exists mostly to hold them

1. **The exception set is not an initial segment.** `n = 8` and `n = 9` **pass**; `n = 10`
   **fails**. So "for `n ≥ 11`" is a correct statement of the conclusion but **not** a monotone
   crossing — an induction from a base case will look for the boundary in the wrong place.
   Four panelists computed the same set independently (`synthesis.md` §2 C5).
2. **`decompose` §4.3 asserts `T_n < L_n²` "at every `n ≥ 11` in range" and tags the CSG test
   `[decidable, sufficient]` without stating the exception set.** The tag is right, the
   justification is incomplete, and the missing exception set is where the error would live.
3. **Warrant and applicability are disjoint sets.** Over the range where this card's finite half
   is verified, `max c_n = 0.70257` — a CSG breach is impossible there. The criterion is verified
   exactly where it cannot fire, and is *used* exactly where it is unverified. The analytic half
   above is what repairs that, which is why it is stated in full rather than cited.
4. `T_n < L_n²` says the CSG bar is **above** the true bar. It does **not** say by how much; that
   is **L2**, and the gap is `≈ L + 1`.

## Declared gap

The analytic half is an in-run derivation. It is elementary and its only external input
(Dusart 6.9) is at L0, but **it has not been independently checked** and it should be re-derived
by the verification leg rather than trusted on sight.
