# Firoozbakht's conjecture — synthesis of the attack

**Molecule:** `task-20260726-7d7d` (leg `synthesize`, crew role: synthesizer) — **ROUND 2**
**Run:** `germ-20260725-791a7c45` · **Re-attack loop:** `reattack-20260726-57d1` (`rounds = 2`)
**Date:** 2026-07-26 · **Formal backend:** Lean 4 / Mathlib
**Conjecture under attack (`F`):**

> `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1` — equivalently, `n ↦ (p_n)^{1/n}` is strictly
> decreasing.

**This document supersedes the round-1 `synthesis.md` of the same name, in place.** The galaxy
carries exactly one current answer, and this is it. Round 1's synthesis (molecule
`task-20260725-cfd7`, 2026-07-25) rested on `rounds_target = 1`, `rounds_run = 0` — the early-exit
path, where round 1 *was* the whole attack. Since then a re-attack loop ran two full rounds and
left `attack/re-attack/reattack-verdict.json` on disk naming **round 2** as the final round. Per
the v4 rounds rule, **the verdict below rests on round 2's artifacts**
(`attack/re-attack/attack-round-2/`), not round 1's. §1 states the trajectory across both rounds,
including the question a single round cannot answer: did the still-unproved list *shrink*, or
merely *churn*?

**What changed versus round 1, in one line each.** Both of round 1's BLOCKERs (F1, F2) are now
**mathematically fixed** — by independent re-derivation, not re-assertion, and confirmed by a
skeptic who recomputed every constant from scratch. Three genuinely new mathematical results
landed (§2.2, §3.1, §2.1). **What did not change:** `F` is still OPEN, the Lean `sorry` count is
still exactly one (the conjecture itself), the evidence gate is still **BLOCKED**, and the loop
never reached its fixpoint. The *reason* the gate is blocked did change — from "unrepaired
mathematical defects" to "unreconciled repairs" — and §1 says plainly why that is a worse signal
than it sounds, not a better one.

---

## 0. The verdict, in one screen

| Question the brief posed | Answer |
|---|---|
| Was `F` **PROVEN**? | **No.** |
| Was `F` **REFUTED**? | **No.** |
| Status of `F` after two rounds | **OPEN**, and every one of the round-2 artifacts says so of itself, at the top, unprompted. |
| Rounds run | **2 of 2** (`rounds_target = 2`, `exit_reason: rounds-exhausted`) |
| Did the still-unproved list shrink? | **No — it was unchanged at one entry, and that entry is `F` itself.** See §1; this is the honest, expected shape, not a failure. |
| Did the BLOCKER set shrink? | **No — it grew, 2 → 3, and changed species.** Round 1's two were math defects and are fixed; round 2's three are cross-artifact seams. §1, §5. |
| Evidence-gate status | **BLOCKED** — failing leg `SKEPTIC` (round 2), three residual BLOCKERs. §6. |
| Citation clearance | **NOT ESTABLISHED, and not claimed.** A round-1 paper-side citation audit exists on disk and itself returned **BLOCKED**; no round-2 citation audit has run at all. §6. |

**The one-sentence result of the whole run.** *Firoozbakht's conjecture was neither proved nor
refuted; what two rounds produced instead is (i) a machine-checked reduction of `F` to the
prime-gap inequality `g_n < T_n`, now joined by a machine-checked proof that the only prime-gap
input Mathlib carries (Bertrand) is **provably insufficient at every `n ≥ 2`**, (ii) an
unconditional, table-driven verification architecture reproducing the published `2⁶⁴` frontier
from first principles, tightened in round 2 from `0.93961·p_{n₀}` to `0.94970·p_{n₀}` on Dusart
alone, (iii) an exhaustive independent sweep to `10¹¹` with no counterexample and no near-miss,
(iv) a five-theorem closure of the Riemann-Hypothesis route *as a route* (four refutations plus a
lower bound on the strength any `RH ⟹ F` proof would have to deliver) — now with the quantifier
round 1 dropped restored — and (v) the outright **refutation of the run's own
most-quoted lemma** (`P6′-pair`), together with a proof that two of the surviving predicates are
formally incomparable — offset by three named, unrepaired cross-artifact seams that hold the gate
shut.*

**What must not be written downstream.** Not "Firoozbakht is true": no proof exists and the
obstruction analysis (§4.1) shows none is near — round 2 strengthened that reading by closing a
route rather than opening one. Not "Firoozbakht is false": the Cramér–Granville tension is a
heuristic, not a test. The defensible sentence, inherited from `decompose` §9 and unweakened by
anything found in either round, is: *Firoozbakht's conjecture is numerically robust over the
verified range and simultaneously incompatible with the standard Cramér–Granville heuristic; at
least one of the two must fail, and no current technique can say which.*

---

## 1. The trajectory — two rounds, what each fixed, and shrink versus churn

**Two rounds ran. The verdict rests on round 2.** `attack/re-attack/reattack-verdict.json`
records `rounds_run = 2`, `rounds_target = 2`, `exit_reason = "rounds-exhausted"`,
`final_round.round = 2`. Round 1 is the spore's original informal + formal branches (read by
round 2, never re-run). Round 2 was nucleated forward by the loop: three proof-attempts (one per
subquestion), one lean-probe run in fork discipline (fed only the unproved list, not blocked by
the attempts), one skeptic blocked by all four. Round 2's artifacts are on disk at
`attack/re-attack/attack-round-2/`.

| round | kernel | skeptic | BLOCKERs | unproved | converged? |
|---|---|---|---|---|---|
| 1 | UNPROVABLE_IN_BUDGET | blockers | **2** (F1, F2) | 1 (`F` itself) | **NO** |
| 2 | UNPROVABLE_IN_BUDGET | blockers | **3** (R2-B1/B2/B3) | 1 (`F` itself) | **NO** |

The loop's stop condition — *kernel PROVED **and** skeptic clean, in the same round* — never held.
`while round < rounds` is now false (`2 < 2`), so no round 3 was nucleated. This is the cap working
as designed, recorded as `rounds-exhausted`, never a silent pass.

### Did the still-unproved list shrink, or churn?

**Neither. It was unchanged: one entry, both rounds, and that entry is `F` itself.**
`unproved-1 = unproved-2 = { Firoozbakht.firoozbakht : Conjecture }`. Nothing regressed; nothing
new became `sorry`'d. Saying this plainly is the point: an attack on an open `Π₁` statement whose
`sorry` count reaches zero would be reporting a fabrication, not a result.

**But the *quality* of the non-shrinkage changed, and that change is real.** Round 1 correctly
*declined* to attempt the conjecture. Round 2 attempted it and failed honestly — `exact?`, `aesop`,
`decide` all fail as expected — and then did something round 1 did not: it **proved a barrier**.
`lean/Firoozbakht/Barrier.lean` now carries three `sorry`-free theorems establishing that
Bertrand's postulate — the only prime-gap bound in Mathlib — has a ceiling that sits strictly
*above* the Firoozbakht threshold at **every** `n ≥ 2`. The route is not "hard"; it is **closed**,
kernel-checked. That is genuine progress on the formal leg even though the `sorry` count is
identical.

### Did the BLOCKER set shrink, or churn?

