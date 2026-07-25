# Findings — notebook-2, target `unconditional-verified-range`

**Run:** `germ-20260725-791a7c45` · **leg:** `notebooks__2` · **molecule:** `task-20260725-09a7`
**Artifact:** `notebook-2.ipynb` (executed), `fb_core.py`, `test_fb_core.py`, `deep-runs.json`

**Status of Firoozbakht's conjecture `F` in this note: OPEN.** Not assumed true,
not assumed false. Everything below is computation, and computation corroborates
or refutes; it never constitutes the proof. Where this note writes **PROVEN** it
means a *finite* statement discharged by exhaustive exact arithmetic, or a lemma
derived here in full from one cited effective bound.

---

## 0 · What the target means

Three different claims travel under the name "the verified range", and the leg's
first job was to separate them:

| | claim | what it costs | what it rests on |
|---|---|---|---|
| **(a)** | every consecutive prime pair below `X` was individually checked | `Õ(X)` | a sieve + floating-point discipline |
| **(b)** | no gap size *occurring* below `X` can violate `F`, wherever it occurs | a table lookup | an effective `π(x)` bound + a **first-occurrence gap table** |
| **(c)** | `F` holds below `X` **assuming** RH / Cramér / a gap conjecture | free | an unproved hypothesis |

Target #2 is **(a) + (b)** and explicitly **not (c)**. Route (b) is the one that
reaches `2⁶⁴` in the literature (card **L6**); its analytic half is re-derived
from scratch in the notebook as **Lemma A**, so the leg does not have to be
believed on the strength of a citation it cannot open.

---

## 1 · What the computation supports

### 1.1 Route (a) — exhaustive check to `10¹¹`

**`F` holds at every `n` with `p_n < 10¹¹`.** 4 118 054 812 consecutive prime
pairs, exhaustive, no pruning, no sampling, no assumed lemma.

The protocol is two-tier, and the tiering is the point:

- **screen** — float64 over all pairs, on `ρ_n = g_n/T_n` (**D6**). `ρ_n` has
  `O(1)` operands, so it does not carry the cancellation that kills the
  `F2`-margin statistic (§2.1).
- **escalation** — every pair with `ρ_n ≥ 0.90` is re-decided in `Decimal` with
  an explicit error budget, and `certified_verdict` **raises** rather than
  returns when the margin lands inside that budget. Card **T2** Rule 3 names the
  hazard exactly: *the silent failure is in the verification direction*, so a
  probe that only breaks on a detected violation reports "no counterexample"
  from noise. This one cannot.
- **calibration** — the `Decimal` path is checked against the exact integer
  criterion `p_{n+1}ⁿ < p_nⁿ⁺¹` for every `n ≤ 5000`. **Zero disagreements.**

