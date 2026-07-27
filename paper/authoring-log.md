# Authoring log — `paper/paper.tex`

**Molecule:** `edit-20260727-ace7` (formula `editorial-work`, crew role: writer) — **ROUND 3**
**Run:** `germ-20260725-791a7c45` · **Re-attack loop:** `reattack-20260726-57d1` (rounds 1–2;
round 3 ran outside its cap)
**Date:** 2026-07-27
**Source of record:** `attack/synthesis.md` (round 3, **v2**, molecule `task-20260727-4709`),
read together with the two artifacts it rests on and defers to:
`attack/reconciliation.md` (round 3a, `task-20260727-264e`) and `attack/faults.md` (round 3b,
`task-20260727-5096`, **the corpus's single current fault list**). Where those two contradict an
earlier artifact, they are authoritative; where 3b contradicts 3a, 3b is authoritative. Also read:
`attack/evidence-verdict.md` (v2), `attack/verification-report.md`, `attack/editorial-verdict.md`,
`attack/claims-ledger.md`, `attack/source-ledger.md`.
**External attribution:** Noogram. **Delivery posture:** staged.

> **This file supersedes the round-2 authoring log of the same name, in place**, exactly as the
> paper it describes supersedes the round-2 `paper.tex` (molecule `edit-20260726-5e79`) in
> place. The galaxy carries exactly one current artifact of each name. §0 states what changed;
> everything after it describes the round-3 artifact, so that nothing in this directory
> describes a round the run has moved past.

---

## 0. What changed versus round 2, and what did not

**The headline, stated first so it is not over-read: round 3 opened no mathematics, and this
revision adds no theorem.** Every theorem, lemma, proposition, corollary and constant in
`paper.tex` is round-2 mathematics. What round 3 contributed is *adjudication* (five decisions on
seams round 2 had left between its own artifacts), *independent re-derivation* (twelve of round
2's thirteen review findings closed by recomputation from the statements, not by re-assertion),
and *two new findings about the corpus's accuracy about itself*. This paper's round-3 edition is
therefore a supersession on three axes: corrected inherited numbers, corrected self-description,
and a rewritten disclosure section.

### 0.1 Changed — numbers and labels inside the mathematics

| Site | Round 2 | **Round 3** | Origin |
|---|---|---|---|
| Thm. `thm:pairfalse`, witness W2 | gap `248` at `p = 191 912 783` called the **27th** maximal gap | **28th**, with a new remark giving the enumeration (28 records below `2·10⁸`, `15 683` twelfth, 25 records below `10⁸`) and a new verification item **V14** | R2-m1; four independent enumerations agree |
| Caveat `haz:census` | census counts *indices*, not *pairs* — stated, but the pair count was missing | pair count supplied (**20** below `3·10⁸`) and an explicit prohibition on reading any ratio as a density, with the reason: the admissible-pair count below `10⁹` is of order `10¹⁵` | R2-m2 |
| Rem. `rem:notweakest` | *"The upstream prose has not been amended"* | amended at the three sites the fault named, with `P6′-gov` restored to the canonical obligation list and `P6′-rec` beside it; two further sites still carry the word and are named in §`sec:defects` | R2-M3 / S3-m1 |
| Thm. `thm:ffm`, consequence 3 | `P6′-rec` reported as "0 exceptions" alongside the other two | the asymmetry stated: `gov`/`min` at 50 847 533 indices, **`rec` at 29 data points**, which must not be described as robust | reconciliation §7 item 5 |
| Rem. `rem:margins` | the `P6′-gov` margin *"decays like `p^{−0.83}`"* | the single fitted exponent is withdrawn as non-extrapolable; local per-decade exponents `0.4538 / 0.7364 / 0.9967` given, extrapolation corrected `≈3.4·10⁻¹³ → ≈6.1·10⁻¹⁵`, direction noted as **safe** | R2-m6 |
| Caveat `haz:5592` | three independent recounts; *"the concept card still carries the disputed denominator"* | **seven** independent recounts; the **self-consistency argument** that closes the dispute outright (`121 238 / 216 805` is the answer under *no* convention); range dependence at three decades tabulated; the cards are corrected, one frame document still is not | R2-M1, adjudicated in reconciliation §4 and re-derived in faults §1 |
| §`sec:oscillation` table | two rows (`3·10⁶`, `10⁹`) | four rows (`3·10⁶`, `10⁷`, `10⁸`, `10⁹`), both conventions | same |
| **new** Caveat `haz:margin` | — | Thm. `thm:Cb`'s certified constant clears its own majorant by **`2.40·10⁻⁸`**; the majorant is grid-robust (`0.00175687590387 → 0.00175687597478` under a fine scan); closing it needs interval arithmetic, not a sharper float | R2-m3, plus the round-3 synthesis's grid-robustness check |
| Caveat `haz:axler` | two editorial hazards, tier stated as improved | + **round-3 status**: tier settled **L0** corpus-wide, residual exposure is *edition* not tier — and the settlement reached one artifact out of seven | Decision 2 / S3-B1 |
| Rem. `rem:retired` | *"the corpus contains no rule for choosing; this paper chooses"* | + the corpus has now chosen, and chose the same theorem on the same documentary ground; the retired figures may appear only as history | Decision 1 |
| Caveat `haz:uncond` | the label is too strong; the honest form given | + the dependence **traced**, not assumed: the `0.93961 → 0.94970` improvement comes *entirely* from the `10⁸` cutoff that the `2⁶⁴` height licenses, and the same height sits under both branches — so this is the paper's largest single exposure | R2-M2 / synthesis §4.5 |
| §`sec:limits` "most tractable node" | two further nodes | three: `P6′-rec`'s 29-point base, the unformalised smooth model, and the interval-arithmetic replacement of `thm:Cb`'s certificate | reconciliation §7 |

**No constant changed value.** Every figure the round-2 paper carried survives round 3's
recomputation, including the two the corpus had disputed: `121 238 / 216 806` and
`121 239 / 216 815` are vindicated against two prior review verdicts, and `0.998244` is the
designated theorem.

### 0.2 Changed — self-description, which is where round 2 was faulted

The round-2 editorial gate returned **REWRITE** on two OVERCLAIM rows and one gate failure. Both
OVERCLAIM rows are repaired here; the gate failure is not this leg's to repair and is reported
rather than smoothed.

- **V2 — the false negative about the citation audit.** Round 2 asserted in four places
  (abstract, §1.4, §7.4, Acknowledgements) that no citation audit had been run for this paper and
  that *"no round-2 audit exists"*. **`attack/verification-report.md` is that audit, it audits
  this exact paper, and it returned PASS** — 22/22 citekeys, 91/91 `\cite` instances
  locator-matched, 59 distinct (citekey, locator) pairs, zero at the recall tier, zero fabricated,
  zero orphans. All four sentences are corrected. §`sec:provenance` is retitled and rewritten: it
  now states the audit's finding, states the *origin* of the false sentence (an honest snapshot,
  true when committed at 21:45 and false eleven minutes later at 21:56, that nobody refreshed),
  and gives three reasons why **no citation clearance is nonetheless claimed** — the audit
  predates the round-3 decisions; a PASS carrying its caveats does not discharge them; two
  load-bearing sources remain under-opened.
- **V3 — the unkept methodological promise.** Round 2 promised the bare word *proved* would be
  reserved for `[K]` statements *"without exception"*, and breached it five times, first in the
  abstract where the codes are invisible. The editorial gate offered two repairs and named the
  one-line one as the honest one; that is the one taken. §`sec:vocab` now states the rule the
  paper actually keeps — every labelled statement carries in its heading either its confidence
  code or the word *cited* (the latter for the two results imported wholesale rather than derived
  here), and nothing is asserted above its code anywhere, while running prose speaks ordinary
  mathematical English and cross-references the labelled statement that governs it — and **records the withdrawal of the
  round-2 promise explicitly** rather than silently narrowing it. The abstract's breach is also
  independently defused (`proved formally incomparable` → `formally incomparable, by an explicit
  four-index counter-model in each direction`), so the claim now carries its own evidence.

### 0.3 Changed — the disclosure section (§`sec:defects`), rewritten

Round 2 disclosed three unreconciled seams and said *"neither upstream document has been
amended"* of each. All three are now closed, and the section is restructured into: round 2's
three seams **and how each was closed**; the twelve-of-thirteen disposition of round 2's review
findings; **round 3's two new blocking defects**; the sub-blocking residue, itemised; the boxed
gate statement; and `rem:structural`.

`rem:structural` is the paragraph that changed most, and deliberately. Round 2's edition
predicted that *"more rounds of this shape will not converge"* and that the missing increment was
one editorial reconciliation pass. **That prediction was tested.** The pass was funded, ran,
closed every seam, reversed two prior review verdicts and its own brief's premise where each was
wrong — and the gate still did not clear, because the pass reproduced, about itself, the class of
error it existed to remove. The remark now says so, states that three consecutive rounds have
failed at the identical step each time in the leg created to fix the previous round's failure at
it, and explicitly discounts the one-leg estimate it offers, on the ground that the same estimate
was offered once before and was wrong.

### 0.4 Not changed

- **`F` is OPEN.** Neither proved nor refuted by any round. The defensible sentence in the
  §`sec:vocab` box is verbatim what it was, and is what both round-3 legs carry as a standing
  instruction.
- **The Lean substrate.** One `sorryAx` dependent over 63 declarations, and it is the conjecture.
  Round 3 wrote no Lean; it re-executed the gates twice, independently, from a cold cache.
- **Every theorem and every proof.** No mathematical statement in the paper was altered, added or
  removed. The `\label` set is unchanged except for the two additions `haz:margin` and V14.
- **The delivery posture:** staged. The evidence gate is **BLOCKED**, failing leg SKEPTIC.
- **The 22 ledger rows and 22 citekeys.** No source was added, removed or re-tiered by this leg.

---

## 1. Toolchain and compile summary

| Item | Value |
|---|---|
| Engine | XeTeX, TeX Live (`/Library/TeX/texbin`) |
| Driver | `latexmk -xelatex -interaction=nonstopmode paper.tex` |
| Bibliography backend | `biber` (present on PATH), `biblatex` style `alphabetic`, `maxbibnames=6` |
| Packages | `amsmath`, `amssymb`, `amsthm`, `booktabs`, `longtable`, `geometry`, `xcolor`, `hyperref`, `biblatex` |
| Passes | xelatex ×3 + biber ×1 + `xdvipdfmx`, converged (`All targets up-to-date`) |
| **Exit status** | **0** |
| **Output** | `paper/paper.pdf`, **43 pages**, 370 194 bytes |
| LaTeX warnings | **0** — no undefined reference, no undefined citation, no multiply-defined label, no `Citation ... undefined` |
| `\cite` instances | 95, over **22** citekeys |
| Bibliography | 22 entries, **0 orphans in either direction** (every `.bib` entry is cited; every cited key is in the `.bib`) |

The toolchain was present, so the built PDF is delivered next to the source as the brief requires;
no "recipient compiles" fallback was needed.

**Citation traceability, re-verified by this leg rather than inherited.** All 22 citekeys were
extracted from `paper.tex` and matched against `attack/source-ledger.md`. Eighteen match the
ledger row name literally. Four — `oeisA111943`, `oeisA182514`, `mathlibNatNth`,
`mathlibNatPrimeNth` — are the BibTeX camelCase forms of the ledger's snake_case row names
`oeis_A111943`, `oeis_A182514`, `mathlib_nat_nth`, `mathlib_nat_prime_nth`; each row was opened
and read in the ledger to confirm the correspondence, and the ledger itself carries the BibTeX
form (`@misc{mathlib_nat_prime_nth, …}` at `source-ledger.md:1043`). **Every `\cite{…}` in this
paper traces to a ledger row. No key was added by this leg.**

---

## 2. Coverage of the brief, point by point

| Brief requirement | Where | Status |
|---|---|---|
| LaTeX mandatory, `\documentclass{article}`, `amsmath` + `amsthm` + `hyperref` | `paper.tex` preamble | ✅ |
| theorem / lemma / definition / proof environments | `\newtheorem` block; **77** numbered statements sharing one counter — 15 theorem, 13 lemma, 9 proposition, 4 corollary, 3 definition, 19 remark, 14 caveat | ✅ |
| every proof opens with an italic *Idea:* line | `\idea{…}` macro; **32 proofs, 32 `\idea` lines** — counted, so the correspondence is exact and not assumed | ✅ |
| citations via `biblatex` over `references.bib` | `backend=biber`, `\addbibresource{references.bib}` | ✅ |
| every `\cite{key}` traces to a source-ledger row | §1 above, re-verified by this leg | ✅ 22/22 |
| abstract | present | ✅ |
| intro + literature | §1, with §`sec:lit` in five groups | ✅ |
| setup | §2 | ✅ |
| main results | §3–§8 | ✅ |
| computational evidence | §9 | ✅ |
| honest limitations | §11, incl. §`sec:defects`, §`sec:provenance`, §`sec:limits` | ✅ |
| references | `\printbibliography` | ✅ |
| compile with `latexmk -xelatex`, deliver `paper.pdf` | §1 above | ✅ exit 0 |
| toolchain + compile summary recorded here | §1 | ✅ |
| delivery posture: staged | Acknowledgements, stated | ✅ |
| external attribution: Noogram | title block + Acknowledgements | ✅ |
| claim *proved* only where the kernel leg established it | §`sec:vocab`, rewritten (V3) | ✅ |
| **round-3 resumption**: read `reconciliation.md` + the NEW `faults.md` first, treat as authoritative | header of this file; both read in full before any edit | ✅ |
| produce the round-3 state, superseding the artifact of the same name **in place** | `paper.tex` and this log both rewritten in place; date and title block updated; no second file created | ✅ |
| **state plainly what changed since round 2** | §0 here, and §`sec:rounds` in the paper (a dedicated round-2→round-3 paragraph with the five decisions and the two findings enumerated) | ✅ |
| paths relative, nothing written outside the working directory | only `paper/paper.tex`, `paper/paper.pdf`, `paper/authoring-log.md` touched | ✅ |

**Nothing the brief enumerates was dropped.** Two brief clauses are inapplicable and are recorded
rather than silently skipped: the "if no TeX toolchain is on PATH" fallback (a toolchain *is* on
PATH), and the diagnosis-discipline clause (this molecule claims no root-cause fix and no
performance result).

---

## 3. Self-review (step 2), and what it found

The step-2 review is the author's own; the **independent adversarial review is a separate
downstream molecule** and this log does not anticipate its verdict.

**Coherence.** Read end to end after editing. The paper reads as one document at round 3: every
round-marker now says three rounds, or says two where the statement is genuinely about the first
two. Four residual round-2 phrasings were caught by grep on this pass and fixed — *"still not done
after two rounds"* (smooth model, → three), *"not formalised in Lean in either round"* (→ any
round), *"the one seam in either round that the legs closed by themselves"* (→ *"the one seam
either fan-out round closed by itself, without waiting for the reconciliation stage"*, which is
now the accurate form since a reconciliation stage exists), and *"rests on an L0 source in both
rounds"* (→ every round). No orphaned definition; no dangling `\ref`; the two new anchors
(`haz:margin`, V14) are each referenced from at least two sites.