**It did neither cleanly — it grew, 2 → 3, and changed species. Read honestly, that is the bad
signal, and it is the signal that says more rounds of the same shape will not help.**

- **Round 1's two BLOCKERs are genuinely fixed**, and this is not a self-report: the round-2
  skeptic re-derived every step and every constant from the *statements*, at 40–50 decimal digits,
  and reproduced them to the digit. F1 was fixed by naming (three predicates named in symbols, a
  fourth isolated, every circulating measurement assigned to the predicate it actually measures) —
  and then over-fixed, into a refutation (§3.1). F2 was fixed by re-derivation (the bound restated
  in its tight form, the constant obtained from a proof rather than a numerical sweep).
- **Round 2 introduced three new BLOCKERs of a different kind.** None is a mathematical error.
  None touches `F`. All three are *seams between artifacts that nobody owned*: two legs repaired
  the same fault into two incompatible theorems (R2-B1); two legs assigned the same source
  contradictory bibliographic tiers (R2-B2); one repair rests on a citation that exists only in a
  preprint edition (R2-B3). §5 adjudicates all three.

**The structural reading, which is the useful output of having run two rounds instead of one.**
Round 1's own skeptic named this failure mode and predicted its recurrence — *"a fan-out with no
reconciliation stage … nobody owned the seams."* Round 2 **widened** the fan-out (two proof
attempts now both touching Theorem C(b), where one did before), still supplied no reconciliation
stage, and reproduced the prediction on itself, one round later, on the very artifact meant to fix
it. The loop is not converging on the reconciliation axis; **it is widening.** A third round of
the same shape would very likely be a fourth data point on the same curve.

**So the honest answer to "will more rounds help?" — which round 1 could not give, having only one
measurement — is now: more rounds of *this shape* will not.** What is missing is not more
mathematics. Every mathematical target round 2 was pointed at, it hit. What is missing is a single
**reconciliation leg** (§7), and both the round-2 skeptic (`faults.md` §7) and this synthesis reach
that conclusion independently.

---

## 2. What was PROVED

Confidence codes: **[K]** = machine-checked by the Lean kernel; **[P]** = paper proof, derived
in-run and independently re-derived by the skeptic leg; **[P·s]** = paper proof, skeptic-confirmed,
resting on a source whose ledger status is contested (§5); **[C]** = finite computation, exhaustive
and independently reproduced. Round-2 results are marked **‹r2›**.

### 2.1 The reduction chain, and the barrier — `[K]`

`Conjecture ↔ ConjectureReal ↔ (∀ n ≥ 1, g_n < T_n)`, where `T_n := p_n(p_n^{1/n} − 1)`, is
**machine-checked**. Round 2 re-ran every gate rather than quoting round 1's: `lake build` exit 0
(2208 jobs), `lake env lean audit.lean` and `audit_exhaustive.lean` both exit 0, **63 declarations**
scanned (60 in round 1, `+3`), exactly **one** `sorryAx` dependent — the open target. No `axiom`,
no `native_decide`, no `unsafe`, no `@[implemented_by]` outside docstrings. `Statement.lean` was
verified **byte-identical** (SHA-256 matched before and after), which is what forecloses the
"closed a `sorry` by weakening the statement" failure. The round-2 skeptic **re-executed** these
gates rather than reading them — the only leg in either round it could verify by execution — and
reproduced every exit code and the hash.

**New in round 2 ‹r2› — `lean/Firoozbakht/Barrier.lean`, three `sorry`-free theorems:**

| Theorem | Statement |
|---|---|
| `bertrand_gap` | `p (n+1) ≤ 2 * p n` for `n ≥ 1` — Bertrand, ported to this development's 1-indexed `p` |
| `p_lt_two_pow` | `p n < 2 ^ n` for `n ≥ 2` — induction on `bertrand_gap`, base `p 2 = 3 < 4` |
| `bertrand_ceiling_above_threshold` | `(p n : ℝ) ^ (1 + 1/n) < 2 * (p n : ℝ)` for `n ≥ 2` |

Read the third one in the right direction: for Bertrand to *certify* `F`, its ceiling `2 p_n` would
have to sit **below** the threshold `p_n^{1+1/n}`. It sits strictly **above** it, at every `n ≥ 2`.
The mechanism in one line: Bertrand supplies constant multiplicative slack `2`, while the
threshold's slack `p_n^{1/n} = exp(log p_n / n)` tends to `1`; certification would need
`2^n ≤ p_n`, and `p_n < 2^n` — which is `p_lt_two_pow`, itself proven *from* Bertrand. **The best
available tool proves its own insufficiency.** This is a negative-capability result: it says
nothing about whether `F` is true, and everything about what the substrate can reach.

The checker itself was tested rather than trusted (round 1, unchanged and uncontradicted): 27
adversarial statements, all false or ill-formed, through the same toolchain; 27/27 behaved as
specified, and the one entry **no gate in this run catches** (`V04`, true-but-differently-meant via
ℕ→ℝ coercion) is named rather than omitted. Round 2 additionally re-tested the audit *detector*
against a planted `sorry` in the enlarged tree (scanned 64, two names reported), then deleted the
plant — so the one-entry unproved list is produced by a detector demonstrated to fire.

### 2.2 The first-failure-maximality obligation, restructured — `[P]` ‹r2›

`decompose` §2.4 posed **P6′** and ranked it the attack's most tractable open obligation. Round 1
showed the obligation was misdirected. **Round 2 shows the run had been carrying three different
obligations under one name, refutes the strongest, and proves the remaining two are incomparable.**

The four predicates, named once and for all (`µ(n) := min{m : g_m ≥ g_n}`, `r(n) := ` last record
index `≤ n`):

| Name | Statement | Status after round 2 |
|---|---|---|
| **P6′-pair** | `T_m ≤ T_n` whenever a record index `j` satisfies `m ≤ j < n` | **FALSE** — §3.1 |
| **P6′-gov** | `T_{r(n)} ≤ T_n` for all `n` | open; 0 exceptions swept |
| **P6′-min** | `T_{µ(n)} ≤ T_n` for all `n` | open; 0 exceptions swept |
| **P6′-rec** ‹r2› | `T_j ≤ T_{j′}` for consecutive record indices `j < j′` | open; 0 exceptions in 27–29 record steps |

- **Theorem 2 (FFM)** `[P]` — *if `F` fails first at `n₀`, then **either** `T_{r(n₀)} ≤ T_{n₀}`
  **or** `T_{µ(n₀)} ≤ T_{n₀}` already forces `g_j < g_{n₀}` for every `j < n₀`* — i.e. (M1) holds.
  Both branches are three-line chains, both re-derived by the skeptic. **Two consequences that
  matter more than the theorem:** the pruning never needed the predicate that turned out to be
  false, and **a single instance suffices** — the predicate is consumed only at `n₀`, never as a
  universal statement.
- **Proposition 4 (FFM)** `[P]` — `P6′-gov ⇏ P6′-min` **and** `P6′-min ⇏ P6′-gov`, both by explicit
  four-index counter-models (`g = (2,4,6,3)`). Round 1's fault report had carried the chain
  "(C) ⟹ (A) ⟹ (B), strictly" as though free; **the second link is invalid**, and the missing
  ingredient is P6′-rec, a fourth statement nobody had been measuring under its own name. The
  skeptic calls this "the document's best structural catch" and it is.
