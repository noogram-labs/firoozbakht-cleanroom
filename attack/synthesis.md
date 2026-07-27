# Firoozbakht's conjecture — synthesis of the attack

**Molecule:** `task-20260727-1d5d` (leg `synthesize`, crew role: synthesizer) — **ROUND 3**
**Run:** `germ-20260725-791a7c45` · **Re-attack loop:** `reattack-20260726-57d1` (rounds 1–2) ·
**Reconciliation leg:** `task-20260727-264e` (round 3, `attack/reconciliation.md`)
**Date:** 2026-07-27 · **Formal backend:** Lean 4 / Mathlib
**Conjecture under attack (`F`):**

> `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1` — equivalently, `n ↦ (p_n)^{1/n}` is strictly
> decreasing.

**This document supersedes the round-2 `synthesis.md` of the same name, in place.** The galaxy
carries exactly one current answer, and this is it. Two things make this round's document different
from the one it replaces, and both are stated up front because both change what a downstream reader
may rely on:

1. **A reconciliation leg ran between the two documents, and it is authoritative wherever it
   contradicts an earlier artifact** — that was its entire job. `attack/reconciliation.md`
   (molecule `task-20260727-264e`, 2026-07-27) took five decisions and **landed them in the tree**.
   The round-2 synthesis could only *adjudicate*; §5 below reports what is now **done**, and says
   plainly where the reconciliation overturned what the round-2 synthesis, the round-2 skeptic, or
   both, had written.
2. **This leg re-executed the Lean gates itself** rather than reporting them second-hand, and
   re-derived every headline number in a fresh script written from the statements
   (`attack/verify_syn3.py`, 40/40, exit 0). The round-2 synthesis explicitly could not do the
   first — its worktree had no toolchain cache. §8.

**Which round the verdict rests on.** `attack/re-attack/reattack-verdict.json` names
`final_round.round = 2` (`rounds_run = 2`, `rounds_target = 2`,
`exit_reason: "rounds-exhausted"`). The reconciliation leg was funded **outside** that loop's cap
and does not add a `round: 3` entry to the JSON, because it is not a re-attack round — it opened no
mathematics and nucleated no attempts. So, exactly as `attack/re-attack/rounds.md`'s own "Round 3"
section and `attack/evidence-verdict.md` §0 both resolve it: **the verdict rests on round 2's
artifacts, read as amended by round 3's reconciliation.** Round 1's artifacts are pinned inputs,
cited below only where round 2 left them standing, and every such case is marked.

---

## 0. The verdict, in one screen

| Question the brief posed | Answer |
|---|---|
| Was `F` **PROVEN**? | **No.** |
| Was `F` **REFUTED**? | **No.** |
| Status of `F` after three legs of work | **OPEN**, and every round-2 and round-3 artifact says so of itself, at the top, unprompted. |
| Rounds run | **2 re-attack rounds** (`rounds_target = 2`, `exit_reason: rounds-exhausted`) **+ 1 reconciliation leg** funded outside the cap. |
| Did the still-unproved list shrink? | **No — unchanged at one entry, all three legs, and that entry is `F` itself.** §1. This is the honest, expected shape, not a failure. |
| Did the BLOCKER set shrink? | **No. It grew 2 → 3 and changed species; round 3 then discharged all three *as seams*, which is not the same as clearing them.** §1, §5. |
| Evidence-gate status | **BLOCKED** — failing leg `SKEPTIC`. `attack/evidence-verdict.md` (round-3 rewrite, `task-20260727-30dc`). §6. |
| Citation clearance | **NOT ESTABLISHED, and not claimed.** The citation audit has **not** been run on this corpus; it gates the paper downstream, at citation-gate. The only audit on disk is round-1, paper-side, and it returned **BLOCKED**. §6. |

**The one-sentence result of the whole run.** *Firoozbakht's conjecture was neither proved nor
refuted; what three legs of work produced instead is (i) a machine-checked reduction of `F` to the
prime-gap inequality `g_n < T_n`, joined by a machine-checked proof that the only prime-gap input
Mathlib carries (Bertrand) is **provably insufficient at every `n ≥ 2`**, (ii) a table-driven
verification architecture reproducing the published `2⁶⁴` frontier from first principles on
unconditional analytics alone, whose first-failure-maximality theorems then tighten to
`0.94970·p_{n₀}` on Dusart and `0.998244·p_{n₀}` with Axler — *given* the published `2⁶⁴`
verification height, card `L6`, which is unopened (§4.5), (iii)
an exhaustive independent sweep to `10¹¹` with no counterexample and no near-miss, (iv) a
five-theorem closure of the Riemann-Hypothesis route *as a route*, and (v) the outright
**refutation of the run's own most-quoted lemma** (`P6′-pair`), with a proof that two of the
surviving predicates are formally incomparable — all of it now carried in a corpus that gives **one
answer per question**, which is what round 3 bought, and none of which clears the gate.*

**What must not be written downstream.** Not "Firoozbakht is true": no proof exists and the
obstruction analysis (§4.1) shows none is near — round 2 strengthened that reading by *closing* a
route rather than opening one. Not "Firoozbakht is false": the Cramér–Granville tension is a
heuristic, not a test. The defensible sentence, inherited from `decompose` §9, unweakened by
anything found in three legs, and repeated verbatim by the reconciliation leg as a standing
instruction, is: *Firoozbakht's conjecture is numerically robust over the verified range and
simultaneously incompatible with the standard Cramér–Granville heuristic; at least one of the two
must fail, and no current technique can say which.*

---

## 1. The trajectory — three legs, what each fixed, and shrink versus churn

| leg | shape | kernel | skeptic | BLOCKERs | unproved | converged? |
|---|---|---|---|---|---|---|
| **round 1** (upstream, pinned) | fan-out | UNPROVABLE_IN_BUDGET | blockers | **2** (F1, F2) | 1 (`F` itself) | **NO** |
| **round 2** (nucleated by the loop) | wider fan-out — 3 attempts, 1 probe, 1 skeptic | UNPROVABLE_IN_BUDGET | blockers | **3** (R2-B1/B2/B3) | 1 (`F` itself) | **NO** |
| **round 3** (funded outside the cap) | **one reconciliation leg, no fan-out** | not re-run by that leg | **not re-run at all** | 3 discharged *as seams*, **0 re-certified** | 1 (`F` itself) | **NO** |

The loop's stop condition — *kernel PROVED **and** skeptic clean, in the same round* — never held.
`while round < rounds` went false at `2 < 2`, so the loop exited `rounds-exhausted`, never a silent
pass. Round 3 was then funded separately, on the loop's own recommendation, and it is deliberately
**not** a fourth data point on the fan-out curve.

### Did the still-unproved list shrink, or churn?

**Neither. It was unchanged: one entry, every leg, and that entry is `F` itself.**
`unproved-1 = unproved-2 = { Firoozbakht.firoozbakht : Conjecture }` (`Statement.lean:186`), and
round 3 wrote no Lean at all. Nothing regressed; nothing new became `sorry`'d. Saying this plainly
is the point: **an attack on an open `Π₁` statement whose `sorry` count reaches zero would be
reporting a fabrication, not a result.** This leg re-ran the audit itself and reproduces exactly one
`sorryAx` dependent out of 63 declarations (§8) — so the one-entry list is this document's own
measurement, not an inherited claim.

**But the *quality* of the non-shrinkage changed once, in round 2, and that change is real.** Round
1 correctly *declined* to attempt the conjecture. Round 2 attempted it and failed honestly —
`exact?`, `aesop`, `decide` all fail as expected — and then did something round 1 did not: it
**proved a barrier**. `lean/Firoozbakht/Barrier.lean` carries three `sorry`-free theorems showing
Bertrand's ceiling sits strictly *above* the Firoozbakht threshold at **every** `n ≥ 2`. The route
is not "hard"; it is **closed**, kernel-checked. That is genuine progress on the formal leg with an
identical `sorry` count — and it is the only such progress in three legs.

