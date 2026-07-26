# editorial-verdict.md — fail-closed editorial gate on the Firoozbakht paper

**Molecule:** `review-20260726-7d55` (formula `temp-review`, crew role: **reviewer**) — **ROUND 2**
**Run:** `germ-20260725-791a7c45` · **Re-attack loop:** `reattack-20260726-57d1` · **Date:** 2026-07-26
**Target:** `paper/paper.tex` (2460 lines, v5) + `paper/references.bib` (22 entries) + `paper/paper.pdf`
**Conjecture (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`. **`F` is OPEN.**
Nothing in this verdict proves or refutes it, and nothing in the paper claims to.

**This document supersedes, in place, the round-1 `editorial-verdict.md` of the same name**
(molecule `review-20260725-4b9d`, 25 July 2026). Round 1 scored a 1641-line paper on three
failing checks; this scores the 2460-line round-2 rewrite. **One of round 1's three REWRITE
reasons is gone, one is fixed, one remains, and one new one has appeared.** §5 states exactly
what changed and what did not — read it before quoting either document.

**Author ≠ scorer.** This leg wrote no line of `paper.tex`. Every finding below is a score for
the author to act on, not an edit made on their behalf. Where a claim must change, that is a
REWRITE instruction, not an edit made here.

---

## VERDICT: **REWRITE**

Two failing checks, in descending order of consequence:

1. **The evidence gate is BLOCKED.** `attack/evidence-verdict.md` (round 2) reads
   `VERDICT: BLOCKED`, failing leg **SKEPTIC round 2**, on three unresolved BLOCKERs
   (R2-B1, R2-B2, R2-B3). This is **not** an honest DEGRADED: the DEGRADED carve-out exists for
   a degraded *kernel* leg, and the kernel leg here passes **outright**
   (`formal_backend = 'lean'`, not `'none'`; `lake build` exit 0; exactly one `sorryAx`
   dependent over 63 declarations). Fail-closed rule: SHIP requires PASS or honest DEGRADED.
   **This alone forecloses SHIP, independently of everything else below.**
2. **Two OVERCLAIM rows**, both about the paper's own methodology rather than about `F`:
   - **V2** — the paper states **four times** that no citation audit has been run for it and
     that "no round-2 audit exists". `attack/verification-report.md` is committed at `51756c5`
     (after the paper's own `d33dfe0`), audits this exact `paper.tex` v5 by an independent leg,
     and returns **PASS**. Four sentences are false about the galaxy's committed state.
   - **V3** — §1.5 promises that the word *proved*, unqualified, is reserved for `[K]`
     statements "without exception". There are at least five exceptions, and the first is in
     the **abstract**, where the confidence labels are not visible to the reader.

**Zero UNSUPPORTED-CITATION. Zero UNADDRESSED-FAULT.** The citation gate is **PASS**, and every
BLOCKER and MAJOR the round-2 skeptic raised is addressed in the paper at its point of use.
**The mathematics survived every check this leg could run** — see §1 and §2.

**Delivery posture is not this gate's call.** REWRITE is a verdict on the artifact against the
gate rule, not a recommendation about whether or where the operator stages this paper.

---

## 1. Per-claim verdict table

The full 100-row ledger is `attack/claims-ledger.md` (committed at `607c416`). Reproduced here:
every non-CONFIRMED row, plus the load-bearing CONFIRMED rows a reader needs in order to see
what the REWRITE does *not* touch.

| Claim | Tag | Evidence |
|---|---|---|
| **V1** — The corpus's evidence gate stands at BLOCKED, and the paper reports this accurately (abstract; §1.4; §7.3 box; Acknowledgements) | **gate failure** (not a claim defect) | `attack/evidence-verdict.md`: BLOCKED, failing leg SKEPTIC round 2, three unresolved BLOCKERs. The kernel leg passes outright, so the honest-DEGRADED carve-out does not apply. The paper's *reporting* of the gate is exact; the *gate* is what fails. |
| **V2** — "The citation audit for this paper has not been run… no round-2 audit exists" (§7.4 l.2350–2352); "no citation clearance exists for this paper" (abstract l.97); "in either round" (§1.4 l.268); "for which no citation clearance exists" (Acknowledgements l.2454) | **OVERCLAIM** — unsupported assertion of a negative fact | `attack/verification-report.md`, molecule `cite-20260726-d5a8`, commit `51756c5`: **PASS**, 22/22 citekeys, 91/91 `\cite` instances locator-matched, 0 at L3, 0 fabricated, 0 orphans. Note the direction — this **understates** the paper's provenance. It is nonetheless a false assertion inside the one section whose entire purpose is accurate provenance reporting, and it is the section a downstream reader will quote. |
| **V3** — §1.5: "The word *proved*, unqualified, is reserved in this paper for statements carrying `[K]`… we use it without exception" | **OVERCLAIM** — the rule has exceptions | Five breaches, all on `[P]`/`[P·s]` results: l.74 (**abstract**: "the two survivors are **proved** formally incomparable" — Prop. `prop:incomparable` is `[P]`), l.980, l.1203, l.1385, l.2391. Mitigating, so the REWRITE is correctly sized: each sentence carries a `\ref` to a labelled statement displaying its own confidence code, and none inflates `F`'s status. The defect is that the paper's most load-bearing methodological promise is not kept, and its first breach is where the labels cannot be seen. |
| K1 — Lemma 2.1: `F ↔ (∀n ≥ 1, g_n < T_n)`, **machine-checked** `[K]` | **CONFIRMED** | evidence-verdict §1 KERNEL **PASS**: `lake build` exit 0 (2208 jobs), audits exit 0/0, 63 declarations, exactly 1 `sorryAx` dependent (the conjecture), 1 live `sorry` token, grep-clean of `native_decide`/`axiom`/`unsafe`, `Statement.lean` SHA-256 byte-identical before and after, independently re-run by the round-2 skeptic. |
| K2 — Thm 3.1: Bertrand's postulate, the only prime-gap bound Mathlib carries, is insufficient at **every** `n ≥ 2`, `[K]` | **CONFIRMED** | `lean/Firoozbakht/Barrier.lean`, three `sorry`-free theorems; a machine-checked *negative-capability* result, and the paper says so ("the best available tool proves its own insufficiency"), never as a step toward proving `F`. |
| S1 — `F` is open; neither proved nor refuted in either round | **CONFIRMED** | Asserted in the abstract, §1.4, §1.5 box, §7.1 and §10, and matched by every upstream artifact. |
| R7 — the round-1 F2 defect: the printed bound "does not follow from its stated justification", wrong by a factor **38.813747…** | **CONFIRMED** | **Independently recomputed here: `0.169339812744…/0.004362882388… = 38.8137468958056…`**, matching every printed digit. This is the round-2 brief's F2, repaired *and* correctly denominated. |
| R5/R6 — Thm C(a) `p_m ≤ 0.94970 p_{n_0}`, Thm C(b) `p_m ≤ 0.998244 p_{n_0}`, `[P·s]` | **CONFIRMED** | **Recomputed here at 30 dps:** C(a) majorant max `0.0515990266817599…` on the first cell (`ℓ = 18.4206807439…`) `< 0.0516`; C(b) majorant max `0.00175687590387332…` at the cell beginning `ℓ = 24.4062076872…`; `e^{−0.0516} = 0.949708674346…`, `e^{−0.0017569} = 0.998244642445…`. Both algebraic expansions re-derived by hand and matching. |
| R8 — the retired second repair (`v := ℓ²−ℓ−1−1/ℓ`, `0.995645906670…`) is correct but **not carried**, because its Axler row exists in the preprint edition only | **CONFIRMED** | **`e^{−0.0043636} = 0.995645906669685…` verified here.** The paper states that it is *choosing*, and why — R2-B1/R2-B3 addressed, not smoothed. |
| H1/H2/H3 — `√x > (25/22)log x` (min `0.40686238165947680…`); arithmetic clearance `A = {1,2,3}`; the CMS envelope certifies at **exactly one index of the range where the bound is available** | **CONFIRMED** | **Recomputed here: `h(625/121) = 0.4068623816594768065…`; all eight rows of the clearance table reproduce to the 11 printed digits.** Round 1's "at no other index whatsoever" is explicitly withdrawn as false, with the quantifier restored and the reason named. |
| H6/H7 — the critical constant on the `√p log p` scale is exactly `2/e = 0.7357588823428846…`; certifying to `2^64` would need `C ≤ 1.009·10⁻⁸` | **CONFIRMED** | **Verified here**, including that both published constants (`22/25`, `21/25`) lie *above* `2/e` and therefore give the empty set. |
| C2/C3/C6 — the sweep to `10^11`: 4 118 054 812 pairs, 0 violations, `max_{n≥10} ρ_n = 0.8317570`; the `10^9` re-sweep at 50 847 533 indices; the disputed denominator `216 806` | **CONFIRMED**, and independently adjudicated | **This leg ran its own sieve to `10^9`: `π(10^9) = 50 847 534` (⇒ 50 847 533 consecutive pairs ✓), zero violations of `F`, `max_{n≥10} g_n/T_n = 0.78960` at `n = 1 319 945`, `p = 20 831 323` — strictly below the paper's `10^11` record and attained below its argmax, as it must be. And `π(3·10^6) = 216 816`, so the three-way denominator dispute resolves in the paper's favour: `216 815` steps, `216 806` with `n ≥ 10`; the upstream concept card's `216 805` is the wrong one.** |
| L5/L6/L7 — the three round-2 BLOCKERs R2-B1 (two incompatible correct repairs), R2-B2 (contradictory source tiers plus an unlanded ledger amendment), R2-B3 (an edition-fragile citation) | **CONFIRMED** — addressed, not resolved upstream | Each is stated in §7.3 *and* at its point of use, with "neither upstream document has been amended" said plainly. Addressing ≠ resolving, and the paper does not pretend otherwise. |
| P6/R10/C8 — the three round-2 MAJORs R2-M3 (`gov`/`min` incomparable, prose calls one weakest), R2-M2 (the "unconditional" label resting on an unopened height), R2-M1 (off-by-one denominators) | **CONFIRMED** — all three addressed | Rem. `rem:notweakest`, Caveat `haz:uncond`, Caveat `haz:5592` respectively. |
| L11/L12 — ledger composition 13 L0 / 4 L1 / 3 L2_strong / 2 L2_weak / **0 L3**; the two rows the author leg folded outside its remit carry a standing re-audit obligation | **CONFIRMED**, and now improved | citation-gate §2 gives exactly 13/4/3/2/0; §1.20–1.21 re-verify every locator of `carneiro2019fourier` and `visser2018andrica` against the ledger's §2.8 — an *independent* leg has now checked what the author leg did not. |
| All 22 citekeys (`firoozbakht1982unpublished` … `visser2018andrica`) | **CONFIRMED** — 22/22 | `attack/verification-report.md` **PASS**: 91/91 instances locator-matched, 59 unique (citekey, locator) pairs, 0 at L3, 0 fabricated, 0 orphans in either direction, and every L1/L2 tier caveat carried into the paper's running text rather than smoothed upward. **Zero UNSUPPORTED-CITATION.** |

**Tally: 97 CONFIRMED · 2 OVERCLAIM · 0 UNSUPPORTED-CITATION · 0 UNADDRESSED-FAULT · 1 gate
failure (V1, which is a property of the corpus, not a row the paper got wrong).**

---

## 2. Fail-closed rule, applied

| Condition for SHIP | Status |
|---|---|
| Zero OVERCLAIM | **FAIL** — two (V2, V3) |
| Zero UNSUPPORTED-CITATION | pass — zero |
| Zero UNADDRESSED-FAULT | pass — zero |
| Evidence gate PASS or honest DEGRADED | **FAIL** — **BLOCKED**, failing leg SKEPTIC round 2; the kernel leg passes outright so DEGRADED does not apply |
| Citation gate verification-report PASS | pass — **PASS** (round 2) |
| `evidence-verdict.md` present | pass |
| `verification-report.md` present | pass |

**⇒ REWRITE.** Two failing conditions; either alone suffices. Never SHIP on a BLOCKED gate.

### What a SHIP would require, named precisely

1. **A reconciliation leg** that clears R2-B1/B2/B3 in the *corpus*, not only in the paper —
   land the ledger amendment once, retire `Theorem C(b*)` upstream, write the edition flag into
   the artifact that depends on it, cross-cite the four round-2 artifacts — and a skeptic leg
   that re-confirms a zero-BLOCKER state. The round-2 skeptic's own §7 says the same thing, and
   the paper's Rem. `rem:structural` predicts that more rounds *of this shape* will not deliver
   it. This is editorial work, not mathematics.
2. **Four sentences deleted or rewritten** (V2): the abstract's "no citation clearance exists
   for this paper", §1.4's "in either round", §7.4's "has not been run… no round-2 audit
   exists", and the Acknowledgements'. Replace with the round-2 citation gate's actual finding
   — **PASS, 22/22, 0 at L3** — and keep §7.4's priority list, which the gate does not
   discharge: `granville1995cramer`'s preprint pagination and `oliveira2014goldbach`'s
   never-opened 403 remain exactly as load-bearing as the paper says they are.
3. **Either five sentences softened or one promise weakened** (V3): put a confidence code on
   the abstract's "proved formally incomparable" and on the four in-body breaches, or change
   §1.5's "without exception" to a rule about *theorem statements* rather than *all prose*.
   The second option is one line and is the honest one, since the breaches are ordinary
   mathematical English and not strength inflation.

**Nothing in this list is mathematical.** No constant in the paper comes from a broken
derivation; this leg recomputed every recomputable one and they all hold.

---

## 3. Tracked-delivery contract — verified across the whole run

| Required | Present | Committed |
|---|---|---|
| `attack/` | 118 files + this verdict and `claims-ledger.md` | ✓ |
| `paper/paper.tex` | 2460 lines | ✓ |
| `paper/references.bib` | 22 entries | ✓ |
| `paper/paper.pdf` | 341 645 bytes (a toolchain was present) | ✓ |
| `trace/` | 4 files (`briefs.md`, `build_trace.py`, `events.jsonl`, `hashes.tsv`) | ✓ |
| `lean/` | 13 files | ✓ |
| `corpus/` | 37 files | ✓ |

`git status --short` is **empty** — nothing merely-untracked, nothing dirty. **The
tracked-delivery contract holds; it is not a REWRITE reason.**

---

## 4. DISSENT

*(Required. An editorial verdict with no dissent section blocks promotion. What follows is
this leg's own disagreement with the frame it was handed, not a summary of the above.)*

### D1 — The gate rule scores the corpus and calls it a score on the paper, and here the two point in opposite directions

The fail-closed rule fires on `evidence-verdict.md`, which is a verdict on the *corpus*. But the
artifact being scored is the *paper*, and this paper's central editorial act is **disclosing
that the corpus is blocked** — in the abstract, in §1.4, in a boxed statement in §7.3, and in
the Acknowledgements, with all three BLOCKERs named and the honest reading ("the count went up,
and the species changed") stated rather than buried. The paper is *better* for reporting the
BLOCKED gate, and the gate rule returns REWRITE *because of* the state the paper is being
praiseworthy about reporting.

That is not an argument for changing the verdict — a rule that bends when the prose is gracious
is not a gate. But it exposes a real gap in the instrument: **there is no verdict for "an honest
report on a blocked corpus," which is precisely what this artifact is and says it is.** SHIP and
REWRITE are the only two words available, and neither fits. The paper anticipated this and
coined its own third word — *"This paper is an honest report on a blocked corpus. It is not a
seal."* Round 3's most useful editorial increment might be to give the gate that word, rather
than to have every honest failure report score the same as a paper that hid one. Compare what
the rule would have said about a paper making the same claims and *omitting* §7.3 entirely:
REWRITE, on the same gate line, for the opposite reason. An instrument that cannot distinguish
those two is measuring the corpus and reporting it as a measurement of the paper.

### D2 — The V2 finding is the corpus eating its own tail, and it recurred exactly as round 1 predicted

The paper says "no round-2 citation audit exists". It was true when the sentence was written and
false three commits later, because the audit is a *downstream* leg — the paper cannot describe
its own citation clearance without describing the future. This is not carelessness; it is a
structural consequence of a pipeline in which the artifact that must report its provenance is
built before the leg that certifies it.

And it is the **same species** as the three BLOCKERs the paper itself names: a seam between
artifacts that no leg owns. Round 1's review flagged this exact sentence pattern. Round 2's
author fixed the *other* self-description defect round 1 found (the false universal about
citations) and left this one, where it multiplied from two occurrences to four. So the
prediction in Rem. `rem:structural` — *"more rounds of this shape will not converge"* — is
corroborated by this review leg's own findings, in the crispest possible way: **the reviewer's
principal new finding against round 2 is a recurrence of the reviewer's finding against
round 1.** I record that as evidence for the paper's structural claim, made by a leg that had
every incentive to find something new instead.

### D3 — I dissent from my own V3, on severity

V3 is scored OVERCLAIM because the paper's rule says "without exception" and there are
exceptions. Judged as mathematics, this is nearly nothing: "the two survivors are proved
formally incomparable" is *correct* — Prop. `prop:incomparable` proves it, at ordinary
mathematical standards, and the sentence cross-references a labelled statement whose confidence
code is `[P]`. No reader is misled about `F`.

But I let the row stand at OVERCLAIM, and the reason is worth stating because it cuts against
the paper: **a self-imposed discipline announced in bold and then not kept is worse than no
discipline announced.** The paper's whole rhetorical strategy is that its labels can be trusted
absolutely, which is what licenses a reader to skim `[P]` and `[K]` instead of re-deriving. A
rule with five silent exceptions withdraws that license without saying so. The cheapest honest
repair is to weaken the rule to what the paper actually does — reserve the *unqualified* claim
of proof for theorem *statements*, and let running prose speak English.

### D4 — The most interesting tension in the work is not editorial at all

Setting the gate aside: the substantive tension this paper surfaces and cannot resolve is that
its two strongest results point in opposite directions about whether the attack was worth
running. The **Bertrand barrier** (`[K]`, machine-checked) and the **`2/e` critical constant**
(`[P]`, Lambert-`W`, exact) are both *negative-capability* theorems — each proves that a tool
cannot reach the target, and each is fully rigorous. They are the sharpest things in the paper.
Meanwhile the mathematics the run was actually pointed at — proving `F` — moved the `sorry`
count from 1 to 1.

The honest reading, which the paper gestures at but does not state, is that **this attack's
comparative advantage turned out to be proving impossibility, not possibility**, and that a
round 3 aimed at `F` would be worse-directed than a round 3 aimed at cataloguing barriers. That
is a strategic claim about where to spend, and it is outside a paper's remit to make — which is
exactly why a dissent section is the right place for it.

---

## 5. Round 1 against round 2 — what changed, and what did not

**Changed — one REWRITE reason removed, one fixed:**
- **The citation gate went BLOCKED → PASS.** Round 1's first and heaviest REWRITE reason was a
  BLOCKED citation gate naming `carneiro2019fourier` and `visser2018andrica` as tracing to no
  ledger row (12 of 86 instances). Ledger §2.8 now carries both, and an independent leg
  re-verified every locator invoked. **That reason is gone.**
- Round 1's OVERCLAIM "a universal about its own citations that is false" is **fixed**: the
  paper's ledger-composition claim (13/4/3/2/0) now matches the citation gate exactly.
- Round 1's two BLOCKERs are both repaired and reproduced here: **F1** (the three inequivalent
  `m(n)` predicates — now named apart in symbols as `(P6′-pair)`, `(P6′-gov)`, `(P6′-min)`, with
  a fourth `(P6′-rec)`, the strongest **refuted** with two witnesses) and **F2** (the factor-`38`
  bound — restated tight as `v(1+v/x)`, re-derived twice independently, factor `38.8137468958…`
  reproduced here to every printed digit).
- The paper roughly doubled (1641 → 2460 lines), and every new headline result — the Bertrand
  barrier, the restored RH quantifier, the `2/e` determination, first-failure maximality —
  verified clean against independent recomputation.

**Did not change:**
- **The evidence gate is still BLOCKED, so the verdict is still REWRITE.** The reason migrated
  from unrepaired mathematics (F1, F2) to unreconciled repairs (R2-B1/B2/B3). The paper argues
  this is a worse signal rather than a better one, and this leg agrees: mathematical errors get
  fixed by mathematicians, and seams do not get fixed by widening the fan-out.
- **`F` is OPEN.** Neither round proved or refuted it, and nothing here is evidence that either
  is close.
- The "citation audit has not been run" self-description survived the rewrite and is now
  **false** rather than merely stale (V2) — the one place where round 2 is worse than round 1.

---

*Artifact of leg `review` (step 3), molecule `review-20260726-7d55`, run
`germ-20260725-791a7c45`. Supersedes the round-1 `editorial-verdict.md` in place, so the galaxy
carries exactly one current editorial answer. Sources read: `paper/paper.tex`,
`paper/references.bib`, `attack/evidence-verdict.md`, `attack/verification-report.md`,
`attack/re-attack/attack-round-2/faults.md`, `attack/faults.md`,
`attack/re-attack/reattack-verdict.json`, `attack/source-ledger.md`. Full row-by-row scoring in
`attack/claims-ledger.md`. Every "verified here" figure was recomputed by this leg at 25–30
decimal digits or by its own independent sieve; no number in this document was copied from the
artifact it scores.*
