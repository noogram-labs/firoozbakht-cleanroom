# Authoring log — `paper/paper.tex`

**Molecule:** `edit-20260726-5e79` (formula `editorial-work`, crew role: writer) — **ROUND 2**
**Run:** `germ-20260725-791a7c45` · **Re-attack loop:** `reattack-20260726-57d1` (`rounds = 2`)
**Date:** 2026-07-26
**Source of record:** `attack/synthesis.md` (839 lines, itself a **round-2** artifact superseding
its round-1 predecessor in place), plus the round-2 leg artifacts under
`attack/re-attack/attack-round-2/` and `lean/Firoozbakht/Barrier.lean`.
**External attribution:** Noogram. **Delivery posture:** staged.

> **This file supersedes the round-1 authoring log of the same name, in place.** The paper it
> describes likewise supersedes the round-1 `paper.tex` (molecule `edit-20260725-37f8`). Where
> the rounds differ, round 2 is current. §0 states what changed; the rest of this file describes
> the round-2 artifact only, so that nothing in this directory describes a round the run has
> moved past.

---

## 0. What changed versus round 1, and what did not

**Changed — mathematics.**

| Round 1 | Round 2, as written into the paper |
|---|---|
| The pruning obligation was one name, `(P6′)`, "open and empirically unviolated"; the paper asserted the three readings were strictly ordered `(iii) ⟹ (i) ⟹ (ii)`. | §4 names **four** predicates (`P6′-pair`, `P6′-gov`, `P6′-min`, `P6′-rec`), **refutes** `P6′-pair` with two witnesses and a 17-index census, and **withdraws the ordering**: `P6′-gov ⟹ P6′-min` is invalid, the missing link being `P6′-rec`. The first-failure-maximality theorem then shows the pruning consumes either survivor **at one index only**, so the refutation costs the route nothing. |
| The Axler-sharpened near-record constant was **withheld** — its derivation was false by a factor ≈ 38.8 and unrepaired. | §6.5 states the defect precisely, states the repair, proves it two independent ways, and **carries the sharper theorem**: `p_m ≤ 0.998244·p_{n₀}`. The second repair (`0.99565`) is retired to a remark, with the reason: its Axler table row exists in the preprint edition only. |
| Dusart-only near-record: `p_m ≤ 0.93961·p_{n₀}`. | **`p_m ≤ 0.94970·p_{n₀}`**, the small-branch cutoff raised from `60 184` to `10⁸`. |
| `axler2014newbounds` was **unopened**, quoted through Kourbatov; lemmas resting on it carried `[P·s]`. | Opened in all three editions (preprint, journal, corrigendum), digest-pinned, read at the locator. Tier **L0**. Those lemmas now carry `[P]`. Two *editorial* hazards replace the old one: the corollary numbering differs by one between editions, and one table row is preprint-only. |
| Lean: reduction machine-checked, 60 declarations audited, one `sorryAx`. | Same, at **63** declarations, plus a **new machine-checked barrier**: Bertrand's postulate — the only prime-gap bound Mathlib carries — is proved insufficient at **every** `n ≥ 2`. Round 1 had this as an observation; it is now a kernel-checked theorem, and `[K]` now covers four results rather than one. |
| The RH headline read "at exactly one index **and at no other index whatsoever**". | That clause was **false as stated**. §7.1 splits it into two theorems: arithmetic clearance `A = {1,2,3}` (no RH, no hypothesis) and the certified set `S = {3}`, with a remark stating that the source's hypothesis `p_n > 3`, not the arithmetic, excludes `n = 1,2`. §7.2 introduces `C_n := T_n/(√p_n·L_n)` and closes a silent contradiction between two artifacts of the run. |
| The `55.92 %` statistic was **omitted entirely** (four fractions circulated; the round-1 writer declined to reprint a disputed number). | Now **stated with its adjudication**: carry `121 238/216 806` (`n ≥ 10`) and `121 239/216 815` (all `n`), on three mutually independent recomputations — and record that a round-1 review called the higher denominator an off-by-one and a round-2 leg re-affirmed that call, both wrong. The disputed lower denominator is still live in the corpus and is named as such. |