- **Lemma M / Theorem B (round 1)** `[P]` / `[P·s]` — the monotone-bar principle and its
  instantiation at Kourbatov's surrogate bar `S(x) = log²x − log x − 1.17` — survive round 2
  unchanged and re-verified (`max{g_j : j ≤ 9} = 6 < S(29) = 6.80139`; `S`-breaches below `2·10⁸`
  are exactly `{1,2,3,4,6,9}`).

**The honest status.** P6′-min is the obligation to work (it is what Theorem 2 needs, and its
margin does not decay), P6′-rec must be listed beside it (Proposition 3 needs it), and card `L15`
must be rewritten — its prose states the predicate that is now false, its measurement row measures a
different one. That rewrite is **named, not applied**, and is part of §7's reconciliation leg.

### 2.3 The unconditional finite-range theorem, tightened — `[P·s]` + `[C]` ‹r2›

`proof-attempt-2` (round 1) reconstructed from first principles the architecture by which the
literature's `2⁶⁴` frontier is certified; round 2 repaired its central bound and tightened its
constants.

- **Lemma A / Corollary A2 / the table-free window** — unchanged from round 1 and re-verified:
  `T_n ≥ L(L−1.1)` for `p_n ≥ 60 184` (Dusart 2010 Thm 6.9 eq. (6.6), **L0**, fetched and read);
  a gap of size `g` can violate `F` only at `p_n ≤ S(g) := exp((1.1 + √(1.21+4g))/2)`, converting
  the whole verification into a first-occurrence gap-table lookup; and the window
  `396 738 ≤ p_n ≤ 777 600` where `F` follows from unconditional analytic estimates with **no
  enumeration of primes at all**, together with a proof that the window **closes permanently** at
  `p ≈ 7.776·10⁵` (root `777 600.744…`, re-verified by the skeptic).
- **Independent reproduction of the published `1920`** `[C]` — `L(L−1.1)` at `2⁶⁴` is
  `1919.1379834975…`, so a gap of at least 1920 is needed to violate `F` just below `2⁶⁴`. The
  published integer falls out with no tuning. The caveat that makes this honest stands: Lemma A
  gives the *local* statement at the frontier, and the published endnote's phrasing is *global*.
- **F2 repaired ‹r2›** — the round-1 bound `(A-high)` `T_n ≤ (ℓ²−ℓ−1−1/ℓ)(1 + ℓ⁴/x)` did not follow
  from its stated justification and was false by a factor `≈ 38.8` over part of its range. Both
  round-2 legs restated it in the tight form `T_n < v(1 + v/x)` with `v := ℓ²−ℓ−1−1/ℓ`, proved from
  the elementary primitive rather than by weakening, and **replaced the numerical sweep by a
  proof** (Proposition R1: `E(ℓ) = v²e^{−ℓ}` is decreasing; the majorant `φ` is decreasing; hence
  `d*(ℓ) ≤ d*(ℓ₁) = 0.004363568`). The round-1 conclusion survives — the printed `0.004479` *is*
  sufficient — but for a reason the printed derivation did not supply.
- **Theorem C, round-2 form ‹r2›.** *If `F` first fails at `n₀`, then `g_{n₀}` exceeds every gap
  between primes below a definite multiple of `p_{n₀}`:*

| branch | round 1 | **round 2** | source |
|---|---|---|---|
| Dusart only | `d ≥ 0.0623` → `p_m ≤ 0.93961·p_{n₀}` | **`d ≥ 0.0516` → `p_m ≤ 0.94970·p_{n₀}`** | `dusart2010estimates`, **L0** both rounds |
| with Axler | `d ≥ 0.004479` → `p_m ≤ 0.99553·p_{n₀}`, from a lemma that did not support it | **`d ≥ 0.0017569` → `p_m ≤ 0.998244·p_{n₀}`** (Theorem C-b′) | `axler2014newbounds`, tier **contested** — §5.2 |

  The Dusart branch improves only because the small-branch cutoff rises from `60 184` to `10⁸`
  (licensed by `g_m ≤ 220 < 1919`); it **cannot** improve much further — `d*(ℓ) → 0.05`, so the
  Dusart-only sliver is pinned near `5 %` at every scale. The residual sliver on the Axler branch
  has relative width `0.176 %` at `2⁶⁴`.

  **Round 2 shipped this repair twice, into two incompatible theorems** (Theorem C-b′ at
  `0.998244` and Theorem C(b\*) at `0.99565`), off two different Axler table rows, with neither leg
  citing the other. Both are independently verified correct. That collision is BLOCKER R2-B1;
  §5.1 adjudicates it and designates **Theorem C-b′** as the one to carry forward.

### 2.4 The RH route is closed — as a route — `[P]`, with round 2's quantifier repair ‹r2›

Five theorems, all re-derived by both rounds' skeptics:

| Claim | Verdict |
|---|---|
| The sharpest published RH-conditional gap bound `g_n ≤ (22/25)√p_n·log p_n` (CMS, hypothesis `p_n > 3`) certifies `F` cofinitely | **REFUTED** — it certifies `F` **at exactly one index in the range where the bound is available (`n ≥ 3`), namely `n = 3`** (Thm A) |
| *Some* bound `g_n ≤ C·p_n^θ(log p_n)^A` with `θ > 0` implies `F` beyond finitely many `n` | **REFUTED** (Thm B) |
| *Some* envelope `C√p log p`, any `C > 0`, implies `F` beyond finitely many `n` | **REFUTED** (Thm C) — the **critical constant is `2/e = 0.7357588823…`**, published constants sit above it, and constants below it clear the `L²` bar only on a bounded initial segment `[x⁻(C), x⁺(C)]` given in closed form by the two real Lambert-`W` branches |
| Cramér's `limsup ≤ 1` entails `F` over integer sequences | **REFUTED** by explicit counter-model (Thm E) |
| `RH ⟹ F` as a material implication | **UNDECIDED**, and the leg does not pretend otherwise (Thm D) |

**The round-2 repair, stated because it is a correction and not a restatement ‹r2›.** Round 1's
headline read *"and at no other index whatsoever"*, and that is **false as stated**: the CMS
envelope also sits below the threshold at `n = 1` and `n = 2`. What excludes those two indices is
**the source's hypothesis `p_n > 3`, not the arithmetic**. Round 2 proves the two statements
separately — the *arithmetic clearance* set is `A = {1,2,3}` (Theorem A°), the *certified* set is
`S = A ∩ [3,∞) = {3}` (Theorem A) — and this dissolves a silent cross-artifact contradiction with
`notebook-1`, which reported `p*(22/25) = 5`, i.e. three certified primes `{2,3,5}`. Both artifacts
were numerically right; the words were not. They now cite each other, reconciled through a single
object, the per-index critical constant `C_n := T_n/(√p_n·L_n)`, of which both are level sets.
**This is the one place in either round where a "seam" was closed by the legs themselves rather
than deferred.**

