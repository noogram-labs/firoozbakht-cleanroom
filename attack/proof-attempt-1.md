# Proof attempt 1 — target #1, `RH-conditional-bound`

**Molecule:** `task-20260725-5fcc` (leg `proof-attempt__1`, crew role: proofsmith)
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-25 · **Formal backend:** Lean 4 / Mathlib
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1` — equivalently
`(p_n)^{1/n}` strictly decreasing. **Status of `F` in this document: OPEN.** Nothing below asserts
it, and nothing below refutes it.

---

## 0. Verdict

| Sub-claim of target #1 | Verdict | Where |
|---|---|---|
| **(1a)** The best explicit RH-conditional prime-gap bound implies `F` | **REFUTED** | Thm A §5 |
| **(1b)** *Some* bound of the form `g_n ≤ C·p_n^θ(log p_n)^A`, `θ>0`, implies `F` beyond finitely many `n` | **REFUTED** | Thm B §6 |
| **(1c)** *Some* envelope `C√p log p` (any `C>0`) implies `F` beyond finitely many `n` | **REFUTED** | Thm C §7 |
| **(1d)** `RH ⟹ F` as a material implication | **UNDECIDED** — and the work a proof would require is bounded below | Thm D §8 |
| **(1e)** Cramér's `limsup ≤ 1` hypothesis implies `F` by sequence-level reasoning | **REFUTED** (relative independence) | Thm E §9 |
| **`F` itself** | **OPEN.** Untouched by this leg. | — |

**Headline, in one sentence.** Under the Riemann Hypothesis the sharpest published prime-gap
bound, `g_n ≤ (22/25)√p_n · log p_n` (Carneiro–Milinovich–Soundararajan), certifies the
Firoozbakht inequality at **exactly one index, `n = 3` (`p = 5`)**, and at no other index
whatsoever — and no rescaling of the constant, and no improvement of the exponent short of
reaching `log²`-scale, can change that.

**What this does *not* say.** It does not say `F` is false. It does not say `F` is harder to prove
than RH — that is the overreach concept-card **L11** corrects, and it is not repeated here. It says
that the *route* named by target #1 is closed, and it says so with a proof rather than with a
scale-comparison slogan.

---

## 1. Perimeter and provenance (v5.1 clause)

**Inputs admitted:**

| Input | Provenance |
|---|---|
| `attack/concept-cards/` (30 cards) | leg `concept-cards`, molecule `task-20260725-068e`, this run |
| `attack/source-ledger.md` (20 rows) | leg `source-ledger`, molecule `task-20260725-d320`, this run |
| `attack/decompose.md` | leg `decompose`, molecule `task-20260725-c062`, this run |
| `attack/frame-deliberation/` | leg `frame-deliberation`, molecule `delib-20260725-07fc`, this run |
| **two sources fetched by this leg** (§4) | new; MD5s recorded |
| in-run computation by this leg | `attack/proof-attempt-1/probe_rh.py`, output `probe_rh.out` |

**Nothing else.** No file was consulted because it happened to sit in the working tree. Every
mathematical claim below is (i) an imported card with its ledger row and tier, (ii) a statement
read by this leg at a locator in a source it fetched, or (iii) derived here and marked as such.

**On the target's name.** The brief names target #1 by the slug `RH-conditional-bound` and does
not define it. §3 states the four inequivalent propositions that slug can denote, and each is
attacked separately. Conflating them is the principal hazard of this leg; §3 exists so that the
verdict cannot be misread.

---

## 2. Notation and imported facts

Throughout, `p_n` is the `n`-th prime, **1-indexed**, `p_1 = 2` (card **D1**). All logarithms are
natural.

```
L_n := log p_n                                                          (D2)
g_n := p_{n+1} − p_n                                                    (D2)
T_n := p_n · (p_n^{1/n} − 1)                                            (D5)
```

**Fact 0 (gap form of `F`).** `F ⟺ ∀n ≥ 1 : g_n < T_n`.
*Source:* card **L1** (PROVEN; `kourbatov2015bounds` L0, `visser2019verifying` L0).
*Derivation, for self-containment:* `F` in log form is `log p_{n+1} < (1+1/n)log p_n`, i.e.
`p_{n+1} < p_n·p_n^{1/n}`, i.e. `p_n + g_n < p_n + p_n(p_n^{1/n} − 1)`. Each step is an
equivalence because `t ↦ log t` and `t ↦ e^t` are strictly increasing on the relevant range. ∎

**Fact 1 (`T_n < L_n²` off an explicit exception set).**
`{n : T_n ≥ L_n²} = {1,2,3,4,5,6,7,10}`.
*Source:* card **L13** (PROVEN, in-run + `dusart2010estimates` L0 Thm 6.9). **Re-verified by this
leg** for all `n ≤ 216 815` — check `[C2]`, exact match, no float slack (60-digit arithmetic).
**Hazard imported with it:** L13's asymptotic half rests on Dusart's effective `π(x)` bounds; the
finite half is a computation. Below `p = 3·10⁶` this leg has confirmed it directly; above, it is
L13's claim, not a new one.

**Fact 2 (necessary condition).** `F ⟹ g_k < L_k² − L_k − 1` for all `k > 9`.
*Source:* card **L3** (PROVEN; `kourbatov2015bounds` L0 §2 Thm 1).

**Fact 3 (sufficient condition).** `[∀k>9 (p_k ≥ 29): g_k < L_k² − L_k − 1.17] ⟹ F`.
*Source:* card **L4** (PROVEN; `kourbatov2015bounds` L0 §4 Thm 3).
**Hazard imported with it:** L4 hazard 4 — the chain runs through Axler's Corollary 3.5, **not
opened in this run**, whose validity range was moved by a corrigendum from `x ≥ 5.43` to
`x ≥ 2 634 800 823`. Every use of Fact 3 below is flagged.

**Fact 4 (verified range).** `F` holds for all `p < 2⁶⁴ = 1.8447·10¹⁹`.
*Source:* card **L6** (PROVEN computationally; `kourbatov2015verification` L0, `visser2019verifying` L0).

**Facts 2+3 together (the sandwich).** `F` is trapped between two Cramér-scale gap bounds differing
by an additive `0.17`. This is the single most important structural fact for target #1 and card
**L4** already states it; §8 is where it does its work.

---

## 3. What target #1 actually asserts — four inequivalent readings

The slug `RH-conditional-bound` admits at least four readings. They are **not** equivalent, and
the literature's habit of writing "RH does not help" without saying which is meant is exactly what
this section removes.

> **(1a) Bound-sufficiency.** *The best explicit RH-conditional prime-gap bound implies `F`.*
> A statement about a specific published inequality. **Decidable by elementary calculus.**

> **(1b) Power-class sufficiency.** *Some bound of shape `g_n ≤ C p_n^θ (log p_n)^A` with `θ > 0`
> implies `F` for all but finitely many `n`.* A statement about a whole class of bounds — the class
> that all current unconditional and RH-conditional technology lives in. **Decidable.**

> **(1c) Constant-class sufficiency.** *Some envelope `C√p log p`, `C > 0` arbitrary, implies `F`
> for all but finitely many `n`.* This is (1b) restricted to the RH exponent, and asks whether a
> future sharpening of the *constant* could suffice. **Decidable, and the answer has a clean
> critical value.**

> **(1d) The material implication.** *`RH ⟹ F`.* A statement about two open arithmetic
> propositions. **Not decidable here**, and §8 says precisely why, plus what its proof would cost.

> **(1e) Hypothesis-class sufficiency.** *A hypothesis strong enough to imply `F` — e.g. Cramér's
> `limsup g_n/L_n² ≤ 1` — does so by reasoning available at the level of sequences.* This is the
> "name a hypothesis that is not a disguised restatement of the target" obligation that
> `decompose` §3.2 places on any S2 proposal. **Decidable, negatively.**

The rest of the document proves (1a), (1b), (1c), (1e) and bounds (1d).

---

## 4. New sources fetched by this leg

Card **L11** declares, in its own words: *"The RH-conditional bound `g_n ≪ √p_n log p_n` has no
ledger row … the sentence 'RH does not help' currently rests on an unverified recall."* Target #1
cannot be attacked with that hole open, so this leg closed it. Two sources, both read by this leg
at the locator.

**`carneiro2019fourier` — tier L0** *(proposed ledger addition)*

- **Citation:** Emanuel Carneiro, Micah B. Milinovich, Kannan Soundararajan, "Fourier optimization
  and prime gaps", *Commentarii Mathematici Helvetici* **94** (2019), no. 3, 533–568.
  arXiv:1708.04122 [math.NT].
- **Fetched:** `https://arxiv.org/pdf/1708.04122`, MD5 `2fdff58bc850508d8f124b4e7ad6b594`.
  Text layer present; extracted with `pdftotext -layout` and read.
