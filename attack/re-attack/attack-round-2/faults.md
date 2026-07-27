# faults.md — red-team of the round-2 Firoozbakht re-attack

**Molecule:** `task-20260726-7211` (leg `skeptic`, round 2) · **Parent loop:** `reattack-20260726-57d1`
**Date:** 2026-07-26
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.
**Status of `F` in this document: OPEN.** Nothing below proves or refutes it. This document attacks
the round-2 *artifacts*, not the conjecture.

> ### ⛔ SUPERSEDED — 2026-07-27 by the round-3 skeptic (`task-20260727-5096`)
>
> **This is no longer the corpus's current fault list.** `attack/faults.md` is, and it dispositions
> every finding below — **R2-B1, R2-B2, R2-B3, R2-M1, R2-M2, R2-M3, R2-m1 … R2-m7** — as CLOSED or
> STILL OPEN, verified in the tree rather than from the reconciliation's report of itself. Summary
> of what changed: R2-B1, R2-B3, R2-M1, R2-M3 and all seven MINORs are **CLOSED**; **R2-B2 limb 1 is
> STALE** (the ledger amendment *had* landed — this document's `:406`/`:642` line numbers resolve
> only in a pre-merge worktree); **R2-B2 limb 2 (tier propagation) and R2-M2 are STILL OPEN**, and
> two new BLOCKERs were raised against round 3. Round 1's list is preserved at
> `attack/faults-round-1.md`. **Quote this file only as history.**

> ### 🔗 Round-3 reconciliation banner — read this before quoting anything below
>
> A **reconciliation leg** (`task-20260727-264e`, 2026-07-27, round 3) owned the seams between the
> four round-2 artifacts. Its decisions are recorded in **`attack/reconciliation.md`** and are
> **binding on this document**, which has been amended in place where they touch it. The four
> round-2 artifacts, and where each stands after reconciliation:
>
> | artifact | role | status after round 3 |
> |---|---|---|
> | `proof-attempt-first-failure-maximality.md` (FFM) | P6′ predicates, Theorem C-a′/C-b′ | **carries the designated Theorem C-b′**; §4 denominators corrected, §5 gov/min ordering corrected, C-a′ header corrected |
> | `proof-attempt-unconditional-verified-range.md` (UVR) | Lemma H, (A-high\*), Theorem 2, the unconditional range | **Theorem C(b\*) retired to a remark**; Axler tier corrected L2_strong → **L0** |
> | `proof-attempt-RH-conditional-bound.md` (RH) | the RH route, five theorems | unchanged; its §10 sieve count `216 815` is the **correct** one and corroborates decision 4 |
> | `lean-probe-report.md` | the kernel leg + the barrier | clean; §4's slack table annotated (constants restored) |
>
> **The five decisions in one line each.** (1) The corpus's single repaired Theorem C(b) is
> **Theorem C-b′**, `p_m ≤ 0.998244·p_{n₀}`, off the Axler row `(2.1,0,0,0)/6 690 557` present in
> **both** editions; C(b\*) and the constants `0.99553`/`0.99565` are retired. (2)
> `axler2014newbounds` is **L0**, everywhere, with a standing ⚠ that the `(1,0,0,0)/1 772 201` row
> is **preprint-only**. (3) The ledger amendment **had already landed**; R2-B2's "never made" is
> stale, verified against the tree. (4) The `55.92 %` denominators are `216 806` (`n ≥ 10`) and
> `216 815` (all `n`) — a fourth independent recount, against FFM's original table and against both
> prior skeptics. (5) R2-M2, R2-M3, R2-m1, R2-m2 and R2-m4 are applied in place.
>
> **`F` remains OPEN.** Nothing in round 3 moves it; reconciliation removes ambiguity, not
> obstruction.

---

## 0. Verdict, stated first

**The BLOCKER set is non-empty. Round 2 is NOT clean.**

| Severity | Count | Findings |
|---|---|---|
| **BLOCKER** | **3** | R2-B1, R2-B2, R2-B3 |
| **MAJOR** | **3** | R2-M1, R2-M2, R2-M3 |
| **MINOR** | **7** | R2-m1 … R2-m7 |

### The two verdicts the brief demands, one line each

> **F1 — FIXED.** Not re-worded. `proof-attempt-first-failure-maximality.md` §1.2 names
> **P6′-pair / P6′-gov / P6′-min** explicitly, defines each in symbols, adds the missing fourth
> predicate **P6′-rec**, assigns every circulating measurement to the predicate it actually measures
> (§5 table), reconciles the two contradictory headlines without retracting either, and **refutes**
> the strongest of the three with two exhibited witnesses. I reproduced both witnesses, the full
> exception census, and every margin independently (§6 below). The F1 repair carries two new defects
> of its own (R2-M3, R2-m2), neither of which reopens F1.

> **F2 — FIXED as a derivation, by the leg the brief points at; but the fix is delivered TWICE, in
> two incompatible versions, and the provenance half is contradicted between them.**
> `proof-attempt-unconditional-verified-range.md` does exactly what `faults.md` F2's repair line
> prescribed: §3.2 restates the lemma as **(A-high\*) `T_n < v(1 + v/x)` with `v := ℓ² − ℓ − 1 − 1/ℓ`**
> — the tight form, no weakening step; §3.3 replaces **`ℓ⁴/p_m` by `v²/p_m`** in the displayed
> criterion (★); and §3.4 **re-derives** the constant in closed form (Proposition R1: `E` decreasing,
> a majorant `φ`, `φ` decreasing) instead of re-asserting it or re-sweeping it. I re-derived R1's
> three steps and recomputed every constant at 50 dps: `d*(ℓ₁) = 0.004363567696`, and the true
> requirement solved from Lemma W is `0.0043628824`. **The derivation repair is real.**
> **But** the sibling leg repaired the *same* BLOCKER independently and shipped a *different*
> theorem with a *different* constant off a *different* Axler row (R2-B1), gave the same source a
> contradictory tier on the same day (R2-B2), and the column UVR's repair rests on turns out to
> exist in one edition only (R2-B3). F2's mathematics is closed; F2's artifact-level consequences
> are not.

