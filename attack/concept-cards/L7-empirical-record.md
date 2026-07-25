# L7 — The empirical record and the size of the margin

**Kind:** datum (published, at L0) + an in-run conversion
**Verdict:** **PROVEN** — the record is read at an L0 locator and corroborated by a second L0
source; the unit conversion and the margin are recomputed in this leg.
**Rests on:**
- `oeis_A111943` (L0) `%e` table — the twelve record CSG ratios, last being
  **`0.9206 @ 1693182318746371`**; `%C`: "a(12) was discovered by Bertil Nyman in 1999."
- T. R. Nicely, *New maximal prime gaps and first occurrences* (L0, corroborating fetch) — gap
  **1132** following **1693182318746371**, found by Nyman 24 Jan 1999, CSG ratio
  **0.92063858855742**, "the greatest known value".
- `oeis_A111943` (L0) `%C` (Kourbatov, 28 Jan 2016) — the Firoozbakht-implied ceiling
  `1 − 1/log p` for `p ≥ 11`.
- `granville1995cramer` (L1) preprint p. 10 — the record table to `10¹⁴`, an independent partial
  check of the same sequence.

---

## Statement

At `p = 1 693 182 318 746 371` (gap `g = 1132`, `L = log p = 35.065386`):

| Unit | Observed | Firoozbakht ceiling | Headroom |
|---|---|---|---|
| `c = g/L²` (**D7**) | **0.92063859** | `1 − 1/L = 0.97148185` | **5.234 %** |
| `ρ = g/T` (**D6**) | **0.94845823** | `1` (exact) | **5.154 %** |

All four figures recomputed in this leg from `g = 1132` and `p = 1693182318746371`.

The record has **stood since January 1999**.

## Role in the proof-obligation tree

`L7` is the whole empirical case that the conjecture is *fragile*, and simultaneously the whole
empirical case that it is *robust*. It is the number every reader will remember, so getting the
unit and the ceiling right matters more here than anywhere else in the attack.

## Dependencies

**D6**, **D7**, **L2** (the ceiling comes from **L3**, which comes from **L2**).

## Used by

**L10** (the empirical half of the tension), **T2** (calibration of the search).

## Two corrections this card forces on upstream artifacts

1. **`decompose` §4.3 quotes the record as "recollection ≈ 0.92" at tier L3.** It is now L0,
   confirmed to 4+ decimal places, with the gap, the prime, the discoverer and the date.
2. **`decompose` §3.8 puts `0.7605` and `0.92` in one clause.** Those are different units at
   different primes. In `ρ` units the record is **`0.9485`**, and the in-run maximum is
   `0.76047`. (`synthesis.md` §2 C13.)

## Hazards

1. **A finite record is not evidence about a `limsup`.** The "5% margin" is a fact about one
   prime. Reading it as evidence that the conjecture is close to failing is the promotion that
   **L10**'s card explicitly forbids — a `limsup` statement is invariant under every finite
   computation. State the margin; do not editorialise it into fragility.
   (`synthesis.md` §4.2, popper.)
2. **The margin is anchor-limited, not analysis-limited.** The asymptotic slack in **L2** is
   ~`7·10⁻⁵` in `c` units at this `L` — 750× smaller than the margin. Sharper asymptotics will not
   move this number. Only a new record, or a sharper ceiling, will. (`synthesis.md` §3 D1.)
3. **The record is a record *of the CSG ratio*, not of gap size.** A larger gap at a larger prime
   need not break it. Do not conflate this table with a maximal-gap table.
4. `oeis_A111943` `%C` notes "primes less than 23 are anomalous and are excluded" — the sequence
   has an exception convention of its own, unrelated to **L13**'s.

## Declared gap

None on the datum itself. The ceiling `1 − 1/log p` is quoted from an OEIS comment that cites
Kourbatov Theorem 1; the theorem is at L0 (**L3**) but the *derivation of this particular
sharpened form* from it was not re-done in this run. It is arithmetically plausible and unchecked.
**Flagged.**
