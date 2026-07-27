# claims-ledger.md — every claim and every citation the paper makes, with its support

**Molecule:** `review-20260727-2c6d` (formula `temp-review`, crew role: **reviewer**) — **ROUND 3**
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-27
**Target:** `paper/paper.tex` (2733 lines, round 3) + `paper/references.bib` (22 entries) + `paper/paper.pdf`
**Conjecture (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`. **`F` is OPEN.** Nothing in
this ledger proves or refutes it, and nothing in the paper claims to.

> **This document supersedes the round-2 `claims-ledger.md` in place** (molecule
> `review-20260726-7d55`, commit `607c416`, which scored the 2460-line round-2 paper). The galaxy
> ends with exactly one current claims ledger. §6 states plainly what changed since round 2.

**Author ≠ scorer.** This leg wrote no line of `paper.tex`, `references.bib`, `faults.md`,
`evidence-verdict.md` or `verification-report.md`. Every row below is a score for the author to
act on, not an edit made on their behalf.

---

## 0. Sources read (fail-closed pre-check)

| Input | Path | Present? | Verdict it carries |
|---|---|---|---|
| Paper | `paper/paper.tex` (2733 l.), `paper/references.bib` (22 entries), `paper/paper.pdf` | **yes**, non-empty, all git-tracked | — |
| Evidence gate | `attack/evidence-verdict.md` (221 l., **round 3 v2**, molecule `task-20260727-2fee`) | **yes** | **BLOCKED** — failing leg SKEPTIC (round 3) |
| Citation gate | `attack/verification-report.md` (156 l., **round 3**, molecule `cite-20260727-df58`) | **yes** | **PASS** — but see row **G7**: it audits 21 of the paper's 22 citekeys |
| Skeptic faults (live) | `attack/faults.md` (357 l., **round 3**, molecule `task-20260727-5096`) | **yes** | 2 BLOCKER (S3-B1, S3-B2), 2 MAJOR (S3-M1, S3-M2), 5 MINOR |
| Reconciliation | `attack/reconciliation.md` (566 l., molecule `task-20260727-264e`) | yes | five decisions, all found correct by the round-3 skeptic |
| Skeptic faults (round 1 / round 2, superseded) | `attack/faults-round-1.md`, `attack/re-attack/attack-round-2/faults.md` | yes | preserved, banner-stamped superseded; dispositioned in `faults.md` §0 |
| Source ledger | `attack/source-ledger.md` (1099 l.) | **yes** | **22 rows: 13 L0 / 4 L1 / 3 L2_strong / 2 L2_weak / 0 L3** — recounted here from the row headers |
| Corpus / coverage | `attack/coverage-report.md` (249 l.) | yes | 27/27 adversarial statements behaved as specified |
| Loop verdict | `attack/re-attack/reattack-verdict.json` | yes | `rounds_run=2`, `exit_reason=rounds-exhausted` |

Neither fail-closed **absence** trigger fires: the paper exists and is non-empty, and both gate
reports exist. The fail-closed rule fires instead on the **content** of the evidence gate (§4).

### 0.1 What this leg recomputed itself, before reading any verdict

Scripts run in this leg's scratch, written from the paper's own statements; no upstream script
(`reconcile_recount.py`, `verify_syn*.py`, `s3_*.py`) was opened first.

| quantity | recomputed here | corpus value | agrees? |
|---|---|---|---|
| `π(10⁹)` (own segmented sieve) | **50 847 534** ⇒ 50 847 533 consecutive steps | 50 847 534 / 50 847 533 | ✓ |
| violations of `F` below `10⁹` | **0** | 0 | ✓ |
| `max_{n≥10} g_n/T_n` below `10⁹` | **0.78960** at `n = 1 319 945` | 0.78960 (round-2 ledger); paper's `10¹¹` record `0.8318` is attained above `10⁹` | ✓ consistent |
| maximal-gap records below `2·10⁸` | **28**; 12th at `15 683` (`g=44`); 28th at `191 912 783` (`g=248`); **25** below `10⁸` | 28 / same / 25 | ✓ |
| `log 2⁶⁴` | **44.36141955583649980…** | 44.36141955583649… | ✓ |
| `B(2⁶⁴) = L(L−1.1)` | **1919.1379834975328856…** | 1919.13798349753288… | ✓ |
| largest even `g` with `S♯(g) ≤ 2⁶⁴` | **1918** ⇒ violation needs `g ≥ 1920` | 1920 | ✓ |
| `p* ` (window closure root) | **777 600.7442975646…** | 777 600.744… | ✓ |
| `2/e` | **0.7357588823428846431…** | 0.7357588823428846… | ✓ |
| `A = {n : B_n < T_n}` and with `≤` | **{1,2,3}** both | {1,2,3} both | ✓ |
| `2e^{−γ}` | **1.1229189671337703** | 1.12292… | ✓ |
| ledger row tiers | **13 L0 / 4 L1 / 3 L2_strong / 2 L2_weak / 0 L3, 22 rows** | paper §provenance says the same | ✓ |
| distinct citekeys in `paper.tex` | **22**; `\cite` instances **94** | citation gate reports **21** and **94** | ✗ — **see G7** |

---

## 1. Claims about the *status of `F`*

| # | Claim (paper location) | Asserted strength | Supported by |
|---|---|---|---|
| S1 | `F` is open; neither proved nor refuted in any of the three rounds (abstract l.65–67; §1.3 l.307; §1.4 box l.354; §10) | stated as **not established** | `evidence-verdict.md` §0 ("`F` remains OPEN"); `faults.md` §6 ("`F` remains OPEN"); `reattack-verdict.json` `kernel: UNPROVABLE_IN_BUDGET` |
| S2 | The defensible summary: numerically robust over the verified range **and** incompatible with the Cramér–Granville heuristic; at least one must fail (§1.4 box l.355–358) | *defensible summary*, no proof strength | `granville1995cramer` preprint p.12 after eq.(20) (ledger L1) + eq.(1) necessary condition (`kourbatov2015bounds` §2 Thm.1, L0) + §8 sweep; the identical sentence is `faults.md` §6's own closing |
| S3 | Vocabulary rule: every theorem/lemma/proposition/corollary carries a confidence code or the word *cited*; **no statement is asserted at a strength above its code anywhere**; *machine-checked* is reserved for `𝒦` (§1.4 l.337–350) | methodological promise, **explicitly narrowed** after round 2 faulted the wider version | the paper's own vocabulary table; `\ref`-audit of every labelled statement; grep of "machine-checked" (10 sites, all `lem:reduction` / §3 barrier / title / conclusion) |
| S4 | Passing the kernel leg is **not** the claim "proved"; the kernel verdict on `F` is `UNPROVABLE_IN_BUDGET` (§9.4 box l.2516) | self-limiting statement | `reattack-verdict.json`; `lean-probe-report.md`; `faults.md` §1 (Lean gates re-executed) |

---

## 2. Machine-checked (`𝒦`) claims — the kernel leg

| # | Claim | Asserted strength | Supported by |
|---|---|---|---|
| K1 | `lem:reduction` — `F ↔ (∀n ≥ 1, g_n < T_n)`, `T_n := p_n(p_n^{1/n}−1)` | **`𝒦` machine-checked** in Lean 4/Mathlib | evidence-gate KERNEL leg **PASS**; `faults.md` §1 re-executed `lake build` (exit 0, 2208 jobs) and `audit_exhaustive.lean` (exit 0) directly, from a cold cache |
| K2 | `thm:barrier` (a)(b)(c) — `p_{n+1} ≤ 2p_n`; `p_n < 2ⁿ` for `n ≥ 2`; `p_n^{1+1/n} < 2p_n` for `n ≥ 2` — all `sorry`-free | **`𝒦`** | same; `lean-probe-report.md`; `Statement.lean` SHA-256 `6528868…04e004c1` frozen and reproduced by two legs |
| K3 | The development has **exactly one** `sorryAx` dependent over **63** declarations, namely `Firoozbakht.firoozbakht` | **`𝒦`**, exhaustive axiom audit | `faults.md` §1: "declarations scanned: 63; depending on sorryAx: [Firoozbakht.firoozbakht]" — re-run, not read |
| K4 | Bertrand's postulate is *provably* insufficient at every index `n ≥ 2` — a **barrier**, not a gap | **`𝒦`** (`thm:barrier`(c)), framed in `rem:barrier-scope` as "what the barrier is and is not" | as K2; `coverage-report.md` (adversarial corpus, 27/27) |

---

## 3. Paper-proof (`𝒫`) and computational (`𝒞`) mathematical claims

| # | Claim | Asserted strength | Supported by |
|---|---|---|---|
| M1 | `thm:verified` — `F` holds for every `n` with `p_n < 2⁶⁴` | **`𝒞`, cited** (imported wholesale) | `kourbatov2015verification` §4 Thm. + endnotes 5 Jan 2023 (L0), resting on `oliveira2014goldbach` (**L2_weak, never opened**) — flagged at point of use and in §9.5 priority 2 |
| M2 | `thm:io` — `p_n^{1/n} > p_{n+1}^{1/(n+1)}` infinitely often, unconditionally | **cited** (strength is its source's) | `ferreira2017consequences` Thm 5.2 (ledger **L0**, statement table row present verbatim) — the only unconditional positive statement about `F` in the literature |
| M3 | `thm:pairfalse` — `P_pair` is **false**, already on `[1,1847]`, with two exhibited witnesses; the second witness is the **28th** maximal gap (`rem:ordinal`) | **`𝒞`** exhaustive | recomputed here: 28 records below `2·10⁸`, 28th at `191 912 783` (`g=248`); `faults.md` §1 (independent); R2-m1 closed |
| M4 | `prop:census` — exactly **17 indices** below `10⁹` admit a `P_pair`-failure witness, in two clusters; **20 pairs** below `3·10⁸`; no reading as a density (`haz:census`) | **`𝒞`** + explicit prohibition | `faults.md` R2-m2 CLOSED; the index/pair distinction is carried in the paper's own caveat |
| M5 | `prop:incomparable` — `P_gov` and `P_min` are **formally incomparable**, four-index counter-model each way; `rem:withdrawn` retracts round-1's ordering; `rem:notweakest` retracts "the weakest" | **`𝒫`** | `faults.md` R2-M3 CLOSED at the three named upstream sites; the paper carries the retraction at its own point of use |
| M6 | `thm:ffm` — first-failure maximality from **either** survivor at a single index, so the pruning route is undamaged | **`𝒫`** | round-2 re-derivation; not contested by any round-3 finding |
| M7 | `lem:M`, `lem:Mprime` — monotone-bar principle and its truncated form | **`𝒫`** | uncontested across three rounds |
| M8 | `lem:S2`, `thm:B` — `T_n > S(p_n)` for `p_n ≥ 2 634 800 823`; maximal-gap reduction on `[10, N₂]` | **`𝒫`**, resting on `axler2014newbounds` (now **L0**) | `haz:axler`: the numeral `2 634 800 823` is the post-Corrigendum statement, quoted by statement rather than by corollary number because the corollary numbering differs by edition |
| M9 | `thm:range` + `cor:S` — unconditional finite-range verification from any first-occurrence table, on `dusart2010estimates` alone | **`𝒫`**; explicitly *not* "no computation" (§9.6) | `dusart2010estimates` Thm 6.9 eq.(6.6) (L0); `lem:floor`, `lem:Bmono` |
| M10 | `prop:1920` — `B(2⁶⁴) = 1919.13798349753288…`, so a violating gap at `2⁶⁴` needs `g ≥ 1920`; reproduces the published constant with no tuning | **`𝒞`** | **recomputed here at 40 dps: identical**, and `S♯(1918) ≤ 2⁶⁴ < S♯(1920)`; `haz:agreement` states what the agreement is and is not worth |
| M11 | `prop:window` + `prop:closure` — table-free window `396 738 ≤ p_n ≤ 777 600`, closing permanently above `p* = 777 600.744…` | **`𝒫`** | `dusart2010estimates` Prop. 6.8 (L0); **`p*` recomputed here: 777 600.7442975646…** |
| M12 | `thm:Ca` — near-record maximality, `p_m ≤ 0.94970 p_{n₀}` | **`𝒫·s`** (rests on an unopened source) | constants re-derived by `faults.md` §1 (`s3_constants.py`): cell majorant `0.0515990267`, tail `0.050027515`, exact requirement `0.05149345…` — all ✓. **`haz:uncond`**: the weakest link is the `2⁶⁴` height, not Dusart |
| M13 | `thm:Cb` — near-record maximality with Axler, `p_m ≤ 0.998244 p_{n₀}`; **designated** as the corpus's single repaired near-record theorem | **`𝒫·s`** | `reconciliation.md` decision 1, found **SOUND** by `faults.md` §5 item 1; constants re-derived: majorant `0.00175687590387`, margin `2.41·10⁻⁸`, tail `0.00028380634` — all ✓ |
| M14 | `rem:retired` — the competing repair (`0.99565` / `0.0043636` / row `(1,0,0,0)` at `1 772 201`) is **correct but retired**, on the edition ground | **`𝒫`, historical only** | `faults.md` §5 item 8: corpus hunted for surviving live uses of the retired figures — **none found**; every occurrence sits in a retirement remark, a history column, or an edition flag |
| M15 | `haz:margin` — `thm:Cb`'s certified constant clears its majorant by only **`2.4·10⁻⁸`**; grid-robust to `0.00175687597478`; closing it properly needs interval arithmetic | **hazard, recorded not repaired** | `faults.md` R2-m3 CLOSED as a recorded margin, margin re-derived independently (`2.41·10⁻⁸`) |
| M16 | `prop:obstruction` — closing the residual window needs a short-interval prime count within `1 + 2/L` of truth; Brun–Titchmarsh gives only ≈2 | **`𝒫`**, used **only negatively** (`haz:bt`) | `faults.md` §6 confirms the `0.176 %` sliver is genuinely open mathematics |
| M17 | `lem:A1`, `thm:Azero`, `thm:A` — `A = {n : B_n < T_n} = {1,2,3}` (same with `≤`); the sharpest published RH-conditional bound certifies `F` at **exactly one index** | **`𝒫`** | **`A = {1,2,3}` recomputed here, both strict and non-strict**; `carneiro2019fourier` §1.2 Thm.5 (L1) |
| M18 | `thm:Bpow` — no power-type envelope certifies `F` beyond finitely many indices | **`𝒫`** | uncontested |
| M19 | `thm:Ccrit` — the critical constant on the `√p log p` scale is exactly **`2/e = 0.7357588823428846…`** (Lambert-`W`) | **`𝒫`** | **recomputed here at 40 dps: identical** |
| M20 | `cor:limsup0` — even `g_n = o(√p_n log p_n)` certifies `F` at no index | **`𝒫`**, hypothesis provenance quarantined in `haz:limsup0` | `carneiro2019fourier` §1.2 after eq.(1.14) — the **L2_weak sub-row**, explicitly marked "reported, not proved… second-hand" at the point of use |
| M21 | `thm:D`, `cor:D1`, `cor:D2` — the size of the advance a proof of `RH ⇒ F` would entail; the band left for a candidate hypothesis; `haz:noorder` disclaims any difficulty ordering | **`𝒫`** | uncontested |
| M22 | `thm:E` — Cramér's `limsup` hypothesis does **not** entail `F` over integer sequences (explicit counter-model) | **`𝒫`**, with `rem:E-scope` bounding what it closes | uncontested; `haz:cramer` records that Cramér did not conjecture `limsup = 1` about the primes (`cramer1936order` p.24 eq.(4) vs p.27) |
| M23 | `prop:smooth` — `(x log x)^{1/x}` strictly decreasing on `x ≥ 5` (the smooth model) | **`𝒫`** | uncontested |
| M24 | `prop:ffm` (§8.5) — explicit sequence whose first Firoozbakht failure occurs at a **non-record** gap | **`𝒞`** | uncontested |

---

## 4. Computational-evidence claims

| # | Claim | Asserted strength | Supported by |
|---|---|---|---|
| C1 | Exhaustive sweep to `p < 10¹¹` — **4 118 054 812** consecutive prime pairs, **no violation, no near-miss**, `max_{n≥10} g_n/T_n = 0.8318` | **`𝒞`**, exhaustive; five further independent sweeps across rounds 2–3 reproduce it | in-run sweep + round-2/3 reproductions. **Not re-run at full range by this leg** (cost); re-run to `10⁹` here: 0 violations, `max = 0.78960`, consistent with the record being attained above `10⁹`. `π(10¹¹) = 4 118 054 813` ⇒ 4 118 054 812 pairs ✓ |
| C2 | `haz:5592` — the `55.92 %` descent figure, its denominator convention, and its **range dependence** across three decades (`55.918 %` at `3·10⁶` → `56.931 %` at `10⁸`) | **`𝒞`** with two explicit riders (range-dependence; **non-diagnostic** for `P6′`) | `faults.md` §1: sixth independent recount agrees with the reconciliation; the `n ≥ 11` cut shows the old figure mixed one cut's numerator with another's denominator. `reconcile_recount.py` re-executed byte-identically |
| C3 | §8.4 lemma/constant verification table, and `rem:stability` — the table test is stable across four decades | **`𝒞`** | `verify_syn*.py` outputs committed in `attack/` |
| C4 | §9.6 — the sweep verifies **the lemmas, not the range**; `10¹¹` is 8.27 decades short of `2⁶⁴`; "must never be cited as a verification of `F`" | self-limiting statement | arithmetic; `haz:agreement` |

---

## 5. Claims the paper makes about the **corpus and its gates**

| # | Claim (paper location) | Asserted strength | Supported by |
|---|---|---|---|
| G1 | The evidence gate stands at **BLOCKED**, failing leg = adversarial review, on the two round-3 findings (abstract l.96; §9.3 l.2472–2497; §9.3 box l.2513) | self-report of a gate | `attack/evidence-verdict.md`: `VERDICT: BLOCKED`, failing leg SKEPTIC round 3 — quoted accurately |
| G2 | The kernel leg **passes outright**, re-executed from a cold cache by two independent round-3 legs; the adversarial-corpus leg passes 27/27 (§9.3 box) | self-report | `evidence-verdict.md` §1 (KERNEL PASS), §3 (CORPUS PASS); `faults.md` §1 |
| G3 | Round 3's **BLOCKER 1** — a tier settled "at every site" reached one artifact out of seven; "this paper is unaffected in substance" (§9.3 item 1) | accurate restatement of S3-B1 | `faults.md` S3-B1 — six sites listed (5 concept cards + 1 round-2 proof attempt); `verification-report.md` §"Relationship to faults.md": none of the six is in `paper/` |
| G4 | Round 3's **BLOCKER 2** — four false statements about the corpus's own state, re-published as gate status; origin was this paper's own round-2 snapshot, true when written and false 11 minutes later (§9.3 item 2) | accurate restatement of S3-B2, **including the paper's own share of the blame** | `faults.md` S3-B2 (all four claims checked against `git log`) |
| G5 | Below the blocking level: `haz:uncond`'s two surviving upstream sites (S3-M1); the script credited with computations it does not contain (S3-M2); "the weakest" residue (S3-m1); the 17-exceptions residue (S3-m2); `decompose.md`'s retired denominator (S3-m3); the Axler "v4" instruction (S3-m4); the two cards disagreeing on the recount count (S3-m5) — **all seven named** (§9.3 l.2499–2509) | accurate restatement | `faults.md` §3–§4, item by item |
| G6 | §9.5 — the ledger has **22 rows: 13 L0 / 4 L1 / 3 L2_strong / 2 L2_weak / 0 L3**; no citation rests on recall | factual claim about the ledger | **recounted here from the row headers of `source-ledger.md`: exactly 13/4/3/2, 22 rows, zero L3** ✓ |
| G7 | §9.5 — "the audit that exists, stated correctly": an independent leg audited **round 2's edition** and returned **PASS** (22/22 citekeys, 91 `\cite` instances, 59 locator pairs, 0 L3); **what is outstanding is a re-audit against the round-3 state** | factual claim about the citation gate | **Contradicted by the tree as it now stands.** The round-3 re-audit *has* run (`cite-20260727-df58`, commit `327ba72`, **PASS**) and **superseded `attack/verification-report.md` in place** — the numbers the paper quotes (22/91/59) no longer appear at the path it points to, which now reads 21/94. Separately, that round-3 report audits **21** citekeys; the paper has **22** (see §6.2) |
| G8 | §9.5 — no citation clearance is claimed here; three reasons that survive the correction (predates round 3; a PASS that carries caveats is not a clearance of them; two load-bearing sources under-opened) | self-limiting statement | reasons 2 and 3 hold verbatim; reason 1 is the stale half of **G7** |
| G9 | §9.5 — load-bearing unopened sources, priority order: `granville1995cramer` at preprint pagination (**priority 1**); `oliveira2014goldbach` never opened, under **both** branches of the near-record theorem (**priority 2**); the two newly-folded rows (**priority 3**) | provenance disclosure | `faults.md` §6 confirms exactly these as "not closable by editing text"; `verification-report.md` §"Standing cautions" confirms both |
| G10 | `rem:structural` — three consecutive rounds have failed at the same step, each in the leg created to fix the previous round's failure at it; the round-2 one-leg estimate was **wrong** and the same estimate offered again should be discounted | self-critical structural reading | `faults.md` §6 ("the corpus's problem has moved from mathematics to bookkeeping"); the round-1/2/3 verdict trail |
| G11 | §9.3 — "Nothing in §§2–9 rests on an unrepaired defect… **This paper is an honest report on a blocked corpus. It is not a seal.**" | self-limiting statement | `faults.md` §5 item 8 (no stale live site found); rows M1–M24 above |

---

## 6. Citations — 22 citekeys, 94 `\cite` instances

Extracted independently for this review with
`grep -oE '\\cite[a-zA-Z]*(\[[^]]*\])?\{[^}]+\}' paper/paper.tex`, comma-expanded.

| # | citekey | instances (here) | ledger tier | locators used in the paper | supported by |
|---|---|---:|---|---|---|
| K01 | `kourbatov2015bounds` | 9 | L0 | §1, §1 eq.(1), §2 Thm.1, §4 Thm.3, §4 Thm.4, §5 Thm.5 | ledger statement table; `verification-report.md` row |
| K02 | `ferreira2017consequences` | **9** | **L0** | §1, Thm.2.2 ×2, Lem.3.2, Cons.3.3, Thm.4.5, Thm.5.1, Thm.5.2, bare | **ledger row `source-ledger.md:343`, statement table checked here locator-by-locator — all nine match.** *Not present in `verification-report.md`'s per-citekey table* (§6.2) |
| K03 | `dusart2010estimates` | 8 | L0 | Thm.6.9 eq.(6.6) ×3, Prop.6.8 ×2, Thm.6.9, bare ×2 | ledger; `verification-report.md` row |
| K04 | `carneiro2019fourier` | 7 | L1 (one L2_weak sub-row) | §1.2 Thm.5 ×2, §1.2 Cor.4, §1.2 after eq.(1.14), bare ×2 | ledger; the L2_weak sub-row quarantined in `haz:limsup0` at the point of use |
| K05 | `visser2019verifying` | 6 | L0 | Conj.2, Conj.3 eq.(2.4), Abstract §1, Abstract §1 eq.(1.4), bare ×2 | ledger; `verification-report.md` row |
| K06 | `baker2001difference` | 6 | L1 | bare (abstract-level only) | ledger; disclosed as abstract-level in §9.5 |
| K07 | `axler2014newbounds` | 6 | **L0** (promoted 2026-07-26) | bare; edition named in prose | `haz:axler`; ledger row `:426` tier L0 with three-document fetch table |
| K08 | `visser2018andrica` | 5 | L0 | Thm.1 eq.(1.4), §7, §2 Thm.4, §2 Thm.5, bare | ledger; the `≤`-vs-`<` strictness discrepancy recorded rather than smoothed |
| K09 | `oliveira2014goldbach` | 5 | **L2_weak** | bare | ledger; never cited for content read in it; disclosed at §9.5 priority 2 |
| K10 | `oeisA111943` | 5 | L0 (`oeis_A111943`) | bare | ledger; camelCase bib spelling of the ledger-prose name |
| K11 | `kourbatov2015verification` | 4 | L0 | §4 Thm., endnotes 5 Jan 2023, bare ×2 | ledger; paper quotes the `2⁶⁴` frontier, not the superseded title figure |
| K12 | `granville1995cramer` | 4 | **L1** | preprint p.12 after eq.(20), preprint pp.10&12, preprint p.12, bare | ledger; every bracket says "preprint"; §9.5 priority 1 |
| K13 | `sun2013sequence` | 3 | L0 | §1 ×2, Thm.2.1 | ledger |
| K14 | `ribenboim2004little` | 3 | **L2_strong** | p.185 ×2, bare | ledger; §9.5 discloses "not opened, rests on two independent citers" |
| K15 | `ford2016large` | 3 | L1 | bare | ledger; corrected `(log log log X)²` exponent applied |
| K16 | `cramer1936order` | 3 | L0 | p.24 eq.(4), p.27, pp.24&26–27 | ledger; `haz:cramer` carries the proved-vs-suggested distinction |
| K17 | `shanks1964maximal` | 2 | **L2_weak** | bare | ledger; attribution only, disclosed twice |
| K18 | `farhadian2017new` | 2 | **L2_strong** | bare | ledger; attribution only, disclosed |
| K19 | `oeisA182514` | 1 | L0 (`oeis_A182514`) | bare | ledger |
| K20 | `mathlibNatNth` | 1 | L0 (`mathlib_nat_nth`) | bare | ledger |
| K21 | `mathlibNatPrimeNth` | 1 | L0 (`mathlib_nat_prime_nth`) | bare | ledger |
| K22 | `firoozbakht1982unpublished` | 1 | **L2_strong** | bare | ledger; attribution only ("never published by her") |

**Total: 22 citekeys, 94 instances, 22 ledger rows, one-to-one. Zero orphans in either direction
(checked both ways against `references.bib` and `source-ledger.md`). Zero L3.**

### 6.1 Note on tier arithmetic
The paper's §9.5 tier census (13 L0 / 4 L1 / 3 L2_strong / 2 L2_weak) reproduces exactly when the
ledger's 22 row headers are counted, and the 22 ledger rows are in bijection with the 22 citekeys.
This is an independent confirmation that the *paper's* count is right.

### 6.2 Where the citation gate and this ledger disagree
`attack/verification-report.md` (round 3) reports **21** unique citekeys and prints a
per-citekey table of **21** rows. `ferreira2017consequences` is absent from it. Its own headline
instance count (**94**) does not equal the sum of its table's per-citekey instance counts
(**85**) — the 9-instance difference is exactly `ferreira2017consequences`. Its stated
explanation for differing from round 2's "22" (the four camelCase/underscore renames) does not
account for the discrepancy, since those four appear in both counts. This is scored in §7 as
**G7-b**.

---

## 7. Round-3 tags (step 2 of this molecule)

Tag key: **CONFIRMED** · **OVERCLAIM** · **UNSUPPORTED-CITATION** · **UNADDRESSED-FAULT**.
Every row not listed below is **CONFIRMED**; the exceptions are itemised in full.

| Row | Tag | Evidence |
|---|---|---|
| S1–S4 | **CONFIRMED** | The paper's status claims are exactly the evidence gate's and the skeptic's, quoted rather than paraphrased. S3's narrowed vocabulary rule is kept: all 10 "machine-checked" sites are `𝒦` statements. |
| K1–K4 | **CONFIRMED** | KERNEL leg PASS, re-executed from a cold cache by the round-3 skeptic (`lake build` 0, audit 0, 63 declarations, one `sorryAx`). Nothing beyond the barrier is claimed at `𝒦`. |
| M1–M24 | **CONFIRMED** | Nine constants re-derived independently in this leg (§0.1), all identical; the remainder re-derived by the round-3 skeptic from statements with its own scripts. `faults.md` §5 attacked the designated theorem and could not break it. **No `𝒫`/`𝒞` statement is dressed as `𝒦`, and `𝒫·s` is applied to exactly the two theorems whose weakest link is the unopened `2⁶⁴` height.** |
| C1–C4 | **CONFIRMED** | C1 not re-run at `10¹¹` here (cost); re-run to `10⁹` reproduces 0 violations and a max consistent with the record being attained above `10⁹`. C2's riders are both present and both correct. |
| G1–G6, G8–G11 | **CONFIRMED** | Each is a verbatim-accurate restatement of `evidence-verdict.md` / `faults.md`. G6's tier census recounted here and exact. |
| **G7-a** | **OVERCLAIM** — a false statement about the corpus's own state, of the S3-B2 species | §9.5 says "what is outstanding is a **re-audit against the round-3 state**". That re-audit ran and returned **PASS** (`cite-20260727-df58`, `327ba72`), 11 minutes-equivalent after the paper's own commit (`c536696`). Worse, it **superseded `attack/verification-report.md` in place**, so the paper's quoted figures (22 citekeys / 91 instances / 59 pairs) no longer exist at the path §9.5 sends the reader to, which now reads 21 / 94. Direction of error: it **understates** the paper's provenance — as it did in round 2. **This is the third consecutive round in which this paper's provenance section went stale within minutes of being committed.** |
| **G7-b** | **UNSUPPORTED-CITATION** (of the gate, not of the paper) | `attack/verification-report.md` asserts "21 unique citekeys", "**21/21 citekeys: OK**", and "grep … → 21 unique keys… **no citekey in `paper.tex` lacks a ledger row**". The paper has **22**. `ferreira2017consequences` — 9 instances, tied for most-cited, carrying five distinct locators including `Thm.~5.2`, the sole support for **M2**, the only unconditional positive statement about `F` in the paper — **was never audited**. The report's own table sums to 85 of the 94 instances it claims to have checked. **The nine locators do in fact resolve** (checked here, one by one, against `source-ledger.md:343`), so the *paper* carries no unsupported citation; what is unsupported is the *gate's* claim of complete coverage. |
| **G-fault-1** | **UNADDRESSED-FAULT — none.** | Both round-3 BLOCKERs (S3-B1, S3-B2) and both MAJORs (S3-M1, S3-M2) are named in §9.3 at the blocking level, and all five MINORs are named below it. Neither BLOCKER names `paper/paper.tex` as a site needing correction; the paper is the artifact that reports them, not one of the artifacts that carries them. |
| **V-abstract** | **OVERCLAIM** (narrow) | Abstract l.85: "first-failure maximality now holds against all primes below `0.94970 p_{n₀}` **on Dusart alone**". `haz:uncond` is the paper's own finding that this exact phrasing — *"unconditionally, on Dusart alone"* — is the defect it faults upstream at FFM l.751, because the weakest link is the `2⁶⁴` height and not Dusart. `thm:Ca` carries `𝒫·s` precisely for that reason. The abstract asserts the source basis without the height, in the one place where the confidence codes are not visible. Round 2's V3 was the same failure mode in the same place; the vocabulary rule was narrowed, but this sentence still asserts above its code. Narrow, non-fatal, one clause to fix. |

**Tally: 2 OVERCLAIM (G7-a, V-abstract), 1 UNSUPPORTED-CITATION (G7-b, against the gate),
0 UNADDRESSED-FAULT, all other rows CONFIRMED.**

---

## 8. What changed since round 2

| round-2 finding (`editorial-verdict.md`, `42f023a`) | round-3 status |
|---|---|
| **V1** — evidence gate BLOCKED (3 BLOCKERs: R2-B1/B2/B3) | **Still BLOCKED, different reasons.** All three round-2 BLOCKERs are **closed** (verified by the round-3 skeptic against the tree, not against reports); two new ones opened (S3-B1, S3-B2), both cross-artifact bookkeeping, neither mathematical, neither touching `F` |
| **V2** — the paper asserted four times that no citation audit existed | **FIXED.** §9.5 is rewritten, states the audit exists and returned PASS, and names the false assertion as the first item of its own revision. **But it has gone stale again in the same section — G7-a** |
| **V3** — the "*proved* is reserved for `𝒦` without exception" promise had ≥5 breaches, first in the abstract | **FIXED, honestly.** The promise is explicitly **withdrawn** (§1.4 l.347–350) and replaced by a narrower rule the paper actually keeps; all 10 "machine-checked" sites verified `𝒦` here. **Residue: one abstract clause still asserts above its code — V-abstract** |
| citation gate | round 2: PASS (22/22). round 3: PASS, **but 21/22 audited** — a *new* defect, found here (G7-b) |
| ledger | unchanged at 22 rows / 13-4-3-2 / zero L3; recounted here |
| paper | 2460 → 2733 lines; every round-3 decision applied at its point of use; §9.3 and §9.5 rewritten |
| this ledger | 100 rows (round 2) → 62 rows (round 3), reorganised by claim species rather than by section; nine constants re-derived here rather than four |

---

*Artifact of leg `review`, round 3, molecule `review-20260727-2c6d`, run `germ-20260725-791a7c45`.
Supersedes the round-2 `attack/claims-ledger.md` (molecule `review-20260726-7d55`, commit
`607c416`) in place. Independent recomputation: own segmented sieve to `10⁹` and `mpmath` at
40 dps; own citekey extraction over `paper/paper.tex`. No line of `paper.tex` was edited by this
leg. **`F` remains OPEN.***
