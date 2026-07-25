# D7 — The Cramér–Shanks–Granville ratio `c_n := g_n / log² p_n`

**Kind:** definition
**Verdict:** **PROVEN** — definitional. Its *relation* to `F` is a one-way implication, proven,
with an explicit exception set (**L13**).
**Rests on:** `oeis_A111943` (L0) — the sequence's own definition: "C-S-G ratio is `(q−p)/(log p)²`".
Corroborated at L0 by `granville1995cramer` preprint p. 10 (the table of record ratios) and by
T. R. Nicely's first-occurrence tables.

---

## Statement

```
c_n  :=  g_n / (log p_n)²
```

Relation to `F`, stated in the direction that is true:

```
c_n ≥ 1   ⟹   ρ_n ≥ 1   ⟹   F fails at n         provided  T_n < L_n²  (which holds iff n ∉ {1,…,7,10})
```

So a CSG breach is a **sufficient**, not necessary, refutation criterion — and a conservative one:
the true bar is `T_n`, which sits about `L + 1` *below* `L²`.

## Role in the proof-obligation tree

`c_n` is the unit the *literature* uses. Cramér's conjecture, Granville's correction, the OEIS
record table and every published "how close is it?" statement are in this unit. It is therefore
the unit for reading the field, and **D6** is the unit for doing the search.

## Dependencies

**D2**, **D5**, **L13** (the direction of the implication is only valid where `T_n < L_n²`).

## Used by

**L7** (the record), **L9**, **L10** (Cramér and Granville are statements about `limsup c_n`),
**L3** (Ferreira–Mariano's `limsup c_n ≤ 1`), **T2**.

## Conversion between the two units

`ρ_n = c_n · L²/(L² − L − 1)`. At the record (`p ≈ 1.693·10¹⁵`, `L = 35.0654`):

| Unit | Observed record | Firoozbakht-implied ceiling | Headroom |
|---|---|---|---|
| `c_n` (CSG) | **0.9206386** | `1 − 1/L = 0.9714818` (Kourbatov, via `oeis_A111943` `%C`) | **5.23 %** |
| `ρ_n` | **0.9484582** | `1` exactly | **5.15 %** |

All four figures recomputed in this leg. The often-quoted "0.92" and the often-quoted "5% margin"
are the same fact in two units, and neither is the ratio the search should track.

## Hazards

1. **Unit collision.** `decompose` §3.8 puts `0.7605` (a `ρ`) and `0.92` (a `c`) in one clause as
   though comparable. They are not: the in-run `ρ` record is `0.76047` (at `p = 1327`) and the
   in-run `c` record is `0.70257` (at `p = 2 010 733`) — *different primes*; the all-primes `c`
   record `0.9206` is `ρ = 0.9485`. **Always name the unit.**
   (`synthesis.md` §2 C13.)
2. **The exception set is not `n ≤ 10`.** `T_n ≥ L_n²` at exactly `n ∈ {1,2,3,4,5,6,7,10}` —
   note `n = 8, 9` **pass** and `n = 10` **fails**, so this is not a monotone crossing and an
   induction from a base case will look in the wrong place. Recomputed in this leg. See **L13**.
3. **Warrant and applicability are disjoint.** Where the sufficiency is verified
   (`11 ≤ n ≤ 216 815`), `max c_n = 0.703`, so a CSG breach is impossible there. The criterion is
   valid exactly where it cannot fire. (`synthesis.md` §2 C5, popper.)
4. **A finite record is not evidence about a `limsup`.** Reading `c = 0.9206` against a ceiling of
   `0.9715` as evidence that the conjecture is *fragile* is the same promotion of heuristic into
   test that **L10**'s card forbids, by another door — a `limsup` statement is invariant under
   every finite computation. (`synthesis.md` §4.2.)

## Declared gap

None.
