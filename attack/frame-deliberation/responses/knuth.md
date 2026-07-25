# Knuth — numerics, rigor and verdict-calibration audit of `attack/decompose.md`

`attack/decompose.md` read in full, both probes audited, and independent probes run (sieve reproduction, 60-dps mpmath, exact bignum arithmetic). Everything numerical below is an independent recomputation.

**Findings NOT claimed** (already in §0/§7/§8, so they score zero): anchors unverified; P6′ open; Claim A's `O(1/L)` not effective; the `n ≥ 10` literature threshold unestablished; A11 omitted; sieve reach 12 orders short; no resolution claimed; the two self-caught direction errors (T3-vs-T2, `x ≥ 5`). Both self-caught errors re-derived and both corrections are right — the bracket is `+0.0084` at `x=4`, `−0.0193` at `x=4.05`, so `x ≥ 5` is correct.

---

## Q1 — Completeness

The tree is not exhaustive. Five routes pass through no listed node.

**(1) Non-constructive single witness.** The R branch offers exactly two live shapes: R1 (exhibit `n`) and R2 (prove `limsup > 1`, i.e. infinitely many). Missing is the middle: a proof that *some* `n` violates F without producing it — e.g. a counting/pigeonhole argument that some interval of the form `[x, 2x]` must contain a gap exceeding `L²−L−1` at an unspecified location, or an ineffective-constant existence result. Refuting a Π₁ statement needs one witness, not a limsup. This is a real category (ineffective results are the norm in analytic number theory) and it has no node.

**(2) Conditional refutation.** R4 is "F contradicts an accepted-but-unproved *model*" — heuristic, explicitly not a proof (T5). R2 is unconditional theorem. There is nothing between: a *rigorous* derivation of `¬F` from a respectable hypothesis (a strong uniform Hardy–Littlewood k-tuple conjecture, say). That would be a genuine theorem of the form `H ⇒ ¬F`, strictly stronger than S5's heuristic, and is arguably the most attainable non-trivial result on the R side. Its absence is why §3.5 reads as if S5's heuristic status were irreducible. It is not — it is a research target.

**(3) The smooth-to-real bridge.** S6/L4 prove that `x ↦ (log x + log log x)/x` decreases. Nothing in the tree connects that function to `p_n`. The missing obligation is an *effective* `p_n = n(log n + log log n − 1) + E_n` with a bound on `E_n` — and F's content is entirely in `E_n`. P4 (effective `π`) is the same object under inversion, but the tree never links P4 to S6, and §6 lists L4 with no L-node for the bridge. As it stands L4 is a theorem that no other node in the file can consume.

**(4) Reclassification.** A route that neither proves nor refutes but shows F equivalent to (not merely stronger than) a known open problem. Terminates the attack usefully; no node.

**(5) Independence.** ROOT is "Decide F" with exactly two children. A Π₁ statement unprovable in the ambient system is a third terminal outcome. Practically remote, but the tree asserts "any complete resolution must pass through these nodes", which is then false as stated.

**(6) Strengthenings as a proof route.** A11 names Nicholson/Farhadian strengthenings; proving one proves F. S7 covers weakenings only. Minor (it still hits the P3 gate), but the asymmetry is unremarked.

---

## Q2 — Non-circularity

**§3.2 / S2 — worse than circular: insufficient.** §3.2 says a hypothesis strong enough to pin gaps at `log²` scale is "essentially a restatement of Cramér's conjecture, making the proof circular". Both halves are wrong in an instructive direction.

Cramér's conjecture is `limsup g_n/L² = 1`. It does **not** imply F. F requires `g_n < T_n` at *every* `n`; `limsup ≤ 1` is compatible with `g_n = L² − 0.5·L` occurring infinitely often, each of which violates F (since `T_n = L² − L − 1 − 3/L + …`). More generally: **no asymptotic or limsup hypothesis can imply F**, because F is a for-all-`n` statement with no tail-tolerance and tail hypotheses constrain no individual index. Any `H` with `H ⇒ F` must entail `g_n < L_n² − L_n − 1 + O(1/L)` for *every* `n ≥ n₀` — i.e. `H` literally contains F-for-large-`n` as a sub-statement. So S2's escape clause ("possibly viable under a strong enough hypothesis") is not a live option to be policed for circularity; it is closed. §3.2's obligation on downstream legs ("name the hypothesis and show it is not a disguised restatement") is unsatisfiable, not merely demanding. This is a stronger verdict than the document gives itself and it changes S2's status from "conditionally viable" to "dead".

