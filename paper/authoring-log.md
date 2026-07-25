# Authoring log — `paper/paper.tex`

**Molecule:** `edit-20260725-37f8` (formula `editorial-work`, crew role: writer)
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-25
**Source of record:** `synthesize/synthesis.md` (520 lines), plus the eleven leg artifacts it
folds.
**External attribution:** Noogram. **Delivery posture:** staged.

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
$ latexmk -xelatex -interaction=nonstopmode paper.tex
```

| Gate | Result |
|---|---|
| `latexmk -xelatex` exit status | **0** |
| pages produced | **25** |
| `paper.pdf` size | 239093 bytes |
| unresolved `\ref` | **0** |
| unresolved `\cite` | **0** |
| `biber` warnings / errors | **0** |
| Overfull `\hbox` | **0** |
| Underfull `\hbox` | **1** — one table cell of typewriter tokens that cannot hyphenate; cosmetic, no text loss |

Reproduce with `latexmk -C && latexmk -xelatex paper.tex`.

## 3. Citation traceability

Every `\cite{}` key in `paper.tex` resolves to an entry in `references.bib`, and every entry
in `references.bib` is cited. Mechanically checked:

```
cited keys: 22   bib keys: 22
cited-but-missing-from-bib: (none)
in-bib-but-never-cited:     (none)
```

**Twenty of the twenty-two** correspond one-to-one to rows of
`source-ledger/source-ledger.md` §2 (the run's ledger: 20 rows — 11 at L0, 3 at L1,
4 at L2_strong, 2 at L2_weak, 0 at L3).

**Two are PENDING LEDGER ROWS**, and this is flagged in three places (the `references.bib`
header comment, §10.3 "Source provenance" of the paper, and here):

| Key | Status |
|---|---|
| `carneiro2019fourier` | Fetched, version-pinned (arXiv:1708.04122v2, MD5 `2fdff58bc850508d8f124b4e7ad6b594`) and read at the locator by leg `proof-attempt__1`; proposed as a ledger addition; **not folded into the ledger artifact**. Tier L1 (preprint pagination against journal coordinates). |
| `visser2018andrica` | Fetched, version-pinned (arXiv:1804.02500v3, MD5 `38b405e83543fb6968754f90bac9c2d4`) and read at the locator by the same leg; proposed as a ledger addition; **not folded in**. Tier L0 (cited as preprint, locators agree). |

Without these two, §5 (the RH route) could not be written at all: card `L11` of the run
declared in its own words that "the sentence 'RH does not help' currently rests on an
unverified recall". Suppressing them would have been the less honest choice; citing them
silently would have been worse. They are cited and flagged.

## 4. The `proved` discipline

The brief requires that `proved` be claimed only for targets the kernel leg established. The
paper fixes an explicit vocabulary in §1.4 and holds to it:

- `[K]` — machine-checked by the Lean kernel. **Exactly one result carries it:**
  Lemma 2.1 (the reduction `F ⟺ ∀n≥1, g_n < T_n`), which is what `lean-probe` discharged
  with real proof terms (audit over 60 declarations, one `sorryAx` dependent, and that one is
  the conjecture itself).
- `[P]`, `[P·s]`, `[C]`, `[H]` — paper proof, paper proof on an unopened source, exhaustive
  computation, heuristic. Each is labelled at the point of use.
- The word *proved*, unqualified, is reserved for `[K]`. A boxed statement in §1.4 says
  outright that `F` is neither proved nor refuted.

**`F` is nowhere claimed to be true or false.** The synthesis's standing instruction is
carried verbatim into the conclusion.

## 5. Brief coverage — every enumerated point

| Brief requirement | Where | Status |
|---|---|---|
| LaTeX, never markdown-only | `paper/paper.tex` | done |
| `\documentclass{article}` | l.1 | done |
| `amsmath` + `amsthm` + `hyperref` | preamble | done |
| theorem / lemma / definition / proof environments | preamble + throughout | done — 31 numbered theorem-like results (definitions, lemmas, propositions, theorems, corollaries) plus 19 numbered remarks and caveats |
| every proof opens with an italic *Idea:* line | `\idea{}` macro | done — 23 proofs, 23 `\idea` lines, mechanically checked |
| `biblatex` over `paper/references.bib` | preamble, `\printbibliography` | done (backend `biber`) |
| every `\cite{}` traces to a source-ledger row | §10.3 + `references.bib` header | done, with two pending rows flagged (see §3 above) |
| abstract | p.1 | done |
| intro + literature | §1, incl. §1.3 in five groups | done |
| setup | §2 | done |
| main results | §3 (monotone bar), §4 (finite range), §5 (RH route), §6 (smooth model) | done |
| computational evidence | §7 | done |
| honest limitations | §9 (tension) + §10 (what remains open / what is not established) | done |
| references | `\printbibliography` | done — 22 entries, 22 distinct labels in the rendered list |
| compile with `latexmk -xelatex`, deliver `paper.pdf` | §2 above | done |
| toolchain + compile summary in `authoring-log.md` | this file | done |
| delivery posture: staged | §10.2, §10.3, Acknowledgements | done, stated three times |
| external attribution: Noogram | title block, Acknowledgements | done |
| `proved` only for kernel targets | §4 above | done |
| `paper/` git-tracked in the worktree | committed on `feat/edit-20260725-37f8` | done |

**Nothing in the brief was silently dropped.**

## 6. Editorial decisions, and why

1. **The Axler-sharpened constant `0.004479` is NOT quoted.** The skeptic leg's BLOCKER F2
   established that the derivation of that sharpened statement misapplies its upper bound on
   `T_m` by a factor `≈ ℓ²`, that the theorem as printed upstream is false by a factor `≈ 38`
   over part of its own validity range, and that the in-run numerical check reproduced the
   error rather than catching it. The repair is one line and **has not been applied**. The
   paper therefore states only the Dusart-only Theorem 3.10 with its constant `0.0623`, which
   the skeptic independently confirmed conservative, and Remark 3.11 says explicitly why the
   sharper constant is withheld. This follows the synthesis's own rule: *nothing here quotes
   `0.004479` as a derived constant.*
2. **The `m(n)` vocabulary collision (BLOCKER F1) is written out, not inherited.** §10.2 names
   the three inequivalent predicates, states the implication order, identifies which one the
   search pruning actually consumes, and records that the two apparently contradictory
   upstream headlines are both true of different predicates. It also states that the
   float64-noise-floor inference upstream is derived from the wrong predicate and does not
   survive. The paper is written entirely in the disambiguated vocabulary.
3. **The `55.92 %` statistic is omitted from the paper entirely.** Four fractions circulate in
   the corpus for one statistic because the counting convention was never written down, and
   the synthesis's independent recomputation found the numerators stable and the denominators
   differing by exactly one. The figure is also range-dependent (57.88 % at `10⁹`) and, by
   the corpus's own reading, uninformative about the pruning obligation. Rather than reprint
   a disputed number, the paper states only the qualitative fact it needs — that `T` decreases
   at about 55.9 % of steps below `3·10⁶`, i.e. that `T` is not monotone — which is what
   §3.1's argument actually consumes. *This is a deliberate omission and is recorded here so
   it is not read as an oversight.*
4. **Theorem 5.2 (the CMS envelope) is stated with its quantifier.** The upstream headline
   "at no other index whatsoever" is false as stated; Remark 5.3 gives the correct form ("at
   exactly one index in the range where the CMS bound is available") and explains that what
   excludes `n = 1, 2` is the source's hypothesis `p_n > 3`, not the arithmetic. This also
   dissolves the apparent conflict with the notebook leg that reported three certified primes.
5. **`p*(C)`'s mistyped lower endpoint is not reproduced.** The upstream table's stated range
   `10 ≤ p ≤ P` made its own values vacuous. The paper quotes the corrected reading
   (`p ∈ (1.111, 8099)` for `C = 0.1`, `p ∈ (1.010, 2 122 265)` for `C = 0.01`) without
   reprinting the broken definition.
6. **Unsourced items are marked as such, and used only negatively.** Brun–Titchmarsh, the
   second Hardy–Littlewood conjecture, and Montgomery–Vaughan have no ledger row in this run.
   They appear only to *name* obstructions (Caveat 3.13, §7.5) and never to support a positive
   claim; each is flagged inline.
7. **Theorem 5.15's gloss is separated from the theorem.** Remark 5.16 states the boxed
   counter-model result and then explicitly refuses the stronger informal reading ("no
   derivation using only growth and distribution can succeed"), because the derivation class
   is not formalised and is contingent on what this run fetched.
8. **The `2⁶⁴` frontier is cited, never claimed.** Theorem 2.3 is stated as a cited result,
   and §10.3 names `oliveira2014goldbach` — the gap table it rests on — as unopened, HTTP 403,
   Priority 3 for the citation gate, together with the exact consequence: if that table is
   incomplete, Proposition 4.6 and every use of Theorem 2.3 say nothing.

## 7. What this paper does NOT do — carried forward for the downstream verdict node

1. **The citation audit has not run.** No clearance is claimed; §10.3 states this and lists
   the three load-bearing unopened/under-located sources in priority order (Axler, Granville's
   pagination, Oliveira e Silva–Herzog–Pardi).
2. **The evidence gate on the underlying corpus stands at BLOCKED**, failing leg SKEPTIC, two
   unrepaired defects. §10.2 discloses both. This paper reconciles them *in this document*; it
   does **not** repair the upstream artifacts, which still carry them.
3. **No upstream artifact was modified by this leg.** The reconciliations live here only.
4. **No source was opened by this leg.** Every external fact is used at the tier the run's own
   ledger assigned it, and named with that tier where it is load-bearing.
5. **The Lean development was not re-built by this leg.** Its gate table (§8.1 of the paper)
   quotes the exit statuses `lean-probe` recorded.
6. **The `10¹¹` sweeps were not re-run by this leg.** They are reported at the figures their
   own legs recorded, independently reproduced there by two code paths.
7. **The independent adversarial review is a separate molecule downstream** (the
   editorial-verdict node). Step 2 of this molecule is authoring-time self-review only.

## 8. Self-review pass (Step 2)

Checklist from the formula, and the result of each.

**Coherence.** Read end to end as one document. Notation is fixed once in §2.1 and used
without drift: `p_n` one-indexed throughout, `L_n = log p_n`, `g_n`, `T_n`, `ρ_n`. Two
symbols needed disambiguation and were given distinct names rather than being overloaded:
`S(x) = log²x − log x − 1.17` (Kourbatov's monotone surrogate, §3.2), `B(x) = log²x − 1.1 log x`
(the Dusart-only floor, §4.1), and `S♯(g)` (the inverse of `B`, Corollary 4.5). The set
`S = {3}` of Theorem 5.2 is a third use of the letter `S`; it is scoped to one theorem and
declared in its statement — noted, judged acceptable, not repaired, because renaming it would
break the correspondence with the source artifact.

*Fixes applied during the pass, in the order found:*

1. **Two dangling cross-references, and they were real.** The verification list of §7.3 uses
   manual item tags (`\item[V1]`, `\item[V2]`, `\item[V6]`). A manual optional tag does
   **not** set LaTeX's `\@currentlabel`, so the three `\label`s attached to those items
   silently resolved to the enclosing *subsection* number. Three proofs (Theorem 3.6,
   Theorem 3.10, Proposition 4.8) were therefore citing "item V7.3" instead of "item V2",
   "item V1", "item V6". Caught by dumping `paper.aux` and comparing every label to its
   rendered number rather than by trusting that a compile without "undefined reference"
   warnings means the references are right — an unresolved reference warns, a *wrongly*
   resolved one does not. Fixed by dropping the labels and writing the item tags literally.
2. **Two symbols that do not survive extraction from the PDF.** `\ll` and `\asymp` produce
   glyphs that are absent from the extracted text layer, while every other operator (`≤`,
   `≥`, `⇒`, `∼`) extracts correctly — so a reader copying a formula out of the PDF would
   lose exactly the relation symbol and read `g_n  p^{0.525}` as an equation. Replaced:
   `g_n \ll p_n^{0.525}` by `g_n = O(p_n^{0.525})` (twice), `y \asymp x/\log x` by "of
   order", and Corollary 5.10's `\asymp` display by an arrow plus a prose clause.
3. **An arithmetic slip in the proof of Proposition 6.1.** `log(5 log 5)` was stated as
   `2.0873`; recomputed it is `2.0853229…`. The conclusion is unaffected (the bracket at
   `x = 5` is `1.6213`, so the sign is negative either way, by a margin of `0.464`), but the
   printed digit was wrong. Corrected.
4. **A garbled scale sentence in §10.4.** "8.27 decades short of 2⁶⁴ and about 12.8 decades
   short of it from the 3·10⁶ scale" conflated two measurements against two different
   baselines in one clause. Split into two sentences, each naming its own scale.
5. Typographic: the two tables that overflowed the text block were given explicit `p{}`
   column widths; a long inline display (the Ford–Green–Konyagin–Tao bound) was promoted to
   a display; the Mathlib revision hash was given explicit break points. Final state: **0
   overfull boxes**, 1 underfull (a table cell of typewriter tokens that cannot hyphenate).

Items 1–4 are corrections of substance, not polish, and are listed so the downstream verdict
node can see what the self-review actually caught. No mathematical *content* changed: no
theorem statement, no constant other than the corrected `2.0853`, and no claim about `F`.

**Completeness.** Every brief requirement has a section — see §5 above, all rows "done".

**Compliance.** Delivery posture (staged) stated in §10.2, §10.3 and the Acknowledgements.
External attribution (Noogram) in the title block and the Acknowledgements. No confidential
material appears: the paper contains mathematics, cited literature, and this run's own
computational results; no path, no operator identity, no internal molecule ID appears in the
PDF.

**Sources — spot-checks.** Three citations were checked against the ledger row that carries
them, statement by statement:

1. `\cite[Thm.~6.9, eq.~(6.6)]{dusart2010estimates}` for `π(x) ≤ x/(log x − 1.1)`, `x ≥ 60184`.
   Ledger §2.6 records exactly this at exactly this locator, tier **L0**, PDF fetched, MD5
   `b6540b68b8083df37266f57fab34db68`. **Match.**
2. `\cite[\S2, Thm.~1]{kourbatov2015bounds}` for `F ⟹ g_k < log²p_k − log p_k − 1` for `k > 9`.
   Ledger §2.1 records the verbatim statement at that locator, tier **L0**, arXiv v4, MD5
   `5b4b61ea6ad4d5bcca2dbf3bd604e151`, with the explicit warning that the `k > 9` threshold is
   part of the hypothesis and must not be dropped. The paper keeps the threshold in
   equation (2) and in every use. **Match.**
3. `\cite[preprint p.~12]{granville1995cramer}` for `max gap ⪆ 2e^{−γ} log²x`. Ledger §2.2
   records the verbatim sentence at preprint p. 12, tier **L1** *precisely because the
   pagination is the preprint's*. The paper cites it as "preprint p. 12", says so in the
   bibliography `note` field, and flags it as citation-gate Priority 2 in §10.3. **Match, and
   the tier is honoured rather than silently upgraded.**

**Unresolved issues after the pass:** none that are repairable at this leg's perimeter. Two
are explicitly deferred, with justification:

- *Deferred to the citation gate:* the three unopened/under-located sources of §10.3. This leg
  opened no source by construction (perimeter), so it cannot raise a tier.
- *Deferred to a repair round:* the two upstream BLOCKERs. Both are disclosed in §10.2; the
  repairs are named and one-paragraph each, but applying them means editing artifacts owned by
  other molecules, which is outside this leg's perimeter and would destroy the audit trail the
  downstream verdict node needs.

---

*Artifact of leg `write-paper`, molecule `edit-20260725-37f8`, run `germ-20260725-791a7c45`.
The conjecture `F` remains **OPEN** — neither proved nor refuted. The evidence gate on the
underlying corpus is **BLOCKED**. The citation audit has **not** run.*
