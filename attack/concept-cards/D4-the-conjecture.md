# D4 — Firoozbakht's conjecture `F`

**Kind:** definition (the target object)
**Verdict:** **OPEN.** Not proven, not refuted. This card fixes the statement; it asserts
nothing about its truth.
**Rests on:**
- `firoozbakht1982unpublished` (L2_strong) — attribution and date only, never mathematical content.
- `ribenboim2004little` (L2_strong) — p. 185, the first printed appearance; **book not opened**.
- `kourbatov2015bounds` (L0) §1 eq. (1) — `p_{k+1} < (p_k)^{1+1/k}` for all `k ≥ 1`.
- `ferreira2017consequences` (L0) §1 — "the sequence `{ⁿ√p_n}` is strictly decreasing".
- `visser2019verifying` (L0) Conjecture 1 eq. (1.1) — the two most common versions.
- `sun2013sequence` (L0) §1 — `ⁿ√p_n > ⁿ⁺¹√p_{n+1}` for all `n ∈ Z⁺`, citing Ribenboim p. 185.

---

## Statement — four equivalent forms

**(F1) Real-analytic (as posed).**  `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`; i.e.
`n ↦ p_n^{1/n}` is strictly decreasing.

**(F2) Logarithmic.**  `n · log p_{n+1} < (n+1) · log p_n`; i.e. `n ↦ (log p_n)/n` is strictly
decreasing.

**(F3) Purely arithmetic — no reals, no logarithms.**  `p_{n+1}^{\,n} < p_n^{\,n+1}`.

**(F4) Gap form.**  `g_n < T_n`, with `T_n` as in **D5**.

**(F1′) Kourbatov's form.**  `p_{k+1} < (p_k)^{1+1/k}` — this is (F1) with both sides raised to
the power `n(n+1)/(n+1)`; it is what `kourbatov2015bounds` calls "(1)" and is the form all of
that paper's theorems are stated against.

Equivalence is **L1**.

## Role in the proof-obligation tree

The root. `F` is a **Π₁** sentence; `¬F` is **Σ₁**. See **L16** for what that asymmetry does and
does not buy.

## Dependencies

**D1**, **D2**.

## Used by

Everything.

## Why (F3) is the right primary definition

(F3) is a statement about natural numbers only. It needs no `Real.rpow`, no `Real.log`, no
analysis import, and it is decidable for each fixed `n`. Taking (F1) as primitive would drag
`rpow` monotonicity into every downstream proof for no gain. See **T4**.

## Hazards

1. **Strict vs non-strict.** `visser2019verifying` Conjecture 1 eq. (1.1) states the conjecture
   with **`≤`**: `(p_{n+1})^{1/(n+1)} ≤ (p_n)^{1/n}`. `ferreira2017consequences`,
   `sun2013sequence` and `kourbatov2015bounds` all state it **strictly**. The two differ only on
   the possibility of equality, which cannot occur for `n ≥ 2` (it would force
   `p_{n+1}^n = p_n^{n+1}`, impossible for distinct primes by unique factorisation), so the
   forms coincide — but a paper that quotes Visser's `≤` alongside Kourbatov's `<` without
   remarking on it looks careless. **State the strict form and note Visser's variant.**
   *(Equality is impossible at every `n ≥ 1`, not merely asymptotically: `p_{n+1}^n = p_n^{n+1}`
   with `p_n ≠ p_{n+1}` contradicts unique factorisation, since the two sides have disjoint
   prime supports. So `≤` and `<` define the same conjecture, with no exceptional index.)*
2. **The origin locator is second-hand.** Ribenboim p. 185 is attested by two independent L0
   citers (Kourbatov, Sun) but the book was not opened. Cite Kourbatov or Sun for the statement;
   cite Ribenboim only if the citation gate upgrades it. (`source-ledger.md` §6.1, §7.3)
3. Nothing here licenses "Firoozbakht is true" or "Firoozbakht is false." See the closing note of
   `source-ledger.md` §9.

## Declared gap

`ribenboim2004little` and `firoozbakht1982unpublished` are both below L0. The conjecture's
*origin* is therefore not established at first-hand in this run; its *statement* is, five times
over.
