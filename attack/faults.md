# faults.md — red-team of the Firoozbakht attack corpus

**Molecule:** `task-20260725-488f` (leg `skeptic`, crew role: skeptic)
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-25
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.
**Status of `F` in this document: OPEN.** Nothing below proves or refutes it. This document
attacks the *artifacts*, not the conjecture.

---

## 0. Perimeter — what was read and what was independently recomputed

**Artifacts audited (all of them):**

| Artifact | Lines |
|---|---|
| `attack/proof-attempt-0.md` (`first-failure-maximality`) | 603 |
| `attack/proof-attempt-1.md` (`RH-conditional-bound`) | 893 |
| `attack/proof-attempt-2.md` (`unconditional-verified-range`) | 461 |
| `attack/notebook-0/findings-0.md` | 172 |
| `attack/notebook-1/findings.md` | 207 |
| `attack/notebook-2/findings.md` | 375 |
| `attack/concept-cards/` (INDEX + L15, T1 read at the locator; others skimmed) | — |
| `attack/lean-probe-report.md`, `lean/` sources | 279 + tree |
| `attack/notebook-0/ffm_lab.py`, `attack/notebook-2/fb_core.py` | source-read |

**Independent recomputation performed by this leg.** Nothing below is a reading of an
upstream number. A fresh sieve (to `3·10⁶`, `10⁷`, `10⁸`) and independent `mpmath`/`numpy`
implementations were written from the *statements* in the artifacts, not from their code, and
every numeric verdict below is this leg's own. Scripts: `attack/skeptic-checks/`.

**Method.** For each artifact: (i) re-derive every displayed algebraic step by hand; (ii)
re-evaluate every quoted constant; (iii) cross-compare quantities that appear in more than one
artifact under the same name. Category (iii) is where the two BLOCKERs live — neither is
visible from inside a single artifact, which is why no leg caught them.

---

## 1. Verdict

**The BLOCKER set is non-empty. Two findings block the seal.**

| Severity | Count | Findings |
|---|---|---|
| **BLOCKER** | **2** | F1, F2 |
| **MAJOR** | **4** | F3, F4, F5, F6 |
| **MINOR** | **8** | F7 – F14 |

Both BLOCKERs are **repairable** and neither is a mathematical error about `F`. F1 is a
collision of vocabulary that has produced two contradictory headline sentences in the same run;
F2 is a derivation that does not go through as written, whose *conclusion* this leg
independently confirms to be true. Neither is softened below, and neither may be waved through
by pointing at the repair: the artifacts as they stand are what a downstream `write-paper` /
`synthesize` leg will read.

The corpus is, otherwise, unusually disciplined. §5 records what was checked and came back
clean, because a red-team report that lists only hits is not calibrated.

---

## 2. BLOCKERS

### F1 — **BLOCKER** — `P6′` is measured under three inequivalent definitions, and two sibling legs publish opposite trends for the same named quantity

**Where.** `notebook-0/findings-0.md` §2 finding 3 vs `notebook-2/findings.md` §3; card
`L15`; `proof-attempt-0.md` §1 (M1/M2/M3).

**The fault.** The symbol `m(n)` and the phrase "governing record index" carry **three
inequivalent meanings** across the run, and the quantity `min(T_n − T_{m(n)})` is reported
under all of them without any leg naming which one it used:

| Definition | Where | Source |
|---|---|---|
| **(A)** `m(n)` = the most recent maximal-gap index `≤ n` | card `L15`; `notebook-2` | `fb_core.py:181-197` (`cur_Tm` = `T` at the last record) |
| **(B)** `m(n) := min{ m : g_m ≥ g_n }` | `notebook-0` | `ffm_lab.py:14` |
| **(C)** `T_m ≤ T_n` for **all** `m < n` straddling a record gap | card `L15`'s own prose statement of P6′ | — |

(C) ⟹ (A) ⟹ (B) as obligations, and the implications are strict. **(B) is the weakest, and
(B) is the one the search-pruning actually consumes** — `m(n)` under (B) is a record index with
`g_{m(n)} ≥ g_n`, so `g_n ≤ g_{m(n)} < T_{m(n)} ≤ T_n` closes the chain. `notebook-0` says this
explicitly ("it *implies* FFM and is what the standard argument consumes"); `notebook-2` does not
say which it used.

