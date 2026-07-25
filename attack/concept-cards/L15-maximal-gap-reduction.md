# L15 — The maximal-gap reduction (P6′) — **OPEN**

**Kind:** lemma, **not proved**
**Verdict:** **OPEN.** Empirically unviolated by every measurement that bears on it; **no proof
in this run and none found in the literature.** Any leg that uses it is importing a hypothesis.
**Rests on:** in-run computation, plus `dusart2010estimates` (L0) Theorem 6.9 and
Propositions 6.6/6.7 as the tool that would discharge it. **No ledger row asserts it.**

---

## The claim

> **P6′.** For `m < n` with `p_m, p_n` straddling a record (maximal) gap, `T_m ≤ T_n`.

If P6′ holds, then verifying `F` at record-gap indices suffices: for `m` the governing record
index below `n`, `g_n ≤ g_m < T_m ≤ T_n`. Since record gaps are extremely sparse (**21** below
`3·10⁶`), this is an enormous pruning of any search.

## Why it is not a triviality

The chain needs `T` to be nondecreasing across the block, and **`T` is not monotone**:
`T_{n+1} < T_n` at **121 238 of 216 805** steps with `n ≥ 10` (**55.92 %**), verified in-run.
So the reduction cannot simply be asserted.

## Why it is nevertheless very likely true

`T` grows on the *coarse* scale (`T ≈ L² − L − 1`, increasing in `p`) while oscillating on the
fine scale, and record gaps are far apart. Four independent measurements, none of which the
`decompose` leg performed:

| measurement | result |
|---|---|
| `T_{m(n)} ≤ T_n` for `m(n)` = governing record index, all `n` ≤ 216 815 | **0 exceptions in 216 815 pairs** — *this leg*; godel reported 0/216 794 under a slightly narrower pair convention |
| pairs (record `m`, later `n` in block) with `T_n < T_m` | **0 across all 21 record blocks**; max drawdown `0.5487` = 1.23 % of `T` |
| max dip of `T` below its running maximum, per decade | `0.55 → 0.018`, decaying as `O(1/L)` while the margin grows as `L` |
| is "the six tightest ρ cases are records" informative? | **no** — see hazard 3 |

The dip decays and the margin grows: on the evidence this is **a Dusart lookup, not a research
leg**. That is the panel's position (`synthesis.md` §2 C7) and this leg concurs — but *concurring
is not discharging*.

## Role in the proof-obligation tree

`L15` is the **sole pruning rule** of the only computationally live route. Without it, a search is
a blind sweep over all `n`; with it, a search over 21 indices instead of 216 815.

## Dependencies

**D5**, **L2**, **T1** (Dusart bounds are what a proof would consume).

## Used by

**T2** (search design), **T5**.

## Hazards — the reason this card is written in red

1. **A pruned search that finds nothing establishes "`F` holds at record indices", not `F`.**
   `decompose` §2.4 says any leg citing the reduction without discharging P6′ "is importing an
   unproved lemma"; §3.4 then writes "by P6′ (once discharged, **or heuristically meanwhile**)".
   The document violates its own gate two sections after setting it (`synthesis.md` §2 C6).
2. **Laundering risk.** If a null result from a pruned search is later reported as a verification
   *height*, the undischarged assumption has been converted into evidence for the search design
   that assumed it. Name the assumption in the result, every time.
3. **The evidence `decompose` offered is non-diagnostic.** Its §5.1 finding 3 — "all six tightest
   `ρ` cases occur at record gaps" — is (a) exactly `probe2.py:13`'s `best[:6]` print truncation,
   breaking to 8/10 and collapsing to 15/100, and (b) **structurally necessary**: `ρ` at a fixed
   gap size is maximal at that gap's first occurrence *because* `T` grows coarsely — i.e. the
   observation restates the uncontested half of P6′. A script's display parameter became a stated
   empirical finding. (`synthesis.md` §2 C7, §4.4.)
4. **The 55.92 % figure is also non-diagnostic**, in the other direction: it measures single steps,
   not record blocks. `decompose` calls P6′ "a live correctness risk" on the strength of a
   statistic that does not bear on it. **So the document's stated evidence carries no weight in
   either direction, and the evidence that does bear on P6′ — zero exceptions — was never
   gathered upstream.**

## Declared gap

**P6′ is not proved.** The route to a proof is: use Dusart's effective `π(x)` and `p_k` bounds
(**T1**) to bound the oscillation of `T` below its coarse trend, and compare that bound against
the spacing of record gaps. Nobody in this run has done it. **This is the single most tractable
open obligation in the attack.**
