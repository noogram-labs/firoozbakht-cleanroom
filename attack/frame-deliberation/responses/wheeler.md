# Wheeler — frame audit of `attack/decompose.md`

Before anything else: I ran my own numerics against the same sieve (scratch script, not committed) to test four load-bearing claims in `attack/decompose.md` §2.4, §4.3, §5.1. Results are quoted inline and are reproducible from `attack/probe2.py` with two added measurements.

---

## Q1 — COMPLETENESS

**The space is not closed.** I claim this affirmatively, with four named holes and the node each would need.

**First, a structural defect that causes three of the four.** §2 of `attack/decompose.md` opens with "Any complete resolution must pass through these nodes." That is a universal claim, load-bearing for the whole document, and it is **untagged** — the one place the tagging discipline is not applied to the discipline itself. It is also false, as H1 below shows.

The deeper defect: **§2 is drawn as a tree, but a proof is a join.** A tree expresses disjunction (alternative routes) and refinement (sub-obligations). It cannot express conjunction — "this node AND that node together discharge the root." Every archetype missing below is missing because it is a *conjunction* of two nodes that are already present separately.

**H1 — Independence / unprovability. Missing node: P8.**
§1.4 establishes the premise with unusual care: `¬F` is Σ₁, `F` is Π₁. It then never draws the standard inference. A false Π₁ statement is refutable in PA. Therefore if `F` is shown independent of any Σ₁-sound theory, **`F` is true** — established without passing through P1–P7 or R1–R4. The tree conflates "prove F" with "establish F". Realistically P8 is `[X]`, but the tree has no node at all, and the document holds the premise for the inference in its own §1.4. This alone falsifies §2's exhaustiveness claim.

**H2 — Computational verification composed with a structure theorem. Missing node: the join P4 ∧ P5.**
This is the most consequential hole, because it is the shape of nearly every explicit theorem in this area: prove the statement for `n > N₀` with `N₀` *named*, then verify `n ≤ N₀` by machine. §2 has both halves — P4 (effectivity) and P5 (finite verification) — as siblings, and then §2.3 forecloses the composition in one sentence: *"Purely computational; establishes nothing about the general case."* True of P5 alone; false of P5 ∧ P4. Because the tree cannot draw the join, the sentence that describes the leaf becomes a verdict on the composition. Note this is also the only realistic shape for the S7 weakenings the document itself calls "the most likely source of an actual theorem."

**H3 — Conditional refutation. Missing node: R5.**
The P branch carries both an unconditional route (S1) and a conditional one (S2, "assume RH or stronger"). The R branch carries an unconditional route (R2/S3) and a *heuristic* one (R4/S5/T5) — and nothing conditional. That asymmetry is unexplained and is a category error: "¬F follows from conjecture X" is a theorem; "the Cramér model predicts limsup > 1" is not a hypothesis one can assume, because the model is not a statement. The document handles the heuristic with real care (§3.5 is among its best passages) but the care is spent policing the heuristic, not on noticing that the conditional slot next to it is empty. R5 — derive ¬F from a precisely-stated standard conjecture — is the shape of the strongest result this attack could plausibly produce.

