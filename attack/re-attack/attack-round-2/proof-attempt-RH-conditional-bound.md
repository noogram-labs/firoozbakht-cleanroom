# Proof attempt, round 2 — subquestion `RH-conditional-bound`

**Molecule:** `task-20260726-b335` (leg `proof-attempt`, RE-ATTACK round 2)
**Parent loop:** `reattack-20260726-57d1` · **Date:** 2026-07-26 · **Formal backend:** Lean 4 / Mathlib
**Round-1 inputs re-read in full:** `attack/proof-attempt-1.md` (893 lines), `attack/faults.md`
(444 lines, molecule `task-20260725-488f`), `attack/lean-probe-report.md` (279 lines, molecule
`task-20260725-9975`), `attack/notebook-1/findings.md` (207 lines).

**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1` — equivalently
`(p_n)^{1/n}` strictly decreasing. **Status of `F` in this document: OPEN.** Nothing below asserts
it and nothing below refutes it. This leg attacks the subquestion only.

---

## 0. Verdict

| Sub-claim of `RH-conditional-bound` | Verdict | Where |
|---|---|---|
| **(1a)** The best explicit RH-conditional prime-gap bound *certifies* `F` (the chain `g_n ≤ B_n ≤ T_n` closes) | **REFUTED** — it closes at exactly one index of the range where the bound is available | Thm A §5.3 |
| **(1b)** *Some* bound `g_n ≤ C·p_n^θ(log p_n)^A`, `θ > 0`, certifies `F` beyond finitely many `n` | **REFUTED** | Thm B §6 |
| **(1c)** *Some* envelope `C√p log p` (any `C > 0`) certifies `F` beyond finitely many `n` | **REFUTED** | Thm C §7 |
| **(1d)** `RH ⟹ F` as a material implication | **UNDECIDED** — with the *strength of what a proof would yield* bounded below | Thm D §8 |
| **(1e)** Cramér's `limsup ≤ 1` hypothesis entails `F` over integer sequences | **REFUTED** (explicit counter-model) | Thm E §9 |
| **`F` itself** | **OPEN.** Untouched by this leg. | — |

**Headline, corrected — this is the load-bearing repair of round 2 (fault F4).**

> Under the Riemann Hypothesis the sharpest published prime-gap bound,
> `g_n ≤ (22/25)√p_n · log p_n` (Carneiro–Milinovich–Soundararajan, hypothesis `p_n > 3`),
> certifies the Firoozbakht inequality **at exactly one index in the range where that bound is
> available (`n ≥ 3`), namely `n = 3` (`p = 5`)**.

The clause "in the range where the bound is available" is not decoration. Round 1's headline read
"*and at no other index whatsoever*", and that is **false as stated**: the envelope `B_n` also sits
below the threshold `T_n` at `n = 1` and `n = 2`. What excludes those two indices is **the source's
hypothesis `p_n > 3`, not the arithmetic** — a materially different statement, and the one a reader
needs, because it locates the obstruction in the *range* of the cited theorem rather than in the
*shape* of the function. §5 now proves both statements separately: the arithmetic clearance set is
`{1,2,3}` (Theorem A°), the certified set is `{3}` (Theorem A).

That repair also removes a silent cross-artifact contradiction: `notebook-1` §1 F2 reports
`p*(22/25) = 5`, i.e. **three** certified primes `{2,3,5}`, against round 1's "one index … and no
other". Both artifacts were numerically right; the words were not. §5.4 reconciles them through a
single object — the **per-index critical constant** `C_n := T_n /(√p_n · L_n)` — of which both the
`p*(C)` table of `notebook-1` and the clearance set of Theorem A° are level sets. The two artifacts
now cite each other.

**What this document does *not* say.** It does not say `F` is false. It does not say `F` is harder
to prove than RH — that is the overreach card **L11** corrects. It says that the *route* named by
the subquestion is closed, with proofs rather than a scale-comparison slogan.

---

## 1. What round 2 changes

Round 1's artifact is `attack/proof-attempt-1.md`. Round-1's skeptic (`attack/faults.md`) raised
three findings against it. All three are repaired here; the mathematics of Theorems A–E is
**unchanged in substance**, and this is stated plainly rather than dressed as new progress.

| Round-1 fault | Severity | Status in this document |
|---|---|---|
| **F4** — headline "at no other index whatsoever" false as stated; `n ≥ 3` restriction dropped; conflict with `notebook-1` | **MAJOR** | **FIXED.** §0 headline, §5.2 (Theorem A°), §5.3 (Theorem A, quantified), §5.4 (explicit reconciliation with `notebook-1`), §13 summary. The two artifacts now cite each other by name. |
| **F8** — "essentially the whole verified range" glosses a real shortfall | MINOR | **FIXED.** §5.5 Remark 3 now carries the number: the unconditional range falls short of `2⁶⁴` by `8.674·10¹⁶`, i.e. `0.470 %`, i.e. `≈ 1.96·10¹⁵` primes. |
| **F9** — §9 Claim 2 draws a universal from one instance, and uses the *wider* of the two brackets card **T1** carries | MINOR | **FIXED.** §9 Claim 2 is now stated for **both** Dusart brackets of card **T1** — eq. (6.5) *and* the tighter eq. (6.6) — and its conclusion is scoped to those two named estimates instead of to "no unconditional estimate". The tighter bracket is the one now displayed. |

Round-1 findings **F1, F2, F3, F5, F6, F7, F10–F14** concern `proof-attempt-0.md`,
`proof-attempt-2.md`, `notebook-0`, `notebook-2` and card `L15`. They are **out of this leg's
perimeter** and are not touched here — with one exception, recorded because it is consumed in §5.4:
**F6** (the mistyped lower endpoint `10 ≤ p` in `notebook-1`'s definition of `p*(C)`). §5.4 reads
that definition with the corrected endpoint `2 ≤ p ≤ P`, states that it is doing so, and shows the
table's values are reproduced exactly under that reading — which is also what the skeptic found.

The skeptic's §5 re-verified, independently, five load-bearing items of round 1 and returned them
**clean**: Lemma A.1, Theorem A's six-row table ("only the `n ≥ 3` framing is at fault"), Theorem C
including the Lambert-`W` endpoints and prime counts, Corollary D.1's `8.72·10⁷`, and Theorem E's
whole construction. Round 2 does not re-litigate those; it re-runs them from their *statements*
(§10) and reports agreement.

---

## 2. Perimeter and provenance

**Inputs admitted:**

| Input | Provenance |
|---|---|
| `attack/concept-cards/` (30 cards) — **pinned, reused verbatim** | leg `concept-cards`, molecule `task-20260725-068e` |
| `attack/source-ledger.md` (20 rows) — **not re-opened** | leg `source-ledger`, molecule `task-20260725-d320` |
| `attack/proof-attempt-1.md` | round 1, molecule `task-20260725-5fcc` |
| `attack/faults.md` | round 1 skeptic, molecule `task-20260725-488f` |
| `attack/lean-probe-report.md` | round 1 kernel, molecule `task-20260725-9975` |
| `attack/notebook-1/findings.md` | round 1, molecule `task-20260725-c885` |
| `lean/` skeleton — **FROZEN, not touched** | molecule `task-20260725-5fd9` + round-1 probe |
| in-round computation by this leg | `attack-round-2/probe_rh2.py`, output `attack-round-2/probe_rh2.out` |

**Bounded source refresh — what was added, and what deliberately was not.**
The brief permits adding **only** anchors the round-1 skeptic flagged as *missing*, and forbids
re-opening the ledger wholesale.

- The skeptic flagged **no missing anchor** against `proof-attempt-1.md`. Its two findings on this
  artifact (F8, F9) are both repairable **from material already in the run**: F8 from a number
  computable from two figures already quoted, F9 from Dusart eq. (6.6), which card **T1** already
  carries at an L0 locator and which round 1 simply did not use.
- Therefore **no new source was fetched by this leg, and no ledger row was opened, edited or
  proposed.** The two sources round 1 fetched (`carneiro2019fourier` tier **L1**;
  `visser2018andrica` tier **L0**) remain *proposed, not merged* — that is round 1's §11 item 4 and
  it is unchanged. They are cited here exactly as round 1 cites them, with their arXiv version pins
  (`arXiv:1708.04122v2`, `arXiv:1804.02500v3`), and with the same L1 caveat on CMS.
- The gaps round 1 declared for want of a source (Axler at L2_strong; a Schoenfeld-type RH-strength
  `π(x)` error term; RH's `Π₁` arithmetization) are **still open and still declared** (§11). Closing
  them would require fetching sources the skeptic did not ask for, which the brief forbids.

**On the target's name.** The slug `RH-conditional-bound` is not defined by the brief. §3 states the
five inequivalent propositions it can denote and attacks each separately. Conflating them is the
principal hazard of this leg — and, as F4 shows, conflating *the quantifier* inside reading (1a) is
the second.

---

## 3. Notation and imported facts

Throughout, `p_n` is the `n`-th prime, **1-indexed**, `p_1 = 2` (card **D1**). All logarithms are
natural.

```
L_n := log p_n                                                          (D2)
g_n := p_{n+1} − p_n                                                    (D2)
T_n := p_n · (p_n^{1/n} − 1)                                            (D5)
B_n := (22/25) · √p_n · L_n                    the CMS envelope, as a function of n (see §5.1)
```

**Fact 0 (gap form of `F`).** `F ⟺ ∀n ≥ 1 : g_n < T_n`.
*Source:* card **L1** (PROVEN; `kourbatov2015bounds` L0, `visser2019verifying` L0). Since round 1
this equivalence is additionally **machine-checked**: `attack/lean-probe-report.md` reports
`conjecture_iff_gap` and the whole chain `Conjecture ↔ ConjectureReal ↔ (∀ n ≥ 1, g_n < T_n)`
discharged with real proof terms, axiom-audited to `[propext, Classical.choice, Quot.sound]`, with
the single `sorryAx` in the development being `Firoozbakht.firoozbakht` itself
(`lean/Firoozbakht/Statement.lean:186`) — the open target, correctly open.
*Derivation, for self-containment:* `F` in log form is `log p_{n+1} < (1+1/n) log p_n`, i.e.
`p_{n+1} < p_n · p_n^{1/n}`, i.e. `p_n + g_n < p_n + p_n(p_n^{1/n} − 1)`. Each step is an
equivalence because `t ↦ log t` and `t ↦ e^t` are strictly increasing on the relevant range. ∎

**Fact 1 (`T_n < L_n²` off an explicit exception set).**
`{n : T_n ≥ L_n²} = {1,2,3,4,5,6,7,10}`.
*Source:* card **L13** (PROVEN; in-run computation + `dusart2010estimates` L0 Thm 6.9).
**Re-verified by this leg** for all `n ≤ 216 816` — check `[R2]`, exact match.
**Hazard imported with it:** L13's asymptotic half rests on Dusart's effective `π(x)` bounds; the
finite half is a computation. Below `p = 3·10⁶` this leg has confirmed it directly; above, it is
L13's claim, not a new one. (§11 item 12 states what Theorem A costs if L13's asymptotic half were
wrong: effectivity, not the theorem.)

**Fact 2 (necessary condition).** `F ⟹ g_k < L_k² − L_k − 1` for all `k > 9`.
*Source:* card **L3** (PROVEN; `kourbatov2015bounds` L0 §2 Thm 1).

**Fact 3 (sufficient condition).** `[∀k>9 (p_k ≥ 29): g_k < L_k² − L_k − 1.17] ⟹ F`.
*Source:* card **L4** (PROVEN; `kourbatov2015bounds` L0 §4 Thm 3).
**Hazard imported with it:** L4 hazard 4 — the chain runs through Axler's Corollary 3.5, **not
opened in this run**, whose validity range was moved by a corrigendum from `x ≥ 5.43` to
`x ≥ 2 634 800 823`. Every use of Fact 3 below is flagged.

**Fact 4 (verified range).** `F` holds for all `p < 2⁶⁴ = 1.8447·10¹⁹`.
*Source:* card **L6** (PROVEN computationally; `kourbatov2015verification` L0,
`visser2019verifying` L0).

**Facts 2 + 3 together (the sandwich).** `F` is trapped between two Cramér-scale gap bounds
differing by an additive `0.17`. §8 is where this does its work.

---

## 4. The imported RH-conditional bound, and its hypothesis

No source was fetched by this leg (§2). The bound below is quoted from the two sources **round 1**
fetched, at the locators round 1 read, with round 1's tiers.

**`carneiro2019fourier` — tier L1** (Carneiro–Milinovich–Soundararajan, "Fourier optimization and
prime gaps", *Comment. Math. Helv.* **94** (2019) 533–568; read as **arXiv:1708.04122v2**, MD5
`2fdff58bc850508d8f124b4e7ad6b594`). L1, not L0, because the locators are preprint locators against
a journal citation — the same standard the ledger applies to `granville1995cramer`.

| Locator | Exact statement |
|---|---|
| §1.2, sentence preceding Theorem 5 | "…assuming the Riemann hypothesis, prove that `p_{n+1} − p_n ≤ (22/25)√p_n log p_n` for all primes **`p_n > 3`**." |
| §1.2, Theorem 5 | "Assume the Riemann hypothesis. Then, for `x ≥ 4`, there is always a prime number in the interval `[x, x + (22/25)√x log x]`." |
| §1.2, Corollary 4, (1.14) | Assume RH. Then `limsup (p_{n+1}−p_n)/(√p_n log p_n) ≤ 1/C⁺(B) < 21/25`. |
| §1.2, after (1.14) | "the limit of this method would yield a constant `1/2` on the right-hand side of (1.14)." |
| §1.2, after (1.14) | "under … the Riemann hypothesis and Montgomery's pair correlation conjecture, **it is known** that the limit supremum in (1.14) is actually zero (see, for instance, [26, 27, 35])." — CMS report this, do **not** prove it; **tier L2_weak**, attributed second-hand wherever used (§7). |

**`visser2018andrica` — tier L0** (Matt Visser, "Variants on Andrica's conjecture with and without
the Riemann hypothesis"; read as **arXiv:1804.02500v3**, MD5 `38b405e83543fb6968754f90bac9c2d4`).

| Locator | Exact statement |
|---|---|
| Theorem 1, eq. (1.4) | "Assuming the Riemann hypothesis, **`∀n ≥ 3, p_n ≥ 5`**, `g_n := p_{n+1} − p_n < (22/25)√p_n ln p_n`." Attributed to CMS. |
| §2, Theorem 4 (2.1) | "(Cramer 1919). Assuming RH, `g_n = O(√p_n ln p_n)`" + "only qualitative, not quantitative, information". |
| §2, Theorem 5 (2.2) | "(Goldston 1982). Assuming RH, `g_n ≤ 4√p_n ln p_n`; `n` sufficiently large." |
| §7 | The CMS inequality is verified **unconditionally** for all primes `< 1.836·10¹⁹`. |
| §8 | "While the Riemann hypothesis provides … a nice explicit bound on prime gaps, it is still not quite sufficient to prove Andrica's conjecture." |

**The hypothesis is the whole point of round 2.** Both sources carry a range restriction, and they
agree on it: CMS write `p_n > 3`; Visser writes `n ≥ 3, p_n ≥ 5`. Over the primes,
`p_n > 3 ⟺ p_n ≥ 5 ⟺ n ≥ 3`, so the two hypotheses are the same hypothesis. Round 1 recorded this
and then dropped it when quoting its own theorem downstream. §5 keeps it attached.

**The `≤` vs `<` discrepancy** (CMS `≤`, Visser `<`) is recorded, not smoothed. Every argument below
uses the bound only as a **non-strict upper envelope**, so the discrepancy is inert here; it must
still be resolved before any paper states one form. (§11 item 4.)

---

## 5. Theorem A — the certification set, with its quantifier attached

This section is the repair of fault **F4**. It separates two statements that round 1 ran together.

### 5.1 Two definitions that must not be confused

`B_n := (22/25)·√p_n·L_n` is a **function of `n`, defined for every `n ≥ 1`** — nothing in its
definition knows about CMS. What CMS supplies is an implication with a hypothesis:

```
(CMS)      RH   ⟹   ∀ n ≥ 3 :  g_n ≤ B_n .                        [§4, both sources]
```

Accordingly there are two sets, and they are different:

```
A   :=  { n ≥ 1 : B_n < T_n }            the ARITHMETIC clearance set  — a fact about two functions
S   :=  { n ≥ 3 : B_n ≤ T_n }            the CERTIFICATION set        — where (CMS) closes the chain
```

`S = A ∩ [3, ∞)`, because every comparison of `B_n` against `T_n` at the indices that matter is
strict (Theorem A° and its proof), so the `<` in `A` and the `≤` in `S` select the same indices;
Lemma A.0 is the separate step that turns membership in `S` into `F` holding at that index. Round 1
proved `S = {3}`
correctly and then quoted it as a statement about `A`. It is not one: `A ⊋ S`.

**Lemma A.0 (non-strict certification upgrades to strict).** Let `n ≥ 3` and suppose `B_n ≤ T_n`.
Then RH implies `g_n < T_n`, i.e. `F` holds at `n`.

*Proof.* RH gives `g_n ≤ B_n ≤ T_n` by (CMS), whose hypothesis `p_n > 3` is exactly `n ≥ 3`. It
remains to exclude equality. `g_n` is an integer, while
`T_n = p_n·p_n^{1/n} − p_n` is irrational: for `n ≥ 2` the number `p_n^{1/n}` is irrational — were
it rational, being a root of `X^n − p_n ∈ ℤ[X]` (monic), the rational root theorem would force it to
be an integer, so `p_n` would be a perfect `n`-th power, which unique factorisation forbids for a
prime. Hence `p_n·p_n^{1/n}` is irrational, `T_n` is irrational, and `g_n ≠ T_n`. ∎

*(The irrationality step needs `n ≥ 2`, and that restriction is real: `T_1 = p_1(p_1 − 1) = 2` is an
integer. It costs nothing here, since Lemma A.0 is applied only at `n ≥ 3`, and the `n = 1` row of
Theorem A° is decided by a strict inequality directly.)*

### 5.2 Theorem A° — the arithmetic clearance set

> ### Theorem A° (arithmetic; no hypothesis, no RH)
> ```
> A  =  { n ≥ 1 : B_n < T_n }  =  { 1, 2, 3 } ,
> ```
> and the same set is obtained with `≤` in place of `<`: every comparison involved is strict.

**Proof.** Two lemmas and a finite check over exactly the exception set of Fact 1.

**Lemma A.1.** For every real `x > 0`, `√x > (25/22)·log x`. Equivalently
`(22/25)√x·log x > (log x)²` for all `x > 1`.

*Proof.* Put `k := 25/22` and `h(x) := √x − k log x` on `(0,∞)`. Then
`h′(x) = 1/(2√x) − k/x = (√x − 2k)/(2x)`, which is negative for `√x < 2k` and positive for
`√x > 2k`. So `h` has a unique stationary point at `x* = (2k)² = (25/11)² = 625/121`, and it is the
global minimum (`h → +∞` as `x → 0⁺`, because `−k log x → +∞`; `h → +∞` as `x → ∞`, because `√x`
dominates `log x`). At that point

```
h(x*) = 25/11 − (25/22)·log(625/121) = 2.272727… − 1.136363…·1.641961…
      = 0.4068623816594768…  >  0 .
