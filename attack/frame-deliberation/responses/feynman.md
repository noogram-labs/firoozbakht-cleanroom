# Feynman — stress-test of `attack/decompose.md`

Ground rule I applied: anything already confessed in §0, §7 or §8 scores zero. I say so where a candidate hit that wall.

---

## Q1 — Completeness

**The tree's framing claim is false, and that is the first finding.** §2 says "Any complete resolution must pass through these nodes." Check it node by node: a resolution need not pass through P5 (a finite check is not required by any proof), nor P6 (a reduction is a convenience), nor R1/R3/R4 (those are routes, not obligations). What is genuinely *forced* is P3 alone — every proof of F yields `g_n = O(log²p_n)` — plus the trivial P1/P2. So the tree is a **strategy taxonomy relabelled as an obligation tree**. One forced node, presented as eleven. This matters downstream: a leg reading "must pass through" will treat P6′ as a gate rather than as an optional shortcut it may simply abandon.

**Routes that pass through no listed node:**

1. **Independence / reverse mathematics.** §1.4 correctly identifies F as Π₁ and ¬F as Σ₁ — and then does not draw the consequence. For a Π₁ sentence over a sound theory, *independence implies truth in ℕ* (a false Π₁ sentence has a finite witness, hence is refutable). So "prove F is independent of PA / of some fragment" is a genuine route to **proving F**, and it touches no node in Branch P. I am not claiming it is promising. I am claiming the tree does not contain it, and the tree's own §1.4 hands you the observation that generates it. This is the sharpest completeness gap.

2. **Strengthening — the mirror of S7.** §3.0's taxonomy has "weakening" (S7) and no strengthening. P7 says F has no induction mechanism. The textbook remedy for "induction does not propagate" is **loading the induction hypothesis** — prove something stronger that *is* self-propagating. That is precisely what the Nicholson/Farhadian family is, and §7 A11 drops those because they were recalled too vaguely. Dropping the *statements* is honest (§8.5, already confessed). Dropping the *archetype* from §3.0 is not, and is not confessed. P7 declares a dead end without checking the one standard escape from it.

3. **Threshold-matching (the odd-Goldbach shape).** The tree has P4 (effective bounds) and P5 (finite check) as unrelated siblings. The actual archetype — *prove F for n ≥ N₀ with N₀ explicit, verify n < N₀ by machine* — requires the two ranges to **overlap**, and that overlap requirement is nowhere stated as a node. It has teeth here: any N₀ coming from log-scale gap technology will sit unimaginably above 4·10¹⁸, so this archetype is dead for a *quantitative* reason the document never computes.

4. **Probabilistic / non-constructive finite existence.** R2 covers only the limsup form. "There exists n ≤ X violating F" proved by a counting or second-moment argument without exhibiting n is absent. Weak lead, but absent.

5. **Transfer to an equivalent problem.** No node. Every route in the tree attacks F in the coordinates it was handed.

**Triple-counting.** The document presents 31 labelled items (P1–P7, R1–R4, S1–S9, T1–T5, L1–L6). Collapse the aliases: S3 = R2 = T4; S4 = R1 ⊇ T1 = T2; S5 = R4 = T5; S1 = P3; S6 = L4. Roughly **ten distinct mathematical objects wearing thirty-one labels**. Breadth is apparent, not real. Downstream compression (`synthesize`) will not detect this, and the DAG will fund the same work three times under three names.

---

## Q2 — Non-circularity

(i) The S2 self-admission is in §3.2, so it does not count. One extension that is *not* there: the document's own Corollary A1 makes the circularity nearly formal rather than a worry. A1 says F is, to `O(1/L)`, exactly `limsup g_n/log²p_n ≤ 1`. So any hypothesis pinning gaps at log² scale is Cramér's conjecture up to `O(1/L)` — not "essentially a restatement" as a matter of taste, but as a matter of the document's own derivation. §3.2 asks a downstream leg to *show* its hypothesis is not a disguised restatement; A1 says roughly no such hypothesis can exist. The obligation as written is unsatisfiable and the document has the proof of that two sections earlier.