- **Statements read, verbatim:**

  | Locator | Exact statement |
  |---|---|
  | **§1.2**, sentence preceding Theorem 5 | "…assuming the Riemann hypothesis, prove that `p_{n+1} − p_n ≤ (22/25)√p_n log p_n` for all primes `p_n > 3`." |
  | **§1.2, Theorem 5** | "Assume the Riemann hypothesis. Then, for `x ≥ 4`, there is always a prime number in the interval `[x, x + (22/25)√x log x]`." |
  | **§1.2, (1.10)** | Cramér's classical RH bound `limsup (p_{n+1}−p_n)/(√p_n log p_n) ≤ c`, `c` a universal constant; "the current best form of this bound is due to Dudek [19, Theorem 1.3], who obtained (1.10) with constant `c = 1`." |
  | **§1.2, Corollary 4, (1.14)** | Assume RH. Then `limsup (p_{n+1}−p_n)/(√p_n log p_n) ≤ 1/C⁺(B) < 21/25`. |
  | **§1.1, (1.8)** | `C(A) ≤ C⁺(A) ≤ min{…, 2}` — hence `1/C⁺(B) ≥ 1/2`, the floor of the method. |
  | **§1.2**, after Theorem 5 | "It has been verified by Oliveira e Silva, Herzog, and Pardi [37, §2.2] that `p_{n+1} − p_n < log²p_n` for all primes `11 ≤ p_n ≤ 4·10¹⁸`." |

**`visser2018andrica` — tier L0** *(proposed ledger addition; a **second** Visser paper, distinct
from the `visser2019verifying` row already in the ledger)*

- **Citation:** Matt Visser, "Variants on Andrica's conjecture with and without the Riemann
  hypothesis", arXiv:1804.02500 [math.NT].
- **Fetched:** `https://arxiv.org/pdf/1804.02500`, MD5 `38b405e83543fb6968754f90bac9c2d4`;
  `pdftotext -layout`, read.
- **Statements read, verbatim:**

  | Locator | Exact statement |
  |---|---|
  | **Theorem 1**, eq. (1.4) | "Assuming the Riemann hypothesis, `∀n ≥ 3, p_n ≥ 5, g_n := p_{n+1} − p_n < (22/25)√p_n ln p_n`." Attributed to Carneiro–Milinovich–Soundararajan, ref. [14]. |
  | **§2, Theorem 4**, eq. (2.1) | "(Cramer 1919). Assuming the Riemann hypothesis, `g_n := p_{n+1} − p_n = O(√p_n ln(p_n))`." + "this particular theorem only gives qualitative, not quantitative, information." |
  | **§2, Theorem 5**, eq. (2.2) | "(Goldston 1982). Assuming the Riemann hypothesis, `g_n ≤ 4√p_n ln(p_n)`; `n` sufficiently large." |
  | **§7** | The CMS inequality is verified **unconditionally** for all primes `< 1.836·10¹⁹`, by checking it at each known maximal-gap start (the RHS is monotone increasing). |
  | **§8** | "While the Riemann hypothesis provides … a nice explicit bound on prime gaps, it is still not quite sufficient to prove Andrica's conjecture." |

