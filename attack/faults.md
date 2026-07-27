# faults.md — red-team of the round-3 reconciliation, **the corpus's single current fault list**

**Molecule:** `task-20260727-5096` (leg `skeptic`, round 3) · **Run:** `germ-20260725-791a7c45`
**Date:** 2026-07-27 · **Audited leg:** `task-20260727-264e` (`reconcile`), `attack/reconciliation.md`
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.
**Status of `F` in this document: OPEN.** Nothing below proves or refutes it, and nothing in the
round-3 reconciliation leg moves it. This document attacks *artifacts*, not the conjecture.

> **This file supersedes both prior fault lists and is the only current one.**
> Round 1's list is preserved verbatim at **`attack/faults-round-1.md`** (renamed, not rewritten,
> not deleted). Round 2's list stays at
> **`attack/re-attack/attack-round-2/faults.md`** as the record of what round 3 was asked to close;
> it now carries a supersession banner pointing here. Every finding of both is dispositioned below,
> **by re-checking the tree, not by reading either report.**

---

## 0. Verdict, stated first

**The BLOCKER set is non-empty. Round 3 is NOT clean, and the evidence gate stays BLOCKED.**

| Severity | Count | Findings |
|---|---|---|
| **BLOCKER** | **2** | S3-B1, S3-B2 |
| **MAJOR** | **2** | S3-M1, S3-M2 |
| **MINOR** | **5** | S3-m1 … S3-m5 |

### Disposition of every round-2 finding, one line each — the answer the brief demands

