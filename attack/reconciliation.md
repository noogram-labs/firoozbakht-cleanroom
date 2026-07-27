# reconciliation.md — round 3, the leg that owns the seams

**Molecule:** `task-20260727-264e` (leg `reconcile`, crew role: synthesizer) — **ROUND 3**
**Run:** `germ-20260725-791a7c45` · **Parent re-attack loop:** `reattack-20260726-57d1` (rounds 1–2)
**Date:** 2026-07-27 · **Formal backend:** Lean 4 / Mathlib (no Lean written or re-run by this leg)
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.

> **Status of `F`: OPEN.** Nothing in this document proves or refutes `F`, and nothing in it is
> capable of doing so. **This leg is not a proof attempt and opened no mathematics.** Its entire
> output is the removal of ambiguity between artifacts that two rounds of fan-out left
> contradicting each other. Reconciliation removes ambiguity, not obstruction.

---

## 0. Why this leg exists, and what it is not

Two rounds ran. Round 1's skeptic named the failure mode — *"a fan-out with no reconciliation stage
… nobody owned the seams"* — and round 2 **doubled the fan-out without adding one**, then reproduced
the prediction on itself. The round-2 skeptic's own structural reading is unusually precise about
what came out of it (`attack/re-attack/attack-round-2/faults.md` §7):

> *"Every one of the three BLOCKERs is a seam, not a step. Not one of them is an error inside a
> proof."*

Two legs repaired the same fault differently; two legs assigned one source opposite tiers; one leg's
repair rested on a citation the other leg had already shown to be edition-only. **A third fan-out
would have manufactured more seams.** This leg is the stage that owns them. Its brief was five
decisions, and this document is the record of those five decisions plus the edits that make the tree
consistent with them.

**What this leg did not do**, stated first so nothing here is over-read:

- It **re-ran no mathematics** from either round except the one recount its brief required
  (decision 4) and two cheap integer checks used to adjudicate ordinals.
- It **opened no source.** Every provenance statement below rests on the round-2 fetch record and on
  the round-2 skeptic's *independent* re-fetch of the same three documents with matching MD5s — two
  independent fetches agreeing is the strongest evidence available on disk, and it is second-hand
  here.
- It **did not re-run the Lean gates** (`lake` toolchain cache is not materialised in this
  worktree). The kernel leg's status is reported at the exit codes the round-2 skeptic
  **re-executed**, and is labelled as second-hand.
- It **cleared no gate.** The evidence gate is a skeptic's and an evidence-gate leg's call, not a
  reconciler's. §7.

**Write perimeter, declared.** `faults.md` **R2-m5** records a tension: the round-2 briefing's
rule 6 says *"round K writes ONLY under `attack-round-K/`"*, while repairing a seam requires editing
the artifacts that carry it. This leg's brief resolves the tension explicitly and in the other
direction — it instructs *"edit in place the artifacts your decisions change
(`attack/source-ledger.md`, the affected proof attempts, `attack/synthesis.md`)"*. Every edit made
outside this file is therefore authorised, is marked in place with the date `2026-07-27`, the
decision number and the finding it discharges, and is listed in §6. **Nothing was silently
changed and nothing was deleted** — retired material is retired to a remark, never removed, because
the history of a repair is part of the evidence that the repair was needed.

---

## 1. Decision 1 — one repaired Theorem C(b): **Theorem C-b′**, `p_m ≤ 0.998244·p_{n₀}`

### The collision (`faults.md` R2-B1)

Round 2 was fed round-1's BLOCKER **F2** twice, and both legs repaired it, correctly and
independently, into two different theorems that neither cited:

| | **Theorem C-b′** (FFM §7.4) | Theorem C(b\*) (UVR §3.5) |
|---|---|---|
| repaired lemma | (A-high′), `v = ℓ² − ℓ − 1 − 2.1/ℓ` | (A-high\*), `v = ℓ² − ℓ − 1 − 1/ℓ` |
| Axler row consumed | `(a,b,c,d) = (2.1,0,0,0)`, `x₀ = 6 690 557` | `(1,0,0,0)`, `x₀ = 1 772 201` |
| uniform constant | `d ≥ 0.0017569` | `d ≥ 0.0043636` |
| headline | **`p_m ≤ 0.998244·p_{n₀}`** | `p_m ≤ 0.99565·p_{n₀}` |
| finite branch | `p_m < 6 690 557`, `g_m ≤ 154` | `p_m < 1 772 201`, `g_m ≤ 132` |
| edition of the row | **present in BOTH arXiv v3 and *Integers* 16 (2016) A22** | ⚠ **arXiv preprint ONLY** |

**Both theorems are mathematically correct.** The round-2 skeptic verified both by solving Lemma W's
hypothesis rather than evaluating either leg's sufficient condition, at 40–50 decimal digits, and
each leg's constant covers its own true requirement (`0.00175606031` at `ℓ = 24.4295` for the
`a = 2.1` bar; `0.00436288239` at `ℓ = ℓ₁` for the `a = 1` bar). **This is not a correctness
dispute.** It is a corpus carrying **three constants under one theorem name** — `0.99553` (round 1,
from a lemma that did not support it), `0.99565`, `0.998244` — and **two finite branches** that a
Lean leg is told to certify.

### The decision

> **Theorem C-b′ is the corpus's single repaired Theorem C(b).** Live constants: `d ≥ 0.0017569`,
> `p_m ≤ 0.998244·p_{n₀}`, finite branch `6 690 557 / 154`. **Theorem C(b\*) is retired to a
> remark.** `0.99553`, `0.99565`, `0.0043636` and the pair `1 772 201 / 132` may appear only as
> history, and only with the edition flag attached.