**Recomputed independently by this leg** (fresh sieve, both definitions, same code path):

| range | (A) `min(T_n − T_{m(n)})` | (B) `min(T_n − T_{m(n)})` |
|---|---|---|
| `3·10⁶` | `+1.04642·10⁻²` at `p = 2 011 211` | `+0.484528` at `n = 1879`, `p = 16 141` |
| `10⁷` | `+6.06048·10⁻³` at `p = 4 652 581` | `+0.484528` (unchanged) |
| `10⁸` | `+1.11181·10⁻³` at `p = 47 326 957` | `+0.484528` (unchanged) |

Both notebooks are **numerically correct**. Column (A) reproduces `notebook-2` §3 to every digit
it quotes (`1.046·10⁻²`, `6.060·10⁻³`, `1.112·10⁻³`). Column (B) reproduces `notebook-0`
finding 3's global minimum `0.485 at n = 1879`. Zero exceptions under both, at every scale.

**Why this blocks.** The run now carries two headline sentences that a reader cannot reconcile:

> `notebook-2` §3, billed as "**the one unexpected result**" and escalated as a *cosmon-ward
> observation*: "**The empirical case for P6′ does not strengthen with range — it weakens.**"

> `notebook-0` §2 finding 3: "**The margin does not decay.** … The global minimum is at
> `n = 1879` and is never approached again."

They are both true, of different predicates, and **neither notebook cites the other**.
`notebook-2` reconciles its result against card `L15`'s *dip* statistic and concludes the card is
wrong; it never considers that a sibling leg measured a different `m(n)`. A `synthesize` or
`write-paper` leg reading both has no way to tell that `min(T_n − T_{m(n)})` denotes two things.

**Two consequences that are themselves defects, not just risks:**

1. **`notebook-2` §3 consequence 2 — the float64-noise-floor alarm — is scoped to the wrong
   predicate.** "A float64 check of P6′ hits the noise floor at the published frontier" is derived
   from the (A)-margin's `p^{−0.83}` decay. Under (B) — the version a pruned search consumes —
   the margin is flat at `0.485` across every decade measured here and is `~10¹²` ulps clear of
   zero. The warning is real for (A) and **does not apply** to the obligation the search route
   needs. As written it reads as a general indictment of computational checks of P6′.
2. **`notebook-2` §3 consequence 3 — "the route to discharging P6′ must therefore be the analytic
   one" — is an inference from the mis-scoped premise** and does not survive it.