- **Discrepancy, recorded not smoothed:** CMS write `≤` with hypothesis `p_n > 3`; Visser writes
  `<` with hypothesis `n ≥ 3, p_n ≥ 5`. Same content; `p_n > 3 ⟺ p_n ≥ 5 ⟺ n ≥ 3`. Every argument
  below uses the bound only as a **non-strict upper envelope**, so the discrepancy is inert here.
  It must still be resolved before the paper quotes either form.

**Consequence for card L11.** Its declared gap is **closed**, and closed with something *stronger*
than what it asked for: not the ineffective `≪` recalled from memory, but a fully explicit,
effective, published inequality valid from `p = 5` on. That upgrade is what makes Theorem A below
a theorem rather than an asymptotic remark.

---

## 5. Theorem A — the explicit RH bound certifies `F` at exactly one index

**Definition.** For `n ≥ 3` put the **CMS envelope**

```
B_n  :=  (22/25) · √p_n · L_n .
```

By `carneiro2019fourier` §1.2, **RH implies `g_n ≤ B_n` for every `n ≥ 3`.**

Say the envelope **certifies `F` at `n`** when `B_n ≤ T_n`  — the non-strict form is the honest
one, since `B_n ≤ T_n` is what RH's `g_n ≤ B_n` can be chained with — i.e. when RH alone, through this
bound, forces `g_n < T_n` and hence the Firoozbakht inequality at that index. (Strictness: `g_n ≤
B_n ≤ T_n` gives `g_n ≤ T_n`; `g_n = T_n` is impossible because `T_n` is irrational for `n ≥ 2` —
`p_n^{1/n}` is irrational by unique factorisation — so `g_n < T_n` follows. Flagged as a one-line
step, justified here, not imported.)

> ### Theorem A
> Let `S := { n ≥ 3 : B_n ≤ T_n }` be the set of indices at which the CMS envelope certifies `F`.
> Then
> ```
> S = { 3 } .
> ```
> That is: **the sharpest published RH-conditional prime-gap bound certifies the Firoozbakht
> inequality at the single index `n = 3` (`p_3 = 5`), and fails to certify it at every other
> index.**

**Proof.** Two lemmas and a finite check.

**Lemma A.1.** For every real `x > 0`, `√x > (25/22)·log x`. Equivalently
`(22/25)√x · log x > (log x)²` for all `x > 1`.

*Proof.* Put `k := 25/22` and `h(x) := √x − k log x` on `(0,∞)`. Then
`h′(x) = 1/(2√x) − k/x = (√x − 2k)/(2x)`, so `h` has a unique stationary point at
`x* = (2k)² = (25/11)² = 625/121 = 5.16528925…`, which is a minimum (`h′ < 0` left of it, `h′ > 0`
right of it, and `h → +∞` at both ends of `(0,∞)`). At that point

```
h(x*) = 25/11 − (25/22)·log(625/121) = 2.27272727… − 1.13636363…·1.64196…
      = 0.40686238…  >  0.
```

Hence `h > 0` everywhere on `(0,∞)`. Multiplying `√x > k log x` by `log x > 0` (valid for `x > 1`)
and dividing by `k` gives `(22/25)√x log x > (log x)²`. ∎
*(In-run check `[C1]`: `x* = 5.1652892562`, `h(x*) = 0.406862381659 > 0`, 60-digit arithmetic. PASS.)*

**Lemma A.2.** For every `n ≥ 3`, `B_n > L_n²`.

*Proof.* Immediate from Lemma A.1 with `x = p_n ≥ 5 > 1`. ∎

**Completion.** Let `n ≥ 3`.

- If `n ∉ {3,4,5,6,7,10}` then by **Fact 1** `T_n < L_n²`, and by Lemma A.2 `B_n > L_n² > T_n`.
  So `n ∉ S`. This disposes of every index outside a set of six.
- The six remaining indices are checked directly (60-digit arithmetic, check `[C3-table]`); all
  six comparisons are strict, so `≤` and `<` agree on them:

| `n` | `p_n` | `T_n` | `B_n` | `B_n < T_n` ? |
|---:|---:|---:|---:|:---:|
| 3 | 5 | 3.549879733 | 3.166955068 | **yes** |
| 4 | 7 | 4.386035932 | 4.530587009 | no |
| 5 | 11 | 6.769336928 | 6.998568638 | no |
| 6 | 13 | 6.934281081 | 8.138289656 | no |
| 7 | 17 | 8.481637825 | 10.27984133 | no |
| 10 | 29 | 11.61044961 | 15.95742984 | no |

Hence `S = {3}`. ∎

**Remarks.**

1. **The single certified index is worthless.** `n = 3` means `p = 5`; `F` at `n = 3` is
   `7³ = 343 < 5⁴ = 625`, decidable by hand. Moreover Kourbatov's criteria (Facts 2, 3) carry the
   hypothesis `k > 9` precisely because the small indices are handled by inspection. So the CMS
   envelope's *entire* contribution to `F` lies inside the range every treatment already discards.
2. **The near miss at `n = 4` is not a near miss in disguise.** `[C4]`: the minimum of `B_n/T_n`
   over `4 ≤ n ≤ 216 815` is `1.032957112`, attained at `n = 4` (`p = 7`) — a 3.3 % shortfall. From
   there the ratio climbs monotonically in scale: `110.15` at `p = 2 999 957`, and at the verified
   frontier `p = 2⁶⁴` it is `8.72·10⁷` — **the envelope overshoots the threshold by roughly eight
   orders of magnitude exactly where a proof would have to work.**