### Why — verified against the artifacts, not inherited

The brief asked that the round-2 skeptic's preference be **verified against the artifacts rather
than inherited**. It was, and it survives, on a ground that is documentary rather than aesthetic:

1. **The edition question decides it, and it is settled on disk in three places.** The Axler row
   `(1,0,0,0) / x₀ = 1 772 201` that C(b\*) consumes exists in **arXiv:1409.1780v3 only** and is
   **absent from the published *Integers* 16 (2016) A22** — the preprint's lower-bound table has 14
   columns, the journal's 12, dropping `(1,0,0,0)/1 772 201` and `(2.65,11.6,0,0)/166 219 973`. This
   was established by the FFM leg from the PDFs (its §7.1 Finding B) and **independently confirmed by
   the round-2 skeptic**, which re-fetched all three documents and reproduced all three MD5s
   (`f4cde1df…`, `29a92c5e…`, `4817ba68…`) and decoded the journal's font-scrambled table
   digit-for-digit. Two independent fetches agreeing is as strong as this run's evidence gets.
2. **It is already the tree's own standing rule, written before this decision.** The
   `axler2014newbounds` row of `attack/source-ledger.md` (amended 2026-07-26, verified in the
   tracked tree by this leg — §3) reads: *"**Downstream rule:** do not quote `x ≥ 1 772 201` against
   the journal citation. The `(2.1,0,0,0)/6 690 557` row is present in **both** editions and is
   strictly stronger; use it."* Card `T1-effective-pi-bounds.md` carries the same ⚠. **The
   designation is not a new judgement; it is the corpus applying a rule it had already recorded and
   then failed to propagate.**
3. **C-b′ is also the sharper theorem** (`0.998244 > 0.99565` — the excluded sliver narrows from
   `0.435 %` to `0.176 %`), so the edition-safe choice is not bought at a mathematical cost. That is
   the unusual and lucky part: the two criteria agree.
4. **C(b\*)'s own leg says the same thing about it, for a different reason.** UVR declared *"no
   source PDF was opened by this leg"* and instructed that its theorem *"must never be quoted inside
   a sentence containing the word 'unconditional'"*. That instruction was **over-strict on tier**
   (the source *was* opened, the same day, by the sibling) and **exactly right on row**. Retiring
   the theorem discharges the row exposure; §2 fixes the tier.

### What C(b\*) is kept for

Not sentiment. C(b\*) is the sharp statement of *what round 1's printed lemma would have ordered*,
and therefore the cleanest available proof that **round 1's conclusion survived its own broken
derivation** — its `0.0043636` sits below round 1's printed `0.004479`, which is exactly the F2(c)
question. It is retained as a remark and as calibration, in place, in UVR §3.5.

### What is retired, and where

`attack/re-attack/attack-round-2/proof-attempt-unconditional-verified-range.md` now carries the
retirement notice at §3.5, the rescoped quarantine on the theorem statement, a retired-pricing note
at §3.7 (the live finite pair is `6 690 557 / 154`, not `1 772 201 / 132`), an amended §4.4
"what may be called unconditional" row, an amended §9 gap **G3 → G3′**, and an amended §10 verdict.
`…/proof-attempt-first-failure-maximality.md` §7.4 carries the designation notice.
`attack/source-ledger.md`'s Axler row records that its downstream rule is now load-bearing on a
designation.

### What this decision does **not** settle

Both theorems remain **conditional on card `L6`** (`p_{n₀} > 2⁶⁴`, tier **L2_weak, NOT OPENED**) for
their small branches, and on the Axler corollaries for their main branches. Designating one of them
does not upgrade either. See §5 (R2-M2) and §7.

---

## 2. Decision 2 — one Axler tier: **`axler2014newbounds` is L0**, with a standing edition ⚠

### The contradiction (`faults.md` R2-B2, limb 2)

The same source carried three answers on the same day:

| site | tier as written before 2026-07-27 |
|---|---|
| `attack/source-ledger.md` (amended 2026-07-26) | **L0**, opened, three MD5s, edition table, ⚠ on the preprint-only row |
| `attack/concept-cards/T1-effective-pi-bounds.md` (amended 2026-07-26) | **L0**, same ⚠ |
| FFM §7.1 / §7.5 / §11 items 8–9 | **L0**, opened, both editions |
| UVR §3.2, §3.5, §4.4, §6 item 1, §9 G3, §10 | **L2_strong, NOT OPENED**, MAJOR gap G3, hard quarantine |

### The decision

> **`axler2014newbounds` is tier L0** at every site in the corpus: the arXiv v3 preprint, the
> published *Integers* **16** (2016) A22 and the 18 Jan 2018 Corrigendum were fetched, MD5-pinned
> and read at the locators on 2026-07-26. **The residual exposure is not tier, it is edition**, and
> it has exactly two components, both of which travel with every Axler citation from now on:
>
> 1. **⚠ Corollary numbering differs between editions.** arXiv Cor. 3.5 / 3.6 are *Integers*
>    Cor. 3.4 (p. 8) / 3.5. The 2018 Corrigendum — *"In Corollary 3.4 on page 8, replace «If
>    `x ≥ 5.43`» by «If `x ≥ 2 634 800 823`»"* — uses the **journal's** numbering while this run's
>    cards use the **preprint's**. Both point at the same inequality, so **no mathematical error
>    propagated**; every locator must nevertheless name its edition.
> 2. **⚠ The `(1,0,0,0) / x₀ = 1 772 201` row is preprint-only.** Never quote `x ≥ 1 772 201`
>    against the journal citation. Use `(2.1,0,0,0) / 6 690 557`, present in both and strictly
>    stronger. This is what decision 1 does.