Only two pairs in the whole range reach `ρ ≥ 0.9`, and both are at `n < 5`
(`ρ₂ = 0.9107`, `ρ₄ = 0.9120`) — which is why cards **D6**/**T2** quote the
record for `n ≥ 10`.

| statistic | value |
|---|---|
| pairs checked | 4 118 054 812 |
| violations (`ρ_n ≥ 1`) | **0** |
| max `ρ_n` (`n ≥ 10`) | **0.8317570** at `n = 1 094 330 259`, `p_n = 25 056 082 087`, `g = 456` |
| max `c_n = g/L²` (`n ≥ 10`) | 0.7953487, same prime |
| largest gap in range | 464 at `p = 42 652 618 343` |
| maximal-gap records in range | 40 |

### 1.2 Reproduction of the run's existing figures

Independent code path, same numbers to the last digit quoted, at `N = 3·10⁶`:

| quantity | this leg | prior in-run figure |
|---|---|---|
| max `ρ` (`n ≥ 10`) | 0.7604709 at `n=217`, `p=1327`, `g=34` | card **D6**: 0.7604709 |
| runner-up `ρ` | 0.7590821 at `p = 2 010 733` | card **D6**: 0.759 |
| max `c` (`n ≥ 10`) | 0.7025656 at `p = 2 010 733` | card **T2**: 0.70257 |
| max `F2` margin | 0.9999984 | `decompose` §5.1: 0.9999984 |
| maximal-gap records below `3·10⁶` | 21 | card **L15**: 21 |

These are asserted in `test_fb_core.py`, so a future leg that breaks them breaks
the test suite.

### 1.3 Lemma A — the unconditional half, derived here

> **Lemma A.** Let `x := p_n ≥ 60184` and `L := log x`. Then `T_n ≥ L(L − 1.1)`.
>
> *Proof.* `T_n = x(e^{L/n} − 1)` with `n = π(x)` (**D3** — the index of a prime
> *is* its counting function). Dusart (2010) Thm 6.9 eq. (6.6) gives
> `π(x) ≤ x/(L − 1.1)` for `x ≥ 60184`, hence `L/n ≥ L(L−1.1)/x`. The map
> `u ↦ x(e^u − 1)` is increasing and `e^u − 1 ≥ u`, so
> `T_n ≥ x(e^{L(L−1.1)/x} − 1) ≥ L(L−1.1)`. ∎

**The direction is the content.** `T_n` decreases in `n` at fixed `p_n`
(**D5**), so lower-bounding `T_n` needs an **upper** bound on the index — which
is what Dusart's upper bound on `π` supplies. Card **T3** names this asymmetry
(verification consumes an upper bound on the rank, refutation a lower one);
Lemma A sits on the verification side and uses the correct one.

**Falsification-tested, not asserted:**

- over every prime in `[60184, 10¹¹]`, `min(T_n − L(L−1.1)) = +0.0798914728…` —
  the lemma holds, and the minimum is attained at the very bottom of the range.
- the validity range is **load-bearing, not decoration**: `L(L−1.1)` crosses
  `L² − L − 1` (the true asymptotic size of `T_n`, card **L2**) exactly at
  `L = 10`, i.e. `x = e¹⁰ = 22026`. Below that the lemma's conclusion is *false*.
  Dusart's `x ≥ 60184` clears it, but only by `≈ 0.10` at the boundary.

> **Corollary A1.** For `p_n ≥ 60184`: `g_n ≤ 108 ⟹ F` holds at `n`.
> (`L(L−1.1) = 109.0079…` at `x = 60184`, increasing thereafter.)

### 1.4 Corollary A2 — the reduction to a finite table, and its safety factor

> **Corollary A2.** A gap of size `g` can violate `F` only at a prime
> `p_n ≤ S(g) := exp((1.1 + √(1.21 + 4g))/2)`, for `p_n ≥ 60184`.

**Why the table test is sound.** Fix `n` with `p_n < X`. Either `g_n ≤ 108` and
Corollary A1 settles it (for `p_n ≥ 60184`; below that §1.1 checked it exactly),
or `g_n ≥ 110` and `p_n ≥ P₁(g_n) > S(g_n)` — the first inequality because `P₁`
is by definition the smallest prime carrying that gap — whence `g_n < L(L−1.1)
≤ T_n`. Note that a gap size which passes is safe **everywhere**, not merely
below `X`: `S(g)` does not depend on `X`.

Applied to the in-run table, complete for every gap size occurring below `10¹¹`:

| | |
|---|---|
| gap sizes occurring below `10¹¹` | 209 (largest 464) |
| of which `S(g) < 60184` — excluded by Cor. A1 | 55 |
| of which need the table test | 154 |
| **UNSETTLED** | **none** |
| **minimum safety factor `P₁(g)/S(g)`** | **5.337 at `g = 112`** |
| maximum safety factor | 203.9 at `g = 334` |

`safe_bound_S` rounds **up** and `gap_needed` rounds **down**, so every "safe"
verdict is conservative in the direction that matters.

**The finding a null result cannot give you:** the safety factor is neither flat
nor shrinking — it grows roughly linearly in `g` across the whole range, and its
minimum sits at the *small* end (`g = 112`), not at the frontier. Over
`[60184, 10¹¹]`, route (b) gets **easier** as the range extends. That is the
empirical shape of the Cramér-side expectation (**L9**) rather than the
Granville-side one (**L10**) — *over this range and no further*; see §4.

### 1.5 The certificate that scales

Route (b) as run above still consumed a complete first-occurrence table, hence a
complete sieve. The form that scales past any sieve needs only the **maximal-gap
record table**: split `[60184, X]` into geometric windows `[a,b)` and check

```
max{ g_n : p_n < b }  <  L(L−1.1) |_{L = log a}.
```

All 22 windows covering `[60184, 10¹¹]` certify, consuming **the 40 maximal-gap
records** and nothing else — no sieve, no `π(x)` computation, no per-prime check.
This is the shape in which a frontier like `2⁶⁴` is actually certified, and it is
implemented and validated here on data the run owns.

### 1.6 Independent reproduction of the `1920` constant

`L(L−1.1)` at `2⁶⁴` is **1919.1379834975…**, so a gap of at least 1920 is
required to violate `F` at a prime just below `2⁶⁴`. Card **L6** records
Kourbatov's 2023 endnote: *"prime gaps of size `g < 1920` cannot violate (1)"*.
The published integer falls out of Lemma A with no tuning — a genuine
cross-check on both.

**With a caveat this leg insists on.** What Lemma A yields is the *local*
statement at the frontier. The endnote's phrasing is a *global* claim, and Lemma
A alone does not give it: `S(1918) = 1.82·10¹⁹`, so our bound leaves a gap of
1918 free to violate `F` anywhere below `1.82·10¹⁹`. Closing that needs the
first-occurrence table again. The two statements agree numerically at `2⁶⁴` and
are logically different — the same species of conflation card **L6** hazard 1
warns about for the three circulating frontier figures.

---

## 2 · What the computation refutes

**Nothing about `F`.** Three claims **about the evidence**:

### 2.1 The `F2` margin is an artefact, not a measure of tightness

`decompose` §5.1 headlines `max n·log p_{n+1}/((n+1)·log p_n) = 0.9999984` and
reads it as the conjecture nearly failing. Card **T2** Rule 2 says it is a `1/n`
artefact. Demonstrated, with a synthetic control:

| | `10⁷` | `10⁸` | `10⁹` | `10¹⁰` | `10¹¹` |
|---|---|---|---|---|---|
| max `F2` margin | 0.99999937 | 0.99999994 | 0.999999993 | 0.9999999992 | 0.99999999992 |
| max `ρ` (`n ≥ 10`) | 0.7605 | 0.7896 | 0.7896 | 0.7896 | 0.8318 |

In a **synthetic universe where every gap is 2** (`q_n = 2n+1`, `F` true by a
mile), the `F2` margin reads `0.99999991` at `n = 10⁷` — indistinguishable from
the figure quoted as evidence of tightness — while `ρ_n` there is `0.059`, an
order of magnitude below the bar. The statistic measures `1/n`. Every number in
this leg is in `ρ` or in gap units.

### 2.2 "The tightest `ρ` cases sit at record gaps" does not survive the range

Card **L15** hazard 3 already showed that `decompose`'s finding *"all six
tightest `ρ` cases occur at record gaps"* was a `best[:6]` print truncation,
breaking to 8/10 and 15/100 at `3·10⁶`. At `10¹¹`: **22 of the top 40**, and the
**4th-tightest case in four billion pairs is not at a record index**
(`g = 444` at `p = 36 172 730 063`, `ρ = 0.78502`).

*Read this precisely:* if P6′ holds, a record-index search still misses no
*counterexample*. What it misses is *near-misses* — so record indices are not
where the tight cases live, and the observation cannot be used as evidence for
the pruning rule that produced it.

### 2.3 More sieve is not more evidence — with one exception

Three decades of extra sieving (`10⁸ → 10¹⁰`, 5.8 M pairs to 455 M) produced **no
new near-miss**: the record `ρ` sat at `0.7896` (`g = 210`, `p = 20 831 323`)
throughout. It moved exactly once, at `10¹¹`, and it moved *at the next maximal
gap* (`g = 456`, `p = 25 056 082 087`, `ρ = 0.8318`). Sieving buys the next
maximal gap and nothing in between.

Card **T2** is nonetheless right that this range cannot be informative about the
record: `ρ = 0.94846` at `p = 1.693·10¹⁵` (card **L7**) is **4.2 decades** above
`10¹¹`. The compute that would matter goes into gap *tables*, not prime *counts*.

---

## 3 · The one unexpected result: P6′ (card **L15**) has a shrinking margin

Card **L15** calls the maximal-gap reduction *"the single most tractable open
obligation in the attack"*:

> **P6′.** For `m` the governing record (maximal-gap) index below `n`, `T_m ≤ T_n`.

It is **unproved**, and its entire empirical base was *0 exceptions in 216 815
pairs* (`p < 3·10⁶`). The sweep of §1.1 already carries every quantity it needs,
so it was checked at no extra cost — and, more usefully, its **margin** was
measured rather than just its exception count:

| range | records | P6′ exceptions | `min(T_n − T_{m(n)})` | relative |
|---|---|---|---|---|
| `3·10⁶` | 21 | **0** | `+1.046·10⁻²` | `+5.4·10⁻⁵` |
| `10⁷` | 22 | **0** | `+6.060·10⁻³` | `+2.8·10⁻⁵` |
| `10⁸` | 25 | **0** | `+1.112·10⁻³` | `+3.8·10⁻⁶` |
| `10⁹` | 30 | **0** | `+1.120·10⁻⁴` | `+3.3·10⁻⁷` |
| `10¹⁰` | 35 | **0** | `+2.495·10⁻⁵` | `+6.0·10⁻⁸` |
| `10¹¹` | 40 | **0** | `+2.933·10⁻⁶` | `+5.1·10⁻⁹` |

**Zero exceptions everywhere** — P6′ survives a 4.5-decade extension of its
empirical base. But the margin at its tightest point **shrinks like `p^-0.83`**
(fitted), while the quantity being compared grows like `log²p`. The tightest point
is always the same structural spot: a few indices *after* a record gap, where `T`
has jumped up across the record and then drifted back down toward `T_m`.

Three consequences, in decreasing order of confidence:

1. **The empirical case for P6′ does not strengthen with range — it weakens.**
   This is the opposite of the reading in card **L15** (*"the dip decays and the
   margin grows"*), and the discrepancy is not a contradiction: the card's two
   statistics measure `T`'s excursion below its own running maximum, whereas the
   quantity P6′ actually needs is `T_n − T_{m(n)}`, measured here.
2. **A float64 check of P6′ hits the noise floor at the published frontier.**
   Fitting the five measured margins gives `margin ≈ 10^3.60 · p^-0.828`. One ulp
   of `T ≈ log²p` at `2⁶⁴` is `4.269·10⁻¹³`; the extrapolated margin there is
   `4.457·10⁻¹³` — **a ratio of 1.04**, and the fitted crossover sits at
   `p ≈ 10^19.3`, which is where `2⁶⁴` sits. Past that point a `float64` check of
   P6′ returns "no exceptions" whether or not there are any: silent, and in the
   reassuring direction — exactly card **T2** Rule 3's hazard, in a new place.
   *(Five points across four decades: this is an extrapolation, not a theorem.
   The coincidence of the crossover with `2⁶⁴` should be read as "the same order
   of magnitude", not as a prediction. The* ordering *is the finding, not the
   location, and it is a warning about method, not a claim about `T`.)*
3. **The route to discharging P6′ must therefore be the analytic one card L15
   already names** — bound `T`'s oscillation with Dusart (card **T1**) and compare
   against record-gap spacing — because the computational route is running out of
   resolution rather than accumulating confidence.

This is a **cosmon-ward observation for cards L15 and T2**, not a patch applied
quietly downstream: L15's "on the evidence this is a Dusart lookup" is still
plausible, but the evidence cited for it does not bear on the inequality, and the
evidence that does bear on it points the other way.

---

## 4 · At what scale — and the honest ceiling

| claim | established to | short of `2⁶⁴` by |
|---|---|---|
| route (a), per-pair exhaustive | `p < 10¹¹` | **8.27 decades** |
| route (b), per-gap-size, from in-run data | every gap size occurring below `10¹¹` | — |
| published frontier (card **L6**, *not* re-run here) | `p < 2⁶⁴` | — |

**The frontier of `2⁶⁴` is not established by this notebook**, and the leg
declines to imply otherwise. What it does establish is that the distance between
what we own and that frontier is now **exactly one external table with exactly one
inequality to check against it**:

> for every even `g` occurring as a prime gap in `[10¹¹, 2⁶⁴]`: `P₁(g) > S(g)`
> — equivalently, in window form: for every `[a,b) ⊂ [10¹¹, 2⁶⁴]`,
> `max{g : p < b} < L(L−1.1)|_{log a}`.

The checker for both is written (`lemma_A_certificate`, `window_certificate`) and
validated on data we own. **Supply the table and the frontier is re-derived here
in seconds.**

---

## 5 · Declared gaps

1. **The load-bearing external table was never opened.** Card **L6** names
   `oliveira2014goldbach` — the first-occurrence gap table to `4·10¹⁸` — at ledger
   tier **L2_weak, NOT OPENED** (AMS returned HTTP 403). Everything the run
   asserts about `2⁶⁴` is mediated through Kourbatov's use of it. This notebook
   does not repair that; it *localises* it to one table and one inequality.
2. **One external input is consumed and not verified here:** Dusart (2010)
   Thm 6.9 eq. (6.6). Card **T1** has it at **L0** (opened and read). Lemma A is
   the only place it enters, and every consequence drawn from it is checked
   numerically. Nothing else external is consumed anywhere in the notebook.
3. **The value 1550** ("81st maximal prime gap", the largest maximal gap below
   `2⁶⁴`) appears in §7 of the notebook as a *pointer for the citation gate*,
   recalled and not read. **It is not an input to any computation.** Do not let
   it become one without a ledger row.
4. **The safety-factor trend of §1.4 and the P6′ decay fit of §3 describe this
   range only.** Neither is evidence about the Cramér/Granville tension
   (**L9**/**L10**), whose disagreement lives far above any sieve, and neither may
   be cited as such.
