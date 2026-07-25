# L3 — Necessary condition: `F ⟹ g_k < log²p_k − log p_k − 1` for `k > 9`

**Kind:** lemma (published, one-directional)
**Verdict:** **PROVEN.** Read at the locator.
**Rests on:**
- `kourbatov2015bounds` (L0) §2 **Theorem 1**, verbatim: *"If conjecture (1) is true, then
  `p_{k+1} − p_k < log² p_k − log p_k − 1` for all `k > 9`."*
- `ferreira2017consequences` (L0) **Theorem 2.2**, verbatim: *"If the Firoozbakht's conjecture is
  true, then `g_n < ln²(p_n) − ln(p_n) − 1, ∀ n ≥ 10`. In particular,
  `g_n < ln²(p_n) − ln(p_n), ∀ n ≥ 5`, and `limsup_{n→∞} g_n/ln²(p_n) ≤ 1`."*
- `sun2013sequence` (L0) §1 — the weaker `+1` variant:
  *"This implies the inequality `p_{n+1} − p_n < log²p_n − log p_n + 1` for large n."*
- `oeis_A111943` (L0) `%C` (Kourbatov, 28 Jan 2016) — the **sharper** form:
  *"Firoozbakht's conjecture implies that the ratio is below `1 − 1/log(p)` for all primes
  `p ≥ 11`."*

---

## Statement

```
F  ⟹  g_k  <  L_k² − L_k − 1          for all k > 9        (Kourbatov Thm 1)
F  ⟹  g_n  <  L_n² − L_n              for all n ≥ 5        (Ferreira–Mariano Thm 2.2)
F  ⟹  limsup_{n→∞}  g_n / L_n²  ≤  1                       (Ferreira–Mariano Thm 2.2)
F  ⟹  c_n = g_n/L_n²  <  1 − 1/L_n    for all p_n ≥ 11     (Kourbatov, OEIS A111943)
```

## Role in the proof-obligation tree

This is the **load-bearing obstruction**, and the single most consequential card in the set.
It says: *any proof of `F` yields, as a corollary, an unconditional `O(log² p)` bound on prime
gaps.* That bound is far beyond what is currently provable — see **L11**. Every "direct proof"
strategy must say how it clears this gate, or it is proposing something the field does not know
how to do.

It is also the bridge to the refutation side: combined with **L10** it produces the tension that
is the honest headline of this whole attack.

## Dependencies

**D2**, **D4**, **D5**, **L1**, **L2**, **T1** (the proof consumes Axler's `π(x)` bounds).

## Used by

**D7** (the direction of the CSG implication), **L10** (the contradiction with Granville),
**L11**, **L12**, **T2**, **T4** (the Lean L6 node).

## Hazards

1. **One-directional. Do not use as an equivalence.** The converse is a *different* theorem with
   a *different* constant — see **L4**. `kourbatov2015bounds` §3 makes the asymmetry concrete with
   a worked illustration at `p_k = 2 010 733`, where the gap bound holds and a prime
   `q = 2 010 929` lies in the interval that the conjecture itself would have to exclude.
2. **The `k > 9` threshold is part of the statement.** It is real, not decorative, and it is
   stated 1-indexed. Under Mathlib's 0-indexing (**D1**) it becomes `k > 8`. This is exactly where
   the off-by-one does its damage.
3. **Sun's variant is `+1`, i.e. weaker than Kourbatov's `−1`.** Both are correct; quoting Sun
   where the argument needs Kourbatov's sharpness would silently loosen the bound by 2.
4. **The provenance is single-threaded.** Ferreira–Mariano Theorem 2.2 is proved
   *"(Following [15])"* = Kourbatov. It is a restatement, not independent corroboration. Beneath
   both sits Axler's Corollary 3.6, unopened. See **L2** hazard 1.
5. `limsup ≤ 1` is an *asymptotic* consequence. No finite computation bears on it, in either
   direction. See **D7** hazard 4.

## Declared gap

Same as **L2**: the effective `π(x)` input (`axler2014newbounds`) was never opened.
