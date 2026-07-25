# Gödel — circularity and classification audit of `attack/decompose.md`

## Q1 — Completeness

**Already in the document (does not count):** §2.5's "no induction mechanism", §3.0's archetype table, §8's list of gaps.

**Finding 1.1 — the tree conflates two different arrows and therefore cannot be exhaustive in the sense it claims.** A proof-obligation tree should be *downward*: nodes whose discharge is required to obtain the root. P1, P2, P4, P6′ are downward nodes. **P3 is not.** P3 (`g_n = O(log²p_n)` unconditional) is a *consequence* of F, not a lemma for F. A proof of F discharges P3 automatically; nothing needs P3 first. The same is true of Corollary A1. Calling P3 "a hard gate on Branch P" (§2.1) is a statement about *difficulty*, not about *obligation*, and the tree has no notation to distinguish the two. Consequence for the frame: the claim "any complete resolution must pass through these nodes" is true for the downward nodes and vacuously true for the upward ones — so it cannot be used, as §2.1 uses it, to demand that a strategy "say how it clears P3". A strategy clears P3 by succeeding. This is a real structural defect and it is nowhere in §0/§7/§8.

**Finding 1.2 — a missing archetype: strengthening for inductive traction.** §2.5 declares P7 [X] because "there is no telescoping and no self-propagating structure". The standard cure for exactly that diagnosis — *strengthen the statement until it becomes inductive* (Nicholson/Farhadian-type strengthenings are gestured at in A11 and then deliberately omitted) — has no slot in §3.0's table. The table has "weakening" (S7) but no "strengthening". These are not symmetric: a weakening gives an easier theorem that says less about F; a strengthening can give a *harder* theorem that is nonetheless *easier to prove* because it carries a stronger induction hypothesis. Omitting it means §2.5's [X] verdict is asserted against the space of unstrengthened statements only.

**Finding 1.3 — a missing archetype: audit the heuristic rather than its citation.** S5/T5 make the Cramér–Granville prediction the load-bearing reason to believe F fails, and §7 flags A9 as the priority citation. But the only thing §9 dispatches is *checking that the citation exists*. There is no node anywhere for "assess whether the model is the right model at log-power scale" — which is precisely the scale where the Cramér model is known to be an unreliable guide (the Maier-type short-interval phenomena are the historical reason Granville corrected it in the first place). A leg that confirms A9 verbatim will have confirmed nothing about whether the tension in S5 is real. This is an archetype gap, not a citation gap, and §7's risk table cannot see it because it only grades attribution.

**Finding 1.4 — R2 is stronger than a refutation needs.** Refuting F requires `∃n: ρ_n ≥ 1`. R2 asks for `limsup g_n/log²p_n > 1`, which is strictly stronger (an asymptotic law). The branch has no node for a *non-constructive single-witness* existence proof — e.g. a pigeonhole/counting argument over an astronomically large but bounded range, which would refute F without establishing any limsup. R1 is constructive, R2 is asymptotic; the middle is empty.

## Q2 — Non-circularity (lead)

### (i) §3.2's self-admission — **under-stated, and mis-aimed**

The admission says an S2 hypothesis strong enough to yield F "is essentially a restatement of Cramér's conjecture, making the proof circular". Two things are wrong with this, and neither is in §8.

First, **"H implies F" is not circularity.** Every conditional proof has that property. The admission gives no criterion separating "legitimate strong hypothesis" from "disguised target", so the obligation it imposes on downstream legs ("show it is not a disguised restatement") is unfalsifiable as written. The correct criterion is proof-theoretic and statable: H is admissible iff H is *not* a consequence of F, or is independently verified. Assuming a **consequence** of F is worse than circular — it is useless.

Second, and sharper: **the document's own Corollary A1 shows that the Cramér-limsup hypothesis is a consequence of F** (`F ⟹ limsup ≤ 1`). So the specific hypothesis §3.2 warns about splits into two cases with opposite defects, and §3.2 names neither:

- *limsup form* (`limsup g_n/L² = 1`): implied by F (A1), therefore strictly weaker, therefore **cannot** yield F. Not circular — simply too weak. It constrains no finite `n`, and F is a statement at every finite `n`.
- *every-n form* (`g_n < L² − L − 1` for all `n ≥ n₀`): this is not "a disguised restatement" — by Claim A it is F itself up to `O(1/L)`, i.e. **literally equivalent modulo the error term the document has not made effective (§8.3)**. The word "disguised" understates it to the point of misdescription.

So the honest statement of the S2 obstruction is a **dichotomy with an unexamined middle**: any hypothesis at Cramér scale is either limsup-type (too weak to reach any finite `n`) or uniform-in-`n` (equal to the target). A legitimate S2 hypothesis must live in the gap — e.g. a *density* or *short-interval* hypothesis that is uniform but not pointwise. §3.2 does not locate that gap, so its instruction to downstream legs points at no target.

**Verdict: not circular, but the admission is a misdiagnosis. The real defect in S2 is a weakness/equivalence dichotomy, not circularity.**

### (ii) P6′ — **not circular in F; but the evidence offered for it measures the wrong thing**

`T_n = p_n(e^{L_n/n} − 1)` depends only on `(p_n, n)` — on the *location and count*, not on any gap. Its repair route (effective `π(x)` bounds, P4) therefore imports nothing about `g_n < T_n`. **No, the repair does not assume the bound it enables checking.** The suspicion is unfounded and I say so plainly.

The reduction *using* P6′ does invoke F — at index `m` — but legitimately: it is a minimal-counterexample argument (`n₀` minimal ⟹ F holds at every `m < n₀`), which is well-founded on ℕ. Sound.

**But there are two live defects the document does not see.**

**(a) §3.4 violates §2.4, three sections later.** §2.4 states that any leg citing "it suffices to check maximal gaps" without discharging P6′ "is importing an unproved lemma". §3.4 then writes: "By P6′ (**once discharged, or heuristically meanwhile**) the search may focus on record gaps". That is the document doing the exact thing its own gate forbids, in its only computationally live strategy. The consequence is not cosmetic: with the pruning in force and P6′ undischarged, a **null result from S4 no longer establishes anything about the swept range** — it establishes "no violation at record indices", which is a strictly weaker claim. §8.2 says P6′ is a hypothesis; it does not say that treating it as one silently downgrades the only live search from exhaustive to conditional. This is an internal inconsistency, not a self-flagged gap.

**(b) The empirical support offered for P6′ is non-diagnostic, and the diagnostic test was never run.** §5.1 finding 3 offers "all six tightest ρ cases occur at record gaps" as support for the maximal-gap reduction. That statistic is a manifestation of the reduction's *conclusion*; it is not evidence for its *hidden premise* `T_m ≤ T_n`. The document measured local monotonicity instead (55.9% of steps decrease) — which refutes the naive premise but says nothing about the record-straddling premise actually needed. The diagnostic test, run here:

For every `n` in the sieve range, with `m(n)` the last record index `≤ n`: **`T_{m(n)} ≤ T_n` holds at all 216 794 pairs, zero exceptions.**