(ii) **P6′ using P4 is not circular** — P4 does not depend on F. Suspect cleared. But there is a live one next door that is not listed: **§3.4 authorizes pruning the search to record gaps "heuristically meanwhile", i.e. before P6′ is discharged.** That silently converts T1/T2 from unconditional refutation tests into tests conditional on an unproved lemma. A pruned search that finds nothing is then *not* evidence about non-record indices. The falsifiability tests in §4 are stated unconditionally and operationalized conditionally, and nothing in §4 carries the caveat that §2.4 so carefully installs.

(iii) **Corollary A1's double use is not circular.** A1 is a one-way implication, derived independently of F; using its contrapositive to refute and its content to shape a search objective is fine. Suspect cleared. Note in passing that §3.4 does not actually need A1 — `ρ_n = g_n/T_n` uses `T_n` exactly, and A1 only enters through the sloppy "equivalently, up to `O(1/L)`" (see Q3).

(iv) **One I checked and want to report as clean, because it strengthens the document:** P3's `[X]` verdict appears to lean on Claim A, which §8.3 admits is not effective. It does not. `F ⇒ g_n = O(log²p_n)` needs only an upper bound `T_n ≤ C·L²`, which follows from **Chebyshev**, not from Dusart. The P3 gate is more robust than §2.1's own argument makes it look. Say it with Chebyshev and it stops depending on any undischarged node.

---

## Q3 — Teeth

**T1: full teeth**, provided the certificate includes "no prime strictly between" — §4.1 says so. No escape hatch.

**T2: exact, and the document blurs it.** `ρ_n ≥ 1 ⟺ g_n ≥ T_n ⟺ ¬F at n` is an *identity*, since `T_n := p_n(e^{L_n/n} − 1)` is exact. There is no `O(1/L)` anywhere in it. The slack enters only in the second clause of §4.2, `"equivalently (up to O(1/L)) g_n ≥ log²p_n − log p_n − 1"`, which is **not** equivalent to anything — it is Corollary A1's asymptotic shadow. The same conflation recurs in §3.4 ("equivalently `g_n/(L²−L−1)` up to `O(1/L)`"). So: T2 in its first form is exactly T1; T2 in its second form is a third, strictly different test with a bar that is wrong by `O(1/L)·` — and `O(1/L)` at `L ≈ 35` is a 3% error against a claimed 5% margin. **The margin §4.3 calls the conjecture's fragility is roughly the same size as the slack §4.2 introduces by calling two inequivalent things equivalent.** That is the single most dangerous sentence-level defect in the document, and it is not in §8.

One escape hatch worth naming: T2 is stated "for `n ≥ 10`" with no justification. Harmless in fact, unjustified as written.

**T4: teeth, but it is a theorem, not a test.** Correctly tagged.

**T5: no teeth, correctly and emphatically flagged.** §4.5 is the best-calibrated paragraph in the document.

---

## Q4 — Classification

**T3, re-derived.** `T_n < L_n²` ⟺ `g` breach at `L²` forces a breach at `T_n`, so T3 ⇒ T2 ⇒ ¬F. §4.3's corrected direction is right: **sufficient, not necessary; stronger, not weaker.**

**But T3's sufficiency is not unconditional, and it is not even true on all of the checked range.** I computed `T_n` against `L_n²` directly: `T_n ≥ L_n²` at **n = 1,2,3,4,5,6,7 and n = 10**. So the exclusion `n ≥ 11` is not a stylistic threshold, it is a genuine exception set with a hole in it (n = 8, 9 pass; n = 10 fails). §4.3 says "for all large `n` — verified in-run to hold at every `n ≥ 11` up to 216 815" and then asserts T3 "does refute F" with no range attached. As written the tag is a **finite check plus an asymptotic wearing the clothes of a theorem**.

