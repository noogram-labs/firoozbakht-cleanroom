# Firoozbakht's conjecture — synthesis of the attack

**Molecule:** `task-20260727-4709` (leg `synthesize`, crew role: synthesizer) — **ROUND 3, v2:
written against the post-reconciliation skeptic re-audit**
**Run:** `germ-20260725-791a7c45` · **Re-attack loop:** `reattack-20260726-57d1` (rounds 1–2) ·
**Reconciliation leg:** `task-20260727-264e` (`attack/reconciliation.md`) ·
**Skeptic re-audit leg:** `task-20260727-5096` (`attack/faults.md`) ·
**Evidence gate:** `task-20260727-2fee` (`attack/evidence-verdict.md`, v2)
**Date:** 2026-07-27 · **Formal backend:** Lean 4 / Mathlib
**Conjecture under attack (`F`):**

> `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1` — equivalently, `n ↦ (p_n)^{1/n}` is strictly
> decreasing.

**This document supersedes, in place, both the round-2 `synthesis.md` and the earlier round-3
`synthesis.md` (molecule `task-20260727-1d5d`, committed `4753437`).** The galaxy carries exactly
one current answer, and this is it. Three things separate this document from the one it replaces:

1. **A fresh skeptic re-audit ran after that document was written** (`attack/faults.md`, molecule
   `task-20260727-5096`, committed `5e69ce9`/`ce783d7`) and it **supersedes both prior fault lists**.
   It closes **12 of round 2's 13 findings by independent re-derivation** and opens **2 new
   BLOCKERs** — one of which is *the superseded synthesis itself*, for republishing four false
   statements about the state of the tree (S3-B2). §5.7.
2. **Those four statements are corrected here**, each against `git log` and the tracked files, by
   this leg's own check and not by reading the skeptic's report. The largest of them: this corpus
   **does** carry a round-2 citation audit and it returned **PASS** — the previous synthesis said no
   audit existed. What that does and does not license is stated precisely in §6.
3. **This leg re-executed the Lean gates and re-derived every headline number itself**
   (`attack/verify_syn4.py`, **47/47, exit 0**, own sieve, 60 dps, no upstream code path opened).
   §8.

**Which round the verdict rests on.** `attack/re-attack/reattack-verdict.json` names
`final_round.round = 2` (`rounds_run = 2`, `rounds_target = 2`, `exit_reason: "rounds-exhausted"`).
The reconciliation and the skeptic re-audit were funded **outside** that loop's cap and add no
`round: 3` entry to the JSON, because neither is a re-attack round — neither opened mathematics nor
nucleated attempts. So: **the verdict rests on round 2's artifacts, read as amended by the round-3
reconciliation and as re-certified (and partly faulted) by the round-3 skeptic.** Round 1's
artifacts are pinned inputs, cited only where later rounds left them standing, and every such case is
marked.

---

## 0. The verdict, in one screen

| Question the brief posed | Answer |
|---|---|
| Was `F` **PROVEN**? | **No.** |
| Was `F` **REFUTED**? | **No.** |
| Status of `F` after four legs of work | **OPEN**, and every round-2 and round-3 artifact says so of itself, at the top, unprompted. |
| Rounds run | **2 re-attack rounds** (`rounds_target = 2`, `exit_reason: rounds-exhausted`) **+ 2 legs funded outside the cap**: one reconciliation, one skeptic re-audit. |
| Did the still-unproved list shrink? | **No — unchanged at one entry, every leg, and that entry is `F` itself.** §1. This is the honest, expected shape, not a failure. |
| Did the BLOCKER set shrink? | **Its *content* did, measurably and for the first time — 12 of 13 round-2 findings closed by independent re-derivation. Its *count* did not reach zero: 2 → 3 → 2, and the species recurred a third time.** §1, §5.7. |
| Evidence-gate status | **BLOCKED** — failing leg `SKEPTIC`. `attack/evidence-verdict.md` (v2, `task-20260727-2fee`), read against the fresh audit. §6. |
| Citation clearance | **NOT CLAIMED here.** A round-2 citation audit **does** exist (`attack/verification-report.md`, `51756c5`, verdict **PASS** on the round-2 paper) — the previous synthesis wrongly said none did. But the citation gate runs downstream, on the final paper, *after* the round-3 decisions it has not yet seen, and two load-bearing sources remain under-opened. **This document claims no citation clearance.** §6. |

**The one-sentence result of the whole run.** *Firoozbakht's conjecture was neither proved nor
refuted; what four legs of work produced instead is (i) a machine-checked reduction of `F` to the
prime-gap inequality `g_n < T_n`, joined by a machine-checked proof that the only prime-gap input
Mathlib carries (Bertrand) is **provably insufficient at every `n ≥ 2`**, (ii) a table-driven
verification architecture reproducing the published `2⁶⁴` frontier from first principles on
unconditional analytics alone, whose first-failure-maximality theorems then tighten to
`0.94970·p_{n₀}` on Dusart and `0.998244·p_{n₀}` with Axler — *given* the published `2⁶⁴`
verification height, card `L6`, which is unopened (§4.5), (iii) an exhaustive independent sweep to
`10¹¹` with no counterexample and no near-miss, (iv) a five-theorem closure of the
Riemann-Hypothesis route *as a route*, and (v) the outright **refutation of the run's own most-quoted
lemma** (`P6′-pair`), with a proof that two of the surviving predicates are formally incomparable —
all of it now carried in a corpus whose mathematics has been re-derived independently four times over
and whose remaining defects are entirely bookkeeping, none of which clears the gate.*

**What must not be written downstream.** Not "Firoozbakht is true": no proof exists and the
obstruction analysis (§4.1) shows none is near — round 2 strengthened that reading by *closing* a
route rather than opening one. Not "Firoozbakht is false": the Cramér–Granville tension is a
heuristic, not a test. The defensible sentence, inherited from `decompose` §9, unweakened by anything
found in four legs, and repeated verbatim by both round-3 legs as a standing instruction, is:
*Firoozbakht's conjecture is numerically robust over the verified range and simultaneously
incompatible with the standard Cramér–Granville heuristic; at least one of the two must fail, and no
current technique can say which.*

---

## 1. The trajectory — four legs, what each fixed, and shrink versus churn

| leg | shape | kernel | skeptic | BLOCKERs | unproved | converged? |
|---|---|---|---|---|---|---|
| **round 1** (upstream, pinned) | fan-out | UNPROVABLE_IN_BUDGET | blockers | **2** (F1, F2) | 1 (`F` itself) | **NO** |
| **round 2** (nucleated by the loop) | wider fan-out — 3 attempts, 1 probe, 1 skeptic | UNPROVABLE_IN_BUDGET | blockers | **3** (R2-B1/B2/B3) | 1 (`F` itself) | **NO** |
| **round 3a — reconcile** (outside the cap) | one leg, five decisions, no fan-out | not re-run by that leg | not re-run by that leg | 3 repaired, 0 self-certified | 1 (`F` itself) | **NO** |
| **round 3b — skeptic re-audit** (outside the cap) | one leg, re-derives rather than reads | **re-executed: PASS** | **fresh audit** | **2** (S3-B1, S3-B2) — after closing 12 of round 2's 13 | 1 (`F` itself) | **NO** |

The loop's stop condition — *kernel PROVED **and** skeptic clean, in the same round* — never held.
`while round < rounds` went false at `2 < 2`, so the loop exited `rounds-exhausted`, never a silent
pass. Rounds 3a and 3b were funded separately, on the loop's own recommendation, and are deliberately
**not** further data points on the fan-out curve.

### Did the still-unproved list shrink, or churn?

**Neither. It was unchanged: one entry, every leg, and that entry is `F` itself.**
`unproved-1 = unproved-2 = { Firoozbakht.firoozbakht : Conjecture }` (`Statement.lean:186`), and
neither round-3 leg wrote Lean. Nothing regressed; nothing new became `sorry`'d. Saying this plainly
is the point: **an attack on an open `Π₁` statement whose `sorry` count reaches zero would be
reporting a fabrication, not a result.** This leg re-ran the audit itself and reproduces exactly one
`sorryAx` dependent out of 63 declarations (§8) — so the one-entry list is this document's own
measurement, not an inherited claim. The round-3 skeptic independently reproduced the same numbers
and the same `Statement.lean` SHA-256 on its own toolchain run.

**But the *quality* of the non-shrinkage changed once, in round 2, and that change is real.** Round 1
correctly *declined* to attempt the conjecture. Round 2 attempted it and failed honestly — `exact?`,
`aesop`, `decide` all fail as expected — and then did something round 1 did not: it **proved a
barrier**. `lean/Firoozbakht/Barrier.lean` carries three `sorry`-free theorems showing Bertrand's
ceiling sits strictly *above* the Firoozbakht threshold at **every** `n ≥ 2`. The route is not
"hard"; it is **closed**, kernel-checked. That is genuine progress on the formal leg with an
identical `sorry` count — and it is the only such progress in four legs.

### Did the BLOCKER set shrink, or churn?

**For the first time the answer is not "churn" — but it is not "converged" either. Read it in two
registers, because they now disagree, and that disagreement is the most useful thing this run has
produced.**

- **By content: real, measured shrinkage.** Round 3b is the first leg to re-audit the tree by
  *recomputation*, and it **closed 12 of round 2's 13 findings** — all three BLOCKERs, all three
  MAJORs, seven MINORs — six of them by recomputing the number from the statement, two by reversing
  the leg's own report of itself against `git log`. Round 1's two BLOCKERs were already closed the
  same way by round 2. **Nothing in the mathematics is now in dispute anywhere in the corpus.**
- **By count: 2 → 3 → 2, and never zero.** The two survivors (S3-B1, S3-B2) are narrower than
  anything before them: neither is a mathematical error, neither touches `F`, and both are closable
  by editing text — no sieve, no fetch, no derivation.
- **By species: the same failure, a third time, and this is the finding.** Round 1's skeptic named it
  — *"a fan-out with no reconciliation stage … nobody owned the seams."* Round 2 widened the fan-out
  and reproduced it. Round 3a supplied the missing reconciliation stage, closed the seams — **and
  then committed the identical error inside the document whose own closing lesson is "a leg's claim
  about the state of a file is not evidence about the state of that file; `git show` is"** (S3-B2).
  Round 3b caught that only because it ran `git log` on files nobody had asked it about.

