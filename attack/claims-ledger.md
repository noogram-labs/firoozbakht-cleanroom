# claims-ledger.md — every claim and every citation the paper makes, with its support

**Molecule:** `review-20260726-7d55` (formula `temp-review`, crew role: **reviewer**) — **ROUND 2**
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-26
**Target:** `paper/paper.tex` (2460 lines, v5, round 2) + `paper/references.bib` + `paper/paper.pdf`
**Conjecture (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`. **`F` is OPEN.** Nothing in
this ledger proves or refutes it, and nothing in the paper claims to.

**This document supersedes the round-1 `claims-ledger.md`** (molecule `review-20260725-4b9d`,
which wrote it to its molecule directory only and never tracked it — this is therefore the
galaxy's first *tracked* claims ledger, and the round-1 copy is superseded rather than
overwritten, since it sits outside the tree). Round 1 scored a 1641-line paper against a citation
gate that was **BLOCKED**; round 2 scores a 2460-line paper against a citation gate that is
**PASS**. What changed and what did not is stated in §5.

**Author ≠ scorer.** This leg wrote no line of `paper.tex`. Every row below is a score for the
author to act on, not an edit made on their behalf.

---

## 0. Sources read (fail-closed pre-check)

| Input | Path | Present? | Verdict it carries |
|---|---|---|---|
| Paper | `paper/paper.tex` (2460 l.) + `references.bib` (22 entries) + `paper.pdf` (341 645 B) | **yes**, non-empty, all tracked | — |
| Evidence gate | `attack/evidence-verdict.md` (236 l., round 2) | **yes** | **BLOCKED** — failing leg SKEPTIC round 2 |
| Citation gate | `attack/verification-report.md` (295 l., round 2) | **yes** | **PASS** — 22/22 citekeys, 91/91 instances, 0 at L3 |
| Skeptic faults (live round) | `attack/re-attack/attack-round-2/faults.md` (493 l.) | **yes** | 3 BLOCKER, 3 MAJOR, 7 MINOR |
| Skeptic faults (round 1, superseded) | `attack/faults.md` (444 l.) | yes | F1, F2 — both disposed FIXED in round 2 |
| Source ledger | `attack/source-ledger.md` (1075 l., 22 rows) | **yes** | 13 L0 / 4 L1 / 3 L2_strong / 2 L2_weak / 0 L3 |
| Loop verdict | `attack/re-attack/reattack-verdict.json` | yes | `rounds_run=2`, `exit_reason=rounds-exhausted`, live round = 2 |

Neither fail-closed absence trigger fires on the *inputs*: the paper exists and is non-empty, and
both gate reports exist. The fail-closed rule fires instead on the **content** of the evidence
gate (§4).

**Independent recomputation.** Every numeric row tagged `[verified here]` below was recomputed by
this leg at 25–30 decimal digits with `mpmath`, or by an independent segmented sieve written for
this review — not read off the artifact being scored. That includes a full independent sieve to
`10^9` (`π(10^9) = 50 847 534`, 50 847 533 consecutive pairs), which reproduces the paper's sieve
validation row and its `50 847 533` index count, and finds **zero violations of `F`** and
`max_{n≥10} g_n/T_n = 0.78960` at `n = 1 319 945`, `p = 20 831 323` — consistent with (and below)
the paper's `10^11` record of `0.8317570`, which is attained above `10^9`.

---

## 1. Claims about the *status of `F`* — the ones that matter most

| # | Claim (paper location) | Asserted strength | Supported by | Tag |
|---|---|---|---|---|
| S1 | `F` is open; neither proved nor refuted in either round (abstract; §1.5; §7 box; §10) | stated as *not established* | evidence-verdict §0 "`F` remains OPEN"; faults R2 §7; `reattack-verdict.json` `kernel: UNPROVABLE_IN_BUDGET` | **CONFIRMED** |
| S2 | The word *proved*, unqualified, is reserved for `[K]` statements, "without exception" (§1.5) | methodological rule | the paper's own vocabulary table | **OVERCLAIM** — the rule has ≥5 exceptions in the paper's own prose (§3, row V3) |
| S3 | "`F` is numerically robust over the verified range and simultaneously incompatible with the standard Cramér–Granville heuristic; at least one of the two must fail" (§1.5 box) | *defensible summary*, no proof strength | §9 tension + `granville1995cramer` p.12 (ledger L1) + §8 sweep | **CONFIRMED** |
| S4 | Do not write "Firoozbakht is true"/"is false" (§10) | instruction | — | **CONFIRMED** |
| S5 | The underlying corpus's evidence gate stands at **BLOCKED** on three named seams (abstract; §7.3 box; Acknowledgements) | self-report | `attack/evidence-verdict.md` verdict line, verbatim | **CONFIRMED** (the paper reports its own gate accurately) |
| S6 | "No citation clearance exists for this paper, in either round" / "the citation audit for this paper **has not been run**" / "no round-2 audit exists" (abstract l.97; §1.4 l.268; §7.4 l.2350-2352; Acknowledgements l.2454) | asserted as fact | **contradicted** by `attack/verification-report.md`, committed at `51756c5`, which audits `paper/paper.tex` v5 + `references.bib` and returns **PASS** | **OVERCLAIM** (unsupported assertion of a negative fact — see §3, row V2) |

---

## 2. Mathematical claims, by section

`[K]` machine-checked · `[P]` paper proof · `[P·s]` paper proof on an unopened/contested source ·
`[C]` exhaustive finite computation · `[H]` heuristic.

### 2.1 The formal substrate (§2–§3)

| # | Claim | Asserted | Supported by | Tag |
|---|---|---|---|---|
| K1 | Lemma 2.1: `F ↔ (∀n≥1, g_n < T_n)` with `T_n := p_n(p_n^{1/n}−1)` | **`[K]`** machine-checked | evidence-verdict §1 KERNEL leg **PASS**: `lake build` exit 0 (2208 jobs), audit exit 0/0, 63 declarations, exactly 1 `sorryAx` dependent | **CONFIRMED** |
| K2 | Thm 3.1 (Bertrand barrier): Mathlib's only prime-gap bound is insufficient at **every** `n ≥ 2` | **`[K]`** | `attack/re-attack/attack-round-2/lean-probe-report.md` §1; 3 new `sorry`-free theorems in `lean/Firoozbakht/Barrier.lean`; skeptic independently re-ran every gate exit code and the `Statement.lean` SHA-256 | **CONFIRMED** |
| K3 | Exactly one `sorryAx` dependent over 63 declarations, namely `F` itself; 1 live `sorry` token (`Statement.lean:186`); no `native_decide`/`axiom`/`unsafe` | **`[K]`** | evidence-verdict §1 table, every row traced to the probe report line number | **CONFIRMED** |
| K4 | Passing the kernel leg is **not** the claim "proved"; the kernel verdict on `F` is `UNPROVABLE_IN_BUDGET` (§7.3 box) | disclaimer | `reattack-verdict.json` `final_round.kernel` | **CONFIRMED** |
| K5 | `F` is *not* formalised beyond the reduction; the missing input is named (Caveat 3.x) | limitation | probe report §1 line 46 (the one declared build warning is the open target) | **CONFIRMED** |

### 2.2 First-failure maximality and the four predicates (§4) — the F1 repair

| # | Claim | Asserted | Supported by | Tag |
|---|---|---|---|---|
| P1 | The pruning lemma carried **three inequivalent** statements under one name; named apart as `(P6′-pair)`, `(P6′-gov)`, `(P6′-min)`, with a fourth `(P6′-rec)` nobody was measuring (Def. 4.1) | `[P]` | round-1 F1 (BLOCKER) → **FIXED**, per faults-R2 §5 and §0; the three predicates are given in symbols, exactly as the round-2 brief required | **CONFIRMED** |
| P2 | Thm 4.3: `(P6′-pair)` is **false**, two exhibited witnesses | `[C]` | faults-R2 §6: both witnesses independently reproduced at 60 digits by the skeptic; witnesses stand 10^8–10^12 ulps clear | **CONFIRMED** |
| P3 | Prop 4.4: exactly **17** exception indices below `10^9`, two clusters, extreme margin `−2.861·10⁻²` | `[C]` | in-run census; skeptic reproduced the full census | **CONFIRMED** |
| P4 | Caveat: the census counts **indices**, not **pairs**; upstream calls it a "complete census of admissible pairs", which it is not | disclosed defect | faults-R2 **R2-m2** (MINOR) | **CONFIRMED** — fault carried, not smoothed |
| P5 | Prop 4.6: `(P6′-gov)` and `(P6′-min)` are **formally incomparable**; `(P6′-gov) ⇒ (P6′-min)` is invalid | `[P]` | round-1 paper's strict ordering explicitly **withdrawn** (Rem. 4.7) | **CONFIRMED** |
| P6 | Rem 4.9: upstream prose calling `(P6′-min)` "the weakest"/"the easier obligation" is wrong; **the upstream prose has not been amended** | disclosed defect | faults-R2 **R2-M3** (MAJOR) | **CONFIRMED** — MAJOR addressed at its point of use |
| P7 | Thm 4.10: first-failure maximality follows from **either** survivor at a single index; the pruning is undamaged | `[P]` | round-2 proof-attempt `first-failure-maximality`; skeptic re-derived | **CONFIRMED** |

### 2.3 The unconditional finite-range architecture (§5–§6)

| # | Claim | Asserted | Supported by | Tag |
|---|---|---|---|---|
| R1 | Thm 6.x (finite-range): any first-occurrence gap table proves `F` up to that table's reach, on one explicit `π(x)` estimate | `[P]` | Dusart Thm 6.9 eq.(6.6), ledger **L0**; citation-gate §1.9 locator-match ✓ | **CONFIRMED** |
| R2 | Prop 6.x: reproduces the published constant **1920** at `2^64` with no tuning | `[C]` | `λ = log 2^64 = 44.3614195558…`, `λ²−1.1λ = 1919.13798349753…` ⇒ `g_{n_0} > 1919` **[verified here to 30 dps]**; Kourbatov's published 1920 matches | **CONFIRMED** |
| R3 | Caveat: the agreement is a consistency check, not an independent verification of the frontier | disclaimer | — | **CONFIRMED** |
| R4 | Table-free window `396 738 ≤ p_n ≤ 777 600`, and Prop 6.x: the window **closes permanently** above `7.776·10^5` | `[P]` | in-run derivation; listed as a dead end in §7.6 | **CONFIRMED** |
| R5 | Thm C(a) (Dusart only): `p_m ≤ 0.94970 p_{n_0} ⇒ g_m < g_{n_0}`, from `d* ≤ 0.051599 < 0.0516` | `[P·s]` | majorant over `[log 10^8, 1000]` in cells of 0.01 **[verified here: max = 0.0515990266817599… on the first cell, `ℓ = 18.4206807439…`; `e^{−0.0516} = 0.949708674346…`]** | **CONFIRMED** |
| R6 | Thm C(b) (with Axler): `p_m ≤ 0.998244 p_{n_0}`, from `ψ/(2ℓ−1) ≤ 0.0017568759` at the cell beginning `ℓ = 24.40621` | `[P·s]` | **[verified here: max = 0.00175687590387332… at cell start `ℓ = 24.4062076872…`; `e^{−0.0017569} = 0.998244642445…`]**; algebraic expansion `d(2ℓ−1)+d² ≥ 0.17 − 2.1/ℓ + v²/p_m` re-derived by hand and matches | **CONFIRMED** |
| R7 | Caveat (F2): round-1's printed bound "does not follow from its stated justification" and is wrong **by a factor `38.813747…`** at the bottom of its range (`0.169339812744…` vs `0.004362882388…`) | disclosed defect | round-1 F2 (BLOCKER) → **FIXED**; **[verified here: quotient = 38.8137468958056…, matching to every printed digit]** | **CONFIRMED** — this is exactly the round-2 brief's F2, repaired and correctly denominated |
| R8 | The retired repair: `v := ℓ²−ℓ−1−1/ℓ`, `d ≥ 0.0043636`, `p_m ≤ 0.995645906670… p_{n_0}` — **correct but not carried**, because its Axler row `x₀ = 1 772 201` exists in the preprint edition only | `[P·s]`, explicitly retired | **[verified here: `e^{−0.0043636} = 0.995645906669685…`]**; faults-R2 **R2-B1**/**R2-B3** | **CONFIRMED** — the brief's `v(1+v/x)` restatement is present, and the choice between the two repairs is stated as a choice |
| R9 | Round-1 vs round-2 comparison table, plus the exact-quadratic sanity anchors `0.051493457` / `0.0017560603`, both **below** the proved constants "as a majorant requires" | `[P]` | internally consistent; both anchors sit below R5/R6's constants ✓ | **CONFIRMED** |
| R10 | Caveat: "unconditional" for Thm C(a) means *unconditional given the published `2^64` height and a finite in-run sieve* — which is why both C-theorems carry `[P·s]`, not `[P]` | disclosed defect | faults-R2 **R2-M2** (MAJOR) | **CONFIRMED** — MAJOR addressed at its point of use |
| R11 | Prop 6.x (obstruction): the residual window needs an unconditional short-interval prime count sharp to `1 + 2/log p`, where Brun–Titchmarsh gives `≈2`; named the most tractable open node | `[P]`, open | Caveat "unsourced, used only negatively" | **CONFIRMED** |

### 2.4 The Riemann-Hypothesis route (§6)

| # | Claim | Asserted | Supported by | Tag |
|---|---|---|---|---|
| H1 | Lem: `√x > (25/22)log x` for all `x > 0`, minimum `h(625/121) = 0.40686238165947680…> 0`; hence `B_n > L_n²` at **every** index | `[P]` | **[verified here to 25 dps: `0.4068623816594768065…`]** | **CONFIRMED** |
| H2 | Thm (arithmetic clearance, no RH): `A = {n : B_n < T_n} = {1,2,3}`, same set with `≤` | `[P]` | 8-row table **[verified here: all eight `T_n`/`B_n` values reproduce to the 11 printed digits]** | **CONFIRMED** |
| H3 | Thm: the CMS envelope certifies `F` at **exactly one index of the range where the bound is available**, `n = 3` | `[P]` | `S = A ∩ [3,∞) = {3}`; hypothesis `p_n > 3` from `carneiro2019fourier` §1.2 Thm 5 (ledger L0-locator ✓) | **CONFIRMED** |
| H4 | Round-1's headline "…and at no other index whatsoever" **is false as stated**; the quantifier is restored | correction | Rem. "Read the quantifier": `n = 1, 2` are excluded by the *source's hypothesis*, not the arithmetic | **CONFIRMED** — a self-correction, correctly scoped |
| H5 | Thm: no power-type envelope `Cx^θ(log x)^A` with `θ > 0` certifies beyond finitely many `n` | `[P]` | one-line `e^{θu}` vs `u²` argument, valid | **CONFIRMED** |
| H6 | Thm: the critical constant on the `√p log p` scale is **exactly `2/e = 0.7357588823428846…`**, with Lambert-`W` endpoints | `[P]` | `φ(x)=log x/√x` unimodal, `φ(e²)=2/e` **[verified here]**; both published constants `22/25`, `21/25` lie **above** `2/e` ⇒ empty set ✓ | **CONFIRMED** |
| H7 | To certify `F` to `2^64` on this scale one would need `C ≤ 1.009·10⁻⁸` | `[P]` | **[verified here: `(λ²−λ−1)/(√(2^64)·λ) = 1.009·10⁻⁸`]** | **CONFIRMED** |
| H8 | Cor: even `g_n = o(√p log p)` certifies at **no** index | `[P]` | explicit counter-sequence `g_n = √p L/log log p` | **CONFIRMED** |
| H9 | Caveat: the `limsup = 0` hypothesis (RH + pair correlation) is **reported, not proved** by CMS, attributed to three works not opened — carried at a strictly weaker tier | disclosed tier | citation-gate §1.20: the ledger's L2_weak sub-row is propagated entry-by-entry, not blanket | **CONFIRMED** |
| H10 | Thm (counter-model): Cramér's `limsup` hypothesis does **not** entail `F` over integer sequences | `[P]` | in-run construction | **CONFIRMED** |
| H11 | Cor: the band left for a candidate gap hypothesis has width `0.17` | `[P]` | derived from (A-low)/(A-high′) surplus | **CONFIRMED** |
| H12 | Caveat: **no difficulty ordering** between RH and `F` is claimed | disclaimer | — | **CONFIRMED** |
| H13 | The per-index constant `C_n := T_n/(√p_n L_n)` dissolves a silent contradiction between two artifacts ("one index" vs "`p ≤ 5`") — "the one seam in either round that the legs closed by themselves" | `[P]` | `B_n < T_n ⟺ C_n > 22/25`; both artifacts were level sets of one object ✓ | **CONFIRMED** |

### 2.5 Computation (§8)

| # | Claim | Asserted | Supported by | Tag |
|---|---|---|---|---|
| C1 | Exhaustive sweep to `10^11` = **4 118 054 812** consecutive pairs, two independent legs, **0 violations** | `[C]` | `π(10^11) = 4 118 054 813` ⇒ 4 118 054 812 pairs — arithmetic checks against the standard value | **CONFIRMED** |
| C2 | `max_{n≥10} ρ_n = 0.8317570` at `p_n = 25 056 082 087`, `g = 456`; `max g_n/L_n² = 0.7953487`, same prime | `[C]` | **[cross-checked here: `456/log²(25 056 082 087) = 0.79535`; implied `T_n = 548.24` against `L²−L−1 = 548.40` — mutually consistent]**; my independent sieve to `10^9` gives `0.78960`, strictly below and attained below the paper's argmax, as it must be | **CONFIRMED** |
| C3 | Round-2 added two further independent sweeps (`10^9` = 50 847 533 indices; `2·10^8` = 11 078 936), reproducing round 1 to every digit quoted | `[C]` | **[verified here: my own sieve gives `π(10^9) = 50 847 534`, i.e. 50 847 533 consecutive pairs ✓]** | **CONFIRMED** |
| C4 | Escalation discipline: every pair with `ρ ≥ 0.90` re-decided in arbitrary precision, and the verdict function **raises** rather than returns inside the error budget | `[C]` | design section; the sign-flipped application to the `(P6′-pair)` refutation is the corroborating instance | **CONFIRMED** |
| C5 | Only two pairs in the whole range reach `ρ ≥ 0.9`, both at `n < 5` (`ρ_2 = 0.9107`, `ρ_4 = 0.9120`) | `[C]` | **[verified here: `T_2 = 2.1961524227`, `g_2 = 2` ⇒ `ρ_2 = 0.9107`; `T_4 = 4.3860359319`, `g_4 = 4` ⇒ `ρ_4 = 0.9120`]** | **CONFIRMED** |
| C6 | `T` is non-monotone; `121 238/216 806 = 55.9200%` (`n≥10`) and `121 239/216 815 = 55.9182%` at `3·10^6`, rising to `≈57.88%` at `10^9` | `[C]` | Caveat: denominator disputed three times; **[verified here by independent sieve: `π(3·10^6) = 216 816`, hence 216 815 steps and 216 806 with `n ≥ 10` — the paper's figures are right and the upstream card's `216 805` is wrong]** | **CONFIRMED** — and this leg independently adjudicates the three-way dispute **in the paper's favour** |
| C7 | The `55.92%` statistic is **not diagnostic** for any of the four predicates | `[P]` | it measures single steps; the predicates compare across records | **CONFIRMED** |
| C8 | Disclosed: the concept card downstream legs read first still carries `216 805` and a transposed sweep size `50 847 503` for `50 847 533` | disclosed defect | faults-R2 **R2-M1** (MAJOR) | **CONFIRMED** — MAJOR addressed; **[the transposition is real: the true count is 50 847 533]**. ✅ **REPAIRED 2026-07-27** by the round-3 reconciliation leg: cards `L15`, `D5` and `INDEX` now read `216 806` (and `216 815` all-`n`), and `50 847 503 → 50 847 533` in both card `L15` and FFM §9. See `attack/reconciliation.md` §4 |

### 2.6 Self-description and limitations (§7, §10)

| # | Claim | Asserted | Supported by | Tag |
|---|---|---|---|---|
| L1 | Any proof of `F` yields `g_n = O(log² p_n)` unconditionally; best known is `O(p_n^{0.525})`, RH gives `≈√p log p` — both powers, `F` needs polylog | limitation | `baker2001difference` (L1, abstract-level ✓), `carneiro2019fourier` (L1 ✓) | **CONFIRMED** |
| L2 | There is **no induction mechanism**: `g_n` is not constrained by `g_1…g_{n−1}` | limitation | — | **CONFIRMED** |
| L3 | Round 2 sharpened the obstruction in three independent places, by legs not talking to each other | claim about method | formal (K2) + analytic (H5, H11) + numerical (crossover `n=245` unconditional, `n=3` under RH) | **CONFIRMED** |
| L4 | Round 2's review returned **three** new BLOCKERs; the count went up and the species changed; none is a mathematical error and none touches `F` | self-report | faults-R2 §0 table (3/3/7) and §7, verbatim | **CONFIRMED** |
| L5 | **R2-B1** — two correct, incompatible repairs of one defect; "the corpus contains no rule for choosing"; this paper chooses Thm C(b) and says so; **neither upstream document has been amended** | disclosed BLOCKER | faults-R2 R2-B1 | **CONFIRMED** — addressed, not resolved upstream |
| L6 | **R2-B2** — contradictory source tiers for `axler2014newbounds`; the paper is written in the corrected tier; the second document has not been amended | disclosed BLOCKER | faults-R2 R2-B2 (the ledger amendment reported as landed **was never made**) | **CONFIRMED** — addressed; note the citation gate has since promoted the row to **L0**, so the *paper's* tier is now the corpus's tier |
| L7 | **R2-B3** — an edition-fragile citation; the paper resolves its own exposure by not carrying that theorem | disclosed BLOCKER | faults-R2 R2-B3 | **CONFIRMED** — addressed at Rem. "the other repair, and why it is retired" |
| L8 | Two further live defects sit inside the repairs (census labelling; the "unconditional" label), both stated at their point of use | disclosed | P4, R10 | **CONFIRMED** |
| L9 | Rem: round 1 predicted this failure mode (fan-out with no reconciliation stage); round 2 widened the fan-out and reproduced the prediction; "more rounds *of this shape* will not converge" | structural claim | round-1 `faults.md`; faults-R2 §7's own recommendation for a single reconciliation leg | **CONFIRMED** — and independently corroborated by `reattack-verdict.json` `exit_reason: rounds-exhausted` |
| L10 | "**This paper is an honest report on a blocked corpus. It is not a seal.**" | posture | evidence-verdict BLOCKED | **CONFIRMED** |
| L11 | Ledger composition: 22 rows — 13 L0, 4 L1, 3 L2_strong, 2 L2_weak, **0 L3**; no citation rests on recall | claim about citations | citation-gate §2 summary table: exactly 13/4/3/2/0 ✓ | **CONFIRMED** |
| L12 | `carneiro2019fourier` and `visser2018andrica` were folded into the ledger **by the paper's own author leg**, outside its remit; the bibliographic envelope was verified but the interior locators were not re-opened; **both rows carry a standing re-audit obligation** | disclosed seam | citation-gate §4 confirms the fold closed round 1's BLOCKER, and §1.20-1.21 re-verifies every locator invoked against §2.8's statement table — an *independent* leg has now checked what the author leg did not | **CONFIRMED** — and materially improved since the paper was written |
| L13 | "The citation audit for this paper has not been run… no round-2 audit exists" (§7.4), + abstract + Acknowledgements | asserted fact | **FALSE** — `attack/verification-report.md` (round 2, molecule `cite-20260726-d5a8`) audits this exact `paper.tex` v5 and returns **PASS** | **OVERCLAIM** (see §3, V2) |
| L14 | Scale: the in-run sweep reached `10^11`, **8.27 decades short** of `2^64`; lemma checks at `3·10^6` are 12.8 decades short; "both sweeps verify the lemmas, not the range" | limitation | `log10(2^64) = 19.27`, `19.27 − 11 = 8.27` ✓ **[verified here]**; `19.27 − 6.48 = 12.8` ✓ | **CONFIRMED** |
| L15 | Dead ends: Littlewood oscillation irrelevant; Bertrand provably closed; `(P6′-pair)` false and `gov ⇒ min` invalid; two-sided `π`-bound route cannot work; more sieving is not more evidence; table-free route permanently dead | limitation | K2, P2, P5, §8.5 | **CONFIRMED** |

---

## 3. Citation rows — all 22 citekeys

Source of truth: `attack/verification-report.md` (round 2, **PASS**), which independently
locator-matched **91/91 `\cite` instances** and **59 unique (citekey, locator) pairs** against
`attack/source-ledger.md`. This leg re-checked the bib↔tex correspondence and the four
underscore-normalized citekeys, and spot-checked the highest-risk rows.

| Citekey | Ledger tier | Instances | Locator-match | Second-hand framing carried in the paper? | Tag |
|---|---|---:|---|---|---|
| `firoozbakht1982unpublished` | L2_strong | 1 | ✓ | ✓ attribution/date only | **CONFIRMED** |
| `ribenboim2004little` | L2_strong | 3 | ✓ p.185 | ✓ self-declared unopened in §7.4 | **CONFIRMED** |
| `kourbatov2015bounds` | L0 | 9 | ✓ §1 eq.(1), §2 Thm 1, §4 Thm 3/4, §5 Thm 5 | n/a — v4 cited, per the ledger's mandatory-version flag; necessary/sufficient kept as separate implications, never an iff | **CONFIRMED** |
| `kourbatov2015verification` | L0 | 4 | ✓ endnotes 5 Jan 2023 | n/a — quotes the **endnote** `2^64`, not the title's `4·10^18` | **CONFIRMED** |
| `cramer1936order` | L0 | 3 | ✓ p.24 eq.(4), p.27 | n/a — the paper's hazard separates the *proved* urn-model claim (p.27) from the *suggested* prime analogue (p.24) | **CONFIRMED** |
| `granville1995cramer` | L1 | 4 | ✓ preprint p.12 | ✓ every locator prefixed "preprint"; bib note pins pagination 1–16 | **CONFIRMED** |
| `ferreira2017consequences` | L0 | 9 | ✓ Thm 2.2, Lem 3.2, Cons 3.3, Thm 4.5, Thm 5.1, Thm 5.2 | n/a — Thm 5.2's "infinitely often" never drifts to "eventually" | **CONFIRMED** |
| `sun2013sequence` | L0 | 3 | ✓ Thm 2.1, §1 | n/a — labelled "weaker `+1` variant" | **CONFIRMED** |
| `dusart2010estimates` | L0 | 8 | ✓ Prop 6.8, Thm 6.9 eq.(6.6) | n/a | **CONFIRMED** |
| `axler2014newbounds` | **L0** (promoted 2026-07-26) | 4 | ✓ (no bare corollary number cited at all) | n/a — the edition split gets a dedicated hazard block, and the `(2.1,0,0,0)` / `x₀=6 690 557` row present in **both** editions is chosen for Thm C(b) | **CONFIRMED** — the ledger's highest-risk row, actively neutralised |
| `baker2001difference` | L1 | 6 | ✓ abstract-level only | ✓ self-declared; no constant quoted | **CONFIRMED** |
| `ford2016large` | L1 | 3 | ✓ abstract-level only | ✓ corrected `(log log log X)²` exponent used | **CONFIRMED** |
| `oliveira2014goldbach` | **L2_weak** | 4 | ✓ | ✓ never opened (publisher 403); cited only as the computational basis *reported by Kourbatov*; named **priority 2** in §7.4 | **CONFIRMED** |
| `shanks1964maximal` | L2_weak | 2 | ✓ | ✓ attribution only | **CONFIRMED** |
| `farhadian2017new` | L2_strong | 2 | ✓ | ✓ attribution only | **CONFIRMED** |
| `visser2019verifying` | L0 | 6 | ✓ Conj 2, Conj 3 eq.(2.4), Abstract/§1 | n/a — `2^64`, not the superseded `4·10^18` | **CONFIRMED** |
| `oeisA111943` | L0 | 5 | ✓ | n/a — CSG record `0.9206` (Nyman 1999) matches the `%e` entry | **CONFIRMED** |
| `oeisA182514` | L0 | 1 | ✓ | n/a — sole published trace of Nicholson's conjecture | **CONFIRMED** |
| `mathlibNatNth` | L0 | 1 | ✓ | n/a | **CONFIRMED** |
| `mathlibNatPrimeNth` | L0 | 1 | ✓ | n/a | **CONFIRMED** |
| `carneiro2019fourier` | L1 (+L2_weak sub-row) | 7 | ✓ §1.2 Thm 5, Cor 4, after eq.(1.14) | ✓ the L2_weak sub-row is hazard-boxed separately — tier propagation entry-by-entry, not blanket | **CONFIRMED** |
| `visser2018andrica` | L0 | 5 | ✓ Thm 1 eq.(1.4), §2 Thm 4/5, §7 | n/a — the `≤`/`<` strictness discrepancy is recorded rather than smoothed | **CONFIRMED** |

**Citation totals: 22/22 resolved, 0 at L3, 0 fabricated, 0 orphans in either direction.
Zero `UNSUPPORTED-CITATION` rows.**

---

## 4. The three non-CONFIRMED rows, stated in full

| ID | Row | Tag | Evidence |
|---|---|---|---|
| **V1** | The paper's own **evidence gate stands at BLOCKED** (S5/L4–L7). The paper reports this accurately and honestly — but the fail-closed editorial rule is on the *gate*, not on the honesty of the reporting. | **gate failure** (not a claim defect) | `attack/evidence-verdict.md`: `VERDICT: BLOCKED`, failing leg SKEPTIC round 2, three unresolved BLOCKERs (R2-B1/B2/B3). Not an honest **DEGRADED**: the DEGRADED carve-out exists for a degraded *kernel* leg, and the kernel leg here passes **outright** (`formal_backend = 'lean'`, not `'none'`). |
| **V2** | "The citation audit for this paper **has not been run**, and no citation clearance is claimed… **no round-2 audit exists**" (§7.4 l.2350–2352), repeated in the abstract (l.97, "no citation clearance exists for this paper"), §1.4 (l.268, "in either round") and the Acknowledgements (l.2454). | **OVERCLAIM** — unsupported assertion of a negative fact | `attack/verification-report.md` is committed at `51756c5`, *after* the paper's own commit `d33dfe0`, audits `paper/paper.tex` v5 + `references.bib` by an independent leg (`cite-20260726-d5a8`), and returns **PASS** on all 22 citekeys and 91 instances. Four sentences of the paper are therefore false about the galaxy's committed state. This is the **same species of finding round 1 raised and the author fixed by other means** — the round-1 verdict flagged "twice states that its citation audit has not been run"; round 2 now states it four times, and it is now *more* wrong, because a round-2 audit exists and passed. Note the direction: this **understates** the paper's provenance. It is nonetheless a false assertion in a section whose entire purpose is the accurate reporting of provenance. |
| **V3** | §1.5: "The word *proved*, unqualified, is reserved in this paper for statements carrying `[K]`… and we use it without exception." | **OVERCLAIM** — the rule has exceptions | At least five `[P]`-strength results are described with unqualified "proved"/"proves" in running prose: l.74 (abstract, "the two survivors are **proved** formally incomparable" — Prop 4.6 is `[P]`), l.980 ("Lemma `lem:floor` **proves** `T_n > B(p_n)`" — `[P]`), l.1203 ("what can be **proved** outright is a windowed version" — `[P]`), l.1385 ("both below the constants **proved** above" — `[P·s]`), l.2391 ("Prop `prop:closure` **proves** the computation cannot be removed" — `[P]`). Mitigating, and stated so the REWRITE is correctly sized: every one of these sentences carries a `\ref` to a labelled statement that displays its own confidence code, so a reader can always recover the strength; and *none* of them is an inflation of `F`'s own status. The defect is that the paper's most load-bearing methodological promise — "without exception" — is not kept, and the first breach is in the **abstract**, where the labels are not visible. |

**Zero `UNSUPPORTED-CITATION`. Zero `UNADDRESSED-FAULT`** — all three round-2 BLOCKERs
(R2-B1/B2/B3) and all three MAJORs (R2-M1/M2/M3) are addressed at their point of use *and*
again in §7.3; the round-2 MINORs that touch the paper's own numbers (R2-m2 census labelling,
R2-m1's enumeration family, R2-m6's decay exponent) are carried rather than smoothed. Round 1's
F1 and F2 are both repaired, and this leg reproduced the F2 repair's factor `38.8137468958…`
and both branch constants independently.

---

## 5. What changed against round 1, and what did not

**Changed.**
- The citation gate went **BLOCKED → PASS**. Round 1's editorial REWRITE rested first on a
  BLOCKED citation gate naming `carneiro2019fourier` and `visser2018andrica` as tracing to no
  ledger row. That gap is closed: §2.8 of the ledger now carries both rows, and an independent
  leg re-verified every locator invoked. **That REWRITE reason is gone.**
- Round 1's two BLOCKERs (F1: three inequivalent `m(n)` predicates; F2: the factor-`38` bound)
  are both **repaired**, by re-derivation, and this leg reproduced both repairs numerically.
- The round-1 "universal about its own citations" OVERCLAIM is **fixed** — the paper's ledger
  composition claim (13/4/3/2/0) now matches the citation gate exactly.
- The paper roughly doubled in size (1641 → 2460 lines) and every new headline result
  (Bertrand barrier, restored RH quantifier, `2/e`, first-failure maximality) verified clean.

**Did not change.**
- The **evidence gate is still BLOCKED**, and therefore the editorial verdict is still
  **REWRITE**. The *reason* migrated from unrepaired mathematics to unreconciled repairs; the
  paper says so itself and argues it is a worse signal, not a better one.
- **`F` is still OPEN.**
- The "citation audit has not been run" self-description is still in the paper, and is now
  false rather than merely stale (V2).

---

*Artifact of leg `review` (step 1–2), molecule `review-20260726-7d55`, run
`germ-20260725-791a7c45`. Supersedes the round-1 `claims-ledger.md` in place. No number in this
document was copied from the artifact it scores without independent recomputation where
recomputation was possible; every `[verified here]` figure was produced by this leg.*