3. **RH is not even load-bearing in the range where the envelope is smallest.** By
   `visser2018andrica` §7 the CMS inequality holds **unconditionally** for all `p < 1.836·10¹⁹`.
   So over essentially the whole verified range (**Fact 4**, `2⁶⁴ = 1.8447·10¹⁹`) the hypothesis RH
   adds nothing that is not already known, and what is already known still does not certify `F` at
   a single index above `n = 3`.

> **Verdict on (1a): REFUTED.** The best explicit RH-conditional prime-gap bound does not imply
> `F`. It implies `F` at one index below `p = 7` and nowhere else.

---

## 6. Theorem B — no power-type envelope can ever suffice

Theorem A is about one published constant. The obstruction is structural, and this is the
statement that says so.

> ### Theorem B
> Let `C > 0`, `θ > 0`, `A ∈ ℝ`. Define the envelope `E(x) := C·x^θ·(log x)^A`. Then
> ```
> #{ n : E(p_n) ≤ T_n }  <  ∞ ,
> ```
> and in fact `E(p_n)/T_n → ∞`. No such envelope certifies `F` at more than finitely many indices,
> for any values of `C, θ, A`.

**Proof.** By **Fact 1**, `T_n < L_n²` for all `n ∉ {1..7,10}`, so it suffices to show
`E(x)/(log x)² → ∞` as `x → ∞`. Write `u := log x`; then

```
E(x)/(log x)²  =  C·e^{θu}·u^{A−2}  →  ∞      (u → ∞),
```

because `e^{θu}` with `θ > 0` dominates any fixed power of `u`. Since `T_n < L_n²` eventually and
`p_n → ∞`, the ratio `E(p_n)/T_n > E(p_n)/L_n² → ∞`. A divergent ratio is `≤ 1` only finitely
often. ∎

**Why this is the whole game.** Every prime-gap upper bound currently available — unconditional or
conditional — lives in this class:

| Bound | Shape | `θ` | Certifies `F` beyond finitely many `n`? |
|---|---|---:|:---:|
| Baker–Harman–Pintz, unconditional (card **L11**, `baker2001difference` L1) | `g_n ≪ p_n^{0.525}` | 0.525 | **no** |
| Cramér 1919 under RH (`visser2018andrica` Thm 4, L0) | `g_n = O(√p_n log p_n)` | 0.5 | **no** |
| Goldston 1982 under RH (`visser2018andrica` Thm 5, L0) | `g_n ≤ 4√p_n log p_n` | 0.5 | **no** |
| Dudek under RH (`carneiro2019fourier` §1.2, L0) | `c = 1` in (1.10) | 0.5 | **no** |
| CMS under RH, explicit (`carneiro2019fourier` §1.2, L0) | `g_n ≤ (22/25)√p_n log p_n` | 0.5 | **no** (Thm A: one index) |
| CMS under RH, asymptotic (`carneiro2019fourier` Cor. 4, L0) | `limsup ≤ 1/C⁺(B) < 21/25` | 0.5 | **no** |
| What `F` needs (**Fact 2**, card **L3**) | `g_n < L_n² − L_n − 1` | **0** | — |

The column that matters is `θ`. Every entry above the rule has `θ > 0`; the requirement has
`θ = 0`. **Improving the exponent from 0.525 to 0.5 — which is exactly what RH buys — moves nothing
across the line drawn by Theorem B, because the line is at `θ = 0`, not at any positive value.**

> **Verdict on (1b): REFUTED.** No bound of power type, at any exponent `θ > 0`, any constant, and
> any logarithmic decoration, certifies `F` beyond finitely many indices.

---

## 7. Theorem C — the critical constant is `2/e`, and it does not help

A sceptic's natural next move: the CMS constant `22/25 = 0.88` is not known to be optimal; CMS's own
Corollary 4 already gives an asymptotic `< 21/25 = 0.84`, and the smallest value their expression
`1/C⁺(B)` could ever take is `1/2`, since `C⁺ ≤ 2` by eq. (1.8). Could a future constant be small enough? Theorem C settles this exactly.

> ### Theorem C
> For `C > 0` let `E_C(x) := C√x·log x`. Then
> ```
> { x > 1 : E_C(x) ≤ (log x)² }  ≠  ∅   ⟺   C ≤ 2/e = 0.735758882… ,
> ```
> and when non-empty this set is the **bounded** interval `[x⁻(C), x⁺(C)]` with
> ```
> x^∓(C) = exp( −2·W_0(−C/2) ),  exp( −2·W_{−1}(−C/2) )
> ```
> (`W_0`, `W_{−1}` the two real branches of the Lambert `W`). Consequently, for **every** `C > 0`,
> `E_C` certifies `F` at only finitely many indices.

**Proof.** `E_C(x) ≤ (log x)² ⟺ C ≤ log(x)/√x` for `x > 1`. The function `φ(x) := log(x)/√x` has
`φ′(x) = (2 − log x)/(2x^{3/2})`, so it increases on `(0, e²)`, decreases on `(e², ∞)`, and attains
its maximum `φ(e²) = 2/e² · e = 2/e` at `x = e² = 7.389056…`. Hence the sublevel set is non-empty
iff `C ≤ 2/e`, and since `φ(x) → 0` as `x → ∞` and as `x → 1⁺`, the set `{φ ≥ C}` is a compact
interval. Solving `C√x = log x` by the substitution `t = log x` gives `t·e^{−t/2} = C`, i.e.
`(−t/2)e^{−t/2} = −C/2`, i.e. `−t/2 = W(−C/2)`, whence the stated endpoints; two real branches
exist iff `−C/2 ≥ −1/e`, i.e. `C ≤ 2/e`, consistently. Finally the set is bounded, so it contains
finitely many primes; away from it `E_C(x) > (log x)² > T_n` by **Fact 1**. ∎