**Repair (not applied by this leg).** Name the three predicates (P6′-pair, P6′-gov, P6′-min),
state which one each measurement used, and state that the pruning consumes P6′-min. Then
`notebook-0` and `notebook-2` cease to conflict and both results stand. `L15` must be amended:
its prose states (C) while its measurement row ("`T_{m(n)} ≤ T_n` for `m(n)` = governing record
index") states (A).

---

### F2 — **BLOCKER** — `proof-attempt-0.md` Theorem C(b): the cited bound **(A-high)** is too weak by a factor `≈ ℓ²` to support the theorem, and the quoted constant is below the document's own criterion

**Where.** `proof-attempt-0.md` §6.1 (A-high), §6.2 Theorem C(b) and its proof, §9 item 15,
and every downstream quotation of `0.004479` / `0.99553` (§2 verdict table, §6 "Reading of
Theorem C", §7, §10 gap 1, §11 correction 3, §13 defensible sentence).

**The fault, in three parts.**

**(a) The stated lemma does not support the theorem.** §6.1 states

> **(A-high)** `T_n ≤ (ℓ² − ℓ − 1 − 1/ℓ)(1 + ℓ⁴/x)` for `x ≥ 1 772 201`,
> justified as "`T_n ≤ v(1 + v/x) ≤ v(1 + ℓ⁴/x)` using `v < ℓ²`".

`v < ℓ²` gives `v(1 + v/x) ≤ v(1 + ℓ²/x)`, **not** `v(1 + ℓ⁴/x)`. The stated justification does
not produce the stated inequality (it would need `v² < ℓ⁴`, which is a different — and true —
fact, but then the `ℓ⁴/x` belongs *inside* the expansion as `v²/x`, not as a factor multiplying
`v`). As printed, (A-high) is a *valid but much weaker* bound.

**(b) Under (A-high) as printed, Theorem C(b) is false by a factor of 38.** Requiring
`C(p_m) ≤ A(p_{n₀})` in Lemma W with `C =` (A-high)-as-printed and `A =` (A-low), and solving for
the true minimal separation `d = L_{n₀} − L_m` at each `ℓ = L_m` (this leg, `mpmath`, 50 digits,
`p_m = e^ℓ`, `ℓ ∈ [ℓ₁, 300]`):

| ℓ | `p_m` | required `d`, (A-high) **as printed** | `d` from PA-0's displayed formula |
|---|---|---|---|
| `ℓ₁ = 14.3877` | `1.772·10⁶` | **0.169340** | 0.0044887 |
| 16 | `8.89·10⁶` | 0.060196 | 0.0037056 |
| 18 | `6.57·10⁷` | 0.017191 | 0.0033155 |
| 20 | `4.85·10⁸` | 0.006280 | 0.0030854 |
| 44.36 | `1.84·10¹⁹` | 0.001681 | 0.0016810 |

The claimed uniform constant `d ≥ 0.004479` becomes valid only for `p_m ≳ 1.33·10⁹`. At the
bottom of (A-high)'s *own* stated validity range the required `d` is **0.1693**, i.e.
`p_m ≤ 0.8443·p_{n₀}` — **worse than Theorem C(a)'s Dusart-only `0.9396`**, inverting the
document's headline that Axler buys `0.99553`.

**(c) The quoted constant does not match the document's own displayed criterion.** §6.2 displays
the sufficient condition `d(2ℓ−1) + d² ≥ 0.17 − 1/ℓ + ℓ⁴/p_m`, whose maximum over `ℓ ≥ ℓ₁` is
**0.0044887** (attained at `ℓ₁`), not the `0.004479` that §6.2 and §9 item 15 report as
"`max d* = 0.004479 at ℓ = ℓ₁`". The reported sweep is **below** the document's own criterion —
i.e. it errs in the *unsafe* direction relative to the formula printed one line above it. §9 item
15 is presented as corroboration; it corroborates neither the printed lemma nor the printed
formula.

**What is nevertheless true — stated so the repair is not overstated.** With the *tight* form
`T_n ≤ v(1 + v/x)`, `v := ℓ² − ℓ − 1 − 1/ℓ` — which is what §6.2's algebra silently assumes —
this leg computes the true maximal required separation over `ℓ ∈ [ℓ₁, 300]` as
**`d* = 0.0043629` at `ℓ = ℓ₁`**. So `d ≥ 0.004479` **is** sufficient, and **Theorem C(b)'s
conclusion is correct**. The sweep-free branch `0.006992` is also sufficient. The defect is
entirely in the derivation and in the lemma the derivation names.

**Why this blocks anyway.** (i) The artifact states a lemma and then proves a theorem that does
not follow from it — the exact "mis-cited lemma" failure the run's own gates exist to catch.
(ii) The in-run numerical check (§9 item 15) reproduced the error rather than catching it, so the
artifact's verification apparatus gave a false green. (iii) §12 hands (A-high) to the Lean legs as
a hypothesis to transcribe; a faithful transcription of §6.1 makes `M-8`/Theorem C(b)
**unprovable**. (iv) The constant `0.004479` appears in §13's *defensible sentence* — the sentence
downstream is instructed to quote.

**Repair (one line).** Restate (A-high) as `T_n ≤ v(1 + v/x)` with `v := ℓ² − ℓ − 1 − 1/ℓ`;
replace `ℓ⁴/p_m` by `v²/p_m` in §6.2's displayed criterion; re-run §9 item 15 against the
corrected expression. `0.004479` then stands (true max `0.0043629`). **Theorem C(a) is
unaffected** — see §5.

---

## 3. MAJOR

### F3 — **MAJOR** — `proof-attempt-0.md` labels Theorem B's discharge "unconditional" and directs that P6′ be *retired*, on the strength of a source the run has not opened

**Where.** `proof-attempt-0.md` §2 verdict table, §4, §11 correction 1.

§2's verdict table row reads: "**The search-pruning that (M3) was wanted for** — **DISCHARGED**
unconditionally by Thm A + Thm B". §11 correction 1 escalates this to a directive: the obligation
"should be **retired**, not worked."

Theorem B's second half — the step from `g_k < S(p_k)` to `F` at `k` — is **Fact S2**, which the
document itself flags in §10 gap 4 as resting on `axler2014newbounds`, tier **L2_strong, NOT
OPENED in this run**, with a validity range (`x ≥ 2 634 800 823`) that card `T1` records as
having been **moved nine orders of magnitude by a corrigendum**. "Unconditional" is being used in
its mathematical sense (no unproved *conjecture*) in a table that a reader will take as "nothing
outstanding", two sections before the flag appears.

Retiring the run's ranked open obligation #1 on an unread paper is a one-way action. The
mitigation exists and the document names it (§10 gap 4: re-derive Theorem B on the Dusart-only bar
`B(x) = log²x − 1.1 log x`, feasible, at the cost of a bar `≈ 0.1L` looser) — **but it has not
been done**, and §11 does not condition the retirement on it.

**Repair.** Either carry out the Dusart-only re-derivation (`proof-attempt-2.md` §2.4 Lemma 3
already supplies exactly that bar, and §5 below confirms it is monotone and correct), or
downgrade §11 correction 1 from "retire" to "retire *conditional on the citation gate raising
Axler to L0, else re-derive on Dusart*".

### F4 — **MAJOR** — `proof-attempt-1.md`'s headline "at no other index whatsoever" is false as stated, and conflicts with `notebook-1`

**Where.** `proof-attempt-1.md` §0 headline, §5 Theorem A, §13 summary; vs
`notebook-1/findings.md` §1 F2 table.

Theorem A is correctly stated: `S := { n ≥ 3 : B_n ≤ T_n } = {3}`. The **`n ≥ 3` restriction is
load-bearing** and it is dropped in both places the result is quoted for downstream use:

> §0: "certifies the Firoozbakht inequality at **exactly one index, `n = 3` (`p = 5`)**, and at no
> other index whatsoever."
> §13: "certifies Firoozbakht's inequality at the single index `n = 3` — the prime 5 — and at no
> other."

Recomputed by this leg (`mpmath`, 40 digits):

| `n` | `p_n` | `B_n = (22/25)√p·log p` | `T_n` | `B_n < T_n` |
|---:|---:|---:|---:|:---:|
| 1 | 2 | 0.86262717 | 2.0000000 | **yes** |
| 2 | 3 | 1.6745100 | 2.1961524 | **yes** |
| 3 | 5 | 3.1669551 | 3.5498797 | yes |

The envelope clears the bar at `n = 1` and `n = 2` as well. What excludes them is **CMS's
hypothesis `p_n > 3`**, not the arithmetic — a materially different statement, and the one a
reader needs, since it says the obstruction is the *source's range*, not the *function*.

This also produces a visible cross-artifact conflict: `notebook-1` §1 F2 reports
`p*(22/25) = "p ≤ 5"`, i.e. three certified primes, against PA-1's "one index … and no other".
Neither artifact cites the other. Both are right; the words are not.

**Repair.** Quote Theorem A with its quantifier: "*at exactly one index in the range where the
CMS bound is available (`n ≥ 3`), namely `n = 3`*".

### F5 — **MAJOR** — `notebook-0`'s claim of *exact* reproduction of the `55.92 %` statistic is false, and three mutually incompatible fractions for it circulate in the run

**Where.** `notebook-0/findings-0.md` §3 R4 and §5; `proof-attempt-0.md` §5 and §9 item 18;
card `L15` "Why it is not a triviality"; `notebook-1/findings.md` §2.

Recomputed by this leg at `N = 3·10⁶` (216 816 primes):

| convention | count | percent |
|---|---|---|
| `T_{n+1} < T_n`, **`n ≥ 10`** | **121 238 / 216 805** | 55.9203 % |
| `T_{n+1} < T_n`, **all `n`** | **121 239 / 216 814** | 55.9184 % |

- Card `L15` states `121 238 / 216 805` — **correct**, for `n ≥ 10`.
- `notebook-0` R4 states `121 239 / 216 814` and describes it as "reproduced **exactly** at its own
  bound". It is the *all-`n`* count. The numerator differs from `L15`'s. The percentages agree to
  four significant figures; the fractions do not, and "exactly" is the wrong word for a different
  numerator over a different denominator.
- `proof-attempt-0.md` §9 item 18 states `121 238 / 216 806`, and §5 asserts that the difference
  from upstream's `216 805` "is a range convention". It is not: `216 805` is the exact count of
  steps `n → n+1` with `n ≥ 10` in this sieve, and `216 806` matches **neither** convention. PA-0's
  denominator is an off-by-one; its claim that the numerator "agrees exactly" with upstream is
  correct, and its explanation of the denominator is not.

Same class of slip in `notebook-1` §2: `374 485 / 664 569` at `10⁷`; this leg gets
`374 485 / 664 568` (numerator exact, denominator off by one).

**Why MAJOR and not MINOR.** The `55.92 %` figure is the single most-quoted statistic in the
corpus — it is the stated reason `T` is not monotone, which is the stated reason P6′ is open,
which is the stated reason target #0 exists. Three different fractions for it, one of them
labelled an *exact reproduction* of another, is a provenance failure at the root of the
obligation tree.

### F6 — **MAJOR** — `notebook-1/findings.md` §1 F2's definition of `p*(C)` contradicts its own table

**Where.** `notebook-1/findings.md` §1 F2.

> "Define `p*(C)` = the largest `P` such that `B_C(p) < T(p)` for all **`10 ≤ p ≤ P`**"

The table then reports `p*(1) = 3`, `p*(22/25) = 5`, `p*(4/π) = 2` — all **below** the stated
lower endpoint `10`, which makes the defining condition vacuous and the reported values
unreachable under the definition as written. This leg reproduces the table's values under the
reading `2 ≤ p ≤ P` (see F4), so the values are right and the definition is mistyped.

The row that matters downstream is `1/(8π) → p ≤ 62 869`, quoted as evidence that circulating
constants "certify a conditional theorem weaker than a laptop". That conclusion survives; the
definition must be fixed before the paper reprints the table, because as written the table is
unfalsifiable.

---

## 4. MINOR

### F7 — **MINOR** — `proof-attempt-0.md` §9 item 7 states the P6′ predicate with the inequality reversed

The verification table row reads "`T_n < T_{m(n)}`, `m(n)` = governing record index — **0
exceptions in 216 815 pairs**". The predicate P6′ requires `T_{m(n)} ≤ T_n`. As printed, the row
claims zero exceptions to the *opposite* inequality, which this leg's recomputation shows is
violated at essentially every index. A transcription slip in a table headed "Verification
performed by this leg" — the one place a reader is entitled to read literally.

### F8 — **MINOR** — `proof-attempt-1.md` §5 Remark 3: "essentially the whole verified range" glosses a real shortfall

Remark 3 argues RH is not load-bearing because `visser2018andrica` §7 verifies the CMS inequality
unconditionally for `p < 1.836·10¹⁹`, "so over essentially the whole verified range (**Fact 4**,
`2⁶⁴ = 1.8447·10¹⁹`)". `1.836·10¹⁹ < 1.8447·10¹⁹`: the unconditional range falls short of the
verified range by `≈ 0.47 %`, i.e. by roughly `8.7·10¹⁶` — about `1.9·10¹⁵` primes. The remark's
point stands; "essentially" is carrying an unstated gap and should carry a number instead.

### F9 — **MINOR** — `proof-attempt-1.md` §9 Claim 2 draws a universal from one instance, and picks the *widest* available bracket

Claim 2 concludes "**no** unconditional `π(x)` estimate in the run's toolbox (card **T1**)
separates `q` from the primes" from a single comparison against Dusart Thm 6.9 eq. (6.5), whose
two-sided bracket has width `0.2762·x/log²x`. Card `T1` also carries eq. (6.6)
(`x/(log x − 1) ≤ π(x) ≤ x/(log x − 1.1)` on their ranges), whose bracket width is
`≈ 0.1·x/log²x` — narrower by a factor `≈ 2.8`, and the tighter of the two.

The conclusion survives (`0.1·x/log²x` still dwarfs `log x · log log x` by an unbounded factor),
so nothing downstream moves. But the argument as written establishes the claim for one estimate
and asserts it for all of them, and it does so using the weaker instrument when the stronger one
was in hand. The document already marks the surrounding gloss as unproved (§11 item 9); this is
inside the *proved* Claim 2.

### F10 — **MINOR** — `notebook-2/findings.md` §3 mislabels `eps · T` as "one ulp"

> "One ulp of `T ≈ log²p` at `2⁶⁴` is `4.269·10⁻¹³`"

`T ≈ L² − L − 1 = 1922.57` at `2⁶⁴`, which lies in `[1024, 2048)`, so one float64 ulp is
`2⁻⁴² = 2.2737·10⁻¹³`. The quoted `4.269·10⁻¹³` is `eps · T = 2.2204·10⁻¹⁶ × 1922.57` — the
*relative* machine epsilon times the value, i.e. an upper bound of about two ulps, not one ulp.
The stated crossover ratio `1.04` becomes `≈ 1.96` with the true ulp; the qualitative conclusion
(same order of magnitude) is unchanged, and the section already caveats the extrapolation. The
label is still wrong in a passage whose whole point is numerical hygiene.

### F11 — **MINOR** — `proof-attempt-2.md` G1 offers a mitigation that its own §2.7 caveat 2 withdraws

G1 (the unread Dusart eq. (6.6)) is rated MAJOR "mitigated twice", the second mitigation being
"the threshold agreement with Kourbatov's independently published `g < 1920` would expose a wrong
range". §2.7 caveat 2 then records that Kourbatov's *own* criterion yields `1922`, so his
published `1920` is conservative relative to it, and that the agreement with this leg's `1918` is
"partly arithmetic luck at even-gap granularity".

A threshold that is conservative by an unquantified margin cannot detect a wrong validity range.
The mitigation should be struck, leaving G1 with one mitigation (the 1.27 M-prime numerical check,
which is genuine — this leg reproduces it, §5).

### F12 — **MINOR** — `proof-attempt-0.md` §9 item 19's misclassification rates do not reproduce to the four digits claimed

PA-0 reports the `T`-increase rule's misclassification at threshold `L − t` as `t=0`: 7.0745 %,
`t=1`: 2.7942 %, `t=2`: **0.2947 %**, `t=3`: 7.1875 %, and states this "reproduces upstream to 4
digits". This leg, at the same `N = 3·10⁶`, gets **7.0747 / 2.7946 / 0.2952 / 7.1877**. The
agreement is to three digits, not four; the discrepancy is consistent with a `≥` vs `>` boundary
convention or an `n ≥ 10` cut that is not stated. The finding PA-0 draws from it (`L − 2` is the
correct single-step threshold, because `π(x)/x ≈ 1/(L−1)`) is unaffected — this leg confirms
`t = 2` is the minimiser by an order of magnitude.

### F13 — **MINOR** — `proof-attempt-0.md` §10 gap 6's constants will need re-checking under the F2 repair

Gap 6 notes that if the `p_{n₀} > 2⁶⁴` frontier were smaller, "the constants `72` and `132` would
need re-checking". Under the F2 repair the small-`p_m` branch of Theorem C(b) must be extended
from `p_m < 1 772 201` to `p_m < 1.33·10⁹` (where the corrected `d*` falls below `0.004479` under
the *as-printed* lemma) if the printed (A-high) is retained rather than tightened. The relevant
constant is then the largest gap below `1.33·10⁹`, not `132`. Recorded here so the repair is not
applied half-way.

### F14 — **MINOR** — `notebook-2/findings.md` §1.4's dichotomy relies on gap parity without saying so

"Either `g_n ≤ 108` and Corollary A1 settles it … or `g_n ≥ 110`" is exhaustive only because
prime gaps are even above `p = 2`. The step is correct (the section is scoped to `p_n ≥ 60 184`)
and the same parity assumption is used explicitly elsewhere in the corpus (`proof-attempt-2.md`
§2.7: "Every prime gap after `g_1 = 1` is even"). It is unstated here, in the passage titled "Why
the table test is sound", which is the passage a Lean transcription would work from.

---

## 5. What was attacked and came back clean

A red-team report that lists only hits is not calibrated. Every item below was independently
recomputed or re-derived by this leg and **survives**.

| # | Claim attacked | Verdict |
|---|---|---|
| 1 | **PA-0 Lemma M / M′** (monotone-bar principle) — the engine of the whole document | **CORRECT.** Re-derived line by line. Only monotonicity of `B` is used; the `N₁` side condition in M′ is genuinely load-bearing and correctly discharged (`max{g_j : j ≤ 9} = 6 < S(29) = 6.80139`, reproduced). |
| 2 | **PA-0 Theorem C(a)** and its constant `0.0623` | **CORRECT and conservative.** This leg's independent sweep of the true required separation under (D-high)/(D-low) gives `max d* = 0.062080` at `ℓ = log 60 184`; `0.0623` covers it. The `ε = (ℓ²−ℓ)²/p_m` bookkeeping — the exact place C(b) goes wrong — is right here. |
| 3 | **PA-0 §9 items 2–5, 13** | Reproduced exactly: `S`-breaches `= {1,2,3,4,6,9}`; of these `{1,2,4,9}` are records and `{3,6}` are not; max gap below `60 184` `= 72` at `p = 31 397`; max gap below `1 772 201` `= 132` at `p = 1 357 201`. |
| 4 | **PA-1 Lemma A.1** (`√x > (25/22) log x`) | **CORRECT.** Stationary point `x* = 625/121 = 5.16529`, `h(x*) = 0.406862 > 0`. Reproduced at 40 digits. |
| 5 | **PA-1 Theorem A's six-row table** | **CORRECT** to every digit quoted (`n = 3,4,5,6,7,10`), all comparisons strict. Only the `n ≥ 3` framing is at fault (F4). |
| 6 | **PA-1 Theorem C** (critical constant `2/e`) | **CORRECT.** `max_x log x/√x = 2/e = 0.7357589` at `x = e²`; Lambert-`W` endpoints correct; the table rows `C = 0.5, 0.1, 0.01` reproduce (`x⁺ = 74.19`, `8099`, `2 122 265` — 20 / ~1018 / ~157 000 primes). |
| 7 | **PA-1 Theorem D / Cor. D.1** (`8.72·10⁷` at `2⁶⁴`) | **CORRECT.** `(22/25)√p·L/(L²−L−1) = 8.722·10⁷` at `p = 2⁶⁴`. The `C ≤ 1.009·10⁻⁸` figure also reproduces. |
| 8 | **PA-1 Theorem E** (counter-model to `(Cr) ⟹ F`) | **CORRECT.** Construction re-derived; `J_k ≥ 0` restriction is genuinely load-bearing and correctly flagged; Claims 1–4 go through; the `n_k ∈ {5,16,256,65536}` table reproduces exactly (`q = 11, 57, 1634, 821 709`; `J = 4, 11, 53, 180`; `T^{(q)} = 6.769, 16.387, 47.914, 170.778`). The `n_k = 5` non-violation is correctly attributed to the `L13` exception set, not to a defect. |
| 9 | **PA-2 Lemmas 1–4 and Theorem 2** | **CORRECT.** Lemma 3's derivation (`e^t − 1 > t` + Dusart upper bound on `π` → lower bound on `T`) is right, and the direction (upper bound on the *rank* yields a lower bound on the *bar*) is the correct one. Lemma 4's monotonicity is right. Theorem 2's two-case split is exhaustive and case 2's `G₀ = 72 < B(60 184) = 109.008` is reproduced. |
| 10 | **PA-2 §4 verification table** | Reproduced: `min(T − L(L−1.1)) = +0.079891473` at `p = 155 893` for `p ≥ 60 184`; `max ρ (n ≥ 10) = 0.7604709` at `n = 217`, `p = 1327`, `g = 34`; largest even `g` with `S(g) ≤ 2⁶⁴` is **1918** (`S(1918) = 1.8209·10¹⁹`, `S(1920) = 1.8629·10¹⁹`); under `L²−L−1.17` it is **1922**; `h(p)` sign change at `p* ≈ 777 601`. |
| 11 | **PA-2 Prop. 3 / Prop. 4** (the table-free window `[396 738, 777 600]`) | **CORRECT.** `h(396 738) = −2.35·10⁵`, `h(777 600) < 0 < h(777 601)`, `h' > 0` on `[4·10⁵, ∞)` verified. The obstruction (Prop. 4) is correctly stated as a scale mismatch, not a constant. |
| 12 | **notebook-2 §1.6** (`L(L−1.1)` at `2⁶⁴`) | **CORRECT** to all digits: `1919.1379834975`. The local/global caveat the leg insists on is the right caveat. |
| 13 | **notebook-2 §1.4** safety factors | Reproduced: `min P₁(g)/S(g) = 5.3371` at `g = 112`, `P₁(112) = 370 261`, `S(112) = 69 375.4`. The claim that this minimum does not move across four decades is consistent with everything this leg can reach. |
| 14 | **notebook-2 §2.1** (`F2` margin is a `1/n` artefact) | **CORRECT and important.** Independently confirmed that `max ρ (n≥10) = 0.7604709` at `3·10⁶` while the `F2` margin reads `0.9999984` — the two statistics are measuring different things and only `ρ` is diagnostic. This is the single best catch in the corpus. |
| 15 | **`ρ` extrema** | Reproduced: `max ρ` over all `n` is `0.911985` at `n = 4`, then `0.910684` at `n = 2`; both below the `n ≥ 10` cutoff. `notebook-0` R4 and `notebook-2` §1.1 agree with each other and with this leg. |
| 16 | **`lean/` tree** | **Clean on inspection.** `p n := Nat.nth Nat.Prime (n - 1)` — the 0-indexing correction is applied, `Conjecture := ∀ n, 1 ≤ n → F3 n` carries the `1 ≤ n` guard, `T n := (p n)^(1+1/n) − p n` is the right bar. Exactly one `sorry` (`Statement.lean:186`, the open target). No `axiom`, no `native_decide`, no `unsafe`, no `@[implemented_by]` — grep-confirmed by this leg. `audit_exhaustive.lean` replaces a hand-maintained list with an environment walk and was self-tested against a planted `sorry`: this is the right shape for the gate. |
| 17 | **Does any artifact assume `F`?** | **No.** Every one of the six documents states `F` OPEN at the top and none of them uses `F` as a hypothesis anywhere. The `Σ₁/Π₁` asymmetry is stated correctly in all four places it appears. |
| 18 | **Does any artifact pass a scale-limited computation off as general?** | **No.** Every notebook and proof attempt carries an explicit scale disclaimer naming the decades short of `2⁶⁴`, and PA-0 §9, PA-1 §10 and PA-2 §4 each restate it after the table rather than before. This is the discipline the brief asked me to hunt for and I could not find a violation of it. |

---

## 6. Reading of the fault set

The corpus does not fail in the way a math-attack corpus usually fails. There is **no** assumed
conclusion, **no** circular reasoning, **no** sieve-to-`10⁷` result dressed as a theorem, and no
laundering of a pruned search into a verification height — every one of those was hunted and
came back clean (§5 items 17–18).

It fails in two other ways, and both are structural rather than local:

1. **Vocabulary collision across legs (F1, F4, F5, F6).** Four of the six findings above are the
   same failure: a symbol or a phrase that means different things in different artifacts, with no
   leg holding the cross-artifact view. `m(n)`, "certifies at index `n`", `55.92 %`, `p*(C)`.
   Each leg is internally rigorous and each is scrupulous about *its own* declared gaps; nobody
   owned the seams. This is the predictable failure mode of a fan-out with no reconciliation
   stage, and it is what a `synthesize` leg must be tasked with — not summarising, but
   **reconciling**.

2. **In-run numerical checks that reproduce the algebra instead of testing it (F2, F12).** PA-0
   §9 item 15 swept an expression derived from the same wrong step as the theorem it was meant to
   corroborate, and reported PASS. A check written from the *derivation* cannot catch an error in
   the derivation; it must be written from the *statement*. Every numeric verdict in this document
   was produced that way, which is why F2 was visible from here and not from inside PA-0.

Neither BLOCKER touches `F`. **`F` remains OPEN**, and nothing in this red-team moves it in either
direction.

---

*Artifact of leg `skeptic`, molecule `task-20260725-488f`, run `germ-20260725-791a7c45`.
Verification scripts: `attack/skeptic-checks/`. The conjecture remains **OPEN**.*