**Changed — the disclosure section.** Round 1 disclosed **two** unrepaired blocking defects.
Round 2 discloses **three**, of a different species: two correct-but-incompatible repairs of the
same defect; contradictory source tiers for the same source across two legs; and an
edition-fragile citation whose dependent artifact does not carry the flag. §11.3 of the paper
states plainly that the count went **up** and that this is the worse signal, and a remark there
records the structural reading — a fan-out with no reconciliation stage, which round 2 widened.

**Not changed.**

- `F` is **OPEN** — neither proved nor refuted, in either round. The paper says so in the
  abstract, in a boxed statement in §1.5, in §11.1 and in the conclusion.
- The Lean `sorry` count is exactly **one**, and it is the conjecture.
- The obstruction analysis is unchanged, and was *reinforced* in three independent places.
- The evidence gate is **BLOCKED**. The reason changed; the verdict did not.
- **No citation clearance exists**, and none is claimed.
- Delivery posture **staged**; external attribution **Noogram**.

---

## 1. Toolchain

| Item | Value |
|---|---|
| Engine | XeTeX 3.141592653-2.6-0.999997 via `latexmk -xelatex` |
| `latexmk` | `/Library/TeX/texbin/latexmk` |
| `xelatex` | `/Library/TeX/texbin/xelatex` |
| Bibliography backend | `biber` (`/Library/TeX/texbin/biber`), driven by `biblatex` (`style=alphabetic`) |
| TeX distribution | TeX Live 2025 (`/usr/local/texlive/2025`) |
| Packages | `amsmath`, `amssymb`, `amsthm`, `booktabs`, `longtable`, `geometry`, `xcolor`, `hyperref`, `biblatex` |
| PDF writer | `xdvipdfmx` (20250205) |

**A TeX toolchain WAS present.** The compiled PDF is delivered next to the sources; the
recipient does not need to rebuild.

## 2. Compile summary

Command, run from `paper/`:

```
$ latexmk -C && latexmk -xelatex -interaction=nonstopmode paper.tex
```

| Gate | Result |
|---|---|
| `latexmk -xelatex` exit status | **0** |
| pages produced | **38** (round 1: 25) |
| `paper.pdf` size | 341 645 bytes |
| unresolved `\ref` | **0** |
| unresolved `\cite` | **0** |
| multiply-defined labels | **0** |
| `biber` warnings / errors | **0** |
| Overfull `\hbox` | **0** |
| Underfull `\hbox` | **6** — table cells of typewriter tokens that cannot hyphenate, plus two theorem headers; cosmetic, no text loss |

Reproduce with `latexmk -C && latexmk -xelatex paper.tex`.

## 3. Citation traceability — the round-1 gate failure, closed

Every `\cite{}` key in `paper.tex` resolves to an entry in `references.bib`, every entry is
cited, and **every key now traces to a row of `attack/source-ledger.md`**. Mechanically checked:

```
cited keys: 22   bib keys: 22
cited-but-missing-from-bib: (none)
in-bib-but-never-cited:     (none)
keys with no ledger row:    (none)
```

*(Four keys differ from their ledger rows by camelCase-vs-snake_case only — `oeisA111943` /
`oeis_A111943` and the like — which the round-1 audit already checked and classified as a
cosmetic rename, same sequence, same URL.)*

**What this leg had to do to reach that state, stated in full because it is an upstream edit.**
The round-1 citation audit (`attack/verification-report.md`, molecule `cite-20260725-9eef`)
returned **BLOCKED** on exactly two keys — `carneiro2019fourier` and `visser2018andrica` — which
traced to no ledger row, and the downstream editorial gate consequently returned **REWRITE**.
Their actual provenance was: fetched, arXiv-version-pinned, MD5-pinned and read at the locator by
round-1 leg `proof-attempt__1`, **proposed** as ledger additions, and never merged. Round 2's RH
leg (`task-20260726-b335`) re-quoted both at the same locators with the same version pins and
MD5s and re-affirmed the proposed tiers, but explicitly opened no source and merged no row.

