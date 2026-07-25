# L11 — Best unconditional upper bound on prime gaps (Baker–Harman–Pintz)

**Kind:** theorem (published; the obstruction on the proof side)
**Verdict:** **PROVEN** (by the cited authors). Tier **L1** here — abstract read at the
publisher, no internal theorem locator obtained.
**Rests on:**
- `baker2001difference` (L1) — *Proc. LMS* **83** (2001), 532–562, abstract read verbatim at the
  OUP page: *"showing that `[x, x + x^{0.525}]` contains prime numbers for large x."*
- `ferreira2017consequences` (L0) **Theorem 3.1** (attributed) — states it as `g_n ≤ p_n^{0.525}`
  for `n ≫ 0`, and adds: *"It is easy to see that Firoozbakht's conjecture improves the
  Baker-Harman-Pintz's bound significantly."*

---

## Statement

```
Unconditional  :   g_n  ≪  p_n^{0.525}
Under RH       :   g_n  ≪  √p_n · log p_n          [no ledger row — see Declared gap]
Firoozbakht needs (L3) :   g_n  <  log²p_n − log p_n − 1
```

## Role in the proof-obligation tree

**This card is the hard gate on the proof side.** By **L3**, any proof of `F` delivers an
unconditional polylogarithmic gap bound. The best available is a *power of `p`*. The distance
between `p^{0.525}` and `log²p` is not a matter of sharpening constants — it is the difference
between power-scale and log-scale, which no known method in analytic number theory bridges, and
which RH does not bridge either.

**Consequence for strategy:** any leg proposing a "direct proof" must state how it clears this
gate, or it is proposing something the field does not know how to do.

## Dependencies

**D2**, **L3**.

## Used by

The verdicts on every direct-proof and conditional-proof strategy.

## Correction this card forces — the overreach to avoid

`decompose` §2.1 concludes: *"Proving Firoozbakht is strictly harder than proving the Riemann
Hypothesis is useful for prime gaps."* **All five panelists rejected this, unanimously**
(`synthesis.md` §2 C3).

What is true: **`F` yields an unconditional gap bound not known to follow from RH.** That is a
*strength* comparison between statements, and it is correct.

What is false: an ordering of *proof difficulty*. `F` and RH are incomparable — no partial order
is supplied, and "strictly harder" would additionally require knowing that no easier route to `F`
exists. This is the classic error of reading implication-strength as proof-difficulty.

The overreach has a cost beyond the sentence: §2.1 elevates it to "a hard gate on Branch P", and
the asymptotic gate is then used to prune a **finite-range** strategy (prove for `n > N₀` with
`N₀` named, machine-check below it) that it does not touch at all.

A second correction runs in the artifact's favour: the `[X]` verdict **does not need** the
undischarged threshold asymptotics — Chebyshev-level bounds already separate `p^{0.525}` from
`log²p`. The gate is more robust than the argument offered for it. (`synthesis.md` §4.1.)

## Hazards

1. **The exponent is not the point.** Were it improved to `0.5` or `0.4`, nothing about the gate
   changes. Quote it qualitatively.
2. **No internal locator.** Only the abstract was read. Adequate for the qualitative use; **not
   adequate if any constant is quoted**. (`source-ledger.md` §6.5.)
3. Do not write "BHP is the best known bound" without "unconditional" — under RH the exponent
   improves, and the sentence is false as stated for conditional bounds.

## Declared gap

**The RH-conditional bound `g_n ≪ √p_n log p_n` has no ledger row.** It appears in
`decompose` §2.1 (P3b) as recall and was **not resolved** by the source-ledger leg. It is
standard and not in dispute, but this run has not sourced it. **Any paper stating it must fetch a
source first.** The strategic conclusion does not depend on it — `√p` is a power of `p` for the
same reason `p^{0.525}` is — but the sentence "RH does not help" currently rests on an
unverified recall.
