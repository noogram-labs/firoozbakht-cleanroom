# L8 — The strengthening chain: Farhadian ⟹ Nicholson ⟹ Firoozbakht ⟹ Forgues

**Kind:** lemma (published, with proof)
**Verdict:** **PROVEN.** Read at the locator, proof given in `ferreira2017consequences`.
**Rests on:**
- `ferreira2017consequences` (L0) **Theorem 4.5**: *"Farhadian ⟹ Nicholson ⟹ Firoozbakht ⟹
  Forgues."* With proof.
- `visser2019verifying` (L0) **Conjecture 2**, eqs. (2.1)–(2.3) and the following sentence:
  *"the standard inequalities `n ln n < p_n < n ln p_n` show that Farhadian ⟹ Nicholson ⟹
  Firoozbakht."*
- `visser2019verifying` (L0) **Conjecture 3**, eqs. (2.4)–(2.6) — the three conjectures in gap
  form.
- `oeis_A182514` (L0) `%C` (J. W. Nicholson, 2013/2016) — the **only citable trace** of
  Nicholson's conjecture.
- `farhadian2017new` (**L2_strong, NOT OPENED**) — attribution for Farhadian only.

---

## Statement — the three conjectures in gap form (Visser, Conjecture 3)

```
Firoozbakht :  g_n ≤ p_n ( p_n^{1/n} − 1 )                        n ≥ 1
Nicholson   :  g_n ≤ p_n ( (n ln n)^{1/n} − 1 )                   n > 4
Farhadian   :  g_n ≤ p_n ( (p_n ln n / ln p_n)^{1/n} − 1 )        n > 4
```

and the ratio form:

```
Nicholson   :  (p_{n+1}/p_n)^n  <  n ln n            (n ≥ 5)
Farhadian   :  (p_{n+1}/p_n)^n  ≤  p_n^{ln n / ln p_n}   (n > 4)
Forgues     :  (ln p_{n+1} / ln p_n)^n  <  e
```

**Chain:** Farhadian ⟹ Nicholson ⟹ Firoozbakht ⟹ Forgues, via `n ln n < p_n < n ln p_n`.

## Role in the proof-obligation tree

Two distinct uses, and they point in opposite directions:

1. **Upward (a strengthening for inductive traction).** The standard cure for a statement with no
   internal induction mechanism is to prove a *stronger* statement that does. Nicholson and
   Farhadian are the two named candidates. `decompose` §3.0 listed "weakening" as an archetype
   and had **no mirror for strengthening** — a completeness hole three of five panelists found
   independently (`synthesis.md` §2 C8).
2. **Downward (a cheaper refutation target).** Refuting Nicholson does *not* refute Firoozbakht,
   but a near-miss on Nicholson locates where to look. `oeis_A182514`'s terms — `2, 3, 7, 113,
   1327, 1693182318746371` — are exactly the primes where the naive `n`-bound is breached, and the
   last of them is **the same prime as the CSG record in L7**, seen from another angle.

## Dependencies

**D4**, **D5**, **L1**.

## Used by

The strategy layer. No other card consumes it.

## What this card closed

`decompose` §7 A11 deliberately omitted the Nicholson and Farhadian statements as "recalled too
vaguely to state safely". That was the right call at the time; the statements are now available
verbatim at L0 and **may be stated**. (`source-ledger.md` §3 A11, §4.)

## Hazards

1. **Nicholson's conjecture has no publication.** Its only citable trace is an OEIS comment plus
   Visser's restatement. Attribute it as such — "conjectured by J. W. Nicholson (OEIS A182514,
   2013)" — never as a paper. (`source-ledger.md` §6.9.)
2. **`farhadian2017new` was not opened.** Cite Visser (Conjecture 2, eq. 2.3) or Ferreira–Mariano
   (Conjecture 4.3) for the *statement*; cite the Farhadian–Jakimczuk row only for the
   *attribution*. (`source-ledger.md` §2.4.)
3. **Visser states all of these with `≤`.** Ferreira–Mariano uses strict. See **D4** hazard 1 —
   for Firoozbakht the two coincide; for Nicholson and Farhadian, whose right-hand sides are not
   integers, **the distinction has not been checked in this run**.
4. **The chain's proof consumes `n ln n < p_n < n ln p_n`** (Rosser; `ferreira2017consequences`
   Theorem 4.4). That is an unconditional classical bound, but it is an input, and a leg
   formalizing the chain needs it in Mathlib. See **T4**.

## Declared gap

The strict-vs-non-strict question for Nicholson and Farhadian is **open and unexamined**. Recorded
as a gap rather than guessed.