**Completeness.** Every requirement of the brief has a section (§2 above). Every finding of the
current fault list that bears on the paper is applied at its point of use or disclosed in
§`sec:defects`; nothing was applied silently.

**Compliance.** Delivery posture *staged* and attribution *Noogram* are stated in the
Acknowledgements. Nothing claims a clean gate. **`proved` beyond the kernel leg:** the four `[K]`
results are the reduction lemma and the three barrier theorems, and no other statement is
asserted at that strength; the abstract's one borderline sentence was rewritten to carry its own
evidence rather than the bare word.

**Sources — spot-check performed, as the step requires.** `dusart2010estimates`, the single
external mathematical input to Theorem `thm:range`, was checked against its ledger row
(`source-ledger.md:400–414`, tier **L0**, MD5 `b6540b68…`). The paper cites
`[Thm. 6.9, eq. (6.6)]` for *"π(x) ≤ x/(log x − 1.1) for x ≥ 60 184"*; the ledger's statement
table gives that locator as *"`x/(ln x − 1) ≤ π(x)` for `x ≥ 5393`; `π(x) ≤ x/(ln x − 1.1)` for
`x ≥ 60184`"*. **Locator, statement and range all match**, and the paper uses only the upper half,
which is the half its Lemma `lem:floor` needs. The same row's Prop. 6.8 was checked against the
paper's table-free window (`x ≥ 396 738`, factor `1 + 1/(25 ln²x)`): matches.

