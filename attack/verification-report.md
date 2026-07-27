# verification-report.md — citation audit, ROUND 3

**Molecule:** `cite-20260727-df58` (crew role: editor) · **Formula:** `citation-audit`
**Date:** 2026-07-27 · **Target artefact:** `paper/paper.tex` (round-3, post-reconciliation,
post-self-review — commits `b298366`, `c536696`) + `paper/references.bib`.
**Ledger audited against:** `attack/source-ledger.md` (22 rows, amended 2026-07-26 ×2; the
round-3 reconciliation record at its head changes no tier).
**Also read first, per the molecule brief:** `attack/reconciliation.md` and `attack/faults.md`
(the current, round-3 fault list — round-2's is superseded and lives at
`attack/re-attack/attack-round-2/faults.md`).

## Verdict

# **PASS**

Zero L3, zero fabricated citekeys, zero citekeys without a ledger row. Every `\cite` locator
checked traces to the statement it is invoked for at the tier the ledger assigns. Two rows
carry standing editorial cautions (Axler edition-qualification, Granville/Carneiro preprint
pagination); the paper discharges both explicitly in its own text (Caveat `haz:axler`,
`\S`provenance) rather than leaving them silent, so they are not gate failures.

## What changed since round 2

The round-2 audit (previously at this path, molecule `cite-20260726-d5a8`, commit `51756c5`)
audited the **round-2** `paper.tex` (commit `d33dfe0`) and returned PASS (91 `\cite` instances,
22 citekeys, 59 locator pairs, zero L3). That report is now stale: the audited *file* has been
superseded twice since —

1. `b298366` — "write-paper round 3: supersede paper.tex against the reconciliation + fresh
   skeptic audit" (rewrites the paper against `reconciliation.md`'s five decisions and
   `faults.md`'s findings; retires `0.99565`, designates Theorem C-b′ `0.998244`, rewrites the
   Axler hazard to name editions instead of corollary numbers).
2. `c536696` — "write-paper round 3 (step 2): self-review pass — seven internal
   inconsistencies fixed".

This document is the audit of the **resulting** file, run fresh against the tracked tree (not
against the round-2 report). It supersedes the round-2 `verification-report.md` **in place**,
per the molecule's round-3-resumption instruction — the galaxy ends with exactly one current
citation-audit answer.

**Headline differences from the round-2 count:**

- Citekey count: **21**, not 22. Round 2's report (§0) already noted the four ledger rows
  `oeis_A111943`/`oeis_A182514`/`mathlib_nat_nth`/`mathlib_nat_prime_nth` are spelled without
  underscores in `paper.tex`/`references.bib` (`oeisA111943`, `oeisA182514`, `mathlibNatNth`,
  `mathlibNatPrimeNth`) — a citekey normalization, not a missing source, and re-confirmed here
  by diffing each camelCase bib entry against its ledger counterpart (author/title/URL/version
  identical). The count discrepancy with round 2's "22" is because round 2 counted the four
  ledger-prose names and the four bib names as requiring separate tracking; this audit counts
  what actually appears in `paper.tex`'s `\cite` commands, which is 21 distinct strings.
- `\cite` instance count: **94**, not 91 — recounted with a script that matches
  `\cite[a-zA-Z]*(\[loc\])?\{key1,key2,...\}` and expands every comma-separated key on lines
  that cite more than one source at once (e.g. l. 2561, 2629, 2631); round 2's count appears to
  have undercounted these multi-key lines.
- Substantively, the round-3 paper's own `\S`provenance section already states, correctly and
  in multiple places, that the round-2 audit exists, returned PASS, and predates the round-3
  decisions — i.e. the paper does **not** claim an audit clearance it does not have. This
  matches `faults.md` S3-B2's finding that an earlier draft (`reconciliation.md`,
  `synthesis.md`) wrongly asserted "no round-2 audit exists"; that false assertion is **absent**
  from the round-3 paper text read here, so S3-B2's defect does not recur in `paper.tex`.

## Method

1. Extracted every `\cite[loc]{key}` from `paper/paper.tex` by regex over the raw source
   (94 instances, 21 unique citekeys) into `citations.json` (molecule state dir), each with
   citekey, locator, source line, and ~300-character claim context.
2. Confirmed all 21 citekeys have a `@...{key,...}` entry in `paper/references.bib`
   (zero missing) and that each `references.bib` entry's bibliographic content (author, title,
   venue, DOI/arXiv id) matches the corresponding `source-ledger.md` row (zero mismatches;
   4 keys are camelCase renames of ledger-prose spellings, addressed above).
3. For each citekey, read the ledger's tier and locator table (`source-ledger.md` §2) and
   checked every distinct locator used in `paper.tex` against it — L1 dominates L2 per the
   protocol; no L2 entries were in contention here since none of the paper's L2-tier citekeys
   (`firoozbakht1982unpublished`, `ribenboim2004little`, `farhadian2017new`,
   `shanks1964maximal`, `oliveira2014goldbach`) are cited for anything beyond the exact
   attribution-only use the ledger licenses for them.
