# L4 — Sufficient condition: `g_k < log²p_k − log p_k − 1.17` for `k > 9` implies `F`

**Kind:** lemma (published; the converse direction of **L3**)
**Verdict:** **PROVEN.** Read at the locator.
**Rests on:**
- `kourbatov2015bounds` (L0) §4 **Theorem 3**, verbatim: *"If `p_{k+1} − p_k < log²p_k − log p_k
  − 1.17` for all `k > 9` (`p_k ≥ 29`), then Firoozbakht's conjecture (1) is true."*
- `kourbatov2015bounds` (L0) §4 **Theorem 4** — three further sufficient conditions with
  `b → 1`, e.g. `g_k < log²p_k − log p_k − 1 − 3.83/log p_k`, each assumed for all
  `p_k > 4·10¹⁸`.
- `visser2019verifying` (L0) §1 eq. (1.3) — independent restatement of the same criterion
  (`g_n ≤ ln²p_n − ln p_n − 1.17`, `n ≥ 10`, `p_n ≥ 29`).
- `ferreira2017consequences` (L0) **Theorem 2.3** — restatement **without proof**
  ("we refer the reader to [15]"). *Not* independent corroboration.

---

## Statement

```
[  g_k < L_k² − L_k − 1.17   for all k > 9  (p_k ≥ 29)  ]   ⟹   F
```

and a family approaching the necessary condition:

```
[  g_k < L_k² − L_k − 1 − 3.83/L_k   for all p_k > 4·10¹⁸  ]  ⟹   F   (modulo the finite check below)
```

## Role in the proof-obligation tree

**L3** and **L4** together *sandwich* `F` between two gap bounds:

```
        g_k < L² − L − 1.17         ⟹     F     ⟹      g_k < L² − L − 1
        └──── sufficient (L4) ────┘         └──── necessary (L3) ────┘
```

The two differ by `0.17`, and Theorem 4 narrows that to `3.83/L`, which at `L ≈ 35` is `0.109`.
So **`F` is, to within an additive `O(1/L)`, exactly the Cramér-scale gap bound
`g_n < log²p_n − log p_n − 1`.** That identification is the reason this problem is genuinely a
prime-gap problem and not a curiosity about roots.

This card also **closes an open hole the `decompose` leg declared**: its §7 A4 said
"converse-direction gap criteria implying Firoozbakht — do not build on until sourced". They are
sourced. (`source-ledger.md` §4.4.)

## Dependencies

**D2**, **D4**, **D5**, **L1**, **L2**, **T1**.

## Used by

**L6** (Kourbatov's verification is exactly this criterion, run over a first-occurrence gap
table), **T2**, **T5**.

## Hazards

1. **The hypothesis is a universally quantified statement over all `k > 9`.** It is not something
   a finite computation can establish. **L4** converts one open problem into another open problem
   of the same shape and difficulty — its value is that the new shape is the one the gap
   literature speaks. It is **not** a route to a proof by itself.
2. **`p_k ≥ 29` and `k > 9` are both in the hypothesis.** Dropping either invalidates it.
3. **Theorem 4's family is conditional on `p_k > 4·10¹⁸`** — i.e. it presupposes the finite
   verification (**L6**) below that point. A paper quoting Theorem 4 without **L6** has an
   unstated hypothesis.
4. **Single-threaded provenance, and it matters more here than anywhere.** Theorem 3 rests on
   Axler's **Corollary 3.5** — the corollary whose range of validity Axler's own corrigendum moved
   from `x ≥ 5.43` to `x ≥ 2 634 800 823`. Kourbatov's §7 Corrigendum propagates that fix through
   Theorem 3. Cite **arXiv v4 only**. Axler was **not opened in this run**; this is Priority 1 for
   the citation gate. (`source-ledger.md` §4.4, §6.3, §7.1.)
5. Ferreira–Mariano Theorem 2.3 looks like a second source and is not one. Visser eq. (1.3) *is* a
   second statement, but Visser is also restating Kourbatov rather than reproving him.

## Declared gap

The sufficient-condition chain is **single-author and single-source beneath the top layer**. This
run established the statements; it did not establish independence.
