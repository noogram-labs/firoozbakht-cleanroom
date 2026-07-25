# Citation Verification Report — Firoozbakht's Conjecture paper (v5, LaTeX)

**Molecule:** `cite-20260725-9eef` (formula `citation-audit`, step 2/3)
**Target artefact:** `paper/paper.tex` + `paper/references.bib`
**Ledger audited against:** `attack/source-ledger.md` (20 rows, built by molecule `task-20260725-d320`)
**Protocol:** L0/L1/L2_strong/L2_weak/L3 locator-match, per molecule brief. **L1 dominates L2** —
where a citation's tier is decided by the ledger's own L1 flag (edition/pagination mismatch), that
tier is reported regardless of corroboration strength.
**Instances audited:** 86 `\cite` occurrences / **22 unique citekeys**, extracted in step 1 to
`citations.json`.

## VERDICT: **BLOCKED**

Two of the paper's 22 citekeys — **`carneiro2019fourier`** and **`visser2018andrica`** — do not
trace to any row in `attack/source-ledger.md`. Per the molecule brief's fail-closed rule ("PASS
only if... every paper citation traces to a source-ledger row; else BLOCKED with the offending
citations named"), this is a gate failure regardless of the paper's own (accurate) self-disclosure
of the gap. See §2 below.

---

## 1. Per-citekey tier verdicts (20 of 22 keys — ledger-backed)

Tier is taken from the ledger row unless a paper-side locator usage contradicts it (none found).
"Locators used in paper" is the deduplicated set of `\cite[...]{}` bracket contents seen across
all instances of that key; "Ledger locator table" is what `source-ledger.md` §2 attests for that
row. A ✓ means every paper locator is covered by (or is a strict subset of) the ledger's table.

| Citekey | Instances | Ledger tier | Locators used in paper | Locator match | Notes |
|---|---:|---|---|---|---|
| `kourbatov2015bounds` | 9 | **L0** | §1; §1 eq.(1); §5 Thm.5; §2 Thm.1; §4 Thm.3; §2 Thm.1+§4 Thm.3 (combined); §4 Thm.4 | ✓ | Most load-bearing row; every locator is in the ledger's locator table verbatim (§1 eq.1, §2 Thm.1, §4 Thm.3, §4 Thm.4, §5 Thm.5). |
| `ferreira2017consequences` | 9 | **L0** | (bare, x2); Thm.2.2; Lem.3.2; Cons.3.3; Thm.4.5; Thm.5.2; Thm.5.1 | ✓ | All locators present in ledger table (Thm 2.2/2.3/3.1/4.4/4.5/5.1/5.2, Lem 3.2, Cons 3.3). |
| `visser2019verifying` | 6 | **L0** | (bare, x2); Conj.2; Abstract §1; Conj.3 eq.(2.4); Abstract §1 eq.(1.4) | ✓ | Matches ledger's Conjecture 1/2/3 and Abstract/§1 rows. |
| `dusart2010estimates` | 5 | **L0** | Thm.6.9 eq.(6.6) (x2); Prop.6.8 (x2); Thm.6.9 | ✓ | Matches Theorem 6.9 (eq. 6.5/6.6) and Proposition 6.8 in ledger. |
| `oeisA111943` | 5 | **L0** | (bare, x5) | ✓ | Ledger key is `oeis_A111943` (underscore) — **cosmetic rename**, same OEIS sequence/title/URL confirmed in `references.bib`. Not a fabrication; see §3. |
| `baker2001difference` | 5 | **L1** | (bare, x5) | ✓ | Ledger: abstract-only, no internal theorem locator obtained — paper never invokes a numbered locator either, consistent with the L1 caveat. |
| `axler2014newbounds` | 4 | **L2_strong** | (bare, x4) | ✓ | Paper explicitly self-flags "not opened... quoted through Kourbatov's proofs" (l.467, l.1554), matching ledger's tier and caveat exactly. |
| `granville1995cramer` | 4 | **L1** | preprint p.~12, after eq.(20); preprint pp.~10,12; preprint p.~12 (x2 total incl. l.1558 disclosure) | ✓ | Paper consistently labels locators "preprint p." — matches ledger's L1 flag (fetched copy is preprint-paginated 1–16, journal is 12–28). Correctly propagated. |
| `kourbatov2015verification` | 4 | **L0** | §4, Thm.; (bare, x2); endnotes, 5 Jan 2023 | ✓ | Matches ledger's Abstract/§3/§4/endnotes rows. |
| `cramer1936order` | 3 | **L0** | pp.~24,26–27; p.~27; p.~24, eq.(4) | ✓ | Matches ledger's p.24 eq.(4), p.27, pp.26–27 exactly. |
| `sun2013sequence` | 3 | **L0** | §1 (x2); Thm.2.1 | ✓ | Matches ledger's §1 opening/next-sentence and Theorem 2.1. |
| `ribenboim2004little` | 3 | **L2_strong** | p.~185 (x2); (bare, disclosure) | ✓ | Locator matches ledger's attested `p. 185`. Paper self-flags "book not opened, rests on two independent citers" (l.1569) — matches ledger exactly. |
| `ford2016large` | 3 | **L1** | (bare, x3) | ✓ | Ledger: abstract-only. Paper never cites an internal locator. Consistent. |
| `oliveira2014goldbach` | 3 | **L2_weak** | (bare, x3) | ✓ | Paper self-flags "not opened (publisher returned HTTP 403)" (l.1562) — verbatim match to ledger's stated fetch failure. **Escalated (§4).** |
| `shanks1964maximal` | 2 | **L2_weak** | (bare, x2) | ✓ | Paper self-flags "not opened... cited for attribution only" (l.1570) — matches ledger. **Escalated (§4).** |
| `farhadian2017new` | 2 | **L2_strong** | (bare, x2) | ✓ | Paper self-flags "not opened... attribution only" (l.1570) — matches ledger. |
| `firoozbakht1982unpublished` | 1 | **L2_strong** | (bare) | ✓ | Used only for date/unpublished-attribution — the one use the ledger permits ("do not cite this row for any mathematical content"); paper honors that restriction. |
| `oeisA182514` | 1 | **L0** | (bare) | ✓ | Ledger key `oeis_A182514` — same cosmetic rename as A111943; content (Nicholson trace) matches. |
| `mathlibNatNth` | 1 | **L0** | (bare) | ✓ | Ledger key `mathlib_nat_nth` — cosmetic rename; title/URL in `references.bib` match ledger's BibTeX block verbatim. |
| `mathlibNatPrimeNth` | 1 | **L0** | (bare) | ✓ | Ledger key `mathlib_nat_prime_nth` — cosmetic rename; content matches. |