### Why L0 rather than L2_strong

Because the source was in fact opened, and the opening is the most thoroughly corroborated act in
the whole run: **two legs fetched the same three documents independently and reported identical
MD5s**, the corrigendum's text is quoted verbatim and matches, the edition-numbering finding
reproduces from both PDFs, and the skeptic additionally *falsified* the pre-corrigendum range from
the primes themselves (4 987 066 counterexamples below `10⁸` to the `x ≥ 5.43` clause, smallest at
`p = 59 753`, all below the corrected range — so the corrigendum is not merely cited, it is
independently *needed*). A tier is a statement about what the run has read. The run read it.

**UVR's `L2_strong, NOT OPENED` was true of UVR** — that leg fetched nothing, and said so honestly.
It was **false of the corpus** the moment its sibling landed the promotion, and no mechanism existed
to tell it. That is the seam, in one sentence: **a per-leg truth published as a corpus truth.**

### What was edited

`…/proof-attempt-unconditional-verified-range.md`: the tier bracket under (A-high\*) §3.2; the tier
bracket under Theorem C(b\*) §3.5 (quarantine **rescoped**, not struck — it now bites on the row and
on the §4 conflation hazard, not on an unopened source); the §4.4 table row; §6 item 1; §9 gap
**G3 → G3′** (tier gap closed, *edition* gap opened and then discharged by retirement); §10's
`F2 — provenance` and `Theorem C(b\*)` verdict rows. `attack/source-ledger.md` and card `T1`
required **no tier change** — they were already correct (§3).

---

## 3. Decision 3 — the ledger amendment: **it had already landed.** Verified in the tree.

The brief states, following `faults.md` **R2-B2** limb 1: *"One leg reported an amendment as landed;
it never did. Apply it for real."* **This leg checked the tracked tree instead of either report, and
reports the opposite: the amendment landed on 2026-07-26 and is complete.** Reporting this plainly
is the whole point of a reconciliation stage — the alternative is a third round re-fixing something
that was fixed, and calling that convergence.

**Evidence, line by line, from the committed tree at the time of writing:**

| claim in R2-B2 | state in the tracked tree |
|---|---|
| *"`source-ledger.md:406` still reads tier **L2_strong**"* | `source-ledger.md` line 412 reads **`tier L0`** *(promoted from L2_strong on 2026-07-26 by the re-attack leg `task-20260726-56a7`)*, followed by the citation, the three-document fetch table with MD5s, the edition-numbering ⚠ table, the statements read at the locator, and the preprint-only-row ⚠ with its downstream rule |
| *"`source-ledger.md:642` still reads «Axler was not opened»"* | §6 gap 3 reads **`~~Axler was not opened.~~ CLOSED 2026-07-26`** — preprint, journal version and Corrigendum |
| *"`T1-effective-pi-bounds.md:15` still reads L2_strong, NOT OPENED"* | card `T1` line 5 records the promotion `L2_strong → **L0**`; line 17 heads the Axler block **`(L0 — arXiv:1409.1780v3, Integers 16 (2016) A22 and the 2018 …)`**; line 24 carries the ⚠ on the `(1,0,0,0)/1 772 201` row; the hazard section carries *"Every Axler locator must name its edition"* |
| ledger head | records the amendment explicitly, and a second, separate amendment adding two rows in §2.8 |

**Why the skeptic saw otherwise, and why that is the more interesting finding.** The amendment
landed in commit `61689d0` and merged at `4526b27`. The skeptic's two line numbers (`406`, `642`)
resolve **only** in the pre-merge tree — it read a worktree branched before the merge. The round-2
**synthesis** independently reached this same conclusion (`attack/synthesis.md` §5.2, verified with
`git show`) and, notably, caught the identical error in **its own draft**, which had asserted the
amendment was still pending. So the same class of error — *reading a report instead of the tree* —
was committed by a skeptic and by a synthesizer, one round apart, about the same commit.

**Conclusion.** R2-B2 limb 1 is **STALE, not open**; FFM §11 items 8 and 9 are **accurate as
written**. What genuinely had not landed was limb 2 — the propagation of the tier into the sibling
leg's document — and **that is what this leg landed** (§2). The ledger amendment this decision was
asked to apply is therefore recorded, not re-applied: `attack/source-ledger.md` now carries a
round-3 reconciliation record at its head stating the tier is settled, that no row was reopened,
and where the propagation went.

**One honest consequence for the skeptic's arithmetic:** R2-B2 was one of three BLOCKERs. After
§1–§3, **all three are discharged** — B1 by designation, B2 limb 1 as stale and limb 2 by
propagation, B3 by retiring the theorem that consumed the fragile row. That is a claim about the
seams, and **it is not a gate clearance** (§7).

---

## 4. Decision 4 — the `55.92 %` denominators, recounted **from the statement**

### Why a fourth count

`faults.md` **R2-M1** is *"a wrong number inherited from the previous round's skeptic and
re-published as settled"*, and the round-2 skeptic's own warning is the operative instruction:
*"«reproduces `faults.md` exactly» is a confirmation of agreement, not of correctness."* So this leg
wrote a fresh script from the **statement**, with no upstream code path open, and was prepared to
contradict both prior rounds.