| round-2 finding | verdict | how I verified it **in the tree** |
|---|---|---|
| **R2-B1** — two incompatible repairs of one theorem | **CLOSED** | FFM §7.4 carries the `✅ DESIGNATED` notice for **C-b′**; UVR §3.5 carries `⛔ RETIRED` on C(b\*) with the quarantine rescoped, §3.7 re-priced to `6 690 557 / 154`, §9 `G3 → G3′`, §10 both verdict rows amended; `source-ledger.md`'s Axler row makes the edition rule load-bearing on the designation; `claims-ledger.md` R8, `evidence-verdict.md`, `synthesis.md` and `paper/paper.tex` Rem. `rem:retired` all say the same thing. **No concept card carries a Theorem C constant at all** (grep for `0.99553`/`0.998244`/`0.94970` over `attack/concept-cards/`: zero hits), so there is no stale card site. I re-derived the designated theorem's constants myself — see §1 |
| **R2-B2** limb 1 — *"the ledger amendment was never made"* | **CLOSED — the round-2 skeptic was wrong, the reconciliation is right** | `attack/source-ledger.md` line 426 reads **`tier L0`** with the three-document fetch table, the edition-numbering ⚠ and the preprint-only-row rule; §6 gap 3 reads `~~Axler was not opened.~~ CLOSED 2026-07-26`. `git log` puts the promotion in `61689d0` (07-26 19:22), merged at `4526b27` (19:26); the round-2 `faults.md` was committed at 20:46 **on a branch cut before that merge**, which is why its `:406`/`:642` line numbers resolve only in the pre-merge tree. Verified by `git log --format` on the file, not from any report |
| **R2-B2** limb 2 — the tier never propagated to the sibling | **STILL OPEN — see S3-B1** | It propagated into UVR (§3.2, §4.4, §6 item 1, §9, §10) and nowhere else. Five concept cards and one round-2 proof attempt still assert `L2_strong` / *"never opened"* / *"Citation-gate Priority 1"* |
| **R2-B3** — repair resting on a preprint-only Axler row | **CLOSED** | Discharged the only way it can be — by retirement (UVR §3.5) — and the surviving `1 772 201` sites all carry the edition flag (`paper.tex` l. 928/1399 + `haz:axler`, `T1` hazard 2, ledger). Residue in round-1 `proof-attempt-0.md` is flagged at its §11 (S3-m3). I re-verified the row's *mathematics* independently: `π(x) > x/(ℓ−1−1/ℓ−a/ℓ²)` has **0 failures** at every prime in range below `10⁸` for `a = 1` and for `a = 2.1` |
| **R2-M1** — the `55.92 %` denominators | **CLOSED** | FFM §4's table, its convention paragraph and its **reversed** adjudication are in the tree; §9 item 11 matches; cards `L15`, `D5`, `INDEX` corrected; sweep size `50 847 503 → 50 847 533` in card `L15` and FFM §9 items 5/7. **I recounted from the statement with my own script** (`attack/skeptic-round3-checks/s3_recount.py`) and I agree with the reconciliation and disagree with both prior skeptics — §1 |
| **R2-M2** — C-a′'s *"unconditional / Dusart only"* label | **STILL OPEN (partially applied) — see S3-M1** | §7.4's header and §13's defensible sentence are corrected. **Two of the three sites R2-M2 names are untouched:** FFM §2's verdict row (l. 173) still reads *"**PROVED** unconditionally, Dusart only"*, and §7.4's own "Reading of Theorem C" (l. 751) still reads *"unconditionally, on Dusart alone"* — neither names card `L6` |
| **R2-M3** — *"the weakest of the three"* | **CLOSED at the three named sites**, with a wording residue elsewhere (S3-m1) | FFM §3.3 point 2 (l. 336), §5 closing (l. 421–428) and §5.2's instruction (l. 470) all now say **incomparable (Prop. 4)** and keep `gov`; card `L15`'s "Declared gap" (l. 118–123) lists **P6′-min *and* P6′-gov**, with `rec` beside them |
| **R2-m1** — `248` is the 27th or the 28th maximal gap | **CLOSED** | FFM §3 W2 table (l. 215) reads **28th**. **Independently recomputed here**: running-maximum enumeration to `2·10⁸` gives exactly 28 records, `15 683` twelfth (`g = 44`), `191 912 783` twenty-eighth (`g = 248`), and 25 records below `10⁸` — consistent with FFM §9 item 2's census |
| **R2-m2** — census counts indices, not pairs | **CLOSED** (one wording residue, S3-m2) | FFM §3's census paragraph now says *indices*, records **20** violating pairs below `3·10⁸`, states the true admissible-pair count `≈ 10¹⁵` and forbids reading any ratio as a density; §9 items 3/5/7 relabelled |
| **R2-m3** — C-b′'s constant clears its majorant by `2.4·10⁻⁸` | **CLOSED as a recorded margin** (not repaired — correctly, that needs interval arithmetic) | The ⚠ block is in FFM §7.4. **I reproduced the margin from the statement**: majorant max `0.00175687590387`, so `0.0017569 − majorant = 2.41·10⁻⁸` |
| **R2-m4** — the lean-probe slack table drops both constants | **CLOSED** | `lean-probe-report.md` l. 201–203 annotates both columns as `C = 1` illustrations, not measurements, and names the exponent as what carries the conclusion |
| **R2-m5** — write-perimeter tension | **CLOSED for this loop, OPEN as a process question** | The reconciliation's brief authorised in-place edits and §0 declares the perimeter; the standing rule-6 exemption is correctly deferred to the next loop's brief |
| **R2-m6** — `p^{−0.83}` extrapolated nine decades | **CLOSED** | FFM §5.1 l. 439–441 carries the three local exponents, the corrected `≈ 6.1·10⁻¹⁵` and the "direction is safe" note. I re-derived the local exponents from the four published margins: `0.4538`, `0.7364`, `0.9967` — agrees |
| **R2-m7** — the `10³` per-decade entry | **CLOSED** | FFM §5 l. 406–408 reads `1.354`, attributed, with the out-of-range note |

**Nothing above is softened, and nothing was cleared to be helpful.** Two BLOCKERs means the loop
has not reached its fixpoint; the honest exit is **BLOCKED**, not convergence. Note the shape of
what survives: **the reconciliation's five decisions are right, and its two failures are both of the
same species as the fault it was created to fix** — a statement about the state of the tree that the
tree does not support.

---

## 1. What I recomputed myself, before reading anyone's verdict

Every number in this section is mine. Scripts: `attack/skeptic-round3-checks/s3_recount.py` and
`…/s3_constants.py`, both written from the **statements** in FFM §7.4 and in the reconciliation's
§4 convention paragraph; no upstream script (`reconcile_recount.py`, `r2_*.py`, `chk_*.py`,
`verify_syn*.py`) was opened before they were written and run.

