# L2 — Asymptotics of the threshold (Kourbatov, Theorem 5)

**Kind:** lemma (published; supersedes the in-run "Claim A")
**Verdict:** **PROVEN** — published, read at the locator, with an **effective** two-sided form.
**Rests on:** `kourbatov2015bounds` (L0), §5 Appendix, **Theorem 5**:
`f_k := p_k^{1+1/k} − p_k = log² p_k − log p_k − 1 + o(1)` as `k → ∞`; and the explicit bracket
recorded in the same row's §4 Theorem 4 family,
`log²p_k − log p_k − 1 − 3.83/log p_k < f_k < log²p_k − log p_k − 1`.
Underneath it: `axler2014newbounds` (**L2_strong, NOT OPENED**) Corollaries 3.5/3.6.

---

## Statement

With `L = L_n = log p_n` and `T_n = f_n` as in **D5**:

```
T_n  =  L² − L − 1 + o(1)          (k → ∞)

and, effectively:

L² − L − 1 − 3.83/L   <   T_n   <   L² − L − 1
```

An in-run expansion refines the middle term: `T_n = L² − L − 1 − 3/L + O(1/L²)`, which sits
inside the published bracket and identifies the leading correction's sign and coefficient.

**Honest check of the refinement, recomputed in this leg** (sieve to `3·10⁶`, so `L ≤ 14.9` —
too small for an asymptotic to be decisive, which is itself the finding):

| `n` | `p_n` | `T_n` (exact) | `L²−L−1` | `L²−L−1−3/L` |
|---|---|---|---|---|
| 10 000 | 104 729 | 121.1276 | 121.0544 | 120.7949 |
| 100 000 | 1 299 709 | 182.9814 | 183.1026 | 182.8895 |
| 216 815 | 2 999 957 | 206.3659 | 206.5165 | 206.3154 |

The `−3/L` correction halves the residual at the two larger checkpoints and **worsens it** at
`n = 10⁴`. That is the expected behaviour of an `O(1/L²)` remainder at `L ≈ 11.6`, but it means
**the in-run data does not confirm the coefficient `3`** — it is consistent with it, no more.
Treat `−3/L` as a refinement to be checked, and the published bracket as the citable fact.

## Role in the proof-obligation tree

`L2` is the **translation layer**. It converts the exact but opaque bar `T_n` (**D5**) into a
function of `L` alone, which is what makes the gap literature (**L11**, **L12**) and the Cramér
apparatus (**L9**, **L10**) comparable to Firoozbakht at all. Both **L3** and **L4** are
statements in the translated coordinates.

## Dependencies

**D3** (`n = π(p_n)` — the substitution of an effective `π` estimate *is* the proof),
**D5**, **T1** (effective `π(x)` bounds).

## Used by

**L3**, **L4**, **L7**, **L10**, **L13**, **D7**.

## Correction this card forces on the upstream `decompose` leg

`decompose` §1.3 presents `T_n = L² − L − 1 + O(1/L)` as an in-run derivation and declares in §8.3
that "Claim A's `O(1/L)` is not made effective" — listing it as an open gap. **It is not open.**
It is Kourbatov's Theorem 5, published in 2015, and the error term is explicit. Do not re-derive;
cite. (`source-ledger.md` §4.3.)

## Consequence for the "5% margin" argument

The `o(1)` slack at the size of the record (`L = 35.0654`) is, in `g/L²` units,
`(3/L)/L² = 6.96·10⁻⁵` — roughly **750× smaller** than the ≈5.2% headroom of **D7**. Even the
crude published bracket width `3.83/L` gives `8.9·10⁻⁵`, still ~580× smaller. Therefore:

> **The 5% margin is anchor-limited, not analysis-limited.** Sharper asymptotics will not move it;
> only a better empirical record (or a better ceiling) will. This inverts the priority the
> `decompose` leg set. (`synthesis.md` §3 D1.)

## Hazards

1. **The whole chain is single-threaded under one author and one unopened source.** Kourbatov's
   Theorems 1, 3 and 5 all consume Axler's Corollaries 3.5/3.6, which were **not fetched** in this
   run — and Axler's own corrigendum moved Corollary 3.5's range of validity from `x ≥ 5.43` to
   `x ≥ 2 634 800 823`, nine orders of magnitude. `ferreira2017consequences` Theorems 2.2/2.3
   restate Kourbatov's results but carry no independent proof ("we refer the reader to [15]"), so
   they are **not corroboration**. **Priority 1 for the citation gate.** (`source-ledger.md` §6.3,
   §7.1.)
2. **Do not use the asymptotic form at small `p`.** See **D5** hazard 1: the surrogate understates
   `T_n` by 16% at `p = 113`.
3. Cite **arXiv v4** of `kourbatov2015bounds`, never v1–v3 — v4 carries the §7 Corrigendum that
   propagates Axler's range fix through Theorem 3.
4. **The two-sided bracket's locator is softer than Theorem 5's.** Theorem 5 (the `o(1)` form) was
   read at its numbered locator. The explicit bracket `−3.83/L < … < 0` is recorded in
   `source-ledger.md` §4.3 as the paper's error term, while the ledger's own §2 row locates
   `3.83/log p_k` inside **Theorem 4**, where it appears as a *sufficient condition* assumed for
   `p_k > 4·10¹⁸`, not as a proved bound on `f_k`. These are different statements. **Before the
   final paper quotes the bracket, re-open Kourbatov §4–§5 and confirm which theorem it lives
   in.** Flagged for the citation gate as a locator-precision item.

## Declared gap

`axler2014newbounds` is at L2_strong and unopened. Every effective statement on this card is
therefore quoted *through* Kourbatov. If the final paper reproves anything in this chain, Axler
must be fetched to L0 first.