**Script:** `attack/reconcile_recount.py` · **log:** `attack/reconcile_recount.out.txt`.
Own sieve of Eratosthenes; `T_n := p_n·(p_n^{1/n} − 1)` formed from the actual `p_n` via `expm1`;
every comparison whose relative margin fell inside `10⁻⁹` re-adjudicated with `mpmath` at 60 decimal
digits (`23` / `498` / `16 218` such near-ties at the three ranges, **0 reclassified** — the count is
not float-fragile). `π(10⁹)` obtained from an independent segmented sieve.

**The convention, stated so the number is reproducible.** A *step* is an index `n` for which both
`T_n` and `T_{n+1}` are defined from the sieve, i.e. `1 ≤ n ≤ π(N) − 1`.

### The result

| `N` | `π(N)` | steps, all `n` | decreasing | steps, `n ≥ 10` | decreasing | `%` (`n ≥ 10`) |
|---|---:|---:|---:|---:|---:|---:|
| `3·10⁶` | 216 816 | **216 815** | **121 239** | **216 806** | **121 238** | **55.920039 %** |
| `10⁷` | 664 579 | **664 578** | **374 486** | **664 569** | **374 485** | 56.350055 % |
| `10⁸` | 5 761 455 | **5 761 454** | **3 280 064** | **5 761 445** | **3 280 063** | 56.931256 % |

and `π(10⁹) = 50 847 534`, hence **`50 847 533`** consecutive steps below `10⁹`.

### The adjudication — it reverses two skeptic verdicts, and this leg is the fourth to say so

> **Carry `121 238 / 216 806 = 55.9200 %` (`n ≥ 10`) and `121 239 / 216 815 = 55.9182 %` (all `n`).**

- **`proof-attempt-0.md` §9 item 18's `121 238 / 216 806` is CORRECT.** Round 1's `faults.md` **F5**
  called it an off-by-one; round 2's FFM §4 re-affirmed that verdict in bold and declared the
  three-fractions dispute settled. **Both were wrong, and round 2 was wrong more emphatically.**
- **`notebook-1` §2's `374 485 / 664 569` at `10⁷` is CORRECT**, not "denominator off by one".
- **Card `L15`'s `121 238 / 216 805` and `notebook-0` R4's `121 239 / 216 814` are each one too
  low.** L15 is the worse of the two, because round 2's amendment landed the *wrong* denominator
  into the *canonical card downstream legs read first*. **Corrected in the tree** (§6).
- **FFM §4's whole table was one too low in every denominator, at every range, under both
  conventions** — while **every numerator was right**. The diagnosis is mechanical and worth
  recording, because it is the fingerprint of the bug: a `T`-array truncated to the *gap*-array
  length `π(N) − 1` **before** differencing drops the last step, which happens to be an increase.
  That is an implementation artefact, **not a counting convention** — which is precisely what
  `proof-attempt-0.md` §5 was accused of inventing.

**Independent corroboration inside round 2 itself — and it is stronger than anyone noticed.** The
RH leg did not merely state a compatible sieve size in its §10; its **§11 item 15** ran the count
deliberately, got **`121 238 / 216 806` (55.9200 %)** — this leg's figures exactly — and then found
the *internal* inconsistency that settles the matter beyond a vote:

> *"the `n ≥ 11` convention that would give `216 805` should also drop one descent
> (`T_11 = 11.3584 < T_10 = 11.6104`, so the step `10 → 11` is itself a descent and is the one that
> cut removes), yielding `121 237 / 216 805` — so **`121 238 / 216 805` is not self-consistent under
> either cut**."*

That is decisive in a way agreement between recounts is not: **there is no convention at all under
which the pair `121 238 / 216 805` is the answer.** Either you count from `n = 10`, and the answer is
`121 238 / 216 806`, or you count from `n = 11`, and the answer is `121 237 / 216 805`. The published
figure mixes the numerator of one with the denominator of the other. The RH leg flagged this
explicitly *"so the next skeptic re-counts rather than inherits"* — **and the round-2 skeptic, the
round-2 synthesis and the FFM leg all failed to read it.** A finding sitting in a sibling artifact,
correctly labelled, going unread for a full round: that is the seam problem in miniature, and it is
the sharpest argument in the corpus for why this stage has to exist.

**Five independent counts now agree** (round-1 synthesis `verify_syn.py`; round-2 skeptic `chk_*.py`;
round-2 RH leg §11 item 15; round-2 synthesis `verify_syn2.py`; this leg `reconcile_recount.py`),
one of them with a self-consistency argument, against one document. **The dispute is closed.**

**Two riders that must travel with the figure, every time.** It is **range-dependent**
(`55.92 % → 56.93 %` across two decades, and `≈ 57.9 %` at `10⁹`) and must never be quoted without
its bound and its convention; and it is **uninformative about P6′** under every reading — it measures
single steps, while every P6′ predicate compares an index to a governor many steps back. The margin
that *is* diagnostic (`P6′-min`, `+0.4845277` at `n = 1879`) does not move at all across the same two
decades.

### One further count this leg made itself

`faults.md` **R2-m1** claims the gap `248` at `p = 191 912 783` is the **28th** maximal prime gap,
not the 27th. **Confirmed independently here** — own running-maximum enumeration to `2·10⁸` gives
**28** record indices, with `15 683` twelfth (`g = 44`) and `191 912 783` twenty-eighth (`g = 248`),
which is consistent with FFM's own census of 25 records below `10⁸`. FFM's W2 table is corrected in
place.