*(In-run check `[C6]`, 60-digit: `2/e = 0.735758882343` at `x = e² = 7.389056099`.)*

| `C` | Where `E_C(p) < L²` is possible | Comment |
|---|---|---|
| `22/25 = 0.88` (CMS explicit, L0) | **empty** | Theorem A's Lemma A.2 |
| `21/25 = 0.84` (CMS Cor. 4 asymptotic, L0) | **empty** | above critical |
| `2/e = 0.7358` (**critical**) | `{e²}` — a single point | — |
| `0.5` (floor of the CMS method, from (1.8) `C⁺ ≤ 2`) | `p ∈ (2.044, 74.19)` | 20 primes |
| `0.1` | `p ∈ (1.111, 8099)` | 1018 primes |
| `0.01` | `p ∈ (1.010, 2 122 265)` | 157 340 primes |

Read the last rows carefully: even a constant **fifty times smaller than anything the method can
produce** buys a bounded initial segment and then stops. Driving `C → 0` pushes `x⁺(C)` out only like `C⁻²` up to logarithmic factors (from
`x⁺ = (t/C)²` with `t = 2log(t/C)`), while the verified frontier is already at `2⁶⁴`. To certify
`F` merely up to the *already-verified* range one would need
`C ≤ (L²−L−1)/(√p·L) = 1.009·10⁻⁸` at `p = 2⁶⁴` — not a constant improvement but the abandonment
of the `√p` scale.

> **Verdict on (1c): REFUTED.** The critical constant is `2/e ≈ 0.7358`; the published constants
> `22/25` and `21/25` are both above it, and even constants far below it certify only a bounded
> initial segment.

---

## 8. Theorem D — the material implication `RH ⟹ F`, and what proving it would cost

Theorems A–C refute the *route*. They say nothing about the *proposition* `RH ⟹ F`. This section
states exactly what can and cannot be said about it, because conflating the two is the failure mode
this leg most needs to avoid.

**D.0 — Why (1d) is not decidable here, stated plainly.** `RH` and `F` are both open Π-statements
about the standard model of arithmetic. To *refute* `RH ⟹ F` one must establish `RH ∧ ¬F`: prove
the Riemann Hypothesis *and* exhibit a counterexample to `F`. To *prove* it one must derive `F`
from `RH`. Neither is available, and no computation bears on either: `¬F` is `Σ₁` and finitely
certifiable in principle (card **L16**), but the certificate must certify the *rank* `n`, not
merely the two primes, and no search has reached beyond `2⁶⁴` (**Fact 4**). **(1d) is UNDECIDED and
this leg does not pretend otherwise.**

What *can* be proved is a lower bound on the work any proof of (1d) would have to do.

> ### Theorem D
> Suppose `RH ⟹ F` were proved. Then, as an immediate corollary, one would have proved
> ```
> RH  ⟹  ( ∀k > 9 :  g_k  <  L_k² − L_k − 1 ) ,
> ```
> i.e. **an RH-conditional Cramér-type prime-gap bound at `log²`-scale**, uniform in `k` and with
> the constant `1` on the leading term.

**Proof.** Compose the hypothesised implication with **Fact 2** (card **L3**, Kourbatov Thm 1),
which is an unconditional theorem `F ⟹ (∀k>9: g_k < L_k² − L_k − 1)`. ∎

**Corollary D.1 (the size of the required advance).** The best published RH-conditional bound is
`g_n ≤ (22/25)√p_n L_n` (§4). The bound Theorem D would deliver is `g_n < L_n² − L_n − 1`. Their
ratio is

```
(22/25)√p_n·L_n  /  (L_n² − L_n − 1)   ≍   (22/25)·√p_n / L_n   →   ∞ ,
```

with value `8.72·10⁷` at `p = 2⁶⁴` (`[C4]`) and unbounded thereafter. So proving `RH ⟹ F` requires
improving RH-conditional prime-gap technology by an **unbounded** factor — not by a constant, not
by an exponent shave.

**Corollary D.2 (the circularity charge, made quantitative).** `decompose` §3.2 requires that any
S2 proposal "name the hypothesis and show it is not a disguised restatement of the target". Combine
**Fact 2** and **Fact 3**:

```
 [ ∀k>9 : g_k < L² − L − 1.17 ]   ⟹   F   ⟹   [ ∀k>9 : g_k < L² − L − 1 ] .
```

Any gap-bound hypothesis `H` that suffices for `F` must therefore imply the right-hand statement,
and any gap-bound hypothesis implied by `F` is implied by the left-hand one. **A sufficient
gap-bound hypothesis is within an additive `0.17` of being `F` itself** — and Kourbatov's Theorem 4
narrows that to `3.83/L`, which at `L ≈ 35` is `0.109` (card **L4**). Naming such an `H` and calling
it "a hypothesis stronger than RH" does not produce a conditional proof of `F`; it produces a
restatement of `F` with a different constant. **This is the precise, quantitative form of the
circularity objection, and it discharges `decompose` §3.2's obligation.**
*Flag:* Corollary D.2 uses **Fact 3**, hence Axler's Corollary 3.5, **unopened in this run** (card
**L4** hazard 4, `source-ledger.md` §6.3). The *inequality direction* used here is robust to the
constant — any constant `b` with `1 < b < ∞` gives the same conclusion, with `b − 1` in place of
`0.17` — but the numeral `0.17` must not be quoted downstream until Axler is at L0.

**D.3 — What is *not* claimed.** Not "`F` is harder to prove than RH". No difficulty ordering on
open problems is available, and card **L11** records that all five panelists rejected that
sentence. Theorem D is a **strength** statement about what a proof would yield, and Corollary D.1 a
**quantitative distance** between two published inequalities. Both are facts about statements, not
about proofs.