So P6′ is considerably better supported than the document claims — and the document does not know this, because it reported a statistic that does not bear on the question. (Also checked the pruning's soundness directly: no non-record index anywhere in range has `ρ_n` exceeding that of its governing record. Zero cases.) The correction runs *in favour* of the artifact; the methodological error — offering evidence for a proposition adjacent to the one at issue — is the finding.

### (iii) Corollary A1 used twice — **reuse, not a loop, and the overclaim is elsewhere**

A1 is a single implication `F ⟹ limsup g_n/L² ≤ 1`, used in direct form for calibration and in contrapositive form for refutation. Two uses of one implication, in a tree where no node's discharge depends on the other's conclusion. **Not a loop. Well-founded.** Suspect dismissed.

But the sentence attached to it is false in a way that matters: "*This single implication drives almost the whole strategic picture in §3 and the primary refutation route in §4.*" It does not drive §3.4. **§3.4's search objective `ρ_n = g_n/T_n` comes from F4, which is an exact equivalence (P1, [E]), not from A1, which is asymptotic with a non-effective error (§8.3).** Attributing the search objective to A1 transfers A1's asymptotic softness onto a criterion that is in fact exact, and — worse — invites a downstream leg to search on `g_n` vs `L²−L−1` (asymptotic, wrong by `O(1/L)`) instead of `g_n` vs `T_n` (exact). §4.3 gets this right; §1.3's own summary sentence gets it wrong.

### Well-foundedness sweep — one further node

**§4.3's T3 depends on P4, which the document treats as undischarged.** T3's sufficiency requires `T_n < L_n²`, whose only warrant offered is a finite check plus a non-effective asymptotic. Making that warrant a theorem requires explicit `π(x)` bounds — i.e. node P4, tagged [O]. So a test tagged `[decidable, sufficient]` in §4 rests on an open node in §2, and the tree draws no edge. Details in Q4.

No node's stated discharge route passes back through an ancestor. **The tree is well-founded.** Its defects are edge-omissions and mis-attributions, not cycles.

## Q3 — Teeth

- **T1** — teeth, *conditional on three certificates, one of which the document does not mention.* Failure refutes F outright given (a) primality of both, (b) no prime strictly between — both listed — and **(c) a certificate that `p` is the `n`-th prime**. See Q4. Second escape hatch: the in-run implementation (`attack/probe.py`, lines 14–15) tests `n·log p_{n+1} ≥ (n+1)·log p_n` in double precision. The relative margin is `≈ (1−ρ_n)/n` (verified: at `n = 149 689`, predicted 1.6095e-6, measured 1.6094e-6). At the recalled published frontier `p < 4·10¹⁸` (`n ≈ 9.5·10¹⁶`) with `ρ ≈ 0.95`, that margin is `≈ 5·10⁻¹⁹` — **below double epsilon by three orders of magnitude.** The log-difference form loses its sign around `n ~ 10¹⁴`–`10¹⁵`. A double-precision "violation" at scale would not be a refutation, and a double-precision "no violation" at scale is not information. The `ρ = g/expm1(...)` form survives (both quantities are `O(L²)`); the form the probe actually uses for the violation test does not. §5.2 flags bignum size and `Nat.nth` kernel reduction — it does not flag this, and the two hazards are unrelated.
- **T2** — teeth, exactly as T1, minus indices 1–9. See Q4 for the `n ≥ 10` defect.
- **T3** — teeth **only with the side condition stated in the test**. As written it has no teeth at three explicit indices. See Q4.
- **T4** — teeth. `F ⟹ limsup ≤ 1` is asymptotic, so the non-effectivity of A1's `O(1/L)` is harmless here. This is the one test whose warrant is clean.
- **T5** — correctly no teeth; the document is right and says so.

**Cross-cutting:** the tests all have teeth in the *failure* direction. The asymmetry that actually endangers the compute plan is the *null-result* direction — see Q2(ii)(a). A swept range under record-gap pruning yields no exhaustiveness claim.

## Q4 — Classification (lead)

### §4.3 re-derived from scratch

T3: `g_n ≥ L_n²`. T2: `g_n ≥ T_n`. If `T_n < L_n²` then `g_n ≥ L_n² > T_n`, hence T2 breached, hence ¬F. **The document's direction is correct: T3 ⟹ T2, T3 is sufficient and not necessary.** The reversal it made was the right one.

**But the sufficiency is conditional, the condition is absent from the test statement, and there are explicit counterexamples to the unguarded form.** `T_n ≥ L_n²` holds exactly at `n ∈ {1,2,3,4,5,6,7,10}` in range. And T3 is *actually breached* at three of those:

| n | pₙ | gₙ | gₙ/Lₙ² | Tₙ | Lₙ² | F holds? |
|---|---|---|---|---|---|---|
| 1 | 2 | 1 | 2.081 | 2.000 | 0.481 | yes (exact integer check) |
| 2 | 3 | 2 | 1.657 | 2.196 | 1.207 | yes |
| 4 | 7 | 4 | 1.056 | 4.386 | 3.787 | yes |

So T3 as stated in §4.3 — "`Find n with g_n/log²p_n ≥ 1`", tagged `[decidable, sufficient]` — is **satisfied right now, three times over, by a conjecture that holds at those indices.** The guard lives in a parenthetical about what was verified, not in the test. The tag is wrong; it should read `[decidable, sufficient for n ≥ 11]`.

**Is the sufficiency unconditional or only on the checked range?** Neither, as the document stands. Its warrant is "verified in-run to hold at every `n ≥ 11` up to 216 815" plus "`< L²` for all large `n`" from Claim A, whose `O(1/L)` is explicitly not effective (§8.3). **The verified range is precisely the range in which T3 cannot fire** (no breach above `n = 4`), and the range in which T3 could fire is precisely the unverified one. The finite check therefore contributes *zero* to the sufficiency claim as it is used. That is a clean instance of a test's warrant and its domain of application being disjoint, and it is nowhere in §8.

**The repair is cheap and the document misses it.** `T_n < L_n²` unwinds to an elementary condition: `p_n(e^{L/n} − 1) < L² ⟺ L/n < log(1 + L²/p_n)`, and since `log(1+u) > u − u²/2`, it suffices that `p_n/n < L_n − L_n³/(2p_n)`. The correction term is exponentially small; the substance is `p_n/n < log p_n`, i.e. `π(x) > x/log x` — an explicit, unconditional, classical estimate with a named validity range. So T3's sufficiency is provable for all `n` above a small explicit bound using precisely the Dusart-type input that node **P4** is supposed to supply. Two consequences: (1) the fix is a half-page, not a research problem; (2) **T3's classification is not independent of the tree — it is a P4 client, and P4 is [O] and undischarged.** No edge in §2 records this.

### T2 ≡ T1?

**Exactly equivalent, with no `O(1/L)` involved — and the document's own phrasing obscures why.** F4 is an exact equivalence: `g_n < T_n ⟺ p_{n+1} < p_n e^{L_n/n} ⟺ n log p_{n+1} < (n+1) log p_n ⟺ p_{n+1}^n < p_n^{n+1}`. The `O(1/L)` in §4.2 attaches solely to the *paraphrase* `g_n ≥ L² − L − 1`, which is a third, strictly weaker test that §4.2 sets in apposition to `ρ_n ≥ 1` with the word "equivalently". They are not equivalent; one is exact and one is asymptotic, and the sentence invites the search leg to implement the wrong one.

**Two further defects in T2, both unflagged:**

**(a) The `n ≥ 10` restriction is an unwarranted import — and it is the exact propagation §1.3 forbids.** §1.3 says in bold: "**Do not** propagate 'for n ≥ 10' downstream as established". T2 propagates it, into the test statement (§4.2) and into §5.1's headline statistic. There is no reason for it: `ρ_n ≥ 1 ⟺ ¬F at n` holds at every `n ≥ 1` with no threshold, because F4 is exact. The threshold belongs to the *recalled literature form* `g_n < L²−L−1` (A3, [needs-anchor]) and to nothing else.

**(b) The restriction hides the two tightest cases in existence.** Over all `n` with no cut:

| rank | n | pₙ | gₙ | ρₙ |
|---|---|---|---|---|
| 1 | 4 | 7 | 4 | **0.9120** |
| 2 | 2 | 3 | 2 | **0.9107** |
| 3 | 217 | 1327 | 34 | 0.7605 |
| 4 | 149 689 | 2 010 733 | 148 | 0.7591 |

`ρ = 0.912` at `p = 7`. The document's reported maximum, 0.7605, is an artifact of the cut. This matters for the *fragility* narrative: converting the recalled all-primes record (gap 1132 at `p ≈ 1.693·10¹⁵`, `L ≈ 35.07`) into ρ units gives `ρ ≈ 0.949` — so the conjecture's high-water mark at `10¹⁵` is barely above its high-water mark at `p = 7`, and `ρ` is nowhere near monotone in `p`. Any downstream claim of the form "the record ratio grows slowly toward 1" is reading a trend into a statistic whose global maximum sits at the fourth prime.

**(c) Tag inconsistency:** T1 is `[decidable, Σ₁]`, T2 is `[decidable]`. They are the same Σ₁ search. Also, "decidable" is doing double duty: per-`n` decidability (true for both) versus resolvability of the search (semi-decidable only). The alphabet does not distinguish them, and R1 carries `[C]` — the same code as P5, a genuinely terminating finite check. That is a category error in the status alphabet, not just in one node.

### §4.6 anti-test

**The estimate is right; the heading over-scopes it.** Confirmed: `T ≈ xL/n`, so `δT/T ≈ −Δ/li(x) ≈ −log log log x/√x`, giving `δT = O(L²·log log log x/√x) → 0`. Littlewood oscillation cannot move the threshold. No hidden case in *that* claim.

**But the claim proved is "irrelevant to the threshold `T_n`" and the heading is "what does NOT bear on F".** F is `g_n < T_n`, a two-sided relation. The estimate bounds the effect on the right side and says nothing about the left. Regions of persistent prime deficit are exactly where one would look for anomalously large `g_n`; that line is not excluded by anything in §4.6, yet the heading tells a downstream leg it has been closed. "**This closes an otherwise attractive line of attack**" is true of the threshold-shift version and false of the gap-correlation version. Given that §4.6 exists specifically to prevent wasted effort, an over-scoped exclusion is more costly than a missing one.

The Bertrand item is correct as stated.

### §1.4 arithmetization

**`¬F` is Σ₁ and `F` is Π₁ — correct**, and correct with `p_n` via `Nat.nth`: `q = p_n` is expressible with bounded quantifiers (`q` prime ∧ the count of primes `≤ q` is `n`), so the matrix is Δ₀ and the classification stands over PA. No objection.

**The sentence built on it is wrong, and it is load-bearing.** §1.4: "*A refutation is therefore finitely certifiable — a single integer `n` plus the two primes, with primality certificates, settles it.*" It does not. The exponents in `p_{n+1}^n < p_n^{n+1}` **are the index**, so a refutation must also certify `π(p_n) = n`. Primality certificates are succinct (Pratt/ECPP); **an index certificate is not** — no succinct certificate for `π(x) = n` is known, and the best verification is a `Õ(x^{2/3})` analytic computation or a full sieve. §1.4 conflates *finite* witness (Σ₁, true) with *short* witness (false). Three concrete consequences the document never draws:

1. It explains why the verification frontier tracks the prime-*enumeration* frontier (the recalled `4·10¹⁸` in A2/A12 is an enumeration limit, not a primality limit) — and therefore why §3.4's instruction to "extend the ratio table" is an exhaustive-sieve project, not a spot-check project. That is the single largest compute-planning fact in the document and it is absent.
2. It undercuts §1.4's own claim that the Σ₁/Π₁ asymmetry "is the reason §3's feasibility verdicts are so lopsided". The asymmetry is real but far less lopsided than stated: refutation is cheap in *logical* form and expensive in *computational* form.
3. For the Lean legs it is the deep version of §5.2's `Nat.nth` observation. §5.2 says `Nat.nth Nat.Prime n` is not kernel-reducible and proposes "prime literals plus a no-prime-strictly-between lemma". That workaround supplies (a) and (b) and **silently omits the index certificate** — the `n` in the exponent still has to be justified. The workaround as written does not formalize F at index `n`; it formalizes a statement about two adjacent primes with an unjustified exponent.

**One more, in §6/L1 — an off-by-one that changes the theorem.** L1 defines `p n := Nat.nth Nat.Prime n` and `Firoozbakht : Prop := ∀ n ≥ 1, (p (n+1))^n < (p n)^(n+1)`, while §1.1 fixes `p_1 = 2`. `Nat.nth` counts from 0, so `Nat.nth Nat.Prime 0 = 2` and `p k = p_{k+1}` in the document's own indexing. L1 then states `p_{n+2}^n < p_{n+1}^{n+1}` for `n ≥ 1`, i.e. with `m = n+1 ≥ 2`: `p_{m+1}^{m−1} < p_m^{m}` — equivalently `log p_{m+1}/log p_m < m/(m−1)`, against F's `< (m+1)/m`. Since `m/(m−1) > (m+1)/m`, **L1 as written is strictly weaker than F, and additionally drops the index `m = 1`.** §6 tags Mathlib *names* as `[needs-anchor]`; indexing convention is semantics, not naming, and no tag covers it. This is the "anchor object every other leg must import", so the error propagates to L2, L3, L5 and to every equivalence the plan is meant to guarantee.

## Q5 — Quiet assumptions

The tagging discipline is not applied to itself, in five places.

1. **Claim A is tagged `[self-contained]` and is not.** Its first line imports "the standard asymptotic expansion of π", `π(x) = (x/L)(1 + 1/L + 2/L² + O(L⁻³))` — PNT with a three-term expansion and an error term. That is exactly the class of statement §0 says must be anchored. The algebra downstream of it is self-contained (checked: the inversion `(1 + 1/L + 2/L²)⁻¹ = 1 − 1/L − 1/L² + O(L⁻³)` and the second-order term `L⁴/(2x) → 0` are both right). The *input* is not. This is the document's most load-bearing derivation and it carries the wrong tag.
2. **P2 is tagged `[E]` while §6 says its input is unavailable.** §2 marks P2 "established here or elementary". §6 states "PNT with error terms is *not* assumed available in Mathlib proper; if needed it must be sourced from the PNT+ development or axiomatized". A node cannot be [E] in §2 and an axiom candidate in §6.
3. **P3's second pillar has no anchor ID at all.** §2.1 rests on two recalled theorems: Baker–Harman–Pintz (A5) and "under the Riemann Hypothesis the bound improves only to roughly `g_n ≪ √p_n log p_n`". The second appears in no row of §7. §7 claims to be where every `[needs-anchor]` points; the hard gate on Branch P is half-uncovered by its own ledger. The Jacobsthal-function claim in §3.8 is likewise unanchored.
4. **Units are conflated in §3.8.** It writes "`ρ_{n₀} ≥ 1` where the observed maximum below `3·10⁶` is `0.7605` and the recalled record over all known primes is `≈ 0.92` (A10)". 0.7605 is `g/T`; A10's 0.9206 is `g/L²`. Two different statistics in one clause, presented as one series. In ρ units A10 is `≈ 0.949`. §4.3 handles the conversion correctly (its "bar `1 − 1/L − 1/L² ≈ 0.971`" checks out at `L ≈ 35.07`); §3.8 does not, and §3.8 is the section recommended as a `proof-attempt` target.
5. **The in-run evidence carries no error analysis.** Every number in §5.1 is double precision. §5.2 is titled "Numerical hazard" and discusses integer sizes and kernel reduction — i.e. hazards for Lean, not for the probe that produced the evidence. The tier-L1 "verified in-run" label is applied to floating-point results with no bound stated. At `3·10⁶` this is harmless; the label is what travels downstream, and the label does not carry the range of validity. Related: "record gaps are far apart" (§2.4), used to argue P6′ is repairable, is an untagged heuristic.

## Q6 — Verdict calibration

- **P1 [E]** — correct.
- **P2 [E]** — wrong, see Q5.2. Should be `[E modulo an imported PNT expansion, needs-anchor]`.
- **P3 [X]** — correct *as a difficulty verdict on proving that statement*, but the node is misplaced in the tree (Q1.1). It is not an obligation.
- **"Proving Firoozbakht is strictly harder than proving the Riemann Hypothesis is useful for prime gaps"** — the hedged form is defensible; the word **"strictly" is overreach**. "Strictly harder" is a claim about relative provability: it would require showing RH ⊬ F. Nothing of the sort is known — no one has derived F from RH, which is a fact about the current state of technique, not about implication. The defensible sentence is: *no known argument derives F, or even its `O(log²p)` consequence, from RH; the shortfall is a full power scale, not a constant.* As written, a downstream leg could quote "strictly harder than RH" as an established relation. It is not one.
- **R2/R3/R4 section pointers are all wrong.** The tree routes `R2 → §4.2`, but §4.2 is T2 (decidable ratio breach) while R2 is the limsup theorem, which is §4.4/§3.3. `R4 → §4.4`, but §4.4 is T4 (asymptotic breach, a theorem route) while R4's own gloss says "Cramér–Granville heuristic — refutes F only heuristically", which is §4.5/§3.5. `R3 → §4.3` maps an [O] node onto a decidable search test. Three broken cross-references in the artifact's central diagram, and the [O]/[C] codes drift with them.
- **R4 [O] is a category error.** [O] means "open but plausibly reachable" — a route that could resolve the root. R4 *cannot* resolve the root by construction; §4.5 says so. The alphabet has no code for "non-probative in principle". The same hole covers T5, and it is the sort of hole that lets a heuristic be promoted by a compressing leg — which §9 identifies as the exact risk it wants `synthesize` to guard against, while leaving the notation unable to express it.
- **R1 [C] alongside P5 [C]** — P5 terminates; R1 is a semi-decidable search that may never terminate. Same code, different kinds.
- **"L4 is the only node that is a genuine theorem"** — **false, and mis-prioritized.** L2 (F1 ⟺ F2 ⟺ F3) and L5 (F ↔ ∀n, gₙ < Tₙ) are genuine theorems: non-trivial iff statements about real powers and logarithms, neither a definition nor a finite check. More to the point, **L4 contains no primes.** It is the calculus fact that `(log x + log log x)/x` is strictly decreasing on `[5,∞)` — the derivative expression and the sign change verified (`+0.0089` at `x = 4`, so `x ≥ 5` is right and `x ≥ 4` is not). Its deductive contribution to F is zero: §3.6 concedes that relating the smooth model to `p_n` "is exactly P3 again". So the node designated "the primary deliverable of the Lean legs" is the node with the least arithmetic content and no path to the root. That is optimizing for a shippable artifact, not for progress on the problem, and the phrase "genuine theorem" is what makes the substitution invisible.

## Q7 — Ranking

Ordered by how much damage the defect does to the next weeks of compute.

## Weakest branches (ranked)

1. **L1 (and through it L2, L3, L5) — off-by-one in the anchor definition.**
   `Nat.nth` is 0-indexed against the document's `p_1 = 2`, so L1 states `p_{m+1}^{m−1} < p_m^{m}` — strictly weaker than F, and missing `m = 1`. Everything imports L1.
   *What must change:* state L1 with an explicit index lemma pinning `p 1 = 2` under the pinned toolchain's convention, and add `Firoozbakht ↔ ∀ n ≥ 1, p_{n+1}^n < p_n^{n+1}` in the document's own 1-indexed notation as a proved equivalence, not a reading convention. §6's `[needs-anchor]` must be widened from *names* to *names and indexing*.

2. **T1 / R1 — the missing index certificate.**
   §1.4's "finitely certifiable" conflates Σ₁ with succinct. Certifying a counterexample requires certifying `π(p_n) = n`, for which no short certificate is known.
   *What must change:* §1.4 must separate "finite witness" from "short witness"; the certificate schema in §4.1 must add the index obligation; §5.2's Lean workaround must be marked incomplete (it supplies primality and no-prime-between, not the exponent); and §3.4's search plan must state that extending the ρ table is an exhaustive-sieve or analytic-π project with `Õ(x^{2/3})` verification, not a spot search.

3. **T3 — sufficiency asserted where its warrant does not reach, with live counterexamples to the unguarded form.**
   T3 fires at `n = 1, 2, 4` with F holding; `T_n ≥ L_n²` at `n ∈ {1..7, 10}`; the finite check covers exactly the region where T3 cannot fire.
   *What must change:* put the guard in the test (`sufficient for n ≥ 11`); replace the finite-check warrant with the elementary reduction `T_n < L_n² ⟸ p_n/n < L_n − L_n³/(2p_n) ⟸ π(x) > x/log x`, and draw the resulting **T3 → P4** edge in §2.

4. **S4 / P6′ — the search is pruned by an undischarged lemma, in violation of §2.4.**
   §3.4's "heuristically meanwhile" converts the only live search from exhaustive to conditional; a null result then proves nothing about the swept range. Separately, the evidence offered for P6′ (tight ρ at records) does not bear on its hidden premise.
   *What must change:* either run the search unpruned, or state every null result as "no violation **at record indices** in range". And replace §5.1's finding 3 with the diagnostic statistic — `T_{m(n)} ≤ T_n` for `m(n)` the governing record index, which holds with **zero exceptions across 216 794 pairs** in the sieve range. That measurement supports P6′ far better than anything currently in §5.1 and should be extended, not the ρ table alone.

5. **T2 / §5.1 headline — the `n ≥ 10` cut, which §1.3 explicitly forbids propagating.**
   It hides `ρ = 0.912` at `p = 7` and `0.911` at `p = 3`, the two largest values known, and it makes 0.7605 look like a trend.
   *What must change:* drop the cut (F4 is exact at every `n ≥ 1`); report ρ over all `n`; and restate the fragility calibration in a single unit — the recalled A10 record is `ρ ≈ 0.949`, not 0.92, in ρ units. Fix §3.8's unit conflation at the same time.

6. **P3 / §2.1 — an upward node presented as a gate, plus an unanchored pillar and an overclaim.**
   *What must change:* mark P3 as a consequence-node, drop the demand that strategies "clear" it (they clear it by succeeding), add a §7 row for the RH-conditional gap bound, and replace "strictly harder than RH" with the technique claim it actually supports.

7. **L4 — designated primary deliverable, zero deductive contribution.**
   *What must change:* keep it (it is correct, and `x ≥ 5` is the right range) but demote it. Promote L2 and L5, which are genuine theorems *about the object under study* and which deliver the stated value of the Lean legs — no leg silently using a wrong reformulation.

8. **§4.6 anti-test — correct estimate, over-scoped heading.**
   *What must change:* retitle to "irrelevant to the threshold `T_n`" and add one sentence noting that the correlation between prime-deficit regions and large `g_n` is untouched by the estimate.

9. **The status alphabet itself.**
   `[E] [O] [X] [C]` cannot express "non-probative in principle" (R4, T5), cannot distinguish terminating from semi-decidable computation (P5 vs R1), and cannot distinguish downward obligations from upward consequences (P4 vs P3). A tree whose notation cannot state the status of its own non-probative nodes will lose them under compression — which §9 already fears, without seeing that the cause is notational.

10. **§3.0's taxonomy — two missing archetypes.** No slot for *strengthening for inductive traction* (the standard cure for the very diagnosis that makes P7 [X]), and no slot for *auditing the heuristic model* as opposed to its citation (S5 is load-bearing for the belief-direction, and §9 dispatches only a citation check).
    *What must change:* add both rows before the strategy legs are dispatched, since §3.0 is what those legs will read as the closed space of options.

**Files read:** `attack/decompose.md`, `attack/probe.py`, `attack/probe2.py`. Verification scripts written to the session scratchpad; nothing written into the repository.