---

## 5. Decision 5 — the four artifacts now cite each other; and the remaining MAJORs/MINORs

### The cross-reference layer

Every round-2 artifact — the three proof attempts, the lean-probe report **and** `faults.md` — now
opens with the same **round-3 reconciliation banner**: the four-artifact table with each one's
post-reconciliation status, the five decisions in one line each, a pointer to this file, and the
restatement that `F` is OPEN. Inside each document, every amendment names its date, its decision
number, the finding it discharges, and the sibling document it defers to. `attack/synthesis.md`
(§5.1–§5.6, §6, §7) is updated to record the decisions as **landed** rather than **adjudicated**,
and `attack/source-ledger.md` and card `L15` carry round-3 records. **A `write-paper` leg reading any
one of these files now reaches the other three, and finds one answer at every site.**

### R2-M2 — the "unconditional" label on Theorem C-a′. **Does not stand. Applied.**

The brief asks whether decisions 1–4 leave it standing. They do not touch it, so it was applied
directly. FFM's Theorem C-a′ was headed *"Dusart only — no source outside `dusart2010estimates`,
L0"* and quoted in §13 as holding *"unconditionally"*, while its **small branch consumes card `L6`**
(`p_{n₀} > 2⁶⁴`, tier **L2_weak, NOT OPENED**, mediated through Kourbatov) and an **in-run gap sieve**
(`max{g_m : p_m < 10⁸} = 220`). Neither is Dusart. The dependence is not incidental: round 1's
`0.93961 → 0.94970` improvement comes **entirely** from raising the small-branch cutoff from
`60 184` to `10⁸`, i.e. **from `L6`**. This is round-1 **F3** reintroduced with a sharper label, in
the one branch round 1 had passed clean.

**Applied:** the §7.4 header now reads *"Dusart-only **analytics**; the finite branch consumes card
`L6` (L2_weak, unopened) and an in-run gap sieve to `10⁸`"*, with the honest form spelled out —
*unconditional given the published `2⁶⁴` verification height and a finite in-run gap computation*,
both named inputs, neither an analytic hypothesis — and a pointer to UVR §4.4, which builds the
correct "what may be called unconditional" table and gets this right. §13's defensible sentence is
requalified in place. **The theorem is correct; only the provenance sentence was.**

### R2-M3 — "the weakest of the three". **Does not stand. Applied.**

FFM §3.3/§5/§5.2 called `P6′-min` *"the weakest of the three"* and *"the easier obligation"* and
**dropped `P6′-gov` from card `L15`'s obligation list** — on the strength of an ordering **its own
Proposition 4 disproves**. Proposition 4 proves `P6′-gov ⇏ P6′-min` **and** `P6′-min ⇏ P6′-gov`, by
two explicit four-index counter-models; the only order relations proved anywhere are `pair ⟹ gov`,
`pair ⟹ rec` and `gov ∧ rec ⟹ min`. **In the abstract setting the document itself fixes, `gov` and
`min` are incomparable.** The ordering that does hold is **empirical** — `T_{µ(n)} ≤ T_{r(n)}` at
every index in the swept range, which *on that range* gives `gov ⟹ min`. FFM §3.2 states that
honestly (*"which is the honest statement, and is not a proof"*) and §3.3/§5/§5.2 then spend it as
if it were the proof. Since Theorem 2 shows **either** predicate at `n₀` suffices, dropping `gov` is
also **strictly lossy**.

**Applied** in three places in FFM (§3 point 2, §5's closing paragraph, §5.2's instruction to `L15`)
and **in card `L15` itself**, whose "Declared gap" now lists **`P6′-min` and `P6′-gov`** as the
obligations, with `P6′-rec` beside them because `gov ∧ rec ⟹ min` is the valid chain.

### The seven MINORs — disposition, in full

| # | finding | disposition |
|---|---|---|
| **R2-m1** | `248` called the 27th maximal gap; it is the **28th** | **APPLIED** in FFM §3's W2 table, and **independently re-verified by this leg** (§4) |
| **R2-m2** | the P6′-pair census counts **indices**, not **pairs** | **APPLIED** — FFM §3's census paragraph now says *indices* (17), records the true pair count (**20** below `3·10⁸`), and states explicitly that no ratio here may be read as a density (the true admissible-pair count below `10⁹` is `Σ_n r(n−1) ≈ 10¹⁵`); §9 items 3/5/7 relabelled |
| **R2-m3** | C-b′'s constant clears its own majorant by `2.4·10⁻⁸`, no interval arithmetic | **APPLIED as a recorded margin** next to the constant in FFM §7.4, with the explicit warning that a Lean `norm_num` without directed rounding has far less headroom here than elsewhere. **Not** repaired — repairing it means interval arithmetic, which is a funded leg, not an edit |
| **R2-m4** | the lean-probe §4 slack table drops both bounds' constants | **APPLIED** — the table is annotated: the BHP column is the `C = 1` case of a bound with an *unspecified* constant, the CMS column drops the `22/25` its own row names, so both crossovers are illustrations at a chosen constant, **not** measurements. The conclusion is unaffected and the reason is named: it rests on the **exponent**, and Theorems B and C refute every `C > 0` |
| **R2-m5** | write-perimeter tension (rule 6 vs in-place amendment) | **RESOLVED for this leg by its brief** — see §0's declared write perimeter. Recorded as a standing process question for the next loop: *a reconciliation stage cannot obey a round-scoped write rule*, so the rule needs an exemption clause naming that stage |
| **R2-m6** | `p^{−0.83}` quoted while the local exponent drifts to `≈ 1.0`, then extrapolated nine decades | **APPLIED as an annotation** in FFM §5.1, with the three local per-decade exponents (`0.4536`, `0.7365`, `0.9967`), the corrected extrapolation (`≈ 6.1·10⁻¹⁵`, a factor `≈ 55` smaller) and the note that the direction is **safe** (the noise-floor alarm strengthens). Figures attributed to the round-2 skeptic; **not** re-derived here |
| **R2-m7** | the `10³` entry of the per-decade P6′-min table does not reproduce | **APPLIED** — `2.42 → 1.354` in FFM §5, attributed to the skeptic, with the note that the discrepancy is confined to `n < 10` where every criterion in the corpus is out of range, and that the section's claim is unaffected |