**Issues found during review and fixed in place.** Seven, all found by re-reading or by counting
rather than by assuming, and all repaired before this log was closed:

1. The four residual round-2 phrasings listed above (*two rounds* → *three*, *either round* → *any
   round*, and two more).
2. A forward reference to verification item **V14** written before the item existed. Added.
3. The `haz:uncond` round-3 note initially said the correction was applied at two of three named
   sites *and that the third survived*. The current fault list records **two** surviving sites,
   one of which was not among the three originally named. Corrected to the fault list's own count
   and shape.
4. §`sec:rounds` initially said the re-audit *"confirmed all five decisions"*. The fault list is
   more precise: three of the four substantive decisions were confirmed by recomputation, the
   fourth against the version history, and the fifth — the cross-referencing — was delivered but
   **incompletely**, which is exactly what the first round-3 BLOCKER is about. Saying "all five
   confirmed" two paragraphs before disclosing that the fifth was faulted is an internal
   contradiction; corrected.
5. §`sec:defects` described the stale-tier sites as *"five concept cards, the concept-card index in
   two places, and one round-2 proof attempt"* — which sums to eight, not the seven claimed. The
   fault list's table has seven rows: **four** concept cards, the concept-card index in **three**
   separate places, and one round-2 proof attempt. Corrected; the count now adds up.