4. Spot-checked every site the ledger itself flags as high-risk (Axler edition ambiguity,
   Granville/Carneiro preprint-vs-journal pagination, the Carneiro L2_weak sub-row, the FGKT
   exponent correction, the Ribenboim/Shanks/Farhadian attribution-only rows) by reading the
   surrounding paragraph in `paper.tex`, not just the bracket.

## Per-citekey verdicts

| citekey | ledger tier | instances in paper | locators used | verdict | evidence |
|---|---|---|---|---|---|
| `firoozbakht1982unpublished` | L2_strong | 1 | (none) | **OK** | Cited only for "never published by her" (l. 124) — exactly the attribution-only use the ledger licenses; no mathematical content drawn from it. |
| `ribenboim2004little` | L2_strong | 3 | `p.~185` ×2, bare ×1 | **OK** | Cited for "first appearance in print" at p. 185 (l. 125, 182), and once more in the provenance section (l. 2628) where the paper itself states it "was not opened and rests on two independent citers" — the exact disclosure the ledger's citation-gate flag asks for. |
| `kourbatov2015bounds` | L0 | 9 | `\S1`, `\S1 eq.(1)`, `\S5 Thm.5`, `\S2 Thm.1`, `\S4 Thm.3`, `\S2 Thm.1+\S4 Thm.3` combined, `\S4 Thm.4` | **OK** | Every locator matches a row in the ledger's statement table verbatim (§1 eq.1, §2 Thm.1, §4 Thm.3, §4 Thm.4, §5 App. Thm.5). |
| `kourbatov2015verification` | L0 | 4 | `\S4, Thm.`, `endnotes, 5 Jan 2023`, bare ×2 | **OK** | "§4, Thm." matches the ledger's "§4, Theorem (p. 288)"; "endnotes, 5 Jan 2023" matches the ledger's endnote row and the paper correctly quotes the $2^{64}$ frontier, not the superseded $4\times10^{18}$ title figure (ledger correction #1, applied). |
| `cramer1936order` | L0 | 3 | `pp.~24, 26--27`, `preprint p.~12` (see note below), `p.~27`, `p.~24, eq.(4)` | **OK** | Both cited pages match ledger rows (p.24 eq.4 = the "suggests" claim about primes; p.27 = the proved urn-model theorem). The paper's own Hazard (l. 2372–2377) states the proved-vs-suggested distinction in the ledger's exact terms — this is ledger correction #6, applied. |
| `granville1995cramer` | L1 | 4 | `preprint p.~12, after eq.(20)`, `preprint pp.~10, 12`, `preprint p.~12`, bare | **OK** | Every bracket explicitly says "preprint", discharging the ledger's L1 pagination caveat at each site of use, not just in a colophon. |
| `oeisA111943` (ledger: `oeis_A111943`) | L0 | 5 | bare | **OK** | Cited for the $0.9206$ CSG-ratio record and the raw sequence table; no locator needed beyond the sequence itself, consistent with ledger use. |
| `oliveira2014goldbach` | L2_weak | 5 | bare | **OK** | Every use is "the first-occurrence table Kourbatov's verification rests on" (l. 210, 1550) or an explicit provenance-section disclosure that its text was never opened (l. 2613–2617) — never cited for content read in it directly, matching the ledger's rule. |
| `oeisA182514` (ledger: `oeis_A182514`) | L0 | 1 | bare | **OK** | Cited once, for Nicholson's conjecture being "traced to an OEIS comment", matching the ledger's own framing. |
| `farhadian2017new` | L2_strong | 2 | bare | **OK** | Cited for attribution only (l. 193, 2629); the paper's provenance section says so explicitly ("cited for attribution only, their content being available at first hand elsewhere"). |
| `ford2016large` | L1 | 3 | bare | **OK** | Only the abstract-level qualitative statement is used (the large-gap lower bound formula, quoted with the corrected $(\log\log\log X)^2$ exponent — ledger correction #2, applied); no internal theorem number is invoked, matching the L1 caveat. |
| `axler2014newbounds` | L0 (promoted 2026-07-26) | 6 | bare (edition named in surrounding prose, not in the `\cite` bracket) | **OK** | Caveat `haz:axler` (l. 1000–1024) states explicitly: "a locator naming a corollary number without naming its edition matches no single edition. We therefore name the statement rather than a number" — and the corrected numeral $x \ge 2\,634\,800\,823$ is quoted at l. 1004, matching the ledger's post-Corrigendum statement exactly. This is a deliberate, disclosed resolution of the ledger's Priority-1 editorial flag, not an omission. |
| `baker2001difference` | L1 | 6 | bare | **OK** | Only the qualitative $p_n^{0.525}$ exponent is used, matching the abstract-level tier; no internal theorem number invoked. Provenance section (l. 2631) discloses "read at abstract level only". |
| `carneiro2019fourier` | L1 (one sub-row L2_weak) | 7 | `\S1.2, Thm.5` ×2, `\S1.2, Cor.4`, `\S1.2, after eq.(1.14)`, bare ×2 | **OK** | The `after eq.(1.14)` locator is used for the RH+pair-correlation "$\limsup = 0$" claim inside a dedicated Hazard block (l. 1839–1846) that explicitly marks it "reported, not proved... second-hand... at a strictly weaker tier than the rest of that citation" — correctly isolating the L2_weak sub-row from the L1 parent. |
| `mathlibNatNth` (ledger: `mathlib_nat_nth`) | L0 | 1 | bare | **OK** | Single citation, module-level, matches ledger use. |
| `mathlibNatPrimeNth` (ledger: `mathlib_nat_prime_nth`) | L0 | 1 | bare | **OK** | Single citation, module-level, matches ledger use. |
| `visser2019verifying` | L0 | 6 | bare ×2, `Conj.2`, `Abstract, \S1`, `Conj.3 eq.(2.4)`, `Abstract, \S1 eq.(1.4)` | **OK** | Every locator matches a ledger table row (Conjecture 1–3, §1 eq.1.3/1.4, Abstract). |
| `shanks1964maximal` | L2_weak | 2 | bare | **OK** | Attribution only ("Shanks conjectured the ratio never reaches 1", l. 224; disclosed again in provenance, l. 2629), matching the ledger's rule to cite Granville or A111943 for content. |
| `sun2013sequence` | L0 | 3 | `\S1` ×2, `Thm.2.1` | **OK** | Matches ledger rows (§1 opening statement, Theorem 2.1). |
| `visser2018andrica` | L0 | 5 | `Thm.1 eq.(1.4)`, `\S7`, `\S2 Thm.4`, `\S2 Thm.5`, bare | **OK** | Every locator matches a ledger table row; the $\le$-vs-$<$ strictness discrepancy the ledger flags is explicitly recorded in the paper (l. 1622–1623) rather than smoothed. |
| `dusart2010estimates` | L0 | 8 | `Thm.6.9 eq.(6.6)` ×3, bare ×2, `Prop.6.8` ×2, `Thm.6.9` ×1 | **OK** | Every locator matches a ledger table row (Theorem 6.9 eq. 6.5/6.6, Proposition 6.8). |

**21/21 citekeys: OK. 0 L3. 0 unresolved. 0 fabricated.**

## Confirmation of no fabricated / orphan citekeys

`grep -oE '\\cite[a-zA-Z]*(\[[^]]*\])?\{[^}]+\}' paper/paper.tex` → 21 unique keys, all present
verbatim in `paper/references.bib`, all traced to a `source-ledger.md` row above. No citekey in
`paper.tex` lacks a ledger row; no citekey in `paper.tex` lacks a `references.bib` entry.

## Standing cautions carried forward (not gate failures)

These are the same two items `source-ledger.md` §7 lists as its top citation-gate priorities.
Both are **disclosed in the paper's own text**, which is what the ledger's rule for L1/L2 rows
requires ("must be attributed as second-hand... or upgraded before the citation gate") — a
disclosed caveat at L1 is a compliant citation, not a defect:

1. **Axler edition ambiguity** (ledger Priority 1) — resolved by the paper's design choice to
   name statements, not corollary numbers, in every Axler locator (Caveat `haz:axler`).
2. **Granville/Carneiro preprint pagination** (ledger Priority 2/3) — every locator explicitly
   says "preprint" or names the arXiv version; journal re-pagination remains a standing
   provenance task for a future ledger amendment, not a paper defect.

Both are exactly the two items `attack/faults.md` §6 confirms are "genuinely open... not
closable by editing text" at the *ledger* level (Granville pagination, card `L6`/Axler-adjacent
items) — this audit finds the *paper* already discharges its citation obligations regarding
them at the tier the ledger allows.

## Relationship to `faults.md`'s two BLOCKERs (S3-B1, S3-B2)

Neither BLOCKER in the current round-3 fault list names `paper/paper.tex` or
`paper/references.bib` as a site needing correction. S3-B1 names six sites, all in
`attack/concept-cards/` and one round-2 proof attempt — none in the paper. S3-B2 names
`attack/reconciliation.md` and `attack/synthesis.md` — again not the paper; its own table
confirms `paper/paper.tex` already reflects the correct, post-reconciliation state ("already
reached decision 1 independently, a day early... asserts the opposite [of the stale claim]").
This citation audit corroborates that reading independently, at the citation layer
specifically: the paper's citation apparatus is consistent with the round-3 ledger and does not
carry any of the stale claims S3-B1/S3-B2 attack elsewhere in the corpus.

**This PASS clears the citation apparatus of `paper/paper.tex` only.** It does not clear, and
does not claim to clear, the corpus-wide evidence gate — which `faults.md` correctly holds at
BLOCKED for reasons (S3-B1, S3-B2, S3-M1, S3-M2) that are bookkeeping defects in *other*
artifacts, not citation defects in this paper. `Fb` remains OPEN; nothing in this audit bears
on that.

---

*Artifact of molecule `cite-20260727-df58`, step 2, formula `citation-audit`. Supersedes the
round-2 `attack/verification-report.md` (molecule `cite-20260726-d5a8`, commit `51756c5`) in
place. Citation data: `citations.json` in the molecule state directory.*