```

Hence `h > 0` on all of `(0,∞)`. For `x > 1` multiply `√x > k log x` by `log x > 0` and divide by
`k`: `(22/25)√x log x > (log x)²`. ∎
*(In-round check `[R1]`, 50 digits: `x* = 5.1652892561983471…`, `h(x*) = 0.40686238165947680…`.
Round-1 value and the skeptic's independent recomputation both agree to every digit quoted.)*

**Lemma A.2.** For every `n ≥ 1`, `B_n > L_n²`.

*Proof.* Lemma A.1 at `x = p_n ≥ 2 > 1`. ∎
*(Note this holds at **every** index, `n = 1` included — the CMS hypothesis plays no role in it,
because `B_n` is just a function. That is precisely why `A` can be, and is, larger than `S`.)*

**Completion.** Let `n ≥ 1`.

- If `n ∉ {1,…,7,10}` then Fact 1 gives `T_n < L_n²`, and Lemma A.2 gives `B_n > L_n² > T_n`. So
  `n ∉ A`. This disposes of every index outside a set of eight.
- The eight remaining indices are checked directly (50-digit arithmetic, check `[R3]`); all eight
  comparisons are strict, so `<` and `≤` agree on them:

| `n` | `p_n` | `T_n` | `B_n` | `B_n < T_n` ? |
|---:|---:|---:|---:|:---:|
| **1** | **2** | **2.0000000000** | **0.86262716625** | **yes** |
| **2** | **3** | **2.1961524227** | **1.6745100256** | **yes** |
| 3 | 5 | 3.5498797334 | 3.1669550684 | **yes** |
| 4 | 7 | 4.3860359319 | 4.5305870087 | no |
| 5 | 11 | 6.7693369282 | 6.9985686377 | no |
| 6 | 13 | 6.9342810812 | 8.1382896560 | no |
| 7 | 17 | 8.4816378252 | 10.279841332 | no |
| 10 | 29 | 11.610449607 | 15.957429839 | no |

Hence `A = {1,2,3}`. ∎

*(The two bold rows are the content of fault F4. They are not new mathematics — the skeptic
computed them independently at 40 digits and this leg reproduces them at 50 — they are the two rows
round 1's finite check never printed, because round 1's check started at `n = 3`, exactly where its
theorem started. A check that inherits the theorem's range cannot detect that the range is doing
work; cf. `faults.md` §6 item 2.)*

### 5.3 Theorem A — the certification set

> ### Theorem A (certification under RH, quantified)
> Let `S := { n ≥ 3 : B_n ≤ T_n }` be the set of indices at which the CMS envelope certifies `F`
> — i.e. at which the chain `g_n ≤ B_n ≤ T_n` supplied by (CMS) closes. Then
> ```
> S  =  { 3 } .
> ```
> **In words, with the quantifier that must travel with it:** the sharpest published RH-conditional
> prime-gap bound certifies the Firoozbakht inequality at **exactly one index in the range where
> that bound is available (`n ≥ 3`), namely `n = 3` (`p_3 = 5`)**, and at no other index of that
> range.

**Proof.** `S = A ∩ [3,∞)` by definition together with the strictness observation of Theorem A°
(`<` and `≤` define the same set here). Theorem A° gives `A = {1,2,3}`, so `S = {3}`. By Lemma A.0
the certification at `n = 3` is genuine: RH gives `g_3 ≤ B_3 < T_3`, hence `g_3 < T_3`, hence `F` at
`n = 3`. ∎

**The two excluded indices, stated as the repair requires.** `1, 2 ∈ A \ S`. They are excluded
from `S` **by the hypothesis `p_n > 3` of the cited theorem, not by the arithmetic**: at `n = 1, 2`
the envelope sits comfortably below the threshold (`0.863 < 2.000`, `1.675 < 2.196`), and no
inequality in this document fails there. What fails there is *availability*: CMS assert nothing
about `g_1` or `g_2`, so nothing can be chained. Saying "at no other index whatsoever" misplaces the
obstruction — from the *source's range* to the *function's shape* — and that is the error round 1
shipped in its headline and its summary.

**A remark that keeps the repair from being over-read.** Suppose, counterfactually, that the CMS
inequality were also known at `n = 1, 2`. Then the certified set would be `A = {1,2,3}` — **three**
indices — and every conclusion of this document would stand unchanged, because three is still
finite, still contained in `{p ≤ 5}`, and still below every threshold at which the literature's
criteria begin (Facts 2 and 3 both require `k > 9`). The quantifier repair changes what the sentence
*means*; it does not rescue the route. Round 2 states both halves.

### 5.4 Reconciliation with `notebook-1` — the per-index critical constant

This subsection exists because `faults.md` F4 records a **visible cross-artifact conflict**:
`notebook-1/findings.md` §1 F2 reports `p*(22/25) = "p ≤ 5"` — three certified primes — while
round 1's `proof-attempt-1.md` reported "one index … and no other", **and neither artifact cited the
other**. Both were right. Here is the object that makes that visible in one line.

**Definition.** For `n ≥ 1` put the **per-index critical constant**

```
C_n  :=  T_n / (√p_n · L_n) .
```

Then for any constant `C > 0`, writing `B_C(p_n) := C√p_n L_n`,

```
B_C(p_n) < T_n     ⟺     C < C_n .                                      (★)
```

So *every* statement of the form "the envelope with constant `C` clears the bar at `n`" is a
statement about where `C` sits relative to the sequence `(C_n)`. Both artifacts measure `(C_n)`;
they report different functionals of it.

| `n` | `p_n` | `C_n` |
|---:|---:|---:|
| 1 | 2 | 2.0402789 |
| 2 | 3 | 1.1541371 |
| 3 | 5 | 0.98640306 |
| 4 | 7 | 0.85192308 |

*(In-round `[R7]` and the auxiliary evaluation in §10; `C_n → 0` as `n → ∞`, since `T_n = L² − L − 1
+ o(1)` by card **L2** gives `C_n ≍ L_n/√p_n`.)*

- **`proof-attempt-1` / Theorem A° measures a level set:** by (★), `A = {n : C_n > 22/25}`, and
  Theorem A° says that level set is `{1,2,3}`. Where the work is done: Lemma A.2 together with
  Fact 1 gives `C_n < 22/25` for every `n ∉ {1,…,7,10}` in one stroke; the eight exceptional indices
  are the finite check, and on them `22/25 = 0.88` separates `C_3 = 0.986` from `C_4 = 0.852`.
- **`notebook-1` §1 F2 measures the initial segment:** `p*(C) :=` the largest `P` with
  `B_C(p) < T(p)` for **all** primes `2 ≤ p ≤ P`. By (★), `p*(C) = p_m` where
  `m = max{ m : C < C_n for all n ≤ m }`.
  *(Read with the corrected lower endpoint `2 ≤ p ≤ P`. `notebook-1` prints `10 ≤ p ≤ P`, which
  would make the condition vacuous for the reported values — that is `faults.md` **F6**, a typo in
  the definition, not in the table. This leg reproduces the whole table under the corrected
  reading; see `[R7]`.)*

**They agree, and here is why the agreement is not a coincidence.** In general a level set and an
initial segment are different objects, and they need not coincide: `C_n` is **not** monotone (it
inherits the oscillation of `T_n`, which descends at a large fraction of steps — card **D5** /
**L15**; the exact fraction is contested across artifacts, `faults.md` **F5**, and is not needed
here). What makes them coincide at `C = 22/25` is Theorem A°: it confines the level set inside
`{1,2,3}`, and on those three indices `C_n` *is* strictly decreasing (`2.040 > 1.154 > 0.986`), so
every level set inside them is an initial segment. Hence:

```
A = {1,2,3}          (Theorem A°, this document)
p*(22/25) = 5        (notebook-1 §1 F2)   ⟺   the certified indices are exactly 1, 2, 3
```

— **the same three indices, the same three primes `{2,3,5}`.** Reproduced independently by this leg
at 50 digits, check `[R7]`:

| `C` | `p*(C)` — this leg | `notebook-1` §1 F2 | initial segment cleared, `{1,…,π(p*(C))}` |
|---|---:|---|---|
| `1` | `3` | `p ≤ 3` | `{1,2}` |
| `22/25 = 0.88` | `5` | `p ≤ 5` | `{1,2,3}` |
| `4/π = 1.27324` | `2` | `p ≤ 2` | `{1}` |
| `1/(8π) = 0.0397887` | `62 869` | `p ≤ 62 869` | `{1,…,6307}` |
| `10⁻²` | `1 772 591` | `≈ 1.77·10⁶` | `{1,…,133 145}` |

*(The last column is the **initial segment**, which is what `p*` measures. For `C ≥ 22/25` it is also
the full level set `{n : C < C_n}`, by Theorem A°; for the two small constants it need not be —
`C_n` oscillates, so isolated indices above `p*(C)` may also clear. Nothing here depends on that,
and no claim is made about them: `p*` is a statement about a prefix, and it is quoted as one.)*

Every row matches. **The conflict was verbal, not numerical**, and it is now closed in both
directions: this document quotes Theorem A with its quantifier and cites `notebook-1`; a downstream
`synthesize` or `write-paper` leg reading either artifact is pointed at the other.

**One inherited caveat, not repaired here.** `notebook-1` §4 item 3 states that all its literature
constants (`22/25`, `4/π`, `1/(8π)`, the `4·10¹⁸` range) are `[L3-recall]` and **unsourced in that
notebook**. For `22/25` this document supplies the anchor (§4, `carneiro2019fourier` L1 +
`visser2018andrica` L0, both read at the locator by round 1). `4/π` and `1/(8π)` are **still
unsourced in this run** and are quoted above only as *inputs to a reproduction of notebook-1's
table*, never as literature claims. **[GAP: no ledger row for `4/π`, `1/(8π)`.]**

### 5.5 Remarks

1. **The single certified index is worthless for `F`.** `n = 3` means `p = 5`; `F` at `n = 3` is
   `7³ = 343 < 5⁴ = 625`, decidable by hand — and it is inside the range the Lean development
   already discharges by `norm_num` (`firoozbakht_le_four`, `lean-probe-report.md`). Moreover `n = 3`
   sits below the `k > 9` threshold that **both** Kourbatov criteria (Facts 2, 3) carry by
   hypothesis. So the CMS envelope's entire contribution to `F` lies in a range that every criterion
   in the literature excludes by hypothesis and that direct computation settles. **Under the F4
   repair this remark gets stronger, not weaker:** even counting the two arithmetically-clear
   indices `n = 1, 2`, the total contribution is `{p ≤ 5}`.
2. **The near miss at `n = 4` is not a near miss in disguise.** `[R5]`: the minimum of `B_n/T_n`
   over `4 ≤ n ≤ 216 816` is `1.032957111858…`, attained at `n = 4` (`p = 7`) — a `3.3 %` shortfall.
   From there the ratio grows *in scale* though **not monotonically**: counting steps `n → n+1` with
   `n ≥ 4` and both endpoints inside the sieve (216 812 steps), the ratio falls at **29 770** of them
   (`13.73 %`), the first at the step `9 → 10`. *(Convention stated because `faults.md` **F5**
   records three mutually incompatible fractions circulating in this run for a statistic of exactly
   this kind, each under an unstated step convention. Round 1 reported `29 769 / 216 811` for the
   same quantity — one step fewer at each end, consistent with an endpoint convention it did not
   state. The discrepancy is recorded, not smoothed; nothing here depends on it, since the claim used
   is only "not monotone". The companion statistic — `T_n` itself descending at ≈`55.9 %` of steps,
   card **D5** / **L15** — is quoted qualitatively for the same reason: its exact fraction is one of
   the three F5 contests, and this leg is not in scope to settle it.)* The trend is what matters:
   `110.1536` at
   `p = 2 999 999`, and `8.72097·10⁷` at `p = 2⁶⁴` — the envelope overshoots the threshold by roughly
   **eight orders of magnitude exactly where a proof would have to work**.
   *(The `2⁶⁴` figure uses the surrogate `L² − L − 1` for `T` (card **L2**), because `π(2⁶⁴)` is not
   computed here; round 1 records the true-rank value as `8.7213·10⁷`, a `0.004 %` difference.)*
3. **RH is not load-bearing in the range where the envelope is smallest — with the shortfall now
   quantified (fault F8).** By `visser2018andrica` §7 the CMS inequality holds **unconditionally**
   for all `p < 1.836·10¹⁹`, while the verified range (Fact 4) is `2⁶⁴ = 1.84467·10¹⁹`. Round 1
   wrote "essentially the whole verified range"; the number that word was hiding is:

   ```
   2⁶⁴ − 1.836·10¹⁹  =  8.6744·10¹⁶       ( 0.4702 % of 2⁶⁴ )
   primes in the shortfall window ≈ 8.6744·10¹⁶ / log(2⁶⁴) ≈ 1.96·10¹⁵ .
   ```

   `[R8]`. So the honest sentence is: over `99.53 %` of the verified range RH adds nothing that is
   not already known unconditionally, and what is already known still certifies `F` at no index
   above `n = 3`. The remaining `0.47 %` — about two quadrillion primes — is a window where the CMS
   inequality is *conditional*; nothing in this document uses that window, and the estimate
   `1.96·10¹⁵` is a PNT-scale count, not a certified one.

> **Verdict on (1a): REFUTED.** The best explicit RH-conditional prime-gap bound certifies `F` at
> exactly one index of the range where it is available (`n ≥ 3`), namely `n = 3`. Off that range,
> the envelope's arithmetic clearance extends only to `n = 1, 2` (Theorem A°) — three indices in
> total, all with `p ≤ 5`. The route is closed. *Not claimed:* that the material implication
> "`B ⟹ F`" is false — see §3 (1a) and §8 D.0 for why no method here can decide that.

---

## 6. Theorem B — no power-type envelope can ever suffice

Theorem A is about one published constant. The obstruction is structural.

> ### Theorem B
> Let `C > 0`, `θ > 0`, `A ∈ ℝ`. Define `E(x) := C·x^θ·(log x)^A`. Then
> ```
> #{ n : E(p_n) ≤ T_n }  <  ∞ ,        and in fact   E(p_n)/T_n → ∞ .
> ```
> No such envelope clears the threshold at more than finitely many indices, for any `C, θ, A`.

**Proof.** By Fact 1, `T_n < L_n²` for all `n ∉ {1,…,7,10}`, so it suffices to show
`E(x)/(log x)² → ∞`. Write `u := log x`; then `E(x)/(log x)² = C·e^{θu}·u^{A−2} → ∞` as `u → ∞`,
because `e^{θu}` with `θ > 0` dominates every fixed power of `u`. Since `p_n → ∞` and `T_n < L_n²`
eventually, `E(p_n)/T_n > E(p_n)/L_n² → ∞`. A divergent ratio is `≤ 1` only finitely often. ∎

**Note the quantifier discipline, applied here too.** Theorem B is a statement about **envelopes as
functions** — like Theorem A°, it has no hypothesis range. When an entry in the table below is a
*theorem with a hypothesis* (as CMS is), the verdict column reports what it certifies **inside its
own range**; the F4 lesson is that these are two different scores and the table must say which it
gives.

| Bound | Shape | `θ` | Certifies `F` beyond finitely many `n`? |
|---|---|---:|:---:|
| Baker–Harman–Pintz, unconditional (card **L11**, `baker2001difference` L1) | `g_n ≪ p_n^{0.525}` | 0.525 | **no** |
| Cramér 1919 under RH (`visser2018andrica` Thm 4, **L0**) | `g_n = O(√p_n log p_n)` † | 0.5 | **no** |
| Goldston 1982 under RH (`visser2018andrica` Thm 5, **L0**) | `g_n ≤ 4√p_n log p_n`, `n` large | 0.5 | **no** |
| Dudek under RH (`carneiro2019fourier` §1.2, **L1**) | `c = 1` in (1.10) † | 0.5 | **no** |
| CMS under RH, explicit (`carneiro2019fourier` §1.2, **L1**), hypothesis `p_n > 3` | `g_n ≤ (22/25)√p_n log p_n` | 0.5 | **no** — Thm A: one index in-range (`n = 3`); Thm A°: the envelope clears at `{1,2,3}` |
| CMS under RH, asymptotic (`carneiro2019fourier` Cor. 4, **L1**) | `limsup ≤ 1/C⁺(B) < 21/25` † | 0.5 | **no** |
| RH **+ Montgomery pair correlation** (`carneiro2019fourier` §1.2 after (1.14), **L2_weak** — CMS report it, do not prove it) | `limsup = 0`, i.e. `g_n = o(√p_n log p_n)` † | 0.5 | **no** — Cor. C.1 |
| **What certifies `F`** (Fact 3, card **L4**, `kourbatov2015bounds` **L0**; `k > 9`, `p_k ≥ 29`) | `g_k < L_k² − L_k − 1.17` | **0** | *this is the bar* |
| *(the necessary side, for contrast — Fact 2, card **L3**; do not read as an equivalence)* | `g_k < L_k² − L_k − 1` | **0** | — |

**†** These four rows are one `O`-statement and three `limsup` statements, not literally envelopes
of the form Theorem B quantifies over. Each *implies* such an envelope for every `C` above the
stated constant, from some index on, which is how the verdict column scores them; the strongest —
`limsup = 0` — is handled separately by Corollary C.1, because "for every `C`, beyond an
uncontrolled threshold" is a weaker input than "for one `C`, from a named index on".

The column that matters is `θ`. Every entry above the rule has `θ > 0`; the bar has `θ = 0`.
**Improving the exponent from `0.525` to `0.5` — exactly what RH buys — moves nothing across the
line drawn by Theorem B, because the line is at `θ = 0`, not at any positive value.**

> **Verdict on (1b): REFUTED.** No bound of power type, at any exponent `θ > 0`, any constant, and
> any logarithmic decoration, certifies `F` beyond finitely many indices.

---

## 7. Theorem C — the critical constant is `2/e`, and it does not help

The natural next move: `22/25 = 0.88` is not known to be optimal; CMS's Corollary 4 already gives an
asymptotic `< 21/25`, and CMS note that "the limit of this method would yield a constant `1/2` on
the right-hand side of (1.14)" — a floor on the **limsup constant of (1.14)**, not on a uniform
envelope valid from a named index. Could a future constant be small enough?

> ### Theorem C
> For `C > 0` let `E_C(x) := C√x·log x`. Then
> ```
> { x > 1 : E_C(x) ≤ (log x)² }  ≠  ∅   ⟺   C ≤ 2/e = 0.735758882342885… ,
> ```
> and when non-empty this set is the **bounded** interval `[x⁻(C), x⁺(C)]` with
> ```
> x^∓(C) = exp(−2·W_0(−C/2)),   exp(−2·W_{−1}(−C/2))
> ```
> (`W_0`, `W_{−1}` the two real branches of Lambert `W`). Consequently, for **every** `C > 0`, `E_C`
> clears the threshold `T_n` at only finitely many indices.

**Proof.** For `x > 1`, `E_C(x) ≤ (log x)² ⟺ C ≤ log(x)/√x =: φ(x)`. Now
`φ′(x) = (2 − log x)/(2x^{3/2})`, so `φ` increases on `(1, e²)`, decreases on `(e², ∞)`, and attains
its maximum `φ(e²) = 2/e² · e = 2/e` at `x = e²`. Hence the superlevel set `{x > 1 : φ(x) ≥ C}` is
non-empty iff `C ≤ 2/e`; being the superlevel set of a unimodal function tending to `0` at both ends
of `(1,∞)`, it is a compact interval. Solving `C√x = log x` with `t := log x` gives `t e^{−t/2} = C`,
i.e. `(−t/2)e^{−t/2} = −C/2`, i.e. `−t/2 = W(−C/2)`, whence the endpoints; two real branches exist
iff `−C/2 ≥ −1/e`, i.e. `C ≤ 2/e`, consistently. The set is bounded, so it contains finitely many
primes; off it, `E_C(x) > (log x)² > T_n` for every `n` outside Fact 1's exception set. ∎
*(In-round `[R6]`, 50 digits: `max_x log x/√x = 0.73575888234288464319… = 2/e` at
`x = e² = 7.38905609893…`.)*

**Read the table as a statement about `E_C(p) ≤ (log p)²`, not about certification of `F`.** The two
coincide off the exception set `{1,…,7,10}` of Fact 1, where `T_n < L_n²`; *on* that set clearance
is easier, and that is exactly where Theorem A°'s three indices live. By (★) of §5.4, clearing at
`n = 3` needs only `C < C_3 = 0.98640`, which `22/25 = 0.88` satisfies; clearing at `n = 1, 2` needs
`C < 2.0403`, `C < 1.1541`.

| `C` | Where `E_C(p) ≤ L²` is possible | Primes in range | Comment |
|---|---|---:|---|
| `22/25 = 0.88` (CMS explicit) | **empty** | 0 | Lemma A.2 |
| `21/25 = 0.84` (CMS Cor. 4 asymptotic) | **empty** | 0 | above critical |
| `2/e = 0.735759` (**critical**) | `{e²}` — a single point | 0 | — |
| `0.5` (floor of the CMS *limsup* constant, `1/C⁺(B) ≥ 1/2`) | `p ∈ (2.0438, 74.187)` | **20** | — |
| `0.1` | `p ∈ (1.1112, 8099.1)` | **1018** | — |
| `0.01` | `p ∈ (1.0101, 2 122 264.6)` | **157 340** | — |

*(All three counts reproduced by this leg, `[R6]`, and independently by the round-1 skeptic — see
`faults.md` §5 item 6.)*

Even a constant **fifty times smaller than anything the method can produce** buys a bounded initial
segment and then stops. Driving `C → 0` pushes `x⁺(C)` out only like `C⁻²` up to logarithmic factors
(from `x⁺ = (t/C)²` with `t = 2 log(t/C)`), while the verified frontier is already at `2⁶⁴`. To
clear the bar merely up to the *already-verified* range one would need
`C ≤ (L² − L − 1)/(√p·L) = 1.00906·10⁻⁸` at `p = 2⁶⁴` — i.e. **not a constant improvement but the
abandonment of the `√p` scale**. This is the same quantity as the per-index critical constant `C_n`
of §5.4, evaluated at the frontier via the `L² − L − 1` surrogate; `notebook-1` §1 F2 reports the
same figure from the other direction (`largest admissible C` at `4·10¹⁸`: `2.09·10⁻⁸`), and the two
agree in scale as they must.

**Corollary C.1 (even `limsup = 0` does not help).** CMS record (§1.2, after (1.14)) that under RH
*and* Montgomery's pair correlation conjecture the limsup in (1.14) is zero, i.e.
`g_n = o(√p_n log p_n)`. **Provenance, stated because it matters:** CMS do **not** prove this and do
not claim it — they write "it is known … (see, for instance, [26, 27, 35])", attributing it to three
works this run did not open. Under the ledger's scheme that is **tier L2_weak**, attributed
second-hand here, and flagged to the citation gate. **The corollary does not depend on the statement
being true** — it says that *even if* it holds, nothing is certified.

*First, and decisively: `o(√p log p)` is still enormously weaker than `O(log²p)`.* The hypothesis is
compatible with gaps far above the threshold: a growth rate `g_n = √p_n·L_n/log log p_n` satisfies
`g_n/(√p_n L_n) → 0` while `g_n/L_n² = √p_n/(L_n·log log p_n) → ∞`. So `o(√p log p)` does not even
imply `g_n < L_n²`, let alone `g_n < T_n`. (The witness is a growth rate, not a constructed
sequence; it is used only to exhibit that the two conditions are compatible, which is a statement
about rates.) Killing the constant does not change the *scale*, and Theorem B shows the scale is the
whole obstruction. ∎

*A second, weaker observation — epistemic, not part of the proof.* The `o(·)` form gives no usable
index: it supplies, for each `C > 0`, a threshold `N(C)` beyond which `g_n ≤ C√p_n L_n`, with no
control on `N(C)`, while clearance at `n` additionally forces `C < C_n ≍ L_n/√p_n → 0`. The required
constant shrinks with `n` while the index from which the bound becomes available is uncontrolled, so
the two are never *known* to hold together. That is a claim about present knowledge and is marked as
one; Corollary C.1 rests on the first argument alone.

> **Verdict on (1c): REFUTED.** The critical constant is `2/e ≈ 0.7358`; the published constants
> `22/25` and `21/25` are both above it; constants far below it clear the `L²` bar only on a bounded
> initial segment; and even `limsup = 0` (Cor. C.1) certifies nothing.

---

## 8. Theorem D — the material implication `RH ⟹ F`, and how strong a proof's output must be

Theorems A–C refute the *route*. They say nothing about the *proposition* `RH ⟹ F`.

**D.0 — Why (1d) is not decidable here.** `RH` and `F` are both **open** statements about the
standard model of arithmetic. To *refute* `RH ⟹ F` one must establish `RH ∧ ¬F`: prove the Riemann
Hypothesis *and* exhibit a counterexample to `F`. To *prove* it one must derive `F` from `RH`.
Neither is available, and no computation bears on either: `¬F` is `Σ₁` and finitely certifiable in
principle (card **L16**), but the certificate must certify the **rank** `n`, not merely the two
primes, and no search has reached beyond `2⁶⁴` (Fact 4). **(1d) is UNDECIDED and this leg does not
pretend otherwise.**

*(Both statements are also expressible in `Π₁` form. For `F` that is card **L16** — and the shape
such a refutation certificate must take is now machine-checked as `refuted_of_witness`, proven
without `sorry` in the frozen skeleton, `lean-probe-report.md`. For RH the `Π₁` arithmetization is a
real theorem with a real citation and **this run has neither card nor row. [GAP: unsourced.]**
Nothing above or below uses the classification — only that both statements are open.)*

> ### Theorem D
> Suppose `RH ⟹ F` were proved. Then, as an immediate corollary, one would have proved
> ```
> RH  ⟹  ( ∀k > 9 :  g_k  <  L_k² − L_k − 1 ) ,
> ```
> i.e. **an RH-conditional Cramér-type prime-gap bound at `log²`-scale**, uniform in `k`, with
> constant `1` on the leading term.

**Proof.** Compose the hypothesised implication with Fact 2 (card **L3**, Kourbatov Thm 1), an
unconditional theorem `F ⟹ (∀k>9: g_k < L_k² − L_k − 1)`. ∎

**Corollary D.1 (the size of the required advance).** The best published RH-conditional bound is
`g_n ≤ (22/25)√p_n L_n` (§4, for `p_n > 3`). The bound Theorem D would deliver is
`g_n < L_n² − L_n − 1`. Their ratio is

```
(22/25)√p_n·L_n / (L_n² − L_n − 1)   ≍   (22/25)·√p_n/L_n   →   ∞ ,
```

with value `8.72097·10⁷` at `p = 2⁶⁴` (`[R5]`) and unbounded thereafter. A proof of `RH ⟹ F` would
therefore *yield* an RH-conditional bound stronger than the published one by an **unbounded** factor
— not by a constant, not by an exponent shave. **This is a distance between two statements, not a
measure of proof effort:** nothing here says such a proof must first pass through a sharpened
`√p`-scale bound, and nothing here orders `RH ⟹ F` against any other open problem by difficulty
(card **L11**, correction #8).

**Corollary D.2 (the circularity charge, made quantitative).** Combine Facts 2 and 3:

```
 [ ∀k>9 : g_k < L² − L − 1.17 ]   ⟹   F   ⟹   [ ∀k>9 : g_k < L² − L − 1 ] .