### Did the BLOCKER set shrink, or churn?

**It grew, then changed shape, and it has still never been re-measured. Read honestly: the ledger
churned. That is the signal that says more rounds of the same shape will not help.**

- **Round 1's two BLOCKERs are genuinely fixed** — not self-reported: the round-2 skeptic re-derived
  every step and every constant from the *statements*, at 40–50 decimal digits, and reproduced them
  to the digit. F1 (the three-way `m(n)` definition collision) was fixed by naming, and then
  over-fixed into a refutation (§3.1). F2 (the factor-≈38 bound) was fixed by re-derivation.
- **Round 2 introduced three new BLOCKERs of a different kind.** None is a mathematical error, none
  touches `F`; all three are *seams between artifacts that nobody owned* — two legs repairing the
  same fault into two incompatible theorems (R2-B1), two legs assigning one source contradictory
  tiers (R2-B2), one repair resting on a preprint-only citation (R2-B3).
- **Round 3 closed all three as seams — and closing a seam is not clearing a finding.** The
  corpus now carries one Theorem C(b), one Axler tier, one set of denominators and a cross-reference
  layer. `faults.md`'s own verdict table still reads **3 BLOCKER**, verbatim and unstruck, by the
  reconciler's deliberate choice not to rewrite a red-team report about its own work. **No skeptic
  has read the amended tree.** So the ledger's honest state is: *repaired, un-recertified.*

**The structural reading, which is the useful output of having run three legs instead of one.**
Round 1's own skeptic named the failure mode and predicted its recurrence — *"a fan-out with no
reconciliation stage … nobody owned the seams."* Round 2 **widened** the fan-out, supplied no
reconciliation stage, and reproduced the prediction on itself, one round later, on the very artifact
meant to fix it. Round 3 supplied the missing stage, and the single sharpest thing it found is not
in any of its five decisions: **a correct finding, correctly labelled, sitting in a sibling artifact
(`proof-attempt-RH-conditional-bound.md` §11 item 15) went unread for a full round** — by a skeptic,
a synthesizer and a proof-attempt leg alike, all three of whom then published the wrong side of the
dispute it settled (§5.4). That is the fan-out pathology in one sentence, and no amount of extra
mathematics addresses it.

**So the honest answer to "will more rounds help?" is: more rounds of the *fan-out* shape will
not, and round 3 is the evidence, not the counterexample.** Every mathematical target round 2 was
pointed at, it hit. What remains between this corpus and a clean gate is not research: it is one
skeptic re-run (§7 item 1), and after that a citation audit and one paywalled PDF (§7 items 2–3).

---

## 2. What was PROVED

Confidence codes: **[K]** = machine-checked by the Lean kernel — and, in this document, re-executed
by this leg (§8); **[P]** = paper proof, derived in-run and independently re-derived by the skeptic
leg; **[P·L6]** = paper proof, skeptic-confirmed, resting on the unopened `2⁶⁴` verification height
(card `L6`, tier **L2_weak**) — the corpus's largest remaining provenance exposure, §4.5;
**[C]** = finite computation, exhaustive and independently reproduced. Round-2 results are marked
**‹r2›**; round-3 changes **‹r3›**.

### 2.1 The reduction chain, and the barrier — `[K]`

`Conjecture ↔ ConjectureReal ↔ (∀ n ≥ 1, g_n < T_n)`, where `T_n := p_n(p_n^{1/n} − 1)`, is
**machine-checked**. This leg re-ran every gate rather than quoting round 2's: `lake build` exit 0
(2208 jobs), `lake env lean audit.lean` and `audit_exhaustive.lean` both exit 0, **63 declarations**
scanned, exactly **one** `sorryAx` dependent — the open target. Grep-clean of `axiom`,
`native_decide`, `unsafe`, `@[implemented_by]` outside docstrings; exactly one live `sorry` token,
at `Statement.lean:186`. Full transcript in §8.

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
theorem covers.

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
| **P6′-rec** ‹r2› | `T_j ≤ T_{j′}` for consecutive record indices `j < j′` | open; 0 exceptions in 29 record steps |

- **Theorem 2 (FFM)** `[P]` — *if `F` fails first at `n₀`, then **either** `T_{r(n₀)} ≤ T_{n₀}`
  **or** `T_{µ(n₀)} ≤ T_{n₀}` already forces `g_j < g_{n₀}` for every `j < n₀`.* Both branches are
  three-line chains, both re-derived by the skeptic. **Two consequences that matter more than the
  theorem:** the pruning never needed the predicate that turned out to be false, and **a single
  instance suffices** — the predicate is consumed only at `n₀`, never as a universal statement.
- **Proposition 4 (FFM)** `[P]` — `P6′-gov ⇏ P6′-min` **and** `P6′-min ⇏ P6′-gov`, both by explicit
  four-index counter-models (`g = (2,4,6,3)`). Round 1's fault report had carried the chain
  "(C) ⟹ (A) ⟹ (B), strictly" as though free; **the second link is invalid**, and the missing
  ingredient is P6′-rec, a fourth statement nobody had been measuring under its own name.
- **Lemma M / Theorem B (round 1)** `[P]` — the monotone-bar principle and its instantiation at
  Kourbatov's surrogate bar `S(x) = log²x − log x − 1.17` — survive round 2 unchanged and
  re-verified (`max{g_j : j ≤ 9} = 6 < S(29) = 6.80139`; `S`-breaches below `2·10⁸` are exactly
  `{1,2,3,4,6,9}`).

**The honest status ‹r3›.** P6′-min is the obligation to work (Theorem 2 needs it and its margin does
not decay), **and P6′-gov must be listed beside it, not below it** — round 2's prose had called
P6′-min *"the weakest of the three"* on the strength of an ordering its own Proposition 4 disproves.
Round 3 struck that prose in three places and **restored `P6′-gov` to card `L15`'s obligation list**,
with `P6′-rec` beside them because `gov ∧ rec ⟹ min` is the one valid chain (R2-M3, §5.5). Card
`L15` in the tracked tree now reads exactly that — checked, not inferred.

### 2.3 The finite-range theorem — one theorem, one constant ‹r3› — `[P·L6]` + `[C]`

> ⚠ **Read the code `[P·L6]` before quoting anything in this section.** Every Theorem C constant
> below is *unconditional in its analytics* and *conditional on card `L6`* — the published `2⁶⁴`
> verification height, tier **L2_weak, NOT OPENED** — for its finite branch. The honest form is
> **"unconditional given the published `2⁶⁴` verification height and a finite in-run gap
> computation"**, both named inputs, neither an analytic hypothesis. This is R2-M2's discipline
> (§5.5), and it binds this document as much as the artifacts it folds.

`proof-attempt-2` (round 1) reconstructed from first principles the architecture by which the
literature's `2⁶⁴` frontier is certified; round 2 repaired its central bound; **round 3 chose which
repair the corpus carries.**

- **Lemma A / Corollary A2 / the table-free window** — unchanged and re-verified: `T_n ≥ L(L−1.1)`
  for `p_n ≥ 60 184` (Dusart 2010 Thm 6.9 eq. (6.6), **L0**, fetched and read); a gap of size `g`
  can violate `F` only at `p_n ≤ S(g) := exp((1.1 + √(1.21+4g))/2)`, converting the whole
  verification into a first-occurrence gap-table lookup; and the window `396 738 ≤ p_n ≤ 777 600`
  where `F` follows from unconditional analytic estimates with **no enumeration of primes at all**,
  which **closes permanently** at `p ≈ 7.776·10⁵`.