**Nothing below is softened.** Three BLOCKERs means the loop did not reach its quality fixpoint in
round 2, and the honest exit is `rounds-exhausted / BLOCKED`, not convergence.

---

## 1. Perimeter — what was read, and what was recomputed from scratch

**Read in full:** `attack/faults.md` (round 1, 444 lines — read first, for calibration and to avoid
re-litigating its §5 clean list); `attack-round-2/proof-attempt-first-failure-maximality.md` (857 l.),
`…-RH-conditional-bound.md` (1075 l.), `…-unconditional-verified-range.md` (788 l.),
`attack-round-2/lean-probe-report.md` (280 l.), `attack-round-2/unproved.md`;
`attack/proof-attempt-0.md` §1 and `attack/concept-cards/L15…`, `T1…`, `attack/source-ledger.md`
at the locators the round-2 legs claim to have amended; the committed `lean/` tree.

**Independently recomputed by this leg — every number below is mine, not a reading of an upstream
one.** Fresh sieve of Eratosthenes to `2·10⁸` and `3·10⁸` (`π(3·10⁸) = 16 252 325`), a segmented
sieve to `1.4·10⁹` for the gap constants, and `mpmath` at 50 decimal digits for every analytic
quantity. All code written from the **statements** in the round-2 attempts, never from their scripts
(`r2_*.py`, `verify-uvr-round2.py`, `probe_rh2.py` were **not** opened while writing the checks) —
this is the discipline `faults.md` §6 item 2 identified and both round-2 legs adopted; it is why the
off-by-one of R2-M1 is visible from here.

**Two sources fetched by this leg** (to adjudicate R2-B2/R2-B3, which cannot be settled from inside
the run): Axler arXiv:1409.1780v3 and the published *Integers* 16 (2016) #A22 with its corrigendum.
Byte-level provenance below.

**The Lean gates were re-run by this leg**, not read: `lake exe cache get` → 0, `lake build` → 0
(`Build completed successfully (2208 jobs)`, `Built Firoozbakht.Barrier`),
`lake env lean audit_exhaustive.lean` → 0, `declarations scanned: 63`,
`depending on sorryAx: [Firoozbakht.firoozbakht]`, and
`shasum -a 256 lean/Firoozbakht/Statement.lean = 6528868823c0637dd182c914e2ef43a7455f851335cafaba6cee934802e004c1`.
Every one matches `lean-probe-report.md` §1 and §8 exactly. **The kernel leg is clean** (§7).

---

## 2. BLOCKERS

### R2-B1 — **BLOCKER** — round 2 ships **two** incompatible repairs of the same BLOCKER, under two names, with two constants, off two different Axler rows, and neither leg cites the other

**Where.** `proof-attempt-unconditional-verified-range.md` §3.2/§3.5/§10 vs
`proof-attempt-first-failure-maximality.md` §7.2/§7.4/§11 item 6/§13.

Both legs were fed F2. Both repaired it. They did not repair it to the same thing:

| | `unconditional-verified-range` | `first-failure-maximality` |
|---|---|---|
| repaired lemma | **(A-high\*)** `v = ℓ² − ℓ − 1 − 1/ℓ` | **(A-high′)** `v = ℓ² − ℓ − 1 − 2.1/ℓ` |
| Axler row consumed | `(a,b,c,d) = (1,0,0,0)`, `x₀ = 1 772 201` | `(2.1,0,0,0)`, `x₀ = 6 690 557` |
| repaired theorem | **Theorem C(b\*)** | **Theorem C-b′** |
| uniform constant | `d ≥ 0.0043636` | `d ≥ 0.0017569` |
| headline | `p_m ≤ 0.99565·p_{n₀}` | `p_m ≤ 0.998244·p_{n₀}` |
| finite branch | `p_m < 1 772 201`, `g_m ≤ 132` | `p_m < 6 690 557`, `g_m ≤ 154` |
| source tier asserted | **L2_strong, NOT OPENED** | **L0, opened, both editions** |
| may the word "unconditional" appear near it? | *"must never"* (§3.5, §4.4) | *"the label is now **earned**"* (§11 item 7) |
| cites the sibling? | **no** | **no** |

