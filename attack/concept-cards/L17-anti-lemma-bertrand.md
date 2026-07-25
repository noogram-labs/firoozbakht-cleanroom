# L17 — Anti-lemma: Bertrand's postulate is useless here

**Kind:** anti-lemma (a closed line of attack)
**Verdict:** **PROVEN** — the exclusion is exact, not asymptotic, and is recomputed here.
**Rests on:** in-run derivation. Bertrand's postulate itself is standard and is available in
Mathlib as `Nat.bertrand` (named in `decompose` §6; **not** confirmed against a pinned toolchain
— see **T4**).

---

## Statement

Bertrand's postulate gives `p_{n+1} < 2p_n`. That implies `F` only when `2 ≤ p_n^{1/n}`, i.e.
`p_n ≥ 2^n`. This holds at

```
n = 1  only  ( p_1 = 2 = 2^1 ),
```

and fails at **every** `n ≥ 2` — already at `n = 2` (`p_2 = 3 < 4`), and increasingly badly
thereafter, since `p_n ∼ n log n` grows polynomially while `2^n` grows exponentially.

## Why it fails, in one sentence

`p_n^{1/n} → 1`. The multiplicative room available to `p_{n+1}` shrinks to nothing, so any bound
of the form `p_{n+1} < C·p_n` with a **constant** `C > 1` is eventually useless — and "eventually"
here means "from `n = 2` on".

## Role in the proof-obligation tree

`L17` closes what is, for most readers, the *first* idea. It is recorded so no downstream leg
spends effort rediscovering that a constant-factor bound cannot beat a bar that tends to 1. The
same argument kills every Bertrand-type strengthening with a fixed multiplier.

## Dependencies

**D4**, **L1**.

## Used by

Nothing — that is the point.

## Hazards

1. The generalisation matters more than the instance: **no bound `p_{n+1} < C·p_n` with constant
   `C > 1` helps at any `n ≥ 2`.** Bounds of the form `p_{n+1} < p_n^{1+ε_n}` with `ε_n → 0` are
   the only shape that can compete, and `F` *is* such a bound with `ε_n = 1/n`.
2. Do not confuse this with **L8**: the Nicholson and Farhadian strengthenings are *not* of the
   constant-multiplier form and are not killed by this argument.

## Declared gap

None.
