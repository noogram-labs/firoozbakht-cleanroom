# L18 — Anti-lemma: Littlewood oscillation does not shift the threshold

**Kind:** anti-lemma (a closed line of attack) — **with a scope correction**
**Verdict:** **PROVEN for what it actually claims**; the claim it is usually stated as making is
**broader than what is proved**. Both halves below.

**Rests on:** in-run estimate. The Littlewood oscillation result itself has **no ledger row** in
this run — declared as a gap.

---

## What is proved

Since `T_n` depends on `n = π(p_n)` exactly (**D3**), one might hope the sign changes of
`π(x) − li(x)` — of amplitude `≈ √x · log log log x / log x` — shift the threshold enough to
matter. They do not. Writing

```
L/n = L/(li(x) + Δ) ≈ (L/li(x))·(1 − Δ/li(x))
```

the induced change in `T_n = x(e^{L/n} − 1)` is

```
O( L² · logloglog x / √x )  →  0.
```

At `log²`-scale the oscillation is negligible by a factor of order `√x/L`. Four panelists
re-derived this estimate and agree (`synthesis.md` §2 C12).

## The scope correction — read this before quoting the card

`decompose` §4.6 files this under the heading *"what does NOT bear on F"*. **The estimate bounds
the effect of the oscillation on the RIGHT-hand side of `g_n < T_n` only.** It says nothing about
the left-hand side. In particular:

> **Prime-deficit regions correlating with large `g_n` are entirely untouched by this argument.**

That is a different mechanism — irregularity in `π` co-locating with irregularity in gaps — and
this card does not close it. The heading over-scopes what the computation proves.
(`synthesis.md` §2 C12, godel.)

## A second, more useful reading

The same computation is **half of a lemma that the effective-`π(x)` node (T1) needs** — bounding
the deviation of `L/n` from its smooth value is exactly the estimate that would discharge **L15**.
A section written to prevent wasted effort is doing work it does not know about
(`synthesis.md` §4.3, popper). **Do not delete this card when pruning dead ends; re-file it under
T1.**

## Role in the proof-obligation tree

Closes an attractive-looking route on the threshold side; contributes a fragment to **T1**;
leaves the left-hand-side mechanism explicitly open.

## Dependencies

**D3**, **D5**.

## Used by

**T1** (as a fragment), **L15** (as a fragment).

## Declared gap

1. **No ledger row for Littlewood's theorem** or for the amplitude
   `√x · logloglog x / log x`. Both are classical and undisputed; neither was sourced in this run.
   **Any paper stating them must fetch a source.**
2. **The prime-deficit / large-gap correlation mechanism is open** and is not addressed anywhere in
   this run.