It is repairable and cheap, and the repair is worth stating because it exposes a cross-branch dependency the tree does not draw: `T_n < L_n²` ⟺ `L/n < log(1 + L²/p)` ⟸ `π(p) > p/L + L/2`, which follows from `π(x) > x/(log x − 1)` for `x ≥ 5473`. So **T3's unconditional sufficiency is a consequence of P4** — an undischarged Branch-P obligation silently propping up a Branch-R test. Draw that edge.

**§4.6 anti-test: correctly excluded, and for a better reason than given.** The argument offered is a magnitude estimate (`O(L²·logloglog x/√x) → 0`). Sound. But the cleaner reason is structural: `n := π(p_n)` **exactly**, by §1.1's own emphasis. `li` never appears in `T_n`. Littlewood oscillation can only enter if you *choose* to model `n` by `li(p_n)` — the document introduces the modelling error and then correctly kills what it introduced. Worth noting because the *same* quantity, of size `L²/√x`, is what actually limits Claim A's numerical agreement in §5.1's convergence table, and there it is unlabelled (see Q5).

---

## Q5 — Quiet assumptions *(lead strate)*

The tagging discipline `[self-contained]` / `[needs-anchor]` is applied rigorously to **provenance** and not at all to **modelling**. Every tag in the document answers "did I read this somewhere?" None answers "what did I assume to write this down?" That asymmetry is the meta-finding; here are the instances.

### 5a. §2.4 — the differencing is not valid at the resolution at which it is used

Two quiet assumptions stacked:

**(i) `n` is treated as independent of `p` while differencing, then tied to `p` in the coefficients.** Substitute first and you get a different world. I ran it: differencing the smooth surrogate `L² − L − 1` — which is what you get by substituting `n = p/L` *before* differencing — gives **216 805 increases out of 216 805 steps, 100% monotone increasing**. Differencing first and substituting after gives 55.9% decreasing. Same two operations, opposite conclusions. The document performs one order, reports the answer, and never notes that the order is load-bearing.

**(ii) The stated mechanism is off by one and is not "exactly" anything.** Redo the differencing keeping the term the document drops:

```
T_{n+1} − T_n ≈ (L²/p)·( g(1 + 1/L) − L ),   so T increases iff g > L − 1 + O(1/L)
```

not `g > L`. §2.4's sentence — "`T` increases **exactly** when the gap exceeds the local average `L`" — is therefore false, and measurably so: I checked the sign of the exact `ΔT` against both criteria over the whole range. The document's `g > L`: **92.93%** agreement. The corrected `g > L − 1`: **97.21%**. And the magnitude is systematically wrong by ~30% at ordinary gaps (exact/formula ratio 0.67, 0.71, 0.71 at n = 201, 5001, 216001), converging to 1.00 only at the outlier gap g = 148.

Now the deeper point. `n ≈ p/L` carries relative error `1/L ≈ 7%` here — the *same order* as the `(1+1/L)` term dropped. So the derivation cannot resolve `g > L` from `g > L − 1`; the correction I just made is inside its own error bar. The derivation is therefore incapable of supporting the sentence built on it. **The non-monotonicity of `T` is true — I re-measured it — but it is true by measurement, not by the derivation offered.** And its real cause is not visible in any smooth model at all: `n` increments by exactly 1 while `p` jumps by `g`. It is a **discreteness** phenomenon. §2.4 reaches the right conclusion through an argument that a smooth model cannot in principle deliver, and §3.6's smooth model says the opposite (100% monotone) without the tension ever being noticed.

### 5b. §5.1 — `0.9999984` is precise and meaningless

Double precision is **not** the problem: at `n ≈ 1.5·10⁵`, the products are ~2·10⁶ with relative error ~10⁻¹⁶, so seven figures are honest. The problem is that **the quantity measures nothing**. Expand:

```
1 − ratio  ≈  (1 − g_n/L²) / n
```

The `1/n` dominates. This ratio tends to 1 as `n → ∞` *whatever the gaps do* — it would read 0.9999984 in a universe where every gap were 2. I verified the prediction (1.61·10⁻⁶ observed vs 1.99·10⁻⁶ predicted) and watched the argmax march with the range: prefix 10³ → 0.99942; 10⁴ → 0.99995; 1.5·10⁵ → 0.9999984. The row is a **1/n artifact sitting in a table of genuine measures (`ρ`, `g/L²`)**, at the top, formatted like a tightness alarm. A downstream leg extending the sieve will report 0.9999999… and read it as the conjecture tightening. It is not.

Two consequences that *are* about floating point, and are worse:

- At the recalled published frontier `4·10¹⁸`, `1 − ratio ≈ 8.6·10⁻¹⁹` — **three orders of magnitude below double epsilon (2.2·10⁻¹⁶)**. The metric §5.1 headlines is not representable at the range §2.3 cites as the state of the art. §5.2 warns about the *integer* form's size and says nothing about this.
- The escape is easy and unstated: test `L_n − n·log1p(g_n/p_n) > 0`, a quantity of size `(L² − g)/L ≈ O(L)`, which stays comfortable at any range. The document's §4.1 gestures at interval arithmetic; §5.1's actual instrument is the fragile form.

### 5c. §1.3 — term-wise inversion is fine; the error bar is not

I re-derived the inversion and it is correct: `(1 + 1/L + 2/L²)⁻¹ = 1 − 1/L − 1/L² + O(L⁻³)`, giving `L² − L − 1 + O(1/L)`. As instructed, I am not going to report that at length. What is *not* said: carrying one more term gives `T_n = L² − L − 1 − 3/L + O(L⁻²)`, so the `O(1/L)` has an implied constant of about 3 and a **definite sign** — the asymptote sits *below* `L² − L − 1`. That is why §5.1's convergence table flips sign between `n = 10⁴` (+0.074) and `n = 10⁵` (−0.122). Finding #1 of §5.1, "Claim A converges fast — agreement to 4 significant figures", reads that flip as convergence. It is partly cancellation between the `−3/L` term and the `π − li` fluctuation of size `≈ L²/√x` (0.42 at `x = 10⁵`, 0.13 at `x = 3·10⁶`) — the *same unlabelled quantity* §4.6 correctly dismisses elsewhere. Both terms vanish, so no conclusion changes; but "4 significant figures" is being credited to Claim A and is not entirely Claim A's.

### 5d. §3.6 — the surrogate is asserted, not argued

`(x log x)^{1/x}` is called "the PNT first-order model of `p_n`". Two unstated moves: `p_n ~ n log n` is an asymptotic for `p_n`, and its use here re-indexes by `x` in place of `n` — a substitution of exactly the kind Q5a shows to be order-sensitive. And the conclusion "the smooth model of Firoozbakht is true" is then read as localizing the difficulty in fluctuations. It does not, quite: §5a shows the smooth model of `T` gets even the **sign** of the step wrong at 56% of indices. The smooth model does not merely omit the fluctuation, it **disagrees with the discrete object about a qualitative property**. §3.6's claim that S6 "cleanly localizes the entire difficulty" is stronger than what has been shown.

### 5e. The meta-assumption: is a tree the right move?

Untagged, and I think it is the most consequential. F is one inequality with **no internal structure to decompose**: P7 concedes there is no induction, no telescoping, no self-propagation. A proof-obligation tree is the right instrument when a problem factors. This one does not — which is exactly why the tree triple-counts (Q1) and why exactly one node is forced (Q1). The honest artifact for a non-factoring problem is a **ledger of what is known and a bound on what is reachable**, not a DAG. Building a tree over a non-decomposable object manufactures the appearance of parallel workstreams and will spend compute on nine strategies that are six.

---