5. **The `Decimal` certified path assumes `Decimal.ln()` is correctly rounded**
   to the working precision — documented CPython behaviour, cross-validated here
   against exact integer arithmetic for `n ≤ 5000`, but *assumed* above that. The
   exact integer criterion is the only unconditional decision procedure in the
   file, and it costs `O(n·log p)` digits, so it does not scale.
6. **The sweep is unpruned.** The pruning rule of card **L15** is undischarged and
   this leg deliberately did not use it, so the null result of §1.1 is about `F`,
   not about `F`-at-record-indices. §3 is a *measurement* of P6′, not a use of it.
7. **`F` remains open.** A verified range bounds where a counterexample can live
   and shrinks the difficulty of the general case by nothing (card **L6**,
   hazard 4). The obstruction identified in **L3** is untouched by every line of
   this notebook.

---

## 6 · Build / test status, reported honestly

```
$ python3 test_fb_core.py
--- test_sieve … test_certificate   (34 checks)
all checks passed                                        # exit 0

$ python3 build_notebook.py
wrote notebook-2.ipynb with 36 cells                     # exit 0

$ jupyter nbconvert --to notebook --execute --inplace notebook-2.ipynb
[NbConvertApp] Writing … bytes to notebook-2.ipynb       # exit 0, no cell raised
```

The notebook executes end to end with `N_NOTEBOOK = 10⁸` (seconds) and reads the
recorded `10⁷ … 10¹¹` runs from `deep-runs.json`, produced by `deep_run.py`
through the **same** `fb_core.scan` code path (`10¹¹` takes ~13 min). Both are
re-runnable from this directory with no network access and no data files.

One bug was found and fixed during the leg, and it is worth recording because it
is the kind that produces confident wrong numbers: the maximal-gap detector
initially carried the running record across segment boundaries incorrectly,
reporting 120 records below `10⁸` instead of 25 and manufacturing 124 spurious
P6′ "exceptions". It is now covered by a segment-size-invariance test
(`test_p6_prime`), and the record count is pinned against card **L15**'s
independent figure of 21 records below `3·10⁶`.