This leg **folded the pending proposal** into the ledger as its new §2.8 — two rows,
`carneiro2019fourier` at **L1** (preprint pagination against a journal citation, the same
standard the ledger applies to `granville1995cramer`) and `visser2018andrica` at **L0**, with an
L2_weak sub-row flagged on the one CMS locator that is a *report* of works nobody opened. The
ledger header now reads **22 rows — 13 L0, 4 L1, 3 L2_strong, 2 L2_weak, 0 L3**.

Three things about that fold are recorded in the ledger itself (§2.8 head, §6 item 11, §7 item 3),
in `references.bib`'s header, and in the paper (§11.4), rather than smoothed:

1. **A writer leg is not a sourcer leg.** Folding rows outside one's own remit is the same
   species of cross-leg seam as the three BLOCKERs the paper discloses. It is logged as such,
   in the paper as well as here.
2. **This leg did not re-open either PDF.** What it verified independently is the *bibliographic
   envelope* of both — title, authors, journal, volume, pages, DOI, and the existence of the
   pinned arXiv version — against the publishers' own listing pages on 2026-07-26 (§8, spot-check).
   The interior locator tables are `proof-attempt__1`'s reading, not this leg's.
3. **Both rows carry a standing re-audit obligation**, and a citation-audit leg must discharge it.
   Folding the rows closes the *traceability* condition; it does not constitute an audit, and the
   paper claims no clearance.

Two entries also gained data this leg verified: `visser2018andrica` now carries its journal
reference and DOI (round 1 had it as a bare `@misc`), and `carneiro2019fourier` its DOI.

**Alternatives considered and rejected.** (a) *Dropping the two citations*: impossible without
deleting §7 (the RH route), whose central object is the CMS envelope — the paper would lose five
theorems rather than two footnotes. (b) *Leaving them unledgered and flagged, as round 1 did*:
that is precisely the state the citation gate already failed on, and repeating it would reproduce
round 1's outcome verbatim. (c) *Opening both sources afresh and minting rows from a first
reading*: that is a sourcer leg's job at a sourcer leg's budget, and doing it here would create a
**second** provenance record for the same two sources — a new seam of exactly the kind the paper's
§11.3 adjudicates. Folding the existing proposal verbatim was chosen because it adds no new claim.

## 4. The `proved` discipline

The brief requires that `proved` be claimed only for targets the kernel leg established. The
paper fixes an explicit vocabulary in §1.5 and holds to it:

- `[K]` — machine-checked by the Lean kernel. **Exactly four results carry it:** the reduction
  `F ⟺ ∀n≥1, g_n < T_n`, and the three barrier theorems `bertrand_gap`, `p_lt_two_pow`,
  `bertrand_ceiling_above_threshold`. All four are `sorry`-free in a tree whose exhaustive,
  list-free audit over **63** declarations finds exactly one `sorryAx` dependent — the conjecture
  itself.
- `[P]`, `[P·s]`, `[C]`, `[H]` — paper proof; paper proof on a contested-tier source; exhaustive
  computation; heuristic. Each is labelled at the point of use.
- The word *proved*, unqualified, is reserved for `[K]`.
- **The kernel leg's `PASS` is not the claim `PROVED`.** The paper states this inside the boxed
  disclosure of §11.3: the kernel verdict on `F` itself was `UNPROVABLE_IN_BUDGET`.
- **`F` is nowhere claimed to be true or false.** The synthesis's standing instruction is carried
  verbatim into the conclusion.