- **Independent reproduction of the published `1920`** `[C]` — `L(L−1.1)` at `2⁶⁴` is
  `1919.13798349753288…` (this leg's own value, 60 dps), so a gap of at least 1920 is needed to
  violate `F` just below `2⁶⁴`. The published integer falls out with no tuning. The caveat that
  makes this honest stands: Lemma A gives the *local* statement at the frontier, and the published
  endnote's phrasing is *global*.
- **F2 repaired ‹r2›** — the round-1 bound `(A-high)` `T_n ≤ (ℓ²−ℓ−1−1/ℓ)(1 + ℓ⁴/x)` did not follow
  from its stated justification and was false by a factor `≈ 38.8` over part of its range. Both
  round-2 legs restated it in the tight form `T_n < v(1 + v/x)`, proved from the elementary
  primitive rather than by weakening, and **replaced the numerical sweep by a proof**. The round-1
  conclusion survives — the printed `0.004479` *is* sufficient — but for a reason the printed
  derivation did not supply.
- **Theorem C, as the corpus now carries it ‹r3›.** *If `F` first fails at `n₀`, then `g_{n₀}`
  exceeds every gap between primes below a definite multiple of `p_{n₀}`:*

| branch | round 1 | **live form** | source |
|---|---|---|---|
| Dusart only (**Theorem C-a′**) | `d ≥ 0.0623` → `p_m ≤ 0.93961·p_{n₀}` | **`d ≥ 0.0516` → `p_m ≤ 0.94970·p_{n₀}`** | `dusart2010estimates`, **L0** — *analytics only*; the finite branch consumes card `L6` and an in-run gap sieve ‹r3› |
| with Axler (**Theorem C-b′**) | `d ≥ 0.004479` → `p_m ≤ 0.99553·p_{n₀}`, from a lemma that did not support it | **`d ≥ 0.0017569` → `p_m ≤ 0.998244·p_{n₀}`** | `axler2014newbounds`, **L0** ‹r3›, row `(2.1,0,0,0)/6 690 557`, present in **both** editions |

  The Dusart branch improves only because the small-branch cutoff rises from `60 184` to `10⁸`
  (licensed by `g_m ≤ 220 < 1919`); it **cannot** improve much further — `d*(ℓ) → 0.05`, so the
  Dusart-only sliver is pinned near `5 %` at every scale. The residual sliver on the Axler branch
  has relative width `0.176 %` at `2⁶⁴`.

  **Round 2 shipped the F2 repair twice, into two incompatible theorems; round 3 designated one.**
  **Theorem C-b′ (`0.998244`) is the corpus's single repaired Theorem C(b).** Theorem C(b\*)
  (`0.99565`, off the preprint-only Axler row `(1,0,0,0)/1 772 201`) is **retired to a remark**, and
  `0.99553` and `0.99565` are retired with it. The deciding ground is documentary, not aesthetic —
  §5.1 — and it is lucky in one respect worth recording: the edition-safe theorem is also the
  sharper one, so nothing was paid for the provenance.

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

**The round-2 quantifier repair, recorded because it is a correction and not a restatement.**
Round 1's headline read *"and at no other index whatsoever"*, and that is **false as stated**: the
CMS envelope also sits below the threshold at `n = 1` and `n = 2`. What excludes those two indices
is **the source's hypothesis `p_n > 3`, not the arithmetic**. Round 2 proves the two statements
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
row names — so both crossovers are **illustrations at a chosen constant, not measurements**
(R2-m4). The conclusion is unaffected, and the reason is worth carrying: it rests on the
**exponent**, and Theorems B and C refute every `C > 0`.

### 2.5 The smooth model — `[P]`

`decompose` §3.6: the smooth surrogate `(x log x)^{1/x}` is strictly decreasing on `x ≥ 5`. **The
smooth model of Firoozbakht is true and elementary**, and the entire difficulty localizes to the
fluctuation of `p_n` around `n log n`. Still not formalized in Lean after three legs — every probe
leg names this as a non-delivery, and it remains §7's highest-leverage formalization target.

### 2.6 Computational corroboration — `[C]`

Round 1: two independent legs, independent code paths, exhaustive to **`10¹¹`** — 4 118 054 812
consecutive prime pairs; **0** violations of `F`; max `ρ_n = g_n/T_n` (`n ≥ 10`) = **0.8318** at
`p_n = 25 056 082 087`; 40 maximal-gap records; sieve validated against `π(10⁹)`, `π(10¹¹)`.

Round 2 ‹r2› added two further independent sweeps written from statements rather than any round-1
code path: FFM's to `10⁹` (`50 847 533` **indices** — relabelled from "pairs" in round 3, R2-m2) and
the skeptic's own to `2·10⁸`. Round 3 added another (`reconcile_recount.py`), and **this leg adds one
more** (`verify_syn3.py`, own sieve, 60-dps re-adjudication of every near-tie). All of them
reproduce round 1's headline statistics to every digit quoted, and all return **0** exceptions for
P6′-gov, P6′-min, P6′-rec and `T_{µ(n)} ≤ T_{r(n)}`. The discipline worth carrying: the round-2
skeptic is explicit that FFM's `10⁹` decade is one beyond its own sieve and is **not** independently
confirmed, and that nothing in its report depends on that decade.

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

Two exhibited witnesses, both recomputed at 60 decimal digits, both independently reproduced by the
skeptic, and W1 reproduced again by this leg (§8):

| | `m` | `j` (record) | `n` | margin `T_m − T_n` |
|---|---|---|---|---|
| **W1** | 1823 (`p = 15 641`) | 1831 (`p = 15 683`, `g = 44`, the **12th** maximal gap) | 1847 (`p = 15 823`) | `+0.0286106048…` — `2·10¹²` ulps |
| **W2** | 10 655 449 (`p = 191 912 639`) | 10 655 462 (`p = 191 912 783`, `g = 248`, the **28th** maximal gap ‹r3›) | 10 655 590 (`p = 191 915 033`) | `+3.5792097·10⁻⁵` — `6.3·10⁸` ulps |

Exception census below `10⁹`: **17 exception *indices*** — round 3 relabelled this from "pairs"
(R2-m2), recorded the true pair count (**20** below `3·10⁸`) and stated explicitly that no ratio
here may be read as a density. The ordinal of W2's record gap is corrected `27th → 28th` (R2-m1) and
**independently re-enumerated by this leg**: 28 records below `2·10⁸`, `15 683` twelfth, `191 912 783`
twenty-eighth, 25 records below `10⁸`.

**The refutation costs the run nothing**, and saying why is the point: by Theorem 2 the pruning
route consumes either of the two weaker predicates, and both survive. A strong-looking lemma was
being carried, unmeasured, for a job it was never needed for.

### 3.2 The implication chain "(gov) ⟹ (min)" is false ‹r2›

Proposition 4 (§2.2). The two surviving predicates are formally **incomparable** — the run had been
treating one as free from the other for two rounds, and round 2's own prose kept doing so after
proving otherwise. Round 3 struck the prose and restored the obligation (§5.5). The empirical
ordering that *does* hold (`T_{µ(n)} ≤ T_{r(n)}` at every swept index) is a measurement, on a range,
and is not a proof — FFM §3.2 said so honestly and three later sections spent it as though it were.

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
   density input is wrong.* The counter-model is excluded unconditionally by Montgomery–Vaughan, by
   a factor that **grows** with scale (1.41 at `10³`, 9.13 at `10¹⁸`).
2. **The two-sided π-bound route to P6′ cannot work.** Past `≈10¹⁰` it is unsatisfiable at *any* gap
   size; no sharpening of constants rescues it.
3. **The `0.9999984` "near-miss" is an artefact.** In a synthetic universe where every gap is `2`
   the same statistic reads `0.99999991` while `ρ` is `0.059`. The statistic measures `1/n`. Only
   `ρ` is diagnostic.
4. **"The tightest cases sit at record gaps" does not survive the range.** A `best[:6]` print
   truncation. At `10¹¹`: 22 of the top 40, and the 4th-tightest case in four billion pairs is not
   at a record index.
5. **More sieve is not more evidence.** Two decades of extra sieving produced no new near-miss; the
   record `ρ` moved exactly once, and moved *at the next maximal gap*. The record that would matter
   (`ρ ≈ 0.948` at `p ≈ 1.693·10¹⁵`) is **4.2 decades** above anything any leg reached.
6. **Littlewood oscillation is irrelevant** to the threshold (`O(L²·log log log x/√x) → 0`).

---

## 4. What remains OPEN

### 4.1 `F` itself — and why it is not close

The load-bearing obstruction, unchanged by three legs and *reinforced* by round 2: **any proof of
`F` yields `g_n = O(log² p_n)` unconditionally.** The best known unconditional gap bound is
`g_n ≪ p_n^{0.525}`; under RH it improves only to `≈ √p_n log p_n`. Both are *powers* of `p_n`; `F`
needs *polylogarithmic*. That is square-root scale versus log scale, and no known method bridges it
even conditionally on RH.

Round 2 sharpened this in three independent places, produced by three legs that were not talking to
each other:

- **Formally** — the only prime-gap input Mathlib carries is proven insufficient at every index
  (§2.1, `[K]`).
- **Analytically** — every envelope `C·p^θ(log p)^A` with `θ > 0` fails beyond finitely many `n`,
  because the bar sits at `θ = 0`; and any hypothesis sufficient for `F` must itself deliver the
  full `log²`-scale uniform bound with leading constant `1` and the second-order term `−L−1`
  pinned, while a hypothesis only `0.17` stronger than that bound already suffices — **the band left
  for a candidate gap bound has width `0.17`** (Theorem D.2, with its own "what this does not say"
  attached).
- **Numerically** — the crossover table, read with round 3's annotation (§2.4): both BHP and RH are
  insufficient exactly where it matters, and the reading rests on the exponent, not on the plotted
  constants.

Compounding it: **there is no induction mechanism.** `g_n` is not constrained by `g_1 … g_{n−1}`.
Any proposed inductive proof must first supply the missing mechanism.

On the refutation side: the best large-gap results reach
`≍ log n · log log n · log log log log n / log log log n` — a **full power of `log` below** what a
counterexample needs, and explicit constructions place the gap at an *unspecified* location while
`F` needs the gap and the count `π(p_n) = n` at the *same* point. **The refutation door is narrower
than it looks even so:** `¬F` is `Σ₁` and finitely certifiable, but the certificate must certify the
**rank** `n`, not merely the two primes.

### 4.2 The tension that will not resolve itself

The Cramér random model, in Granville's corrected form, predicts
`limsup g_n/log²p_n ≥ 2e^{−γ} ≈ 1.1229 > 1`, **incompatible with `F`**. This is the strongest reason
to believe `F` is false, and it is not a proof. Both cannot be right; no current technique says
which. `granville1995cramer` sits at tier **L1** — fetched and read, but at *preprint pagination*;
every locator must be re-expressed against the journal copy before publication. **Neither round 2
nor round 3 touched this row, and it is the load-bearing citation of the entire refutation-side
argument.** Audit priority 1 (§7 item 2).

### 4.3 The residual analytic window

Theorem C-a′ proves first-failure maximality against all primes below `0.94970·p_{n₀}` on Dusart
analytics, tightening to a **`0.176 %`** sliver under Theorem C-b′. **Inside that sliver the
sandwich is useless by construction**, and the obstruction is exact and named: one needs an
**upper** bound on `π(p_m + y) − π(p_m)` within a factor `1 + 2/L` of the truth, where
Brun–Titchmarsh gives only a factor `2`. `notebook-0` reaches the same wall computationally and
prices it: typical windows are settled unconditionally by Brun–Titchmarsh at **99.861 %** of
governed indices, but the extremal configuration needs a short-interval count sharp to
`1 + 2.2/log p` — **Cramér strength** — and that gap *widens* with scale even as empirical coverage
improves. A pruning rule is worth its worst case.

This remains, in all three legs' judgement, the most tractable genuinely-open analytic node the run
produced — and it is an open problem in analytic number theory, not a lookup.

### 4.4 Lean, honestly

Not formalized after three legs: the smooth model (`L4`), the `limsup` corollary (needs effective
`π(x)` bounds not assumed present in Mathlib), and any verified range past `n ≤ 4`. The last is a
hard limit worth naming: `Nat.nth` is noncomputable with no kernel reduction, and Mathlib's
prime-specific `nth` API is exactly five `@[simp]` base lemmas. Extending needs `Nat.count`↔`Nat.nth`
bridging machinery — a separate budgeted leg. Reporting a larger `N` without it would be a
fabrication, and both probe legs say so in those words.

**And the missing input, named precisely by the round-2 probe:** a Cramér-strength gap bound
`g_n < p_n^{1+1/n} − p_n ≈ (log p_n)²`. No such unconditional theorem exists in the literature.
**Even a complete formalization of every published prime-gap bound, unconditional or
RH-conditional, would not discharge this `sorry`** — the obstruction is mathematical first and
formalization-budget second.

### 4.5 The provenance node that is bigger than any seam ‹r3›

Round 3's clearest structural finding is not one of its five decisions. It is that **card `L6` — the
`2⁶⁴` verification height — is tier `L2_weak` and UNOPENED, and it is load-bearing in *both*
branches of the corpus's headline theorem.** C-a′ consumes it (via `g_{n₀} > 1919`, which licenses
the `10⁸` small branch and therefore the *entire* `0.93961 → 0.94970` improvement) and C-b′
consumes it by the same mechanism at `6 690 557`. It is mediated through Kourbatov because
`oliveira2014goldbach` returned HTTP 403 to the round-2 fetch. In the reconciliation leg's own
words: *"This is the largest remaining provenance exposure in the corpus, and it is larger than
anything decisions 1–5 touched."* It is named here at the same altitude as the mathematics because
the round-2 synthesis buried it in a citation paragraph, and that is how a load-bearing unopened
source stays unopened for three legs.