**The recount, at three ranges and three cuts** (own sieve; float64 pass with every relative margin
inside `10⁻⁹` re-adjudicated at 60 dps — **0 reclassifications**, so the count is not float-fragile):

| `N` | `π(N)` | all `n` | `n ≥ 10` | `n ≥ 11` |
|---|---:|---|---|---|
| `3·10⁶` | 216 816 | `121 239 / 216 815` = 55.918179 % | **`121 238 / 216 806` = 55.920039 %** | `121 237 / 216 805` = 55.919836 % |
| `10⁷` | 664 579 | `374 486 / 664 578` | `374 485 / 664 569` = 56.350055 % | `374 484 / 664 568` |
| `10⁸` | 5 761 455 | `3 280 064 / 5 761 454` | `3 280 063 / 5 761 445` = 56.931256 % | `3 280 062 / 5 761 444` |

This is the **sixth** independent count and it agrees with the reconciliation. It also reproduces
the RH leg's self-consistency argument from my own code path: the `n ≥ 11` cut gives
`121 237 / 216 805`, so **`121 238 / 216 805` is the answer under no convention** — the published
card figure mixed one cut's numerator with another's denominator. I state this having recomputed it,
not because it matches `reconciliation.md`; the brief's warning about agreement-is-not-correctness
applies to me as much as to my predecessor.

**Re-running the audited leg's own script.** I executed `attack/reconcile_recount.py` and diffed the
result against the committed `reconcile_recount.out.txt`: **byte-identical**. The script is what it
claims to be, and its `π(10⁹) = 50 847 534` (⇒ `50 847 533` steps) reproduces.

**The designated theorem's constants, re-derived from FFM §7.4's statement** (`s3_constants.py`):

| quantity | my value | corpus value | verdict |
|---|---|---|---|
| `ℓ_A = log 6 690 557` | `15.7162076872…` | same | ✓ |
| C-b′ cell majorant `sup (0.17 − 2.1/b + a⁴e^{−a})/(2a−1)`, width `0.01` | **`0.00175687590387`** at cell `a = 24.40621` | same | ✓ |
| certified `0.0017569` minus that majorant | **`2.41·10⁻⁸`** | `2.4·10⁻⁸` (R2-m3) | ✓ |
| C-b′ tail `ℓ ≥ 300` | `0.00028380634` | `0.00028381` | ✓ |
| C-b′ exact requirement (quadratic solved) | `0.00175606…` at `ℓ ≈ 24.4289` | `0.0017560603` at `24.4295` | ✓ |
| C-a′ cell majorant | **`0.0515990267`** at the first cell | same | ✓ |
| C-a′ tail `ℓ ≥ 1000` / exact requirement | `0.050027515` / `0.05149345…` | `0.050028` / `0.051493457` | ✓ |
| finite branches: max gap below `60 184` / `468 049` / `1 772 201` / `6 690 557` / `10⁸` | `72@31 397` / `112@370 261` / `132@1 357 201` / `154@4 652 353` / `220@47 326 693` | same | ✓ |
| maximal-gap records below `2·10⁸` | **28**, `15 683` 12th, `191 912 783` 28th, 25 below `10⁸` | 28 (R2-m1) | ✓ |
| `e^{−0.0017569}` / `e^{−0.0043636}` / `e^{−0.0516}` at 40 dps | `0.9982446424453653…` / `0.9956459066696853…` / `0.9497086743460633…` | same | ✓ |

**The Lean gates, re-executed by me, not read.** `lake exe cache get` → 0; `lake build` → 0,
`Build completed successfully (2208 jobs)`; `lake env lean audit_exhaustive.lean` → 0,
`declarations scanned: 63`, `depending on sorryAx: [Firoozbakht.firoozbakht]`;
`shasum -a 256 lean/Firoozbakht/Statement.lean` = `6528868823c0637dd182c914e2ef43a7455f851335cafaba6cee934802e004c1`.
Every value matches `lean-probe-report.md` and the round-2 skeptic. **The kernel leg is clean.**
The reconciliation declared its Lean status second-hand; that declaration was honest, and the
underlying facts hold.