6. §`sec:provenance` initially credited the round-2 audit with having *"re-opened both sources at
   every locator this paper invokes"*. It did not: `verification-report.md` §1.20–1.21 and §4 say
   it re-verified every invoked locator **against the ledger's own §2.8 statement table**, which is
   a different and weaker act. Since the whole point of this revision is that round~2 overstated
   what an audit had done, overstating it in the opposite direction would have been the same error
   with the sign flipped. Rewritten to what the audit says of itself, with the standing re-audit
   obligation left explicitly standing.
7. §`sec:provenance` said the false sentence was quoted by *three* downstream documents; the trace
   is **two** (the reconciliation, then the synthesis it fed). Corrected. Also in the abstract:
   *four* further independent sweeps → **five** (two in round 2, three in round 3), and the vocabulary
   rule's claim that every labelled statement carries a confidence code, which is false for the two
   results imported wholesale rather than derived here — those carry *cited*, and the rule now says so.

**Issues deliberately NOT repaired, with justification:**

1. **The two round-3 BLOCKERs are not repaired, only reported.** Seven upstream sites carry a
   stale source tier; four statements in two upstream documents describe the corpus wrongly.
   Repairing upstream artifacts is an editing leg's job over the whole corpus, and this leg is the
   paper's author. Both are disclosed in §`sec:defects` at blocking severity, and this paper's own
   text is correct at every corresponding site — verified, not assumed.
