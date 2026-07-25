# Firoozbakht's conjecture — synthesis of the attack

**Molecule:** `task-20260725-cfd7` (leg `synthesize`, crew role: synthesizer)
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-25 · **Formal backend:** Lean 4 / Mathlib
**Conjecture under attack (`F`):**

> `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1` — equivalently, `n ↦ (p_n)^{1/n}` is strictly
> decreasing.

---

## 0. The verdict, in one screen

| Question the brief posed | Answer |
|---|---|
| Was `F` **PROVEN**? | **No.** |
| Was `F` **REFUTED**? | **No.** |
| Status of `F` after this run | **OPEN**, and every one of the eleven artifacts read below says so of itself. |
| Evidence-gate status | **BLOCKED** — failing leg `SKEPTIC`, two unrepaired BLOCKERs. |
| Citation clearance | **NOT ESTABLISHED — the citation audit has not run.** It gates the paper downstream, not this document. |

**The one-sentence result of the whole run.** *Firoozbakht's conjecture was neither proved nor
refuted; what the run produced instead is (i) a machine-checked reduction of `F` to the prime-gap
inequality `g_n < T_n`, (ii) an unconditional, table-driven verification architecture that
reproduces the published `2⁶⁴` frontier from first principles, (iii) an exhaustive independent
sweep to `10¹¹` finding no counterexample and no near-miss, (iv) four proved theorems closing the
Riemann-Hypothesis route as a route, and (v) an unconditional discharge of the run's own
ranked-#1 open obligation — offset by two named, unrepaired defects in the corpus that hold the
gate shut.*

**What must not be written downstream.** Not "Firoozbakht is true": no proof exists and the
run's own obstruction analysis (§4.1) shows none is near. Not "Firoozbakht is false": the
Cramér–Granville tension is a heuristic, not a test. The defensible sentence, inherited from
`decompose` §9 and unweakened by anything found since, is: *Firoozbakht's conjecture is
numerically robust over the verified range and simultaneously incompatible with the standard
Cramér–Granville heuristic; at least one of the two must fail, and no current technique can say
which.*

---

## 1. The trajectory — how many rounds, and did the list shrink or churn?

**One round ran. It was round 1, and it is the round the verdict rests on.**