---

## 2. BLOCKERS

### S3-B1 — **BLOCKER** — decision 2 says `axler2014newbounds` is L0 *"at every site in the corpus"*; **six sites still say it is L2_strong and unopened**, one of them a round-2 artifact the reconciliation declared consistent. **R2-B2 limb 2 is not closed.**

**Where** (all quoted from the tracked tree, 2026-07-27, after the round-3 merges):

| site | what it still says |
|---|---|
| `attack/concept-cards/L2-threshold-asymptotics.md:9` | `` `axler2014newbounds` (**L2_strong, NOT OPENED**) Corollaries 3.5/3.6 `` |
| `…/L2-threshold-asymptotics.md:78,98` | *"which were **not fetched** in this run"*; *"is at L2_strong and unopened"* |
| `…/L3-necessary-condition.md:61,67` | *"Axler's Corollary 3.6, unopened"*; *"the effective `π(x)` input … was never opened"* |
| `…/L4-sufficient-condition.md:70` | *"Axler was **not opened in this run**; this is Priority 1 for the citation gate"* |
| `…/D3-pi-and-count-index-identity.md:60` | *"is at tier L2_strong and was never opened"* |
| `…/INDEX.md:62` and `INDEX.md:248` | dependency table: *"`axler2014newbounds` (**L2_strong, unopened**)"*; next-action 2: *"**Open Axler.** … unopened … Citation-gate Priority 1"* |
| `attack/re-attack/attack-round-2/proof-attempt-RH-conditional-bound.md:708–711, 941–945` | *"Axler's Corollary 3.5, **unopened in this run** … the numeral `0.17` must not be quoted downstream until Axler is at L0"*; *"**Axler is still unopened.** … **Citation-gate Priority 1, unchanged since round 1**"* |

**Why this is a BLOCKER and not bookkeeping.** It is R2-B2's exact failure mode, one round later,
in a document whose §2 asserts the opposite in its own words — *"`axler2014newbounds` is tier L0 at
every site in the corpus"* — and whose §5 asserts *"a `write-paper` leg reading any one of these
files now reaches the other three, and finds one answer at every site."* The tree does not support
either sentence. Concretely:

1. **The RH artifact is one of the four the banner declares reconciled**, and `reconciliation.md` §6
   records it as *"banner only — nothing in this document needed correcting."* That is false: two of
   its flag blocks gate a live numeral (`0.17` in Corollary D.2) on a tier that decision 2 says is
   already cleared, and one of them declares a citation-gate priority that is already discharged.
2. **The cards are the layer the reconciliation itself calls load-bearing** — its own §5 says a wrong
   number in a canonical card *"is read first by every downstream leg, which is exactly what made
   R2-M1 worse than a disputed line in a proof attempt."* The same argument applies verbatim to a
   wrong **tier** in a canonical card, and the leg applied it to the denominator and not to the tier.
3. **The ledger's own amendment names the missing sites.** The `axler2014newbounds` row's edition ⚠
   ends *"…while cards **T1**/**L2**/**L4** use the preprint's numbering"*. Only `T1` was ever
   amended. The instruction to propagate is written on the row that was propagated *from*.
4. A downstream leg reading `INDEX.md` — the entry point — is told to spend a funded leg **opening a
   source that has been open since 2026-07-26**, with MD5s on the ledger.

**Repair.** Amend the six sites to tier **L0** with the two standing ⚠ (edition numbering; the
preprint-only `(1,0,0,0)/1 772 201` row), exactly as `T1` and the ledger already carry them. In the
RH artifact this is a tier pointer only — its mathematics is untouched and `0.17` becomes citable.
`INDEX.md`'s next-action 2 should be struck and replaced by the two sources that *are* unopened
(`granville1995cramer` at journal pagination, `oliveira2014goldbach`).

---

### S3-B2 — **BLOCKER** — the reconciliation's *"what is still open"* section states four things about the tree that the tree contradicts, and the round-3 synthesis has already re-published them as the corpus's gate status

