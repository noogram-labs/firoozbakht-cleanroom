# L14 — The smooth model of Firoozbakht is true and elementary

**Kind:** lemma (proved in-run; pure calculus, no primes)
**Verdict:** **PROVEN** — and simultaneously **the most over-billed object in the attack**. Read
the "Hazards" before using it.
**Rests on:** in-run derivation. Its bridge to the primes, if ever built, would rest on
`dusart2010estimates` (L0) **Propositions 6.6/6.7** — two-sided effective bounds
`k(ln k + ln₂k − 1 + (ln₂k − 2.1)/ln k) ≤ p_k ≤ k(ln k + ln₂k − 1 + (ln₂k − 2)/ln k)` — and on
`ferreira2017consequences` (L0) **Theorem 4.4** (`p_n > n ln n`; Rosser).

---

## Statement

Let `f(x) := (x log x)^{1/x}` be the PNT first-order surrogate for `p_n^{1/n}`. Then

```
d/dx [ (log x + log log x)/x ]  =  [ 1 + 1/log x − log x − log log x ] / x²   <  0
```

for all `x ≥ 5`, so **`f` is strictly decreasing on `[5, ∞)`** — the smooth model of Firoozbakht
holds, and its proof is one derivative.

**Domain note.** The bracket changes sign just above `x = 4`: it is `+0.0084` at `x = 4`,
`−0.0193` at `x = 4.05`, `−0.464` at `x = 5`. The safe stated range is **`x ≥ 5`, not `x ≥ 4`** —
a slip that reads plausibly and that `decompose` §8.8 records having caught in its own review.
Recomputed here: the sign change sits at **x = 4.01507**, so `x ≥ 4.02` is already safe and
`x ≥ 5` is the safe *round* range. `x ≥ 4` is false by a margin of 0.0084 — small, and real.

## Role in the proof-obligation tree

`L14` performs a genuine **localization of the difficulty**: `F` is true for the *mean behaviour*
of `p_n` and can therefore fail only through *fluctuation*. That converts the question into "how
large can the fluctuation of `p_n` around `n log n` be at a single index" — which is **L11**
again, but now with the hard part named precisely.

## Dependencies

Nothing. This is the card's whole problem — see below.

## Used by

Nothing, currently. Also the card's whole problem.

## Hazards — four, and together they are a demotion

1. **`L14` contains no primes.** It is a calculus lemma that would be true if primes did not
   exist. Three panelists converged on this independently (`synthesis.md` §2 C4).
2. **No other node can consume it**, because the bridge from `(x log x)^{1/x}` to `p_n^{1/n}` is
   *itself* a missing node — and building that bridge requires effective two-sided bounds on `p_k`
   (Dusart 6.6/6.7), which is the same effective machinery every other card needs. The bridge, not
   the lemma, is the work.
3. **`decompose` §6 calls `L14` "the only node in L1–L6 that is a genuine theorem rather than a
   definition or a finite check" and makes it the primary Lean deliverable. Both halves are
   wrong**, unanimously per the panel: the equivalence chain and the gap reformulation are
   theorems too, and §6's own stated value proposition ("a machine-checked equivalence chain")
   names one of them two paragraphs earlier. **Promote the equivalence chain and the gap
   reformulation; keep `L14` but restate its billing.** (`synthesis.md` §2 C4, §3 D4.)
4. **The smooth model says the *opposite* of the discrete truth about `T`.** The smooth surrogate
   is 100% monotone; the actual `T_n` decreases at 55.92% of steps (**D5**). The tension is real
   and never surfaced upstream: non-monotonicity of `T` is a **discreteness** phenomenon (`n`
   increments by 1 while `p` jumps by `g`) that no smooth model can deliver. **Never use `L14` to
   reason about `T`'s local behaviour.** (`synthesis.md` §3 D2.)

## The honest billing

`L14` is *the only mathematics in this attack whose content is independent of whether `F` is true*
— it survives whichever way the conjecture goes. That is a real argument for formalizing it, and
it is a different argument from the one `decompose` made. Make that one instead.

## Declared gap

**The bridge from the smooth model to `p_n^{1/n}` is not built and is not costed.** Until it is,
`L14` is a decoration on the tree, not a node in it.
