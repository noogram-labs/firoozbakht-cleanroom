# D3 — `π(x)` and the count–index identity `π(p_n) = n`

**Kind:** definition + identity
**Verdict:** **PROVEN** — trivial from the definitions, and used explicitly at an L0 locator:
`kourbatov2015verification` §3 eq. (5) writes Firoozbakht as a statement about `π(p_k)`.
**Rests on:** `kourbatov2015verification` (L0) §3 eq. (5):
`Firoozbakht ⟺ π(p_k) < log p_k / (log p_{k+1} − log p_k)`.

---

## Statement

`π(x) := #{q ≤ x : q prime}`. Under the 1-indexed convention of **D1**:

```
π(p_n) = n        exactly, for every n ≥ 1.
```

## Role in the proof-obligation tree

This identity is **what makes Firoozbakht harder than a pure gap bound.** The threshold that
`g_n` must beat (**D5**) depends on `n`, and `n` is not a free parameter — it is `π(p_n)`,
pinned to the location `p_n`. A statement of the form "there exists a gap of length `≥ G` near
`x`" is therefore *not* enough to refute the conjecture; one also needs to know the *rank* of
the prime at which it occurs.

## Dependencies

**D1**, **D2**.

## Used by

**D5** (the threshold is a function of `n = π(p_n)`), **L2** (the asymptotics are obtained by
substituting an effective estimate for `π`), **L6** (Kourbatov's verification method is
`π`-bound arithmetic), **L13**, **L16** (the certificate problem), **T1**, **T3**.

## Why it is load-bearing

Two consequences that are easy to lose:

1. **Substituting an estimate for `n` is where all the effective work happens.** Every card that
   converts `T_n` into `log²p_n − log p_n − 1` does so by replacing `n` with a two-sided bound on
   `π(p_n)`. That substitution — not the algebra around it — is the analytic content. See **T1**.
2. **A refutation must certify the rank, not just the primes.** See **L16**. Primality has
   succinct certificates; primality *rank* has none known.

## Hazards

1. `decompose` §1.1 states this identity and §4.1 forgets it, describing a refutation
   certificate as `(n, p_n, p_{n+1})` plus primality proofs. Three panelists caught the omission
   (`synthesis.md` §2 C2). The omission fails in the **dangerous** direction: `T_n` is decreasing
   in `n` at fixed `p_n`, so an *overstated* index lowers the bar a counterexample must clear.
2. `π(x)` estimates come with named validity ranges (`x ≥ 599`, `x ≥ 5393`, `x ≥ 60184`,
   `x ≥ 1772201`, `x ≥ 2634800823`). A range is part of the statement; dropping it is the most
   common way this card is misused. See **T1** and the Axler corrigendum note in **L4**.

## Declared gap

None here; the *effective* content is deferred to **T1**, whose primary source
(`axler2014newbounds`) is at tier L2_strong and was never opened.