**H4 — Transfer, and the un-instantiated R3.**
§3.0's table has no row for reformulate-then-import (restate F in the ψ/θ world, or as a zero-density statement, where explicit technology actually exists). More seriously, R3 ("refute a consequence of F that is easier to attack") is listed `[O]` and **never instantiated** — not one consequence besides the gap bound appears anywhere. Combined with §1.3's Corollary A1 being the hinge of "almost the whole strategic picture" (§1.3's own words), the result is that §2 is not a tree of routes to F. It is a tree of routes to a Cramér-scale gap bound, with one node of fan-in. Single point of failure, undeclared.

**Two further coverage illusions in §3.0's table.**

- **S3 and S9 are the same node.** §3.3 blocks S3 on the FGKMT large-gap magnitude wall; §3.9 blocks S9 on the same wall "from the other side." But the FGKMT-lineage lower bounds *are* Erdős–Rankin-style constructions — the construction is how the bound is proved. So two rows of the archetype table ("Contradiction" and "Construction") are discharged by one obstruction, and the table reads as broader coverage than it has.
- **P3 is a consequence, not a prerequisite.** `F ⟹ g_n = O(log²p_n)`. It is not a step you must first prove; it is a lower bound on `F`'s strength. Drawing it as a child of "PROVE F" alongside P1, P4, P5 (which *are* prerequisites) means the tree mixes arrow directions and cannot be read as a plan. See Q6.

Not counted as findings, already in the document: the unverified-anchor status of §7 (§0), P6′'s openness (§8.2), the O(1/L) ineffectivity (§8.3), the two caught direction errors (§8.8).

---

## Q2 — NON-CIRCULARITY

**(i) §3.2's own admission.** Already in the document — does not count. One addition that is not: the obligation §3.2 imposes ("show it is not a disguised restatement of the target") is stated with **no criterion for discharge**. As written it is unfalsifiable, so any downstream leg can satisfy it by assertion. A usable criterion exists in the document's own material — the hypothesis must have a consequence outside the gap regime, or must be known consistent with `¬F` — but it is not stated, so the guard has no teeth.

**(ii) P6′ — no circularity, and the repair route is misdescribed.** P6′ (`attack/decompose.md` §2.4) proposes to control "T's oscillation" using P4. It nowhere assumes `g_n < T_n`, so it is not circular. But the framing imports a false picture of the difficulty: **`T` is a function of the point, not of the path.** `T_n = p_n(e^{L_n/n}−1)` depends only on `(n, p_n)`. Comparing `T_m` and `T_n` therefore needs no oscillation control and no record-gap structure — it needs a two-sided pointwise envelope from explicit π bounds, and nothing else. The differencing in §2.4 correctly explains *why* `T` wobbles, and is then mistaken for the obligation. See Q6 and Q7 for what this costs.

**(iii) Corollary A1's double use — not a loop.** Both uses are the same single implication `F ⟹ limsup g_n/L² ≤ 1`, direct for the objective and contrapositive for refutation. That is legitimate. Note also that §3.4's search objective `ρ_n = g_n/T_n` does not actually use A1 at all — it uses F4 exactly. A1's asymptotic form only enters the *surrogate*, which is where the damage is (Q3).

**An evidential loop that is not listed.** §3.4 prunes the S4 search to record gaps "by P6′ (once discharged, or heuristically meanwhile)", and §3.8 supports the same pruning with §5.1's observation that all six tightest ρ cases sit at record gaps. Both the pruning rule and the search it prunes draw on the same in-run sieve — a range over which the conclusion (no counterexample) is already known. Using no-counterexample-range statistics to design a counterexample search is a selection loop: the range is uninformative about the regime where the rule would matter. Not circular in the logical sense; circular in the evidential sense, and untagged.

---

## Q3 — TEETH

**T1.** Exact ¬F. No escape hatch in the statement. The certificate obligation *is* priced honestly in §4.1 except for one item: "a proof that no prime lies strictly between them" is not free at the published frontier — it is a gap-verification over an interval of ~1500 integers with primality certificates for none of them, which is a different and larger artifact than the two primality proofs named. Under-priced, not wrong.

**T2 — exactly equivalent to T1, but the document immediately spends the exactness.** The primary form `ρ_n = g_n/T_n ≥ 1` is precisely `¬F4` at `n`; no O(1/L) is involved, because `T_n` is the exact quantity. The O(1/L) attaches only to the parenthetical surrogate. **But §3.4 then makes the surrogate the search objective** ("equivalently `g_n/(L²−L−1)` up to O(1/L)"), and the slack is not academic. I measured it:

```
top-8 by exact rho:      n=217(p=1327), 149689, 3385, 31545, 30(p=113), ...
top-8 by surrogate:      n=30(p=113),   11(p=31), 217, 149689, 3385, ...
relative error at n=217: +2.744%
```

The surrogate **reorders the leaderboard** and inflates ρ by 2.7% at the tightest observed case. Against the 5% margin the document calls the conjecture's fragility (§4.3), a 2.7% objective error is half the margin. So: T2 has full teeth in its exact form; the form §3.4 hands to the search leg does not, and can only flag candidates, never certify a breach. The document does not distinguish the two.

Restriction to `n ≥ 10` in T2's statement leaves `n < 10` uncovered — trivially checked, but the test as written is not literally equivalent to T1.

**T3.** Teeth are real but conditional — see Q4.

**T4, T5.** Correctly handled. T5's exclusion (§4.5) is one of the document's strongest moves and I have nothing to add.

**Are the refutation-implications theorems of the document, or assertions?** T1 and T2 are theorems (the F1–F4 derivation in §1.2 is complete and correct — I checked the equivalence chain). T3's is an assertion resting on a finite check. T4's rests on Corollary A1, whose derivation I verified (the inversion `(1+1/L+2/L²)⁻¹ = 1−1/L−1/L²` and the `L⁴/2x` second-order term are both right).

---

## Q4 — CLASSIFICATION

**The "decidable" tags are wrong in kind on T1–T3.** *Finding* an `n` is semi-decidable, not decidable; *checking* a given `n` is decidable. `[decidable, Σ₁]` on T1 puts both words on the same object. In a document that builds its central structural insight on the Π₁/Σ₁ asymmetry (§1.4), this is a slip worth correcting, and it is not among the two errors §8.8 records. T2 additionally drops the `Σ₁` half of the same tag for no stated reason.

**T3 re-derived.** The direction in §4.3 is **correct**: `T_n < L²` ⟹ a `g_n ≥ L²` breach implies `g_n > T_n` implies ¬F. T3 is sufficient, not necessary, and conservative by ≈ `L+1`. The correction the document made to itself stands.

**But the sufficiency is not unconditional, and the tag does not say so.** It rests entirely on `T_n < L_n²`, which §5.1 establishes only by checking `n ≥ 11` up to 216815. Unconditionally, `T_n < L²` requires `p_n/n < L_n` at second order — i.e. an explicit lower bound of Rosser–Schoenfeld/Dusart shape `π(x) > (x/L)(1 + 1/L)`. That is exactly node **P4**, which the document itself tags `[O]` and §8.3 declares undischarged. So T3's classification silently depends on an open node. The tag should read `[sufficient, conditional on P4]`.

Two details from my run that matter for anyone formalizing this. The exceptional set is `{1,2,3,4,5,6,7,10}` — `T_n ≥ L²` fails at `n = 8` and `n = 9` and then **returns** at `n = 10`:

```
n where T_n >= L^2:  1,2,3,4,5,6,7,10   (count 8)
```

So `n ≥ 11` is empirically the right threshold but is **not** a clean monotone crossing. Any Lean leg attempting `T_n < L²` by induction from a base case will find the base case is not where it looks.

**§4.6 anti-test — correctly excluded, and I re-derived it.** With `n = li(x)+Δ`, `δT ≈ T·Δ/n ≈ L³Δ/x`, and `Δ ≍ √x·log log log x/log x` gives `δT = O(L²·log log log x/√x) → 0`. The document's estimate matches mine. This is a genuinely good exclusion and should be preserved.

One scope caution, not a correction: §4.6 closes *global* π oscillation as irrelevant to the threshold. It does not close, and must not be cited to close, π control in P4 and P6′, where explicit two-sided bounds are precisely what is needed. The anti-test and the effectivity node point in opposite directions about π and sit four sections apart.

---

## Q5 — QUIET ASSUMPTIONS

The tagging discipline is applied rigorously to *imported* claims and not at all to the document's own *inferential* moves. Six untagged assumptions, ordered by what they cost.

**1. Frequency substituted for amplitude (§2.4, §5.1).** The document measures how *often* `T` decreases (121238/216805 = 55.9%) and never how *much*. The reduction in P6′ needs the amplitude — specifically, how far `T` ever dips below its own running maximum. I measured it:

```
n in [10,100]:      max dip 0.5457   min margin T-g  5.286   dip/margin 1.0e-01
n in [100,1000]:    max dip 0.5487   min margin      10.709  dip/margin 5.1e-02
n in [1000,10^4]:   max dip 0.2207   min margin      24.188  dip/margin 9.1e-03
n in [10^4,10^5]:   max dip 0.1025   min margin      38.529  dip/margin 2.7e-03
n in [10^5,216800]: max dip 0.0181   min margin      46.972  dip/margin 3.8e-04
```

The dip decays like O(1/L) while the margin grows like L. **The 55.9% figure is the uninformative statistic**, and the document's verdict that P6′ is "a live correctness risk" and one of "the two places this decomposition is most likely wrong" (§9) is drawn from it. Monotonicity of `T` is indeed false — but it was never the obligation. See Q7 item 1.

**2. Float conditioning of §5.1's headline statistic.** Double precision is *ample* at the in-run range — the reported margin `1 − 0.9999984 = 1.6e-6` sits ten orders above float noise, so the suspicion that seven significant figures is over-claimed is unfounded and I say so explicitly. The untagged assumption is elsewhere. The statistic `1 − n log p_{n+1}/((n+1) log p_n)` decays like `≈ 0.9/n`:

```
n=10: 7.3e-02   n=10^3: 8.9e-04   n=10^5: 9.3e-06   n=216815: 3.7e-06
```

It reaches double epsilon near **n ≈ 4·10¹⁵** — *below* the recalled published frontier of 4·10¹⁸ primes (A2). `ρ_n` meanwhile stays O(1) at every scale (`1−ρ ≈ 0.8` throughout). So §5.1's headline check silently stops meaning anything before the frontier the document wants a search leg to extend past, while §5.2's "numerical hazard" section discusses bignum digit counts and Lean kernel reduction — a different hazard entirely. Untagged, and directly actionable for `notebooks`.

**3. `n ≈ p_n/L_n` substituted inside the differencing (§2.4).** PNT-level and fine for a sign heuristic. But the substitution carries relative error O(1/L) ≈ 3%, and the quantity whose *sign* is being read is `(g_n − L)`, which is O(1) — the error is comparable to the signal exactly for gaps near the average, which is the majority of gaps. The empirical count happens to corroborate the conclusion, so nothing breaks; the derivation nonetheless does not support the verdict it is used to justify.

**4. Term-wise inversion of π's expansion (§1.3).** Legitimate as asymptotics, and I verified the algebra. What is untagged is that the resulting `O(1/L)` has **no named range**, and is then silently reused at finite `n` in three places: §4.3's `n ≥ 11`, §3.4's surrogate objective, and P6′'s repair. §8.3 says P4 is not discharged; it does not say that three downstream conclusions already spend it.

**5. The smooth surrogate `(x log x)^{1/x}` (§3.6).** This is the *first-order* model. `p_n ≈ n(log n + log log n − 1)`, and the dropped `−1` is of the same order as the `−L−1` in `T_n = L²−L−1` that makes the threshold sit below `L²` — which is the entire content of §4.3. So L4, the document's nominated "primary deliverable of the Lean legs", is a theorem about a model that discards a term of the same magnitude as the phenomenon under study. Untagged.

**6. The meta-assumption.** Answered in Q1/H2: tree-shape was assumed, and a tree cannot express the conjunction that is the only realistic proof shape here.

---

## Q6 — VERDICT CALIBRATION

**P3.** `[X]` is right about the *statement* and wrong about the *node*. `F ⟹ P3`, so P3 is a consequence, not an obligation. Placing it as a child of "PROVE F" next to genuine prerequisites means the tree cannot be read as a plan.

The forced verdict — "proving Firoozbakht is strictly harder than proving RH is useful for prime gaps" — is a **valid strength comparison and an invalid difficulty claim**. Valid: any proof of F yields, in the same theory, a proof of a bound beyond current technology, so no *gap-estimate-based* route is near. Invalid as stated: a statement can imply something no current method delivers and still be provable by a method that never passes through the intermediate — the document's own S6 demonstrates the pattern, showing the smooth part is elementary and the difficulty is confined to the fluctuation.

The cost is not rhetorical. §2.1 elevates this to "**a hard gate on Branch P**", and §3.1 uses it to close S1/S2. The gate is justified by an asymptotic argument and is then applied to prune the entire P branch — including the effective-plus-finite join (Q1/H2) which is finite-range by construction and which the asymptotic argument does not touch. An asymptotic gate closing a finite-range route is the single most expensive mis-inference in the document.

**S9 "two independent reasons" — one reason, not two.** Magnitude is the FGKMT wall, identical to S3's (Q1). Localization is soft: Erdős–Rankin-style constructions *do* place the interval near an explicit modulus, and `π` there is estimable from the same explicit bounds P4 requires — so `n = π(p_n)` is recoverable to within the precision `T_n` needs. Localization is a nuisance, not a block. The verdict `not viable` survives; the "two independent reasons" does not, and it matters because it makes S9 look like an independently-blocked branch when it is S3 wearing a different archetype label.

**L4 "the only node here that is a genuine theorem" — false as stated.** L2 (F1 ⟺ F2 ⟺ F3, via rpow and log monotonicity) is a theorem and a non-trivial one in Mathlib. L5 (`F ↔ ∀n, g n < T n`) is a theorem. L6 is a conditional theorem. What §6 means is "the only node that is a theorem about a function rather than about the statement" — but that gloss inverts the value judgment, because L4 **contains no prime input at all**. It is a calculus lemma that would be true if primes did not exist. Nominating it as the primary deliverable optimizes the Lean legs for producing *a theorem*, not for producing a theorem about `F`.

**P6′ — mis-priced.** Tagged `[O]`, flagged as "a live correctness risk", and named in §9 as one of the two most-likely-wrong places. My numbers (Q5.1) say the dip amplitude is bounded and vanishing, and Q2(ii) says the obligation is pointwise, not path-dependent. Correct pricing: a corollary of P4 with slack O(1/L), cheap, downstream. This is the largest calibration error in the document, and unlike the two errors §8.8 records, it does not read as a slip — it reads as diligence.

**P5 `[C]`** is correctly tagged; the §2.3 gloss around it is what forecloses H2.

---

## Q7 — RANKING

Ranked weakest first. Each item carries a what-must-change clause and the finding it descends from. This tells the downstream DAG where **not** to spend compute.

**1. P6′ (§2.4) and the `notebooks` / `skeptic` legs aimed at it — the largest single misallocation.**
*From Q5.1, Q6, Q2(ii).* The document sends two legs at a node it has mis-priced. **What must change:** replace the obligation. Drop "prove `T_m ≤ T_n` whenever `m<n` straddle a record gap" — that asks for a special case of a statement that is false in general. Substitute the pointwise envelope `|T_n − (L_n² − L_n − 1)| ≤ c/L_n` with `c` explicit, which follows from P4 alone, needs no record-gap structure, and closes the reduction with a slack of O(1/L) against margins that my run measures at 5.3 (worst, `n ≥ 10`) rising to 47. Retire the 55.9% figure from §5.1 and replace it with the dip amplitude table. Estimated remaining work: a Dusart lookup, not a research leg.

**2. L4 as the nominated primary Lean deliverable (§6, §9).**
*From Q6, Q5.5.* A calculus lemma about a first-order model that discards the very term the threshold is made of. **What must change:** demote L4 to a supporting lemma and promote **L5** (`F ↔ ∀n, g n < T n`) to primary — L5 is the node that pins the object every other leg reasons about, and it is where a wrong reformulation would actually do damage. If L4 is kept as a headline, it must be restated against the second-order model `n(log n + log log n − 1)`.

**3. S9 (§3.9) — spend zero.**
*From Q6, Q1.* Not an independent branch; it is S3 relabelled, and its second blocking reason does not hold. **What must change:** collapse S9 into S3 as a remark, and correct §3.0's table, which currently shows two archetypes covered where one obstruction operates.

**4. S1 / S2 (§3.1, §3.2) — correctly closed, but the gate that closes them must be fenced.**
*From Q6, Q1/H2.* Do not spend compute on S1 or S2. **What must change:** P3's gate must be explicitly scoped to *gap-estimate-based* routes, so it cannot be inherited by the effective-plus-finite join. And §3.2's "not a disguised restatement" obligation needs a stated discharge criterion or it is decorative.

**5. §5.1's headline ratio statistic as the search instrument.**
*From Q5.2.* It decays like `0.9/n` and dies in double precision near `n ≈ 4·10¹⁵`, below the frontier the search leg is asked to pass. **What must change:** `ρ_n` becomes the reported statistic everywhere; the `n log p_{n+1}/((n+1) log p_n)` ratio is retired from §5.1 or annotated with its conditioning limit. Cheap fix, prevents a silent failure at exactly the scale that matters.

**6. S4's search objective as handed over in §3.4.**
*From Q3.* §4.3 already says "track `ρ_n`, not `g_n/L²`" — and then §3.4 offers the surrogate `g_n/(L²−L−1)` as an equivalent. It is not equivalent enough: it reorders my top-8 and inflates ρ by 2.7% at the tightest case. **What must change:** the surrogate is a candidate filter only; every reported ρ is computed against exact `T_n`, and no breach is certified from the surrogate.

**7. T3's tag (§4.3).**
*From Q4.* The re-derivation is right; the classification is over-strong. **What must change:** `[decidable, sufficient]` → `[each instance decidable, semi-decidable to find, sufficient conditional on P4]`, plus the note that the exceptional set is `{1..7, 10}` and is not a monotone threshold.

**8. R3 (§2, §4) — an empty node presented as a live one.**
*From Q1/H4.* Tagged `[O]` and never instantiated with a single consequence other than the gap bound. As it stands it is a placeholder that makes the R branch look two-wide when it is one-wide. **What must change:** instantiate it or retire it. Until then no leg should be pointed at it.

**9. Not a branch to defund — a prerequisite before this ranking is trustworthy.**
*From Q1.* §2's exhaustiveness claim is untagged and false. **P8** (independence), the **P4 ∧ P5 join**, and **R5** (conditional refutation) have no nodes. Until the tree can draw a conjunction, any ranking over it — including this one — is a ranking over a proper subset of the attack surface. The cheapest correction is also the most important: change §2's opening sentence from a claim of exhaustiveness to a claim of coverage, and let the three missing nodes exist even at `[X]`.

**Strongest parts, which should not be touched by any pruning:** §1.2's four-form equivalence (I verified the chain), §4.5's refusal to promote T5, §4.6's Littlewood exclusion (I re-derived the estimate and it is correct), and §1.4's Π₁/Σ₁ observation — which is the document's best idea and the one it under-uses, since P8 follows from it in one line.

Files: `attack/decompose.md`, `attack/probe.py`, `attack/probe2.py`.
