# D2 — Prime gap `g_n` and the logarithm `L_n`

**Kind:** definition
**Verdict:** **PROVEN** — definitional; the notation matches the one used at L0 in
`kourbatov2015bounds`, `ferreira2017consequences` and `visser2019verifying`.
**Rests on:** `kourbatov2015bounds` (L0) §2 Theorem 1, which writes the gap as
`p_{k+1} − p_k`; `ferreira2017consequences` (L0) Theorem 2.2, which writes `g_n`.

---

## Statement

```
g_n := p_{n+1} − p_n          (the n-th prime gap, n ≥ 1)
L_n := log p_n                (natural logarithm)
```

`g_1 = 1` (from `2 → 3`); every `g_n` for `n ≥ 2` is even.

## Role in the proof-obligation tree

The **left-hand side of the gap form** of the conjecture (see **D4** F4 and **D5**). Every
upper-bound obstruction (**L11**, BHP) and every lower-bound obstruction (**L12**, FGKMT) is a
statement about `g_n`. All of the empirical apparatus (**L7**, **T2**) is a ratio with `g_n` on
top.

## Dependencies

**D1** (indexing — `g_n` inherits the 1-indexed convention).

## Used by

**D5**, **D6**, **D7**, **L3**, **L4**, **L11**, **L12**, **L13**, **L15**, **T2**, **T5**.

## Why it is load-bearing

The whole attack rests on the observation (**D5**/**L1**) that Firoozbakht is a *gap bound*
rather than a statement about `n`-th roots. Once that reformulation is made, `g_n` is the only
quantity being bounded, and the entire literature on prime gaps becomes admissible evidence.

## Hazards

1. **`g_1 = 1` is the only odd gap.** Any argument that assumes gaps are even must exclude
   `n = 1`, which is precisely the index the off-by-one in **D1** silently drops.
2. Some sources index gaps by the *lower* prime and some by position in a first-occurrence
   table. `visser2019verifying` counts *maximal* gaps (the "81st maximal prime gap"), which is a
   different index entirely. Do not cross the two.

## Declared gap

None.
