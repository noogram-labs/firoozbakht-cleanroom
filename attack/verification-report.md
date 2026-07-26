# Citation Verification Report — Firoozbakht's Conjecture paper (v5)

**Molecule:** `cite-20260726-d5a8` (formula `citation-audit`, step 2/3)
**Target artefact:** `paper/paper.tex` (LaTeX v5) + `paper/references.bib`
**Ledger audited against:** `attack/source-ledger.md` (22 rows, dated 2026-07-25, amended
2026-07-26 twice — Axler promotion, §2.8 fold)
**Protocol:** L0/L1/L2_strong/L2_weak/L3 locator-match, per the spore README §4 tier definitions
reproduced in the ledger's own §1. L1 dominates L2 — if L1 decides, short-circuit.
**Input:** `citations.json` (this molecule's step-1 output) — 91 `\cite` instances, 22 unique
citekeys, 59 unique (citekey, locator) pairs.

**HEADLINE VERDICT: PASS.** Zero L3 entries. Zero fabricated citations. All 22 citekeys used in
`paper.tex` have exactly one matching `@`-entry in `references.bib` (22/22, no orphans in either
direction). Every citation traces to a source-ledger row. Every L2_strong/L2_weak/L1-pagination
caveat the ledger imposes is carried into the paper's running text or its `references.bib` notes
— this paper does not silently upgrade a second-hand source to first-hand.

---

## 0. Bib-key ↔ ledger-row correspondence

Four ledger row names use underscores (`oeis_A111943`, `oeis_A182514`, `mathlib_nat_nth`,
`mathlib_nat_prime_nth`); the paper's `references.bib` and `paper.tex` use the same identifiers
without underscores (`oeisA111943`, `oeisA182514`, `mathlibNatNth`, `mathlibNatPrimeNth`). This is
a citekey-spelling normalization, not a different source — content (title, URL, OEIS sequence
number / mathlib4 doc page) is identical in both. Noted, not an escalation.

All other 18 citekeys are spelled identically between ledger and bib/tex.

---

## 1. Per-citekey verdicts

Tier column is the **ledger's own tier** for that row (this audit does not re-open primary
sources; it verifies (a) the citekey exists in the ledger, (b) the bib entry matches the ledger's
BibTeX, and (c) every locator invoked in `paper.tex` corresponds to a statement the ledger
actually records at that locator). Confidence reflects how well the *invoked claim* — not just
the *existence* of the citekey — matches the ledger's recorded statement.