**The prediction the previous synthesis made, and the test it failed — reported because it is the
cleanest evidence in this document.** That document wrote: *"the distance from here to a clean gate
is one leg, and it is not a research leg."* **That leg was funded and it ran. The gate did not
clear.** It did not clear because the fixer inherited a false statement about the tree and
republished it as a gate status. This is the third consecutive round in which the leg created to fix
the previous round's bookkeeping failure committed a fresh instance of it. **The honest reading is
that the corpus's residual defect is not a quantity of remaining work but a missing discipline** —
no leg in four rounds has been *required* to check the tree before describing it, and every leg that
did check found something.

**So the honest answer to "will more rounds help?"** More rounds of the *fan-out* shape will not; the
mathematics stopped moving after round 2 and every subsequent finding has been bookkeeping. One more
targeted editing pass, with a tree-check requirement in its brief, plausibly clears the gate — but
that is now the *second* time this document's predecessor has offered a one-leg estimate, and the
first one was wrong. **Take the estimate at the confidence of a leg that has been wrong once at
exactly this task.**

---

## 2. What was PROVED

Confidence codes: **[K]** = machine-checked by the Lean kernel — and, in this document, re-executed
by this leg (§8); **[P]** = paper proof, derived in-run and independently re-derived by at least one
skeptic leg; **[P·L6]** = paper proof, skeptic-confirmed, resting on the unopened `2⁶⁴` verification
height (card `L6`, tier **L2_weak**) — the corpus's largest remaining provenance exposure, §4.5;
**[C]** = finite computation, exhaustive and independently reproduced. Round-2 results are marked
**‹r2›**; round-3 changes **‹r3›**.

### 2.1 The reduction chain, and the barrier — `[K]`

`Conjecture ↔ ConjectureReal ↔ (∀ n ≥ 1, g_n < T_n)`, where `T_n := p_n(p_n^{1/n} − 1)`, is
**machine-checked**. This leg re-ran every gate rather than quoting any report: `lake build` exit 0
(2208 jobs), `lake env lean audit.lean` and `audit_exhaustive.lean` both exit 0, **63 declarations**
scanned, exactly **one** `sorryAx` dependent — the open target. Grep-clean of `axiom`,
`native_decide`, `unsafe`, `@[implemented_by]` outside docstrings; exactly one live `sorry` token, at
`Statement.lean:186`. Full transcript in §8.

**`lean/Firoozbakht/Barrier.lean` ‹r2› — three `sorry`-free theorems:**

| Theorem | Statement |
|---|---|
| `bertrand_gap` | `p (n+1) ≤ 2 * p n` for `n ≥ 1` — Bertrand, ported to this development's 1-indexed `p` |
| `p_lt_two_pow` | `p n < 2 ^ n` for `n ≥ 2` — induction on `bertrand_gap`, base `p 2 = 3 < 4` |
| `bertrand_ceiling_above_threshold` | `(p n : ℝ) ^ (1 + 1/n) < 2 * (p n : ℝ)` for `n ≥ 2` |

Read the third in the right direction: for Bertrand to *certify* `F`, its ceiling `2 p_n` would have
to sit **below** the threshold `p_n^{1+1/n}`. It sits strictly **above** it, at every `n ≥ 2`. The
mechanism in one line: Bertrand supplies constant multiplicative slack `2`, while the threshold's
slack `p_n^{1/n} = exp(log p_n / n)` tends to `1`; certification would need `2^n ≤ p_n`, and
`p_n < 2^n` — which is `p_lt_two_pow`, itself proven *from* Bertrand. **The best available tool
proves its own insufficiency.** This is a negative-capability result: it says nothing about whether
`F` is true, and everything about what the substrate can reach. This leg re-checked both directions
numerically over `2 ≤ n ≤ 20 000` and `p_n < 2^n` in exact integers to `π(3·10⁶)` — 0 failures each,
and Bertrand ties exactly at `n = 1` (`2² = 4 = 2·2`), so it certifies nowhere in the range the
theorem covers. *(This is the one check whose polarity the previous leg's script got backwards on its
first run; it is written here in the certification direction deliberately.)*

The checker itself was tested rather than trusted (round 1, unchanged and uncontradicted): 27
adversarial statements, all false or ill-formed, through the same toolchain; 27/27 behaved as
specified, and the one entry **no gate in this run catches** (`V04`, true-but-differently-meant via
ℕ→ℝ coercion) is named rather than omitted. Round 2 additionally re-tested the audit *detector*
against a planted `sorry` in the enlarged tree, then deleted the plant — so the one-entry unproved
list is produced by a detector demonstrated to fire.

### 2.2 The first-failure-maximality obligation, restructured — `[P]` ‹r2›

`decompose` §2.4 posed **P6′** and ranked it the attack's most tractable open obligation. Round 1
showed the obligation was misdirected. **Round 2 shows the run had been carrying three different
obligations under one name, refutes the strongest, and proves the remaining two are incomparable.**

The four predicates, named once and for all (`µ(n) := min{m : g_m ≥ g_n}`, `r(n) := ` last record
index `≤ n`):

| Name | Statement | Status |
|---|---|---|
| **P6′-pair** | `T_m ≤ T_n` whenever a record index `j` satisfies `m ≤ j < n` | **FALSE** — §3.1 |
| **P6′-gov** | `T_{r(n)} ≤ T_n` for all `n` | open; 0 exceptions swept |
| **P6′-min** | `T_{µ(n)} ≤ T_n` for all `n` | open; 0 exceptions swept |
| **P6′-rec** ‹r2› | `T_j ≤ T_{j′}` for consecutive record indices `j < j′` | open; 0 exceptions in **29 record steps** — not a robust base, §4.5 |

- **Theorem 2 (FFM)** `[P]` — *if `F` fails first at `n₀`, then **either** `T_{r(n₀)} ≤ T_{n₀}`
  **or** `T_{µ(n₀)} ≤ T_{n₀}` already forces `g_j < g_{n₀}` for every `j < n₀`.* Both branches are
  three-line chains, both re-derived by the round-2 skeptic. **Two consequences that matter more than
  the theorem:** the pruning never needed the predicate that turned out to be false, and **a single
  instance suffices** — the predicate is consumed only at `n₀`, never as a universal statement.
- **Proposition 4 (FFM)** `[P]` — `P6′-gov ⇏ P6′-min` **and** `P6′-min ⇏ P6′-gov`, both by explicit
  four-index counter-models (`g = (2,4,6,3)`). Round 1's fault report had carried the chain
  "(C) ⟹ (A) ⟹ (B), strictly" as though free; **the second link is invalid**, and the missing
  ingredient is P6′-rec, a fourth statement nobody had been measuring under its own name.
- **Lemma M / Theorem B (round 1)** `[P]` — the monotone-bar principle and its instantiation at
  Kourbatov's surrogate bar `S(x) = log²x − log x − 1.17` — survive round 2 unchanged and re-verified
  (`max{g_j : j ≤ 9} = 6 < S(29) = 6.80139`; `S`-breaches below `2·10⁸` are exactly `{1,2,3,4,6,9}`).

**The honest status ‹r3›.** P6′-min is the obligation to work (Theorem 2 needs it and its margin does
not decay), **and P6′-gov must be listed beside it, not below it** — round 2's prose had called
P6′-min *"the weakest of the three"* on the strength of an ordering its own Proposition 4 disproves.
Round 3a struck that prose at the three sites the fault named and **restored `P6′-gov` to card
`L15`'s obligation list**, with `P6′-rec` beside them because `gov ∧ rec ⟹ min` is the one valid
chain. Card `L15` in the tracked tree reads exactly that — checked, not inferred. ⚠ **Residue:** two
further sites in the same document still say *"the weakest"* (S3-m1, §5.7); they were not in the
fault's list and were not swept.

### 2.3 The finite-range theorem — one theorem, one constant ‹r3› — `[P·L6]` + `[C]`

> ⚠ **Read the code `[P·L6]` before quoting anything in this section.** Every Theorem C constant
> below is *unconditional in its analytics* and *conditional on card `L6`* — the published `2⁶⁴`
> verification height, tier **L2_weak, NOT OPENED** — for its finite branch. The honest form is
> **"unconditional given the published `2⁶⁴` verification height and a finite in-run gap
> computation"**, both named inputs, neither an analytic hypothesis. ⚠ **And note that the round-2
> source document still violates this discipline at two of its own sites** (S3-M1, §5.7): its verdict
> table and the paragraph it wrote to be quoted still say *"unconditionally, on Dusart alone"*. The
> honest form above is the one to carry.

`proof-attempt-2` (round 1) reconstructed from first principles the architecture by which the
literature's `2⁶⁴` frontier is certified; round 2 repaired its central bound; **round 3a chose which
repair the corpus carries, and the round-3 skeptic re-derived the chosen theorem's constants from its
statement and confirmed the choice.**

- **Lemma A / Corollary A2 / the table-free window** — unchanged and re-verified: `T_n ≥ L(L−1.1)`
  for `p_n ≥ 60 184` (Dusart 2010 Thm 6.9 eq. (6.6), **L0**, fetched and read); a gap of size `g` can
  violate `F` only at `p_n ≤ S(g) := exp((1.1 + √(1.21+4g))/2)`, converting the whole verification
  into a first-occurrence gap-table lookup; and the window `396 738 ≤ p_n ≤ 777 600` where `F`
  follows from unconditional analytic estimates with **no enumeration of primes at all**, which
  **closes permanently** at `p ≈ 7.776·10⁵`.