**D.4 — The converse direction, for completeness.** Nothing in this run gives `F ⟹ RH`, and no
source in the ledger asserts it. `F` and RH are, as far as this leg can establish, incomparable.
`¬RH` likewise bears on `F` in neither direction. **[GAP: no ledger row; stated as an absence of
evidence, not as a theorem.]**

> **Verdict on (1d): UNDECIDED**, with the work required bounded below by Corollary D.1 and the
> "stronger hypothesis" escape route closed by Corollary D.2.

---

## 9. Theorem E — Cramér's `limsup` hypothesis does not formally suffice

The last escape from §8 is: *"Then assume Cramér's conjecture instead of RH."* Card **L9** records
what Cramér actually proved (`limsup = 1` **for his urn model**, `cramer1936order` L0 p. 27) and
that he only *suggested* it for the primes. Take the strongest common reading of the primes
statement:

```
(Cr)      limsup_{n→∞}  g_n / L_n²  ≤  1 .
```

Does `(Cr) ⟹ F`? Theorem E says: not by any argument that sees only the sequence's distribution.

**Lemma E.1.** For every `δ > 0` there are infinitely many `n` with `g_n < (1+δ)·L_n`.

*Proof.* Suppose not: `g_n ≥ (1+δ)L_n` for all `n ≥ N_0`. Summing,
`p_N = p_{N_0} + Σ_{n=N_0}^{N−1} g_n ≥ (1+δ)·Σ_{n=N_0}^{N−1} L_n`. By the prime number theorem
`p_n ~ n log n`, so `L_n ~ log n` and `Σ_{n≤N} L_n ~ N log N`. Hence `p_N ≥ (1+δ+o(1))·N log N`,
contradicting `p_N ~ N log N` for `N` large. ∎
*(Uses only PNT; the `p_n ~ n log n` form is standard and is the same input card **T1** makes
effective. No new source needed.)*

> ### Theorem E (relative independence)
> Assume `(Cr)`. Then there exists a strictly increasing sequence of positive integers `(q_n)_{n≥1}`
> such that
> 1. `q_n = p_n + O((log n)² · log log n)` — so `q` and the primes agree far inside the error term
>    of every effective `π(x)` estimate in the run's toolbox (card **T1**);
> 2. `limsup_{n→∞} (q_{n+1} − q_n)/(log q_n)² = 1` — so `q` satisfies `(Cr)` in the same form the
>    primes do;
> 3. `q_{n+1}^{1/(n+1)} ≥ q_n^{1/n}` for **infinitely many** `n` — so `q` violates the Firoozbakht
>    inequality infinitely often.
>
> Hence **no derivation of `F` from `(Cr)` can succeed if it uses only the sequence's growth and
> distribution** (PNT, effective `π(x)` bounds, gap statistics, monotonicity). Any successful
> derivation must invoke primality in a way that distinguishes `p` from `q`.

**Proof.** *Construction.* By Lemma E.1 with `δ = 1`, for each `k ≥ 1` let

```
n_k  :=  least  n ≥ 2^{2^k}  with  g_n ≤ 2·L_n ,
```

which exists, and `n_k → ∞` strictly. Define recursively

```
J_k  :=  ⌈ (log q_{n_k})² ⌉ − g_{n_k} ,          q_n  :=  p_n + Σ_{k : n_k < n} J_k .
```

(The recursion is well-founded: `q_{n_k}` depends only on `J_1,…,J_{k−1}`.)

*Claim 1 — `J_k ≥ 0` for large `k`, and `q` is strictly increasing.* `g_{n_k} ≤ 2L_{n_k}` while
`⌈(log q_{n_k})²⌉ ≥ L_{n_k}²`, and `L² > 2L` for `L > 2`, i.e. `p > e² ≈ 7.39`. So `J_k ≥ 0` for
every `k` with `p_{n_k} ≥ 11`. `q` is `p` plus a non-decreasing step function, hence strictly
increasing. ✔

*Claim 2 — the drift bound (1).* `q_n − p_n = Σ_{k : n_k < n} J_k`, with `J_k ≤ ⌈(log q_{n_k})²⌉`.
Since `n_k ≥ 2^{2^k}`, the number of terms with `n_k < n` is at most `log_2 log_2 n + O(1)`, and
each `J_k ≤ (log q_{n_k})² + 1 ≤ (log q_n)² + 1 = O((log n)²)`. Hence
`q_n − p_n = O((log n)² log log n)`. ✔
*(Scale of this drift, in-run `[C7]`: at the sieve edge `p = 2 999 957` the accumulated drift is
`248`, a relative perturbation of `8.3·10⁻⁵`. Every effective `π(x)` bound in card **T1** has error
terms larger than this by many orders of magnitude — Dusart's Theorem 6.9 controls `π(x)` only to
`O(x/log²x)`. The two sequences are indistinguishable by that toolbox.)*

*Claim 3 — the `limsup` (2).* At `n = n_k`: `q_{n_k+1} − q_{n_k} = g_{n_k} + J_k = ⌈(log q_{n_k})²⌉`
by construction, so the ratio is `⌈(log q_{n_k})²⌉/(log q_{n_k})² → 1`. At `n ∉ {n_k}`:
`q_{n+1} − q_n = g_n` and `log q_n ≥ log p_n`, so the ratio is `≤ g_n/L_n²`, whose limsup is `≤ 1`
by `(Cr)`. Hence `limsup = 1` exactly. ✔