`attack/re-attack/reattack-verdict.json` records `rounds_target = 1`, `rounds_run = 0`,
`exit_reason = "rounds-exhausted"`, `final_round.round = 1`. The zero is not a failure to run —
it is the formula's early exit: at `rounds = 1` the re-attack loop never nucleates a *second*
round, because round 1 (the spore's pinned informal + formal branches) **is** the whole attack.
Every artifact this synthesis folds is round 1's. There is no `attack-round-K/` directory on disk
because at `rounds = 1` there is nothing to disambiguate.

**Did the still-unproved list shrink, or merely churn?** Neither, honestly — and saying so
plainly is the point:

- On the **formal side it shrank, sharply and once**: the Lean skeleton declared five `sorry`s;
  `lean-probe` discharged four with real proof terms, and six further declarations were promoted
  from `sorryAx`-contaminated to clean without being touched. The survivor is
  `Firoozbakht.firoozbakht` — the conjecture itself. That number **cannot** go to zero inside
  this run, and an attack on an open `Π₁` statement whose `sorry` count reaches zero would be
  reporting a fabrication, not a result.
- On the **informal side there is no trend to report at all.** One measurement is not a
  trajectory. The skeptic's fault set (2 BLOCKER / 4 MAJOR / 8 MINOR) is a first reading, not a
  second one, and nothing in this run compares it to a predecessor.

**So the honest signal about "will more rounds help?" is: unknown, and the run cannot say.**
What it *can* say is narrower and more useful — the two BLOCKERs both have named, one-paragraph
repairs already written down (§6), neither touches `F`, and a round 2 whose only job was to apply
them would clear the gate. That is a mechanical claim about two documents, **not** a claim that
more rounds move the conjecture. Nothing in this run suggests any number of rounds moves the
conjecture.

---

## 2. What was PROVED

Confidence codes: **[K]** = machine-checked by the Lean kernel; **[P]** = paper proof, derived
in-run and independently re-derived by the skeptic leg; **[P·s]** = paper proof, derived in-run,
skeptic-confirmed, but resting on a source not opened in this run; **[C]** = finite computation,
exhaustive and independently reproduced.

### 2.1 The reduction chain — `[K]`

`Conjecture ↔ ConjectureReal ↔ (∀ n ≥ 1, g_n < T_n)`, where `T_n := p_n(p_n^{1/n} − 1)`, is now
**machine-checked**, not asserted. `lake build` exits 0 (1984 jobs); an exhaustive, list-free
axiom audit walks 60 declarations and finds exactly one `sorryAx` dependent — the open target.
No `axiom`, no `native_decide`, no `unsafe`, no `@[implemented_by]`, grep-confirmed by two
independent legs.

This matters more than its difficulty suggests. The run's central strategic move is *"Firoozbakht
is a prime-gap bound, therefore the analytic gap literature is admissible."* That move now rests
on the kernel rather than on a paper argument, and the equivalences were shown non-vacuous:
`g 1 = 1` and `T 1 = 2^2 − 2` are pinned to numerals, so a wrong `g` or a wrong `T` fails to
compile instead of passing quietly. The fidelity anchor (`Statement.lean` signatures) was
mechanically diffed against the skeleton — zero signature changes — which is what forecloses the
"closed a `sorry` by weakening the statement" failure.

The checker itself was tested rather than trusted: 27 adversarial statements, all false or
ill-formed, run through the same toolchain; 27/27 behaved as specified, and the one entry that
**no gate in this run catches** (`V04`, a true-but-differently-meant statement produced by ℕ→ℝ
coercion) is named as such instead of being omitted.

### 2.2 The maximal-gap reduction — the run's ranked-#1 obligation, discharged — `[P·s]`

`decompose` §2.4 posed **P6′** ("prove `T_m ≤ T_n` for record-straddling pairs") and ranked it the
attack's most tractable open obligation. `proof-attempt-0` shows the obligation is **misdirected**:

- **Lemma M (monotone-bar principle)** `[P]` — if `B` is nondecreasing in `p` and a `B`-breach
  exists, the *least* one is a strict maximal-gap index. Elementary; only monotonicity is used.
  Skeptic re-derived it line by line: correct, and the `N₁` side condition in the truncated form
  `M′` is genuinely load-bearing and correctly discharged (`max{g_j : j ≤ 9} = 6 < S(29) =
  6.80139`).
- **Theorem B** `[P·s]` — instantiate `M′` at Kourbatov's *monotone* surrogate bar
  `S(x) = log²x − log x − 1.17`. Checking record indices then certifies **every** index in range.
  `T`'s oscillation is irrelevant to the pruning, because the pruning need never run against `T`.

**The consequence, stated carefully.** The pruning rule that the whole computationally-live route
depends on is licensed unconditionally — *provided* the step from `S` to `T` (Fact S2) holds, and
that step rests on `axler2014newbounds`, tier **L2_strong, not opened in this run**, with a
validity range (`x ≥ 2 634 800 823`) that a corrigendum moved by nine orders of magnitude. The
skeptic flags (**F3**) that `proof-attempt-0` calls this "unconditional" in a verdict table two
sections before the flag appears, and directs that P6′ be *retired* on that basis. **This
synthesis does not retire it.** The correct status is: *discharged, conditional on the citation
gate raising Axler to L0 — else re-derivable on the Dusart-only bar `L² − 1.1L`, which
`proof-attempt-2` §2.4 already supplies and which the skeptic independently confirms is monotone
and correct, at the cost of a bar looser by `≈ 0.1L`.*

### 2.3 The unconditional finite-range theorem — `[P·s]` + `[C]`

`proof-attempt-2` reconstructs, from first principles, the architecture by which the literature's
`2⁶⁴` frontier is actually certified:

- **Lemma A** `[P·s]` — for `p_n ≥ 60 184`, `T_n ≥ L(L − 1.1)`, from Dusart (2010) Thm 6.9
  eq. (6.6) (tier **L0**, fetched and read). The *direction* is the content: `T_n` decreases in
  `n` at fixed `p_n`, so lower-bounding `T_n` requires an **upper** bound on the rank — which is
  what Dusart's upper bound on `π` supplies. The validity range is load-bearing, not decoration:
  `L(L−1.1)` crosses `L² − L − 1` exactly at `x = e¹⁰ = 22 026`, below which the lemma is false.
- **Corollary A2** `[P]` — a gap of size `g` can violate `F` only at `p_n ≤ S(g) :=
  exp((1.1 + √(1.21 + 4g))/2)`. This converts the whole verification into a **first-occurrence
  gap-table lookup**, and a gap size that passes is safe *everywhere*, not merely below the
  sieved bound.
- **Independent reproduction of the published `1920`** `[C]` — `L(L−1.1)` at `2⁶⁴` is
  `1919.1379834975…`, so a gap of at least 1920 is needed to violate `F` just below `2⁶⁴`. The
  published integer falls out of Lemma A with no tuning. `notebook-2` insists on the caveat that
  makes this honest: Lemma A yields the *local* statement at the frontier; the endnote's phrasing
  is *global*, and closing that needs the table again.
- **A table-free window** `[P]` — `396 738 ≤ p_n ≤ 777 600`, where `F` follows from unconditional
  analytic estimates with **no enumeration of primes at all** — and a proof that the window
  **closes permanently** at `p ≈ 7.776·10⁵`. Skeptic re-derived both endpoints and the
  monotonicity: correct. To this run's knowledge the window is not stated anywhere in its inputs.

### 2.4 The RH route is closed — as a route — `[P]`

`proof-attempt-1` proves four theorems, all of which the skeptic re-derived and confirmed:

| Claim | Verdict |
|---|---|
| The sharpest published RH-conditional gap bound `g_n ≤ (22/25)√p_n·log p_n` certifies `F` cofinitely | **REFUTED** — it certifies `F` at exactly one index in the range where the source is available |
| *Some* bound `g_n ≤ C·p_n^θ(log p_n)^A` with `θ > 0` implies `F` beyond finitely many `n` | **REFUTED** (Thm B) |
| *Some* envelope `C√p log p`, any `C > 0`, implies `F` beyond finitely many `n` | **REFUTED** (Thm C) — `p*(C)` is finite for every `C > 0`; sharpening the constant is a treadmill, not a route |
| Cramér's `limsup ≤ 1` entails `F` over integer sequences | **REFUTED** by explicit counter-model (Thm E) |
| `RH ⟹ F` as a material implication | **UNDECIDED**, and the leg does not pretend otherwise |

**Theorem D** bounds below the *strength* of any proof of `RH ⟹ F`: composed with Kourbatov's
unconditional `F ⟹ (∀k>9: g_k < L_k² − L_k − 1)`, such a proof would immediately yield an
RH-conditional Cramér-scale gap bound — stronger than the best published RH-conditional bound by
a factor `8.72·10⁷` at `2⁶⁴` and **unbounded** thereafter. This is a distance between two
statements, not a measure of proof effort, and `proof-attempt-1` says so explicitly.

### 2.5 The smooth model — `[P]`

`decompose` §3.6 derives that the smooth surrogate `(x log x)^{1/x}` is strictly decreasing on
`x ≥ 5` — so **the smooth model of Firoozbakht is true and elementary**, and the entire difficulty
localizes to the fluctuation of `p_n` around `n log n`. Not formalized in Lean this run
(`lean-probe` names this as a non-delivery); the paper derivation stands, including its own
correction that the safe stated range is `x ≥ 5`, not `x ≥ 4`.

### 2.6 Computational corroboration — `[C]`

Two independent legs, independent code paths, exhaustive to **`10¹¹`** — 4 118 054 812 consecutive
prime pairs:

| | |
|---|---|
| violations of `F` | **0** |
| max `ρ_n = g_n/T_n` (`n ≥ 10`) | **0.8318** at `p_n = 25 056 082 087`, `g = 456` |
| largest gap in range | 464 |
| maximal-gap records | 40 |
| calibration against exact integer arithmetic | zero disagreements (`n ≤ 5000` one leg, `n ≤ 4000` the other) |
| sieve validation | `π(10⁹)`, `π(10¹¹)` match standard values |

The verification discipline is the part worth carrying: the escalation path **raises** rather than
returns when a margin lands inside its error budget, because *the silent failure is in the
verification direction* — a probe that only breaks on a detected violation reports "no
counterexample" out of noise.

---

## 3. What was REFUTED

Nothing about `F`. Everything below is a refutation of a *claim about the evidence* or of a
*route* — and that distinction is the whole discipline of this run.

1. **The RH route** — four theorems, §2.4.
2. **First-failure maximality does not follow from the definitions.** `notebook-0` exhibits an
   explicit increasing integer sequence whose first Firoozbakht failure is at a **non-record**
   gap, verified in exact integer arithmetic. Consequence: *any proof of FFM that does not consume
   an arithmetic density input is wrong.* The same section shows the counter-model is excluded
   unconditionally by Montgomery–Vaughan, by a factor that **grows** with scale (1.41 at `10³`,
   9.13 at `10¹⁸`) — so a weak arithmetic input suffices for this mechanism.
3. **The two-sided π-bound route to P6′ cannot work.** Bounding `T_m` above and `T_n` below with
   explicit `π(x)` estimates at the two endpoints separately demands record gaps orders of
   magnitude larger than reality, and past `≈10¹⁰` is unsatisfiable at *any* gap size. No
   sharpening of constants rescues it.
4. **The `0.9999984` "near-miss" is an artefact.** `decompose` §5.1 headlined
   `max n·log p_{n+1}/((n+1)·log p_n) = 0.9999984` as evidence of tightness. In a synthetic
   universe where **every gap is 2** the same statistic reads `0.99999991` while `ρ` is `0.059`.
   The statistic measures `1/n`. Only `ρ` is diagnostic. The skeptic calls this the single best
   catch in the corpus, and this synthesis agrees.
5. **"The tightest cases sit at record gaps" does not survive the range.** `decompose`'s "all six
   tightest `ρ` cases occur at record gaps" was a `best[:6]` print truncation. At `10¹¹`: 22 of
   the top 40, and the 4th-tightest case in four billion pairs is **not** at a record index. Read
   precisely: if P6′ holds a record search still misses no *counterexample* — what it misses is
   *near-misses*, so the observation cannot be used as evidence for the pruning rule that produced
   it.
6. **More sieve is not more evidence.** Two decades of extra sieving (`10⁸ → 10¹⁰`) produced no new
   near-miss; the record `ρ` moved exactly once, at `10¹¹`, and moved *at the next maximal gap*.
   Sieving buys the next maximal gap and nothing in between. The record that would matter
   (`ρ ≈ 0.948` at `p ≈ 1.693·10¹⁵`) is **4.2 decades** above anything this run reached.
7. **Littlewood oscillation is irrelevant** to the threshold (`O(L²·log log log x/√x) → 0`), and
   **Bertrand's postulate is useless** here (it implies `F` only at `n = 1`). Both recorded so no
   future leg rediscovers them as dead ends.

---

## 4. What remains OPEN

### 4.1 `F` itself — and why it is not close

The load-bearing obstruction, unchanged by anything in this run: **any proof of `F` yields
`g_n = O(log² p_n)` unconditionally.** The best known unconditional gap bound is `g_n ≪ p_n^{0.525}`;
under RH it improves only to `≈ √p_n log p_n`. Both are *powers* of `p_n`; `F` needs
*polylogarithmic*. That is not a matter of sharpening constants — it is square-root scale versus
log scale, and no known method bridges it even conditionally on RH. Any future leg proposing a
"direct proof" must say how it clears this, or it is proposing something already beyond the field.

Compounding it: **there is no induction mechanism.** `g_n` is not constrained by `g_1 … g_{n−1}`;
knowing `F` up to `n` gives no leverage at `n+1`. Any proposed inductive proof must first supply
the missing mechanism.

And on the refutation side: the best large-gap results reach
`≍ log n · log log n · log log log log n / log log log n` — an iterated-log factor above `log n`,
but a **full power of `log` below** what a counterexample needs. Explicit constructions fail for
a second, independent reason: they place the gap at an *unspecified* location, while `F` needs the
gap and the count `π(p_n) = n` at the *same* point.

**The refutation door is narrower than it looks even so.** `¬F` is `Σ₁` and finitely certifiable,
but the certificate must certify the **rank** `n`, not merely the two primes.

### 4.2 The tension that will not resolve itself

The Cramér random model, in Granville's corrected form, predicts `limsup g_n/log²p_n ≥ 2e^{−γ} ≈
1.1229 > 1`, which is **incompatible with `F`**. This is the strongest reason to believe `F` is
false, and it is not a proof. Both cannot be right; no current technique says which. The ledger
carries `granville1995cramer` at tier **L1** — fetched and read, but the pagination is the
preprint's, not the journal's, and all locators must be re-expressed before publication.

### 4.3 The residual analytic window

`proof-attempt-0`'s Theorem C proves first-failure maximality against all primes below
`0.939·p_{n₀}` (Dusart only, unconditional), tightening to a relative `O(1/log p)` sliver under
Axler. Inside that sliver the obstruction is exact and named: one needs an **upper** bound on
`π(p_m + y) − π(p_m)` within a factor `1 + 2/L` of the truth, where Brun–Titchmarsh gives only a
factor 2. `notebook-0` reaches the same wall from the computational side and prices it: typical
windows are settled unconditionally by Brun–Titchmarsh at **99.861 %** of governed indices, but
the extremal configuration needs a short-interval count sharp to `1 + 2.2/log p` — **Cramér
strength** — and that gap *widens* with scale even as empirical coverage improves. A pruning rule
is worth its worst case.

This is, in the run's own judgement and this synthesis's, the most tractable genuinely-open
analytic node it produced — and it is still an open problem in analytic number theory, not a
lookup.

### 4.4 Lean, honestly

Not formalized: the smooth model (`L4`), the `limsup` corollary (needs effective `π(x)` bounds not
assumed present in Mathlib), and any verified range past `n ≤ 4`. The last is a hard limit worth
naming: `Nat.nth` is noncomputable with no kernel reduction, and Mathlib's prime-specific `nth`
API is exactly five `@[simp]` base lemmas. Extending needs `Nat.count`↔`Nat.nth` bridging
machinery — a separate budgeted leg. Reporting a larger `N` without it would be a fabrication, and
the probe leg says so in those words.

---

## 5. Reconciliation — the seams between legs

The skeptic's structural reading is that this corpus does **not** fail the way math-attack corpora
usually fail. There is no assumed conclusion, no circular reasoning, no sieve-to-`10⁷` result
dressed as a theorem, no pruned search laundered into a verification height — all four were hunted
and came back clean, and eighteen further claims were independently re-derived and confirmed. It
fails at the **seams**: symbols that mean different things in different artifacts, with no leg
holding the cross-artifact view. Reconciling those is this leg's job, so here it is done — with
the caveat in §6 that reconciling in *this* document does not repair the *upstream* ones.

**`m(n)` and P6′ — three predicates, not one.** The phrase "governing record index" carries three
inequivalent meanings across the run, and `min(T_n − T_{m(n)})` was reported under all of them:

| Name (assigned here) | Definition | Who measured it |
|---|---|---|
| **P6′-gov** | `m(n)` = most recent maximal-gap index `≤ n` | card `L15`, `notebook-2` |
| **P6′-min** | `m(n) := min{ m : g_m ≥ g_n }` | `notebook-0` |
| **P6′-pair** | `T_m ≤ T_n` for **all** `m < n` straddling a record gap | `L15`'s prose |

`P6′-pair ⟹ P6′-gov ⟹ P6′-min`, strictly. **The search pruning consumes only the weakest,
`P6′-min`.** With that named, the run's two contradictory headlines cease to contradict — both
are true, of different predicates, and the skeptic reproduced both to every digit quoted:

- *"The empirical case for P6′ weakens with range"* is true of **P6′-gov**: its margin decays like
  `p^{−0.83}` (`+1.05·10⁻²` at `3·10⁶` → `+2.93·10⁻⁶` at `10¹¹`), zero exceptions throughout.
- *"The margin does not decay"* is true of **P6′-min**: flat at `+0.4845`, global minimum at
  `n = 1879`, never approached again across eleven decades, zero exceptions.

**Two downstream consequences of this reconciliation, which are corrections, not restatements.**
`notebook-2`'s float64-noise-floor alarm ("a float64 check of P6′ hits the noise floor at the
published frontier") is derived from the **P6′-gov** decay and **does not apply** to `P6′-min`,
which is `~10¹²` ulps clear of zero at every decade measured. Its inference that "the route to
discharging P6′ must therefore be the analytic one" rests on that mis-scoped premise and does not
survive it. Both stand corrected here.

**"Certifies at index `n`" — the quantifier is load-bearing.** `proof-attempt-1`'s headline says
the CMS bound certifies `F` "at exactly one index, `n = 3`, and at no other index whatsoever."
The theorem is stated correctly (`{n ≥ 3 : B_n ≤ T_n} = {3}`) but the `n ≥ 3` restriction is
dropped where it is quoted for downstream use. The envelope in fact clears the bar at `n = 1` and
`n = 2` as well; what excludes them is **the source's hypothesis `p_n > 3`**, not the arithmetic —
a materially different statement, and the one a reader needs. The correct form is: *at exactly one
index in the range where the CMS bound is available.* This also dissolves an apparent conflict
with `notebook-1`, which reported three certified primes: both were right, the words were not.

**`55.92 %` — one statistic, four fractions, and a convention nobody stated.** The most-quoted
number in the corpus circulates as `121 238/216 805` (card `L15`), `121 239/216 814`
(`notebook-0`, the all-`n` count, described as an "exact" reproduction of a *different* numerator
over a *different* denominator), and `121 238/216 806` (`proof-attempt-0`, which the skeptic leg
called an off-by-one matching neither convention).

**This leg recomputed it independently** (fresh `sympy` sieve to `3·10⁶`, written from the
statement, script `verify_syn.py`) and gets **`121 238/216 806 = 55.9200 %` for `n ≥ 10`** and
**`121 239/216 815 = 55.9182 %` over all `n`** — i.e. the two *numerators* are stable and
reproduce everywhere, but this leg's denominators are one **higher** than the skeptic's in both
conventions, and the `n ≥ 10` denominator matches `proof-attempt-0`'s exactly.

The correct reading is therefore *not* that one leg made an arithmetic error. There are 216 816
primes below `3·10⁶`, hence 216 815 comparisons `T_{n+1}` vs `T_n` available, of which 216 806
have `n ≥ 10`. Whether the **final** comparison is counted is a convention that **no leg states**,
and it moves every denominator by exactly one. That — not an off-by-one in any single document —
is the real defect: three legs and this verification produce four fractions for one statistic
because the counting convention was never written down. All four agree to four significant
figures.

The figure is also range-dependent — **57.88 % at `10⁹`** — and must never be quoted without its
bound. It remains uninformative about P6′.

**`p*(C)`'s definition.** `notebook-1`'s stated lower endpoint (`10 ≤ p ≤ P`) makes its own table
vacuous, since the reported values are all below 10. The values are right under the reading
`2 ≤ p ≤ P`; the definition is mistyped and must be fixed before any table reprint.

---

## 6. Evidence gate — status stated honestly

### **BLOCKED.** Failing leg: **SKEPTIC.**

| Leg | Status | Basis |
|---|---|---|
| LOOP (round resolution) | resolved | round 1 is live; `reattack-verdict.json` present and well-formed |
| KERNEL | **PASS** | `lake build` exit 0; exhaustive audit over 60 declarations finds exactly one `sorryAx` — the declared open target |
| SKEPTIC | **FAIL** | 2 residual BLOCKERs, repairs proposed and explicitly **not applied** |
| CORPUS | **PASS** | 27/27 adversarial entries behaved as specified; 109/109 verification checks green; non-coverage stated rather than omitted |

The backend is `lean`, not `none`, so the DEGRADED carve-out does not apply and the kernel leg
passes outright. One failing applicable leg blocks, regardless of the other three.

**The two BLOCKERs, and their exact status after this synthesis.**

- **F1 — the `m(n)` vocabulary collision.** *Reconciled in §5 of this document; **not repaired
  upstream**.* `notebook-0/findings-0.md`, `notebook-2/findings.md` and card `L15` still carry
  the collision, and `notebook-2` §3's two mis-scoped consequences are still printed there. A
  reader of those files, not of this one, is still misled.
- **F2 — `proof-attempt-0` Theorem C(b)'s mis-derived bound.** The stated lemma (A-high) does not
  follow from its stated justification; as printed the theorem is **false by a factor ≈ 38** over
  part of its own validity range, and the in-run numerical check reproduced the error rather than
  catching it — a check written from the *derivation* cannot catch an error in the derivation.
  The skeptic independently confirms the theorem's *conclusion* is nonetheless **true** under the
  corrected tight form (true required separation `d* = 0.0043629`, so the quoted `0.004479` is
  sufficient). The repair is one line — restate (A-high) as `T_n ≤ v(1 + v/x)` with
  `v := ℓ² − ℓ − 1 − 1/ℓ`, replace `ℓ⁴/p_m` by `v²/p_m`, re-run the numerical sweep against the
  corrected expression. **It has not been applied.** Theorem C(a) and its constant `0.0623` are
  unaffected and were independently confirmed conservative.

**Neither BLOCKER touches `F`.** That does not clear the gate, and this document does not ask it
to. The gate is on the state of the artifacts, and two of them are defective as written.

**Why this synthesis is publishable anyway, and what it is not.** Everything in §2–§4 above is
either kernel-checked, independently recomputed by the skeptic leg, or explicitly flagged with the
unopened source it rests on. Nothing here quotes `0.004479` as a derived constant, and nothing
here repeats the mis-scoped P6′ inferences. **This is a synthesis of a blocked corpus, honestly
labelled — not a seal.** A `write-paper` leg must treat it as such.

### Citation status — not cleared, and not claimed

The citation audit **has not run.** It gates the paper downstream. What exists now is the
`source-ledger`: 20 rows, 11 at **L0** (primary source fetched and statement read at the
locator), 3 at L1, 4 at L2_strong, 2 at L2_weak, **0 at L3**. Seven PDFs fetched and read in full
with MD5s recorded. That is a strong ledger, and it is *not* a citation clearance.

Three unopened sources are load-bearing and are named as the audit's priorities:

1. **Axler** — quoted through Kourbatov's proofs; his own corrigendum moved Corollary 3.5's
   validity range from `x ≥ 5.43` to `x ≥ 2 634 800 823`. Kourbatov's Theorems 1, 3 and 5 depend
   on it, and so does §2.2's Fact S2. **Priority 1.**
2. **Granville** — fetched and read, but at preprint pagination. Every locator must be
   re-expressed against the journal copy. This is the load-bearing citation of the entire
   refutation-side argument. **Priority 2.**
3. **Ribenboim, Oliveira e Silva–Herzog–Pardi, Shanks, Dusart (2018), Farhadian–Jakimczuk** — not
   opened; each is either mediated through an L0 citer or cited only for something available at
   L0 elsewhere.

---

## 7. What a next run should do

Ordered by leverage, and each one either repairs a named defect or attacks a node this run
localized rather than opened.

| # | Action | Why |
|---|---|---|
| 1 | Apply the two named repairs (F1 vocabulary, F2 one-line restatement) and re-run the skeptic | Mechanical, ~one hour of work, clears the gate. The repairs are already written. |
| 2 | Run the citation audit, Axler first, Granville second | §2.2's discharge and §4.2's tension both rest on unopened sources |
| 3 | Re-derive Theorem B on the Dusart-only bar `L² − 1.1L` | Removes the Axler dependency from the pruning discharge entirely, at the cost of a bar looser by `≈ 0.1L`. The bar is already proved in-run. |
| 4 | Attack the residual window (§4.3) as a short-interval prime-count problem | The one genuinely-open analytic node this run isolated exactly; the criterion is `1 + 2/L`, and it is stated in closed form |
| 5 | Formalize the smooth model (`L4`) in Lean | The only node in the formalization plan that is a genuine theorem rather than a definition or a finite check, and it is fully within Mathlib's reach |
| 6 | Do **not** fund more sieving | §3 item 6: sieving buys the next maximal gap and nothing in between, and the record that matters is 4.2 decades away |

**Standing instruction, carried forward unchanged.** The conjecture is open. Do not write
"Firoozbakht is true". Do not write "Firoozbakht is false". The Cramér–Granville tension is
evidence about which way to bet and nothing more.

---

## 8. Verification of this document

This leg emitted no notebook and no Lean, so there is no build to report. Instead, the synthesis
was checked against its brief in two ways.

**(a) Independent recomputation of every headline number this document states as a figure.** A
fresh sieve to `3·10⁶` (`sympy`, no upstream code path, written from the *statements* rather than
from any leg's source) — script `synthesize/verify_syn.py`, exit 0:

| Quantity as stated here | This leg's independent value | Verdict |
|---|---|---|
| primes below `3·10⁶` | 216 816 | ✓ |
| violations of `F` below `3·10⁶` | **0** | ✓ |
| max `ρ` (`n ≥ 10`) `= 0.7604709` at `n = 217`, `p = 1327`, `g = 34` | `0.7604708659…`, same index | ✓ |
| max `ρ` over all `n` `= 0.911985` at `n = 4` | `0.9119852327…` | ✓ |
| `L(L−1.1)` at `2⁶⁴` `= 1919.1379834975…` | `1919.1379834975328` | ✓ exact |
| `S(29) = 6.80139 > 6 = max{g_j : j ≤ 9}` | `6.8013853766…`, max gap `6` | ✓ (Theorem B's hypothesis (ii)) |
| CMS envelope clears the bar at `n = 1, 2, 3` but not `n = 4` | `B/T` = 0.863/2.000, 1.675/2.196, 3.167/3.550, **4.531/4.386** | ✓ — confirms §5's correction *and* `proof-attempt-1` Theorem A's `S = {3}` |
| smooth-model bracket changes sign just above `x = 4` | `+0.0084` at 4, `−0.0193` at 4.05, `−0.464` at 5 | ✓ (`x ≥ 5` is the safe range, not `x ≥ 4`) |
| `55.92 %` | see §5 — numerators reproduce, denominators disagree by one | **discrepancy, reported rather than smoothed** |

The last row is the one finding of this verification pass that changed the document. The first
draft of §5 asserted the skeptic's fractions as settled; the recomputation showed the skeptic's
denominators are one lower than this leg's in *both* conventions, and that `proof-attempt-0`'s
disputed `216 806` is the one this leg reproduces exactly. §5 was rewritten to state the real
defect — an unstated counting convention, not an arithmetic error in any one document. **This is
a correction to the skeptic leg's F5, made against the skeptic leg's own standard: a check
written from the derivation cannot catch an error in the derivation.**

**(b) Consistency against the brief.** Each required element is present and locatable: what was
proved (§2, with confidence codes), what was refuted (§3), what remains open (§4), the
evidence-gate status stated honestly as **BLOCKED** with the failing leg named (§6), the rounds
trajectory with the shrink-vs-churn question answered plainly rather than dressed up (§1), and an
explicit statement that the citation audit has not run and no clearance is claimed (§0, §6). No
claim in §2–§4 rests on the two BLOCKERs: the F2 constant `0.004479` is never quoted here as a
derived result, and the mis-scoped P6′ inferences are corrected in §5 rather than repeated.

**Not done.** This leg did not re-run the Lean build, the `10¹¹` sweeps, or the red-team corpus —
those are reported at the exit statuses their own legs recorded, which are quoted here rather than
re-derived. It did not repair the upstream artifacts (§6 says so), and it did not open any source
(§6's citation status).

---

## 9. Sources folded

All under `/Users/eserie/galaxies/firoozbakht-cleanroom/.cosmon/state/spore-runs/germ-20260725-791a7c45/`,
mirrored at `attack/` in the repository. Round 1 is the only round; every path below is round 1's.

| Artifact | Leg | Lines |
|---|---|---|
| `decompose/decompose.md` | decompose | 636 |
| `frame-deliberation/{frame,synthesis,outcomes}.md` + 5 persona responses | frame-deliberation | — |
| `concept-cards/` (30 cards + INDEX) | concept-cards | — |
| `source-ledger/source-ledger.md` | source-ledger | 898 |
| `proof-attempt__0/proof-attempt-0.md` | proof-attempt (target #0) | 603 |
| `proof-attempt__1/proof-attempt-1.md` | proof-attempt (target #1) | 892 |
| `proof-attempt__2/proof-attempt-2.md` | proof-attempt (target #2) | 461 |
| `notebooks__0/findings-0.md` | notebooks (target #0) | 172 |
| `notebooks__1/findings.md` | notebooks (target #1) | 207 |
| `notebooks__2/findings.md` | notebooks (target #2) | 375 |
| `lean-skeleton/`, `lean-probe/lean-probe-report.md` | lean | 279 |
| `red-team-corpus/coverage-report.md` | red-team-corpus | 249 |
| `skeptic/faults.md` | skeptic | 444 |
| `evidence-gate/evidence-verdict.md` | evidence-gate | 166 |
| `attack/re-attack/reattack-verdict.json` | re-attack | — |

---

*Artifact of leg `synthesize`, molecule `task-20260725-cfd7`, run `germ-20260725-791a7c45`.
No number in this document was invented; every figure traces to a cited source artifact. The
conjecture `F` remains **OPEN** — neither proved nor refuted by this run. The evidence gate is
**BLOCKED**. The citation audit has **not** run.*