- **Independent reproduction of the published `1920`** `[C]` — `L(L−1.1)` at `2⁶⁴` is
  `1919.137983497532885…` (this leg's own value, 60 dps), so a gap of at least 1920 is needed to
  violate `F` just below `2⁶⁴`. The published integer falls out with no tuning. The caveat that makes
  this honest stands: Lemma A gives the *local* statement at the frontier, and the published
  endnote's phrasing is *global*.
- **F2 repaired ‹r2›** — the round-1 bound `(A-high)` `T_n ≤ (ℓ²−ℓ−1−1/ℓ)(1 + ℓ⁴/x)` did not follow
  from its stated justification and was false by a factor `≈ 38.8` over part of its range. Both
  round-2 legs restated it in the tight form `T_n < v(1 + v/x)`, proved from the elementary primitive
  rather than by weakening, and **replaced the numerical sweep by a proof**. The round-1 conclusion
  survives — the printed `0.004479` *is* sufficient — but for a reason the printed derivation did not
  supply.
- **Theorem C, as the corpus now carries it ‹r3›.** *If `F` first fails at `n₀`, then `g_{n₀}`
  exceeds every gap between primes below a definite multiple of `p_{n₀}`:*

| branch | round 1 | **live form** | source |
|---|---|---|---|
| Dusart only (**Theorem C-a′**) | `d ≥ 0.0623` → `p_m ≤ 0.93961·p_{n₀}` | **`d ≥ 0.0516` → `p_m ≤ 0.94970·p_{n₀}`** | `dusart2010estimates`, **L0** — *analytics only*; the finite branch consumes card `L6` and an in-run gap sieve ‹r3› |
| with Axler (**Theorem C-b′**) | `d ≥ 0.004479` → `p_m ≤ 0.99553·p_{n₀}`, from a lemma that did not support it | **`d ≥ 0.0017569` → `p_m ≤ 0.998244·p_{n₀}`** | `axler2014newbounds`, **L0** ‹r3› (in the ledger and at `T1`; ⚠ six-to-seven cards still say otherwise — S3-B1, §5.7), row `(2.1,0,0,0)/6 690 557`, present in **both** editions |

  The Dusart branch improves only because the small-branch cutoff rises from `60 184` to `10⁸`
  (licensed by `g_m ≤ 220 < 1919`); it **cannot** improve much further — `d*(ℓ) → 0.05`, so the
  Dusart-only sliver is pinned near `5 %` at every scale. The residual sliver on the Axler branch has
  relative width `0.176 %` at `2⁶⁴`.

  **Round 2 shipped the F2 repair twice, into two incompatible theorems; round 3a designated one, and
  round 3b independently re-derived it and endorsed the designation.** **Theorem C-b′ (`0.998244`) is
  the corpus's single repaired Theorem C(b).** Theorem C(b\*) (`0.99565`, off the preprint-only Axler
  row `(1,0,0,0)/1 772 201`) is **retired to a remark**, and `0.99553` and `0.99565` are retired with
  it. The deciding ground is documentary, not aesthetic — §5.1 — and it is lucky in one respect worth
  recording: the edition-safe theorem is also the sharper one, so nothing was paid for the
  provenance.

  **The certification margin, stated because it is thin.** C-b′'s certified constant `0.0017569`
  exceeds the cell majorant of its own defining supremum by **`2.40·10⁻⁸`** — re-derived here at 60
  dps on a fine scan of cell left-endpoints, so the figure is grid-robust, not an artefact of one
  chosen grid (§8.2). That is far less headroom than a Lean `norm_num` without directed rounding can
  be assumed to have. R2-m3 recorded it and correctly declined to "repair" it: closing it needs
  interval arithmetic, which is a funded leg, not an edit.

  **What the designation does *not* buy.** Both branches remain conditional on card `L6`
  (`p_{n₀} > 2⁶⁴`, tier **L2_weak, NOT OPENED**) for their small branches. **No sentence containing
  "Theorem C" may also contain "unconditional" without naming `L6` in the same breath** — §4.5.

### 2.4 The RH route is closed — as a route — `[P]` ‹r2›

Five theorems, all re-derived by both rounds' skeptics:

| Claim | Verdict |
|---|---|
| The sharpest published RH-conditional gap bound `g_n ≤ (22/25)√p_n·log p_n` (CMS, hypothesis `p_n > 3`) certifies `F` cofinitely | **REFUTED** — it certifies `F` **at exactly one index in the range where the bound is available (`n ≥ 3`), namely `n = 3`** (Thm A) |
| *Some* bound `g_n ≤ C·p_n^θ(log p_n)^A` with `θ > 0` implies `F` beyond finitely many `n` | **REFUTED** (Thm B) |
| *Some* envelope `C√p log p`, any `C > 0`, implies `F` beyond finitely many `n` | **REFUTED** (Thm C) — the **critical constant is `2/e = 0.7357588823428846…`** (re-derived here at 60 dps, attained at `x = e²`), published constants sit above it, and constants below it clear the `L²` bar only on a bounded initial segment `[x⁻(C), x⁺(C)]` given in closed form by the two real Lambert-`W` branches |
| Cramér's `limsup ≤ 1` entails `F` over integer sequences | **REFUTED** by explicit counter-model (Thm E) |
| `RH ⟹ F` as a material implication | **UNDECIDED**, and the leg does not pretend otherwise (Thm D) |

**The round-2 quantifier repair, recorded because it is a correction and not a restatement.** Round
1's headline read *"and at no other index whatsoever"*, and that is **false as stated**: the CMS
envelope also sits below the threshold at `n = 1` and `n = 2`. What excludes those two indices is
**the source's hypothesis `p_n > 3`, not the arithmetic**. Round 2 proves the two statements
separately — the *arithmetic clearance* set is `A = {1,2,3}` (Theorem A°), the *certified* set is
`S = A ∩ [3,∞) = {3}` (Theorem A) — dissolving a silent cross-artifact contradiction with
`notebook-1`'s `p*(22/25) = 5`. Both artifacts were numerically right; the words were not. They now
cite each other through a single object, the per-index critical constant `C_n := T_n/(√p_n·L_n)`.
**This is the one seam either fan-out round closed by itself.**

**Theorem D** bounds below the *strength* of any proof of `RH ⟹ F`: composed with Kourbatov's
unconditional necessary condition, such a proof would immediately yield an RH-conditional
Cramér-scale gap bound — stronger than the best published RH-conditional bound by a factor
`8.72·10⁷` at `2⁶⁴` and **unbounded** thereafter. This is a distance between two *statements*, not a
difficulty ordering between two open *problems*, and the leg says so explicitly (card `L11`).

**One corrected reading ‹r3›.** The lean-probe's §4 slack table is annotated: its BHP column is the
`C = 1` case of a bound with an *unspecified* constant, and its CMS column drops the `22/25` its own
row names — so both crossovers are **illustrations at a chosen constant, not measurements** (R2-m4).
The conclusion is unaffected, and the reason is worth carrying: it rests on the **exponent**, and
Theorems B and C refute every `C > 0`.

⚠ **A live provenance flag inside this branch.** The RH artifact gates its numeral `0.17`
(Corollary D.2) on Axler being *"unopened … must not be quoted downstream until Axler is at L0"*.
Axler **is** at L0 (ledger, since 2026-07-26) — so the numeral is citable — but the artifact was
never told. That is one of the six-to-seven stale sites of S3-B1 (§5.7), and it is the only one that
gates a live number rather than a tier label.

### 2.5 The smooth model — `[P]`

`decompose` §3.6: the smooth surrogate `(x log x)^{1/x}` is strictly decreasing on `x ≥ 5`. **The
smooth model of Firoozbakht is true and elementary**, and the entire difficulty localizes to the
fluctuation of `p_n` around `n log n`. Still not formalized in Lean after four legs — every probe leg
names this as a non-delivery, and it remains §7's highest-leverage formalization target.

### 2.6 Computational corroboration — `[C]`

Round 1: two independent legs, independent code paths, exhaustive to **`10¹¹`** — 4 118 054 812
consecutive prime pairs; **0** violations of `F`; max `ρ_n = g_n/T_n` (`n ≥ 10`) = **0.8318** at
`p_n = 25 056 082 087`; 40 maximal-gap records; sieve validated against `π(10⁹)`, `π(10¹¹)`.

Round 2 ‹r2› added two further independent sweeps written from statements rather than any round-1
code path: FFM's to `10⁹` (`50 847 533` **indices** — relabelled from "pairs" in round 3, R2-m2) and
the round-2 skeptic's own to `2·10⁸`. Round 3a added `reconcile_recount.py`, round 3b added
`s3_recount.py`, **and this leg adds `verify_syn4.py`** (own sieve, 60-dps re-adjudication of every
near-tie, own segmented-sieve maximal-gap enumeration to `2·10⁸`). All of them reproduce round 1's
headline statistics to every digit quoted, and all return **0** exceptions for P6′-gov and P6′-min in
their range. The discipline worth carrying: the round-2 skeptic is explicit that FFM's `10⁹` decade
is one beyond its own sieve and is **not** independently confirmed, and that nothing in its report
depends on that decade.

The verification discipline itself, unchanged: the escalation path **raises** rather than returns
when a margin lands inside its error budget, because *the silent failure is in the verification
direction*. Round 2 applied it with the sign flipped in the one place it mattered: FFM's refutation
of P6′-pair is the outcome that is *bad news for the run*, so its witnesses were recomputed at 60
digits even though they stand `10⁸`–`10¹²` ulps clear.

---

## 3. What was REFUTED

Nothing about `F`. Everything below refutes a *claim about the evidence* or a *route* — and that
distinction is the whole discipline of this run.

### 3.1 `P6′-pair` is false ‹r2› — the run's own most-quoted lemma, refuted

> **Theorem 1 (FFM).** There exist `m < j < n` with `j` a record index and `T_m > T_n`. Hence
> **P6′-pair is false**, already on `[1, 1847]`.

Two exhibited witnesses, both recomputed at 60 decimal digits, both independently reproduced by two
skeptic legs, and W1 reproduced again by this leg (§8):

| | `m` | `j` (record) | `n` | margin `T_m − T_n` |
|---|---|---|---|---|
| **W1** | 1823 (`p = 15 641`) | 1831 (`p = 15 683`, `g = 44`, the **12th** maximal gap) | 1847 (`p = 15 823`) | `+0.02861060485582…` — `2·10¹²` ulps |
| **W2** | 10 655 449 (`p = 191 912 639`) | 10 655 462 (`p = 191 912 783`, `g = 248`, the **28th** maximal gap ‹r3›) | 10 655 590 (`p = 191 915 033`) | `+3.5792097·10⁻⁵` — `6.3·10⁸` ulps |

Exception census below `10⁹`: **17 exception *indices*** — round 3a relabelled this from "pairs"
(R2-m2), recorded the true pair count (**20** below `3·10⁸`) and stated explicitly that no ratio here
may be read as a density. ⚠ One site in the source document still says *"17 exceptions"* without the
index/pair distinction (S3-m2). The ordinal of W2's record gap is corrected `27th → 28th` (R2-m1)
and **independently re-enumerated by this leg from its own segmented sieve**: 28 records below
`2·10⁸`, `15 683` twelfth, `191 912 783` twenty-eighth, 25 records below `10⁸`.

