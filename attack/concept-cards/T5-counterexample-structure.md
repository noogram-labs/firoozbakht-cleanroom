# T5 — Technique: constrain a counterexample before hunting it (contrapositive)

**Kind:** technique
**Verdict:** **MIXED, and the card says which is which.** Two of the three constraints below are
**PROVEN**; the third (record-index) is **conditional on the open L15**; the sieve-theoretic
constraint is **stated but not sourced**.
**Rests on:** **L2**, **L3**, **L6**, **L7**, **L15**; `ferreira2017consequences` (L0)
**Lemma 3.2**; `dusart2010estimates` (L0) **Prop. 6.8**.

---

## The move

Do not try to prove or refute `F`. Assume a minimal counterexample `n₀` exists and derive
necessary structural conditions on it. This produces no theorem by itself, but it converts a blind
sweep (**T2**) into a targeted search, and it is the natural bridge between the analytic and
computational legs.

## What is forced on `n₀`

### (a) Scale — **PROVEN**

`g_{n₀} ≥ T_{n₀} = L² − L − 1 + o(1)` (**L2**), i.e. `ρ_{n₀} ≥ 1` and `c_{n₀} ≥ 1 − 1/L`
(**L3**). Against an all-primes record of `ρ = 0.94846` (**L7**) that has stood since 1999, and a
verified range of `p < 2⁶⁴` (**L6**), `n₀` must sit at a gap of unprecedented Cramér scale, beyond
19 orders of magnitude of checking.

### (b) A dual constraint from `F` itself — **PROVEN**

`ferreira2017consequences` **Lemma 3.2**: *if `F` is true then `g_n < √n` for all `n ≥ 3645`.*
Contrapositive: **the minimal counterexample `n₀` is the first index where `g_n ≥ √n`**, provided
`n₀ ≥ 3645`. This is a second, independent handle on `n₀` and it is stated in a different variable
(`n`, not `p_n`) — useful precisely because it does not co-vary with (a).

### (c) Prime-free interval — **STATED, NOT SOURCED**

The interval `(p_{n₀}, p_{n₀} + T_{n₀})` is prime-free, so the residues of
`p_{n₀}+1, p_{n₀}+2, …` must cover every small prime modulus. That is a Jacobsthal-function
condition, and a strong sieve-theoretic constraint rather than a mild one.

**No ledger row supports this.** The Jacobsthal function does not appear anywhere in the source
ledger. Dusart **Prop. 6.8** — for `x ≥ 396738` there is a prime in `(x, x(1 + 1/(25 ln²x))]` — is
the *only* sourced statement in this run about prime-free intervals, and it is far too weak to
constrain `n₀` (it forbids gaps of relative size `> 1/(25 ln²x)`, i.e. absolute size `x/(25 ln²x)`,
which is enormous compared to `log²x`). **Treat (c) as a research direction, not a constraint.**

### (d) Record index — **CONDITIONAL ON THE OPEN L15**

Empirically every tight `ρ` case in range sits at a record gap; if **L15** were discharged this
would become a proof that `n₀` is a record index. **It is not discharged.** See **L15** hazard 3
for why the upstream evidence for this was non-diagnostic.

## Role in the proof-obligation tree

The highest-leverage item on the refutation side that is actionable *now*. It produces no theorem
and it makes **T2** rigorous rather than suggestive.

## Dependencies

**D5**, **D6**, **L2**, **L3**, **L6**, **L7**, **L15** (for (d) only), **T1**.

## Used by

**T2**.

## Hazards

1. **Unit collision, again.** `decompose` §3.8 writes "`ρ_{n₀} ≥ 1` where the observed maximum
   below `3·10⁶` is `0.7605` and the recalled record over all known primes is `≈ 0.92`" — mixing
   a `ρ` and a `c` in one clause. In `ρ` units the record is `0.94846`. §3.8 is a *recommended
   attack target*, which makes the slip expensive. (`synthesis.md` §2 C13.)
2. **(b)'s threshold `n ≥ 3645` is 1-indexed** (**D1**).
3. Constraints (a) and (b) are both consequences of `F`; using them to *search* is contrapositive
   reasoning and is sound. Using them to argue `F` is *likely true* is circular.

## Declared gap

**The Jacobsthal / prime-free-interval constraint (c) has no source in this run.** It is the most
attractive-sounding item on this card and the least supported. Recorded as a direction, not a
result.