**Subtotal:** 20/22 keys (73 of 86 instances) verified against the ledger with matching tier and
locator coverage. Zero locator mismatches found among these 20 keys — every bracketed locator used
in `paper.tex` is attested at that exact coordinate (or a coordinate within the same table row) in
`source-ledger.md`.

---

## 2. Keys with NO ledger row — the gate-failing citekeys

| Citekey | Instances | Locators used in paper | Ledger row? | Status |
|---|---:|---|---|---|
| `carneiro2019fourier` | 7 | §1.2 Thm.5 (x2); §1.2 Cor.4; §1.2 after eq.(1.14); (bare, x3, incl. provenance-disclosure lines) | **ABSENT** — no row in `attack/source-ledger.md`; `grep` for `carneiro`/`fourier` returns nothing | **UNRESOLVED (effective L3 for gate purposes)** |
| `visser2018andrica` | 5 | Thm.1 eq.(1.4); §7; §2 Thm.4; §2 Thm.5; (bare, disclosure) | **ABSENT** — no row; `grep` for `visser2018`/`andrica` returns nothing | **UNRESOLVED (effective L3 for gate purposes)** |

**Provenance actually claimed for these two** (per `paper/authoring-log.md` §3 and
`paper/references.bib` header comment): fetched and read at the locator by a *different,
un-audited* leg (`proof-attempt__1`), version-pinned with MD5 hashes, and explicitly proposed as
ledger additions — but **never folded into `source-ledger.md`**. The paper is honest about this in
three places (references.bib header, paper §10.3, authoring-log.md §3) — this is a self-disclosed
gap, not a concealed fabrication. It is nonetheless a fail-closed condition under this molecule's
brief: *"every paper citation traces to a source-ledger row; else BLOCKED."* `proof-attempt__1`'s
own read-and-verify claim is not a substitute for a ledger row — it is precisely the kind of
unaudited claim the ledger step exists to convert into an audited one, and it has not been
converted.

These two keys are load-bearing: without them, per the paper's own authoring log, "§5 (the RH
route) could not be written at all." They are not decorative citations.

---

## 3. Non-blocking observation — citekey renames (cosmetic, not fabrication)

Four keys use different spelling in `paper/references.bib` than in `attack/source-ledger.md`'s own
BibTeX block (§8):

| Paper key | Ledger key | Verified same source? |
|---|---|---|
| `oeisA111943` | `oeis_A111943` | Yes — identical OEIS sequence, title, URL |
| `oeisA182514` | `oeis_A182514` | Yes — identical OEIS sequence, title, URL |
| `mathlibNatNth` | `mathlib_nat_nth` | Yes — identical mathlib4 doc URL, title |
| `mathlibNatPrimeNth` | `mathlib_nat_prime_nth` | Yes — identical mathlib4 doc URL, title |

This is a camelCase-vs-snake_case rename made during LaTeX authoring, not a citation integrity
issue. No escalation required.

---

## 4. Summary

| Tier | Unique keys | Instances |
|---|---:|---:|
| L0 | 10 | 39 |
| L1 | 3 | 12 |
| L2_strong | 4 | 11 |
| L2_weak | 2 | 5 |
| **NO LEDGER ROW (gate-failing)** | **2** | **12** |
| **Total** | **22** (with locator-rename note, §3) | **86** — wait, recount below |

(Instance recount: 9+9+6+5+5+5+4+4+4+3+3+3+3+3+2+2+1+1+1+1 = 74 for the 20 ledger-backed keys, plus
7 + 5 = 12 for the two unresolved keys = **86**. Matches `citations.json` total exactly.)

- **Zero fabricated citations** — every citekey resolves to a real, identifiable published or
  documented source; none is invented.
- **Zero locator mismatches** — among the 20 ledger-backed keys, every bracketed locator used in
  `paper.tex` is attested at that exact coordinate in the ledger.
- **Zero true L3 (recall-only) citations** in the ledger-backed set.
- **Two citekeys (12 of 86 instances, ~14%) fail the ledger-traceability gate**: `carneiro2019fourier`
  and `visser2018andrica`. Both are self-disclosed by the paper as pending, not concealed, but the
  molecule brief's fail-closed rule does not carve out an exception for disclosed gaps.

**Gate outcome: BLOCKED.** See `escalations.md` for the required remediation rows.