Note on the barrier: it is `[K]` and it is a statement about the *substrate*, not about `F`. The
paper says so explicitly in a dedicated remark — a negative-capability result, silent on whether
`F` is true or provable. That distinction is load-bearing and is stated three times (abstract,
§3.2, §11.6).

## 5. Brief coverage — every enumerated point

| Brief requirement | Where | Status |
|---|---|---|
| LaTeX, never markdown-only | `paper/paper.tex` | done |
| `\documentclass{article}` | l.1 | done |
| `amsmath` + `amsthm` + `hyperref` | preamble | done |
| theorem / lemma / definition / proof environments | preamble + throughout | done — **44** numbered theorem-like results plus **31** numbered remarks and caveats |
| every proof opens with an italic *Idea:* line | `\idea{}` macro | done — **32** proofs, **32** `\idea` lines, mechanically checked |
| `biblatex` over `paper/references.bib` | preamble, `\printbibliography` | done (backend `biber`, 0 warnings) |
| every `\cite{}` traces to a source-ledger row | §11.4 of the paper + §3 above | **done, and the round-1 gap is closed** — 22/22 keys trace; the fold and its re-audit obligation are disclosed |
| abstract | p.1 | done |
| intro + literature | §1, incl. §1.3 in five groups | done |
| setup | §2 | done |
| main results | §3 (formal substrate + barrier), §4 (predicates), §5 (monotone bar), §6 (finite range), §7 (RH route), §8 (smooth model) | done |
| computational evidence | §9 | done |
| honest limitations | §10 (tension) + §11 (what remains open / what is not established) | done |
| references | `\printbibliography` | done — 22 entries, 22 distinct labels |
| compile with `latexmk -xelatex`, deliver `paper.pdf` | §2 above | done |
| toolchain + compile summary in `authoring-log.md` | this file | done |
| delivery posture: staged | §11.3, §11.4, Acknowledgements | done, stated three times |
| external attribution: Noogram | title block, Acknowledgements | done |
| `proved` only for kernel targets | §4 above | done |
| **round 2 supersedes round 1 in place** | title block, §1.5, Acknowledgements, §0 of this log | done |
| **state plainly what changed and what did not** | §1.4 of the paper, §0 of this log | done |
| **F1 — name the three predicates explicitly** | §4.1, Definition of the predicates | done — **four** are named. The brief asked for three; round 2 found a fourth (`P6′-rec`) that the implication lattice needs. Recorded as an addition, not a substitution. |
| **F2 — restate as `v(1+v/x)`, `v := ℓ²−ℓ−1−1/ℓ`** | §6.5, the defect caveat, the envelope table, and the retirement remark | done — **both** forms appear: `v := ℓ²−ℓ−1−1/ℓ` (the brief's form: the tight restatement of round 1's own printed lemma, which yields `0.99565` and is retired) and `v := ℓ²−ℓ−1−2.1/ℓ` (edition-independent, carried into the theorem the paper keeps) |
| `paper/` git-tracked in the worktree | committed on `feat/edit-20260726-5e79` | done |

**Nothing in the brief was silently dropped.** Two items were answered with more than they asked
for — F1 with four predicates rather than three, F2 with both repairs rather than one — and both
departures are flagged in the table above and argued in the paper at the point of use.

## 6. Editorial decisions, and why

1. **The `55.92 %` figure is now printed, where round 1 omitted it.** Round 1's omission was
   defensible when four fractions circulated with no adjudication. There is now one: three
   mutually independent recomputations, one written from the statements with its own sieve at
   60 digits, agree on `π(3·10⁶) = 216 816` and hence on `216 815` / `216 806` steps. The paper
   prints the adjudicated figures **with both riders attached** (range-dependence, and
   non-diagnosticity for all four predicates) and records that the review process was wrong about
   this twice in the same direction. A number whose dispute is settled, and whose settlement
   corrected the reviewers, is more useful printed than omitted.