```

Read the chain in the only direction it runs. If `H` is any hypothesis with `H ⟹ F`, composing with
the right-hand implication gives `H ⟹ [∀k>9 : g_k < L_k² − L_k − 1]`. **So every sufficient
hypothesis is at least as strong as the necessary condition** — it must deliver the full
`log²`-scale uniform bound, whether or not it is stated as one. And the left-hand implication shows
that a hypothesis only an additive `0.17` stronger than that bound *already* suffices. **The band in
which a candidate gap-bound hypothesis could sit is squeezed to the interval between `L²−L−1` and
`L²−L−1.17`** — where "the band" means precisely: the set of gap bounds *strong enough* to be forced
by sufficiency (everything at or below `L²−L−1`) and *weak enough* not to be sufficient already
(everything strictly above `L²−L−1.17`). Outside that interval a candidate is either too weak to
give `F` or is itself a sufficient condition, i.e. `F` with a constant changed.

*What this does **not** say:* that every sufficient `H` is *within* `0.17` of `F`. Plainly false —
`g_k < L² − L − 5` is sufficient and far stronger. The sandwich pins **`F`**, not the class of
hypotheses implying it.

*Flags, three of them:*
1. Corollary D.2 uses Fact 3, hence Axler's Corollary 3.5, **unopened in this run** (card **L4**
   hazard 4; `source-ledger.md` §6.3). The *inequality direction* is robust to the constant — any
   `b` with `1 < b < ∞` gives the same conclusion with `b − 1` in place of `0.17` — but the numeral
   `0.17` must not be quoted downstream until Axler is at L0. **This is also the substance of
   `faults.md` F3 against a sibling artifact; it is unrepaired in this run and is restated here as a
   live gap, not as a resolved one.**
2. Kourbatov's **Theorem 4** family (which would narrow `0.17` to `3.83/L`) is **deliberately not
   used.** Card **L2** hazard 4 records that the ledger locates `3.83/log p_k` inside Theorem 4 as a
   *sufficient condition assumed*, not as a proved two-sided bracket, and card **L4** hazard 3
   records that the family carries the hypothesis `p_k > 4·10¹⁸` — i.e. it presupposes the finite
   verification (Fact 4). Quoting it as a "narrowing" is the confusion those hazards exist to
   prevent.
3. The band is stated for hypotheses **of gap-bound shape**. A hypothesis of another shape (about
   zeros, admissible tuples, a sieve) is covered only once one asks what gap bound it yields, at
   which point the chain applies again.

**D.3 — What is *not* claimed.** Not "`F` is harder to prove than RH". No difficulty ordering on
open problems is available, and card **L11** records that all five panelists rejected that sentence.
Theorem D is a **strength** statement about what a proof would yield; Corollary D.1 a
**quantitative distance** between two published inequalities. Both are facts about statements, not
about proofs.

**D.4 — The converse.** Nothing in this run gives `F ⟹ RH`, and no source in the ledger asserts it.
`F` and RH are, as far as this leg can establish, incomparable. **[GAP: no ledger row; stated as an
absence of evidence, not as a theorem.]**

> **Verdict on (1d): UNDECIDED**, with the *strength of the theorem such a proof would yield*
> bounded below by Corollary D.1, and the "stronger hypothesis" escape closed by Corollary D.2. No
> difficulty ordering is claimed or implied.

---

## 9. Theorem E — Cramér's `limsup` hypothesis does not entail `F` over integer sequences

The last escape from §8: *"then assume Cramér's conjecture instead of RH."* Card **L9** records what
Cramér actually proved (`limsup = 1` **for his urn model**, `cramer1936order` L0 p. 27) and that he
only *suggested* it for the primes. Take the strongest common reading:

```
(Cr)      limsup_{n→∞}  g_n / L_n²  ≤  1 .
```

**Lemma E.1.** For every `δ > 0` there are infinitely many `n` with `g_n < (1+δ)·L_n`.

*Proof.* Suppose not: `g_n ≥ (1+δ)L_n` for all `n ≥ N_0`. Summing,
`p_N = p_{N_0} + Σ_{n=N_0}^{N−1} g_n ≥ (1+δ)Σ_{n=N_0}^{N−1} L_n`. By PNT, `p_n ~ n log n`, so
`L_n ~ log n` and `Σ_{n≤N} L_n ~ N log N`. Hence `p_N ≥ (1+δ+o(1))N log N`, contradicting
`p_N ~ N log N`. ∎ *(Uses only PNT.)*

> ### Theorem E (counter-model)
> Assume `(Cr)`. Then there is a strictly increasing sequence of positive integers `(q_n)_{n≥1}`
> with
> 1. `q_n = p_n + O((log n)²·log log n)`;
> 2. `limsup (q_{n+1} − q_n)/(log q_n)² = 1` — so `q` satisfies `(Cr)`;
> 3. `q_{n+1}^{1/(n+1)} ≥ q_n^{1/n}` for **infinitely many** `n` — so `q` violates the Firoozbakht
>    inequality infinitely often.
>
> Hence **`(Cr)` does not entail `F` in the theory of strictly increasing sequences of positive
> integers.**

**Proof.** *Construction.* By Lemma E.1 with `δ = 1`, for each `k ≥ 1` let
`n_k := least n ≥ 2^{2^k} with g_n ≤ 2L_n`, which exists, and `n_k → ∞` strictly. Define recursively

```
J_k  :=  ⌈ (log q_{n_k})² ⌉ − g_{n_k} ,          q_n  :=  p_n + Σ_{k : n_k < n} J_k .
```

(Well-founded: `q_{n_k}` depends only on `J_1,…,J_{k−1}`.)

*Claim 1 — `J_k ≥ 0`, and `q` strictly increasing.* `g_{n_k} ≤ 2L_{n_k}` while
`⌈(log q_{n_k})²⌉ ≥ L_{n_k}²`, and `L² > 2L` for `L > 2`, i.e. `p > e² ≈ 7.39`. So `J_k ≥ 0` for
every `k` with `p_{n_k} ≥ 11`. **Start at the least `k₀` with `p_{n_{k₀}} ≥ 11` and discard
`k < k₀`** — legitimate because the conclusion is about *infinitely many* indices. With that
restriction `q` is `p` plus a non-decreasing step function, hence strictly increasing. ✔
*(The restriction is load-bearing, not cosmetic: a negative `J_k` at small `k` would break
monotonicity. The round-1 skeptic re-derived this and confirmed it is correctly flagged,
`faults.md` §5 item 8.)*

*Claim 2 — the drift bound (1), with the F9 repair.* `q_n − p_n = Σ_{k : n_k < n} J_k` with
`J_k ≤ ⌈(log q_{n_k})²⌉`. Since `n_k ≥ 2^{2^k}`, the number of terms with `n_k < n` is at most
`log₂log₂ n + O(1)`, and each `J_k ≤ (log q_n)² + 1 = O((log n)²)`. Hence
`q_n − p_n = O((log n)²·log log n)`. ✔

*What the drift does to the counting function — the object `π(x)` estimates actually bound.* Write
`D(n) := q_n − p_n` and `Δ(x) := max{D(n) : p_n ≤ x}`; since `n ≍ x/log x`,
`Δ(x) = O((log x)²·log log x)`. Terms are spaced `≈ log x` apart near `x`, so displacing each by at
most `Δ(x)` moves the counting function by

```
|π_q(x) − π(x)|  ≤  Δ(x)/log x · (1+o(1))  =  O( log x · log log x ) .
```

Compare this with the **two** two-sided brackets card **T1** carries from `dusart2010estimates` (L0)
Thm 6.9 — **round 1 compared only against the wider one, and asserted a universal from that single
instance; that is fault F9, and the repair is to display both and to scope the conclusion to them:**

| bracket (card **T1**, `dusart2010estimates` L0 Thm 6.9) | validity | width in `π`-units | at `x = 10⁶` | at `x = 10¹²` | at `x = 2⁶⁴` |
|---|---|---|---:|---:|---:|
| eq. (6.5) `(x/L)(1+1/L) ≤ π(x) ≤ (x/L)(1+1.2762/L)` | `x ≥ 599` / `x > 1` | `0.2762·x/L²` | `1.45·10³` | `3.62·10⁸` | `2.59·10¹⁵` |
| **eq. (6.6)** `x/(L−1) ≤ π(x) ≤ x/(L−1.1)` | `x ≥ 5393` / `x ≥ 60 184` | `≈ 0.1·x/L²` | `6.14·10²` | `1.42·10⁸` | `9.83·10¹⁴` |
| *the counter-model's displacement* `log x·log log x` | — | — | `36.3` | `91.7` | `168.2` |
| **ratio (6.6) / displacement** | — | — | `16.9` | `1.54·10⁶` | `5.85·10¹²` |

`[R9]`. Subtracting the two halves of a bracket is a step taken **here**, not a statement Dusart
makes, and the intersection of the validity ranges is the binding one: `x ≥ 60 184` for eq. (6.6)
(card **T1** hazard 1 — a validity range is part of a bound), `x ≥ 599` for eq. (6.5). The tighter
of the two brackets is narrower by a factor `≈ 2.8`, and it still exceeds the displacement by an
unbounded factor. **Conclusion, scoped as F9 requires: neither of the two unconditional `π(x)`
brackets in card `T1` separates `q` from the primes.** *(Round 1 wrote "no unconditional `π(x)`
estimate in the run's toolbox", a universal drawn from one instance. The statement above is the one
this leg proves. A genuinely universal statement would have to quantify over estimates this run has
not enumerated, and it is not made.)*

*Conditionally the same conclusion is expected but this run cannot assert it:* the RH-strength error
term for `π(x)` is of order `√x·log x`, which would also dwarf `log x·log log x` — but **[GAP:
unsourced. No card, no ledger row; `notebook-1` §1 F3 flags the same bound as "not sourced here". Do
not propagate the words "conditional or not" without fetching a Schoenfeld-type statement first.]**
Nothing in Theorem E depends on the conditional case. In-round `[R10]` prints the term drift at the
sieve edge `p = 2 999 999`: **248**. Dividing by `log 2 999 999 = 14.914` gives a counting-function
displacement of `≈ 16.6` — *that division is done here by hand; the script does not compute it.*

*Claim 3 — the `limsup` (2).* At `n = n_k`: `q_{n_k+1} − q_{n_k} = g_{n_k} + J_k = ⌈(log q_{n_k})²⌉`
by construction, so the ratio is `⌈(log q_{n_k})²⌉/(log q_{n_k})² → 1`. At `n ∉ {n_k}`:
`q_{n+1} − q_n = g_n` and `log q_n ≥ log p_n`, so the ratio is `≤ g_n/L_n²`, whose limsup is `≤ 1` by
`(Cr)`. Hence `limsup = 1` exactly. ✔

*Claim 4 — the violations (3).* Write `T_n^{(q)} := q_n(q_n^{1/n} − 1)`. Fact 0's derivation is
purely formal and applies verbatim to any strictly increasing positive sequence, so the Firoozbakht
inequality fails at `n` iff `q_{n+1} − q_n ≥ T_n^{(q)}`. The index `n` is unchanged by the
construction, and `q_n = p_n(1 + ε_n)` with `ε_n = D(n)/p_n = O((log n)² log log n / p_n)`, which
tends to `0` faster than any negative power of `L_n`. Since `T_n = p_n(e^{L_n/n} − 1)` is smooth in
the value with `∂T_n/∂p_n = O(L_n²/p_n)`, the perturbation moves `T_n` by `O(ε_n L_n²) = o(1)`. Card
**L2** gives `T_n = L_n² − L_n − 1 + o(1)` for the primes, hence `T_n^{(q)} = L_n² − L_n − 1 + o(1)`
too, and in particular `T_n^{(q)} < (log q_n)²` for `n` large. At `n = n_k` the gap is
`⌈(log q_{n_k})²⌉ ≥ (log q_{n_k})² > T_{n_k}^{(q)}`. So `F` fails at every sufficiently large `n_k`
— infinitely many indices. ✔ ∎

*(In-round `[R10]`, 50 digits, `n_k` computed from the actual primes below `3·10⁶`, and reconstructed
**from the construction's statement** rather than from round 1's script:*

| `n_k` | `q_{n_k}` | `J_k` | gap | `T^{(q)}_{n_k}` | `(log q)²` | violates `F` ? |
|---:|---:|---:|---:|---:|---:|:---:|
| 2 | 3 | 0 | 2 | 2.19615242 | 1.20694896 | no — `n_k ≤ 10`, Fact 1's exception set |
| 5 | 11 | 4 | 6 | 6.76933693 | 5.74990174 | no — `n_k ≤ 10`, Fact 1's exception set |
| 16 | 57 | 11 | 17 | 16.3866451 | 16.3462636 | **yes** |
| 256 | 1634 | 53 | 55 | 47.9141256 | 54.7420383 | **yes** |
| 65536 | 821 709 | 180 | 186 | 170.778414 | 185.481018 | **yes** |

*matching round 1 and the skeptic's independent re-derivation row for row. The small-`n_k` rows are
not failures of the theorem: they lie in the exception set `{1,…,7,10}` of Fact 1, which is exactly
why Theorem E says "for all sufficiently large `k`".)*

**What Theorem E does and does not close.**

- It **does** close reading (1e) *as a counter-model result*: `(Cr)` does not entail `F` over
  strictly increasing integer sequences.
- **The stronger, informal reading — "no derivation using only growth and distribution can succeed"
  — is a gloss and is not proved.** The argument for it: a derivation appealing only to `(Cr)`, to
  PNT, and to the `π(x)` brackets of card **T1** cannot distinguish `p` from `q` (Claim 2), so it
  would have to prove `F` for `q` as well, which is false. That argument is only as good as its
  unformalized premise about which appeals a derivation makes. **[GAP: the derivation class is not
  formalized; and the class it names is contingent on what this run fetched. Downstream legs must
  quote the boxed counter-model statement, not the gloss.]**
- It **does not** prove `(Cr) ⇏ F` as a material implication about the primes. `p` is one fixed
  sequence; if `(Cr)` and `F` are both true, the implication is vacuously true. Theorem E quantifies
  over **sequences**.
- It **does** explain structurally why the `0.17` of Corollary D.2 is not a technicality: `(Cr)`
  controls a `limsup`; `F` needs a **uniform** bound at *every* index with the second-order term
  pinned. The distance between "asymptotically at most 1" and "below `L²−L−1` always" is the room
  the construction lives in.

> **Verdict on (1e): REFUTED.** Cramér's `limsup` hypothesis does not entail `F` over strictly
> increasing integer sequences — an explicit counter-model separates them. *Not claimed:* a proved
> bar on any class of derivations (that reading is a flagged gloss).

---

## 10. In-round computation — full record

Script: `attack-round-2/probe_rh2.py`. Output: `attack-round-2/probe_rh2.out`. Sieve of Eratosthenes
to `3·10⁶` (216 816 primes, largest `2 999 999`, 216 815 consecutive pairs), 1-indexed, all
arithmetic at **50 decimal digits** via `mpmath`.

**Written from the statements, not from round 1's code.** `faults.md` §6 item 2 identifies the
failure mode this guards against: *"A check written from the derivation cannot catch an error in the
derivation; it must be written from the statement."* Round 1's `probe_rh.py` was not consulted while
writing any formula here, and `[R3]` deliberately prints the **full** low table `n = 1..10` rather
than the range the theorem lives in — which is what makes the F4 rows visible at all.

| Check | Result | Used by |
|---|---|---|
| `[R1]` `min_x(√x − (25/22)log x) = 0.4068623816594768065…` at `x = 5.16528925619834710…` | **PASS** (`> 0`) | Lemma A.1 |
| `[R2]` `{n : T_n ≥ L_n²} = {1,2,3,4,5,6,7,10}` | **PASS** — exact match with card **L13** | Fact 1 |
| `[R3]` low table `n = 1..10`, `B_n` vs `T_n` | **PASS** — clears at `n = 1,2,3`; fails at `4,5,6,7,10` | Theorem A° |
| `[R4]` `A = {n ≥ 1 : B_n < T_n} = {1,2,3}`; `S = A ∩ [3,∞) = {3}`; `≤`-version identical | **PASS** | Theorems A°, A — **the F4 repair** |
| `[R5]` `min_{n≥4} B_n/T_n = 1.032957111858666789…` at `n = 4`, `p = 7` | — | §5.5 Remark 2 |
| `[R5]` `B/T = 110.15355255526119…` at `n = 216 816`, `p = 2 999 999` | — | §5.5 Remark 2 |
| `[R5]` `B/T = 8.7209716615406·10⁷` at `p = 2⁶⁴`, `T` replaced by the surrogate `L²−L−1` (card **L2**) | — | Cor. D.1 |
| `[R6]` `max_x log x/√x = 0.73575888234288464319… = 2/e` at `x = e²`; Lambert-`W` endpoints; prime counts `20 / 1018 / 157 340` | **PASS** | Theorem C |
| `[R7]` `p*(C)` for `C = 1, 22/25, 4/π, 1/(8π), 10⁻²` → `3, 5, 2, 62 869, 1 772 591` | **PASS** — reproduces `notebook-1` §1 F2 under the corrected endpoint | §5.4 |
| `[R8]` `2⁶⁴ − 1.836·10¹⁹ = 8.6744·10¹⁶ = 0.4702 %`; `≈ 1.955·10¹⁵` primes | — | §5.5 Remark 3 (**F8 repair**) |
| `[R9]` Dusart (6.5) vs (6.6) bracket widths vs `log x·log log x` at `10⁶, 10¹², 2⁶⁴` | — | §9 Claim 2 (**F9 repair**) |
| `[R10]` counter-model rows at `n_k ∈ {2,5,16,256,65536}`; drift `248` at the sieve edge | **PASS on the sample only** — the *infinitary* claim is Claim 4's analytic content, not a computational result (`2^{2⁵}` exceeds the sieve) | Theorem E |
| `[R11]` exact-integer violations of `p_{n+1}^n < p_n^{n+1}` over `n ≤ 10 000` plus the 40 largest-`ρ` indices | **0** (sanity only) | §11 |

Auxiliary evaluation (same session, 30 digits): the per-index critical constants
`C_1 = 2.0402789`, `C_2 = 1.1541371`, `C_3 = 0.98640306`, `C_4 = 0.85192308`, and
`(L²−L−1)/(√p·L) = 1.00906·10⁻⁸` at `p = 2⁶⁴`. Used in §5.4 and §7.

**Honest statement of what that buys.** `mpmath` at `dps = 50` is arbitrary-precision *floating
point*: no interval arithmetic, no directed rounding, no certified error bound. It is **not
proof-grade** and is not claimed to be. What justifies relying on it is **margin**: the tightest
comparison anywhere in the document is `B_4/T_4 = 1.0330` (`3.3 %`) and the tightest counter-model
row is `17` vs `16.3866` (`3.7 %`). Fifty digits against margins of `10⁻²` is ≈48 orders of headroom.
The F4 rows are far looser still (`0.863` vs `2.000`; `1.675` vs `2.196`), so the repair does not
depend on precision at all.

**Scale disclaimer, restated because it is easy to lose.** `3·10⁶` is ≈12.8 orders of magnitude below
the published frontier `2⁶⁴` (card **L6**). The computation here is a **check on this leg's own
algebra**, never evidence about `F`. Theorems A–E are proved analytically; `[R11]` in particular
establishes nothing about `F` and is reported only so that a silent bug in the `T_n` implementation
would have surfaced.

---

## 11. Declared gaps — what this document does NOT establish

1. **`F` is untouched.** Nothing here proves or refutes Firoozbakht's conjecture. Its status is what
   card **INDEX §6** says: verified below `2⁶⁴`, known to hold infinitely often, incompatible with
   the corrected Cramér–Granville heuristic. The frozen Lean development says the same thing
   mechanically: exactly one `sorryAx`, `Firoozbakht.firoozbakht`, at `Statement.lean:186`.
2. **`RH ⟹ F` (reading 1d) is undecided**, and §8 D.0 says why it is out of reach rather than merely
   unattempted.
3. **Axler is still unopened.** Corollary D.2's numeral `0.17` inherits card **L4** hazard 4. The
   *direction* of D.2 is robust to the constant; the numeral is not citable until
   `axler2014newbounds` reaches L0. **Citation-gate Priority 1, unchanged since round 1.** The
   bounded-source-refresh clause of this round's brief does not permit fetching it (the skeptic
   flagged it against a *sibling* artifact, F3, not against this one).
4. **Two sources remain proposed, not merged.** `carneiro2019fourier` (**L1**) and
   `visser2018andrica` (**L0**) were fetched and read by round 1, with MD5s and arXiv version pins;
   they are **not yet rows in `source-ledger.md`**, and this leg did not open the ledger. Until the
   citation gate acts, cite them as "read in run `germ-20260725-791a7c45` by leg `proof-attempt__1`".
   To raise CMS to L0, open the *Comment. Math. Helv.* copy and re-express the §1.1/§1.2 locators
   against journal pagination. The **`≤` vs `<` discrepancy** between CMS and Visser Theorem 1 is
   recorded (§4) and inert here, because the bound is used only as an upper envelope; it must be
   resolved before any paper states one form.
5. **`4/π` and `1/(8π)` are unsourced in this run.** They appear only inside the reproduction of
   `notebook-1`'s table (§5.4) and carry no weight anywhere else. **[GAP: no ledger row.]**
6. **Theorem E is a counter-model result over integer sequences, not a statement about the primes**
   (§9 closing bullets), and **its informal gloss about derivation classes is not proved**.
   Downstream legs must quote the box, not the gloss.
7. **No claim about the *optimality* of the `√p` scale under RH.** Whether RH-conditional methods are
   intrinsically confined to `x^{1/2}`-length intervals is unsourced. **[GAP: no ledger row.]**
   Theorems B and C are written so the verdict does not depend on it — they cover *every* `θ > 0` and
   *every* `C > 0`.
8. **`F ⇏ RH` and `RH ⇏ F` are absences of evidence, not theorems** (§8 D.4).
9. **RH's `Π₁` arithmetization is unsourced** — no card, no ledger row (§8 D.0). Nothing depends on
   it.
10. **The RH-strength `π(x)` error term (`≍ √x log x`) is unsourced** — no card, no ledger row. §9
    Claim 2 therefore states its conclusion for the **two named unconditional Dusart brackets** only
    (the F9 repair), and marks the conditional case as a gap. A Schoenfeld-type statement must be
    fetched before any leg writes "conditional or not".
11. **The `limsup = 0` result under RH + Montgomery pair correlation is tier L2_weak** — CMS report
    it without proving it, and this run opened none of the three works they cite. Corollary C.1 is
    written so its conclusion does not depend on the statement being true.
12. **The exception set `{1,…,7,10}` above `p = 3·10⁶`** is card **L13**'s claim, resting on
    `dusart2010estimates` (L0) plus L13's own asymptotics. This leg re-verified it only inside the
    sieve. Theorems A° and A use it for all `n`; if L13's asymptotic half were wrong, the completion
    step would need the direct comparison `B_n > T_n` instead — which Lemma A.1 plus
    `T_n = L² − L − 1 + o(1)` (card **L2**) supplies anyway, at the cost of an ineffective threshold.
    **The theorems survive either way; only their effectivity depends on L13.**
13. **The computation is not proof-grade** (§10). `mpmath` at 50 digits is arbitrary-precision
    floating point, not interval arithmetic. §12 states how the finite rows would be discharged
    rigorously in Lean.
14. **This leg repaired F4, F8, F9 only.** The round-1 BLOCKERs **F1** and **F2**, and the MAJORs
    **F3**, **F5**, **F6**, live in sibling artifacts (`proof-attempt-0.md`, `proof-attempt-2.md`,
    `notebook-0`, `notebook-2`, card `L15`) and are **not repaired here**. F6 is *read around* in
    §5.4 (the corrected endpoint is stated, not fixed in `notebook-1`). **The corpus-level BLOCKER
    set is therefore still non-empty after this leg**, and nothing in this document should be read as
    clearing it.
15. **A data point for whoever does repair F5 — offered, not acted on.** Nothing in this document
    uses the `55.92 %` fraction (§5.5 Remark 2 quotes it qualitatively for exactly that reason), but
    this leg's sieve makes an independent count free, so it is recorded. Over the same sieve to
    `3·10⁶` (216 816 primes, hence **216 815** consecutive pairs indexed `n = 1,…,216 815`), counting
    steps with `n ≥ 10`:
    ```
    #{ n ≥ 10 : T_{n+1} < T_n }  =  121 238        of   216 806 steps   ( 55.9200 % )
    ```
    The numerator agrees with card **D5**, card **L15** and `faults.md` §5; the **denominator does
    not**. `faults.md` F5 states that `216 805` "is the exact count of steps `n → n+1` with `n ≥ 10`
    in this sieve" and calls `proof-attempt-0`'s `216 806` an off-by-one. On this leg's count the
    arithmetic is `216 815 − 9 = 216 806`, and the `n ≥ 11` convention that would give `216 805`
    should also drop one descent (`T_11 = 11.3584 < T_10 = 11.6104`, so the step `10 → 11` is itself
    a descent and is the one that cut removes), yielding `121 237 / 216 805` (`55.9198 %`) — so
    `121 238 / 216 805` is not self-consistent under either cut. **This is evidence about F5, not a
    repair of it**, and F5 belongs to artifacts outside this leg's perimeter. It is flagged so the
    next skeptic re-counts rather than inherits.

---

## 12. Notes for the Lean leg (backend: `lean`)

The theorem statement is **FROZEN**: `lean/Firoozbakht/Statement.lean` was not touched by this leg,
and the round-1 probe's fidelity check (zero signature changes on the anchor) still applies.

- **Indexing.** Card **D1** / correction #1: Mathlib's `Nat.nth Nat.Prime` is **0-indexed**; every
  statement here is **1-indexed** (`p_n = Nat.nth Nat.Prime (n-1)`). Getting this wrong formalizes a
  different theorem.
- **Lemma A.1 is fully formalizable today** and needs no number theory:
  ```
  theorem sqrt_gt_const_mul_log (x : ℝ) (hx : 0 < x) :
      Real.sqrt x > (25/22) * Real.log x
  ```
  A single-variable calculus fact: one stationary point, one sign check. It is the only step in
  Theorems A°/A that is not a finite computation.
- **Theorem A° reduces to** Lemma A.1 + card **L13**'s exception set + an **eight**-row finite check
  (`n ∈ {1,…,7,10}`) — not six. The two extra rows are the F4 repair and they are the *loosest* rows
  in the table, so they cost nothing in precision.
- **The rows are *not* `F3`-decidable.** Each row decides `B_n ≤ T_n`, i.e.
  `(22/25)√p_n log p_n ≤ p_n(p_n^{1/n} − 1)` — a comparison between two irrational reals needing
  `Real.sqrt`, `Real.log`, `Real.rpow`. It is **not** the Firoozbakht inequality at `n`, and
  confusing the two is the D1-class trap: at `n = 4`, `F` is **true** (`11⁴ = 14641 < 16807 = 7⁵`)
  while the Theorem-A° row at `n = 4` is **"no"** (`B_4 = 4.5306 > T_4 = 4.3860`). Discharge the rows
  with `norm_num` on rational enclosures of `√p`, `log p`, `p^{1/n}`; the tightest margin is
  `n = 4` at `3.2957 %`.
- **Lemma A.0's irrationality step** (`p^{1/n}` irrational for prime `p`, `n ≥ 2`) is the one piece
  of Theorem A that is number theory rather than calculus, and Mathlib has the ingredients
  (`Nat.Prime.prime`, rational root / `irrational_nrt_of_notint_nrt`). Note the `n ≥ 2` side
  condition — `T_1 = 2` is an integer.
- **Theorem C** needs Lambert `W` only for the *endpoint formula*; the qualitative statement
  (`{x : C√x log x ≤ log²x} ≠ ∅ ⟺ C ≤ 2/e`) is again single-variable calculus.
- **Theorem E is not a formalization target.** It quantifies over sequences; formalizing the
  construction buys the kernel leg nothing.
- **Do not formalize the CMS bound.** It is an imported hypothesis
  (`RH → ∀ n ≥ 3, g_n ≤ (22/25)√p_n log p_n`) and must appear as an explicit hypothesis variable,
  **with its `n ≥ 3` binder**, never as an `axiom` — an `axiom` would (correctly) trip the probe's
  grep gate, and dropping the binder would formalize exactly the statement fault F4 is about.

---

## 13. Summary

**The subquestion `RH-conditional-bound` is REFUTED in every reading that is decidable. In the one
that is not — the material implication `RH ⟹ F` — what is bounded below is the *strength of the
theorem a proof would yield*, never the difficulty of finding one.**

The Riemann Hypothesis, routed through the sharpest published conditional prime-gap bound, certifies
Firoozbakht's inequality **at exactly one index in the range where that bound is available
(`n ≥ 3`), namely `n = 3` — the prime 5**. Below that range the envelope also sits under the
threshold at `n = 1` and `n = 2`, so the total arithmetic clearance is the three primes `{2,3,5}`
(Theorem A°) — which is exactly what `notebook-1` §1 F2 reports as `p*(22/25) = 5`, and the two
artifacts now say so in the same words. What excludes `n = 1, 2` from certification is the *source's
hypothesis*, not the arithmetic; saying "at no other index whatsoever" — round 1's headline —
misplaces the obstruction and is withdrawn.

The failure is not a matter of constants: the critical constant is `2/e`, published constants sit
above it, and constants below it clear the `L²` bar only on a bounded initial segment — even the
`limsup = 0` reported second-hand (tier L2_weak) under RH plus pair correlation would certify
nothing. It is not a matter of exponents either: every envelope `C·p^θ(log p)^A` with `θ > 0` fails
beyond finitely many indices, because the bar sits at `θ = 0`. Retreating to a stronger hypothesis
does not escape: composing with Kourbatov's necessary condition, **any** hypothesis sufficient for
`F` must itself deliver the full `log²`-scale uniform bound, while a hypothesis only `0.17` stronger
than that bound already suffices — the band left for a candidate *gap bound* is squeezed to width
`0.17` (a statement about the band of gap bounds, not about the class of sufficient hypotheses). And
Cramér's `limsup` hypothesis does not entail `F` over integer sequences at all: a sequence displaced
from the primes by `O(log²n·log log n)` — invisible to **both** unconditional `π(x)` brackets in card
`T1` — satisfies it and violates `F` infinitely often.

What survives is a precise obstruction, and it is the one to hand forward:

> Any conditional proof of `F` must produce a **uniform** gap bound at `log²`-scale with leading
> constant `1` and the second-order term `−L − 1` pinned, from a hypothesis that is not itself that
> bound. Nothing in the RH-conditional literature is within an unbounded factor of that; the band of
> gap bounds left for a candidate has width `0.17` (§8 D.2, *including its "what this does not
> say"*); and the two natural weaker hypotheses (`(Cr)`, and any power-type bound) are proved here
> to be insufficient. Carried alone, this block still means: a *route* is closed, not a problem
> ranked.

**Four boundaries this document draws around its own verdict, restated so they travel with it.**
It refutes *certification by a bound*, never the material implication `RH ⟹ F` — that stays
undecided (§8 D.0). It states a *distance between theorems*, never a difficulty ordering between
open problems (§8 D.3, card **L11**). Theorem E is a *counter-model over integer sequences*; its
reading as a bar on a class of derivations is a flagged gloss (§9). And **every certification claim
here carries the range of the theorem it chains — that is the repair round 2 exists for.**

`F` remains **OPEN**.

---

*Artifact of leg `proof-attempt` (RE-ATTACK round 2), molecule `task-20260726-b335`, parent loop
`reattack-20260726-57d1`. Companion files: `attack-round-2/probe_rh2.py`,
`attack-round-2/probe_rh2.out`. Round-1 lineage: `attack/proof-attempt-1.md` (superseded on the
points listed in §1), `attack/faults.md` (F4/F8/F9 addressed), `attack/notebook-1/findings.md`
(reconciled, §5.4), `attack/lean-probe-report.md` (frozen skeleton, cited in §3 and §12).*