**The refutation costs the run nothing**, and saying why is the point: by Theorem 2 the pruning route
consumes either of the two weaker predicates, and both survive. A strong-looking lemma was being
carried, unmeasured, for a job it was never needed for.

### 3.2 The implication chain "(gov) ⟹ (min)" is false ‹r2›

Proposition 4 (§2.2). The two surviving predicates are formally **incomparable** — the run had been
treating one as free from the other for two rounds, and round 2's own prose kept doing so after
proving otherwise. Round 3a struck the prose at the three named sites and restored the obligation;
two unnamed sites survive (S3-m1). The empirical ordering that *does* hold (`T_{µ(n)} ≤ T_{r(n)}` at
every swept index) is a measurement, on a range, and is not a proof — FFM §3.2 said so honestly and
three later sections spent it as though it were.

### 3.3 The RH route — five theorems, §2.4.

### 3.4 Bertrand is not merely useless, it is provably closed ‹r2› — `[K]`

Round 1 recorded "Bertrand's postulate is useless here" as an observation. Round 2 turned it into a
kernel-checked theorem at every `n ≥ 2` (§2.1). The difference matters for anyone tempted to
formalize a sharper version: **there is no sharper version of Bertrand that helps**, because the
shortfall is a whole scale, not a constant.

### 3.5 The remaining round-1 refutations, unchanged and uncontradicted

1. **First-failure maximality does not follow from the definitions.** `notebook-0` exhibits an
   explicit increasing integer sequence whose first Firoozbakht failure is at a **non-record** gap,
   in exact integer arithmetic. Consequence: *any proof of FFM that does not consume an arithmetic
   density input is wrong.* The counter-model is excluded unconditionally by Montgomery–Vaughan, by a
   factor that **grows** with scale (1.41 at `10³`, 9.13 at `10¹⁸`).
2. **The two-sided π-bound route to P6′ cannot work.** Past `≈10¹⁰` it is unsatisfiable at *any* gap
   size; no sharpening of constants rescues it.
3. **The `0.9999984` "near-miss" is an artefact.** In a synthetic universe where every gap is `2` the
   same statistic reads `0.99999991` while `ρ` is `0.059`. The statistic measures `1/n`. Only `ρ` is
   diagnostic.
4. **"The tightest cases sit at record gaps" does not survive the range.** A `best[:6]` print
   truncation. At `10¹¹`: 22 of the top 40, and the 4th-tightest case in four billion pairs is not at
   a record index.
5. **More sieve is not more evidence.** Two decades of extra sieving produced no new near-miss; the
   record `ρ` moved exactly once, and moved *at the next maximal gap*. The record that would matter
   (`ρ ≈ 0.948` at `p ≈ 1.693·10¹⁵`) is **4.2 decades** above anything any leg reached.
6. **Littlewood oscillation is irrelevant** to the threshold (`O(L²·log log log x/√x) → 0`).

---

## 4. What remains OPEN

### 4.1 `F` itself — and why it is not close

The load-bearing obstruction, unchanged by four legs and *reinforced* by round 2: **any proof of `F`
yields `g_n = O(log² p_n)` unconditionally.** The best known unconditional gap bound is
`g_n ≪ p_n^{0.525}`; under RH it improves only to `≈ √p_n log p_n`. Both are *powers* of `p_n`; `F`
needs *polylogarithmic*. That is square-root scale versus log scale, and no known method bridges it
even conditionally on RH.

Round 2 sharpened this in three independent places, produced by three legs that were not talking to
each other:

- **Formally** — the only prime-gap input Mathlib carries is proven insufficient at every index
  (§2.1, `[K]`).
- **Analytically** — every envelope `C·p^θ(log p)^A` with `θ > 0` fails beyond finitely many `n`,
  because the bar sits at `θ = 0`; and any hypothesis sufficient for `F` must itself deliver the full
  `log²`-scale uniform bound with leading constant `1` and the second-order term `−L−1` pinned, while
  a hypothesis only `0.17` stronger than that bound already suffices — **the band left for a
  candidate gap bound has width `0.17`** (Theorem D.2, with its own "what this does not say"
  attached).
- **Numerically** — the crossover table, read with round 3a's annotation (§2.4): both BHP and RH are
  insufficient exactly where it matters, and the reading rests on the exponent, not on the plotted
  constants.

Compounding it: **there is no induction mechanism.** `g_n` is not constrained by `g_1 … g_{n−1}`. Any
proposed inductive proof must first supply the missing mechanism.

On the refutation side: the best large-gap results reach
`≍ log n · log log n · log log log log n / log log log n` — a **full power of `log` below** what a
counterexample needs, and explicit constructions place the gap at an *unspecified* location while `F`
needs the gap and the count `π(p_n) = n` at the *same* point. **The refutation door is narrower than
it looks even so:** `¬F` is `Σ₁` and finitely certifiable, but the certificate must certify the
**rank** `n`, not merely the two primes.

### 4.2 The tension that will not resolve itself

The Cramér random model, in Granville's corrected form, predicts
`limsup g_n/log²p_n ≥ 2e^{−γ} ≈ 1.1229 > 1`, **incompatible with `F`**. This is the strongest reason
to believe `F` is false, and it is not a proof. Both cannot be right; no current technique says
which. `granville1995cramer` sits at tier **L1** — fetched and read, but at *preprint pagination*;
every locator must be re-expressed against the journal copy before publication. **No round has
touched this row, and it is the load-bearing citation of the entire refutation-side argument.** The
round-2 citation audit carries the pagination caveat explicitly rather than clearing it. Provenance
priority 1 (§7).

### 4.3 The residual analytic window

Theorem C-a′ proves first-failure maximality against all primes below `0.94970·p_{n₀}` on Dusart
analytics, tightening to a **`0.176 %`** sliver under Theorem C-b′. **Inside that sliver the sandwich
is useless by construction**, and the obstruction is exact and named: one needs an **upper** bound on
`π(p_m + y) − π(p_m)` within a factor `1 + 2/L` of the truth, where Brun–Titchmarsh gives only a
factor `2`. `notebook-0` reaches the same wall computationally and prices it: typical windows are
settled unconditionally by Brun–Titchmarsh at **99.861 %** of governed indices, but the extremal
configuration needs a short-interval count sharp to `1 + 2.2/log p` — **Cramér strength** — and that
gap *widens* with scale even as empirical coverage improves. A pruning rule is worth its worst case.

This remains, in all four legs' judgement, the most tractable genuinely-open analytic node the run
produced — and it is an open problem in analytic number theory, not a lookup.

### 4.4 Lean, honestly

Not formalized after four legs: the smooth model (`L4`), the `limsup` corollary (needs effective
`π(x)` bounds not assumed present in Mathlib), and any verified range past `n ≤ 4`. The last is a
hard limit worth naming: `Nat.nth` is noncomputable with no kernel reduction, and Mathlib's
prime-specific `nth` API is exactly five `@[simp]` base lemmas. Extending needs `Nat.count`↔`Nat.nth`
bridging machinery — a separate budgeted leg. Reporting a larger `N` without it would be a
fabrication, and both probe legs say so in those words.

**And the missing input, named precisely by the round-2 probe:** a Cramér-strength gap bound
`g_n < p_n^{1+1/n} − p_n ≈ (log p_n)²`. No such unconditional theorem exists in the literature.
**Even a complete formalization of every published prime-gap bound, unconditional or RH-conditional,
would not discharge this `sorry`** — the obstruction is mathematical first and formalization-budget
second.

### 4.5 The provenance node that is bigger than any seam ‹r3›

Round 3's clearest structural finding is not one of the reconciliation's five decisions. It is that
**card `L6` — the `2⁶⁴` verification height — is tier `L2_weak` and UNOPENED, and it is load-bearing
in *both* branches of the corpus's headline theorem.** C-a′ consumes it (via `g_{n₀} > 1919`, which
is `p_{n₀} > 2⁶⁴`, licensing the `10⁸` small branch and therefore the *entire* `0.93961 → 0.94970`
improvement) and C-b′ consumes it by the same mechanism at `6 690 557`. **The round-3 skeptic
verified that dependence itself, by tracing it rather than by reading the claim**, and confirms it in
both branches. It is mediated through Kourbatov because `oliveira2014goldbach` returned HTTP 403 to
the round-2 fetch. In the reconciliation leg's own words: *"This is the largest remaining provenance
exposure in the corpus, and it is larger than anything decisions 1–5 touched."* It is named here at
the same altitude as the mathematics because the round-2 synthesis buried it in a citation paragraph,
and that is how a load-bearing unopened source stays unopened for four legs.

Two further exposures travel with it: **every high-precision certificate in the corpus is 50–60-digit
floating point, not interval arithmetic** — and for C-b′'s constant the margin over its own majorant
is `2.40·10⁻⁸` (§2.3, re-derived here); and **`P6′-rec`'s empirical base is 29 record steps**, which
is not a robust statement and must not be described as one.

---

## 5. What round 3 changed — the reconciliation, then the audit that faulted it

Round 3 ran in two legs, and they must be read in order. **Leg 3a (`attack/reconciliation.md`) took
five decisions and landed them in the tree. Leg 3b (`attack/faults.md`) re-audited leg 3a by
recomputation and found all five decisions correct — and two of leg 3a's statements about the tree
false.** §5.1–§5.6 report the decisions; §5.7 reports what the audit found. **Wherever the audit
contradicts the reconciliation, the audit is authoritative**, and this leg has independently
re-checked every such point in the tracked tree.

### 5.1 R2-B1 — two incompatible repairs of one theorem. **CLOSED by designation; designation upheld on re-audit.**

Round 2 was fed round-1's F2 twice and repaired it twice, correctly and independently, into two
theorems neither of which cited the other:

| | **Theorem C-b′** (FFM §7.4) — **LIVE** | Theorem C(b\*) (UVR §3.5) — **RETIRED** |
|---|---|---|
| repaired lemma | (A-high′), `v = ℓ² − ℓ − 1 − 2.1/ℓ` | (A-high\*), `v = ℓ² − ℓ − 1 − 1/ℓ` |
| Axler row | `(2.1,0,0,0)`, `x₀ = 6 690 557` | `(1,0,0,0)`, `x₀ = 1 772 201` |
| uniform constant | `d ≥ 0.0017569` | `d ≥ 0.0043636` |
| headline | **`p_m ≤ 0.998244·p_{n₀}`** | `p_m ≤ 0.99565·p_{n₀}` |
| finite branch | `p_m < 6 690 557`, `g_m ≤ 154` | `p_m < 1 772 201`, `g_m ≤ 132` |
| edition of the row | **present in BOTH arXiv v3 and *Integers* 16 (2016) A22** | ⚠ **arXiv preprint ONLY** |