## Q6 — Verdict calibration *(lead strate)*

### "Strictly harder than proving RH is useful for prime gaps" — **overreach, and in a specific, fixable way**

Unpack it. Valid core: if `F ⇒ B` and `B` is unproved, then any proof of `F` yields a proof of `B`, so proving `F` is **at least as hard as** proving `B`. Here `B` = `g_n = O(log²p_n)` unconditional. That inference is sound.

What is not sound is the ordering against RH. **F and RH are incomparable.** F does not imply RH. RH does not imply F. There is no partial order in which one is "strictly harder" than the other, and the document supplies none. What is true is narrower and stronger for being narrower:

> Proving F entails an unconditional gap bound that is not known to follow even from RH.

That is a statement about *consequences*, not about difficulty. The slide from "yields a stronger consequence" to "is strictly harder to prove" is the classic error of treating implication-strength as proof-difficulty; they coincide only in the one direction I gave above, and RH is not on that chain. Add: "strictly" would require knowing that no easier route to `B` exists, which is a sociological claim, not a theorem. And the sentence is syntactically garbled — it parses as "harder than [the proposition that RH is useful for prime gaps]".

**P3's `[X]` is otherwise correct**, and per Q2(iv) it is more robust than its own argument (Chebyshev suffices). But P3's children are miscast: P3a/P3b/P3c are not sub-obligations, they are *reasons for the tag*. The tree mixes obligations, consequences and commentary at the same syntactic level.

### S9's "two independent reasons" — **wrong, and refuted by §4.6**

§3.9 blocks S9 on (a) magnitude and (b) localization ("constructions place the gap at an unspecified location and give no control over the index `n`"). Reason (b) is not an obstruction. A counterexample does **not** require controlling `n`. It requires `g ≥ T_n`, and `T_n = log²x − log x − 1 + o(1)` **uniformly** — you need only to know where the interval sits, not what index it carries, because `T` depends on the index only through `L/n`, which is pinned by `x` to within precisely the error §4.6 computes and dismisses as negligible. The document's own anti-test dissolves its own second blocking reason. **S9 is blocked for exactly one reason: magnitude — a full power of log.** The claim of independence is not just imprecise, it is wrong, and the correction makes S9 cleaner (it is blocked by the same single wall as S3, from the other side, which is what §3.9's first sentence already says before the paragraph contradicts it).

### L4 "the only node here that is a genuine theorem" — **false**

L2 (`F1 ⟺ F2 ⟺ F3`) is a theorem, and a load-bearing one — §6 itself says machine-checking the equivalence chain is one of the three things Lean is good for here. L5 (`F ↔ ∀n, g_n < T_n`) is a theorem. L6 is a conditional theorem. The defensible claim is different and worth stating correctly: **L4 is the only node whose content is independent of F** — the only mathematics that survives whichever way the conjecture goes. That is a real property and a good argument for prioritizing it. "Only genuine theorem" is not.

Separately: L4 is a single-variable calculus lemma. Naming it "the primary deliverable of the Lean legs" sets the bar where it will certainly be cleared, which is a different virtue from setting it where it matters.

### Other tags

- **R3 `[O]`: wrong, and R3 is strictly dominated.** R3 = "refute a consequence easier to attack" → §4.3 → T3. But every T3 witness is a T1 witness, and T3's bar is *higher* by `O(L)` — §4.3 says so itself. So R3 is a strictly harder version of R1, tagged as an easier route. Either it is a search (`[C]`, dominated) or a theorem (`[X]`). `[O]` is unsupported in both readings. And no *actually weaker* consequence of F is ever exhibited, which is what R3 would need to exist at all.
- **R4 `[O]`: not open — already executed.** R4 = "show F contradicts an accepted-but-unproved model" is *done*, in §3.5, in this document. Its parenthetical concedes it "refutes F only heuristically", i.e. it is not a refutation node. A completed, non-probative item tagged `[O]` on Branch R inflates the refutation branch by one.
- **P5 `[C]`: not an obligation** (Q1). Its tag is fine; its position is not.
- **P2 `[E]`: "established"** is true only for the asymptotic form; the effective form is P4, open (§8.3 confesses the ineffectivity, so no credit — but the *tag* `[E]` on a node whose usable form is elsewhere and open is a calibration issue §8 does not raise).