*Claim 4 — the violations (3).* Write `T_n^{(q)} := q_n(q_n^{1/n} − 1)`; Fact 0's derivation is
purely formal and applies verbatim to any strictly increasing positive sequence, so the Firoozbakht
inequality fails at `n` iff `q_{n+1} − q_n ≥ T_n^{(q)}`. By Claim 2, `q_n = p_n(1 + o(1))` with an
error far below every term in the expansion of card **L2**, so `T_n^{(q)} = L_n² − L_n − 1 + o(1)`,
in particular `T_n^{(q)} < (log q_n)²` for `n` large. At `n = n_k` the gap is `⌈(log q_{n_k})²⌉ ≥
(log q_{n_k})² > T_{n_k}^{(q)}`. So `F` fails at every sufficiently large `n_k` — infinitely many
indices. ✔ ∎

*(In-run check `[C7]`, 60-digit, `n_k` computed from the actual primes below `3·10⁶`:*

| `n_k` | `q_{n_k}` | `J_k` | gap | `T^{(q)}_{n_k}` | `(log q)²` | violates `F` ? |
|---:|---:|---:|---:|---:|---:|:---:|
| 5 | 11 | 4 | 6 | 6.7693369 | 5.7499017 | no — `n_k ≤ 10`, the **L13** exception set |
| 16 | 57 | 11 | 17 | 16.386645 | 16.346264 | **yes** |
| 256 | 1634 | 53 | 55 | 47.914126 | 54.742038 | **yes** |
| 65536 | 821 709 | 180 | 186 | 170.77841 | 185.48102 | **yes** |

*and the ratios `(q_{n+1}−q_n)/(log q_n)²` at those indices are `1.0435, 1.03999, 1.00471, 1.0028`
— converging to 1 as Claim 3 asserts. The `n_k = 5` row is not a failure of the theorem: it lies in
the exception set `{1..7,10}` of **Fact 1**, which is exactly why Theorem E says "for all
sufficiently large `k`".)*

**What Theorem E does and does not close.**

- It **does** close the reading (1e): `(Cr)` is not a hypothesis from which `F` follows by
  distributional reasoning. A leg proposing "assume Cramér, derive Firoozbakht" is proposing
  something that provably cannot work at that level of information.
- It **does not** prove `(Cr) ⇏ F` as a material implication about the primes. `p` is one fixed
  sequence; if both `(Cr)` and `F` happen to be true, the implication is vacuously true. Theorem E
  is a statement about **derivability from a class of premises**, and it is stated that way on
  purpose.
- It **does** explain, structurally, why the `0.17` of Corollary D.2 is not a technicality:
  `(Cr)` controls a `limsup`, `F` needs a **uniform** bound at *every* index with the second-order
  term pinned. The distance between "asymptotically at most 1" and "below `L²−L−1` always" is
  precisely the room Theorem E's construction lives in.

> **Verdict on (1e): REFUTED.** Cramér's `limsup` hypothesis does not formally suffice; the gap
> between it and `F` is exactly the uniformity plus second-order term that Facts 2/3 sandwich.

---

## 10. In-run computation — full record

Script: `attack/proof-attempt-1/probe_rh.py`. Output: `attack/proof-attempt-1/probe_rh.out`.
Sieve of Eratosthenes to `3·10⁶` (216 816 primes, largest `2 999 999`, 216 815 consecutive pairs),
1-indexed, all arithmetic at **60 decimal digits** via `mpmath` so that no claim rests on binary
float rounding.

| Check | Result | Used by |
|---|---|---|
| `[C1]` `min_x (√x − (25/22)log x) = 0.406862381659 > 0` at `x = 5.1652892562` | **PASS** | Lemma A.1 |
| `[C2]` `{n : T_n ≥ L_n²} = {1,2,3,4,5,6,7,10}` | **PASS** (exact match with card **L13**) | Fact 1 |
| `[C3]` `S = {n ≥ 3 : B_n ≤ T_n} = {3}` | **PASS** | Theorem A |
| `[C4]` `min_{n≥4} B_n/T_n = 1.032957112` at `n = 4`, `p = 7` | — | Remark A.2 |
| `[C4]` `B/T = 110.1538156` at `n = 216 815`, `p = 2 999 957` | — | Remark A.2 |
| `[C4]` `B/T = 8.7209717·10⁷` at `p = 2⁶⁴` (`≈ 10^{7.94}`) | — | Cor. D.1 |
| `[C5]` violations of `F` in the sieved range | **0** (sanity only) | §11 |
| `[C6]` `max_x log(x)/√x = 2/e = 0.735758882343` at `x = e²` | **PASS** | Theorem C |
| `[C7]` counter-model violates `F` at every `n_k ≥ 11`; drift `248` at the sieve edge | **PASS** | Theorem E |

**Scale disclaimer, restated because it is easy to lose.** `3·10⁶` is ≈12.8 orders of magnitude
below the published frontier `2⁶⁴` (card **L6**). The computation here is a **check on this leg's
own algebra**, never evidence about `F`. Theorems A–E are proved analytically; the computation
confirms the finite tables and the exception set, nothing more. `[C5]` in particular establishes
nothing about `F` and is reported only so that a silent bug in the `T_n` implementation would have
surfaced.

---

## 11. Declared gaps — what this document does NOT establish

Stated so no downstream leg mistakes silence for coverage.

1. **`F` is untouched.** Nothing here proves or refutes Firoozbakht's conjecture. Its status
   remains exactly what card **INDEX §6** says: verified below `2⁶⁴`, known to hold infinitely
   often, incompatible with the corrected Cramér–Granville heuristic.
2. **`RH ⟹ F` (reading 1d) is undecided**, and §8 D.0 says why it is out of reach rather than
   merely unattempted.
3. **Axler is still unopened.** Corollary D.2's numeral `0.17` inherits card **L4**'s hazard 4.
   The *direction* of D.2 is robust to the constant; the numeral is not citable until
   `axler2014newbounds` reaches L0. **Citation-gate Priority 1, unchanged.**
4. **Two new sources are proposed, not merged.** `carneiro2019fourier` and `visser2018andrica` were
   fetched and read by this leg at tier **L0** (§4), with MD5s. They are **not yet rows in
   `source-ledger.md`**. The citation gate must merge them or reject them; until then, cite them as
   "read in run `germ-20260725-791a7c45` by leg `proof-attempt__1`".
5. **The `≤` vs `<` discrepancy** between CMS §1.2 (`≤`, `p_n > 3`) and Visser Theorem 1 (`<`,
   `n ≥ 3, p_n ≥ 5`) is recorded (§4) and inert for every argument here, because the bound is used
   only as an upper envelope. It must be resolved before the paper states either form.
6. **Theorem E is about a class of derivations, not about the primes.** §9's closing bullets state
   the limit explicitly. A reader who takes Theorem E as "Cramér does not imply Firoozbakht" has
   over-read it.
7. **No claim about the *optimality* of the `√p` scale under RH.** Whether RH-conditional methods
   are intrinsically confined to `x^{1/2}`-length intervals is a methodological claim this run has
   not sourced. **[GAP: no ledger row.]** Theorems B and C are written so that the verdict does not
   depend on it — they cover *every* `θ > 0` and *every* `C > 0`, so even a hypothetical future
   method reaching below `√p` at power scale is already refuted.
8. **`F ⇏ RH` and `RH ⇏ F` are absences of evidence, not theorems** (§8 D.4).
9. **The exception set `{1..7,10}` above `p = 3·10⁶`** is card **L13**'s claim, resting on
   `dusart2010estimates` (L0) plus L13's own asymptotics. This leg re-verified it only inside the
   sieve. Theorem A's completion step uses it for all `n`; if L13's asymptotic half were wrong,
   Theorem A would need the direct comparison `B_n > T_n` instead — which Lemma A.1 plus
   `T_n = L² − L − 1 + o(1)` (card **L2**) supplies anyway, at the cost of an ineffective
   threshold. **The theorem survives either way; only its effectivity depends on L13.**

---

## 12. Notes for the Lean leg (backend: `lean`)

Target #1's results are *far* more formalizable than `F` itself, and the `lean-skeleton` leg may
want them as warm-up theorems that are actually provable.

- **Indexing.** Card **D1** / correction #1: Mathlib's `Nat.nth Nat.Prime` is **0-indexed**; every
  statement here is **1-indexed**. `p_n` here `= Nat.nth Nat.Prime (n-1)`. Getting this wrong
  formalizes a different theorem — the highest-severity correction in the run.
- **Lemma A.1 is fully formalizable today** and needs no number theory whatsoever:
  ```
  theorem sqrt_gt_const_mul_log (x : ℝ) (hx : 0 < x) :
      Real.sqrt x > (25/22) * Real.log x
  ```
  A single-variable calculus fact: one stationary point, one sign check. This is the *only* step in
  Theorem A that is not a finite computation, and it is the right first target for the kernel leg —
  it is a genuine theorem, unlike the smooth model that card **L14** flags as over-billed.
- **Theorem A then reduces to** Lemma A.1 + card **L13**'s exception set + a six-row decidable
  table. The six rows are `Decidable` in the `F3` purely-arithmetic form (card **D4**), needing no
  `Real.rpow` at all: e.g. `n = 4` is `11^4 < 7^5`.
- **Theorem C** needs the Lambert `W` only for the *endpoint formula*; the qualitative statement
  (`{x : C√x log x ≤ log²x} ≠ ∅ ⟺ C ≤ 2/e`) is again single-variable calculus.
- **Theorem E is not a formalization target.** It quantifies over sequences and its content is
  meta-mathematical (what a class of derivations cannot do). Formalizing the *construction* is
  possible but buys nothing the kernel leg needs.
- **Do not formalize the CMS bound.** It is an imported hypothesis (`RH → g_n ≤ (22/25)√p_n log p_n`),
  and in Lean it should appear as an explicit hypothesis variable, never as an axiom. An `axiom`
  here would make the `lean-probe` leg's grep-for-`axiom` gate fire, correctly.

---

## 13. Summary

**Target #1 `RH-conditional-bound` is REFUTED in every reading that is decidable, and bounded below
in the one that is not.**

The Riemann Hypothesis, routed through the sharpest published conditional prime-gap bound,
certifies Firoozbakht's inequality at the single index `n = 3` — the prime 5 — and at no other. The
failure is not a matter of constants: the critical constant is `2/e`, published constants sit above
it, and constants below it buy only a bounded initial segment. It is not a matter of exponents
either: every envelope `C·p^θ(log p)^A` with `θ > 0` fails beyond finitely many indices, because
what `F` requires is `θ = 0`. Retreating to a stronger hypothesis does not escape: Kourbatov's
sandwich puts any sufficient gap-bound hypothesis within an additive `0.17` of `F` itself, and
Cramér's `limsup` hypothesis — the natural candidate — provably cannot yield `F` by distributional
reasoning, because a sequence indistinguishable from the primes by every effective `π(x)` bound in
the toolbox satisfies it and violates `F` infinitely often.

What survives is a precise obstruction, and it is the one to hand to the `re-attack` leg:

> Any conditional proof of `F` must produce a **uniform** gap bound at `log²`-scale with leading
> constant `1` and the second-order term `−L − 1` pinned, from a hypothesis that is not itself that
> bound. Nothing in the RH-conditional literature is within an unbounded factor of that, and the
> two natural weaker hypotheses (`(Cr)`, and any power-type bound) are proved here to be
> insufficient.

`F` remains **OPEN**.

---

*Artifact of leg `proof-attempt__1`, molecule `task-20260725-5fcc`, run `germ-20260725-791a7c45`.
Companion files: `attack/proof-attempt-1/probe_rh.py`, `attack/proof-attempt-1/probe_rh.out`.*