### What this leg deliberately did **not** touch, and why

`notebook-{0,1,2}` and `proof-attempt-{0,1,2}.md` are **round-1 artifacts untouched since
2026-07-25**, and `attack/synthesis.md` §7 item 1 lists their defects (mis-scoped P6′ inferences,
`notebook-1`'s mistyped `p*(C)` lower endpoint, the `216 814` denominator, the reversed `T_{m(n)}`
row). **They are not seams.** They are round-1 defects that a later document already reads with the
correction stated — which is a different class of problem, addressed by rewriting round 1's
artifacts or by superseding them in the paper, not by a reconciler adding a fifth voice to them. The
one exception is where a round-1 *canonical* file carries a number this leg's decision changes:
cards `L15`, **`D5`** and the concept-card **`INDEX`**, plus `attack/source-ledger.md` — all amended,
because a wrong denominator in a canonical card is read first by every downstream leg, which is
exactly what made R2-M1 worse than a disputed line in a proof attempt. **Naming this boundary is part of the
deliverable** — a reconciliation leg that quietly widens its own scope reproduces the fan-out it
exists to stop.

---

## 6. The edits, file by file — so nothing is silent

| file | decision(s) | what changed |
|---|---|---|
| `attack/reconciliation.md` | 1–5 | **new** — this document |
| `attack/reconcile_recount.py`, `…out.txt` | 4 | **new** — the independent recount, written from the statement |
| `…/attack-round-2/proof-attempt-first-failure-maximality.md` | 1, 3, 4, 5 | banner; §3 W2 ordinal `27th → 28th` (R2-m1); §3 census relabelled to *indices* + true pair count (R2-m2); §3.3 point 2 "weakest of the three" struck (R2-M3); §4 **denominators corrected at all three ranges + convention stated + adjudication reversed**; §5 gov/min ordering corrected (R2-M3); §5 `10³` per-decade entry `2.42 → 1.354` (R2-m7); §5.1 `p^{−0.83}` drift annotated (R2-m6); §5.2's instruction to `L15` corrected; §7.4 C-a′ header requalified (R2-M2) + `e^{−0.0017569}` printed value corrected + certification margin recorded (R2-m3) + **C-b′ designation notice**; §7.5 amendment **verified landed**; §9 items 3/5/7/11 corrected; §13 defensible sentence requalified |
| `…/attack-round-2/proof-attempt-unconditional-verified-range.md` | 1, 2, 5 | banner; §3.2 (A-high\*) tier bracket **L2_strong → L0** + edition ⚠; **§3.5 Theorem C(b\*) RETIRED to a remark** + quarantine rescoped; §3.7 retired pricing (live pair `6 690 557 / 154`); §4.4 table row; §6 item 1; §9 **G3 → G3′** (tier gap closed, edition gap opened and discharged); §10 `F2 — provenance` and `Theorem C(b\*)` rows; §11 Lean sketch redirected to the both-editions Axler row |
| `…/attack-round-2/proof-attempt-RH-conditional-bound.md` | 5 | banner only — **nothing in this document needed correcting**, and its §10 count corroborates decision 4 |
| `…/attack-round-2/lean-probe-report.md` | 5 | banner; §4 slack table annotated with the restored constants (R2-m4) |
| `…/attack-round-2/faults.md` | 5 | banner only — the red-team report is **not** rewritten; its findings' dispositions live here and in the amended artifacts |
| `attack/source-ledger.md` | 1, 2, 3 | round-3 reconciliation record at the head (tier settled, no row reopened, where the propagation went); Axler row notes that its downstream edition rule is now load-bearing on the C-b′ designation |
| `attack/concept-cards/D5-threshold-Tn.md` | 4 | denominator `216 805 → 216 806`, both conventions stated |
| `attack/concept-cards/INDEX.md` | 4 | the corpus's headline statistics row corrected likewise |
| `attack/concept-cards/L15-maximal-gap-reduction.md` | 4, 5 | denominator `216 805 → 216 806` + all-`n` figure + convention; sweep size `50 847 503 → 50 847 533` (×2, and relabelled *indices*); "Declared gap" now lists **both** `P6′-min` and `P6′-gov` (R2-M3) |
| `attack/proof-attempt-0.md` | 2 | **tier pointer only** — its two `axler2014newbounds` "L2_strong, NOT OPENED" flags now name the L0 promotion and the edition hazard. No mathematics, no constant and no verdict in this round-1 document was touched |
| `attack/claims-ledger.md` | 4 | claim **C8** (the disclosed card defect) marked **REPAIRED**, with where |
| `attack/re-attack/rounds.md` | 1–5 | round-3 addendum: the disposition of all three round-2 BLOCKERs and the three MAJORs, including the correction of this file's own "never made" statement about the ledger |
| `attack/synthesis.md` | 1–5 | §5's adjudications updated from *adjudicated* to **landed**, with this document cited; §7 item 1's checklist marked off item by item; §6's gate reading unchanged |