**Where.** `attack/reconciliation.md` §6 ("Not edited, deliberately"), §7 item 3, §8 items 2 and 4;
propagated into `attack/synthesis.md` §0 (l. 50), §7 (l. 728–731, 744), §8 item 4 (l. 761), §9
(l. 908–909, 918–919).

| the claim | the tree |
|---|---|
| *"`paper/paper.tex` … a round-1 artifact that §7 says must be **rewritten** against round 2"* (§6, §8 item 4) | `paper.tex` **was** rewritten against round 2 on 2026-07-26 — commit `d33dfe0` *"write-paper round 2: rewrite paper.tex against round 2, superseding round 1"*, plus `1637cf3`. It is 2460 lines, treats Axler as **read at the locator in both editions** (l. 83, 196–199, `haz:axler`), carries `0.998244` as the theorem it keeps, and **already retires `0.99565`** in Rem. `rem:retired` for the preprint-only-row reason — i.e. it reached decision 1 independently, a day early |
| *"It is … asserting a tier that is now wrong (**«Axler … not opened»**)"* (§8 item 4) | No such assertion exists in `paper.tex`. Grep returns zero hits; the paper's Caveat `haz:axler` records the promotion and the two editorial hazards |
| *"and constants that are now superseded — including `0.99553`"* (§8 item 4) | `0.99553` appears **once**, in Rem. `rem:C-compare`'s round-1-vs-round-2 column, correctly labelled *"(from a lemma that did not support it)"* |
| *"**No citation audit has been run on the round-2 corpus at all** — the only one on disk is a round-1, paper-side audit that itself returned **BLOCKED**"* (§7 item 3, §8 item 2) | `attack/verification-report.md` is the **round-2** audit (`cite-20260726-d5a8`, 2026-07-26, commit `51756c5`), **verdict PASS**: 91 `\cite` instances, 22 citekeys, 59 locator pairs, zero L3, audited against the *amended* ledger including the §2.8 rows the reconciliation says carry only a *"standing re-audit obligation"*. It also carries the Granville pagination caveat explicitly. Separately, `attack/editorial-verdict.md` is the **round-2** gate (`review-20260726-7d55`, REWRITE on the 2460-line paper), which `synthesis.md` l. 909 calls *"round 1"* |

**Why this is a BLOCKER.** Three reasons, and the third is the one that matters.

1. **It is the same error the leg exists to prevent, committed by the leg**, and it says so itself:
   §7's closing lesson is *"a leg's claim about the state of a file is not evidence about the state
   of that file. `git show` is."* §3 is entirely a tree check; §6, §7 and §8 are not, and nothing
   marks the change of standard. The leg's §9 self-verification claims *"every string this document
   claims to have edited (`grep` after each edit)"* — that discipline was applied to what it wrote
   and not to what it declined to write.
2. **It has already propagated.** The round-3 synthesis (`4753437`, 15:09, after the reconciliation
   merged at 14:49) now states as the corpus's headline gate status: *"The citation audit has **not**
   been run on this corpus … The only audit on disk is round-1, paper-side, and it returned
   **BLOCKED**"* and *"`paper/paper.tex` is a **round-1** artifact."* A false statement about the
   tree has become a false statement about a **gate**, in the document a `write-paper` leg reads
   first. That is strictly worse than where R2-B2 started.
3. **It misdirects the two most expensive items on the next-run list.** §8 items 2 and 4 fund a
   citation audit that has run and passed, and a paper rewrite that has been done. The genuinely
   open provenance work — `granville1995cramer` at journal pagination, `oliveira2014goldbach`
   behind its paywall — is real and is correctly named in §7 items 1–2; it is buried under two
   recommendations that a reader can check in thirty seconds and that will cost the loop a round.

**Not overstated.** The *substance* of §7 items 1, 2, 4, 5 and 6 is correct and I confirm it: card
`L6` is `L2_weak` and unopened and is load-bearing in **both** branches of Theorem C (I verified the
dependence: C-a′'s small branch consumes `g_{n₀} > 1919`, which is `p_{n₀} > 2⁶⁴`, and its
`0.93961 → 0.94970` improvement comes entirely from the `10⁸` cutoff that fact licenses);
`granville1995cramer` is L1 at preprint pagination and is the load-bearing citation of the
refutation-side argument; the certificates are 50–60-digit floats, not interval arithmetic; `P6′-rec`
rests on 29 record steps; and the residual `0.176 %` window is genuinely open mathematics. **What is
wrong is the account of what the tree already contains, not the account of what is missing.**