### 1.1 `firoozbakht1982unpublished` — tier **L2_strong**
- **Instances:** 1 (line 118, no locator).
- **Verdict: L2_strong, confidence HIGH.** Used only for attribution/date ("was never published by
  her"), exactly the ledger's prescribed use ("Downstream use: attribution and date only. Do not
  cite this row for any mathematical content."). No mathematical content is drawn from it.

### 1.2 `ribenboim2004little` — tier **L2_strong**
- **Instances:** 3 — line 119 `[p.~185]`, line 176 `[p.~185]`, line 2371 (no locator, in the
  limitations section).
- **Verdict: L2_strong, confidence HIGH.** Locator `p. 185` matches the ledger's recorded locator
  exactly (attested twice, by Kourbatov and Sun, per ledger row). Line 2371 explicitly states "was
  not opened and rests on two independent citers" — the paper self-declares the tier in its own
  limitations section, matching the ledger's flag verbatim ("Flagged for the citation gate: if the
  final paper cites Ribenboim p. 185 as its statement source, a physical/PDF check is required to
  reach L0").

### 1.3 `kourbatov2015bounds` — tier **L0**
- **Instances:** 9 — locators `\S1`, `\S1, eq.~(1)`, `\S2, Thm.~1` (×2), `\S4, Thm.~3`, `\S4,
  Thm.~4`, `\S5, Thm.~5` (×2), `\S2 Thm.~1, \S4 Thm.~3` (combined).
- **Verdict: L0, confidence HIGH.** Every locator matches a row in the ledger's statement table
  verbatim: §1 eq.(1) (Firoozbakht ⟺ `p_{k+1} < p_k^{1+1/k}`), §2 Thm.1 (the `k>9` necessary
  direction), §4 Thm.3 (`b=1.17` sufficient direction), §4 Thm.4 (`b→1` family), §5 Thm.5
  (`T_n = L_n²-L_n-1+o(1)`). The paper correctly cites the arXiv v4 (implicit via the bib entry's
  `1506.03042v4` note) — the version carrying the §7 Corrigendum the ledger flags as mandatory
  ("Cite v4, never v1–v3"). The ledger's "Theorem 1 is one-directional; do not use as an
  equivalence" hazard is respected: the paper states the necessary and sufficient directions as
  separate implications (`eq:necessary`, `eq:sufficient`), never as an iff.

### 1.4 `kourbatov2015verification` — tier **L0**
- **Instances:** 4 — `\S4, Thm.`, `endnotes, 5 Jan 2023`, and 2 bare cites.
- **Verdict: L0, confidence HIGH.** The paper cites the 2023 endnotes for the `2⁶⁴` frontier
  (line 413, `[endnotes, 5 Jan 2023]`), not the paper's original title figure of `4×10¹⁸` — this is
  exactly the correction the ledger's §4.1 forces ("Quote the endnote, not the title"). Verified:
  `grep` shows the paper states `2^{64} \approx 1.8447\cdot10^{19}` at the point of use (lines
  415-416), matching the ledger's endnote statement.

### 1.5 `cramer1936order` — tier **L0**
- **Instances:** 3 — `p.~24, eq.~(4)`, `p.~27`, `pp.~24, 26--27`.
- **Verdict: L0, confidence HIGH.** All three locators match the ledger's table exactly (p.24
  eq.4 = the "suggested" analogue for primes; p.27 = the proved `limsup=1` theorem about the urn
  model). The paper's hazard box at line ~2201 ("Cramér did not conjecture limsup=1 about the
  primes... He proved it about his urn model... and suggested the analogue for the primes")
  reproduces the ledger's §4.6 correction verbatim in substance, correctly separating the *proved*
  claim (p.27, about `P_n`) from the *suggested* claim (p.24, about `p_n`).

### 1.6 `granville1995cramer` — tier **L1**
- **Instances:** 4 — `preprint p.~12`, `preprint p.~12, after eq.~(20)`, `preprint pp.~10, 12`,
  1 bare cite.
- **Verdict: L1, confidence HIGH.** Every locator in `paper.tex` is explicitly prefixed
  "preprint" — this discharges the ledger's Priority-2 obligation ("All Granville locators must be
  re-expressed against the journal copy, or explicitly marked 'preprint pagination'"). The
  `references.bib` entry additionally carries the note "Locators in the present paper are to the
  author's preprint, paginated 1–16." The constant `2e^{-\gamma} \approx 1.1229` and the direction
  (contradicts Firoozbakht) match the ledger's p.12 statement exactly.

### 1.7 `ferreira2017consequences` — tier **L0**
- **Instances:** 9 — `\S1`, `Thm.~2.2` (×2), `Lem.~3.2`, `Cons.~3.3`, `Thm.~4.5`, `Thm.~5.1`,
  `Thm.~5.2`, plus a bare cite.
- **Verdict: L0, confidence HIGH.** Every locator maps onto the ledger's statement table (§1
  attribution sentence, Thm.2.2 gap bound, Lem.3.2 `g_n<√n`, Cons.3.3 Sierpiński array, Thm.4.5
  implication chain, Thm.5.1 Zhang bounded gaps, Thm.5.2 the unconditional "infinitely often"
  result). The ledger's hazard on Thm.5.2 ("infinitely often, not eventually — do not let it drift
  into 'F holds for large n'") is respected: the paper never asserts an eventual form from this
  theorem.