2. **The refutation of `P6′-pair` leads §4, ahead of the monotone-bar principle that was round 1's
   headline.** Order follows load-bearing-ness: a reader needs to know the lemma is false before
   reading a section that discharges its practical content by other means. §5 then states
   explicitly what the monotone bar does *not* replace — the first-failure-maximality theorem is
   a statement about the exact bar `T`, and no surrogate substitutes there.
3. **The sharper repair is carried; the other is retired to a remark.** The corpus contains two
   correct repairs of one defect and no rule for choosing. The paper chooses on a ground that is
   not taste — the carried theorem's Axler table row is present in **both** editions of the
   source, so it is not exposed to the edition hazard — and says outright that the corpus did not
   make this choice, this paper did. The retired statement is kept because it is the cleanest
   proof that round 1's *conclusion* survived its own broken derivation.
4. **`0.004479` appears exactly once**, as the number that *survived* its own repair, never as a
   derived constant. `0.99565` appears exactly once, as the theorem being retired. `0.99553` and
   `0.0623` appear only in the round-1-versus-round-2 comparison table.
5. **The withdrawn ordering is stated as withdrawn**, naming round 1's paper as the place that
   asserted it. A superseding paper that silently drops a claim it used to make is harder to audit
   than one that withdraws it by name.
6. **Two labelling defects inside round 2's own repairs are stated at their point of use**, not
   collected in the limitations section: the "census of pairs" that in fact counts indices, and
   the "unconditional" label that rests on a verification height plus an in-run sieve. A defect
   stated where the reader meets the claim cannot be missed by a reader who skips §11.
7. **`e^{−0.0017569} = 0.998244642445…` is printed at the correct value.** An upstream document
   prints `0.99824467`, wrong in its last displayed digit; the paper carries the correct expansion
   and §11.3 records the upstream defect. The theorem's headline `0.998244` is unaffected either
   way.
8. **Unsourced items are marked and used only negatively.** Brun–Titchmarsh, the second
   Hardy–Littlewood conjecture and Montgomery–Vaughan have no ledger row in this run. They appear
   only to *name* obstructions and never to support a positive claim; each is flagged inline.
9. **The counter-model theorem's gloss is separated from the theorem** by a remark that refuses
   the stronger informal reading, because the derivation class it quantifies over is not
   formalised and is contingent on what this run fetched.
10. **The `2⁶⁴` frontier is cited, never claimed.** §2.3 states it as a cited result and names the
    consequence at the point of use; §11.4 names the unopened gap table as citation-gate priority
    2 with the exact consequence — if that table is incomplete, the `1920` reproduction and every
    use of the verified range say nothing. §6.5 additionally names every place where
    `p_{n₀} > 2⁶⁴` is consumed as a hypothesis.
11. **Two round-1 self-review findings were carried forward as constraints, not rediscovered.**
    Round 1 found that (i) `\label` inside `\item[V…]` resolves silently to the enclosing
    subsection, and (ii) `\ll` and `\asymp` do not survive text extraction from the PDF. This
    paper therefore writes the verification-item tags literally (no `\label` inside the list;
    mechanically confirmed: zero such labels) and contains no `\ll` and no `\asymp`
    (mechanically confirmed). The corrected value `log(5 log 5) = 2.0853` is likewise carried,
    not the round-1 typo.

## 7. What this paper does NOT do — carried forward for the downstream verdict node

1. **The citation audit has not run on the round-2 corpus.** No clearance is claimed. §11.4 of the
   paper lists the load-bearing under-located sources in priority order: `granville1995cramer`
   (preprint pagination — now priority 1, Axler having been opened), the `2⁶⁴` height via the
   unopened `oliveira2014goldbach`, and the two newly folded §2.8 rows.
2. **The evidence gate on the underlying corpus stands at BLOCKED**, failing leg the round-2
   adversarial review, three findings. §11.3 discloses all three in a boxed statement. This paper
   *adjudicates* one of them (it chooses which repair to carry, and says so) and *reports* the
   other two; it does **not** repair the upstream artifacts, which still carry them.