**Theorem D** bounds below the *strength* of any proof of `RH ⟹ F`: composed with Kourbatov's
unconditional necessary condition, such a proof would immediately yield an RH-conditional
Cramér-scale gap bound — stronger than the best published RH-conditional bound by a factor
`8.72·10⁷` at `2⁶⁴` and **unbounded** thereafter. This is a distance between two *statements*, not
a difficulty ordering between two open *problems*, and the leg says so explicitly (card `L11`).

### 2.5 The smooth model — `[P]`

`decompose` §3.6: the smooth surrogate `(x log x)^{1/x}` is strictly decreasing on `x ≥ 5`. **The
smooth model of Firoozbakht is true and elementary**, and the entire difficulty localizes to the
fluctuation of `p_n` around `n log n`. Still not formalized in Lean after two rounds — both
lean-probe legs name this as a non-delivery, and it remains §7's highest-leverage formalization
target.

### 2.6 Computational corroboration — `[C]`

Round 1: two independent legs, independent code paths, exhaustive to **`10¹¹`** — 4 118 054 812
consecutive prime pairs; **0** violations of `F`; max `ρ_n = g_n/T_n` (`n ≥ 10`) = **0.8318** at
`p_n = 25 056 082 087`; 40 maximal-gap records; sieve validated against `π(10⁹)`, `π(10¹¹)`.

Round 2 ‹r2› added two further independent sweeps, written from statements rather than from any
round-1 code path: FFM's to `10⁹` (`50 847 533` indices) and the skeptic's own to `2·10⁸`
(`11 078 936` indices). Both reproduce round 1's headline statistics to every digit quoted, and
both return **0** exceptions for P6′-gov, P6′-min, P6′-rec and `T_{µ(n)} ≤ T_{r(n)}`. The skeptic
is explicit that FFM's `10⁹` decade is one beyond its own sieve and is **not** independently
confirmed — and that nothing in its report depends on that decade. That is the discipline worth
carrying.

The verification discipline itself, unchanged and reaffirmed by round 2: the escalation path
**raises** rather than returns when a margin lands inside its error budget, because *the silent
failure is in the verification direction*. Round 2 applied it with the sign flipped, in the one
place it mattered: FFM's refutation of P6′-pair is the outcome that is *bad news for the run*, so
its witnesses were recomputed at 60 digits even though they stand `10⁸`–`10¹²` ulps clear.

---

## 3. What was REFUTED

Nothing about `F`. Everything below refutes a *claim about the evidence* or a *route* — and that
distinction is the whole discipline of this run.

### 3.1 `P6′-pair` is false ‹r2› — the run's own most-quoted lemma, refuted

> **Theorem 1 (FFM).** There exist `m < j < n` with `j` a record index and `T_m > T_n`. Hence
> **P6′-pair is false**, already on `[1, 1847]`.

Two exhibited witnesses, both recomputed at 60 decimal digits and both independently reproduced by
the skeptic:

| | `m` | `j` (record) | `n` | margin `T_m − T_n` |
|---|---|---|---|---|
| **W1** | 1823 (`p = 15 641`) | 1831 (`p = 15 683`, `g = 44`) | 1847 (`p = 15 823`) | `+0.0286106049` — `2·10¹²` ulps |
| **W2** | 10 655 449 (`p = 191 912 639`) | 10 655 462 (`p = 191 912 783`, `g = 248`) | 10 655 590 (`p = 191 915 033`) | `+3.5792097·10⁻⁵` — `6.3·10⁸` ulps |

Exception census below `10⁹`: **17 exception *indices***, in exactly two clusters, both sitting a
few indices *after* a maximal gap. FFM calls this a "complete census of admissible **pairs**";
the skeptic's R2-m2 is right that it counts indices, not pairs, so the census is complete as a list
of `n` and is *not* a pair count — a labelling defect, not an arithmetic one, and it does not touch
the refutation, which needs one witness. Card `L15` currently marks this claim *"OPEN …
empirically unviolated by every measurement that bears on it"*; that is now false as stated — **the
measurement that bears on the prose had never been run**, and it violates it 17 times below `10⁹`.

**The refutation costs the run nothing**, and saying why is the point: by Theorem 2 the pruning
route consumes either of the two weaker predicates, and both survive. A strong-looking lemma was
being carried, unmeasured, for a job it was never needed for.

### 3.2 The implication chain "(gov) ⟹ (min)" is false ‹r2›

Proposition 4 (§2.2). The two surviving predicates are formally **incomparable** — the run had been
treating one as free from the other for two rounds. This is the same species of finding as
`notebook-0`'s R1: the separation is *structural*, visible without any arithmetic input, and it
means any proof of `P6′-gov ⟹ P6′-min` must consume a property of the primes.

### 3.3 The RH route — five theorems, §2.4.

### 3.4 Bertrand is not merely useless, it is provably closed ‹r2› — `[K]`

Round 1 recorded "Bertrand's postulate is useless here (it implies `F` only at `n = 1`)" as an
observation. Round 2 turned it into a kernel-checked theorem at every `n ≥ 2` (§2.1). The
difference matters for anyone tempted to formalize a sharper version: there is no sharper version
of Bertrand that helps, because the shortfall is a whole scale, not a constant.

### 3.5 The remaining round-1 refutations, unchanged and uncontradicted by round 2

1. **First-failure maximality does not follow from the definitions.** `notebook-0` exhibits an
   explicit increasing integer sequence whose first Firoozbakht failure is at a **non-record** gap,
   in exact integer arithmetic. Consequence: *any proof of FFM that does not consume an arithmetic
   density input is wrong.* The counter-model is excluded unconditionally by Montgomery–Vaughan, by
   a factor that **grows** with scale (1.41 at `10³`, 9.13 at `10¹⁸`).
2. **The two-sided π-bound route to P6′ cannot work.** Past `≈10¹⁰` it is unsatisfiable at *any*
   gap size; no sharpening of constants rescues it.
3. **The `0.9999984` "near-miss" is an artefact.** In a synthetic universe where every gap is `2`
   the same statistic reads `0.99999991` while `ρ` is `0.059`. The statistic measures `1/n`. Only
   `ρ` is diagnostic.
4. **"The tightest cases sit at record gaps" does not survive the range.** A `best[:6]` print
   truncation. At `10¹¹`: 22 of the top 40, and the 4th-tightest case in four billion pairs is not
   at a record index.
5. **More sieve is not more evidence.** Two decades of extra sieving produced no new near-miss; the
   record `ρ` moved exactly once and moved *at the next maximal gap*. The record that would matter
   (`ρ ≈ 0.948` at `p ≈ 1.693·10¹⁵`) is **4.2 decades** above anything either round reached.
6. **Littlewood oscillation is irrelevant** to the threshold (`O(L²·log log log x/√x) → 0`).

---

## 4. What remains OPEN

### 4.1 `F` itself — and why it is not close

The load-bearing obstruction, unchanged by two rounds and *reinforced* by round 2: **any proof of
`F` yields `g_n = O(log² p_n)` unconditionally.** The best known unconditional gap bound is
`g_n ≪ p_n^{0.525}`; under RH it improves only to `≈ √p_n log p_n`. Both are *powers* of `p_n`;
`F` needs *polylogarithmic*. That is square-root scale versus log scale, and no known method
bridges it even conditionally on RH.

Round 2 sharpened this in three independent places, which is worth recording because they were
produced by three legs that were not talking to each other:

- **Formally** — the only prime-gap input Mathlib carries is proven insufficient at every index
  (§2.1, `[K]`).
- **Analytically** — every envelope `C·p^θ(log p)^A` with `θ > 0` fails beyond finitely many `n`,
  because the bar sits at `θ = 0`; and any hypothesis sufficient for `F` must itself deliver the
  full `log²`-scale uniform bound with leading constant `1` and the second-order term `−L−1`
  pinned, while a hypothesis only `0.17` stronger than that bound already suffices — **the band
  left for a candidate gap bound has width `0.17`** (Theorem D.2, with its own "what this does not
  say" attached).
- **Numerically** — the crossover table: BHP's slack overtakes what is needed from `n = 245` on,
  RH's from `n = 3` on. Both are insufficient exactly where it matters.

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
which. `granville1995cramer` sits at tier **L1** — fetched and read, but at preprint pagination;
every locator must be re-expressed against the journal copy before publication. Round 2 did not
touch this row.

### 4.3 The residual analytic window

Theorem C proves first-failure maximality against all primes below `0.94970·p_{n₀}` on Dusart alone
(round 2's improved constant), tightening to a `0.176 %` sliver under Axler. **Inside that sliver
the sandwich is useless by construction**, and the obstruction is exact and named: one needs an
**upper** bound on `π(p_m + y) − π(p_m)` within a factor `1 + 2/L` of the truth, where
Brun–Titchmarsh gives only a factor `2`. `notebook-0` reaches the same wall computationally and
prices it: typical windows are settled unconditionally by Brun–Titchmarsh at **99.861 %** of
governed indices, but the extremal configuration needs a short-interval count sharp to
`1 + 2.2/log p` — **Cramér strength** — and that gap *widens* with scale even as empirical coverage
improves. A pruning rule is worth its worst case.

This remains, in both rounds' judgement and this synthesis's, the most tractable genuinely-open
analytic node the run produced — and it is an open problem in analytic number theory, not a lookup.

### 4.4 Lean, honestly

Not formalized after two rounds: the smooth model (`L4`), the `limsup` corollary (needs effective
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

---

## 5. Reconciliation — the seams, and this leg's adjudication of them

Both rounds' skeptics reach the same structural reading: this corpus does **not** fail the way
math-attack corpora usually fail. No assumed conclusion, no circular reasoning, no sieve-to-`10⁷`
result dressed as a theorem, no pruned search laundered into a verification height — all four were
hunted in both rounds and came back clean, and the round-2 skeptic adds twenty further independently
recomputed items that survive, including "does any round-2 artifact assume `F`?" — **no**, all four
state it OPEN at the top and none uses it as a hypothesis. It fails at the **seams**.

Reconciling is this leg's job. Below, each live seam is adjudicated. **A caveat that governs the
whole section: reconciling in *this* document does not repair the *upstream* documents.** Every
adjudication below is a statement about what a downstream reader should carry, and each names what
still has to be edited where.

### 5.1 R2-B1 — two incompatible repairs of the same theorem. **Adjudicated: keep Theorem C-b′.**

`proof-attempt-unconditional-verified-range.md` and `proof-attempt-first-failure-maximality.md`
both repaired round-1's F2, correctly, independently, and into two different theorems:

| | Theorem C(b\*) (UVR) | Theorem C-b′ (FFM) |
|---|---|---|
| constant | `d ≥ 0.0043636` | `d ≥ 0.0017569` |
| headline | `p_m ≤ 0.99565·p_{n₀}` | `p_m ≤ 0.998244·p_{n₀}` |
| Axler row | `(1,0,0,0)`, `x₀ = 1 772 201` | `(2.1,0,0,0)`, `x₀ = 6 690 557` |
| edition | ⚠ **arXiv preprint only** | **present in both editions** |
| tier claimed for the source | L2_strong, NOT OPENED | L0, opened |

Both are verified mathematically correct by the round-2 skeptic at 40–50 digits. The corpus has no
rule for choosing. **This synthesis designates Theorem C-b′ as the one to carry forward**, on the
ground that decides it cleanly and is not a matter of taste: **its Axler row is present in both
editions of the source**, so it is not exposed to R2-B3. C(b\*) should be retired to a remark —
where it remains useful, because it is the sharper statement of *what round 1's printed lemma would
have ordered* and is the cleanest proof that round 1's conclusion survived its own broken
derivation. This adjudication agrees with the round-2 skeptic's own recommendation, reached
independently. **Neither document has been edited; both still stand as written.**

### 5.2 R2-B2 — contradictory tiers for `axler2014newbounds`. **Narrowed, not cleared.**

The BLOCKER has two limbs and they now have different statuses. This leg checked the tracked tree
directly rather than reading either report.

- **Limb 1 — the ledger amendment "was never made" — is STALE as of this synthesis, and the
  staleness is provable to the line number.** The round-2 skeptic reported that
  `source-ledger.md:406` and `concept-cards/T1-effective-pi-bounds.md:15` "still read the old
  tier." In the committed tree today, `source-ledger.md:**407**` reads **tier L0** *(promoted from
  L2_strong on 2026-07-26 by `task-20260726-56a7`)*, and card `T1` carries the same promotion plus
  an explicit ⚠ flag on the preprint-only row. Both landed in commit `61689d0` (2026-07-26 19:22),
  merged at `4526b27` (19:26). **The two line numbers the skeptic cites resolve exactly, and only,
  in the pre-merge tree** — this leg checked with `git show`: at `61689d0^`,
  `source-ledger.md:406` is `` **`axler2014newbounds`** — tier **L2_strong** `` and
  `T1-effective-pi-bounds.md:15` is `` `axler2014newbounds` (**L2_strong, NOT OPENED**) ``; after
  the amendment the ledger row moved to line 407. The skeptic read a worktree branched before the
  merge. **The finding is an artifact of parallel fan-out, not a defect in the tree** — which is
  precisely the class of error a reconciliation leg exists to catch, and for once it cuts in the
  corpus's favour.
- **Limb 2 — the two legs contradict each other — STANDS.** UVR's document still labels
  `axler2014newbounds` **L2_strong, NOT OPENED** at every use, and attaches to Theorem C(b\*) the
  instruction that it *"must never be quoted inside a sentence containing the word
  unconditional."* That instruction is now over-strict on *tier* grounds (the source was opened)
  and exactly right on *row* grounds (its row is preprint-only). The document has not been amended
  and a reader of it alone gets the wrong tier.

**Net: the BLOCKER is narrowed to one limb and is not cleared.** This synthesis does not and cannot
clear it — only a re-run skeptic leg can, and none is funded by this loop. §6 records the gate as
BLOCKED accordingly.

### 5.3 R2-B3 — an edition-fragile citation. **Confirmed, and half-flagged.**

The Axler row `(1,0,0,0)/x₀ = 1 772 201` exists **only** in arXiv:1409.1780v3 and is absent from the
published *Integers* **16** (2016) #A22 (verified by the skeptic via byte-level PDF fetch, MD5s
pinned; the FFM leg fetched the same three documents independently and reports the same MD5s). A
second, related provenance defect surfaced in the same fetch: **the corollary numbering differs by
one between editions** — arXiv Cor. 3.5/3.6 are *Integers* Cor. 3.4/3.5 — while the 2018
corrigendum (which moves a validity range from `x ≥ 5.43` to `x ≥ 2 634 800 823`, a shift of nine
orders of magnitude) targets the **published** numbering. Both editions point at the same
inequality, so **no mathematical error propagated**; the locator as written matches no single
edition.

**Status of the flag, checked in the tree:** card `T1` **does** carry the ⚠ (*"present in the arXiv
preprint only … Do not quote `x ≥ 1772201` against the journal citation"*) and gives both editions'
numbering. The artifact that *depends* on the fragile row — UVR's Theorem C(b\*) — does **not**
carry it. So the corpus flags the hazard in the card and not in the place that consumes it.
§5.1's adjudication resolves the exposure by retiring the dependent theorem; the flag still has to
be written into the document if it is kept.

### 5.4 R2-M1 — the `55.92 %` statistic. **Adjudicated, with a third independent recount.**

This is the one seam where three independent recomputations now exist, and they agree — against the
document that declared the dispute settled.

| convention, at `3·10⁶` | round-1 synthesis (`verify_syn.py`) | round-2 skeptic (`chk_*.py`) | **this leg (`verify_syn2.py`)** | FFM §4 |
|---|---|---|---|---|
| steps, all `n` | 216 815 | 216 815 | **216 815** | 216 814 |
| steps, `n ≥ 10` | 216 806 | 216 806 | **216 806** | 216 805 |
| decreasing, all `n` | 121 239 | 121 239 | **121 239** | 121 239 |
| decreasing, `n ≥ 10` | 121 238 | 121 238 | **121 238** | 121 238 |

Every **numerator** agrees everywhere, in every document, in every round. FFM §4's **denominators
are each exactly one lower**, at every range and under both conventions — consistent with a
`T`-array truncated to the *gap*-array length before differencing, which is an implementation
artefact, not a counting convention. FFM's sibling leg corroborates the larger number from inside
round 2 (`proof-attempt-RH-conditional-bound.md` §10 states `216 815 consecutive pairs`).

**The adjudication, stated plainly because it reverses two skeptic verdicts:**
`proof-attempt-0.md`'s `121 238 / 216 806` — called an off-by-one by round 1's F5 and re-affirmed
as wrong by round 2's FFM §4 — **is the correct `n ≥ 10` count**. Round 1 was wrong about it;
round 2 confirmed the wrong answer more emphatically. The round-2 skeptic caught this against its
own predecessor, and this leg's third independent recount confirms the skeptic. Carry
**`121 238 / 216 806 = 55.9200 %` (`n ≥ 10`)** and **`121 239 / 216 815 = 55.9182 %` (all `n`)**.

Two riders that travel with the figure: it is **range-dependent** (`57.88 %` at `10⁹`) and must
never be quoted without its bound; and it remains **uninformative about P6′** in any of its
readings.

### 5.5 R2-M2 and R2-M3 — the two live MAJORs inside the repairs

- **R2-M2.** FFM's Theorem C-a′ is headed *"no source outside `dusart2010estimates`, L0"* and quoted
  as *"unconditionally"*, while its own proof consumes card **L6** (`p_{n₀} > 2⁶⁴`, tier L2_weak,
  unopened) and this leg's own `10⁸` gap sieve. **This is round-1 F3's exact pattern — an
  "unconditional" label resting on an unopened source — reappearing in the one branch round 1 had
  passed clean.** The theorem is correct; the label is not. The honest form is: *unconditional
  given the published `2⁶⁴` verification height and a finite in-run gap computation*, both of which
  are named inputs, neither of which is an analytic hypothesis.
- **R2-M3.** FFM's prose calls P6′-min *"the weakest of the three"* and *"the easier obligation"*
  and drops P6′-gov from card `L15`'s obligation list — on the strength of an ordering **its own
  Proposition 4 disproves** (§3.2). The correct statement: P6′-min is the one Theorem 2 needs and
  the one whose margin does not decay; **it is not weaker than P6′-gov, it is incomparable to it**;
  and P6′-rec must be listed alongside because Proposition 3 needs it.

### 5.6 One new defect, found by this leg's own recomputation

Reported because the discipline requires it, and flagged as trivial because it is. FFM §7.4 prints
`e^{−0.0017569} = 0.99824467…`. The true value is `0.9982446424…` — the printed expansion's last
digit is wrong by `2.8·10⁻⁸`. The round-2 skeptic independently reports `0.9982446424` in its own
verification table and did not flag the discrepancy with the document it was checking. **Nothing
depends on it**: Theorem C-b′'s headline `p_m ≤ 0.998244·p_{n₀}` is stated to six places and is
correct, and the constant `0.0017569` from which it derives is itself verified correct. It is a
transcription slip in one displayed expansion, and it belongs on §7's reconciliation checklist,
not in anyone's assessment of the mathematics.

### 5.7 Seams round 2 closed by itself

Recorded so the picture is not one-sided. **The CMS quantifier** (round-1 F4) — closed properly:
the two artifacts now cite each other through the per-index critical constant (§2.4). **The `p*(C)`
definition** — `notebook-1`'s mistyped lower endpoint (`10 ≤ p` should be `2 ≤ p`) is read with the
corrected endpoint by the RH leg, which states that it is doing so and reproduces the table
exactly; **`notebook-1` itself is still unamended**. **The float64 noise-floor alarm** —
`notebook-2`'s warning is correct about **P6′-gov** and does not apply to **P6′-min**, which stands
`2.1·10¹²` ulps clear at the published frontier; the inference *"the route must therefore be the
analytic one"* does not survive the rescoping. **The `T_{m(n)} ≤ T_n` row printed reversed** in
`proof-attempt-0.md` §9 — corrected.

---

## 6. Evidence gate — status stated honestly

### **BLOCKED.** Failing leg: **SKEPTIC (round 2).**

Source: `attack/evidence-verdict.md` (molecule `task-20260726-a94b`, itself a round-2 rewrite
superseding its round-1 predecessor). This synthesis reports that verdict; it does not overturn it,
and it has no standing to.

| Leg | Round 1 | **Round 2 (live)** | Basis |
|---|---|---|---|
| LOOP (round resolution) | round 1 was the whole attack | **resolved: round 2** | `reattack-verdict.json` present, well-formed, `rounds_run = 2` |
| KERNEL | PASS | **PASS** | `lake build` exit 0; exhaustive audit over **63** declarations finds exactly one `sorryAx` — the declared open target; gates re-executed by the skeptic, not read |
| SKEPTIC | FAIL — 2 BLOCKERs | **FAIL — 3 BLOCKERs** | R2-B1, R2-B2, R2-B3; repairs named in the document and explicitly **not applied** |
| CORPUS | PASS | **PASS** | 27/27 adversarial entries behaved as specified; 109/109 verification checks green; non-coverage stated rather than omitted; unchanged in round 2 and uncontradicted by it |

The backend is `lean`, not `none`, so the DEGRADED carve-out does not apply and the kernel leg
passes outright. One failing applicable leg blocks, regardless of the other three. **`PASS` on the
kernel leg is not the claim `PROVED`** — the kernel verdict is `UNPROVABLE_IN_BUDGET`, and both
readings are recorded in the same file without conflict.

**What this synthesis adds to the gate reading, and what it does not.** §5.2 establishes that one
limb of R2-B2 (the "unlanded ledger amendment") is stale — the amendment is in the committed tree.
That **narrows** the BLOCKER; it does not clear it, because the second limb (two legs publishing
contradictory tiers, UVR unamended) stands, and because clearing a skeptic finding is a skeptic
leg's job, not a synthesizer's. **The gate stays BLOCKED and this document is a synthesis of a
blocked corpus, honestly labelled — not a seal.** A `write-paper` leg must treat it as such.

**Neither round's BLOCKERs touch `F`.** The round-2 skeptic's own words: *"a seam, not a step" …
"Neither BLOCKER, and none of the MAJORs, touches `F`. `F` remains OPEN."* That does not clear the
gate — the gate is on the state of the artifacts.

**Why this synthesis is nonetheless usable.** Everything in §2–§4 is kernel-checked, independently
recomputed by a skeptic leg, or explicitly flagged with the contested source it rests on. Nothing
here quotes a constant from a broken derivation: the round-1 figure `0.004479` appears only as the
number that *survived* its own repair, and `0.99565` appears only as the theorem §5.1 retires.
Nothing here repeats the mis-scoped P6′ inferences or the false "(gov) ⟹ (min)" chain.

### Citation status — not cleared, and not claimed

**No citation audit has been run on the round-2 corpus.** What exists on disk is a **round-1**,
paper-side audit (`attack/verification-report.md`, molecule `cite-20260725-9eef`) against
`paper/paper.tex`, and it returned **BLOCKED** — two of the paper's 22 citekeys
(`carneiro2019fourier`, `visser2018andrica`) trace to no row in the source ledger. The downstream
editorial gate (`attack/editorial-verdict.md`) consequently returned **REWRITE**. So: no clearance
exists, none is claimed here, and the one audit that did run failed.

**The ledger's own state, after round 2's bounded refresh:** 20 rows; `axler2014newbounds` promoted
**L2_strong → L0** (three documents fetched, MD5-pinned, read at the locator), leaving the
run's load-bearing unopened sources as `granville1995cramer` (L1, preprint pagination — the
load-bearing citation of the entire refutation-side argument, **audit priority 1** now that Axler is
open), card `L6`'s `2⁶⁴` verification height (**L2_weak, unopened** — and load-bearing in Theorem
C-a′ and Theorem C(b\*), per R2-M2), and `ribenboim`, `oliveira-e-silva-herzog-pardi`, `shanks`,
`dusart2018`, `farhadian-jakimczuk`.

