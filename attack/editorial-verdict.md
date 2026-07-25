# editorial-verdict.md — fail-closed editorial gate on the Firoozbakht paper

**Molecule:** `review-20260725-4b9d` (formula `temp-review`, crew role: **reviewer**)
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-25
**Target:** `paper/paper.tex` (1641 lines) + `paper/references.bib` + `paper/paper.pdf`
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`. **`F` is OPEN.**
Nothing in this verdict proves or refutes it, and nothing in the paper claims to.

**Author ≠ scorer.** This leg wrote no line of `paper.tex`. Every finding below is a score for
the author to act on, not an edit made on their behalf.

---

## VERDICT: **REWRITE**

Three failing checks, in descending order of consequence:

1. **The citation gate is BLOCKED.** `attack/verification-report.md` finds two of the paper's
   22 citekeys — `carneiro2019fourier` and `visser2018andrica` — with **no row in
   `attack/source-ledger.md`** (12 of 86 citation instances). Fail-closed rule: a BLOCKED
   citation-gate report is never SHIP.
2. **The evidence gate is BLOCKED.** `attack/evidence-verdict.md` reads BLOCKED with the
   SKEPTIC leg named as failing (2 unrepaired BLOCKERs upstream). This is **not** an honest
   DEGRADED: the DEGRADED carve-out exists for a degraded *kernel* leg, and the kernel leg here
   passes outright. Fail-closed rule: SHIP requires PASS or honest DEGRADED.
3. **Three OVERCLAIM rows.** The paper asserts a universal about its own citations that is
   false, and twice states that its citation audit "has not been run" — which has been overtaken
   by events. These are the paper's claims *about itself*, and they are now wrong.

Zero UNADDRESSED-FAULT. The mathematics survived every check this leg could run.

---

## 1. Per-claim verdict table

Full 100-row ledger in `claims-ledger.md`. Reproduced here: every non-CONFIRMED row, plus the
load-bearing CONFIRMED rows a reader needs in order to see what the REWRITE does *not* touch.

| Claim | Tag | Evidence |
|---|---|---|
| **A8** — "Four theorems close the Riemann-Hypothesis route as a route" (abstract iv, contribution 4) | **UNSUPPORTED-CITATION** | All four theorems consume `carneiro2019fourier` and/or `visser2018andrica`; neither has a source-ledger row (`verification-report.md` §2) |
| **A9** — "the sharpest published RH-conditional gap bound certifies `F` at exactly one index" | **UNSUPPORTED-CITATION** | The envelope `B_n := (22/25)√p_n·L_n` is defined at `paper.tex:842` from `carneiro2019fourier` §1.2 Thm 5 alone — no ledger row |
| **R23** — Thm 5.2 `thm:A`: `S = {n ≥ 3 : B_n ≤ T_n} = {3}` | **UNSUPPORTED-CITATION** | Same defect. The *arithmetic* is correct (recomputed at 40 digits, §3 below); the *envelope's provenance* is not ledger-backed |
| **R25** — Thm 5.5 `thm:Bpow`: catalogue "every prime-gap upper bound currently available lives in this class" | **UNSUPPORTED-CITATION** | The theorem's own proof is sound and source-free; the catalogue at `paper.tex:936–941` cites `visser2018andrica` §2 Thms 4,5 and `carneiro2019fourier` §1.2 Cor 4 — no ledger rows |
| **C21** — `carneiro2019fourier`, 7 instances | **UNSUPPORTED-CITATION** | `grep carneiro\|fourier` on `source-ledger.md` returns nothing. Effective L3 for gate purposes |
| **C22** — `visser2018andrica`, 5 instances | **UNSUPPORTED-CITATION** | `grep visser2018\|andrica` returns nothing. Effective L3 |
| **R47** — §10.3: "**Every citation in this paper traces to a row of a source ledger** built from scratch for this study: 20 rows…" | **OVERCLAIM** | False for 2 of 22 keys. The paper's *own next paragraph* retracts it ("pending ledger rows"), which makes it a self-contradiction rather than a concealment — but the universal sentence stands before its retraction and is what a downstream quoter will lift |
| **R48 / A11** — §10.3 and the abstract: "**The citation audit for this paper has not been run, and no citation clearance is claimed.**" | **OVERCLAIM** | The audit *has* run — molecule `cite-20260725-9eef`, artefact `attack/verification-report.md`, verdict **BLOCKED**, two citekeys named. A paper that reports its own gate state must report the state that exists |
| A1 — `F` is open, neither proved nor refuted | CONFIRMED | Boxed at §1.4; matches evidence-verdict, faults.md, lean-probe |
| A2/A3/R1/R41 — Lean reduction machine-checked, exactly one `sorryAx` dependent (the conjecture itself) | CONFIRMED | Evidence-gate **KERNEL leg PASS**: `lake build` 0, audit 0/0, 60 declarations, 1 `sorry` at the declared open target, grep-clean of `axiom`/`native_decide`/`unsafe` |
| A5/A6/R14–R19 — Dusart-only finite-range architecture; `B(2^64) = 1919.138`, published 1920 reproduced | CONFIRMED | `dusart2010estimates` Thm 6.9 eq.(6.6) is ledger row **L0, read at locator**; constant recomputed here to every quoted digit |
| A10/R34–R39 — exhaustive sweep to `10^11`, 4 118 054 812 pairs, 0 violations, `max ρ = 0.8318` | CONFIRMED | Two independent code paths, raising verdict function, exact-integer calibration |
| R8/R9/R30 — Axler-dependent results carried at `[P·s]`, not `[P]` | CONFIRMED | Caveat `haz:axler` names the unopened source and the nine-orders-of-magnitude corrigendum; strength honestly degraded |
| R12/F2 — the Axler-sharpened constant is **withheld** | CONFIRMED | Rem `rem:C-b` + §10.2(2); nothing in the paper rests on the defective derivation |
| R46 — "the pre-publication evidence gate on the underlying corpus stands at **BLOCKED**" | CONFIRMED | Exact match to `evidence-verdict.md`, including which leg fails and which pass |
| F1 (BLOCKER) | **addressed** | §10.2(1) names all three `m(n)` predicates, gives the ordering, says which the pruning consumes, reconciles both margin series |
| F2 (BLOCKER) | **addressed** | Suppression + disclosure, as above |
| F3, F4, F5, F6 (MAJOR ×4) | **addressed** | F3 → Caveat `haz:axler` + the Dusart-only fallback F3 asked for; F4 → Rem `rem:quantifier`, repair applied verbatim; F5 → no fraction quoted, only "about 55.9 %"; F6 → the faulty table is not reprinted |
| Delivery contract (attack/, paper/{tex,bib,pdf}, trace/) | **HELD** | All tracked at galaxy root; `paper.pdf` 239 093 bytes — a LaTeX toolchain was present. **Not a REWRITE reason** |

**Totals:** 66 CONFIRMED · **3 OVERCLAIM** · **5 UNSUPPORTED-CITATION** · **0 UNADDRESSED-FAULT**.

---

## 2. Fail-closed rule, applied

| Condition for SHIP | Actual | Pass? |
|---|---|---|
| Zero OVERCLAIM | 3 | ✗ |
| Zero UNSUPPORTED-CITATION | 5 | ✗ |
| Zero UNADDRESSED-FAULT | 0 | ✓ |
| Evidence gate PASS or honest DEGRADED | **BLOCKED** (failing leg: SKEPTIC) | ✗ |
| Citation gate report PASS | **BLOCKED** (2 citekeys, 12 instances) | ✗ |
| Both gate artefacts present | present | ✓ (the absent-evidence trapdoor does not fire) |

Four of six fail. **⇒ REWRITE.**

The delivery posture is the operator's call, not this gate's. This verdict says the paper is
not clear to ship *as a cleared artefact*; it does not say the work should be withheld, and the
paper itself already declares its posture **staged** and "not a seal."

---

## 3. What a REWRITE must do — the failing rows, named

Ordered by what unblocks the most.

1. **Fold `carneiro2019fourier` and `visser2018andrica` into `attack/source-ledger.md`.** They
   were fetched, version-pinned with MD5s, and read at the locator by `proof-attempt__1`, and
   proposed as ledger additions — but never converted. This is a *transcription* task, not new
   research, and it clears C21, C22, A8, A9, R23, R25 in one move. Note the residual: Carneiro's
   locators are to arXiv:1708.04122v2 and are not yet mapped to the journal's numbering — the
   ledger row must carry that as an L1 flag rather than silently claim L0.
2. **Delete or correct the universal in §10.3.** "Every citation in this paper traces to a row
   of a source ledger" is false while (1) is outstanding, and the sentence must not survive the
   paragraph that retracts it. Either fix (1) first and keep it, or restate as "20 of 22."
3. **Replace both instances of "the citation audit has not been run"** (abstract, §10.3) with
   what the audit actually returned: BLOCKED, two named citekeys, zero fabricated citations,
   zero locator mismatches among the 20 ledger-backed keys. The honest version is *stronger*
   than the placeholder — the audit found no fabrication and no mis-location anywhere.
4. **Upstream, to lift the evidence gate:** apply the F1 and F2 repairs to the corpus artefacts
   (`notebook-0`/`notebook-2`/`L15` and `proof-attempt-0.md` §C(b)) and re-run the skeptic leg
   to a zero-BLOCKER state. Both repairs are one paragraph and one line respectively, and both
   are already written out in `faults.md` §2. **Note carefully:** the *paper* already handles
   both defects correctly. This item is about the corpus, not the prose.

Residual non-blocking observations, recorded so they are not rediscovered: F8's phrase
"essentially the whole verified range" survives at `paper.tex:916` without carrying the 0.47 %
shortfall as a number; F9's widest-bracket choice survives at `paper.tex:1159`, inside a passage
the paper itself labels a gloss and instructs the reader not to quote. Neither is a gate failure.

---

## 4. What this REWRITE explicitly does **not** touch

Said plainly, because a REWRITE verdict on a 1641-line paper invites the assumption that the
mathematics is in question. It is not.

This leg recomputed from scratch, at 40 digits, from the paper's *statements* rather than its
code: `B(2^64)`, the `S♯` inversion at 1918/1920, the entire six-row Theorem 5.2 table, the two
excluded indices `n = 1, 2`, `h(x*)` in Lemma 5.1, the sign change `p* = 777 600.744…`, and the
critical constant `2/e`. **Zero discrepancies.** Every digit the paper prints is the digit that
comes out.

Nor is the honesty in question. The paper's confidence-code discipline holds: the word *proved*,
unqualified, appears nowhere outside the `[K]` leg and the explicit negations ("neither proved
nor refuted"). Axler-dependent results are demoted to `[P·s]` at the point of use. Two unsourced
standard facts (Brun–Titchmarsh, Montgomery–Vaughan) are flagged as unsourced *and* used only
negatively. The evidence gate's BLOCKED status is reported by the paper about itself, in §10.2,
accurately down to which leg failed.

The failures scored above are failures of **provenance plumbing and of a stale self-description**.
They are two hours of work, not a re-derivation.

---

## 5. DISSENT

Required section. Anti-groupthink: an editorial verdict that only ratifies the upstream gates
adds nothing a `grep` could not.

**The most interesting tension in this work is that its honesty discipline and its fail-closed
gate discipline are pulling in opposite directions, and the gates cannot see it.**

Consider what actually happened at §10.3. The paper wrote down a universal claim about its
citations ("every citation traces to a ledger row"), then — in the very next paragraph —
retracted it, named the two exceptions, explained their provenance, and told the reader where
the disclosure is duplicated (`references.bib` header, `authoring-log.md` §3). The citation gate
read that and returned BLOCKED. It was right to. But note what the gate's verdict is *insensitive
to*: it would have returned exactly the same BLOCKED had the paper concealed the gap entirely.
A paper that hides two unledgered citations and a paper that flags them three times in three
artefacts score identically. The gate measures the artefact's state, not the author's conduct,
and it is designed that way on purpose — an unfalsifiable "but I was honest about it" defence is
precisely what fail-closed exists to refuse.

And yet the asymmetry is real, and it has a cost the pipeline should see. Disclosure is expensive
to write and, under a state-based gate, buys the author *nothing*. Worse: the paper's §10 is the
most elaborate self-incrimination in the corpus — it names its own evidence gate as BLOCKED, ranks
its three load-bearing unopened sources in priority order, and states the exact decade shortfall
of its own sweep. Every one of those sentences is a hostage the author volunteered. Under a purely
state-based gate, the dominant strategy for an author optimising for SHIP is to write *less* §10,
not more — to let the gates find what they find, and to keep the paper's own claims small enough
that no self-assertion can be caught stale. That is exactly backwards from what this pipeline
wants.

I see it sharpest in the one row I found most uncomfortable to score, **R48**. The paper says
"the citation audit for this paper has not been run." When it was written, that was true, and
saying it was an act of discipline — the author refusing to imply a clearance they did not have.
The audit then ran, and the sentence became false. So the author is scored OVERCLAIM for a
sentence whose *only* defect is that it was honest at a moment that has passed. An author who had
written nothing about the audit would have no row here at all. **Volunteering a checkable
statement about your own gate state is strictly riskier than saying nothing**, and this ledger is
the proof.

I do not propose relaxing the gate. Fail-closed is right, and I have applied it without a carve-out
above. What I propose is that the *shape* of the artefact absorb the problem instead: a paper
should not hard-code its own gate verdicts in prose. The gate states belong in a generated stanza
— one block, regenerated from `evidence-verdict.md` and `verification-report.md` at compile time —
so that a paper's self-description cannot go stale between the write leg and the gate leg. As it
stands, the pipeline runs `write-paper` *before* `citation-gate` and then penalises the paper for
not knowing the future. That is a structural fault in the formula, not in the author, and it is
cosmon-ward: **the ordering makes a class of OVERCLAIM unavoidable for any honest author.** I am
recording it here rather than silently patching the paper, per the cosmon-ward rule.

A second, smaller dissent, on the mathematics rather than the process. The paper's proudest
result is that it *closed the RH route as a route* — four theorems, a Lambert-`W` determination
of the critical constant `2/e`, an explicit counter-model. I checked all of it and it holds. But
I want to register that Theorem 5.2's headline — "certifies at exactly one index" — is doing less
work than its prominence suggests, and the paper very nearly says so itself: the single certified
index is `n = 3`, i.e. `7³ < 5⁴`, decidable by a child. The genuinely load-bearing result in §5 is
not Theorem 5.2 but Theorem 5.5 together with Theorem 5.6: **the line is at `θ = 0`, and every
available bound has `θ > 0`.** That is scale-theoretic and permanent; the one-index result is a
striking but essentially decorative corollary of it. Given that Theorem 5.2 is also the result
that hangs entirely on the two unledgered citations, and Theorem 5.6 hangs on nothing external at
all, the paper would be *both* stronger and more defensible with the emphasis inverted. That is a
judgement about framing, not a fault, and I state it as dissent rather than as a required change.

---

*Artefact of leg `editorial-verdict`, molecule `review-20260725-4b9d`, run
`germ-20260725-791a7c45`. Sources read: `paper/paper.tex`, `paper/references.bib`,
`paper/authoring-log.md`, `attack/evidence-verdict.md`, `attack/verification-report.md`,
`attack/faults.md`, `attack/source-ledger.md`. Every constant reported as recomputed was
recomputed by this leg at 40 digits. No line of the paper was edited by this leg.*
