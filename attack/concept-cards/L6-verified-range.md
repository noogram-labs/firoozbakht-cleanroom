# L6 — `F` is verified for all primes `p < 2⁶⁴`

**Kind:** theorem (computational, published)
**Verdict:** **PROVEN** (computationally, by the cited authors — not re-run here).
**Rests on:**
- `kourbatov2015verification` (L0) §4 **Theorem** (p. 288): *"Inequality (1) is true for all
  primes `p_k < 4 × 10¹⁸`."*
- `kourbatov2015verification` (L0) **Endnotes, added 5 Jan 2023**, verbatim: *"Firoozbakht's
  conjecture (1) is true for all primes `p_k < 2⁶⁴`; prime gaps of size `g < 1920` cannot violate
  (1)."*
- `visser2019verifying` (L0) §1 eq. (1.4) and Abstract: *"certainly the Firoozbakht conjecture
  holds for all primes `p < 2⁶⁴ = 18,446,744,073,709,551,616 ≈ 1.844×10¹⁹`"*, framed as "below the
  location of the 81st maximal prime gap".
- `oliveira2014goldbach` (**L2_weak, NOT OPENED** — AMS returned HTTP 403) — the
  first-occurrence prime-gap table to `4·10¹⁸` that the verification consumes.

---

## Statement

```
F holds at every n with p_n < 2⁶⁴ ≈ 1.8447 · 10¹⁹.
```

## Method (this is the part worth carrying, not just the number)

The verification is **not** a per-prime check. It is a *per-gap-size* argument:

1. Rewrite `F` as `π(p_k) < log p_k / (log p_{k+1} − log p_k)` (`kourbatov2015verification` §3
   eq. (5)) — see **D3**.
2. Insert the explicit bound `π(x) < x/(log x − 1.1)` for `x ≥ 60184`
   (credited there to Dusart 2010, Theorem 6.9 — see **T1**).
3. For each even gap size `g`, this yields a **computable safe bound** `S(g)`: a gap of size `g`
   can never violate `F` once it occurs at a prime `> S(g)`.
4. So it suffices to check the *first occurrence* of each `g` against `S(g)`. Checked for all even
   `g ∈ [2, 1476]` (2015), extended to `g < 1920` (2023 endnote).

The whole verification therefore reduces to a **first-occurrence gap table** plus arithmetic —
which is why `oliveira2014goldbach` is the load-bearing input and why the frontier moves when the
table does, not when someone re-sieves.

## Role in the proof-obligation tree

`L6` is the floor. It is what makes the empirical side of the tension in **L10** substantial: the
conjecture is not merely unrefuted, it is *checked* over 19 orders of magnitude. It is also the
unstated hypothesis of **L4**'s Theorem-4 family, which assumes `p_k > 4·10¹⁸`.

## Dependencies

**D3**, **D4**, **L1**, **T1** (Dusart's `π(x)` bound).

## Used by

**L4** (Theorem 4 family), **L7**, **L10** (the empirical half of the tension), **T2**, **T3**.

## Correction this card forces on the upstream `decompose` leg

`decompose` §2.3 and §8.6 quote the frontier as `4·10¹⁸`. **The current frontier is `2⁶⁴`**, per
Kourbatov's own 2023 endnote and Visser's abstract. The in-run sieve reached `3·10⁶`, which is
**≈12.79 orders of magnitude** short of `2⁶⁴` (the document's "twelve" was computed against
`4·10¹⁸`, where it is 12.12 — right arithmetic, superseded frontier).
(`source-ledger.md` §4.1.)

## Hazards

1. **Three different frontier figures circulate** — `4·10¹⁸`, `1·10¹⁹`, `2⁶⁴` — and
   `visser2019verifying` §1 reports all three in sequence as history. **Quote `2⁶⁴` and say where
   it comes from (the 2023 endnote), or quote `4·10¹⁸` and say it is the 2015 title.** Never quote
   one and cite the other.
2. **`kourbatov2015verification`'s title says `4·10¹⁸`.** A bibliography entry and a claim in the
   text can therefore disagree while both being correct. Add a `note` field — the ledger's BibTeX
   already does.
3. **The empirical foundation was never opened.** `oliveira2014goldbach` is the one row in the
   ledger whose text nobody in this run read. Everything `L6` asserts is mediated through
   Kourbatov. Priority 4 for the citation gate. (`source-ledger.md` §6.2, §7.4.)
4. **A verified range establishes nothing about the general case.** It bounds where a
   counterexample can live and does not shrink the difficulty of **L3**'s obstruction by anything.

## Declared gap

`oliveira2014goldbach` unopened; the in-run sieve (`3·10⁶`) is a sanity probe and **must never be
cited as a verification**.