2. **The sub-blocking residue is likewise reported, not repaired** — the two *"unconditional,
   Dusart only"* sites, the two *"weakest"* sites, the *"17 exceptions"* site, the frame document
   still printing `216 805`, the `arXiv v4` instruction on one card, and the two cards disagreeing
   on how many recounts agree. Same reason; all seven are itemised in §`sec:defects`.
3. **`thm:Cb`'s `2.40·10⁻⁸` margin is recorded, not closed.** Closing it means interval
   arithmetic, which is a funded computational leg, not an editing pass. Caveat `haz:margin` says
   exactly that, and §`sec:limits` lists it as outstanding.
4. **The fourth use of the letter `S`** (the RH certification set, alongside `S(x)`, `S♯(g)` and
   the sweep bar) is carried over from round 2 unrepaired, for round 2's reason: it is scoped to
   one theorem, declared in its statement, and renaming it would break correspondence with the
   source artifact.
5. **Underfull `\hbox`es** in table cells and two theorem headers. No text loss; repairing them
   means re-wording statements to suit the line breaker.

**Result: no unresolved issue remains within this leg's remit.** Everything deferred is deferred
to a named owner, in writing, above.

---

*Artifact of leg `write-paper`, molecule `edit-20260727-ace7`, run `germ-20260725-791a7c45`,
**round 3**. Supersedes the round-2 authoring log in place; the galaxy carries exactly one
current answer. The conjecture `F` remains **OPEN** — neither proved nor refuted by any round.
The evidence gate remains **BLOCKED**, failing leg SKEPTIC, on two findings that are bookkeeping
rather than mathematics. A round-2 citation audit of this paper's predecessor exists and returned
**PASS**; no citation clearance is claimed here, and that is not a contradiction — §`sec:provenance`
states why.*