**Not edited, deliberately:** `lean/` (no gate re-run, no Lean written), `paper/paper.tex` (a round-1
artifact that §7 says must be **rewritten** against round 2, not patched), `notebook-{0,1,2}`,
`proof-attempt-{0,1,2}.md`, `attack/faults.md` (round 1), `attack/evidence-verdict.md`,
`attack/verification-report.md`, `attack/editorial-verdict.md` — the last three are gate artifacts
and belong to their own legs.

---

## 7. What is still open after this leg — stated plainly, and not papered over

### `F` itself

**OPEN.** Nothing here touches it. The obstruction is unchanged and is not close: any proof of `F`
yields `g_n = O(log² p_n)` unconditionally, the best unconditional bound is `g_n ≪ p_n^{0.525}` and
the best RH-conditional one `≈ √p_n log p_n` — both *powers* of `p_n` where `F` needs
*polylogarithmic* — and there is no induction mechanism, because `g_n` is not constrained by
`g_1 … g_{n−1}`. Round 2 sharpened this formally (Bertrand, the only prime-gap input Mathlib
carries, is **kernel-checked insufficient at every `n ≥ 2`**), analytically (no `C·p^θ(log p)^A`
envelope with `θ > 0` works, for any `C`) and numerically. **Reconciliation removes ambiguity; it
does not narrow this gap by one line.**

### The evidence gate

**Still BLOCKED, and this leg has no standing to clear it.** §1–§3 discharge the three round-2
BLOCKERs *as seams* — the corpus now carries one Theorem C(b), one Axler tier, one set of
denominators, and one set of cross-references. **That is not the same as a clean skeptic run.**
Clearing a skeptic finding is a skeptic's job; a reconciler who marked its own work clean would be
committing the exact error `faults.md` §7 diagnoses. The honest next step is item 1 of §8: **re-run
the skeptic against the amended tree.**

### Seams this leg could **not** close, and what would close each

Named rather than smoothed, per the brief.

1. **Card `L6` — the `2⁶⁴` verification height — is L2_weak and UNOPENED, and it is load-bearing in
   both branches of Theorem C.** Both C-a′ (via `g_{n₀} > 1919`, which is what licenses the `10⁸`
   small branch and therefore the whole `0.93961 → 0.94970` improvement) and C-b′ (same mechanism at
   `6 690 557`) consume it, mediated through Kourbatov because `oliveira2014goldbach` returned
   HTTP 403 to the round-2 fetch. **What would close it:** opening Oliveira e Silva–Herzog–Pardi at
   the locator, by a route that gets past the paywall. Until then no sentence containing "Theorem C"
   may also contain "unconditional" without naming `L6` in the same breath. **This is the largest
   remaining provenance exposure in the corpus, and it is larger than anything decisions 1–5
   touched.**
2. **`granville1995cramer` is L1 at preprint pagination, and it is the load-bearing citation of the
   entire refutation-side argument** (the `limsup g_n/log² p_n ≥ 2e^{−γ} ≈ 1.1229 > 1` tension that
   is the strongest reason to doubt `F`). Untouched by rounds 2 and 3. **What would close it:**
   re-expressing every locator against the journal copy. **Audit priority 1** now that Axler is
   open.
3. **No citation audit has been run on the round-2 corpus at all** — the only one on disk is a
   round-1, paper-side audit that itself returned **BLOCKED** (two of `paper.tex`'s citekeys traced
   to no ledger row; both have since been added to the ledger §2.8 with a standing re-audit
   obligation, which is not the same as audited). **What would close it:** a citation-audit leg on
   the round-2 tree, Granville first, `L6` second.
4. **Every high-precision certificate in the corpus is 50–60-digit floating point, not interval
   arithmetic** (UVR G6; and R2-m3 for the one constant whose margin is only `2.4·10⁻⁸`). **What
   would close it:** a certified-arithmetic pass, which is a funded leg.
5. **`P6′-rec`'s empirical base is 29 record steps.** A statement with 29 data points must not be
   described as robust, and `gov ∧ rec ⟹ min` is the chain that needs it. **What would close it:**
   proving it, or measuring it as a first-class obligation over a real range.
6. **The residual analytic window is genuinely open mathematics, not a lookup.** Inside the
   `0.176 %` sliver the sandwich is useless by construction; closing it needs an **upper** bound on
   `π(p_m + y) − π(p_m)` within a factor `1 + 2/L` of the truth, where Brun–Titchmarsh gives only a
   factor `2`. **What would close it:** a short-interval prime-count theorem of Cramér strength —
   i.e. new mathematics, and the reason no amount of reconciliation reaches it.

### One seam this leg closed in the *unexpected* direction, recorded because it is the finding

Decision 3's premise was false. The brief said the ledger amendment never landed; the tree says it
did. **Two prior legs — a skeptic and a synthesizer, one round apart — reached the wrong state of
the same file by reading a report instead of the tree**, and the synthesizer caught itself doing it.
The generalisable lesson, which belongs in the next loop's brief rather than in this file: **a leg's
claim about the state of a file is not evidence about the state of that file.** `git show` is.

---

## 8. What a next run should do