**Both are mathematically correct** — the round-2 skeptic verified both by *solving* Lemma W's
hypothesis rather than evaluating either leg's sufficient condition, at 40–50 dps. This was never a
correctness dispute; it was a corpus carrying **three constants under one theorem name** (`0.99553`,
`0.99565`, `0.998244`) and **two finite branches** a Lean leg is told to certify.

**The decision, landed:** Theorem C-b′ is the single repaired Theorem C(b); C(b\*) is retired to a
remark; `0.99553`, `0.99565`, `0.0043636` and the pair `1 772 201 / 132` may appear only as history,
with the edition flag attached. **The deciding ground is documentary and was already written down**:
the ledger's `axler2014newbounds` row had carried, since 2026-07-26, a standing downstream rule —
*"do not quote `x ≥ 1 772 201` against the journal citation … the `(2.1,0,0,0)/6 690 557` row is
present in both editions and is strictly stronger; use it"* — **which nobody propagated.** The
designation is the corpus applying a rule it had already recorded.

**On re-audit ‹3b›:** the round-3 skeptic re-derived the designated theorem's cell majorant, tail
bound, exact quadratic requirement and both finite branches from FFM §7.4's *statement*, hunted the
tree for stale live sites of the retired constants, and found none — every surviving `0.99565` /
`1 772 201` / `132` sits inside a retirement remark, a history column or an edition flag. It records
that the decision went **against** the longer sibling document's own theorem, *"the opposite of the
'prefer the leg that wrote more' failure."* This leg re-derived the same constants a third time (§8).

### 5.2 R2-B2 — contradictory Axler tiers. **Limb 1 CLOSED (a skeptic reversed); limb 2 STILL OPEN.**

The same source carried three answers on one day: `source-ledger.md` and card `T1` at **L0**, FFM at
**L0**, and UVR at **L2_strong, NOT OPENED** with a hard quarantine.