Two further exposures travel with it: **every high-precision certificate in the corpus is 50–60-digit
floating point, not interval arithmetic** — and for one constant (C-b′'s, R2-m3) the margin over its
own majorant is only `2.4·10⁻⁸`, which is far less headroom than a Lean `norm_num` without directed
rounding can be assumed to have; and **`P6′-rec`'s empirical base is 29 record steps**, which is not
a robust statement and must not be described as one.

---

## 5. What the reconciliation changed — stated plainly

The reconciliation leg (`attack/reconciliation.md`, molecule `task-20260727-264e`, 2026-07-27) is
**authoritative wherever it contradicts an earlier artifact, including this document's own
predecessor.** It opened no mathematics, wrote no Lean, re-ran no gate and cleared nothing. What it
did is remove ambiguity: **the corpus now gives one answer per question.** Below, each of the five
decisions, with what it overturned — and this leg has re-checked each in the tracked tree rather
than reading the report, which is the lesson the corpus keeps having to relearn.

### 5.1 R2-B1 — two incompatible repairs of one theorem. **CLOSED by designation.**

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
correctness dispute; it was a corpus carrying **three constants under one theorem name**
(`0.99553`, `0.99565`, `0.998244`) and **two finite branches** a Lean leg is told to certify.

**The decision, landed:** Theorem C-b′ is the single repaired Theorem C(b); C(b\*) is retired to a
remark; `0.99553`, `0.99565`, `0.0043636` and the pair `1 772 201 / 132` may appear only as history,
with the edition flag attached. **The deciding ground is documentary and was already written down**:
the ledger's `axler2014newbounds` row had carried, since 2026-07-26, a standing downstream rule —
*"do not quote `x ≥ 1 772 201` against the journal citation … the `(2.1,0,0,0)/6 690 557` row is
present in both editions and is strictly stronger; use it"* — **which nobody propagated.** The
designation is the corpus applying a rule it had already recorded. Verified in the tree: UVR §3.5
carries the retirement notice; FFM §7.4 carries the designation.

**What C(b\*) is kept for.** Not sentiment: its `0.0043636` sits below round 1's printed `0.004479`,
so it is the cleanest available proof that **round 1's conclusion survived its own broken
derivation**. It is calibration, retained in place as a remark.

### 5.2 R2-B2 — contradictory Axler tiers. **Limb 1 STALE; limb 2 CLOSED.**

The same source carried three answers on one day: `source-ledger.md` and card `T1` at **L0**,
FFM at **L0**, and UVR at **L2_strong, NOT OPENED** with a hard quarantine.

**The decision, landed:** `axler2014newbounds` is **L0** at every site — arXiv:1409.1780v3, the
published *Integers* **16** (2016) A22, and the 18 Jan 2018 Corrigendum were fetched, MD5-pinned and
read at the locators on 2026-07-26, by **two legs independently reporting identical MD5s**. UVR's
tier labels are amended and its quarantine **rescoped** rather than struck: it now bites on the
preprint-only *row* and the §4 conflation hazard, not on an unopened source. The residual exposure
is **edition, not tier**, and has exactly two components that travel with every Axler citation:
(i) ⚠ corollary numbering differs between editions (arXiv Cor. 3.5/3.6 = *Integers* Cor. 3.4/3.5,
while the corrigendum uses the **journal's** numbering) — both point at the same inequality, so **no
mathematical error propagated**, but every locator must name its edition; (ii) ⚠ the
`(1,0,0,0)/1 772 201` row is preprint-only.

**The seam, in one sentence, and it is the generalisable one:** UVR's `L2_strong, NOT OPENED` was
**true of UVR** — that leg fetched nothing and said so honestly — and **false of the corpus** the
moment its sibling landed the promotion, with no mechanism to tell it. *A per-leg truth published
as a corpus truth.*

**Limb 1 — "the ledger amendment was never made" — is FALSE against the tree, and this overturns
the round-2 skeptic.** The amendment landed in commit `61689d0` and merged at `4526b27`; the
skeptic's cited line numbers resolve only in a worktree branched before the merge. The round-2
synthesis reached the same conclusion independently — and caught the identical error *in its own
draft*. **So the same error — reading a report instead of the tree — was committed by a skeptic and
by a synthesizer, one round apart, about the same commit.** This leg's own tree check adds a small
third instance of the same species: the reconciliation leg cites the Axler ledger row at
**line 412**; in the tree today it is at **line 426**, the row having moved under subsequent edits.
The tier is L0 at both. *Line numbers are not evidence about content; `git show` and `grep` are.*

### 5.3 R2-B3 — an edition-fragile citation. **CLOSED by retirement.**

The Axler row `(1,0,0,0)/x₀ = 1 772 201` exists **only** in arXiv:1409.1780v3 and is absent from the
published *Integers* **16** (2016) #A22 — the preprint's lower-bound table has 14 columns, the
journal's 12. Established by the FFM leg from the PDFs and **independently confirmed by the round-2
skeptic**, which re-fetched all three documents, reproduced all three MD5s and decoded the journal's
font-scrambled table digit-for-digit. Round 3 closed it by retiring the theorem that consumed the
row (§5.1) **and** writing the edition ⚠ into the document that consumed it, not only into card
`T1` — the round-2 synthesis's complaint that the corpus flagged the hazard everywhere except where
it was spent is now discharged.

A rider worth carrying: the skeptic additionally *falsified* the pre-corrigendum range from the
primes themselves — 4 987 066 counterexamples below `10⁸` to the `x ≥ 5.43` clause, smallest at
`p = 59 753` — so **the corrigendum is not merely cited, it is independently needed.**

### 5.4 R2-M1 — the `55.92 %` statistic. **Recounted from the statement; two skeptic verdicts reversed.**

This is the seam with the most instructive history in the whole run.

| convention, at `3·10⁶` | round-1 synth | round-2 skeptic | round-2 RH §11 | round-2 synth | round-3 reconcile | **this leg** | FFM §4 (before r3) |
|---|---|---|---|---|---|---|---|
| steps, all `n` | 216 815 | 216 815 | — | 216 815 | 216 815 | **216 815** | 216 814 |
| steps, `n ≥ 10` | 216 806 | 216 806 | 216 806 | 216 806 | 216 806 | **216 806** | 216 805 |
| decreasing, all `n` | 121 239 | 121 239 | — | 121 239 | 121 239 | **121 239** | 121 239 |
| decreasing, `n ≥ 10` | 121 238 | 121 238 | 121 238 | 121 238 | 121 238 | **121 238** | 121 238 |

**Carry `121 238 / 216 806 = 55.920039113 %` (`n ≥ 10`) and `121 239 / 216 815 = 55.918179092 %`
(all `n`).** Every **numerator** agreed everywhere, in every document, in every round. FFM's
denominators were each exactly one lower at every range under both conventions — the fingerprint of
a `T`-array truncated to the *gap*-array length before differencing, which drops the last step (an
increase). **An implementation artefact, not a counting convention** — which is precisely what
`proof-attempt-0.md` §5 had been accused of inventing.

**The adjudication reverses two skeptic verdicts, and it is now six counts against one document.**
`proof-attempt-0.md` §9 item 18's `121 238 / 216 806` was called an off-by-one by round 1's F5 and
re-affirmed as wrong, in bold, by round 2's FFM §4. **Both were wrong, and round 2 was wrong more
emphatically.** `notebook-1` §2's `374 485 / 664 569` at `10⁷` is likewise correct. Card `L15`'s
`216 805` and `notebook-0` R4's `216 814` were each one too low; **`L15` was the worse of the two,
because round 2's amendment landed the wrong denominator into the canonical card downstream legs
read first** — and it is corrected in the tree (this leg re-read the card: it now reads
`121 238 of 216 806`, with both conventions and the correction dated).

**And the decisive argument was sitting unread in a sibling artifact for a full round.** The round-2
RH leg's **§11 item 15** did not merely state a compatible sieve size — it ran the count
deliberately, got `121 238 / 216 806`, and then found the *internal* inconsistency that settles the
matter beyond a vote: the `n ≥ 11` cut that would give `216 805` **also drops one descent**
(`T_11 < T_10`), so it yields `121 237 / 216 805`. **There is no convention under which
`121 238 / 216 805` is the answer** — the published figure mixes the numerator of one cut with the
denominator of the other. The RH leg flagged it explicitly *"so the next skeptic re-counts rather
than inherits"*, and the round-2 skeptic, the round-2 synthesis and the FFM leg **all failed to read
it**. This leg re-verified both the self-consistency argument and the count from its own sieve
(§8): `T_11 < T_10` confirmed, and the `n ≥ 11` cut gives exactly `121 237 / 216 805`.

**Two riders that must travel with the figure, every time.** It is **range-dependent** (`55.92 %` at
`3·10⁶`, `56.35 %` at `10⁷`, `56.93 %` at `10⁸`, `≈ 57.9 %` at `10⁹`) and must never be quoted
without its bound and its convention; and it is **uninformative about P6′** under every reading — it
measures single steps, while every P6′ predicate compares an index to a governor many steps back.
The margin that *is* diagnostic (`P6′-min`, `+0.4845277` at `n = 1879`, re-derived here) does not
move at all across the same decades.

### 5.5 The MAJORs and MINORs — applied, not deferred

- **R2-M2 — the "unconditional" label on Theorem C-a′. Does not stand; applied.** FFM's C-a′ was
  headed *"Dusart only — no source outside `dusart2010estimates`, L0"* and quoted as holding
  *"unconditionally"*, while its small branch consumes card `L6` (L2_weak, unopened) and an in-run
  gap sieve. **Round-1 F3's exact pattern, reappearing in the one branch round 1 had passed clean.**
  The header now reads *"Dusart-only **analytics**; the finite branch consumes card `L6` (L2_weak,
  unopened) and an in-run gap sieve to `10⁸`"*, with the honest form spelled out: *unconditional
  given the published `2⁶⁴` verification height and a finite in-run gap computation* — both named
  inputs, neither an analytic hypothesis. **The theorem is correct; only the provenance sentence
  was.** §4.5 promotes the underlying exposure to a first-class open item.
- **R2-M3 — "the weakest of the three". Does not stand; applied.** Struck in FFM §3.3/§5/§5.2 and
  repaired in card `L15`, whose obligation list now carries **both** `P6′-min` and `P6′-gov`, with
  `P6′-rec` beside them (§2.2). Since Theorem 2 shows *either* predicate at `n₀` suffices, dropping
  `gov` was also **strictly lossy**.
- **All seven MINORs are dispositioned** (`reconciliation.md` §5): R2-m1 the maximal-gap ordinal
  `27th → 28th` (independently re-verified twice, including here); R2-m2 the census relabelled from
  *pairs* to *indices* with the true pair count recorded; R2-m3 C-b′'s `2.4·10⁻⁸` certification
  margin recorded next to the constant, **not repaired** — repairing it means interval arithmetic,
  which is a funded leg, not an edit; R2-m4 the lean-probe slack table annotated (§2.4); R2-m5 the
  write-perimeter tension resolved for that leg by its brief and escalated as a standing process
  question (§7 item 8); R2-m6 the `p^{−0.83}` drift annotated with three local per-decade exponents
  (`0.4536`, `0.7365`, `0.9967`) and the corrected extrapolation `≈ 6.1·10⁻¹⁵` (a factor `≈ 55`
  smaller, and the direction is **safe** — the noise-floor alarm strengthens); R2-m7 the `10³`
  per-decade entry `2.42 → 1.354`. R2-m6 and R2-m7's figures are the round-2 skeptic's and were
  **not** re-derived by round 3 or by this leg, and both say so at each site.

### 5.6 The cross-reference layer, and the boundary round 3 refused to cross

Every round-2 artifact — the three proof attempts, the lean-probe report **and** `faults.md` — now
opens with the same round-3 banner: the four-artifact table with post-reconciliation status, the
five decisions in one line each, a pointer to `reconciliation.md`, and the restatement that `F` is
OPEN. **A `write-paper` leg reading any one of these files now reaches the other three and finds one
answer at every site.**

**What round 3 deliberately did not touch, and why it was right not to.** `notebook-{0,1,2}` and
`proof-attempt-{0,1,2}.md` are round-1 artifacts untouched since 2026-07-25, and they carry real
defects — mis-scoped P6′ inferences, `notebook-1`'s mistyped `p*(C)` lower endpoint, the `216 814`
denominator, the reversed `T_{m(n)}` row. **These are not seams.** They are round-1 defects a later
document already reads with the correction stated, and the fix is to supersede them in the paper,
not to add a fifth voice to them. The exceptions round 3 *did* make are exactly the canonical files
a downstream leg reads first — cards `L15`, `D5`, the concept-card `INDEX`, `source-ledger.md`, plus
tier pointers in `proof-attempt-0.md` — **because a wrong denominator in a canonical card is worse
than a disputed line in a proof attempt**, which is what made R2-M1 expensive. Naming that boundary
is part of the deliverable: a reconciliation leg that quietly widens its own scope reproduces the
fan-out it exists to stop.

---

## 6. Evidence gate — status stated honestly

### **BLOCKED.** Failing leg: **SKEPTIC.**

Source: `attack/evidence-verdict.md` (molecule `task-20260727-30dc`, a **round-3 rewrite** that
supersedes its round-2 predecessor and reads round 2's artifacts *as amended by* the reconciliation).
This synthesis reports that verdict; it does not overturn it, and it has no standing to.

| Leg | Round 2 | **Live (round-3 reading)** | Basis |
|---|---|---|---|
| LOOP (round resolution) | round 2 | **round 2's artifacts, as amended by round 3** | `reattack-verdict.json` present, well-formed, `final_round.round = 2`; `rounds.md`'s own "Round 3" section records the resolution order |
| KERNEL | PASS | **PASS** | `lake build` exit 0 / 2208 jobs; `audit_exhaustive` exit 0, 63 declarations, exactly one `sorryAx` — the declared open target. **Re-executed by this leg** (§8), not read |
| SKEPTIC | FAIL — 3 BLOCKERs | **FAIL — same 3 BLOCKERs, discharged as seams by round 3, re-certified by nobody** | `faults.md` §0 still reads verbatim *"The BLOCKER set is non-empty. Round 2 is NOT clean"* |
| CORPUS | PASS | **PASS**, untouched by round 3 | 27/27 adversarial entries behaved as specified; 109/109 verification checks green; non-coverage stated rather than omitted |

The backend is `lean`, not `none`, so the DEGRADED carve-out does not apply and the kernel leg passes
outright. One failing applicable leg blocks regardless of the other three. **`PASS` on the kernel
leg is not the claim `PROVED`** — the kernel verdict is `UNPROVABLE_IN_BUDGET`, and both readings sit
in the same file without conflict.

**Why the reconciliation did not flip this, in the reconciler's own words rather than this leg's.**
*"Still BLOCKED, and this leg has no standing to clear it … That is not the same as a clean skeptic
run. Clearing a skeptic finding is a skeptic's job; a reconciler who marked its own work clean would
be committing the exact error `faults.md` §7 diagnoses. The honest next step is item 1 of §8: re-run
the skeptic against the amended tree."* The gate is on **the state of the artifacts as certified**,
not on whether the underlying defects have been repaired — and they have been repaired. **The
distance from here to a clean gate is one leg, and it is not a research leg.**

**Neither round's BLOCKERs touch `F`.** The round-2 skeptic's own words: *"a seam, not a step … Not
one of them is an error inside a proof."* That is why §2–§4 are usable and why the gate is still
shut: those are answers to different questions.

**Why this synthesis is nonetheless usable.** Everything in §2–§4 is kernel-checked (and re-executed
here), independently recomputed, or explicitly flagged with the contested source it rests on.
Nothing here quotes a constant from a broken derivation: `0.004479` appears only as the number that
*survived* its own repair, and `0.99565` only as the theorem §5.1 retires. Nothing here repeats the
mis-scoped P6′ inferences or the false "(gov) ⟹ (min)" chain.

### Citation status — not cleared, not claimed, and not yet attempted

**The citation audit has NOT been run on this corpus. It gates the paper downstream, at
citation-gate, and this document makes no claim of citation clearance.** What exists on disk is a
**round-1**, paper-side audit (`attack/verification-report.md`, molecule `cite-20260725-9eef`)
against `paper/paper.tex`, and it returned **BLOCKED** — two of the paper's 22 citekeys
(`carneiro2019fourier`, `visser2018andrica`) traced to no ledger row. Both have since been added to
`source-ledger.md` §2.8 with a standing re-audit obligation, **which is not the same as audited**.
The downstream editorial gate (`attack/editorial-verdict.md`) consequently returned **REWRITE**.

**The ledger's own state**, read from the file: `axler2014newbounds` at **L0** with the full
three-document fetch record and the edition ⚠, §6 gap 3 marked `CLOSED 2026-07-26`, and a round-3
reconciliation record at the head. The run's load-bearing **unopened or under-opened** sources are
therefore: **card `L6`'s `2⁶⁴` verification height** (L2_weak, unopened, load-bearing in *both*
branches of Theorem C — §4.5), **`granville1995cramer`** (L1 at preprint pagination, load-bearing
for the entire refutation-side argument — §4.2), and `ribenboim`, `oliveira2014goldbach`, `shanks`,
`dusart2018`, `farhadian-jakimczuk`.

**A staleness warning that must travel downstream.** `paper/paper.tex` is a **round-1** artifact. It
states that `axler2014newbounds` is *"not opened … quoted through Kourbatov's proofs"* — true when
written, false now — and it carries round 1's version of every constant §2.3 supersedes, including
`0.99553`, which §5.1 retires. **Any paper-side work must be redone against rounds 2–3, not
patched.**

---

## 7. What a next run should do

**The first item is still not a proof attempt, and after three legs that is the finding.**

| # | Action | Why |
|---|---|---|
| 1 | **Re-run the skeptic against the amended tree. Nothing else first.** Feed it `attack/reconciliation.md` so it audits the five **decisions**, not just the arithmetic. | The only leg with standing to convert "seams closed" into "zero residual BLOCKERs". It is the single action between this corpus and a clean evidence gate, and it is not research. `reconciliation.md` §8 item 1. |
| 2 | **Citation audit on the round-2/3 corpus** — `granville1995cramer` first, card `L6` second | Both are load-bearing and under-opened; Axler is now done; the only audit on disk is round-1, paper-side, and BLOCKED. **No citation clearance exists and none is claimed above.** |
| 3 | **Open `oliveira2014goldbach`** (or find another L0 route to the `2⁶⁴` height) | §4.5 — the largest remaining provenance exposure, sitting under *both* branches of the headline theorem, and larger than any seam round 3 closed |
| 4 | **Rewrite `paper/paper.tex` against rounds 2–3 — do not patch it** | It asserts a tier that is now wrong and constants that are now retired; the citation and editorial gates both already failed on it |
| 5 | Attack the residual window (§4.3) as a short-interval prime-count problem | The one genuinely-open analytic node any round isolated exactly, with the criterion `1 + 2/L` in closed form |
| 6 | Formalize the smooth model (`L4`) in Lean | Still the only node in the formalization plan that is a real theorem within Mathlib's reach, and still not done after three legs |
| 7 | **Do not fund another proof-attempt fan-out, and do not fund more sieving** | Sieving buys the next maximal gap and nothing between; the record that matters is 4.2 decades away. The fan-out is what produced every finding round 3 had to reconcile. |
| 8 | **Amend the loop's write rule.** Rule 6 (*"round K writes only under `attack-round-K/`"*) is incompatible with a reconciliation stage and needs an explicit exemption for it | R2-m5 generalised: the stage that owns seams must be allowed to edit the artifacts that carry them, or it can only publish a fifth opinion |
| 9 | **Add a "read your siblings" step to any fan-out brief** | §5.4: a correct, correctly-labelled finding sat unread in a sibling artifact for a full round while three legs published the wrong side of the dispute it settled. That is the cheapest fix in this table. |

**Standing instruction, unchanged through three legs.** The conjecture is open. Do not write
"Firoozbakht is true". Do not write "Firoozbakht is false". The Cramér–Granville tension is evidence
about which way to bet and nothing more.

---

## 8. Verification of this document

This leg emitted no notebook and no Lean of its own. It did two things the round-2 synthesis could
not, and both are reported at their exit statuses.

### 8.1 The Lean gates — re-executed here, first-hand

The round-2 synthesis and the round-3 reconciliation both reported the kernel status **second-hand**
(no toolchain cache in their worktrees). This leg materialised the cache and ran the gates:

| Command | Exit | Output |
|---|---|---|
| `lake exe cache get` | **0** | — |
| `lake build` | **0** | `Build completed successfully (2208 jobs)`; `Built Firoozbakht.Barrier`; **one** warning: `Firoozbakht/Statement.lean:185:8: declaration uses 'sorry'` — the declared open target |
| `lake env lean audit.lean` | **0** | 33 declarations listed; exactly one (`Firoozbakht.firoozbakht`) depends on `sorryAx`; all others on `[propext, Classical.choice, Quot.sound]` only — including all three `Barrier.lean` theorems |
| `lake env lean audit_exhaustive.lean` | **0** | `declarations scanned: 63` · `depending on sorryAx: [Firoozbakht.firoozbakht]` |
| `grep` for `sorry` in `*.lean` | — | exactly **one live token**, `Firoozbakht/Statement.lean:186`; every other hit is a docstring or comment |
| `grep` for `native_decide` / `axiom` / `implemented_by` / `unsafe` | — | **none outside docstrings** (three hits, all prose in `Equivalence.lean`, `Statement.lean`, `Barrier.lean` describing their own absence) |
| `shasum -a 256 Firoozbakht/Statement.lean` | — | `6528868823c0637dd182c914e2ef43a7455f851335cafaba6cee934802e004c1` — recorded so the next leg can check the fidelity anchor by hash rather than by report |

**Reading, first-hand: the build is green, the axiom surface is clean, and the single `sorry` is the
conjecture itself.** Three legs have now produced these numbers by *execution* — the round-2
lean-probe, the round-2 skeptic, and this one; the two legs in between (the round-2 synthesis and
the round-3 reconciliation) reported them second-hand and said so.

### 8.2 Independent recomputation — `attack/verify_syn3.py`

Every headline figure in this document was recomputed from the *statements* in a fresh script with
no upstream code path open — it does not import or copy `verify_syn.py`, `verify_syn2.py` or
`reconcile_recount.py`. Own sieve of Eratosthenes; `mpmath` at 60 decimal digits; every near-tie
(relative margin `< 10⁻⁹`) re-adjudicated exactly.

**Result: `python3 attack/verify_syn3.py` → exit 0, 40/40 checks pass.** Log at
`attack/verify_syn3.out.txt`.

| Quantity as stated in this document | This leg's independent value | Verdict |
|---|---|---|
| `π(3·10⁶)` | 216 816 | ✓ |
| violations of `F` below `3·10⁶` (gap form, 60-dps escalation) | **0** | ✓ |
| violations of `F`, exact integers `p_{n+1}^n < p_n^{n+1}`, `n ≤ 3000` | **0** | ✓ — two independent formulations, no disagreement |
| steps / decreasing, all `n`, at `3·10⁶` | 216 815 / 121 239 | ✓ — **§5.4** |
| steps / decreasing, `n ≥ 10` | 216 806 / 121 238 | ✓ — **§5.4** |
| near-ties reclassified at 60 dps | **0** — the count is not float-fragile | ✓ |
| the two percentages | `55.920039113…` / `55.918179092…` | ✓ |
| the RH leg's self-consistency argument (`T_11 < T_10`; the `n ≥ 11` cut gives `121 237 / 216 805`) | both confirmed | ✓ — **`121 238 / 216 805` is impossible under any convention** |
| ordinal of gap `248` at `p = 191 912 783` | **28th**; 28 records below `2·10⁸`; `15 683` is 12th; 25 records below `10⁸` | ✓ — R2-m1, third independent confirmation |
| P6′-gov / P6′-min exceptions below `3·10⁶` | 0 / 0 | ✓ |
| P6′-min minimum margin | `+0.4845277` at `n = 1879`, `µ = 1831` | ✓ every digit quoted |
| W1: `p_1823 = 15 641`, `p_1831 = 15 683`, `p_1847 = 15 823`; margin | all three; `+0.0286106048…` | ✓ — **P6′-pair is false** |
| `e^{−0.0017569}` (C-b′, live) | `0.9982446424453653…` | ✓ |
| `e^{−0.0043636}` (C(b\*), retired) / `e^{−0.0516}` (C-a′) | `0.995645906669685…` / `0.949708674346063…` | ✓ |
| `log 6 690 557` / `log 1 772 201` | `15.7162076872…` / `14.3877328348…` | ✓ |
| `log 2⁶⁴`; `L(L−1.1)` at `2⁶⁴`; the published integer | `44.36141955583649…`; `1919.137983497532…`; **1920** | ✓ exact |
| RH critical constant `max_x log x/√x` | `0.7357588823428846…` `= 2/e` at `x = e²` | ✓ |
| barrier: no `2 ≤ n ≤ 20 000` where `2p_n ≤ p_n^{1+1/n}`; `p_n < 2^n` exact to `π(3·10⁶)`; Bertrand ties at `n = 1` | 0 / 0 / confirmed | ✓ — §2.1 |

**Ten of this script's checks failed on its first run, and every one of the ten was the script's
fault, not the corpus's.** Reported rather than smoothed, because a verification pass that only ever
confirms is not a verification pass: (a) four were string-prefix comparisons truncating at the wrong
digit; (b) two were my own transcription of `log 6 690 557` / `log 1 772 201` to one digit more than
the reconciliation prints; (c) three were a mis-specified P6′-min minimum — `µ(n) = n` holds
*exactly at record indices*, where the margin is `0` by definition, so the diagnostic minimum is
taken over `µ(n) < n`, which is what the artifacts measure and what my first draft did not; (d) one
was the **barrier inequality written with its polarity reversed** — certification would need
`2p_n ≤ p_n^{1+1/n}`, and I had tested the barrier itself as the failure condition. Corrected, all
40 pass. No artifact number moved.

### 8.3 The tree, checked rather than inherited

Following the lesson §5.2 records twice over, this leg re-read the tracked tree for every claim it
makes about what round 3 landed, rather than reading `reconciliation.md`'s report of it: the
`axler2014newbounds` ledger row (**L0**, with fetch record and edition ⚠), §6 gap 3 (`CLOSED
2026-07-26`), card `L15` (denominator `216 806`, `50 847 533` **indices**, obligation list carrying
both `P6′-min` and `P6′-gov`, all four predicates tabulated), UVR §3.5 (`RETIRED TO A REMARK`), FFM
§7.4 (the designation notice), and the four round-2 artifacts' reconciliation banners. **All present
as described.** The one drift found: the reconciliation cites the ledger's Axler row at line 412 and
it now sits at line 426 — the row moved under later edits, the tier did not. Recorded in §5.2 as a
third instance of the same species of error, not as a defect.

### 8.4 Not done, and named rather than omitted

This leg did **not** re-run the `10¹¹` sweeps, the red-team corpus (`corpus/verify_corpus.py`), or
FFM's `10⁹`/`2·10⁸` decades — its own sieve reaches `3·10⁶` for the statistic and `2·10⁸` for the
maximal-gap enumeration, and every figure above that range is attributed to the leg that produced
it. It **opened no source**; every PDF-level provenance statement (MD5s, the 14-vs-12-column tables,
the corrigendum text, the edition numbering) rests on the FFM leg's fetch and the round-2 skeptic's
independent re-fetch, which agree, and is second-hand here. It did **not** re-derive R2-m6's or
R2-m7's figures. It ran **no citation audit** and claims no citation clearance. It repaired **no
upstream artifact** — round 3 already did that, and adding a fifth voice is the failure mode this
corpus is documenting.

### 8.5 Consistency against the brief

Each required element is present and locatable: what was proved (§2, with confidence codes and round
markers), what was refuted (§3), what remains open (§4, with the provenance node promoted to §4.5),
the evidence-gate status stated honestly as **BLOCKED** with the failing leg named (§6), an explicit
statement that no citation clearance exists and the audit has not been run (§0, §6), the rounds
trajectory with the shrink-versus-churn question answered plainly rather than dressed up (§1), and a
plain statement of what the reconciliation changed, including the three places where it overturned a
skeptic or a synthesizer (§5). The verdict rests on the final round named by
`reattack-verdict.json` — round 2 — read as amended by round 3.

---

## 9. Sources folded

**Round 3 — the reconciliation leg and the gates read against it.**

| Artifact | Leg | Molecule |
|---|---|---|
| `attack/reconciliation.md` + `attack/reconcile_recount.py` / `.out.txt` | reconcile | `task-20260727-264e` |
| `attack/evidence-verdict.md` (round-3 rewrite) | evidence-gate | `task-20260727-30dc` |
| `attack/re-attack/rounds.md` "Round 3" addendum | reconcile | `task-20260727-264e` |

**Round 2 — the final re-attack round, on which the verdict rests.** Under `attack/re-attack/`,
each now carrying a round-3 reconciliation banner:

| Artifact | Leg | Molecule |
|---|---|---|
| `reattack-verdict.json`, `rounds.md`, `synthesis.md` | re-attack loop | `reattack-20260726-57d1` |
| `attack-round-2/proof-attempt-first-failure-maximality.md` | proof-attempt | `task-20260726-56a7` |
| `attack-round-2/proof-attempt-RH-conditional-bound.md` | proof-attempt | `task-20260726-b335` |
| `attack-round-2/proof-attempt-unconditional-verified-range.md` | proof-attempt | `task-20260726-2035` |
| `attack-round-2/lean-probe-report.md`, `unproved.md` | lean-probe | `task-20260726-8ba0` |
| `attack-round-2/faults.md` + `skeptic-round2-checks/` | skeptic | `task-20260726-7211` |
| `lean/Firoozbakht/Barrier.lean` (new, `sorry`-free) | lean-probe | `task-20260726-8ba0` |
| `attack/synthesis.md` (round-2), which this document supersedes | synthesize | `task-20260726-7d7d` |

**Round 1 — pinned, read, never re-run; cited above only where later rounds left it standing.**
Under `attack/`: `decompose.md`, `frame-deliberation/`, `concept-cards/` (30 cards + INDEX, four
amended in round 3), `source-ledger.md` (amended in rounds 2 and 3), `proof-attempt-{0,1,2}.md`,
`notebook-{0,1,2}/`, `lean-probe-report.md`, `coverage-report.md`, `faults.md`, `claims-ledger.md`.

**Downstream artifacts read for §6's honest reporting, not folded as evidence:**
`attack/verification-report.md` (citation audit, round 1, BLOCKED), `attack/editorial-verdict.md`
(editorial gate, round 1, REWRITE), `paper/paper.tex` (round-1 paper, stale as of round 2).

---

*Artifact of leg `synthesize`, molecule `task-20260727-1d5d`, run `germ-20260725-791a7c45`, **round
3**. Supersedes the round-2 `synthesis.md` in place; the galaxy carries exactly one current answer.
No number in this document was invented; every figure traces to a cited source artifact or to this
leg's own `attack/verify_syn3.py` (40/40, exit 0) and its own execution of the Lean gates (exit
0/0/0, 63 declarations, one `sorryAx`). The conjecture `F` remains **OPEN** — neither proved nor
refuted by any round. The evidence gate is **BLOCKED**, failing leg SKEPTIC. **No citation audit has
been run and no citation clearance is claimed.***