| # | Action | Why |
|---|---|---|
| 1 | **Re-run the skeptic against the amended tree.** Nothing else. | The three round-2 BLOCKERs are seams and are now closed *as seams*; only a skeptic leg can convert that into a gate reading, and this leg explicitly does not. Feed it this file so it audits the **decisions**, not just the arithmetic |
| 2 | **Citation audit on the round-2 corpus** — `granville1995cramer` first, card `L6` second | Both are load-bearing and unopened; Axler is done; the only audit on disk is round-1, paper-side, and BLOCKED (§7) |
| 3 | **Open `oliveira2014goldbach`** (or find another L0 route to the `2⁶⁴` height) | §7 item 1: the largest remaining provenance exposure, and it sits under *both* branches of the corpus's headline theorem |
| 4 | **Rewrite `paper/paper.tex` against round 2 + this reconciliation, do not patch it** | It is a round-1 artifact asserting a tier that is now wrong (*"Axler … not opened"*) and constants that are now superseded — including `0.99553`, which decision 1 retires |
| 5 | Attack the residual window (§7 item 6) as a short-interval prime-count problem | The one genuinely-open analytic node either round isolated exactly, with the criterion `1 + 2/L` in closed form |
| 6 | Formalize the smooth model (`L4`) in Lean | Still the only node in the formalization plan that is a real theorem within Mathlib's reach, and still not done after three rounds |
| 7 | **Do not fund another proof-attempt fan-out, and do not fund more sieving** | Sieving buys the next maximal gap and nothing between; the record that matters is 4.2 decades away. And the fan-out is what produced every finding this leg had to reconcile |
| 8 | **Amend the loop's write rule.** Rule 6 (*"round K writes only under `attack-round-K/`"*) is incompatible with a reconciliation stage and must carry an explicit exemption for it | R2-m5, generalised: the stage that owns seams must be allowed to edit the artifacts that carry them, or it can only publish a fifth opinion |

**Standing instruction, unchanged through three rounds.** The conjecture is open. Do not write
"Firoozbakht is true". Do not write "Firoozbakht is false". The defensible sentence remains:
*Firoozbakht's conjecture is numerically robust over the verified range and simultaneously
incompatible with the standard Cramér–Granville heuristic; at least one of the two must fail, and no
current technique can say which.*

---

## 9. Verification of this document

**What this leg computed itself.** `attack/reconcile_recount.py` → the table of §4, plus
`π(10⁹) = 50 847 534` from an independent segmented sieve, plus the maximal-gap record enumeration
to `2·10⁸` (28 records; `15 683` twelfth, `191 912 783` twenty-eighth) that adjudicates R2-m1, plus
the four headline exponentials at 40 dps:

| quantity | this leg's value | used for |
|---|---|---|
| `e^{−0.0017569}` | `0.9982446424453653…` | C-b′'s headline `0.998244`; **confirms** FFM's `0.998244` and the correction of its printed `0.99824467…` |
| `e^{−0.0043636}` | `0.9956459066696853…` | C(b\*)'s retired `0.99565` |
| `e^{−0.0516}` | `0.9497086743460633…` | C-a′'s `0.94970` |
| `log 6 690 557` / `log 1 772 201` | `15.7162076872…` / `14.3877328348…` | the two legs' `ℓ_A` / `ℓ₁` |

**What this leg took second-hand, and from whom.** Every PDF-level provenance fact (the MD5s, the
14-vs-12-column tables, the corrigendum text, the edition numbering) rests on the FFM leg's fetch
**and** the round-2 skeptic's independent re-fetch, which agree; this leg opened no source. Every
Lean gate status rests on the round-2 skeptic's **re-execution**; this leg ran no `lake`. R2-m6's
and R2-m7's figures rest on the round-2 skeptic; this leg did not re-derive them, and says so at
each site. The verification that both repaired Theorem C(b)'s are mathematically correct rests on
the round-2 skeptic's 40–50-dps re-derivation — **this leg's decision between them is a provenance
decision, not a re-verification**, and that is exactly why it could be made without opening
mathematics.

**What this leg checked in the tree rather than in a report.** The full state of
`attack/source-ledger.md`'s Axler row and §6 gap 3, card `T1`'s Axler block and hazard section,
card `L15`'s four disputed numbers, and every string this document claims to have edited (`grep`
after each edit). §3 is entirely a tree check.

**Consistency against the brief.** Five decisions asked, five delivered and recorded: one Theorem
C(b) (§1), one Axler tier (§2), the ledger amendment (§3 — reported honestly as *already landed*,
with the evidence, rather than re-applied), the recount from the statement (§4 — which contradicts
FFM and re-confirms `proof-attempt-0.md` against two prior skeptics), and the cross-reference layer
(§5). R2-M2 and R2-M3 did **not** survive decisions 1–4 untouched and are applied, as are all seven
MINORs in some form (§5's table). Every seam that could **not** be closed is named in §7 with what
would close it. **No seam was resolved by preferring the leg that wrote more** — decision 1 goes
*against* the longer document's own theorem on a documentary ground, and decision 4 goes against the
document that declared the matter settled.

---

*Artifact of leg `reconcile`, molecule `task-20260727-264e`, run `germ-20260725-791a7c45`, **round
3**. This is not a proof and not a gate. It is the removal of ambiguity that a `write-paper` leg
would otherwise have had to guess at. Every number in it is either this leg's own computation
(`attack/reconcile_recount.py`) or explicitly attributed to the leg it came from. **The conjecture
`F` remains OPEN. The evidence gate remains BLOCKED.***
