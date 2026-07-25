# T1 — Technique: effective `π(x)` and `p_k` bounds

**Kind:** technique (the analytic toolbox every effective card consumes)
**Verdict:** **PROVEN** — every bound below is read at a numbered locator in an L0 source, except
the Axler corollaries, which are **L2_strong and unopened**.
**Rests on:**
- `dusart2010estimates` (L0) — arXiv:1002.0442, read in full:
  - **Thm 6.9, eq. (6.5):** `(x/ln x)(1 + 1/ln x) ≤ π(x)` for `x ≥ 599`;
    `π(x) ≤ (x/ln x)(1 + 1.2762/ln x)` for `x > 1`.
  - **Thm 6.9, eq. (6.6):** `x/(ln x − 1) ≤ π(x)` for `x ≥ 5393`;
    `π(x) ≤ x/(ln x − 1.1)` for `x ≥ 60184`.
  - **Prop. 6.6:** `p_k ≤ k(ln k + ln₂k − 1 + (ln₂k − 2)/ln k)` for `k ≥ 688383`.
  - **Prop. 6.7:** `p_k ≥ k(ln k + ln₂k − 1 + (ln₂k − 2.1)/ln k)` for `k ≥ 3`.
  - **Prop. 6.8:** for all `x ≥ 396738` there is a prime `p` with `x < p ≤ x(1 + 1/(25 ln²x))`.
- `axler2014newbounds` (**L2_strong, NOT OPENED**), quoted through Kourbatov's proofs:
  - **Cor. 3.6:** `x/(log x − 1 − 1/log x − 1/log²x) < π(x)` for `x ≥ 1772201`.
  - **Cor. 3.5:** `log x − 1 − 1.17/log x < x/π(x)` for `x ≥ 2634800823` (**range corrected by
    Axler's own corrigendum, from `x ≥ 5.43`**).
- `ferreira2017consequences` (L0) **Thm 4.4** — Rosser: `p_n > n ln n`; and
  `ln n + ln ln n − 1 < p_n/n < ln n + ln ln n` for `n ≥ 6`.

---

## What the technique is

Every effective statement in this attack has the same shape:

1. Start from the exact bar `T_n = p_n(p_n^{1/n} − 1)` (**D5**), whose only opaque ingredient is
   `n = π(p_n)` (**D3**).
2. Replace `n` with a two-sided effective bound on `π(p_n)`.
3. Track the validity range of that bound through the algebra.
4. Emerge with a statement in `L = log p_n` alone.

**Step 2 is the entire analytic content.** Steps 1, 3, 4 are bookkeeping — but step 3 is where the
mistakes live.

## Role in the proof-obligation tree

`T1` is the **shared dependency that the upstream tree draws as a leaf on one branch only**. It is
consumed by:

| consumer | what it needs from T1 |
|---|---|
| **L2** (threshold asymptotics) | Axler Cor. 3.5/3.6 |
| **L3** (necessary condition) | Axler Cor. 3.6 |
| **L4** (sufficient condition) | Axler Cor. 3.5 |
| **L6** (verification to `2⁶⁴`) | Dusart `π(x) ≤ x/(ln x − 1.1)`, `x ≥ 60184` |
| **L13** (`T_n < L_n²`) | Dusart eq. (6.5), `x ≥ 599` |
| **L14** (bridge to the primes, unbuilt) | Dusart Prop. 6.6/6.7 |
| **L15** (P6′, open) | Dusart, to bound `T`'s oscillation |
| **L16** (refutation certificate) | any lower bound on `π(p_n)` |

Note that this list spans **both branches**. `decompose` §2 places effectivity as a leaf on the
proof branch only; **L16** shows the refutation branch needs it too, and **L13** shows a
falsifiability test does.

## Dependencies

**D3**.

## Used by

**L2**, **L3**, **L4**, **L6**, **L13**, **L14**, **L15**, **L16**, **T2**, **T3**.

## Hazards

1. **A validity range is part of a bound.** `x ≥ 599`, `x ≥ 5393`, `x ≥ 60184`, `x ≥ 396738`,
   `k ≥ 688383`, `x ≥ 1772201`, `x ≥ 2634800823`. Dropping one turns a theorem into a guess. The
   Axler corrigendum is the cautionary case: a range moved by **nine orders of magnitude**, and
   Kourbatov had to issue a corrigendum of his own to propagate it.
2. **The Axler corollaries were never opened in this run.** They sit beneath Kourbatov's Theorems
   1, 3 and 5 — i.e. beneath **L2**, **L3** and **L4**, three of the most load-bearing cards in
   the set. **Priority 1 for the citation gate.** (`source-ledger.md` §6.3, §7.1.)
3. **The 2018 Dusart is sharper and was not fetched.** *"Explicit estimates of some functions over
   primes"*, *Ramanujan J.* **45** (2018), 227–251, DOI `10.1007/s11139-016-9839-4` — the one open
   copy found served an expired TLS certificate and was not bypassed. Recorded as a pointer, not a
   ledger row. If sharper constants are ever needed, this is where to go first.
   (`source-ledger.md` §2.6 note, §6.6.)
4. **Do not mix Dusart's and Axler's bounds inside one derivation without re-checking the
   intersection of their ranges.**

## Declared gap

The most consequential unopened source in the run sits inside this card.