3. **Upstream artifacts were modified by this leg in exactly one place**, and it is not a
   mathematical one: `attack/source-ledger.md` gained §2.8 (two rows), an amended header count,
   one declared-gaps entry and one priority-order entry. §3 above states why, what was verified,
   and what obligation stands. **No other file outside `paper/` was touched** — in particular no
   concept card, no notebook, no proof attempt and no fault report.
4. **No source was opened by this leg.** Bibliographic envelopes were re-confirmed for two sources
   (§8); no interior locator was re-read, and no tier was raised on this leg's own authority.
5. **The Lean development was not re-built by this leg.** The paper's gate table quotes the exit
   statuses the round-2 lean-probe recorded and the round-2 adversarial review *re-executed* —
   that re-execution is the strongest attestation available for those numbers, and it is
   second-hand here.
6. **The `10¹¹` sweep was not re-run by this leg**, nor were round 2's two additional sweeps
   (to `10⁹` and `2·10⁸`). All are reported at the figures their own legs recorded. Note that one
   of those legs states that its own `10⁹` decade is one beyond its sieve and is not
   independently confirmed by it; the paper carries that qualification rather than dropping it.
7. **The independent adversarial review is a separate molecule downstream** (the
   editorial-verdict node). Step 2 of this molecule is authoring-time self-review only, and its
   result is §8 below.

## 8. Self-review pass (Step 2)

Checklist from the formula, and the result of each.