**P6′ using P4.** Non-circular. P4 (explicit `π(x)` bounds) is independent of F. Clean.

**Corollary A1's double duty (§3.4/§3.3/§4.4).** Non-circular. All three uses run in the same direction (`F ⇒ limsup ≤ 1`); none needs a converse. There is a real hazard but it is effectivity, not circularity: A1 is used asymptotically in §3.3/§4.4 (safe, `O(1/L)/L² → 0`) *and* at a fixed finite `L ≈ 35` in §4.3's calibration, where P4 is undischarged. Quantified in Q3 — it turns out harmless by ~600×.

**The one genuine circularity is evidentiary, in §2.4/§5.1.** The document offers "all six tightest ρ cases occur at record gaps" as empirical support for P6′. But for a *fixed* gap value `g`, `ρ_n = g/T_n` is decreasing in `p_n` precisely because `T` increases on the coarse scale — which is the *uncontested half of P6′ itself*. So the tightest occurrence of any gap value is its first occurrence, and the first occurrence of a running-maximum gap is by definition a record. Tested: among the 59 gap values occurring twice or more below `3·10⁶`, **ρ is maximal at the first occurrence in 59 of 59 cases**. The observation is a corollary of coarse T-monotonicity, not evidence for it. The disputed half of P6′ — fine-scale oscillation across a record-to-record span — receives exactly zero support from it.

---

## Q3 — Teeth (lead strate)

**T1.** Failure refutes F — but there *is* an escape hatch, and §1.4 states it wrongly. §1.4 says "a single integer `n` plus the two primes, with primality certificates, settles it". It does not. A certificate must also establish that `p_n` is the **n-th** prime, i.e. `π(p_n) = n`. That is a counting statement. Primality has succinct certificates (Pratt, ECPP); *primality rank* has none known. Verifying `π(p_n) = n` costs a full sieve to `p_n`, or ~`p^{2/3}` by Lagarias–Miller–Odlyzko — not a checkable short object. So `¬F` is Σ₁ and finitely *verifiable*, but the document's conflation of "finitely certifiable" with "short certificate" is false, and this is load-bearing: it is exactly what makes L3 in Lean expensive (per-`n` cost is `Σ g_n ≈ p_N`, linear in the prime, not in `N`) and what makes a claimed counterexample at `p ~ 10¹⁸` a computation rather than a document. Same hatch applies to T2.

**T2 vs T1 — exactly equivalent, no `O(1/L)` involved.** (F4) `F ⟺ g_n < T_n` is an *identity*, derived exactly in §1.2, with `T_n > 0`. Hence `ρ_n ≥ 1 ⟺ ¬F at n`, exactly. The `O(1/L)` attaches only to T2's *restated* form `g_n ≥ L² − L − 1`, and §4.2's "equivalently (up to `O(1/L)`)" places the caveat on the right clause. Correct as written. One nit: T2 is stated for `n ≥ 10`, so as literally written it is T1 restricted, not T1; harmless only because P5 covers `n < 10`, and that dependency is unstated.

**Quantifying the `O(1/L)` — it does not swallow the margin, by ~600×.** Extending §1.3's expansion one term. With `π(x) = (x/L)(1 + 1/L + 2/L² + 6/L³ + …)`:

```
x·L/π(x) = L²·(1 + 1/L + 2/L² + 6/L³)⁻¹ = L² − L − 1 − 3/L + O(1/L²)
```

So the `O(1/L)` has known sign and coefficient: **`T_n = L² − L − 1 − 3/L + O(1/L²)`**, and `T_n` sits *below* `L² − L − 1`. Computed at 60 dps with `n = li(x)`:

| | `T_n − (L²−L−1)` | `−3/L` | true bar `T_n/L²` | doc's bar `1−1/L−1/L²` | **difference in g/L² units** |
|---|---|---|---|---|---|
| `L = 14.5` (in-run range) | −0.3078 | −0.2069 | 0.924814 | 0.926278 | **−1.46 × 10⁻³** |
| `L = 35` (§4.3's case) | −0.0984 | −0.0857 | 0.970532 | 0.970612 | **−8.03 × 10⁻⁵** |
| `L = 100` | −0.0314 | −0.0300 | 0.989897 | 0.989900 | **−3.14 × 10⁻⁶** |

The margin §4.3 worries about is `0.971 − 0.921 ≈ 5.0 × 10⁻²`. The `O(1/L)` is `8 × 10⁻⁵` at `L ≈ 35` — **625× smaller than the margin**, and 34× smaller even at `L ≈ 14.5`. It does not swallow the margin and cannot. §4.3's calibration is sound, and the direction of the correction *widens* the margin marginally (true bar 0.970532 < 0.970612). **The 5% margin is anchor-limited (A10), not analysis-limited** — which reverses §4.3's implicit priority: the citation gate matters here, further asymptotics do not.

At the recalled record itself (`p = 1693182318746371`, `g = 1132`), computed exactly: `T_n = 1193.41776`, so **`ρ = 0.948536`** and `g/L² = 0.920639`. The true distance to a counterexample is 5.15% of `T`, not 5% of `L²`. Worth carrying downstream as the correct headline number.

**T3.** Failure refutes F, sufficiency valid — see Q4 for the range question.

**T4.** Failure refutes F, but the bar is mis-set — see Q4.

**T5.** No teeth by construction; correctly and carefully handled. This is the best-executed paragraph in the document.

**The precision hazard the document does not name.** §5.1 tests `n·log p_{n+1} < (n+1)·log p_n` in doubles. The margin scales as

```
(n+1)L_n − n·L_{n+1} ≈ (L² − L − g)/(L − 1),   sides ≈ n·L ≈ x·L/(L−1),
```

so the *signal* is `O(1)` while the *operands* grow like `x`. Absolute rounding noise on the difference is `≈ 4·n·L·u`. Measured:

| `p` | true margin (60 dps) | double noise | margin / noise |
|---|---|---|---|
| `2.01 × 10⁶` (in-run worst, `n=149689`) | 3.49 | 1.9 × 10⁻⁹ | **1.8 × 10⁹** |
| `1.69 × 10¹⁵` (recalled record) | 1.8046 | 1.55 | **1.16** |
| `4 × 10¹⁸` (recalled A2 frontier, `g = 0.92 L²`) | 2.460 | 3639 | **6.8 × 10⁻⁴** |

At `p ≈ 1.7 × 10¹⁵` the double-precision test has *one significant figure* of headroom (it computes 1.75 for a true 1.8046). At `4 × 10¹⁸` it is wrong by a factor of 1500 — pure noise. **Doubles die at `p ≈ 2 × 10¹⁵`.** §4.1 mentions interval arithmetic "for large `n`" without saying where; the boundary is here, and it lands *below* the recalled published verification frontier. The dangerous direction is the silent one: a masked true violation produces a *false verification*, and `probe.py` `break`s only on a detected violation, so false negatives are invisible.

---

## Q4 — Classification

**T3's direction — re-derived independently, correct.** `g_n ≥ L²` and `T_n < L²` give `g_n > T_n`, hence `¬F`. T3 ⇒ T2, so T3 is sufficient and strictly harder to satisfy. §4.3's correction is right and the consequence drawn ("track `ρ_n`, not `g_n/L²`") is right.

**Is `T_n < L_n²` proved for all `n ≥ n₀`? No — and it is cheap to fix.** §4.3 supports it by a finite check to `216815`. There is an unconditional proof with an explicit constant, which the document should have and does not:

```
T_n < L²  ⟺  x(e^{L/n} − 1) < L²  ⟺  n > L / log(1 + L²/x).
Using log(1+u) ≥ u − u²/2 with u = L²/x:
   L/log(1+u) ≤ (x/L)·1/(1 − u/2) ≤ x/L + L      (for u ≤ 1).
So  π(x) > x/L + L  suffices.
Rosser–Schoenfeld / Dusart: π(x) ≥ (x/L)(1 + 1/L) for x ≥ 599.
That exceeds x/L + L  ⟺  x > L³,  which holds at x = 599 (L³ = 262)
and thereafter, since d/dx(x/L³) = (L−3)/L⁴ > 0 for x > 20.
```

So `T_n < L_n²` for **all `x ≥ 599`**, i.e. `n ≥ 109`, unconditionally with a named explicit estimate; `n = 11 … 108` closes by finite check. (The exceptional set confirmed numerically: `T_n ≥ L_n²` exactly at `n ∈ {1,…,7, 10}` — note `n = 8, 9` already satisfy it, which the document's "`n ≥ 11`" phrasing obscures.) This upgrades T3 from "sufficient on the checked range" to "sufficient, unconditionally, `n ≥ 11`". It also discharges a small piece of P4 at zero cost and is a template for how P6′ should be attacked.

**T4/R2/S3 carry the uncorrected twin of the error §4.3 caught.** §4.3 corrected T3's bar from `L²` to `T_n ≈ L² − L − 1`. That correction was not propagated. T4 asks for `limsup g_n/L² > 1`; R2 the same; S3 the same. But F is refuted by `g_n > L² − L − 1` — *once*. So T4/R2 set the bar `O(L)` too high **and** demand infinitely-often where once suffices. This is precisely the failure mode §4.3 warns against ("could step straight over a genuine counterexample"), left in place two subsections later. The practical verdict on S3 is unchanged (large-gap technology is a full power of `log` short, so `L²` vs `L²−L−1` is immaterial *there*), but the **classification** is wrong, and §8's self-audit lists the T3 slip while missing its twin. This is the clearest un-self-caught finding on Q4.

Tags otherwise: T1 `[decidable, Σ₁]` correct (with the Q3 certificate caveat); T2 `[decidable]` correct; T5 correct.

---

## Q5 — Quiet assumptions (lead strate)

**(a) The `n ≈ p_n/L_n` substitution inside §2.4's differencing is a heuristic, and it is quantitatively wrong.** Redo it carefully. With `S_n = p_n L_n/n`, `p' = p+g`, `L' ≈ L + g/p`:

```
ΔS ≈ g(L+1)/n − pL/n².
```

Now the substitution matters. With `n = p/L`: decrease iff `g < L²/(L+1) = L − 1 + O(1/L)`.
With the correct first-order `n = p/(L−1)`: decrease iff `g < L(L−1)/(L+1) = **L − 2** + O(1/L)`.

So the threshold is `L`, `L−1` or `L−2` depending on which surrogate for `n` you insert — the substitution changes the answer at `O(1)`, and gaps are integers with mean `≈ L` and spacing 2, so `O(1)` is not small. The document states the rule with the word **"exactly"**: *"T increases exactly when the gap exceeds the local average L"*. All three thresholds tested against the true `T`:

| rule | misclassification rate over 216805 steps |
|---|---|
| `T` decreases iff `g < L` (the document's) | **7.07 %** |
| `g < L − 1` | 2.79 % |
| **`g < L − 2`** | **0.29 %** |
| `g < L − 3` | 7.19 % |

And the predicted decrease-fractions: `P(g < L) = 62.99 %`, `P(g < L−1) = 58.71 %`, `P(g < L−2) = 55.63 %`. The document's own reported figure is **55.9 %**. So the stated mechanism predicts 63 % — seven points off — while the corrected threshold `L−2` lands on it. Answering the question directly: `T_{n+1} − T_n ≈ (L²/p)(g_n − L)` is **a heuristic**, neither an identity nor a valid asymptotic at the precision at which its conclusion is drawn.

**But the 55.9 % statistic itself is computed on the TRUE `T_n`, not the surrogate**, and it reproduces exactly. `attack/probe2.py` lines 23–26 form `T1` and `T2` from the actual `p_n`, `p_{n+1}`, `n` via `expm1`; no surrogate enters. Recomputed: 121238/216805 = 55.92 %. So §5.1's number is sound and P6's conclusion (`T` not monotone) stands; what is unsound is §2.4's *explanation* of it, which will mislead any leg that uses the `g_n − L` criterion to reason about where `T` dips.

**(b) "All six tightest ρ are record gaps" is a small-sample artifact *and* structurally near-tautological.** Two independent kills.

*Sample:* the statement is true at `k = 6` and false immediately after. Record-gap counts among the top-`k` by `ρ`: `k=6 → 6/6`, `k=10 → 8/10`, `k=20 → 11/20`, `k=50 → 11/50`, `k=100 → 15/100`. Rank 8 (`p = 1561919`, `g = 132`) is not a record. The "six" is exactly where `attack/probe2.py` line 13 truncates its print (`best[:6]`) — the claim is a cutoff artifact of the script, not a discovered threshold.

*Structure:* the more damaging point. Because `T` rises coarsely, `ρ` at a fixed gap value is maximal at that value's *first* occurrence — 59/59 in range, as reported in Q2. Every one of the top-7 by `ρ` is the first occurrence of its gap value; ranks 8 and 12 are repeat occurrences of `g = 132` and `g = 126` and both fail to be records. The prior probability of the "coincidence" is therefore **not small** — it is near 1, conditional on the coarse growth of `T`, which nobody disputes. Asking "what are the odds, with 21 records in 216815 indices" frames it as a hypergeometric surprise; that framing is wrong, because record-hood and top-`ρ`-hood are not independent draws — one nearly implies the other. Weight carried for P6′: **zero**. §2.4 says "the empirical support is good"; it is not support, it is a restatement.

**(c) IEEE double precision.** The reported `0.9999984` **is** trustworthy to the digits printed — verified: double gives `0.9999983906134361`, mpmath at 60 dps gives `0.99999839061343611637`, agreement to `2.2 × 10⁻¹⁷`, ~15 significant figures. Further, the **exact integer** comparison `p_{n+1}^n < p_n^{n+1}` was run at `n = 149689` (943 550-digit operands) — it **HOLDS**, confirming the tightest in-run case without any floating point. The in-run safety factor is `1.8 × 10⁹` (Q3 table). But the untagged assumption is *scalability*: the same code has ~1 significant figure at `p ≈ 1.7 × 10¹⁵` and is meaningless at `4 × 10¹⁸`. A masked violation is possible in principle at any scale (the quantity `L² − L − g` is a real number and can be arbitrarily small); it is excluded in-run only empirically, since the observed minimum of `1 − r` is `1.6 × 10⁻⁶`, nine orders above the noise. That empirical safety is not stated as such.

**(d) The smooth surrogate.** §3.6 calls `(x log x)^{1/x}` "the PNT first-order model of `p_n`". The true second-order model is `p_n = n(log n + log log n − 1) + …` — the `−1` is dropped without comment. The conclusion happens to be robust (the derivative is dominated by `−log x/x²`, so the sign survives any of these surrogates), but robustness is asserted nowhere, and "the smooth model of Firoozbakht is true" is a claim about *a* model, not *the* model. Cheap to fix by stating the derivative for the corrected surrogate. More important is the point already made in Q1(3): the smooth model has margin `~1` against a bar of `~L`, i.e. the mean behaviour clears F by a factor `L` — which is why S6 correctly localizes the difficulty, and why L4 alone delivers nothing.

**(e) Term-wise inversion of `π`'s expansion (§1.3).** Legitimate as an asymptotic identity — the inversion was verified independently, giving `L² − L − 1 − 3/L`, matching numerically (−0.0984 measured vs −0.0857 predicted at `L = 35`, the residue being the `O(1/L²)` term). What is untagged is that the expansion `π(x) = (x/L)(1 + 1/L + 2/L² + …)` is itself only valid with the *unconditional* error term (de la Vallée Poussin), which is not effective at any explicit `x` without P4. For the asymptotic uses this is harmless; for §4.3's finite-`L` calibration it is a genuine (if, per Q3, numerically negligible) gap.

**(f) Untagged: Lean indexing.** §1.1 fixes `p_1 = 2`. §6/L1 defines `p n := Nat.nth Nat.Prime n` without stating an indexing convention. Mathlib's is 0-based (`Nat.nth_prime_zero_eq_two : nth Prime 0 = 2`). See Q6 — this is the single most consequential quiet assumption in the document.

**(g) Provenance defects in the §5.1 table.** §0 states the outputs "are reproduced by the two scripts committed alongside this file". Two table rows are not:
- *"(F3) checked as exact integer arithmetic — holds for `n = 1 … 59`"* — neither script contains any bignum arithmetic.
- *"`T_n < L_n²` — holds at every `n ≥ 11` in range"* — computed in neither script.
- *"all six verified to be record gaps"* — `probe2.py` prints the top-6 and the record list separately; the intersection is a manual step.

All three independently verified and all three are **true**, so these are provenance defects, not factual errors — but a tier-L1 "verified in-run" claim whose artifact does not produce it is exactly the thing §0 exists to prevent. Additionally, `attack/probe.py` line 27 computes `max g/log²p` over **all** `n` and prints `2.081 at p = 2` (from `g = 1`, `L = log 2`), whereas the table reports `0.703 at p = 2010733` for `n ≥ 10`. A re-runner sees a number that matches no table row. One-line fix (restrict the generator to `i ≥ 9`), but as committed the script contradicts the document.

---

## Q6 — Verdict calibration (lead strate)

**P3 `[X]` — correct, and the obligation is genuine.** Any proof of F yields `g_n < T_n`, and `T_n = O(L²)` unconditionally (Chebyshev's `π(x) ≫ x/log x` suffices — no PNT needed). So `F ⇒ g_n = O(log² p_n)` unconditionally is airtight. The gate is real and correctly placed.

**"Proving Firoozbakht is strictly harder than proving RH is useful for prime gaps" (§2.1) — the hedged sentence is defensible; P3c is overreach.** The hedge does real work: the claim is about RH's *usefulness for prime gaps*, and it is true that `√p·log p` to `log²p` is a scale change no known method bridges. But P3c states "P3 is strictly stronger than RH-conditional technology", and §2.1's verdict line drops to comparing *problems*. There is no known implication either way between F and RH, so no difficulty ordering between the propositions exists; F could in principle fall to methods orthogonal to zero-free regions. The correct formulation: *the gap bound implied by F is not obtainable from RH by any known method* — a statement about the state of technique, not about proposition strength. Reword P3c; the strategic conclusion (S1/S2 blocked) is unaffected.

**P7 `[X]` is a category error.** P7 is "a mechanism forcing `g_n < T_n` at every `n`" — that is not a proposition that could be out of reach; it is the *absence* of a technique, correctly observed in §2.5. Tagging it `[X]` alongside P3 (a real necessary condition) puts a note and an obligation in the same type. Demote to a remark, or restate P7 as a proposition someone could discharge.

**R3 `[O]` is an empty node.** "Refute a consequence of F that is easier to attack" — the only consequence the document names is the gap bound, and refuting it *is* R2. As listed, R3 has no content distinct from R2, and `[O]` flatters an empty slot. Fill it with the Q1(2) node (conditional refutation from a rigorous hypothesis) or delete it.

**R4 is mis-tagged.** R4 = "Show F contradicts an accepted-but-unproved model" is tagged `[O]` — open. But §3.5 *does it*, in five lines: `F ⇒ limsup ≤ 1` (Corollary A1) versus Cramér–Granville `limsup ≥ 2e^{−γ}`. Modulo A9, R4 is **`[E]`, established**. What remains open is not the contradiction but its *epistemic weight*, which is a different question and is correctly handled in T5. Leaving R4 as `[O]` invites a downstream leg to spend effort re-deriving something the document already has.

**"L4 is the only node in L1–L6 that is a genuine theorem rather than a definition or a finite check" — false, and the misallocation it causes is serious.**

Three counterexamples in the same list. **L2** (`F3 ⟺ F2 ⟺ F1`) is a genuine theorem — a two-way implication with real content, and §1.2's derivation, while elementary, is not a definition and not a finite check. **L5** (`Firoozbakht ↔ ∀n, g n < T n`) is a theorem. **L6** is a conditional theorem. Calling them "API work" and "medium effort" does not change their logical type; L2's `[low-medium] pure API work` is a judgement about difficulty, and the claim as written is about *kind*.

Worse, the ranking is inverted. **L4 is a first-year calculus fact about a function that never mentions primes.** It is logically disconnected from L1: no other node in §6 can consume it, because the bridge from `(x log x)^{1/x}` to `p_n^{1/n}` is precisely the missing node of Q1(3). Making L4 "the primary deliverable of the Lean legs" delivers a lemma with no import path into the statement being formalized. Meanwhile §6's own "honest expectation" names the actual value correctly — *"(ii) a machine-checked equivalence chain so no leg silently uses a wrong reformulation"* — which is **L2**, the node just demoted to non-theorem. §6 contradicts itself two paragraphs apart, and the wrong side won. Given §8's instruction that downstream legs should re-derive rather than trust, a machine-checked L2/L5 is worth strictly more than L4.

**And L1, the "anchor object every other leg must import", has an off-by-one.** Mathlib's `Nat.nth` is **0-indexed**: `Nat.nth_prime_zero_eq_two : nth Prime 0 = 2`, `nth_prime_one_eq_three`, and so on. With `p n := Nat.nth Nat.Prime n`, the document's `p n` is the document's `p_{n+1}`. L1 as written,

```lean
Firoozbakht : Prop := ∀ n ≥ 1, (p (n+1))^n < (p n)^(n+1)
```

therefore asserts, in the document's 1-indexed notation, `p_{n+2}^n < p_{n+1}^{n+1}` — i.e. `n·log p_{n+2} < (n+1)·log p_{n+1}`, which is F at index `n+1` with exponent ratio `1 + 1/n` in place of `1 + 1/(n+1)`. Since `1 + 1/n > 1 + 1/(n+1)`, **the formalized proposition is strictly weaker than Firoozbakht** (it is implied by F at index `n+1`, and does not imply it). A Lean development could go green on it and have formalized a different, weaker conjecture. The correct form is `∀ n, (p (n+1))^(n+1) < (p n)^(n+2)`, or `p n := Nat.nth Nat.Prime (n-1)`.

This is not covered by §6's `[needs-anchor]` blanket, which is scoped to *API names drifting*. This is a semantic indexing error that survives any name check. Given §6's own framing — "this is the anchor object every other leg must import", and §9's `lean-skeleton` leg "pins the statement so no leg drifts" — a wrong pin is the most expensive single error the document can contain.

**§5.2's Lean blocker claim — right conclusion, wrong reason, and the wrong reason changes the fix.** §5.2 says `Nat.nth Nat.Prime n` "is not efficiently kernel-reducible", framing it as a performance problem and contrasting it with integer size. In fact **`Nat.nth` is `noncomputable`** — defined by cases on finiteness of the predicate's satisfying set, using an order isomorphism / classical machinery in the infinite branch. `decide` cannot reduce it *at all*; there is no efficiency dial. Mathlib supplies `nth_prime_zero_eq_two` … `nth_prime_four_eq_eleven` as hand-proved `@[simp]` lemmas precisely because you cannot evaluate them, and it stops at index 4.

Consequences the document misses:
1. The workaround ("supply the primes as literals with `Nat.Prime` certificates") is necessary but not sufficient — you additionally need the `Nat.count` ↔ `Nat.nth` bridging lemmas to connect a literal to `Nat.nth Nat.Prime n`, and *that* per-`n` cost is what actually caps `N` in L3, not `norm_num`'s bignum speed.
2. The cost is linear in `p_N`, not `N`: the "no prime strictly between" obligation requires compositeness of every integer in each gap, so total work is `Σ g_n ≈ p_N`. This is the Q3 certificate hatch surfacing in the formalization.
3. §5.2 is internally inconsistent: its first paragraph says (F3) is a poor bulk computation *because of digit count* at `n = 10⁵`, then its "correction" says "the real obstacle is different and must not be confused with size". Both are true at different `N` (size bites above `N ≈ 10⁴`, non-reducibility bites at every `N`), but the second is written as superseding the first. The correction over-corrects.

---

## Q7 — Ranking

Ordered by (severity × cheapness of fix), with the change required.

1. **L1** — off-by-one against Mathlib's 0-indexed `Nat.nth`; the formalized proposition is strictly weaker than F. *Must change:* restate as `∀ n, (p (n+1))^(n+1) < (p n)^(n+2)`, or redefine `p n := Nat.nth Nat.Prime (n-1)`, and state the indexing convention explicitly next to §1.1's `p_1 = 2`. Add an indexing sanity lemma (`p 1 = 2`) as a compile-time guard. Non-negotiable before any Lean leg runs.

2. **P6′** — the only empirical support offered is a corollary of the uncontested half of the claim (59/59 structural, and the "six" is a script `[:6]` cutoff that breaks at 8/10). *Must change:* strike "the empirical support is good" from §2.4 and §5.1's finding 3; replace with the explicit statement that ρ-tightness at first occurrences follows from coarse T-growth and carries no information about fine-scale oscillation. Then attack P6′ the way `T_n < L²` was discharged in Q4 — bound the oscillation of `T` between consecutive record indices via a Dusart-type two-sided `π` estimate. That is a concrete, finite, discharge-able task; it is currently phrased as an aspiration.

3. **S2** — declared "possibly viable under a strong enough hypothesis" and policed for circularity. *Must change:* close it. No limsup/tail hypothesis can imply a for-all-`n` statement; Cramér's conjecture does not imply F. Restate S2's verdict as "not viable: any sufficient hypothesis contains F-for-large-`n`", and drop the unsatisfiable obligation placed on downstream legs.

4. **T4 / R2 / S3** — the bar is `L²` where F's true bar is `L² − L − 1`, and "infinitely often" where "once" suffices. The exact twin of the error §4.3 caught for T3, propagated nowhere. *Must change:* restate T4 as "prove `g_n > T_n` for at least one `n`, non-constructively" and note that `limsup g/L² > 1` is a sufficient but `O(L)`-conservative special case — the same sentence §4.3 already wrote for T3.

5. **§1.4 / T1's certificate claim** — "a single integer `n` plus the two primes with primality certificates settles it" omits `π(p_n) = n`, which has no known succinct certificate and costs `~p^{2/3}` at best. *Must change:* separate "Σ₁, hence finitely verifiable" from "admits a short certificate"; the second is false. Propagate the consequence into L3's cost model (linear in `p_N`, not `N`).

6. **L4 as primary Lean deliverable / "only genuine theorem"** — false as stated (L2, L5, L6 are theorems), and L4 has no import path into L1. *Must change:* promote **L2** and **L5** to primary deliverables (§6's own "honest expectation (ii)" already argues for this); keep L4 as a standalone exercise; and add the missing bridge node (effective `p_n = n log n + n log log n − n + E_n`) without which S6/L4 is decorative.

7. **§2.4's differencing** — "T increases *exactly* when the gap exceeds `L`" misclassifies 7.07% of steps; the correct threshold is `L − 2` (0.29%), because `n ≈ p/L` is substituted inside a difference where the `O(1)` term survives. *Must change:* replace with `ΔT ≈ (L/p)[g(L+1) − L(L−1)]`, threshold `g < L − 2 + O(1/L)`, and demote "exactly" to "approximately". The 55.9% figure itself is sound and computed on the true `T` — keep it, fix the explanation under it.

8. **§5.1's method at scale** — doubles carry `1.8 × 10⁹` of headroom at `3 × 10⁶`, `1.16` at `1.7 × 10¹⁵`, and `6.8 × 10⁻⁴` at `4 × 10¹⁸`. *Must change:* state the crossover (`p ≈ 2 × 10¹⁵`) explicitly in §4.1 and §5.2, and mandate exact rational or interval arithmetic above it. Note that the failure is silent in the verification direction. Also: any future comparison against A2's `4 × 10¹⁸` frontier must confirm that frontier was not itself established in doubles.

9. **T3's unconditional range** — supported by finite check where a proof with an explicit constant exists in four lines (Q4). *Must change:* insert the Rosser–Schoenfeld/Dusart argument; upgrade "for all large `n`" to "for all `n ≥ 11`, unconditionally"; note the exceptional set is `{1..7, 10}`, not `{1..10}`.

10. **R3 (empty) and R4 (mis-tagged `[O]`, in fact established)** — *Must change:* retag R4 `[E]`; either fill R3 with the missing "conditional refutation from a rigorous hypothesis" node or delete it. Add R2′ (non-constructive single witness) as a sibling of R1/R2.

11. **§0's reproducibility claim vs the committed scripts** — three §5.1 rows are absent from `attack/probe.py` / `attack/probe2.py`, and `probe.py` line 27 prints `2.081 at p = 2` where the table says `0.703 at p = 2010733`. All three absent rows are true (independently verified, including the 943 550-digit exact-integer check at `n = 149689`, which HOLDS). *Must change:* restrict line 27's generator to `i ≥ 9`, and add the exact-integer, `T_n < L²`, and record-intersection checks to the committed scripts — or downgrade those rows from tier L1.

12. **P3c's phrasing and P7's tag** — lowest severity. *Must change:* P3c to "not obtainable from RH by known methods" (no difficulty ordering between propositions is known); P7 from `[X]` obligation to a remark.

Files referenced: `attack/decompose.md`, `attack/probe.py`, `attack/probe2.py`.

Sources for the Mathlib facts: Mathlib.Data.Nat.Prime.Nth, Mathlib.Data.Nat.Nth (leanprover-community mathlib4 docs).
