# L15 — The maximal-gap reduction (P6′) — **the pair-uniform form is REFUTED; two weaker forms are OPEN**

**Kind:** lemma
**Verdict (amended 2026-07-26 by the re-attack leg `task-20260726-56a7`).** The claim **as stated
below in prose** — the *pair-uniform* form, now named **P6′-pair** — is **FALSE**. Two explicit
witnesses, exact arithmetic at 60 digits; 17 exceptions below `10⁹`. Two strictly weaker
*index-selective* forms, **P6′-gov** and **P6′-min**, are **OPEN** and each of them, at the first
failure alone, suffices for first-failure maximality. **Any leg that uses P6′-min or P6′-gov is
still importing a hypothesis; any leg that uses P6′-pair is importing a false one.**
See `attack-round-2/proof-attempt-first-failure-maximality.md` §1–§3, §5.

> **The three predicates, named once.** For `r(n)` the largest record index `≤ n` and
> `µ(n) := min{ j : g_j ≥ g_n }`:
>
> | name | statement | status |
> |---|---|---|
> | **P6′-pair** | `T_m ≤ T_n` for every `m < n` with a record index `j`, `m ≤ j < n` | **FALSE** |
> | **P6′-gov** | `T_{r(n)} ≤ T_n` for every `n` | OPEN — 0 exceptions in `50 847 503` pairs, `p < 10⁹`; margin decays `≈ p^{−0.83}` |
> | **P6′-min** | `T_{µ(n)} ≤ T_n` for every `n` | OPEN — 0 exceptions in `50 847 503` pairs; margin **flat** at `+0.4845277` (`n = 1879`) across seven decades |
> | **P6′-rec** | `T_j ≤ T_{j'}` for consecutive record indices | OPEN — 0 exceptions in **29** record steps. *New obligation:* `P6′-gov ⟹ P6′-min` is **not** valid without it |
>
> **The refuting witness (least):** `m = 1823` (`p_m = 15 641`), record index `j = 1831`
> (`p_j = 15 683`, `g_j = 44`), `n = 1847` (`p_n = 15 823`); `T_m − T_n = +0.028610605`.
> A second, at a different scale: `m = 10 655 449` (`p = 191 912 639`), `j = 10 655 462`
> (`g = 248`), `n = 10 655 590`; `T_m − T_n = +3.5792097·10⁻⁵`.

**Rests on:** in-run computation, plus `dusart2010estimates` (L0) Theorem 6.9 and
Propositions 6.6/6.7 as the tool that would discharge it. **No ledger row asserts it.**

---

## The claim

> **P6′.** For `m < n` with `p_m, p_n` straddling a record (maximal) gap, `T_m ≤ T_n`.

**⚠ As written, this claim is FALSE** — see the verdict block above. What survives is the
index-selective reading: for `m = r(n)` (P6′-gov) or `m = µ(n)` (P6′-min),
`g_n ≤ g_m < T_m ≤ T_n`. Since record gaps are extremely sparse (**21** below `3·10⁶`, **30** below
`10⁹`), this is an enormous pruning of any search — and the pruning is **not** damaged by the
refutation, because it never consumed the pair-uniform form.

## Why it is not a triviality

The chain needs `T` to be nondecreasing across the block, and **`T` is not monotone**:
`T_{n+1} < T_n` at **121 238 of 216 805** steps with `n ≥ 10` (**55.9203 %**) at `3·10⁶`, verified
in-run and reproduced independently 2026-07-26. The figure is **range-dependent** — `56.3501 %` at
`10⁷`, `56.9313 %` at `10⁸` — and must never be quoted without its bound and its `n ≥ 10`
convention (`faults.md` F5). So the reduction cannot simply be asserted — and in its pair-uniform
form it is in fact false.

## Why it is nevertheless very likely true

`T` grows on the *coarse* scale (`T ≈ L² − L − 1`, increasing in `p`) while oscillating on the
fine scale, and record gaps are far apart. **This section survives for P6′-gov, P6′-min and
P6′-rec only; it does not apply to P6′-pair, which is false.** Four independent measurements, none
of which the `decompose` leg performed:

**⚠ Read the predicate column before the result column.** Round 1 reported all four rows under the
single name `m(n)`, which is the vocabulary collision `faults.md` F1 blocks on.

| measurement | **predicate** | result |
|---|---|---|
| `T_{r(n)} ≤ T_n`, all `n` ≤ 216 815 | **P6′-gov** | **0 exceptions in 216 794 admissible pairs** (`216 815` minus the 21 trivial self-pairs — that *is* godel's "narrower convention", and it is the correct denominator). Margin decays `≈ p^{−0.83}` (`notebook-2` §3) |
| `T_{µ(n)} ≤ T_n` | **P6′-min** | **0 exceptions**; min margin `+0.4845277` at `n = 1879`, **unmoved** from `3·10⁶` to `10¹¹` (`notebook-0` finding 3) |
| pairs (record `m`, later `n` in block) with `T_n < T_m` | **P6′-gov** | **0 across all 21 record blocks**; max drawdown `0.5487` = 1.23 % of `T` |
| max dip of `T` below its running maximum, per decade | bears on **P6′-rec**, *not* on P6′-gov or P6′-min | `0.55 → 0.018`, decaying as `O(1/L)` while the margin grows as `L` |
| is "the six tightest ρ cases are records" informative? | — | **no** — see hazard 3 |

~~The dip decays and the margin grows: on the evidence this is **a Dusart lookup, not a research
leg**.~~ **Withdrawn 2026-07-26.** (a) The dip statistic measures a *third* quantity (P6′-rec) and
does not bear on the two predicates that matter. (b) `proof-attempt-0.md` §7 shows that P6′ for
short blocks is equivalent to a short-interval prime count sharper than Brun–Titchmarsh by a factor
`≈ 2` — not a lookup. (c) The pair-uniform form is not open at all; it is false. What remains true
of the panel's position (`synthesis.md` §2 C7) is only that P6′-min is *empirically robust*, and
robustness is not tractability.

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

**P6′-gov, P6′-min and P6′-rec are not proved; P6′-pair is refuted.** The route round 1 proposed —
use Dusart's effective `π(x)` and `p_k` bounds (**T1**) to bound the oscillation of `T` below its
coarse trend — is shown in `proof-attempt-0.md` §7.3 to be unable to close the window at *any*
level of effective-constant improvement, and `attack-round-2/proof-attempt-first-failure-maximality.md`
§8 adds that the surviving predicates must be attacked **index-selectively**, because the
pair-uniform form is false. ~~**This is the single most tractable open obligation in the attack.**~~
**Withdrawn.** The obligation to state and work is **P6′-min** (the weakest sufficient form,
Theorem 2 of the round-2 attempt), with **P6′-rec** listed beside it because
`P6′-gov ⟹ P6′-min` needs it and its empirical base is 29 data points.
