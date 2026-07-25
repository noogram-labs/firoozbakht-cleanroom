# T2 — Technique: counterexample-search design and numerical precision

**Kind:** technique (the only computationally live route)
**Verdict:** **PROVEN** where it makes claims (the objective function, the precision crossovers);
the route itself is **live but not expected to be decisive**.
**Rests on:** **D6**, **L1**, **L13** for the objective; `oeis_A111943` (L0) and
`kourbatov2015verification` (L0) for calibration and the frontier; in-run computation for the
precision analysis.

---

## The three design rules

### Rule 1 — Track `ρ_n = g_n/T_n`, never `g_n/log²p_n`, never gap size

- `ρ_n ≥ 1` is **exactly** a failure of `F`, at every `n`, with no error term (**D6**).
- `c_n = g_n/L²` sets the bar too high by `O(L)` — it is *sufficient* for refutation but not
  necessary (**D7**, **L13**), so a search using it can step straight over a counterexample.
- Gap size alone is wrong because `ρ` weights by `≈ log²p`: in-run, `ρ = 0.76047` at `p = 1327`
  (gap 34) **beats** `ρ = 0.75908` at `p = 2 010 733` (gap 148).

### Rule 2 — Never use the F2-margin ratio as a progress metric

`decompose` §5.1's headline `max n·log p_{n+1}/((n+1)·log p_n) = 0.9999984` is a **`1/n`
artifact**: its distance from 1 scales like `(1−ρ_n)/n`. It would read `0.9999984` in a universe
where every gap were 2. A leg that extends the sieve and reports `0.9999999…` has measured `1/n`
and will read it as the conjecture tightening. (`synthesis.md` §2 C10.)

### Rule 3 — Double precision dies **below** the frontier; `ρ_n` does not

| statistic | where doubles fail | frontier (**L6**) |
|---|---|---|
| F2-margin ratio | `p ≈ 2·10¹⁵` (most conservative of three independent panel estimates: `4·10¹⁵`, `1.2·10¹⁶`, `2·10¹⁵`) | `2⁶⁴ ≈ 1.84·10¹⁹` |
| `ρ_n` | operands are `O(1)`; no crossover in the relevant range | — |

**Adopt `p ≈ 2·10¹⁵` as the stated crossover.** Past it, use certified interval arithmetic on
logarithms (or exact rational bounds), not doubles. **The failure is silent in the verification
direction** — a probe that breaks only on a detected violation will report "no counterexample"
from pure noise. That is the dangerous direction. (`synthesis.md` §2 C10, §3 D5.)

## Calibration — what the search must beat

| Range | max `ρ` | max `c` |
|---|---|---|
| in-run, `p < 3·10⁶` | **0.76047** (`p = 1327`) | **0.70257** (`p = 2 010 733`) |
| all known primes (**L7**) | **0.94846** (`p = 1.693·10¹⁵`) | **0.92064** |
| refutation bar | `1` exactly | `1 − 1/L ≈ 0.9715` at that size (**L3**) |

The record has stood since 1999, and the published verification (**L6**) already runs four orders
of magnitude past it. **A search leg should aim to reproduce and extend the `ρ` table, not to
expect a hit.**

## Role in the proof-obligation tree

The only route on either branch that a compute budget can advance today. Both theorem-producing
refutation routes are blocked by **L12**; both proof routes are blocked by **L11**.

## Dependencies

**D6**, **D7**, **L1**, **L6**, **L7**, **L13**, **L15** (the pruning rule — **open**),
**L16** (index certification), **T1**, **T3**.

## Hazards

1. **The pruning rule is undischarged.** Restricting the search to record-gap indices assumes
   **L15**. A null result under that pruning establishes "`F` holds at record indices", *not* `F`.
   **Say so in the result, every time.** (`synthesis.md` §2 C6.)
2. **The evidential loop.** The pruning rule's empirical support and the search it prunes draw on
   the same sieve range — over which the answer is already known. Extending the search past the
   range that justified the pruning is where the assumption starts doing real work.
3. **Index certification is not free** (**L16**). Extending the `ρ` table is an exhaustive-sieve
   project, not a spot search — or it needs certified `π` lower bounds from **T1**.
4. **The in-run sieve reached `3·10⁶`** — ≈12.79 orders below `2⁶⁴`. It is a sanity probe. **It
   must never be cited as a verification.**

## Declared gap

No search was run in this leg beyond the `3·10⁶` reproduction. The precision crossovers are panel
estimates re-adopted here, **not re-derived** — this leg reproduced the sieve statistics, not the
floating-point error analysis.