**Repair.** Correct the four claims in `reconciliation.md` §6/§7/§8 and in `synthesis.md`
§0/§7/§8/§9 against `git log`; re-point §8 item 2 at the two sources that are actually unopened;
replace §8 item 4 with *"re-audit the round-2 paper against the round-3 decisions"* (the paper agrees
with them already, so this is a check, not a rewrite).

---

## 3. MAJOR

### S3-M1 — **MAJOR** — R2-M2 is applied at one of its three named sites; FFM still says C-a′ holds *"unconditionally, Dusart only"* in its verdict table and in the sentence it hands downstream

`faults.md` R2-M2's "Where" names **three** sites: §7.4's header, §2's verdict row, §13's defensible
sentence. `reconciliation.md` §5 reports R2-M2 *"Does not stand. Applied."* Two survive:

- `proof-attempt-first-failure-maximality.md:173` — *"| **(M1)** restricted to `p_m ≤ 0.94970·p_{n₀}` | **PROVED** unconditionally, Dusart only (§7.4, Thm C-a′) |"*
- `…:751` (§7.4's own **"Reading of Theorem C, round 2"**, the paragraph written to be quoted) — *"`g_{n₀}` exceeds every gap between primes below `0.94970·p_{n₀}` — **unconditionally, on Dusart alone**"*

Neither names card `L6`, and l. 751 sits **eighty lines below** the corrected header that says the
label is false — so the document now asserts both readings, and the quotable one is the wrong one.
§13's corrected sentence shows the honest form and is the model: *"on Dusart's L0 analytics, given
the published `2⁶⁴` verification height (card `L6`, L2_weak, unopened) and a finite in-run gap
computation."*

**Repair.** Apply §13's wording to l. 173 and l. 751. One line each. Until then R2-M2 is open, and
round-1 F3's pattern — *"unconditional"* asserted on a chain containing an unopened source — is
still live in the corpus's own summary table.

### S3-M2 — **MAJOR** — `reconciliation.md` §9 credits `reconcile_recount.py` with three computations the script does not contain

§9 reads: *"`attack/reconcile_recount.py` → the table of §4, **plus** `π(10⁹) = 50 847 534` …,
**plus the maximal-gap record enumeration to `2·10⁸`** (28 records; `15 683` twelfth, `191 912 783`
twenty-eighth) that adjudicates R2-m1, **plus the four headline exponentials at 40 dps**"*, and §4
says of the ordinal *"**Confirmed independently here** — own running-maximum enumeration."*

The script is 111 lines. It sieves, counts descents, re-adjudicates near-ties and runs a segmented
`π(10⁹)`. **It contains no gap enumeration and no exponential** — `grep -E "gap|record|exp\("`
returns nothing, and its committed log (which I reproduced byte-identically) prints neither. So the
two claims the leg marks as *its own* computation rest on no artifact on disk.

**The numbers are right** — I computed both independently (§1: 28 records, `15 683` 12th,
`191 912 783` 28th; the three exponentials to 40 dps) — which is why this is MAJOR and not BLOCKER.
But the defect is precisely the one the leg's own §9 promises against: *"Every number in it is either
this leg's own computation (`attack/reconcile_recount.py`) or explicitly attributed to the leg it
came from."* A third party auditing R2-m1's reversal from the named script finds nothing, and the
adjudication of a MINOR that reverses a published ordinal then rests on an unpublished code path.

**Repair.** Either add the enumeration and the exponentials to `reconcile_recount.py` (twenty lines)
and re-commit its log, or amend §9 to attribute them to an unpublished ad-hoc computation. Do not
leave the script credited with work it does not do.

---

## 4. MINOR

### S3-m1 — **MINOR** — the "weakest" wording survives R2-M3 at two uncited sites in the same document

`proof-attempt-first-failure-maximality.md:171` — *"this is the **weakest** known sufficient
hypothesis"* — and `:180` — *"the **weakest** of them is precisely the one whose …"*. R2-M3 named
§3.3/§5/§5.2 and those are fixed; these two were not in its list and were not swept. Since
Proposition 4 makes `gov` and `min` incomparable, "the weakest" has no referent among the three at
either site. One-word fix (*"weakest known sufficient hypothesis"* → *"a minimal sufficient
hypothesis, incomparable to P6′-gov"*).

### S3-m2 — **MINOR** — one index/pair conflation survives R2-m2

`…-first-failure-maximality.md:913` (§11 item 1) still reads *"17 exceptions below `10⁹`"* — the
census is 17 **indices** (`p < 10⁹`) carrying 20 **pairs** (`p < 3·10⁸`), which §3 and §9 now state
correctly. Same fix as §3's.

### S3-m3 — **MINOR** — the retired denominator is still live in three round-1 documents, one of which is not a notebook

`attack/decompose.md:222` and `:485` print *"`T` decreases at **121 238 of 216 805** consecutive
steps"* as a headline; `attack/proof-attempt-0.md:217` still defends the one-step difference as
*"a range convention"*, which decision 4 shows is an implementation artefact; `notebook-0` R4 still
carries `216 814`. The reconciliation's exclusion of round-1 artifacts is declared and defensible
for notebooks and proof attempts, and it made the right call to amend the **cards**. `decompose.md`
is neither — it is the frame document a fresh leg reads before the cards, and it was not in the list.
Add it to the next amendment sweep, or add a one-line supersession pointer at both sites.

### S3-m4 — **MINOR** — card `L4`'s edition instruction contradicts the ledger's own fetch record

`concept-cards/L4-sufficient-condition.md:70`: *"Cite **arXiv v4 only**."* The ledger's Axler row
pins **arXiv:1409.1780v3** (MD5 `f4cde1df…`) plus the journal and the corrigendum; no `v4` was
fetched by this run. The same card sentence also carries the stale *"not opened in this run"* of
S3-B1, so both are fixed in one edit — but the version numeral is a separate error and would survive
a tier-only sweep.

### S3-m5 — **MINOR** — the canonical cards disagree on how many recounts agree

Card `L15:45` says *"**Four** independent recounts agree"*; card `D5:49` says *"**Five** independent
counts agree"*; `reconciliation.md` §4 says five and lists them. Both cards were amended by the same
leg in the same commit. With this document the number is **six**. Cosmetic, but it is a discrepancy
between two cards that a downstream leg would have to adjudicate, which is the class of thing this
round exists to remove.

---

## 5. What I attacked and could not break

Listed so the report is calibrated. Every item was re-derived or re-executed here, not read.

| # | attacked | verdict |
|---|---|---|
| 1 | **Decision 1** — is C-b′ the right designation? | **SOUND.** The deciding ground is documentary and checks out: the `(2.1,0,0,0)/6 690 557` row is the one present in both editions per two independent fetches with matching MD5s, the ledger recorded the downstream rule *before* the decision, and C-b′ is also the sharper theorem (`0.176 %` vs `0.435 %` sliver). The decision goes **against** the longer sibling document's own theorem, which is the opposite of the "prefer the leg that wrote more" failure |
| 2 | **The designated theorem itself** | **CORRECT.** Cell majorant, tail bound, exact quadratic requirement, both finite branches and the Axler row's empirical validity all re-derived here (§1). The proof structure — majorant over cells, not a sample — is a genuine proof |
| 3 | **Decision 3's reversal of a BLOCKER** | **CORRECT, and correctly reported.** The `git log` timing explains the round-2 skeptic's error exactly; reporting *"the premise of my brief is false"* is the behaviour the loop needs and it is not softened anywhere in the document |
| 4 | **Decision 4 against its own predecessors** | **CORRECT.** My sixth count agrees, including the `n ≥ 11` self-consistency test that makes the disputed pair impossible under any convention. The leg contradicted the document that had declared the matter settled, which is the right instinct |
| 5 | **Does any round-3 artifact assume `F`, or launder a scale-limited computation as general?** | **No.** `reconciliation.md` states `F` OPEN at the top, in §7 and in its colophon, refuses to clear the gate, and names the obstruction (`g_n ≪ p^{0.525}` unconditional, `≈ √p log p` under RH, both *powers* where `F` needs polylog; no induction mechanism). The two riders on the `55.92 %` figure — range-dependence and non-diagnosticity for P6′ — are both correct and both stated |
| 6 | **The kernel leg** | **CLEAN**, re-executed here: cache 0, build 0 (2208 jobs), audit 0, 63 declarations, one `sorryAx` (`Firoozbakht.firoozbakht`), `Statement.lean` byte-frozen at the reported SHA-256 |
| 7 | **The reconciliation's declared perimeter** | **HONEST.** *"Opened no source", "re-ran no mathematics except the recount", "cleared no gate", "took second-hand from whom"* — each is true of what the document does, and the second-hand attributions are marked at the sites, not only in the colophon |
| 8 | **R2-B1's retirement, hunted for stale live sites** | **No stale site found.** Every surviving `0.99565` / `1 772 201` / `132` is inside a retirement remark, a history column or an edition flag. The single residue is round-1 `proof-attempt-0.md`'s own §6.1/§7, whose §11 now carries the pointer |

---

## 6. Reading of the fault set

Round 3 did the job it was asked to do. **All five decisions are correct**, three of the four checked
against my own recomputation, one against `git log`, and the fifth — the cross-reference layer —
substantially delivered. The reconciliation reversed two skeptics and one proof attempt on the
denominators, and reversed **its own brief** on the ledger; both reversals hold. That is the
behaviour the loop was missing.

**Both surviving BLOCKERs are the same fault, and it is the fault the leg was created to fix.** Not
one of them is an error inside a decision. They are: a tier that was decided *"at every site"* and
propagated to one artifact out of seven (S3-B1); and a section describing the state of the tree from
memory of a report, inside the document whose closing lesson is *"a leg's claim about the state of a
file is not evidence about the state of that file"* (S3-B2). The reconciliation caught this species
of error in a skeptic and in a synthesizer. It did not catch it in itself, and the round-3 synthesis
has already inherited it.

The structural reading, stated once: **the corpus's problem has moved from mathematics to
bookkeeping, and bookkeeping is now the cheaper thing to get right.** Every finding in this document
is closable by editing text — no sieve, no fetch, no derivation. What is *not* closable that way is
listed in `reconciliation.md` §7 items 1, 2, 4, 5, 6, which I confirm: card `L6` unopened under both
branches of the headline theorem, Granville at preprint pagination under the whole refutation-side
argument, floating-point certificates where interval arithmetic is needed, 29 data points under
`P6′-rec`, and one genuinely open short-interval prime-count problem in the `0.176 %` sliver.

**A note to whoever runs the next skeptic.** Round 2 inherited a wrong number from round 1 and
re-published it; round 3 caught that and then made a structurally identical mistake about the
paper and the citation gate; and I found it only because I ran `git log` on files nobody had asked
me about. **Do not confirm a finding of mine by observing that it matches this document.** Six of
the fourteen round-2 findings I confirmed as closed, I confirmed by recomputing the number from the
statement; two I reversed against the leg's own report of itself. Recompute, and check the tree.

**Neither BLOCKER, neither MAJOR, and none of the MINORs touches `F`. `F` remains OPEN**, and
nothing in round 3 moves it in either direction. The defensible sentence is unchanged:
*Firoozbakht's conjecture is numerically robust over the verified range and simultaneously
incompatible with the standard Cramér–Granville heuristic; at least one of the two must fail, and no
current technique can say which.*

---

*Artifact of leg `skeptic`, round 3, molecule `task-20260727-5096`, run `germ-20260725-791a7c45`.
Verification scripts: `attack/skeptic-round3-checks/s3_recount.py`, `…/s3_constants.py`. The Lean
gates and the audited leg's own recount script were **re-executed**, not read. Round 1's fault list
is preserved at `attack/faults-round-1.md`; round 2's at
`attack/re-attack/attack-round-2/faults.md`. **The conjecture remains OPEN. The evidence gate
remains BLOCKED.***