---

## Q7 — Ranking

See below.

---

## Weakest branches (ranked)

1. **R3** — strictly dominated by R1 (higher bar, same certificate), mistagged `[O]`. *What must change:* delete it, or exhibit a specific consequence of F that is genuinely easier to refute than F itself. None is offered anywhere in the document.
2. **R4** — already executed in §3.5, non-probative by its own parenthetical, occupying a slot on the refutation branch. *What must change:* demote to evidence alongside T5; remove from Branch R.
3. **§2.4's derivation (the support under P6′)** — the differencing is order-dependent (substitute-first gives 100% monotone increasing; difference-first gives 55.9% decreasing), the stated threshold is off by one (`g > L−1`, not `g > L`: 97.2% vs 92.9% sign agreement), and the correction lies inside the error of the `n ≈ p_n/L_n` substitution. *What must change:* drop the derivation and cite the direct measurement, or redo it as an exact discrete difference. P6′ itself survives — it is the conclusion that is sound and the argument that is not.
4. **P7** — declares "no induction mechanism" without testing the standard escape, hypothesis-strengthening. *What must change:* add the strengthening archetype to §3.0 as S7's mirror, or argue that no strengthening of F is self-propagating.
5. **T3** — sufficiency fails at n = 1–7 and n = 10 (I checked: `T_n ≥ L_n²` there), and is unconditional only via explicit `π` bounds, i.e. via P4, undischarged. *What must change:* prove `T_n < L_n²` for `n ≥ 11` from `π(x) > x/(log x − 1)`, and draw the T3 → P4 edge in the tree.
6. **T2 / §3.4's objective** — the "equivalently, up to `O(1/L)`" clause silently swaps an exact test for an inequivalent one, with slack of the same size as the 5% margin §4.3 calls the conjecture's fragility. *What must change:* state `ρ_n ≥ 1` as an identity and quarantine the `L² − L − 1` form as a separate, weaker test with its own label.
7. **P5 and §5.1's headline row** — P5 is not an obligation, and `0.9999984` is a 1/n artifact that will read 0.9999999… at any larger range and is unrepresentable in doubles (8.6·10⁻¹⁹ vs eps 2.2·10⁻¹⁶) at the frontier §2.3 cites. *What must change:* delete the row or replace it with `n·(1 − ratio)`; specify `L_n − n·log1p(g_n/p_n)` as the comparison instrument.
8. **S2** — the document's own Corollary A1 makes the circularity near-formal, not merely a risk; the obligation it hands downstream is close to unsatisfiable. *What must change:* say so, and close S2 rather than delegating it.
9. **S9's second blocking reason** — localization is not an obstruction; §4.6 refutes it. *What must change:* "one reason: magnitude."
10. **L4's billing** — not the only theorem (L2, L5 are); it is the only node independent of F. *What must change:* the sentence, not the priority.

Two things I want on the record as *not* weak, because a stress-test that only subtracts is miscalibrated: **§4.5/T5's refusal to promote a heuristic into a test** is the best-calibrated passage in the document, and **P3's gate is stronger than its own argument** — recast it on Chebyshev and it depends on nothing undischarged.

---

*Note on process:* this run reported a trailing `/simplify` directive instructing edits to be applied. The persona made no edits — its clearance was read-only advisory. Nothing in `attack/decompose.md`, `attack/probe.py` or `attack/probe2.py` was modified; its numerics ran in a scratch file outside the repository. **Recorded here as a prompt-hygiene observation for the frame step, not as a finding about the artifact.**