**Coherence.** Read end to end as one document. Notation is fixed once in §2.1 and used without
drift: `p_n` one-indexed throughout, `L_n = log p_n`, `g_n`, `T_n`, `ρ_n`, plus `r(n)` and `µ(n)`
introduced once in the predicate definition and never overloaded — which is the direct remedy for
round 1's collision. Three symbols needed disambiguation and were given distinct names rather
than being overloaded: `S(x) = log²x − log x − 1.17` (Kourbatov's monotone surrogate, §5.1),
`B(x) = log²x − 1.1 log x` (the Dusart-only floor, §6.1) and `S♯(g)` (the inverse of `B`). The
four predicates each have their own macro, so a rename remains a one-line change.

**Completeness.** Every brief requirement has a section; the mapping is §5 above, and it now
carries the two round-1 BLOCKERs named in the brief (F1, F2) as explicit rows.

**Compliance.** Delivery posture *staged*, stated three times. External attribution *Noogram*, in
the title block and the acknowledgements. `proved` reserved for `[K]` (§4 above). No claim that
`F` is true or false. Round-2 supersession stated in the title block, §1.4 and the
acknowledgements. No confidential material appears: the paper contains mathematics, cited
literature and this run's own computational results — no filesystem path, no operator identity,
and no internal molecule identifier appears in the PDF. Nothing was written outside the working
directory, and no absolute path to a deliverable was constructed.

**Sources — spot-check.** The brief asks for at least one citation checked against its source. Two
were, and they were chosen as the two that mattered — the keys that failed the round-1 gate.
`arXiv:1708.04122` was fetched at its listing page and returned title *"Fourier optimization and
prime gaps"*, authors Carneiro–Milinovich–Soundararajan, *Comment. Math. Helv.* **94** (2019)
no. 3, 533–568, DOI `10.4171/CMH/467`, versions v1 (2017-08-14) and v2 (2018-09-14) — matching
`references.bib` and the v2 pin exactly. `arXiv:1804.02500` returned *"Variants on Andrica's
conjecture with and without the Riemann hypothesis"*, Matt Visser, *Mathematics* **6** (2018)
no. 12, 289, DOI `10.3390/math6120289`, versions through v3 (2018-11-28) — matching the v3 pin,
and supplying the journal data round 1's entry lacked. **Reported honestly: the listing pages
confirm the bibliographic envelope and the version pins; they do not confirm the interior
locators** (`§1.2 Thm. 5`, `Thm. 1 eq. (1.4)` and the rest), which remain `proof-attempt__1`'s
reading. That is exactly why the re-audit obligation stands and is written into the ledger.

*Fixes applied during this pass, in the order found:*

1. **Three malformed environment terminators** (`\end{hazard>`, `\end{proposition>`,
   `\end{theorem>`), an artefact of drafting the document in five parts. Two were caught by
   mechanical scan before the first compile, one by the compile itself. Re-checked mechanically:
   no `\end{…>` remains.
2. **Five overfull `\hbox`es**, all in tables and one display, all cosmetic but all real: the
   predicate-lattice display in the withdrawal remark (split into a display plus a sentence), the
   envelope table of §6.5 and the round-1/round-2 comparison table (re-columned; the latter's
   source-status column moved into a following sentence), the RH-readings summary table
   (re-columned to `p{}`/`p{}`) and the results table of §9.2 (`\small`). Recompiled to
   **0 overfull**.
3. **`references.bib`'s header still described the two folded keys as PENDING LEDGER ROWS.**
   Rewritten to describe the actual state and to carry the re-audit obligation, so the bib file
   and the ledger cannot drift apart silently. The two entries' inline comment block was
   rewritten for the same reason.
4. **The literature subsection still said Axler's dependency was "load-bearing and unresolved
   here"** — round 1's state. Rewritten to say it is opened, with a pointer to the two editorial
   hazards that replace it.
5. **Cross-reference and citation sweep**, done mechanically rather than by reading, because
   round 1's own log records that a *wrongly* resolved reference does not warn: `0` undefined,
   `0` multiply-defined per `paper.log`; and an independent extraction of every `\cite` key
   compared against both `references.bib` and the ledger's row names — `22/22` in both
   directions, listed in §3.
6. **Placeholder sweep.** No `TODO`, `TBD`, `XXX` or `FIXME` remains; every `…` in the document is
   a truncated numeric expansion, and every such expansion traces to §9.4's verification list or
   to the synthesis's own recomputation table.
7. **A confidence-code inconsistency between the contributions list and the body, and it was the
   substantive one.** The contributions list assigned `[P·s]` to the finite-range theorem, which
   the body labels `[P]` — correctly, since its only analytic input is Dusart at L0. Fixing that
   exposed a second, opposite error: `[P·s]` would then have been *defined and never used*, and
   the two near-record theorems were labelled `[P]` even though both consume the published `2⁶⁴`
   verification height, which rests on a source this work never opened. **Both were relabelled
   `[P·s]`**, the caveat there now states why in one sentence (*the weakest link is the
   verification height, not the estimate*), and the vocabulary row was widened from "contested
   ledger status" to "not opened in this work, or contested". Net effect: one theorem's tier
   improved and two theorems' tiers were *lowered* by this pass. The lowering is the honest
   direction and is recorded as such.
8. **Section cross-references in this log were checked against `paper.toc`, not against memory,**
   after the fact — five were off by one subsection (the round-2 paper gained §1.4, which shifted
   §1.5 and §1.6, and §6 gained a subsection). Corrected mechanically.
9. **The verification-list subsection was titled for §5–§6 while carrying items for §3 and §7.**
   Retitled, and the item ranges are now stated explicitly (V1–V9, V10–V11, V12, V13) so a reader
   can find the item a proof cites without scanning. All five `item V…` references in proofs were
   checked against the thirteen defined tags: all resolve.
10. **The factor-38 denominator ambiguity**, and it is the one substantive arithmetic correction
    this pass made. See the recomputation table above.

**Independent recomputation of the two places where this paper contradicts an upstream document.**
A paper that reverses two of its own sources should not do so on a third party's word, so both were
recomputed from the statements in a fresh script (own sieve to `3·10⁶`, `mpmath` at 60 decimal
digits, no upstream code path):

| Claim, as printed in the paper | This leg's independent value | Verdict |
|---|---|---|
| `π(3·10⁶) = 216 816` | `216 816` | ✓ |
| `121 239 / 216 815` (all `n`) `= 55.9182 %` | `121 239 / 216 815 = 55.91817909…` | ✓ — **the adjudication holds** |
| `121 238 / 216 806` (`n ≥ 10`) `= 55.9200 %` | `121 238 / 216 806 = 55.92003911…` | ✓ — the denominators reported one lower upstream are wrong |
| W1: `p_1823 = 15 641`, `p_1831 = 15 683` (`g = 44`), `p_1832 = 15 727`, `p_1847 = 15 823` | all four | ✓ |
| `T_1823 = 83.0807167192698…`, `T_1847 = 83.0521061144139…` | both, to every digit printed | ✓ |
| W1 margin `T_m − T_n = +0.02861060485582…` | `+0.028610604855820881…` | ✓ — **`P6′-pair` is false, confirmed independently** |
| `max{g_k : p_k < 60 184} = 72` at `p = 31 397`, over `6 076` gaps | `72` at `31 397`, over `6 076` gaps | ✓ (the count is `6 076` under the paper's own indexing — the `n` with `p_n < X₀`, whose last gap crosses `X₀`; a reader counting gaps *within* the set would get `6 075`) |

Every other numeric constant in §6.5, §6.3, §7 and §9.4 was likewise recomputed at 30–60 digits
(`e^{−0.0516}`, `e^{−0.0017569}`, `e^{−0.0043636}`, `log 2⁶⁴`, `L(L−1.1)` at `2⁶⁴`, `2/e`,
`log 10⁸`, `log 6 690 557`, Lemma A.1's `h(x*)`, `S(29)`, `B(60 184)`, `log(5 log 5)`), and all
matched what is printed.

**One substantive correction this recomputation forced.** The factor by which the round-1 bound is
wrong was printed upstream, and initially here, as `38.8137…` *against the printed `0.004479`* —
but `0.169339812744 / 0.004479 = 37.807504…`, so a reader checking the arithmetic would find a
mismatch. The factor's true denominator is the separation required under the bound's **tight**
form, `0.004362882388…`, and `0.169339812744 / 0.004362882388 = 38.813747…`. The caveat and item
V11 now name all three numbers and say which quotient is which, including the wrong quotient a
reader might otherwise compute. Nothing downstream of that factor changes — it quantifies a defect
in a bound the paper does not use.

*Issues found and deliberately NOT repaired, with justification:*

1. **A fourth use of the letter `S`** — the certification set `S = {3}` of the RH section,
   alongside `S(x)`, `S♯(g)` and the sweep bar. It is scoped to one theorem and declared in its
   statement; renaming it would break correspondence with the source artifact. Noted, not
   repaired.
2. **Six underfull `\hbox`es.** Typewriter tokens in table cells and two theorem headers that
   cannot hyphenate. No text loss. Repairing them would mean re-wording statements to suit the
   line breaker.
3. **The three upstream BLOCKERs are not repaired**, only adjudicated or reported (§7 item 2).
   Repairing upstream artifacts is a reconciliation leg's job, and this leg is not it. The single
   upstream edit made (§3) was the minimum needed for the paper's own citations to trace, and it
   is disclosed in four places.
4. **The disputed denominator `216 805` still stands in the concept card** that downstream legs
   read first, together with a transposed sweep size (`50 847 503` for `50 847 533`). The paper
   carries the adjudicated figures and names the card's discrepancy; it does not edit the card.

**Result: no unresolved issue remains within this leg's remit.** Everything deferred is deferred
to a named owner, in writing, above.

---

*Artifact of leg `write-paper`, molecule `edit-20260726-5e79`, run `germ-20260725-791a7c45`,
re-attack loop `reattack-20260726-57d1`, **round 2**. Supersedes the round-1 authoring log in
place. The conjecture `F` remains **OPEN** — neither proved nor refuted by either round. The
evidence gate is **BLOCKED**. No citation clearance exists.*