**A staleness warning that must travel downstream.** `paper/paper.tex` is a **round-1** artifact.
It states that `axler2014newbounds` is *"not opened … quoted through Kourbatov's proofs"* — true
when written, false now — and it carries round 1's version of every constant §2.3 tightened. Any
paper-side work must be redone against round 2, not patched.

---

## 7. What a next run should do

**The first item is not a proof attempt, and that is the finding of having run two rounds.**

| # | Action | Why |
|---|---|---|
| 1 | **A single reconciliation leg — not another fan-out.** Its whole job list: adopt §5.1's designation (keep Theorem C-b′, retire C(b\*) to a remark); amend UVR's tier labels to L0 and write the edition ⚠ into any document that keeps a preprint-only row; rewrite card `L15` per §2.2 (P6′-pair FALSE, P6′-min + P6′-rec as the obligations, measurement row relabelled P6′-gov); correct FFM §4's denominators to §5.4's; strike the "unconditional" label on Theorem C-a′ (R2-M2) and the "weakest of the three" prose (R2-M3); amend `notebook-1`'s `p*(C)` endpoint; fix FFM §7.4's printed expansion of `e^{−0.0017569}` (§5.6); relabel FFM's P6′-pair "census of pairs" as a census of indices (R2-m2); make the four round-2 artifacts cite each other. Then re-run the skeptic. | This is the only path to a clean gate. **None of it is research.** All of it is what a `write-paper` leg would otherwise have to guess at. Both the round-2 skeptic and this synthesis reach this conclusion independently. |
| 2 | Run a citation audit on the **round-2** corpus, Granville first, card `L6` second | Axler is now open; Granville is the load-bearing citation of the refutation-side argument and sits at preprint pagination; `L6` is load-bearing in two theorems and unopened (R2-M2) |
| 3 | Rewrite `paper/paper.tex` **against round 2**, not patch it | It is a round-1 artifact stating a tier that is now wrong and constants that are now superseded; the existing citation and editorial gates both failed on it |
| 4 | Attack the residual window (§4.3) as a short-interval prime-count problem | The one genuinely-open analytic node either round isolated exactly; the criterion is `1 + 2/L`, stated in closed form |
| 5 | Formalize the smooth model (`L4`) in Lean | Still the only node in the formalization plan that is a genuine theorem rather than a definition or a finite check, and still fully within Mathlib's reach after two rounds of not being done |
| 6 | Prove `P6′-rec`, or measure it as a first-class obligation | Proposition 3 needs it and nobody had been measuring it under its own name until round 2 |
| 7 | Do **not** fund more sieving; do **not** fund another proof-attempt fan-out | §3.5 item 5: sieving buys the next maximal gap and nothing in between, and the record that matters is 4.2 decades away. §1: the fan-out is widening the reconciliation debt, not closing it. |