### 1.8 `sun2013sequence` — tier **L0**
- **Instances:** 3 — `Thm.~2.1`, `\S1` (×2).
- **Verdict: L0, confidence HIGH.** Matches ledger's Theorem 2.1 (provable analogue for prime
  sums) and §1 (Sun's own restatement, the weaker `+1` gap-bound variant). The paper correctly
  labels Sun's variant "weaker $+1$ variant" (line 140 context), matching the ledger's verdict
  that Sun's is weaker than Kourbatov's sharp `-1` form.

### 1.9 `dusart2010estimates` — tier **L0**
- **Instances:** 8 — `Prop.~6.8` (×2), `Thm.~6.9` (bare), `Thm.~6.9, (6.6)` (×2), `Thm.~6.9,
  eq.~(6.6)`, 2 bare cites.
- **Verdict: L0, confidence HIGH.** All locators match the ledger's table: Theorem 6.9 eq.(6.6)
  (`x/(ln x-1) ≤ π(x) ≤ x/(ln x-1.1)`), Proposition 6.8 (prime existence in a short interval).

### 1.10 `axler2014newbounds` — tier **L0** (promoted from L2_strong, 2026-07-26)
- **Instances:** 4, all bare cites (no corollary number in the `\cite[...]` optional argument).
- **Verdict: L0, confidence HIGH — this is the citation the ledger flags as highest editorial
  risk, and the paper handles it correctly.** The ledger's §2 row and §7 Priority-1 item both
  demand: (a) never cite a corollary number without naming its edition, because the number differs
  by one between the arXiv preprint (Cor. 3.5/3.6) and the *Integers* 16 (2016) A22 journal
  version (Cor. 3.4/3.5); (b) never cite the preprint-only table row (`x₀=1,772,201`) against the
  journal. Verified in `paper.tex`: the paper never cites a bare corollary number for Axler at all
  — it states the inequality itself in prose (`\log x - 1 - 1.17/\log x < x/\pi(x)` for
  `x \ge 2,634,800,823`, lines 903-905) and dedicates an entire `\hazard` block
  (`haz:axler`, lines 911-936) to spelling out the edition split and explicitly choosing the
  `(2.1,0,0,0)/x₀=6,690,557` row that is present in *both* editions for its own Theorem C(b) fix
  (the exact repair the round-2 resumption brief flags as F2's correction target). This is the
  paper actively neutralizing the ledger's highest-priority hazard, not merely repeating it.

### 1.11 `baker2001difference` — tier **L1**
- **Instances:** 6, all bare cites.
- **Verdict: L1, confidence HIGH.** Used only for the qualitative statement `g_n = O(p_n^{0.525})`
  — exactly the abstract-level content the ledger's row supports ("adequate for the qualitative
  use both are put to, inadequate if any constant is quoted"). No numbered-theorem locator is
  invoked, consistent with L1's constraint (no internal theorem locator available). Line 2373-2374
  of the paper self-declares this tier ("read at abstract level only — adequate for the
  qualitative use... inadequate if any constant is quoted").

### 1.12 `ford2016large` — tier **L1**
- **Instances:** 3, all bare cites.
- **Verdict: L1, confidence HIGH.** Used only qualitatively ("best large-gap results... reach an
  iterated-log factor above log n but remain a full power of log below what a counterexample
  needs"). The paper's large-gap formula (line 225) uses the corrected exponent
  `(\log\log\log X)^2`, matching the ledger's §4.2 correction over the decompose leg's uncorrected
  `/\log\log\log n` — confirms the paper incorporated this fix, not merely the earlier
  decomposition's arithmetic.

### 1.13 `oliveira2014goldbach` — tier **L2_weak**
- **Instances:** 4, all bare cites.
- **Verdict: L2_weak, confidence HIGH (tier compliance), MODERATE (source itself unopened by
  design).** The ledger explicitly flags this as "the one row whose text was never opened" (AMS
  403) and mandates: "cite it only as the computational basis reported by Kourbatov, never for a
  statement read in it." The paper complies exactly — every instance frames it as "the
  first-occurrence prime-gap table of Oliveira e Silva, Herzog and Pardi" feeding
  Kourbatov's verification (lines 204, 415), and the paper's own limitations section (lines
  2362-2364) restates the L2_weak tier and the 403 explicitly: "`oliveira2014goldbach` was *not
  opened*... resting on it at the weakest ledger tier."

### 1.14 `ribenboim2004little`, `shanks1964maximal`, `farhadian2017new` — attribution-only group
- Covered individually above (§1.2) and jointly at line 2371-2372, where the paper groups all
  three as "not opened... cited for attribution only, their content being available at first hand
  elsewhere in the bibliography" — this is an accurate compressed restatement of the ledger's
  per-row "downstream rule: cite [X] for the statement; cite this row only for the attribution."

### 1.15 `visser2019verifying` — tier **L0**
- **Instances:** 6 — `Abstract, \S1`, `Abstract, \S1 eq.~(1.4)`, `Conj.~2`, `Conj.~3, eq.~(2.4)`,
  2 bare cites.
- **Verdict: L0, confidence HIGH.** All locators match the ledger's table (Conjecture 3 eqs.
  2.4-2.6 the three gap-bound conjectures, Conjecture 2 the implication chain, Abstract/§1 the
  `2⁶⁴` verification frontier). The paper's frontier claim (`2⁶⁴`, line 415-416) matches the
  ledger's corrected figure, not the superseded `4×10¹⁸`.

### 1.16 `oeisA111943` — tier **L0**
- **Instances:** 5, all bare cites.
- **Verdict: L0, confidence HIGH.** Used for the record CSG ratio `0.9206` (Nyman, 1999) — matches
  the ledger's `%e` table entry `0.9206@1693182318746371` and `%C` Nyman-1999 attribution exactly.

### 1.17 `oeisA182514` — tier **L0**
- **Instance:** 1, bare cite (line 186).
- **Verdict: L0, confidence HIGH.** Cited as the sole published trace of Nicholson's conjecture
  ("traced to an OEIS comment... otherwise unpublished") — matches the ledger's row exactly
  ("this is the primary published trace of Nicholson's conjecture, which is otherwise
  unpublished").

### 1.18 `mathlibNatNth` — tier **L0**
- **Instance:** 1, bare cite (line 535).
- **Verdict: L0, confidence HIGH.** Cited for `Nat.nth` being `noncomputable` — matches the
  ledger's documentation excerpt verbatim (`noncomputable def Nat.nth`).

### 1.19 `mathlibNatPrimeNth` — tier **L0**
- **Instance:** 1, bare cite (line 538).
- **Verdict: L0, confidence HIGH.** Cited for the five `@[simp]` base-case lemmas (`nth Prime 0=2`
  through `nth Prime 4=11`) — matches the ledger's row exactly.

### 1.20 `carneiro2019fourier` — tier **L1** (with one L2_weak sub-row)
- **Instances:** 7 — `\S1.2, Thm.~5` (×2), `\S1.2, Cor.~4`, `\S1.2, after eq.~(1.14)`, 3 bare
  cites.
- **Verdict: L1, confidence HIGH — this is a round-1→round-2 fold the ledger itself flags for
  mandatory re-audit (§2.8), and it passes.** Every substantive locator (§1.2 Thm.5 — the RH
  gap bound with hypothesis `p_n>3`; §1.2 Cor.4 — the `limsup ≤ 1/C⁺(B) < 21/25` asymptotic) is
  read verbatim from the ledger's §2.8 statement table. The one sub-row the ledger marks
  L2_weak — "after eq.(1.14), the `limsup=0` claim under RH+pair-correlation, reported not proved
  by CMS, attributed to three works not opened" — is correctly downgraded in the paper's own
  `\hazard[Provenance of the hypothesis of Corollary~\ref{cor:limsup0}]` block (lines 1697-1703):
  "is *reported*, not proved... therefore second-hand and is attributed as such here, at a
  strictly weaker tier than the rest of that citation." This is exact tier propagation, entry by
  entry, not a blanket citekey-level tier. `references.bib` additionally carries an explicit note
  pinning the preprint version and tier ("ledger tier L1").

### 1.21 `visser2018andrica` — tier **L0**
- **Instances:** 5 — `Thm.~1, eq.~(1.4)`, `\S2, Thm.~4`, `\S2, Thm.~5`, `\S7`, 1 bare cite.
- **Verdict: L0, confidence HIGH — the second round-1→round-2 fold, also re-audited here and
  passing.** §7's unconditional-verification claim (`< 1.836×10¹⁹`) and Theorem 1 eq.(1.4)'s
  hypothesis (`n≥3, p_n≥5`) match the ledger's §2.8 table exactly, including the ledger's own
  flagged non-strict/strict discrepancy (`≤` in CMS vs `<` in Visser), which the paper records
  rather than smooths (lines 1481-1484: "The two sources differ in strictness... every argument
  here consumes the bound only as a non-strict upper envelope, so the discrepancy is inert here,
  and it is recorded rather than smoothed").

---

## 2. Summary table

| Citekey | Ledger tier | Instances | Locator-match | Second-hand attribution carried? |
|---|---|---:|---|---|
| firoozbakht1982unpublished | L2_strong | 1 | ✓ | ✓ (attribution/date only) |
| ribenboim2004little | L2_strong | 3 | ✓ | ✓ (self-declared in text) |
| kourbatov2015bounds | L0 | 9 | ✓ | n/a |
| kourbatov2015verification | L0 | 4 | ✓ | n/a |
| cramer1936order | L0 | 3 | ✓ | n/a (model-vs-primes nuance carried) |
| granville1995cramer | L1 | 4 | ✓ | ✓ (preprint pagination flagged) |
| ferreira2017consequences | L0 | 9 | ✓ | n/a |
| sun2013sequence | L0 | 3 | ✓ | n/a |
| dusart2010estimates | L0 | 8 | ✓ | n/a |
| axler2014newbounds | L0 (promoted) | 4 | ✓ | n/a (edition hazard explicitly boxed) |
| baker2001difference | L1 | 6 | ✓ | ✓ (abstract-only, qualitative use) |
| ford2016large | L1 | 3 | ✓ | ✓ (abstract-only; corrected exponent used) |
| oliveira2014goldbach | L2_weak | 4 | ✓ | ✓ (never-opened, mediated-through-Kourbatov) |
| shanks1964maximal | L2_weak | 2 | ✓ | ✓ (attribution only) |
| farhadian2017new | L2_strong | 2 | ✓ | ✓ (attribution only) |
| visser2019verifying | L0 | 6 | ✓ | n/a |
| oeisA111943 | L0 | 5 | ✓ | n/a |
| oeisA182514 | L0 | 1 | ✓ | n/a |
| mathlibNatNth | L0 | 1 | ✓ | n/a |
| mathlibNatPrimeNth | L0 | 1 | ✓ | n/a |
| carneiro2019fourier | L1 (+L2_weak sub-row) | 7 | ✓ | ✓ (sub-row hazard-boxed) |
| visser2018andrica | L0 | 5 | ✓ | n/a |

**Totals: 22/22 citekeys L0/L1/L2_strong/L2_weak resolved, 0 at L3. 91/91 `\cite` instances
locator-matched against the ledger. 0 fabricated citations. 0 unresolved entries.**

---

## 3. Escalation-relevant tiers (for step 3)

Per the ledger's own rule ("An L2_strong or L2_weak row must be attributed as second-hand in the
text or be upgraded before the citation gate"), the following citekeys carry L2_strong or L2_weak
tiers and are checked in §1 above for correct second-hand framing — all pass, but they are the
candidate rows for step 3's escalation review since the ledger itself calls out standing
re-audit or never-opened obligations on several of them:

- `firoozbakht1982unpublished` (L2_strong)
- `ribenboim2004little` (L2_strong)
- `farhadian2017new` (L2_strong)
- `oliveira2014goldbach` (L2_weak) — ledger's own "lowest-confidence row", never opened (AMS 403)
- `shanks1964maximal` (L2_weak)
- `carneiro2019fourier`'s Montgomery/pair-correlation sub-row (L2_weak, embedded within an
  otherwise-L1 citekey)

No L3 rows exist anywhere in the ledger or the paper.

---

## 4. Comparison to round-1 citation audit

The round-1 audit of this paper's predecessor (`cite-20260725-9eef`) returned **BLOCKED** because
the round-1 paper cited `carneiro2019fourier` and `visser2018andrica` with no matching ledger row
(§2.8 had not yet been folded). That gap is now closed: source-ledger.md §2.8 (added
2026-07-26 by `edit-20260726-5e79`) carries both rows, and this audit independently re-verifies
every locator invoked against both against that section's statement table (§1.20-1.21 above). The
BLOCKER that stalled round 1's citation gate does not recur in round 2.

---

## 5. Verdict

**PASS.** No unresolved L3 citations. No fabricated citations. Every one of the 22 citekeys used
in `paper.tex` traces to a row in `attack/source-ledger.md`, every locator invoked in the paper
matches a statement the ledger records at that locator, and every L1/L2 tier caveat the ledger
imposes (pagination warnings, second-hand attribution, edition-splits, never-opened flags) is
carried into the paper's running text or its `references.bib` notes rather than silently smoothed
into a stronger tier than the source supports.