**Both theorems are correct.** I verified both, solving Lemma W's hypothesis rather than evaluating
either leg's sufficient condition: the true maximal required separation is `0.00436288239` at
`ℓ = ℓ₁` for the `a = 1` bar (UVR's `0.0043636` covers it) and `0.00175606031` at `ℓ = 24.4295` for
the `a = 2.1` bar (FFM's majorant `0.00175687590` covers it, and `0.0017569` covers the majorant).
That is exactly the problem: **the corpus now carries three different constants for one theorem
name** — `0.99553` (round 1, from a lemma that does not support it), `0.99565` (UVR), `0.998244`
(FFM) — and two different finite branches (`132` below `1.77·10⁶` vs `154` below `6.69·10⁶`) that a
Lean leg is told to certify.

**Why this blocks.** This is round-1 F1's failure mode — *"a symbol or a phrase that means different
things in different artifacts, with no leg holding the cross-artifact view"* — reproduced one round
later, on the artifact whose whole purpose was to repair the *other* BLOCKER. F1's own reading of the
fault set (§6 item 1) predicted it: *"the predictable failure mode of a fan-out with no
reconciliation stage."* Round 2 added no reconciliation stage and the fan-out widened. A
`synthesize` or `write-paper` leg reading both round-2 attempts has **no rule** for choosing between
`0.99565` and `0.998244`, and quoting both is incoherent.

**Repair (not applied by this leg).** One of the two must be designated. On the mathematics FFM's
`0.998244` is strictly better and its Axler row is present in **both** editions; on the provenance
UVR is the only leg that quarantines the result correctly. The reconciliation is: keep **C-b′**
(`0.0017569`, the `a = 2.1` row), keep UVR's **quarantine language**, and retire C(b\*) and its
`1 772 201 / 132` pair to a remark — see R2-B3 for why that ordering is forced, not aesthetic.

---

### R2-B2 — **BLOCKER** — the two legs assign the *same* source contradictory tiers on the same day, and the ledger amendment one of them reports as **done** was never made

**Where.** FFM §7.1, §7.5, §11 items 8–9 vs UVR §3.2, §4.4, §6 item 1, §9 G3; and the committed
`attack/source-ledger.md`, `attack/concept-cards/T1-effective-pi-bounds.md`.

FFM §7.5: *"`attack/source-ledger.md`'s `axler2014newbounds` row **is amended in place**: tier
**L2_strong → L0** … `attack/concept-cards/T1-effective-pi-bounds.md` hazard 2 is amended
correspondingly."* §11 item 8 reports T1 hazard 2 **"Discharged"**; §11 item 9 reports ledger gap 3
**"Closed"**.

**Checked directly. It was not done.** The working tree is `git status`-clean and

- `attack/source-ledger.md:406` still reads `**axler2014newbounds** — tier **L2_strong**`;
- `attack/source-ledger.md:642` still reads *"Axler was not opened."*;
- `attack/concept-cards/T1-effective-pi-bounds.md:15` still reads
  `axler2014newbounds (**L2_strong, NOT OPENED**)`, and hazard 2 still reads *"The Axler corollaries
  were never opened in this run."*

So the run's ledger says **L2_strong / unopened**, one round-2 headline artifact says **L0 /
discharged / closed**, and the *other* round-2 artifact — written the same day off the same ledger —
says **L2_strong, NOT OPENED, MAJOR gap G3**, and instructs that everything Axler-based *"must never
be quoted inside a sentence containing the word 'unconditional'"*. Three sources of truth, no
arbitration.

This is not a bookkeeping nit. Round-1 **F3** was a MAJOR precisely for calling a discharge
"unconditional" on the strength of a source the run had not opened. Round 2 answers it by *opening*
the source (genuinely — see below) and then **failing to land the amendment**, while a sibling leg
keeps the old tier and builds a quarantine on top of it. Whichever way a downstream leg reads, it is
reading a claim contradicted somewhere else in its own round.

**What is nevertheless true, so the finding is not overstated.** FFM's fetch record is **genuine and
byte-reproducible**. I re-fetched all three documents independently and got the same MD5s:

| document | my MD5 | FFM §7.1 |
|---|---|---|
| arXiv:1409.1780v3 | `f4cde1df54cf3d6987c1ece2f7b0ebeb` | same |
| *Integers* 16 (2016) #A22 (15 pp.) | `29a92c5e7cacb5269e4d7be68ac939bf` | same |
| Corrigendum, 18 Jan 2018 | `4817ba687df1c16d163c94e29b55d1c4` | same |

and the corrigendum's text is verbatim what FFM quotes:
*"In Corollary 3.4 on page 8, replace "If x ≥ 5.43" by "If x ≥ 2 634 800 823"."*
FFM **Finding A** is confirmed by me from the PDFs: arXiv v3 numbers the upper bounds **Cor. 3.5**
(the `1.17/log x` clause is its last display) and the lower-bound table **Cor. 3.6**; the published
paper numbers them **Cor. 3.4 (page 8)** and **Cor. 3.5** respectively, so the corrigendum uses the
journal's numbering while the run's cards use the preprint's. The *mathematics* of the promotion is
sound. **The defect is that the promotion was reported as landed and did not land, and that the
sibling leg was never told.**

**Repair.** Land the amendment (in a round-2-owned path if rule 6 forbids editing round-1 paths —
see R2-m5), or strike §7.5/§11 items 8–9 and restate them as *proposed*. Either way both round-2
attempts must carry the **same** tier for `axler2014newbounds`.

---

### R2-B3 — **BLOCKER** — UVR's repaired lemma rests on an Axler column that exists **only in the preprint**; UVR did not open the source and cannot know, and its headline constants and its F13 pricing inherit the exposure

**Where.** UVR §3.2 (A-high\*), §3.5 Theorem C(b\*), §3.7 (the `1 772 201 / 132` vs `1.332·10⁹ / 288`
pricing), §10 verdict rows; against FFM §7.1 Finding B.

FFM Finding B claims the `(a,b,c,d) = (1,0,0,0)` row with `x₀ = 1 772 201` — the row (A-high\*) is
built on — is present in arXiv v3's Cor. 3.6 (14 columns) and **absent** from the published Cor. 3.5
(12 columns, also dropping `(2.65, 11.6, 0, 0) / 166 219 973`).

**I verified this claim independently from both PDFs.** arXiv v3's table:

```
x0  1245750347 909050897 768338551 547068751 374123969 235194097 166219973
x0  93811339 65951927 38168363 16590551 6690557 1772201 468049          (14 columns)
```

the published table (font-scrambled in extraction; decoded digit-for-digit):

```
x0  1245750347 909050897 768338551 547068751 374123969 235194097
x0  93811339 65951927 38168363 16590551 6690557 468049                 (12 columns)
```

**`1 772 201` is absent from the journal, and the `a = 1` value is absent from the journal's `a`
row.** FFM Finding B is **CONFIRMED**.

**Consequence, which FFM states for round 1's theorem but nobody states for UVR's.** UVR — which
declares *"no source PDF was opened by this leg"* and cites the row through card **T1** — has
rebuilt the run's repaired Theorem C(b) on a **preprint-only column**, and has made that column
load-bearing three further times: the headline `0.99565`, the finite constant `132`, and the whole
F13 counterfactual pricing (*"the constants are `1 772 201 / 132` under (A-high\*)"*, §3.7). A paper
citing the *Integers* version and quoting `x ≥ 1 772 201` would be citing something the journal does
not contain — which is the exact class of defect the run's citation gate exists to catch, and which
FFM raises against round 1 in the very same round without noticing it lands on its sibling too.

**Not overstated:** the preprint is a legitimate source, arXiv v3 is pinned by MD5, and the bound
itself is true — I verified `π(x) > x/(ℓ − 1 − 1/ℓ − 1/ℓ²)` at every prime `p_n < 10⁸` with
`p_n ≥ 1 772 201`: **0 failures**, and likewise for the `(2.1,…)/6 690 557` and `(0,…)/468 049` rows.
**The theorem is not wrong. The citation is edition-fragile and is not flagged as such anywhere in
the artifact that depends on it.**

**Repair.** Either rebuild C(b\*) on the `(2.1,0,0,0) / 6 690 557` column (present in both editions —
which is precisely what FFM did, and is why R2-B1's reconciliation is forced in FFM's direction), or
carry an explicit *"arXiv v3 only; not in Integers 16 A22"* flag on (A-high\*), on `132`, and on
every quotation of `0.99565`.

---

## 3. MAJOR

### R2-M1 — **MAJOR** — FFM §4 "settles the three-fractions dispute" using denominators that are themselves off by one; F5's adjudication is inverted, and round 2 has now blessed it

**Where.** FFM §4 table and §9 item 11; inherited from `faults.md` **F5** and card **L15**.

FFM §4 presents its table as the resolution: *"This reproduces `faults.md` F5 exactly and settles the
three-fractions dispute recorded there: card **L15**'s `121 238 / 216 805` is the `n ≥ 10` convention
and is correct; … `proof-attempt-0.md` §9 item 18's `121 238 / 216 806` matches neither."*

**Recomputed by this leg from the statement** (own sieve, `π(3·10⁶) = 216 816`, `π(10⁷) = 664 579`,
`π(10⁸) = 5 761 455`; a *step* is an `n` with `T_n` and `T_{n+1}` both defined, i.e. `p_{n+1} < N`):

| range | steps, all `n` | steps, `n ≥ 10` | dec (all) | dec (`n ≥ 10`) |
|---|---:|---:|---:|---:|
| `3·10⁶` | **216 815** | **216 806** | 121 239 | 121 238 |
| `10⁷` | **664 578** | **664 569** | 374 486 | 374 485 |
| `10⁸` | **5 761 454** | **5 761 445** | 3 280 064 | 3 280 063 |

FFM reports `216 814 / 216 805`, `664 577 / 664 568`, `5 761 453 / 5 761 444` — **every denominator
exactly one less than mine, at every range, under both conventions.** Every numerator agrees to the
digit. The dropped step is the last one (`n = π − 1`), which is an increase — consistent with a
`T`-array truncated to the *gap*-array length (`M = π − 1`) before differencing, which is an
implementation artefact, not a convention.

**Two consequences, both in the unsafe direction:**

1. **`proof-attempt-0.md` §9 item 18's `121 238 / 216 806` is the correct `n ≥ 10` count.** Round 1
   called it an off-by-one; round 2 re-affirms that verdict in bold. Both are wrong.
2. **`notebook-1` §2's `374 485 / 664 569` at `10⁷` is likewise correct**, not "denominator off by
   one" as `faults.md` F5 states.

**Corroboration from inside round 2 itself:** `proof-attempt-RH-conditional-bound.md` §10 states its
own sieve as *"216 816 primes, largest `2 999 999`, **216 815 consecutive pairs**"* — my number, not
its sibling's.

**Why MAJOR.** `55.92 %` remains the most-quoted statistic in the corpus and the stated reason `T` is
not monotone. Round 1 rated the three-fractions collision MAJOR; round 2 declares it settled, and
settles it on the wrong side while telling a downstream leg the figure *"must never be quoted without
both its bound and its convention"*. The convention it publishes is an artefact.

### R2-M2 — **MAJOR** — FFM Theorem C-a′ is headed *"no source outside `dusart2010estimates`, L0"* and quoted as *"unconditionally"* in §13, while its own proof consumes card **L6** (unopened, L2_weak) and this leg's `10⁸` gap sieve

**Where.** FFM §7.4 Theorem C-a′ header and small branch; §2 verdict row; §13 defensible sentence;
against FFM's own §10 gap 7.

The small branch reads: *"If `p_m < 10⁸` then `g_m ≤ 220` … and `220 < 1919 < g_{n₀}`."* The
`1919` is `T_{n₀} > λ² − 1.1λ` with `λ > log 2⁶⁴` — i.e. **card L6**, which FFM §10 gap 7 correctly
records as *"`oliveira2014goldbach` remains unopened, so `p_{n₀} > 2⁶⁴` … is still mediated through
Kourbatov"*. The branch also consumes this leg's own sieve fact `max{g_m : p_m < 10⁸} = 220`
(reproduced by me: `220` at `p = 47 326 693`). Neither is Dusart.

The improvement from round 1's `0.93961` to `0.94970` comes **entirely** from raising the small-branch
cutoff from `60 184` to `10⁸` — FFM says so — so the L6 dependence is not incidental to the header, it
is the *source* of the headline number. §13 then instructs downstream to quote:
*"…below `0.94970·p_{n₀}` **unconditionally**…"*.

This is round-1 **F3** reintroduced with a sharper label. Round 1's C(a) had the same L6 dependence
and was passed clean, so this is a regression in the *labelling*, not in the mathematics: the theorem
is true, the provenance sentence is not. Note the contrast with UVR §4.4, which builds an explicit
table of *what may be called unconditional* and gets this right.

**Repair.** Head C-a′ *"Dusart-only analytics; the finite branch consumes card L6 (L2_weak, unopened)
and an in-run gap sieve to `10⁸`"*, and strike "unconditionally" from §13's first defensible sentence
or qualify it.

### R2-M3 — **MAJOR** — FFM calls P6′-min *"the weakest of the three"* and *"the easier obligation"*, contradicting its own Proposition 4; `gov` and `min` are formally **incomparable**

**Where.** FFM §3.3 point 2, §5 closing paragraph, §5.2 verdict row; against FFM §3.2 Proposition 4.

Proposition 4 proves **both** `P6′-gov ⇏ P6′-min` (counter-model `g = (2,4,6,3)`, `T = (0,10,1,5)`)
and `P6′-min ⇏ P6′-gov` (`T = (0,1,10,5)`). I checked both counter-models by hand: `r(4) = 3`,
`µ(4) = 2`, and each instance goes through. So in the abstract setting the document itself fixes,
**`gov` and `min` are incomparable**; the only order relations proved are `pair ⟹ gov`,
`pair ⟹ rec`, and `gov ∧ rec ⟹ min`.

Yet §3.3 point 2 states *"**P6′-min is the right obligation** … It is the weakest of the three
(Propositions 2–4)"*, §5 states *"P6′-gov is the harder obligation … P6′-min is the easier
obligation"*, and §5.2 instructs card **L15** that *"**P6′-min** is the obligation"* while listing
only `P6′-rec` alongside it. **P6′-gov is dropped from the obligation list** on the strength of an
ordering the document has just disproved.

The ordering that *does* hold is **empirical**: `T_{µ(n)} ≤ T_{r(n)}` at every index in the swept
range (FFM: 0 exceptions in `50 847 533` below `10⁹`; me: 0 exceptions in `11 078 936` below `2·10⁸`),
which *on that range* makes gov ⟹ min. §3.2 states this honestly (*"empirically available on the
swept range — which is the honest statement, and is not a proof"*) and then §3.3/§5/§5.2 spend it as
if it were the proof. Since Theorem 2 shows **either** predicate at `n₀` suffices, dropping `gov` is
also strictly lossy.

**Repair.** Replace "weakest / easier" with "incomparable to P6′-gov (Prop. 4), implied by P6′-pair,
and empirically dominated by it on `p < 10⁹`"; keep **both** `gov` and `min` on L15's obligation
list, alongside `rec`.

---

## 4. MINOR

### R2-m1 — **MINOR** — FFM calls the gap `248` at `p = 191 912 783` *"the 27th maximal prime gap"*; it is the **28th**, under the same enumeration that makes `15 683` the 12th

FFM §3, witness W2 table. My own record enumeration (running maximum of `g`, `p < 2·10⁸`) yields
**28** record indices, with `191 912 783` last and `15 683` twelfth — so the two labels in the same
document are inconsistent by one. FFM's §9 item 2 counts (21 / 22 / 25 at `3·10⁶` / `10⁷` / `10⁸`) I
reproduce exactly, so the census is right and only the ordinal is wrong.

### R2-m2 — **MINOR** — the P6′-pair census counts **indices**, not **pairs**, and the "complete exception census" is therefore false as literally stated

FFM §3 (*"**17** admissible pairs violate P6′-pair"*) and §9 item 3 (*"**17** in `50 847 532`
admissible pairs"*). I reproduce the **17 violating indices `n`** exactly — same two clusters, same
members, same worst margin `−2.861060·10⁻²` at `n = 1847`:

```
1836 1837 1840 1844 1845 1846 1847
10655562 10655563 10655564 10655566 10655587 10655589 10655590 10655592 10655593 10655594
```

but the number of violating **`(m,n)` pairs** is **20** below `3·10⁸`: `n = 1847`, `n = 10 655 564`
and `n = 10 655 590` each carry **two** violating `m`. The denominator is an index count too — the
true admissible-pair count is `Σ_n r(n−1) ≈ 10¹⁵`, not `5.08·10⁷` — so *"17 exceptions in 50 million
pairs"* misstates the coverage by ~7 orders of magnitude if read as a density. (For **P6′-gov** the
word "pairs" is fine: exactly one pair per `n`.) Same species as round-1 **F7**, in the same
verification table.

### R2-m3 — **MINOR** — Theorem C-b′'s certified constant clears its own majorant by `2.4·10⁻⁸`, with no interval arithmetic anywhere

`0.0017569` vs the majorant `0.00175687590387` (my value; FFM's `0.0017568759` to the digit). The
margin is `2.4·10⁻⁸`, ≈`1.4·10⁻⁵` in relative terms. At 50 dps this is safe and I confirm it; but
FFM §9 carries no counterpart to UVR's **G6** (*"the checks are 50-digit, not interval arithmetic"*),
and FFM §12 hands `M-7`/`M-8` to a Lean leg where a `norm_num` on the quadratic without directed
rounding has far less headroom than the corpus's other constants. Record the margin next to the
constant.

### R2-m4 — **MINOR** — the lean-probe's §4 slack table drops the constants of the two bounds it scores

`lean-probe-report.md` §4: the BHP row prints the available slack as `p^{−0.475}`, i.e. with the
implicit constant `C = 1`, while the cited bound is `g_n ≪ p^{0.525}` with an **unspecified**
constant — so the published crossover *"BHP's slack overtakes what is needed from `n = 245` on"* is a
property of `C = 1`, not of Baker–Harman–Pintz. The CMS row prints `log p/√p` and drops the `22/25`
the same row names. The conclusion (both insufficient for all large `n`) is unaffected — it is
driven by the exponent, per this round's own Theorem B — but §7 of that report presents the
crossovers as the *repair* of an asserted claim, and a crossover index computed with a fabricated
constant is not a measurement.

### R2-m5 — **MINOR** — write-perimeter: an amendment to round-1 paths is announced (rule 6 forbids it), and the formal leg does modify round-1 `lean/` files

The briefing's rule 6: *"Round K writes ONLY under `attack-round-K/`."* FFM §7.5 announces in-place
edits to `attack/source-ledger.md` and `attack/concept-cards/T1-…`. No collision actually occurred
(the edits were never made — R2-B2), so this is recorded as a process conflict to resolve rather than
a violation committed: the bounded-source-refresh clause and rule 6 are in tension and one of them
must give. Separately, the `lean-probe` leg committed changes to `lean/Firoozbakht.lean`,
`lean/audit.lean` and `lean/STATUS.md` — round-1 `lean-skeleton` artifacts — alongside the new
`lean/Firoozbakht/Barrier.lean`. Defensible for a formal leg, and the **fidelity anchor**
`Statement.lean` is byte-frozen (I verified the SHA-256), but "the skeleton was never re-opened" is
true only of that one file.

### R2-m6 — **MINOR** — the P6′-gov decay exponent `p^{−0.83}` is quoted unchanged although round 2's own new data point moves it to ≈`1.0`, and it is then extrapolated nine decades

FFM §5 and §5.1. From FFM's own four margins (which I reproduce to every digit:
`1.046415·10⁻²`, `6.060476·10⁻³`, `1.111812·10⁻³`, `1.120382·10⁻⁴`) the **local** exponent per decade
is `0.4536`, `0.7365`, `0.9967` — monotonically rising, not a constant `0.83`. §5.1 then
extrapolates `0.83` to `2⁶⁴` to get `4.457·10⁻¹³` (extrapolating the `10⁹` point at `0.83` myself
gives `3.4·10⁻¹³`, so the quoted figure is consistent with that exponent). At the **last measured**
exponent the extrapolated margin is `6.1·10⁻¹⁵` — smaller by a factor `≈55`. The direction is
**safe** (the float64 noise-floor alarm FFM
endorses becomes stronger, not weaker) and nothing downstream moves, but a nine-decade extrapolation
of a visibly drifting exponent should carry that fact.

### R2-m7 — **MINOR** — FFM's per-decade P6′-min table does not reproduce in its first row

FFM §5: *"`2.42` (`10³`), `3.05` (`10⁴`), `0.4845` (`10⁵`), `1.68` (`10⁶`), `3.81` (`10⁷`), `1.70`
(`10⁸`), `3.89` (`10⁹`)"*. Mine, over the same decades and excluding the trivial self-pairs:
`3.04863`, `0.484528`, `1.67502`, `3.81457`, `1.69779` for `10⁴ … 10⁸` — **exact agreement** — but
the `10³` entry is `1.35373` (at `p = 5`), not `2.42`. The discrepancy is confined to indices below
`n = 10`, where every criterion in the corpus is out of range, and the section's claim ("no trend",
global minimum `0.4845277` at `n = 1879`, never approached again) is unaffected and confirmed.

---

## 5. Round-1 BLOCKER disposition, item by item, as the brief requires

| round-1 item | round-2 disposition | this leg's verdict |
|---|---|---|
| **F1** — three inequivalent `m(n)`; two sibling legs publish opposite trends | FFM §1.2 names P6′-pair / P6′-gov / P6′-min **in symbols**, adds P6′-rec, assigns each published measurement to its predicate (§5), reconciles both headlines, refutes P6′-pair | **FIXED, not re-worded.** All three definitions are correct and the assignment of measurements is correct — I reproduced `notebook-0`'s `+0.4845277 @ n=1879, µ=1831` and `notebook-2`'s four gov-margins from my own code path. New defects R2-M3, R2-m2 sit *inside* the repair without reopening it. |
| **F2(a)** — `(A-high)` too weak by `≈ℓ²`; stated justification does not produce the stated lemma | UVR §3.2 restates it as `v(1+v/x)`, `v = ℓ²−ℓ−1−1/ℓ`, proved from Lemma H with **no** weakening | **FIXED.** Verified: the four bars at `ℓ₁` are `191.570323`, `191.571994`, `191.573800`, `196.181291`; printed error term is `223.71×` the tight one. |
| **F2(b)** — theorem false by a factor 38 under the printed lemma | UVR §3.6 confirms `0.16933981 / 0.0043628824 = 38.8137` | **FIXED and independently reproduced** (my values: `0.169339813` and `0.00436288239`, both maximised at `ℓ₁`). |
| **F2(c)** — quoted constant below the document's own criterion | UVR §3.1/§3.6 identifies the criterion as the *additive* bar (row 2) and dissolves the discrepancy | **FIXED.** My values: PA-0's displayed criterion maxes at `0.00448872246`, above `0.004479` — F2(c) confirmed and correctly explained; the repaired criterion maxes at `0.00436356770`, below it. |
| **F2 — re-derive, do not re-sweep** | UVR Prop. R1: `E` decreasing (`q(ℓ₁) = 135.98903 > 0`), majorant `φ`, `φ` decreasing (`4/ℓ₁ − 1/ℓ₁² = 0.27318386 < 0.38140756 = 2K`) | **FIXED.** I re-derived all three steps symbolically and reproduced all three certificates. It is a proof, not a sweep. |
| **F2 — provenance** | UVR §10 declares it **NOT fixed and does not claim it**; FFM declares it fixed | **SPLIT — this is R2-B2/R2-B3.** |
| **F3** (MAJOR) | FFM opens Axler (genuinely — MD5s reproduce) but the ledger amendment never landed; and C-a′ acquires a *new* false "unconditional" label | **PARTIALLY FIXED, with a regression** — R2-B2, R2-M2. |
| **F4** (MAJOR) | RH §0/§5.2/§5.3/§5.4 | **FIXED.** `A = {n : B_n < T_n} = {1,2,3}` and `S = A ∩ [3,∞) = {3}` both reproduced by me at 50 dps, including the two bold rows (`0.86262717 < 2`, `1.67451003 < 2.19615242`); the reconciliation with `notebook-1` via `C_n` reproduces (`p*(C) = 3, 5, 2, 62 869, 1 772 591` — every row). |
| **F5** (MAJOR) | FFM §4 declares it settled | **NOT FIXED — inverted.** R2-M1. |
| **F6, F8, F9, F11, F13** | RH §5.4 (F6 read with the corrected endpoint), §5.5 Rem. 3 (F8: `8.6744·10¹⁶`, `0.4702 %`, `1.955·10¹⁵` — mine: `8.6744074·10¹⁶`, `0.470241 %`, `1.95539·10¹⁵`), §9 (F9: both Dusart brackets displayed and the conclusion scoped), UVR §4.7 (F11: the Kourbatov-threshold mitigation struck), UVR §3.7 (F13: `288` at `p = 1 294 268 491` — reproduced by my own segmented sieve to `1.4·10⁹`) | **FIXED**, all five. |
| **F7, F10, F12, F14** | FFM §5 (F7 row corrected), §5.1 (F10 acknowledged) | **FIXED / acknowledged**; F12 and F14 are not revisited by any round-2 leg and are not re-raised here. |

---

## 6. What was attacked and came back clean

A red-team report that lists only hits is not calibrated. Every item below was independently
recomputed or re-derived by this leg and **survives**. Round-1 §5's eighteen clean items are **not**
re-litigated.

| # | Claim attacked | Verdict |
|---|---|---|
| 1 | **FFM Theorem 1, witness W1** | **CORRECT.** `p_1823 = 15 641`, `p_1831 = 15 683` (record, `g = 44`), `p_1847 = 15 823`; `T_m − T_n = 0.0286106049` at 60 dps. `m < j < n` and the whole gap interval lies between — admissible under the most natural reading of L15's prose, which I checked against the card. |
| 2 | **FFM Theorem 1, witness W2** | **CORRECT.** `p_10655449 = 191 912 639`, `p_10655462 = 191 912 783` (record, `g = 248`), `p_10655590 = 191 915 033`; `T_m − T_n = 3.5792097·10⁻⁵`. |
| 3 | **FFM Prop. 2 / Prop. 3 / Prop. 4** | **CORRECT.** Re-derived line by line, including both four-element counter-models. Prop. 4 is the document's best structural catch and it does correct round-1 F1's chain. |
| 4 | **FFM Theorem 2** (both branches) | **CORRECT.** Both chains re-derived; each uses the predicate only at `n₀`, as claimed. |
| 5 | **FFM Theorem C-a′** | **CORRECT.** Exact requirement `0.0514934573` at `ℓ_D`; cell-majorant max `0.0515990267` (first cell); tail `0.0500275`; `e^{−0.0516} = 0.9497086743`. Majorant argument is a genuine majorant, not a sample. |
| 6 | **FFM Theorem C-b′ / (A-high′)** | **CORRECT.** Exact requirement `0.00175606031` at `ℓ = 24.4295`; majorant max `0.00175687590` on the cell at `ℓ = 24.4062`; tail `0.000283806`; `e^{−0.0017569} = 0.9982446424`. Derivation `d(2ℓ−1)+d² ≥ 0.17 − 2.1/ℓ + v²/p_m` re-derived symbolically. |
| 7 | **UVR Lemma H, (A-high\*), (★), Prop. R1, Cor. R1.1, Thm C(b\*)** | **CORRECT** throughout — see §5. `ψ(ℓ₁) = 0.347895529 < 1`, `ℓ₁E(ℓ₁) = 0.297880432`, `0.17/(2ℓ₁−1) = 0.006120509`. |
| 8 | **UVR §3.8 — C(a) unaffected** | **CORRECT.** True max required `d = 0.0620798105` at `ℓ = log 60 184 = 11.005162`; `ε(ℓ₀) = 0.20144665`. PA-0's `0.0623` covers it. The structural reason given (no substitution inside (H-hi)'s second factor) is the right reason. |
| 9 | **UVR V5 counterfactual** | **CORRECT.** The printed lemma's required `d` falls to `0.004479` at `ℓ = 21.0099647`, `p_m = 1 332 022 974`. |
| 10 | **UVR Theorem 2 / Lemmas 1–4 / decision procedure** | **CORRECT.** `G₀ = 72` at `p = 31 397`; `π(60 184) = 6 076`; `B(60 184) = 109.007909 > 72`; min slack `T − B` on `[60 184, 2·10⁶]` is `+0.079891473` at `p = 155 893`; Dusart eq. (6.6) upper holds at every prime in that window. |
| 11 | **UVR §4.7 / V9 / V9b** | **CORRECT** to every digit: `S(1918) = 1.82086847·10¹⁹ ≤ 2⁶⁴ = 1.84467441·10¹⁹ < S(1920) = 1.86290946·10¹⁹`; `S_K(1922) = 1.83619538·10¹⁹`, `S_K(1924) = 1.87853319·10¹⁹`. |
| 12 | **UVR Prop. 3 / Prop. 4 window** | **CORRECT.** `h(396 738) = −234 735.02`, `h(777 600) = −0.51996212 < 0 < 0.17863233 = h(777 601)`, root `777 600.744298`. |
| 13 | **FFM Finding C** (pre-corrigendum range false) | **CORRECT**, under the range the statement carries (`x ≥ 5.43`): exactly **4 987 066** counterexamples below `10⁸`, smallest at `p = 59 753` (`n = 6041`), all below `2 634 800 823`. (Without the `x ≥ 5.43` restriction I get 4 987 069 — `p = 2, 3, 5`, where the bound's denominator is negative. The restriction is part of the statement; noting it only so the number is reproducible.) |
| 14 | **FFM Finding D** (three Axler lower rows) | **CORRECT.** `0` failures each at every prime `< 10⁸` in range, for `(1,0,0,0)/1 772 201`, `(2.1,0,0,0)/6 690 557`, `(0,0,0,0)/468 049`. Also `0` failures for (D-low) `p ≥ 60 184`, (D-high) `p ≥ 5393`, (A-high′) `p ≥ 6 690 557`, (A-high\*) `p ≥ 1 772 201`. |
| 15 | **Small-branch gap constants** | **CORRECT.** `112` @ `370 261` (`<468 049`), `132` @ `1 357 201` (`<1 772 201`), `154` @ `4 652 353` (`<6 690 557`), `220` @ `47 326 693` (`<10⁸`), `288` @ `1 294 268 491` (`<1.332·10⁹`, my own segmented sieve to `1.4·10⁹`). |
| 16 | **`S`-breaches, Lemma M′(ii), the `2 875 681` anchor** | **CORRECT.** `S`-breaches below `2·10⁸` are exactly `{1,2,3,4,6,9}`; `max{g_j : j ≤ 9} = 6 < 6.8013854 = S(29)`; largest `n` with `T_n ≤ L²−L−1.17` below `3·10⁶` is `n = 208 494`, `p = 2 875 681`. |
| 17 | **RH Theorems A°, A, B, C, D, E** | **CORRECT.** Lemma A.1 (`x* = 5.1652892562`, `h(x*) = 0.4068623816594768`); Fact 1's exception set `{n : T_n ≥ L_n²} = {1,2,3,4,5,6,7,10}` verified to `3·10⁸` — no further exception; the eight-row table to every digit; `2/e = 0.7357588823428846` at `x = e²`; `min_{n≥4} B_n/T_n = 1.032957111859` at `n = 4` and **29 770 of 216 812** falling steps — both exact; `(L²−L−1)/(√p L) = 1.0090619·10⁻⁸` at `2⁶⁴` (RH's `1.00906·10⁻⁸` — correct). Theorem B's proof is valid (`E(x)/L² = C e^{θu}u^{A−2} → ∞`). Theorem E's Claims 1–4 re-derived; the `J_k ≥ 0` restriction is load-bearing and correctly flagged. |
| 18 | **The lean-probe leg, end to end** | **CLEAN, and the only leg this skeptic could verify by re-execution.** `lake exe cache get` 0, `lake build` 0 (2208 jobs, `Built Firoozbakht.Barrier`), one warning at `Statement.lean:185`, `audit_exhaustive` 0, `declarations scanned: 63`, `depending on sorryAx: [Firoozbakht.firoozbakht]`, exactly one live `sorry` token in the sources (`Statement.lean:186`), no `axiom` / `native_decide` / `unsafe` / `@[implemented_by]` outside docstrings, and `Statement.lean` byte-frozen at the reported SHA-256. `bertrand_ceiling_above_threshold` is the right shape and its mechanism (`p_n < 2ⁿ` for `n ≥ 2`) is correct. The verdict **UNPROVABLE_IN_BUDGET** is honest and correctly refuses to be read as PROVED. |
| 19 | **Does any round-2 artifact assume `F`, or launder a scale-limited computation as general?** | **No.** Every one of the four states `F` OPEN at the top, none uses `F` as a hypothesis, and each restates its scale disclaimer *after* its verification table (FFM §9, UVR §5, RH §10, probe §6). FFM's §8 heuristic is explicitly quarantined and explicitly refused as a licence. This is the discipline round 1 hunted and could not break, and I could not break it either. |
| 20 | **Do the two "0 exceptions" predicates survive my own range?** | **Yes.** P6′-gov: 0 exceptions in `11 078 936` indices below `2·10⁸`. P6′-min: 0 exceptions, global minimum `+0.484528` at `n = 1879`. P6′-rec: 0 decreasing steps in **27** record steps below `2·10⁸`. `T_{µ(n)} ≤ T_{r(n)}`: 0 exceptions. FFM's `10⁹` figures are one decade beyond my sieve and are **not** independently confirmed here; nothing in this report depends on that decade. |

---

## 7. Reading of the fault set

Round 2 did the mathematics it was asked to do. **Both round-1 BLOCKERs are mathematically closed**,
by legs that re-derived rather than re-asserted, wrote their checks from statements rather than from
derivations, and — in FFM's case — went and fetched the source that round 1 flagged. Every constant I
recomputed from scratch — some forty of them, listed in §6 — agrees to every digit quoted, save the
exceptions recorded in §3–§4, and the two new theorems
(Theorem 1's refutation of P6′-pair, Proposition 4's separation of gov from min) are genuine
structural progress that no earlier leg had.

**Every one of the three BLOCKERs is a seam, not a step.** Not one of them is an error inside a
proof. They are: two legs repairing the same fault differently (R2-B1); two legs assigning the same
source opposite tiers while the ledger records a third answer and the reported amendment never landed
(R2-B2); and one leg's repair resting on a citation the *other* leg had already discovered to be
edition-only (R2-B3). Round-1 §6 named this failure mode and predicted its recurrence: *"a fan-out
with no reconciliation stage … nobody owned the seams."* Round 2 doubled the fan-out — two proof
attempts now both touching Theorem C(b) — and still has no reconciliation stage. **The loop is not
converging on this axis; it is widening.**

The MAJORs point the same way. R2-M1 is a wrong number *inherited from the previous round's
skeptic* and re-published as settled — a reminder that the skeptic leg is not exempt from the
discipline it enforces, and that "reproduces `faults.md` exactly" is a confirmation of agreement, not
of correctness. R2-M2 is round-1 F3's exact pattern reappearing in the one branch that had been
clean.

The structural recommendation, stated once: **round 3 must not be another fan-out.** What is missing
is a reconciliation leg with a single job — pick one repaired Theorem C(b), pick one Axler tier, land
one ledger amendment, recount the `55.92 %` denominators from the statement, and make the four
artifacts cite each other. None of that is research; all of it is what a `write-paper` leg will
otherwise have to guess at.

**Neither BLOCKER, and none of the MAJORs, touches `F`. `F` remains OPEN**, and nothing in this
red-team moves it in either direction.

---

*Artifact of leg `skeptic`, round 2, molecule `task-20260726-7211`, parent `reattack-20260726-57d1`.
Verification scripts: `attack-round-2/skeptic-round2-checks/`. The Lean gates were re-executed, not
read. **The conjecture remains OPEN.***