**Standing instruction, carried forward unchanged through both rounds.** The conjecture is open. Do
not write "Firoozbakht is true". Do not write "Firoozbakht is false". The Cramér–Granville tension
is evidence about which way to bet and nothing more.

---

## 8. Verification of this document

This leg emitted no notebook and no Lean, so there is **no build of its own to report**. It did not
re-run `lake build` — the toolchain cache is not materialized in this worktree — and it therefore
reports the kernel gates at the exit statuses round 2's own legs recorded, noting that the round-2
skeptic **re-executed** them independently (`lake exe cache get` 0, `lake build` 0 / 2208 jobs /
`Built Firoozbakht.Barrier`, `audit_exhaustive` 0, 63 scanned, one `sorryAx`) rather than merely
reading them. That is the strongest attestation available for those numbers and it is second-hand
here; it is labelled as such.

**Independent recomputation.** Every headline figure this document states was recomputed from the
*statements* in a fresh script — `attack/verify_syn2.py`, own sieve, `mpmath` at 60 decimal digits,
no upstream code path — covering: the three-fractions denominators (§5.4), `F` over the swept
range, FFM's witness W1 (§3.1), the four predicates and their margins, Proposition 4's two
counter-models (§3.2), both repaired Theorem C constants and the round-1 factor-38 defect (§2.3),
the `2⁶⁴` frontier constants, the RH leg's critical constant `2/e` (§2.4), and the barrier
inequality `p_n^{1+1/n} < 2 p_n` (§2.1).

**Result: `python3 attack/verify_syn2.py` → exit 0, 30/30 checks pass.** Full log at
`attack/verify_syn2.out.txt`.