**The decision, landed:** `axler2014newbounds` is **L0** — arXiv:1409.1780v3, the published
*Integers* **16** (2016) A22, and the 18 Jan 2018 Corrigendum were fetched, MD5-pinned and read at
the locators on 2026-07-26, by **two legs independently reporting identical MD5s**. UVR's tier labels
are amended and its quarantine **rescoped** rather than struck: it now bites on the preprint-only
*row* and the §4 conflation hazard, not on an unopened source. The residual exposure is **edition,
not tier**, and has exactly two components that travel with every Axler citation: (i) ⚠ corollary
numbering differs between editions (arXiv Cor. 3.5/3.6 = *Integers* Cor. 3.4/3.5, while the
corrigendum uses the **journal's** numbering) — both point at the same inequality, so **no
mathematical error propagated**, but every locator must name its edition; (ii) ⚠ the
`(1,0,0,0)/1 772 201` row is preprint-only.

**Limb 1 — "the ledger amendment was never made" — is FALSE against the tree, and this overturns the
round-2 skeptic.** The amendment landed in commit `61689d0` and merged at `4526b27` (07-26 19:22 /
19:26); round 2's `faults.md` was committed at 20:46 **on a branch cut before that merge**, which is
why its line numbers resolved only in the pre-merge tree. The round-3 skeptic re-verified this by
`git log` on the file rather than from any report, and confirms the reversal.

**Limb 2 — the tier propagation — is NOT closed, and the reconciliation's claim that it is, is
false.** The reconciliation states `axler2014newbounds` is L0 *"at every site in the corpus"*. It
propagated to UVR and nowhere else. **Six sites named by the round-3 skeptic still assert
`L2_strong` / "never opened" / "Citation-gate Priority 1", and this leg's own grep found a seventh**
— see S3-B1 in §5.7 for the full list, the seventh site, and why it is a BLOCKER rather than
bookkeeping.

**The seam, in one sentence, and it is the generalisable one:** UVR's `L2_strong, NOT OPENED` was
**true of UVR** — that leg fetched nothing and said so honestly — and **false of the corpus** the
moment its sibling landed the promotion, with no mechanism to tell it. *A per-leg truth published as
a corpus truth.* The same sentence now describes the reconciliation's own claim to have fixed it.

### 5.3 R2-B3 — an edition-fragile citation. **CLOSED by retirement.**

The Axler row `(1,0,0,0)/x₀ = 1 772 201` exists **only** in arXiv:1409.1780v3 and is absent from the
published *Integers* **16** (2016) #A22 — the preprint's lower-bound table has 14 columns, the
journal's 12. Established by the FFM leg from the PDFs and **independently confirmed by the round-2
skeptic**, which re-fetched all three documents, reproduced all three MD5s and decoded the journal's
font-scrambled table digit-for-digit. Round 3a closed it by retiring the theorem that consumed the
row (§5.1) **and** writing the edition ⚠ into the document that consumed it, not only into card `T1`.
The round-3 skeptic additionally re-verified the retired row's *mathematics* independently —
`π(x) > x/(ℓ−1−1/ℓ−a/ℓ²)` has **0 failures** at every prime below `10⁸` for `a = 1` and `a = 2.1`.

A rider worth carrying: the round-2 skeptic additionally *falsified* the pre-corrigendum range from
the primes themselves — 4 987 066 counterexamples below `10⁸` to the `x ≥ 5.43` clause, smallest at
`p = 59 753` — so **the corrigendum is not merely cited, it is independently needed.**

⚠ **One residue** (S3-m4): card `L4` instructs *"Cite **arXiv v4 only**"*, while the ledger pins
**v3** plus the journal and the corrigendum; no `v4` was fetched by any leg. The same card sentence
carries the stale tier, so both are one edit.

### 5.4 R2-M1 — the `55.92 %` statistic. **Recounted from the statement; two skeptic verdicts reversed; now seven counts against one document.**

This is the seam with the most instructive history in the whole run.

| convention, at `3·10⁶` | round-1 synth | round-2 skeptic | round-2 RH §11 | round-2 synth | reconcile ‹3a› | skeptic ‹3b› | **this leg** | FFM §4 (before r3) |
|---|---|---|---|---|---|---|---|---|
| steps, all `n` | 216 815 | 216 815 | — | 216 815 | 216 815 | 216 815 | **216 815** | 216 814 |
| steps, `n ≥ 10` | 216 806 | 216 806 | 216 806 | 216 806 | 216 806 | 216 806 | **216 806** | 216 805 |
| decreasing, all `n` | 121 239 | 121 239 | — | 121 239 | 121 239 | 121 239 | **121 239** | 121 239 |
| decreasing, `n ≥ 10` | 121 238 | 121 238 | 121 238 | 121 238 | 121 238 | 121 238 | **121 238** | 121 238 |

**Carry `121 238 / 216 806 = 55.920039113 %` (`n ≥ 10`) and `121 239 / 216 815 = 55.918179092 %`
(all `n`).** Every **numerator** agreed everywhere, in every document, in every round. FFM's
denominators were each exactly one lower at every range under both conventions — the fingerprint of a
`T`-array truncated to the *gap*-array length before differencing, which drops the last step (an
increase). **An implementation artefact, not a counting convention** — which is precisely what
`proof-attempt-0.md` §5 had been accused of inventing.

**The adjudication reverses two skeptic verdicts.** `proof-attempt-0.md` §9 item 18's
`121 238 / 216 806` was called an off-by-one by round 1's F5 and re-affirmed as wrong, in bold, by
round 2's FFM §4. **Both were wrong, and round 2 was wrong more emphatically.** `notebook-1` §2's
`374 485 / 664 569` at `10⁷` is likewise correct. Card `L15`'s `216 805` and `notebook-0` R4's
`216 814` were each one too low; **`L15` was the worse of the two, because round 2's amendment landed
the wrong denominator into the canonical card downstream legs read first** — and it is corrected in
the tree.

**The decisive argument was sitting unread in a sibling artifact for a full round.** The round-2 RH
leg's **§11 item 15** ran the count deliberately, got `121 238 / 216 806`, and then found the
*internal* inconsistency that settles the matter beyond a vote: the `n ≥ 11` cut that would give
`216 805` **also drops one descent** (`T_11 < T_10`), so it yields `121 237 / 216 805`. **There is no
convention under which `121 238 / 216 805` is the answer** — the published figure mixed the numerator
of one cut with the denominator of the other. The RH leg flagged it explicitly *"so the next skeptic
re-counts rather than inherits"*, and the round-2 skeptic, the round-2 synthesis and the FFM leg
**all failed to read it**. This leg re-verified both the self-consistency argument and all three cuts
from its own sieve (§8): `T_11 < T_10` confirmed, and the `n ≥ 11` cut gives exactly
`121 237 / 216 805`.

**Two riders that must travel with the figure, every time.** It is **range-dependent** (`55.92 %` at
`3·10⁶`, `56.35 %` at `10⁷`, `56.93 %` at `10⁸`, `≈ 57.9 %` at `10⁹`) and must never be quoted
without its bound and its convention; and it is **uninformative about P6′** under every reading — it
measures single steps, while every P6′ predicate compares an index to a governor many steps back. The
margin that *is* diagnostic (`P6′-min`, `+0.4845277` at `n = 1879`, `µ = 1831`, re-derived here) does
not move at all across the same decades.

⚠ **Bookkeeping residue** (S3-m5): card `L15` says *"Four independent recounts agree"*, card `D5`
says *"Five"*, and both were amended by the same leg in the same commit. With this leg's count the
number is **seven**. Cosmetic, but it is two canonical cards disagreeing, which is the class of thing
round 3 exists to remove.

### 5.5 The MAJORs and MINORs — applied, and where they were only partly applied

- **R2-M2 — the "unconditional" label on Theorem C-a′. Does not stand; applied at one of three
  sites.** FFM's C-a′ was headed *"Dusart only"* and quoted as holding *"unconditionally"*, while its
  small branch consumes card `L6` (L2_weak, unopened) and an in-run gap sieve. **Round-1 F3's exact
  pattern, reappearing in the one branch round 1 had passed clean.** §7.4's header and §13's
  defensible sentence are corrected, and §13's is the model: *"on Dusart's L0 analytics, given the
  published `2⁶⁴` verification height (card `L6`, L2_weak, unopened) and a finite in-run gap
  computation."* ⚠ **Two sites survive** — the verdict table (l. 173) and §7.4's own "Reading of
  Theorem C" (l. 751), the paragraph written to be quoted — **so the document now asserts both
  readings and the quotable one is the wrong one** (S3-M1). Verified in the tree by this leg. §4.5
  promotes the underlying exposure to a first-class open item.
- **R2-M3 — "the weakest of the three". Does not stand; applied at the three named sites.** Struck in
  FFM §3.3/§5/§5.2 and repaired in card `L15`, whose obligation list now carries **both** `P6′-min`
  and `P6′-gov`, with `P6′-rec` beside them (§2.2). Since Theorem 2 shows *either* predicate at `n₀`
  suffices, dropping `gov` was also **strictly lossy**. ⚠ Two unnamed sites in the same document
  still say *"the weakest"* (S3-m1).
- **All seven MINORs dispositioned, and all seven independently re-checked on re-audit:** R2-m1 the
  maximal-gap ordinal `27th → 28th` (now re-enumerated four times, including here); R2-m2 the census
  relabelled from *pairs* to *indices* with the true pair count recorded (one site missed, S3-m2);
  R2-m3 C-b′'s `2.40·10⁻⁸` certification margin recorded next to the constant, **not repaired** —
  repairing it means interval arithmetic; R2-m4 the lean-probe slack table annotated (§2.4); R2-m5
  the write-perimeter tension resolved for that leg by its brief and escalated as a standing process
  question (§7); R2-m6 the `p^{−0.83}` drift annotated with three local per-decade exponents and the
  corrected extrapolation `≈ 6.1·10⁻¹⁵` (a factor `≈ 55` smaller, and the direction is **safe** — the
  noise-floor alarm strengthens); R2-m7 the `10³` per-decade entry `2.42 → 1.354`. The round-3
  skeptic re-derived R2-m6's local exponents itself (`0.4538`, `0.7364`, `0.9967`) and agrees; **this
  leg did not re-derive R2-m6 or R2-m7 and says so.**

### 5.6 The cross-reference layer, and the boundary round 3a refused to cross

Every round-2 artifact — the three proof attempts, the lean-probe report **and** round 2's
`faults.md` — opens with the same round-3 banner: the four-artifact table with post-reconciliation
status, the five decisions in one line each, a pointer to `reconciliation.md`, and the restatement
that `F` is OPEN.

⚠ **The claim the reconciliation attached to that layer does not hold.** It wrote: *"a `write-paper`
leg reading any one of these files now reaches the other three, and finds one answer at every site."*
It reaches them — the banners are real, this leg checked — but it does **not** find one answer at
every site: the RH artifact still gates a live numeral on a tier the corpus has cleared, and six-plus
cards still carry the old tier (S3-B1). *Reachability was delivered; consistency was declared.*

**What round 3a deliberately did not touch, and why it was right not to.** `notebook-{0,1,2}` and
`proof-attempt-{0,1,2}.md` are round-1 artifacts untouched since 2026-07-25, and they carry real
defects — mis-scoped P6′ inferences, `notebook-1`'s mistyped `p*(C)` lower endpoint, the `216 814`
denominator, the reversed `T_{m(n)}` row. **These are not seams.** They are round-1 defects a later
document already reads with the correction stated, and the fix is to supersede them in the paper, not
to add a fifth voice to them. The exceptions it *did* make are exactly the canonical files a
downstream leg reads first — cards `L15`, `D5`, the concept-card `INDEX`, `source-ledger.md`, plus
tier pointers in `proof-attempt-0.md` — **because a wrong denominator in a canonical card is worse
than a disputed line in a proof attempt**. ⚠ One document falls between the two categories and was
missed: `attack/decompose.md` (l. 222, l. 485) still prints the retired `121 238 of 216 805` as a
headline, and it is the frame document a fresh leg reads *before* the cards (S3-m3).

### 5.7 What the round-3 skeptic then found — the two BLOCKERs, re-checked here

`attack/faults.md` (molecule `task-20260727-5096`) is **the corpus's single current fault list**;
round 1's is preserved at `attack/faults-round-1.md` and round 2's at
`attack/re-attack/attack-round-2/faults.md`, both banner-stamped. It closed 12 of round 2's 13
findings (§1) and opened two. **This leg re-checked both against the tree — grep and `git log`, not
the report — and confirms both, and adds one site the skeptic did not list.**

**S3-B1 — BLOCKER — the Axler L0 promotion reached one sibling out of seven.** Decision 2 says the
tier is L0 *"at every site in the corpus"*. Still asserting `L2_strong` / unopened, verified by this
leg's own grep on 2026-07-27:

| site | what it still says |
|---|---|
| `concept-cards/L2-threshold-asymptotics.md:9,78,98` | *"(**L2_strong, NOT OPENED**)"*; *"not fetched in this run"*; *"is at L2_strong and unopened"* |
| `concept-cards/L3-necessary-condition.md:61,67` | *"Axler's Corollary 3.6, unopened"*; *"was never opened"* |
| `concept-cards/L4-sufficient-condition.md:70` | *"not opened in this run; this is Priority 1 for the citation gate"* (+ the `v4` error, S3-m4) |
| `concept-cards/D3-pi-and-count-index-identity.md:60` | *"is at tier L2_strong and was never opened"* |
| `concept-cards/INDEX.md:62`, `:248` | dependency table *"(**L2_strong, unopened**)"*; next-action 2 *"**Open Axler** … Citation-gate Priority 1"* |
| **`concept-cards/INDEX.md:84`** | **`T1` row: *"`axler2014newbounds` (**unopened**)"* — the same INDEX whose own `T1` card records the promotion. Not in the skeptic's list; found by this leg's grep, and it makes the count seven** |
| `re-attack/attack-round-2/proof-attempt-RH-conditional-bound.md:708–711, 941–945` | *"unopened in this run … `0.17` must not be quoted downstream until Axler is at L0"*; *"Citation-gate Priority 1, unchanged since round 1"* |

It is a BLOCKER rather than bookkeeping for a reason this corpus has now paid for twice: **`INDEX.md`
is the entry point, and it currently instructs a funded leg to open a source that has been open since
2026-07-26, with MD5s on the ledger** — and the RH artifact's flag gates a live numeral, not a label.
The instruction to propagate was written on the very ledger row that was propagated *from* (*"…while
cards **T1**/**L2**/**L4** use the preprint's numbering"*); only `T1` was amended.

**S3-B2 — BLOCKER — four statements about the tree, false, and republished by this document's
predecessor as gate status.** Each row below was re-verified by this leg with `git log` and `grep`,
independently of the skeptic's report:

| the claim (reconciliation §6/§7/§8, propagated into the superseded synthesis §0/§7/§8/§9) | the tree, checked here |
|---|---|
| *"`paper/paper.tex` … must be **rewritten** against round 2"* | It **was**, on 2026-07-26 — `d33dfe0` *"write-paper round 2: rewrite paper.tex against round 2, superseding round 1"*, plus `1637cf3`. **2460 lines.** |
| *"it is asserting a tier that is now wrong (« Axler … not opened »)"* | It asserts the **opposite**: its Axler mentions are retrospective (*"the unopened source of the first round; **it is now opened**, read at the locator in both editions"*), with Caveat `haz:axler` recording the promotion and both editorial hazards |
| *"and constants that are now superseded — including `0.99553`"* | `0.99553` appears **exactly once** (verified: `grep -c` = 1), in a round-1-vs-round-2 comparison remark, labelled *"(from a lemma that did not support it)"*. The paper carries **`0.998244`** as the theorem it keeps and already retires `0.99565` — i.e. it reached decision 1 independently, a day early |
| *"**No citation audit has been run on the round-2 corpus at all** — the only one on disk is a round-1, paper-side audit that itself returned **BLOCKED**"* | `attack/verification-report.md` is the **round-2** audit (`cite-20260726-d5a8`, commit `51756c5`, 07-26 21:56), **HEADLINE VERDICT: PASS** — 91 `\cite` instances, 22 citekeys, 59 locator pairs, zero L3, audited against the amended ledger. Separately `attack/editorial-verdict.md` is the **round-2** editorial gate (`42f023a`, REWRITE on the 2460-line paper), which the superseded synthesis called *"round 1"* |

**Where the false claim came from, and why that matters more than the claim.** `paper/paper.tex`
§`sec:defects` says *"no round-2 audit exists"* — **true when the paper was committed (21:45) and
false eleven minutes later (21:56)**. An honest snapshot that nobody refreshed. The reconciliation
carried the snapshot forward as though it were a tree check; the previous synthesis then published it
as the corpus's **headline gate status**, in the document a `write-paper` leg reads first. *A false
statement about a file became a false statement about a gate in two hops, neither of which involved
anyone lying.* That is the mechanism this corpus keeps reproducing, and it is why §1 declines to
promise that one more leg will close it.

**What S3-B2 does *not* overturn.** The reconciliation's §7 items 1, 2, 4, 5, 6 are correct and the
skeptic re-verified each: card `L6` unopened under **both** branches of Theorem C (dependence traced,
not assumed), `granville1995cramer` at preprint pagination under the whole refutation-side argument,
floating-point certificates where interval arithmetic is needed, `P6′-rec` on 29 record steps, and
the `0.176 %` window as genuinely open mathematics. **What was wrong is the account of what the tree
already contains, not the account of what is missing.**

**The two MAJORs, for completeness.** S3-M1 is R2-M2's two unapplied sites (§5.5). S3-M2:
`reconciliation.md` §9 credits `reconcile_recount.py` with a maximal-gap enumeration and four
40-dps exponentials that **the script does not contain** (111 lines; `grep -E "gap|record|exp\("`
returns nothing) — the numbers are right, independently recomputed by the skeptic and again here, but
the named artifact does not produce them. MAJOR rather than BLOCKER for exactly that reason.

---

## 6. Evidence gate — status stated honestly

### **BLOCKED.** Failing leg: **SKEPTIC.**

Source: `attack/evidence-verdict.md` (molecule `task-20260727-2fee`, **v2**, which supersedes the
earlier round-3 verdict in place and reads the *fresh* skeptic audit rather than a stale one). This
synthesis reports that verdict; it does not overturn it, and it has no standing to.

| Leg | Round 2 | **Live (round-3 v2 reading)** | Basis |
|---|---|---|---|
| LOOP (round resolution) | round 2 | **round 2's artifacts, as amended by 3a and re-audited by 3b** | `reattack-verdict.json` present, well-formed, `final_round.round = 2`; `rounds.md`'s "Round 3" section records the resolution order |
| KERNEL | PASS | **PASS** | `lake build` exit 0 / 2208 jobs; `audit_exhaustive` exit 0, 63 declarations, exactly one `sorryAx` — the declared open target. **Re-executed by leg 3b and again by this leg** (§8), not read |
| SKEPTIC | FAIL — 3 BLOCKERs | **FAIL — 2 BLOCKERs (S3-B1, S3-B2), fresh audit, after closing 12 of round 2's 13 findings** | `attack/faults.md` §0: *"The BLOCKER set is non-empty. Round 3 is NOT clean, and the evidence gate stays BLOCKED."* |
| CORPUS | PASS | **PASS**, untouched by round 3 | 27/27 adversarial entries behaved as specified; 109/109 verification checks green; non-coverage stated rather than omitted |

The backend is `lean`, not `none`, so the DEGRADED carve-out does not apply and the kernel leg passes
outright. One failing applicable leg blocks regardless of the others. **`PASS` on the kernel leg is
not the claim `PROVED`** — the kernel verdict is `UNPROVABLE_IN_BUDGET`, and both readings sit in the
same file without conflict.

**What changed at this gate since the previous verdict, precisely.** The previous verdict blocked on
*staleness* — the skeptic artifact had never been re-run against the amended tree. **That re-run has
now happened**, and it is the single most rigorous leg in the run: it re-executed the toolchain,
re-derived every disputed constant from statements with its own scripts, and reversed its own brief's
premise where the brief was wrong. It still blocks — for a **new and narrower reason**: two
cross-artifact accuracy failures, neither mathematical, neither touching `F`.

**Neither round's BLOCKERs touch `F`.** That is why §2–§4 are usable and why the gate is still shut:
those are answers to different questions.

**Why this synthesis is nonetheless usable.** Everything in §2–§4 is kernel-checked (and re-executed
here), independently recomputed (four times over for the disputed figures), or explicitly flagged
with the contested source it rests on. Nothing here quotes a constant from a broken derivation:
`0.004479` appears only as the number that *survived* its own repair, and `0.99565` only as the
theorem §5.1 retires. Nothing here repeats the mis-scoped P6′ inferences or the false "(gov) ⟹ (min)"
chain. And every claim this document makes about the state of a file was checked with `grep` or
`git log` by this leg — the discipline whose absence is S3-B2.

### Citation status — corrected, and still not claimed

**Correction first, because the previous synthesis got this wrong in the direction that matters.** It
stated that no citation audit had been run on this corpus and that the only one on disk was a
round-1, BLOCKED, paper-side audit. **That is false.** On disk:

| artifact | round | molecule / commit | verdict |
|---|---|---|---|
| `attack/verification-report.md` | **round 2** | `cite-20260726-d5a8` / `51756c5` | **PASS** — 91 `\cite`, 22 citekeys, 59 locator pairs, zero L3, zero fabricated citations, every ledger caveat carried into the paper's running text |
| `attack/claims-ledger.md` | **round 2** | `review-20260726-7d55` / `607c416` | 100 rows scored, 3 non-CONFIRMED |
| `attack/editorial-verdict.md` | **round 2** | `review-20260726-7d55` / `42f023a` | **REWRITE** — on the 2460-line round-2 paper, not on round 1's |
| `paper/paper.tex` | **round 2** | `d33dfe0` + `1637cf3` | 2460 lines; treats Axler as opened in both editions; carries `0.998244`; already retires `0.99565` |

**And this document still claims no citation clearance, for three reasons that survive the
correction:**

1. **This leg's brief places the citation audit downstream, at citation-gate, on the final paper.**
   A synthesis leg does not clear it and this one did not run one.
2. **The round-2 audit predates the round-3 decisions.** It passed against the ledger *as of
   2026-07-26*; decisions 1–5 landed on 2026-07-27 (a retired theorem, a designated constant, a
   corrected denominator). Those need re-auditing against the paper — a **check**, not a rewrite,
   since the paper independently reached decision 1.
3. **Two load-bearing sources remain under-opened, and the audit says so rather than clearing
   them:** `granville1995cramer` at preprint pagination (§4.2) and card `L6`'s `2⁶⁴` height (§4.5,
   `oliveira2014goldbach` returned HTTP 403). A PASS that carries its caveats is not clearance of the
   caveats.

**The ledger's own state**, read from the file by this leg: `axler2014newbounds` at **L0**
(`source-ledger.md:426`) with the full three-document fetch record and the edition ⚠, §6 gap 3 marked
`CLOSED 2026-07-26`, and a round-3 reconciliation record at the head. ⚠ Six-to-seven **cards** still
contradict that row (S3-B1) — the ledger is right and the cards are stale, which is the safe
direction but not an acceptable one.

---

## 7. What a next run should do

**The first item is still not a proof attempt, and after four legs that is the finding.** The list is
re-pointed against the tree: two items the previous synthesis funded (a citation audit "that has not
run", a paper rewrite "that must be redone") are struck, because both have run.

| # | Action | Why |
|---|---|---|
| 1 | **One editing pass, tree-checked, closing S3-B1 + S3-B2 + the two MAJORs + five MINORs.** Its brief must *require* `grep`/`git log` before any sentence describing the state of a file, and must forbid describing a file the leg has not opened. | These are the only two BLOCKERs, both closable by editing text — no sieve, no fetch, no derivation. The discipline clause is the load-bearing part: three consecutive rounds have failed **at exactly this step**, and no brief has yet demanded the check. |
| 2 | **Re-audit citations against the round-3 decisions** — a check, not a rewrite | The round-2 audit **PASSED** (`51756c5`) but predates decisions 1–5. The paper already agrees with decision 1 independently. |
| 3 | **Open `granville1995cramer` at journal pagination, and `oliveira2014goldbach`** (or find another L0 route to the `2⁶⁴` height) | The two genuinely-unopened load-bearing sources. `L6` sits under **both** branches of the headline theorem (§4.5); Granville sits under the whole refutation-side argument (§4.2). Larger than any seam round 3 closed. |
| 4 | **Re-run the editorial gate** on the round-2 paper once (1)–(3) land | `editorial-verdict.md` (round 2) returned REWRITE; its reasons should be read against the corrected corpus rather than re-derived. |
| 5 | Attack the residual window (§4.3) as a short-interval prime-count problem | The one genuinely-open analytic node any round isolated exactly, with the criterion `1 + 2/L` in closed form |
| 6 | Formalize the smooth model (`L4`) in Lean | Still the only node in the formalization plan that is a real theorem within Mathlib's reach, and still not done after four legs |
| 7 | Replace C-b′'s float certificate with interval arithmetic | Its margin over its own majorant is `2.40·10⁻⁸` (§2.3) — thin enough that a Lean `norm_num` without directed rounding cannot be assumed to clear it |
| 8 | **Do not fund another proof-attempt fan-out, and do not fund more sieving** | Sieving buys the next maximal gap and nothing between; the record that matters is 4.2 decades away. The fan-out produced every finding rounds 3a/3b had to reconcile. |
| 9 | **Amend the loop's write rule.** Rule 6 (*"round K writes only under `attack-round-K/`"*) is incompatible with a reconciliation stage and needs an explicit exemption | R2-m5 generalised: the stage that owns seams must be allowed to edit the artifacts that carry them, or it can only publish a fifth opinion |
| 10 | **Add a "read your siblings" step to any fan-out brief** | §5.4: a correct, correctly-labelled finding sat unread in a sibling artifact for a full round while three legs published the wrong side of the dispute it settled. Cheapest fix in this table. |

**Standing instruction, unchanged through four legs.** The conjecture is open. Do not write
"Firoozbakht is true". Do not write "Firoozbakht is false". The Cramér–Granville tension is evidence
about which way to bet and nothing more.

---

## 8. Verification of this document

This leg emitted no notebook and no Lean of its own. It re-executed the kernel gates, re-derived
every headline number in a fresh script, and re-checked in the tree every claim it makes about the
state of a file. All three are reported at their exit statuses.

### 8.1 The Lean gates — re-executed here, first-hand

| Command | Exit | Output |
|---|---|---|
| `lake exe cache get` | **0** | — |
| `lake build` | **0** | `Build completed successfully (2208 jobs)`; one warning: `Firoozbakht/Statement.lean:185:8: declaration uses 'sorry'` — the declared open target |
| `lake env lean audit.lean` | **0** | exactly one declaration depending on `sorryAx` |
| `lake env lean audit_exhaustive.lean` | **0** | `declarations scanned: 63` · `depending on sorryAx: [Firoozbakht.firoozbakht]` |
| `grep` for `sorry` in `Firoozbakht/*.lean` | — | exactly **one live token**, `Statement.lean:186`; every other hit is a docstring or comment |
| `shasum -a 256 Firoozbakht/Statement.lean` | — | `6528868823c0637dd182c914e2ef43a7455f851335cafaba6cee934802e004c1` — **identical to the round-3 skeptic's independently recorded anchor** |

**Reading, first-hand: the build is green, the axiom surface is clean, and the single `sorry` is the
conjecture itself.** Four legs have now produced these numbers by *execution* — the round-2
lean-probe, the round-2 skeptic, the round-3 skeptic, and this one.

### 8.2 Independent recomputation — `attack/verify_syn4.py`

Every headline figure was recomputed from the *statements* in a fresh script with no upstream code
path open — it does not import or copy `verify_syn{,2,3}.py`, `reconcile_recount.py`,
`s3_recount.py` or `s3_constants.py`. Own sieve of Eratosthenes and own segmented sieve for the
`2·10⁸` gap enumeration; `mpmath` at 60 decimal digits; every near-tie (relative margin `< 10⁻⁹`)
re-adjudicated exactly.

**Result: `python3 attack/verify_syn4.py` → exit 0, 47/47 checks pass.** Log at
`attack/verify_syn4.out.txt`.

| Quantity as stated in this document | This leg's independent value | Verdict |
|---|---|---|
| `π(3·10⁶)` | 216 816 | ✓ |
| violations of `F` below `3·10⁶` (gap form, 60-dps escalation) | **0** | ✓ |
| violations of `F`, exact integers `p_{n+1}^n < p_n^{n+1}`, `n ≤ 3000` | **0** | ✓ — two formulations, no disagreement |
| near-ties reclassified at 60 dps | **0** — the count is not float-fragile | ✓ |
| steps / decreasing, all `n`; `n ≥ 10`; `n ≥ 11` | `216 815 / 121 239`; `216 806 / 121 238`; `216 805 / 121 237` | ✓ — **§5.4**; `121 238 / 216 805` is impossible under any convention |
| the two percentages | `55.92003911330867…` / `55.91817909277494…` | ✓ |
| `T_11 < T_10` (the descent the `n ≥ 11` cut drops) | confirmed | ✓ |
| ordinal of gap `248` at `p = 191 912 783` | **28th**; 28 records below `2·10⁸`; `15 683` is 12th (`g = 44`); 25 records below `10⁸` | ✓ — R2-m1, fourth independent confirmation |
| P6′-gov / P6′-min exceptions below `3·10⁶` | 0 / 0 | ✓ |
| P6′-min minimum margin | `+0.4845277333983160…` at `n = 1879`, `µ = 1831` | ✓ every digit quoted |
| W1: `p_1823 = 15 641`, `p_1831 = 15 683` (record, `g = 44`), `p_1847 = 15 823`; margin | all four; `+0.02861060485582…` | ✓ — **P6′-pair is false** |
| `e^{−0.0017569}` (C-b′, live) | `0.9982446424453653…` | ✓ |
| `e^{−0.0043636}` (retired) / `e^{−0.0516}` (C-a′) | `0.9956459066696852…` / `0.9497086743460632…` | ✓ |
| `log 6 690 557` / `log 1 772 201` | `15.71620768723352…` / `14.38773283486557…` | ✓ |
| `log 2⁶⁴`; `L(L−1.1)` at `2⁶⁴`; the published integer | `44.36141955583649…`; `1919.137983497532…`; **1920** | ✓ exact |
| RH critical constant `max_x log x/√x` | `0.7357588823428846…` `= 2/e` at `x = e²` | ✓ |
| C-b′ cell majorant, and the certified constant's margin over it | sup `= 0.00175687597478`; margin `= 2.4025·10⁻⁸` | ✓ — R2-m3, and see the correction below |
| barrier: indices `2 ≤ n ≤ 20 000` where Bertrand *certifies* `F`; `p_n < 2^n` exact to `π(3·10⁶)`; Bertrand ties at `n = 1` | 0 / 0 failures / confirmed | ✓ — §2.1 |

**One check failed on the first run, and it was my error, not the corpus's** — reported rather than
smoothed, because a verification pass that only ever confirms is not one. I computed C-b′'s cell
majorant with the `−2.1/b` term evaluated at the cell's **left** endpoint, giving `0.00175614` and a
margin of `7.6·10⁻⁷` — visibly disagreeing with the corpus's `0.00175687590387`. `−2.1/b` is
*increasing* in `b`, so the worst corner is the **right** endpoint; the left-corner value is not a
majorant at all. Corrected, I reproduce `0.0017568759039…` at the corpus's own cell `a = 24.40621` to
twelve digits, and a fine scan of cell left-endpoints gives sup `0.00175687597478` — so the
`2.4·10⁻⁸` margin is **grid-robust**, not an artefact of one chosen grid. That is a slightly stronger
statement than the corpus had, and it arrived through my own mistake.

### 8.3 The tree, checked rather than inherited — the discipline S3-B2 is about

Every claim this document makes about the state of a file was checked here with `grep` or `git log`,
including — especially — the ones I am inheriting from a skeptic report:

- **S3-B2's four rows**: `git log -- paper/paper.tex` (`d33dfe0`, `1637cf3`, 07-26); `wc -l` = 2460;
  `grep -c '0\.99553'` = **1**; `git log -- attack/verification-report.md` (`51756c5`, 07-26 21:56)
  and its own header line 12 — *"HEADLINE VERDICT: PASS"*; `git log -- attack/editorial-verdict.md`
  (`42f023a`) and its header — *"ROUND 2 … supersedes, in place, the round-1 editorial-verdict"*.
  **All four confirmed.**
- **S3-B1's site list**: `grep -rn 'L2_strong\|unopened\|not opened' attack/concept-cards/` — all six
  sites present as described, **plus `INDEX.md:84`, which the skeptic did not list** (§5.7).
- **S3-M1**: FFM `:173` and `:751` read verbatim as the skeptic quotes them. **Confirmed.**
- **S3-m3, S3-m4, S3-m5**: `decompose.md:222`; card `L4:70`'s *"arXiv v4 only"*; `L15:45` *"Four"* vs
  `D5:49` *"Five"*. **All three confirmed.**
- **Ledger and cards**: `source-ledger.md:426` reads tier **L0**; card `L15` carries `216 806`.

### 8.4 Not done, and named rather than omitted

This leg did **not** re-run the `10¹¹` sweeps, the red-team corpus (`corpus/verify_corpus.py`), or
FFM's `10⁹` decade — its own sieve reaches `3·10⁶` for the statistic and `2·10⁸` for the maximal-gap
enumeration, and every figure above that range is attributed to the leg that produced it. It **opened
no source**; every PDF-level provenance statement (MD5s, the 14-vs-12-column tables, the corrigendum
text, the edition numbering) rests on the FFM leg's fetch and the round-2 skeptic's independent
re-fetch, which agree, and is second-hand here. It did **not** re-derive R2-m6's or R2-m7's figures.
It ran **no citation audit** and claims no citation clearance. It **repaired no upstream artifact** —
S3-B1, S3-M1 and the five MINORs are left standing and named, because repairing them is an editing
leg's job (§7 item 1) and a synthesizer that quietly fixed its sources would be reproducing exactly
the un-owned-seam failure this document is about.

### 8.5 Consistency against the brief

Each required element is present and locatable: what was proved (§2, with confidence codes and round
markers), what was refuted (§3), what remains open (§4, with the provenance node promoted to §4.5),
the evidence-gate status stated honestly as **BLOCKED** with the failing leg named (§6), an explicit
statement that no citation clearance is claimed **and** the correction of the previous synthesis's
false claim that no audit exists (§0, §6), the rounds trajectory with the shrink-versus-churn
question answered plainly and in two registers that disagree (§1), and a plain statement of what
round 3 changed — both what the reconciliation landed and what the audit then faulted in it (§5, §5.7).
The verdict rests on the final round named by `reattack-verdict.json` — round 2 — read as amended by
3a and re-certified by 3b.

---

## 9. Sources folded

**Round 3 — the two legs funded outside the loop's cap, and the gate read against them.**

| Artifact | Leg | Molecule |
|---|---|---|
| `attack/faults.md` + `attack/skeptic-round3-checks/` — **the corpus's single current fault list** | skeptic (3b) | `task-20260727-5096` |
| `attack/reconciliation.md` + `attack/reconcile_recount.py` / `.out.txt` | reconcile (3a) | `task-20260727-264e` |
| `attack/evidence-verdict.md` (**v2**, read against the fresh audit) | evidence-gate | `task-20260727-2fee` |
| `attack/re-attack/rounds.md` "Round 3" addendum | reconcile (3a) | `task-20260727-264e` |
| `attack/synthesis.md` (earlier round-3 draft, `4753437`), which this document supersedes | synthesize | `task-20260727-1d5d` |

**Round 2 — the final re-attack round, on which the verdict rests.** Under `attack/re-attack/`, each
carrying a round-3 reconciliation banner:

| Artifact | Leg | Molecule |
|---|---|---|
| `reattack-verdict.json`, `rounds.md`, `synthesis.md` | re-attack loop | `reattack-20260726-57d1` |
| `attack-round-2/proof-attempt-first-failure-maximality.md` | proof-attempt | `task-20260726-56a7` |
| `attack-round-2/proof-attempt-RH-conditional-bound.md` | proof-attempt | `task-20260726-b335` |
| `attack-round-2/proof-attempt-unconditional-verified-range.md` | proof-attempt | `task-20260726-2035` |
| `attack-round-2/lean-probe-report.md`, `unproved.md` | lean-probe | `task-20260726-8ba0` |
| `attack-round-2/faults.md` + `skeptic-round2-checks/` (superseded by `attack/faults.md`) | skeptic | `task-20260726-7211` |
| `lean/Firoozbakht/Barrier.lean` (new, `sorry`-free) | lean-probe | `task-20260726-8ba0` |
| `attack/synthesis.md` (round-2) | synthesize | `task-20260726-7d7d` |
| `paper/paper.tex` (2460 lines), `attack/verification-report.md` (**PASS**), `attack/claims-ledger.md`, `attack/editorial-verdict.md` (REWRITE) | write-paper / cite / review | `d33dfe0`, `cite-20260726-d5a8`, `review-20260726-7d55` |

**Round 1 — pinned, read, never re-run; cited above only where later rounds left it standing.** Under
`attack/`: `decompose.md`, `frame-deliberation/`, `concept-cards/` (30 cards + INDEX, four amended in
round 3), `source-ledger.md` (amended in rounds 2 and 3), `proof-attempt-{0,1,2}.md`,
`notebook-{0,1,2}/`, `lean-probe-report.md`, `coverage-report.md`, `faults-round-1.md`.

---

*Artifact of leg `synthesize`, molecule `task-20260727-4709`, run `germ-20260725-791a7c45`, **round 3,
v2**. Supersedes the round-2 and the earlier round-3 `synthesis.md` in place; the galaxy carries
exactly one current answer. No number in this document was invented; every figure traces to a cited
source artifact or to this leg's own `attack/verify_syn4.py` (47/47, exit 0) and its own execution of
the Lean gates (exit 0/0/0, 2208 jobs, 63 declarations, one `sorryAx`). Every statement about the
state of a file was checked with `grep` or `git log` by this leg. The conjecture `F` remains **OPEN**
— neither proved nor refuted by any round. The evidence gate is **BLOCKED**, failing leg SKEPTIC, on
2 BLOCKERs that are bookkeeping, not mathematics. **No citation clearance is claimed here; a round-2
citation audit exists on disk and returned PASS, and that is not the same thing.***
