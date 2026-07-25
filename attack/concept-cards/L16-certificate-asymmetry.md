# L16 — The Σ₁/Π₁ asymmetry, and why a refutation certificate is not short

**Kind:** lemma (logic) + a correction to a widely-repeated claim
**Verdict:** **PROVEN** — the logical classification is standard; the certificate correction is
derived below and was reached independently by three panelists.
**Rests on:** **D3** (`π(p_n) = n`) and **D5** (`T_n` is decreasing in `n` at fixed `p_n`).
**No ledger row** — this card is self-contained plus the upstream `frame-deliberation` artifact
(`synthesis.md` §2 C2, §4.6). Declared as such.

---

## Statement

**(a) Classification.** `F` is **Π₁**: `∀n, p_{n+1}^n < p_n^{n+1}` (**D4** F3, a decidable matrix).
`¬F` is **Σ₁**.

**(b) What a refutation must exhibit.** A witness is not `(n, p_n, p_{n+1})` with primality
proofs. It is `(n, p_n, p_{n+1})` plus:
  - `p_n`, `p_{n+1}` prime (succinct certificates exist — Pratt);
  - no prime strictly between them (a bounded search, cheap);
  - **`π(p_n) = n`** — and *this* has no known succinct certificate. Verifying a prime's **rank**
    costs a full sieve to `p_n`, or `Õ(x^{2/3})` by Meissel–Lehmer-type counting.

**(c) The repair.** A **certified lower bound `N ≤ π(p_n)`** suffices. Because `T_n` is strictly
decreasing in `n` at fixed `p_n` (**D5**), understating the index *raises* the bar:

```
N ≤ n   ⟹   T_N ≥ T_n   ⟹   [ g_n ≥ T_N  ⟹  g_n ≥ T_n  ⟹  F fails at n ]
```

So a refutation needs only a **lower** bound on the rank — which effective `π(x)` estimates
(**T1**) supply unconditionally, with no sieve at all.

## Role in the proof-obligation tree

`L16` draws an edge the upstream tree omits: **a refutation depends on the effective-`π(x)` node.**
`decompose` places effectivity on the proof branch as a leaf and leaves the refutation branch with
no dependency on it. That is wrong; the refutation branch needs it too, and needs it first.

## Dependencies

**D3**, **D4**, **D5**, **T1**.

## Used by

**T2**, **T3**, **T4** (this is what makes the Lean finite-verification node expensive).

## Correction this card forces

`decompose` §1.4 states: *"`¬F` is a **Σ₁ statement** … A refutation is therefore *finitely
certifiable* — a single integer `n` plus the two primes, with primality certificates, settles
it,"* and calls the Σ₁/Π₁ asymmetry *"the single most important structural fact about the problem
and the reason §3's feasibility verdicts are so lopsided."*

**§1.4 conflates "finite witness" with "short witness".** §1.1 states the reason for the
conflation's falsity ("`π(p_n) = n` exactly — the threshold couples the gap to the count") and
§4.1 forgets it three sections later. The omission fails in the **dangerous direction**: an
overstated index *lowers* the bar a counterexample must clear, so a sloppy certificate can appear
to refute `F` when it does not.

**Consequences nobody upstream drew:**
- Extending the `ρ` table is an **exhaustive-sieve project**, not a spot search (**T3**).
- The verdicts are **less lopsided than stated**: refutation is cheap in *logical* form and
  expensive in *computational* form.

## A missing route this card exposes

For a **Π₁** sentence, independence from a sound theory *entails truth in ℕ* — a false Π₁
statement is refutable by a finite computation, hence provable in any theory that proves true
Σ₁ facts. So **independence is a route to establishing `F`**, not merely a curiosity.
`decompose` §1.4 supplies the premise in its own words and never draws the inference; four of five
panelists flagged the missing node (`synthesis.md` §2 C8).

*This is not a recommendation to pursue it* — proving independence of an open number-theoretic Π₁
statement is not easier than proving it. It is recorded so the tree is honest about what it omits.

## Hazards

1. Do not read (c) as saying rank certification is free. It says the *bar* is safe under
   understatement. Computing a good lower bound still requires **T1**'s effective estimates and
   their validity ranges.
2. `π(p_n) = n` under **1-indexing** (**D1**). Under Mathlib's 0-indexing the identity is
   `π(nth Prime k) = k + 1`.

## Declared gap

**This card has no source-ledger row.** The classification is textbook logic and the certificate
argument is elementary, but neither was sourced in this run. If the final paper states the Π₁
independence remark, it needs a citation the run does not currently have.