| Quantity as stated in this document | This leg's independent value | Verdict |
|---|---|---|
| `π(3·10⁶)` | 216 816 | ✓ |
| steps / decreasing steps at `3·10⁶`, both conventions | 216 815 / 121 239 (all `n`); 216 806 / 121 238 (`n ≥ 10`) | ✓ — **§5.4's adjudication** |
| `55.92 %` (`n ≥ 10`) and `55.9182 %` (all `n`) | `55.92003911…` / `55.91817909…` | ✓ |
| violations of `F` below `3·10⁶` | **0** (gap form), **0** (exact integers, `n ≤ 3000`), **0 disagreements** between the two | ✓ |
| W1: `p_1823 = 15 641`, `p_1831 = 15 683` (`g = 44`), `p_1847 = 15 823` | all three, and `T_1823 = 83.08071671926980…`, `T_1847 = 83.05210611441398…` — every digit FFM quotes | ✓ |
| W1 margin `T_m − T_n` | `+0.02861060485582…` | ✓ — **P6′-pair is false** |
| P6′-gov / P6′-min exceptions below `3·10⁶` | 0 / 0 | ✓ |
| P6′-gov min margin at `3·10⁶` (`notebook-2`) | `1.04641539561833…·10⁻²` | ✓ every digit |
| P6′-min global min (`notebook-0`) | `+0.48452773339831…` at `n = 1879`, `µ = 1831` | ✓ every digit |
| P6′-pair exception indices below `3·10⁶` | `{1836, 1837, 1840, 1844, 1845, 1846, 1847}` — FFM's first cluster, exactly *(local `m`-window, so a lower bound on the census, not a recount of it)* | ✓ |
| Proposition 4's two counter-models | both separations hold | ✓ |
| `d*(ℓ₁)` sufficient (Prop. R1) / true required (tight lemma) | `0.004363567696…` / `0.004362882388…` | ✓ |
| true required `d` under round-1's **printed** lemma; the F2 factor | `0.169339812744…`; ratio `38.8137468954…` | ✓ — **"false by a factor ≈ 38" is exact** |
| PA-0's displayed criterion, and that it exceeds its own reported sweep `0.004479` | `0.004488722463…` > `0.004479` | ✓ — F2(c) confirmed |
| headline constants `e^{−0.0043636}`, `e^{−0.0516}` | `0.995645906670…`, `0.949708674346…` | ✓ |
| `e^{−0.0017569}` | `0.998244642445…` | ✓ **against the skeptic; ✗ against FFM's printed `0.99824467` — §5.6** |
| `log 2⁶⁴`, `L(L−1.1)` at `2⁶⁴` | `44.36141955583649…`, `1919.13798349753288…` | ✓ exact |
| RH critical constant `max_x log x/√x` | `0.7357588823428846…` `= 2/e` at `x = e²`, to 60 digits | ✓ |
| barrier: `p_n^{1+1/n} < 2p_n` (`2 ≤ n ≤ 2·10⁴`) and `p_n < 2^n` (`2 ≤ n ≤ 216 816`, exact) | 0 failures each; and Bertrand does **not** certify at `n = 1` (`2² = 4 = 2·2`) | ✓ |

**Two things this verification changed in the document, reported rather than smoothed.**

1. **A new defect (§5.6).** `e^{−0.0017569} = 0.9982446424…`, not FFM §7.4's printed
   `0.99824467…`. Trivial, nothing depends on it, added to §7's checklist.
2. **Two of this leg's own first-draft checks were wrong, not the artifacts'.** The initial script
   scored round 1's printed-lemma requirement using the *sufficient condition* `(0.17 − 1/ℓ + err)/(2ℓ−1)`
   where the artifacts *solve* the quadratic `d(2ℓ−1) + d² ≥ R`, and used `ℓ⁴e^{−ℓ}` where the
   printed lemma's error term is `v·ℓ⁴e^{−ℓ}`. Corrected, both reproduce the artifacts exactly.
   The mis-specified expression turned out to reproduce a *different* published number
   (`0.0044887225`, PA-0's displayed criterion — the F2(c) figure), which is why the discrepancy was
   diagnosable at all; it is now checked under its correct label.

**Consistency against the brief.** Each required element is present and locatable: what was proved
(§2, with confidence codes and round-2 markers), what was refuted (§3), what remains open (§4), the
evidence-gate status stated honestly as **BLOCKED** with the failing leg named (§6), the rounds
trajectory with the shrink-versus-churn question answered plainly rather than dressed up (§1), and
an explicit statement that no citation clearance exists (§0, §6). The verdict rests on round 2's
artifacts; round 1's are cited only where round 2 left them standing, and every such case is marked.

**Not done, and named rather than omitted.** This leg did not re-run the Lean build, the `10¹¹`
sweeps, or the red-team corpus. It did not repair any upstream artifact — §5's adjudications are
statements about what to carry, not edits, and §5 says so at its head. It opened no source. It ran
no citation audit. And it did not independently reproduce FFM's witness W2 or its `10⁹` decade —
those rest on the FFM leg and, for W2, on the round-2 skeptic's independent reproduction.

---

## 9. Sources folded

**Round 2 — the final round, on which the verdict rests.** Under `attack/re-attack/`:

| Artifact | Leg | Molecule |
|---|---|---|
| `reattack-verdict.json`, `rounds.md`, `synthesis.md` | re-attack loop | `reattack-20260726-57d1` |
| `attack-round-2/proof-attempt-first-failure-maximality.md` | proof-attempt | `task-20260726-56a7` |
| `attack-round-2/proof-attempt-RH-conditional-bound.md` | proof-attempt | `task-20260726-b335` |
| `attack-round-2/proof-attempt-unconditional-verified-range.md` | proof-attempt | `task-20260726-2035` |
| `attack-round-2/lean-probe-report.md`, `unproved.md` | lean-probe | `task-20260726-8ba0` |
| `attack-round-2/faults.md` + `skeptic-round2-checks/` | skeptic | `task-20260726-7211` |
| `attack/evidence-verdict.md` (round-2 rewrite) | evidence-gate | `task-20260726-a94b` |
| `lean/Firoozbakht/Barrier.lean` (new, `sorry`-free) | lean-probe | `task-20260726-8ba0` |

**Round 1 — pinned, read, never re-run; cited above only where round 2 left it standing.** Under
`attack/`: `decompose.md`, `frame-deliberation/`, `concept-cards/` (30 cards + INDEX),
`source-ledger.md` (amended once in round 2), `proof-attempt-{0,1,2}.md`, `notebook-{0,1,2}/`,
`lean-probe-report.md`, `coverage-report.md`, `faults.md`, and the round-1 `synthesis.md` this
document supersedes.

**Downstream artifacts read for §6's honest reporting, not folded as evidence:**
`attack/verification-report.md` (citation audit, round 1, BLOCKED), `attack/editorial-verdict.md`
(editorial gate, round 1, REWRITE), `paper/paper.tex` (round-1 paper, stale as of round 2).

---

*Artifact of leg `synthesize`, molecule `task-20260726-7d7d`, run `germ-20260725-791a7c45`,
re-attack loop `reattack-20260726-57d1`, **round 2**. Supersedes the round-1 `synthesis.md` in
place. No number in this document was invented; every figure traces to a cited source artifact or
to this leg's own `verify_syn2.py`. The conjecture `F` remains **OPEN** — neither proved nor refuted
by either round. The evidence gate is **BLOCKED**. No citation clearance exists.*
