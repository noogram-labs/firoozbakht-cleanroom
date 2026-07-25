# Popper — falsifiability audit of `attack/decompose.md`

All numbers below are from the persona's own re-run of the sieve (`attack/probe.py`-equivalent, plus four new measurements); scratchpad scripts under the session scratchpad (`q34.py`, `q5.py`). It reproduces the document's reported figures (21 record gaps, ρ_max = 0.760471 at p = 1327, 0.999998390613 at n = 149689) and disagrees with none of them. Its findings are about what those numbers *do not* license.

## Q1

**Three routes pass through no listed node.**

1. **Independence.** F is Π₁ (over a Δ₀ definition of `p_n`). "Decide F" admits an outcome — F is independent of the ambient theory — that is neither a P-node nor an R-node. This is not idle: for a Π₁ sentence, independence from a sound theory entails truth in the standard model, so this outcome is *not* symmetric between the branches and would settle the belief question while discharging nothing in Branch P. The tree's framing sentence ("Any complete resolution must pass through these nodes") is false as written.

2. **Conditional refutation.** §3.0's table is asymmetric in a way it does not notice. Branch P has a conditional node (S2: prove F under a hypothesis). Branch R has only unconditional (S3/R2, `[X]`) and heuristic (S5/T5, not a proof). The middle rung — *a theorem of the form "conjecture X ⟹ ¬F" for an independently motivated X* (Hardy–Littlewood k-tuples being the obvious candidate) — exists on the proof side and is simply absent on the refutation side. This is plausibly the most reachable genuine theorem in the whole R branch, and it has no node. Note it is **not** S5: S5 is a heuristic computation, not an implication from a stated conjecture.

3. **Hybrid finite-check-plus-effective-tail.** The standard shape of computer-assisted results in this area (verify n ≤ N₀ exactly, prove n > N₀ analytically) is exactly what P4 + P5 would compose into, and no S-node names it. It happens to be blocked by P3, but a decomposition whose purpose is to stop legs rediscovering dead ends (§2.5's stated rationale) should record it as blocked rather than omit it.

**Structural defect independent of the above:** §2 is called a tree but is a flat two-level enumeration with **no edges**. The one load-bearing structural fact is invisible as a result: **P4 is a shared dependency of both branches.** R1's certificate needs an unconditional lower bound on π(p_n) (see Q3), P6′ needs P4 by the document's own statement, L6 needs P4, and T3's sufficiency needs P4 (Q4). Drawing P4 as a leaf of Branch P misrepresents the refutation route as independent of the proof machinery, which is the opposite of true.

Minor over-closure: S9 is dismissed for "two independent reasons — magnitude and localization". Only magnitude is fatal. The localization objection is precisely what an explicit π estimate repairs — i.e. it is P4, not a wall. Listing a repairable objection alongside a fatal one inflates the confidence of the "not viable" verdict.

## Q2

(i) S2's circularity is already flagged in §3.2 — **does not count**, and I have nothing to add to it directly. What I add is that **the test §3.2 demands of S2 is never applied to the document's own load-bearing R-side item.** S5/T5 asks whether Cramér–Granville is independent of the target. It has the same shape as the S2 worry: the heuristic and F are both statements about the same `log²` normalization, and §3.6 shows the mean part of that model *makes F true*. The check does pass — the heuristic's content lives entirely in the fluctuation term, F's difficulty lives entirely there too, and `2e^{−γ} − 1 = 0.1229` dwarfs the O(1/L) that connects them — but the document demands the audit of a route it disbelieves and skips it for the one it leans on.

(ii) **P6′ using P4 is not circular** (explicit π estimates presuppose nothing about F). But there is a real circularity one level down that §8.2 does not cover. §3.4 authorizes the search to focus on record gaps "by P6′ (once discharged, **or heuristically meanwhile**)", and §9 instructs the `notebooks` leg to extend the ρ table. A pruned search that finds nothing has not tested F at the pruned indices — it has corroborated the strictly weaker "F holds at record indices". If that null result is then reported as verification to a new height, the undischarged assumption has been laundered into the evidence that would later be cited to support the search design. The in-run scan was exhaustive so this has not bitten yet; the very next leg is where it bites. §8.2 says P6′ is unproved; it does not say that using it as a *filter* contaminates the *output*.

(iii) **Corollary A1's double use is not circular** — using F ⟹ bound to define an objective and its contrapositive to refute is standard. But there is an internal inconsistency: §3.4 writes the objective as "ρ_n, equivalently `g_n/(L²−L−1)` up to O(1/L)", which is exactly the substitution class §4.3 forbids two pages later. Measured at the document's own six tightest cases, that substitution inflates ρ by **+2.744% at p = 1327** and **+16.036% at p = 113** — the two cases §5.1 headlines. It deflates by only −0.087% at p = 2010733.

## Q3 — teeth (lead strate)

Each test's *failure* means: the sought object is found / the sought statement proved. Question: does that entail ¬F?

**T1 (§4.1) — ONLY-IF ⟨the exhibited index is certified to be π(p_n), or lower-bounded⟩.**

The inequality `p_{n+1}^n ≥ p_n^{n+1}` is literally ¬F *at the true index n*. The document's certificate is "`(n, p_n, p_{n+1})` plus primality proofs for both and a proof that no prime lies strictly between them." **That list omits the only hard part.** Nothing in it certifies `π(p_n) = n`. And the omission fails in the dangerous direction: `T_n = p_n(e^{L_n/n} − 1)` is *decreasing* in n, so an overstated index lowers the bar. A certificate with an unverified index is exploitable precisely toward a false refutation.

§1.4 calls this "the single most important structural fact about the problem" and states "a single integer `n` plus the two primes, with primality certificates, settles it." **That sentence is false as written, and it is untagged.** §1.1 knows the reason — "π(p_n) = n exactly — the threshold couples the gap to the *count*" — and §4.1 forgets it three sections later.

Decidable in practice? Decompose the cost at the scale a counterexample would live (p ~ 10^19, gap ~ L² ~ 1900):
- interior "no prime strictly between": ~1900 integers each needing a *compositeness* witness. Compositeness certificates are short and cheaply verified (one Fermat/Miller–Rabin base each). **Cheap.**
- endpoint primality: ECPP at 10^19 is routine. **Cheap.**
- the index: no succinct certificate for π(x) is known; verification means re-running a Meissel–Lehmer / LMO computation. **This is the whole cost.**

So T1 as specified is decidable only in principle. **The repair is available and the document misses it:** one does not need π exactly, only a certified *lower* bound N ≤ π(p_n) with `p_{n+1}^N ≥ p_n^{N+1}`, because lowering the index only raises the bar. Explicit unconditional π lower bounds (Dusart-type) supply this, and the precision cost is negligible — the relative slack between true π and a Dusart-type lower bound is ~6/L⁴ ≈ 4·10⁻⁶ at L ≈ 35, against a sought ρ-margin of order 1. **Consequence: R1/T1 depends on P4.** That edge does not exist in §2.

**T2 (§4.2) — the label covers two inequivalent statements.**

- **T2a: `ρ_n = g_n/T_n ≥ 1`. YES — exactly, with no slack anywhere.** Entailment: `g_n ≥ T_n = p_n(e^{L_n/n} − 1)` ⟺ `p_n + g_n ≥ p_n e^{L_n/n}` ⟺ `p_{n+1} ≥ p_n e^{L_n/n}` ⟺ `log p_{n+1} ≥ L_n(1 + 1/n)` ⟺ `n log p_{n+1} ≥ (n+1) log p_n` ⟺ `p_{n+1}^n ≥ p_n^{n+1}`. Every step is an equivalence over positive reals with `exp`/`log` strictly monotone. **T2a is T1, not an approximation of it.** No O(1/L) enters at any step.

- **T2b: `g_n ≥ log²p_n − log p_n − 1`. ONLY-IF ⟨`T_n ≤ L_n² − L_n − 1` at that n⟩ — and that inequality is *false* for small n.**

  The sign of `T_n − (L_n²−L_n−1)`:

  | n | p_n | T_n | L²−L−1 | diff | rel |
  |---|---|---|---|---|---|
  | 100 | 541 | 35.142 | 32.314 | **+2.828** | **+8.05%** |
  | 1 000 | 7 919 | 71.409 | 70.610 | +0.799 | +1.12% |
  | 10 000 | 104 729 | 121.128 | 121.054 | +0.073 | +0.06% |
  | 30 000 | 350 377 | 149.138 | 149.224 | −0.086 | −0.06% |
  | 216 815 | 2 999 957 | 206.366 | 206.517 | −0.151 | −0.07% |

  The sign **flips 733 times**, first at n = 5899 (p = 58231) and last at n = 52371 (p = 644123). Below n ≈ 5900 it is uniformly positive; above n ≈ 52400 uniformly negative in the checked range. So T2b is **not sufficient** for ¬F below n ≈ 5900, is **neither** sufficient nor necessary through the 733-flip transition zone, and is **necessary but not sufficient** above it.

  **Slack versus the ~5% "fragility" margin — the direct answer.** The margin §4.3 calls the conjecture's fragility is `0.9706 − 0.9206 = 0.050`, i.e. 5.2% of the bar, at L ≈ 35. The T2b substitution error:
  - at p = 113: **+16.0%** — three times the margin;
  - at p = 1327 (the document's own headline tightest case): **+2.74%** — same order as the margin;
  - at p = 2 010 733: **−0.087%** — 60× below the margin;
  - extrapolating the O(1/L)/L² ≈ 1/L³ scaling to L ≈ 35 (where the recalled 0.92 record lives): **≈ 2·10⁻³ %** — roughly 2000× below the margin.

  So: **the slack is larger than the fragility margin exactly where the document's rhetoric lives (its six tightest cases, five of which sit at p < 5·10⁵), and negligible compared to it exactly where a counterexample would live.** The substitution is therefore harmless for the search leg and harmful for the narrative. Neither half is stated.

  One further consequence: because the sign flips, the surrogate is not conservative in either direction. A search leg using T2b below n ≈ 5900 can report a breach that is not a refutation.

**T3 (§4.3) — ONLY-IF ⟨`T_n < L_n²` at that n⟩; see Q4 for why that condition's warrant is void where it is needed.** Entailment: `g_n ≥ L_n²` and `T_n < L_n²` give `g_n > T_n`, hence ¬F by (F4). Sound. The condition is verified for 11 ≤ n ≤ 216815 (confirmed: zero exceptions).

**T4 (§4.4) — YES.** Entailment: F ⟹ ∀n, `g_n < T_n = L² − L − 1 + O(1/L)` ⟹ `g_n/L² < 1 − 1/L − 1/L² + O(1/L³)` ⟹ `limsup g_n/L² ≤ 1`. Contrapositive: `limsup > 1` ⟹ ¬F. This is the one test where Claim A's unquantified error term is genuinely harmless — it vanishes in the limit, so P4 is not needed here. Two observations the document does not make: (a) T4 is the *only* test in §4 whose entailment does not route through P4; (b) T4's bar is set looser than F forbids — F forbids `g_n ≥ T_n` at a single n, and `T_n/L² → 1` from below, so a theorem "`limsup g_n/(L²−L−1) ≥ 1` with the limsup attained" would also refute. Stating T4 at the strict-`> 1`, `L²`-normalized bar throws away teeth for free.

**T5 (§4.5) — NO.** The document labels it a non-test; agreeing is worth nothing, so instead: **T5 is not a test in either direction, and the document's own §4.3 violates that.** A limsup statement is invariant under every finite computation — no observation, at any height, bears on it. It follows that the numerical corroboration of F, however far extended, carries *zero* weight against the Cramér–Granville prediction; the two bodies of evidence are not commensurable, and §8.7's even-handed "heuristic points false, numerics point true" quietly presents them as if they were. Worse, §4.3 converts a single finite datum (record ρ ≈ 0.92 at L ≈ 35) into a claim about the conjecture's *fragility* — "the strongest available empirical argument that it is fragile". That inference is untagged and presupposes a growth law for the record-ρ envelope. Under F the envelope converges below 1; under Granville it eventually exceeds 1; one sample at L ≈ 35 does not discriminate between those, and a 5% margin is only "fragile" relative to a rate of approach nobody has estimated. §4.5 forbids promoting the heuristic to a test; §4.3 then borrows the heuristic's frame to read a finite number as evidence of fragility. That is the same promotion by another door.

## Q4 — classification (lead strate)

**T1 `[decidable, Σ₁]`.** ¬F is correctly Σ₁. But "decidable" is doing double duty: each *instance* is decidable; the *test* is a search, i.e. semi-decidable, and a leg reading the tag may expect termination. Tag should read `[semi-decidable; each instance decidable; ¬F is Σ₁]`. Substantively, per Q3, add `— certificate requires a certified lower bound on π(p_n) (P4)`.

**T2 `[decidable]`.** Correct for T2a, and T2a is not an independent test — it is T1 in stable arithmetic. Listing it as a separate falsifiability test overcounts the R-side surface by one. For T2b the tag should be `[decidable; neither sufficient nor necessary without an effective sign for T_n − (L²−L−1); sign measured to flip 733× over 5899 ≤ n ≤ 52371]`.

**T3 `[decidable, sufficient]` — direction re-derived independently, and §4.3's self-correction is CORRECT.** Re-derivation without reference to the document: a T3 breach gives `g_n ≥ L_n²`; if `T_n < L_n²` then `g_n > T_n`, which is a T2a breach, which is ¬F. Conversely a T2a breach gives only `g_n ≥ T_n`, and since `T_n ≈ L² − L − 1 < L²`, that does not give `g_n ≥ L²`. So T3 ⟹ T2, not T2 ⟹ T3: **T3 is strictly stronger, i.e. sufficient and not necessary.** The bar it sets is too high by `≈ L + 1`. §4.3's corrected direction survives re-derivation.

**But the sufficiency tag is not valid unconditionally, and the way it fails is sharper than "only on the checked range".** §4.3 grounds `T_n < L_n²` on a finite check, 11 ≤ n ≤ 216815. In that same range the maximum of `g_n/L²` is 0.703 — a T3 breach is *impossible* there. **The region where T3's sufficiency has been verified and the region where T3 could ever fire are disjoint.** As it stands, the `[sufficient]` tag has support nowhere it could be used. This is not in §8.

It is repairable cheaply. `T_n < L_n²` ⟺ `e^{L/n} < 1 + L²/x` ⟺ `n > L/log(1 + L²/x)`, and expanding, `L/log(1+L²/x) = x/L + L/2 + O(L³/x)`. Check of that expansion:

| n | needed π(x) > | x/L + L/2 | actual n |
|---|---|---|---|
| 11 | 10.652 | 10.744 | 11 |
| 10 000 | 9066.061 | 9066.062 | 10 000 |
| 216 815 | 201156.389 | 201156.389 | 216 815 |

So the required lemma is `π(x) > x/log x + (log x)/2`, and an unconditional Rosser–Schoenfeld/Dusart-type bound `π(x) ≥ (x/L)(1 + 1/L)` for x above a small explicit threshold gives `π(x) − x/L ≥ x/L² ≫ L/2` with enormous room. **T3's `[sufficient]` tag is convertible from finite-range to unconditional by one explicit inequality — which is P4 again.** Corrected tag: `[decidable; sufficient given T_n < L_n²; verified 11 ≤ n ≤ 216815, provable from explicit π lower bounds, currently undischarged]`.

**T4 `[not decidable, requires a theorem]`.** Correct, and per Q3 the bar is set looser than necessary.

**T5 `[not a refutation]`.** Correct label; the objection is to §4.3's use of the same frame, not to the label (Q3).

**§4.6 anti-test — correctly excluded, both items; both re-derived.** Littlewood: `L/n = L/(li+Δ) ≈ (L/li)(1 − Δ/li)`, so `ΔT ≈ xLΔ/li² ≈ L³Δ/x`, and with `Δ ~ √x·logloglog x/L` this is `O(L²·logloglog x/√x) → 0`. Confirmed. Bertrand: `p_n ≥ 2^n` holds only at n = 1 (`p_2 = 3 < 4`, and `p_n ~ n log n ≪ 2^n` thereafter). Confirmed. **What is missed:** the Littlewood computation is filed as a dead end, but it establishes that `T_n` is insensitive to the fine structure of π at √x scale — i.e. `T_n` is pinned by li(x) to within o(1). That is a substantial fraction of exactly the effectivity P4 is asked for, on the T side. Half of a needed lemma is filed under "what does NOT bear on F".

## Q5

The tagging discipline (§0: "Nothing downstream may build an obligation on an untagged assumption") is not applied to the document's own reasoning apparatus.

- **The status codes `[E] [O] [X] [C]` carry no epistemic tag.** `[X]` = "out of reach with current technology" is a forecast about the future of a research field. It forbids no observation and cannot be checked. The falsifiable core of P3 is a different sentence — "no published method yields polylogarithmic unconditional or RH-conditional gap bounds" — which is empirical, checkable against §7, and is what a citation gate could actually resolve. The document tags its number-theoretic claims scrupulously and leaves its four load-bearing verdict codes untagged.

- **§2.4's differencing substitutes `n ≈ p_n/L_n`** — first-order PNT, dropping a relative `1/L ≈ 7%` at p = 3·10⁶ — inside a computation whose *entire output* is a threshold ("T increases exactly when `g_n > L`"). The corrected threshold is near `L + 1`, not `L`. Untagged. Worse epistemically: the in-run 55.9% is offered as confirmation of that derivation, but it is a measurement of the exact T's sign changes and would come out near 50–56% for *any* threshold in the neighbourhood of L. It is a non-discriminating observation presented as corroboration — the verificationist move, in a document that elsewhere avoids it.

- **§5.1's 0.9999984 in double precision.** Checked at 60 digits: the true value is 0.99999839061343611637…, the double is 0.9999983906134361 — correct to every digit printed, with `1 − ratio = 1.609·10⁻⁶` against a double resolution of ~2.2·10⁻¹⁶, i.e. **headroom factor 7.3·10⁹**. The figure is safe. **But the margin scales as `(1−ρ_n)/n`, verified to 3–4 digits across five decades:**

  | decade | tightest 1−ratio | (1−g/T)/n |
  |---|---|---|
  | 10¹ | 4.648e-03 | 4.775e-03 |
  | 10³ | 5.107e-05 | 5.109e-05 |
  | 10⁵ | 1.609e-06 | 1.609e-06 |

  Extrapolating: with `1−ρ ≈ 0.08`, the margin falls below double resolution at **n ≈ 3.6·10¹⁴, i.e. p ≈ 1.2·10¹⁶** — *below* the recalled 4·10¹⁸ frontier (A2), and within one order of magnitude of the p ≈ 1.693·10¹⁵ record the document quotes in A10. `attack/probe.py` is correct at 3·10⁶ and **silently produces noise** if a `notebooks` leg extends it as instructed in §9. §5.2 flags a numerical hazard for the *Lean* legs (bignum sizes, `Nat.nth`) and none for the *search* legs, which is the one that will actually run. `ρ_n = g_n/T_n` does not have this problem — its operands are O(1) — which is a second, stronger reason to prefer ρ than the one §4.3 gives.

- **§3.6's smooth surrogate.** `f(x) = (x log x)^{1/x}` is asserted to be "the PNT first-order model of `p_n`", but the substitution being made is `p_n ↦ n log n` *with n treated as a continuous variable*, and the object under study, `(log p_n)/n`, is then differentiated in that variable. The step "F for the smooth model" ⟹ "F is true for the mean behaviour of `p_n`" (§3.6's verdict) requires that the second-order term `n log log n` — which is *larger* than the `log²` scale of the whole phenomenon — does not affect the sign of the derivative. Untagged. The document already knows the derivative's sign is delicate (§8.8 records the x ≥ 4 / x ≥ 5 slip); the delicacy of the *model choice* is not recorded alongside the delicacy of the *domain*.

- **§1.3's term-wise inversion** `(1 + 1/L + 2/L² + O(L⁻³))⁻¹ = 1 − 1/L − 1/L² + O(L⁻³)` — verified (`(1+a)⁻¹ = 1 − a + a²` with `a = 1/L + 2/L²` gives `1 − 1/L − 2/L² + 1/L²`). **Correct.** No finding here.

- **§2.4's characterization of the P6′ risk is calibrated on the wrong statistic** — see Q7 #3; it belongs here too, as an untagged inference from "56% of steps decrease" to "monotonicity is false, flatly, therefore P6′ is a live correctness risk". The first clause is true and the third does not follow from it.

## Q6

- **P1 `[E]`** — correct; F1⟺F3⟺F2⟺F4 re-derived.
- **P2 `[E]`** — miscalibrated. `[E]` groups an exact algebraic identity (P1) with an asymptotic carrying an unquantified error term. §8.3 admits the O(1/L) is not effective, but the tree still shows `[E]`, and *every finite-n use of P2 in this document* (T2b, T3's sufficiency, the §3.4 objective, P6′) needs the effective version. P2 and P4 are one node split by effectivity, drawn as siblings with no edge.
- **P3 `[X]`** — the *obligation* is correct; the tag is a forecast (see Q5). Separately, P3a/P3b/P3c are not obligations — they are comparisons. Branch P's largest subtree contains no dischargeable node.
- **P5 `[C]`** — misfiled. No proof of F passes through a finite verification. P5 is a precondition of the hybrid strategy that §3 does not list.
- **P6 `[O]`** — **misfiled branch.** The maximal-gap reduction serves the *search* (§3.4/S4 and §3.8/S8), which is Branch R. It sits in Branch P, which is why the document then has to import it into §3.4 informally ("or heuristically meanwhile") — the misfiling is what produced the Q2(ii) contamination.
- **R3 `[O]`** — miscalibrated. "Refute a consequence of F that is easier to attack" points at §4.3, but §4.3 is a search criterion, not a theorem route. The only *consequence* of F identified anywhere in the document is the Cramér-scale bound, and refuting that is R2, tagged `[X]`. R3 as `[O]` has no instance. Either it should be `[X]`, or it should be repopulated with the conditional-refutation route missing per Q1.
- **R4 `[O]`** — miscalibrated in the safe direction: §3.5 *discharges* it. The contradiction with Cramér–Granville is established (modulo A9). R4 is `[E]`, with the caveat that what it establishes is a tension, not a refutation.

**§2.1's verdict sentence.** Parsed as written — "proving F is strictly harder than [proving RH is useful for prime gaps]" — the substance is defensible: F ⟹ `g_n = O(log²p_n)` unconditionally (Claim A, unconditional), which is a strictly stronger conclusion than RH's `g_n ≪ √p_n log p_n`, and the converse fails (an O(log²) bound with an unspecified constant does not give F). So the correct claim is **"any proof of F is at least as hard as an unconditional polylogarithmic gap bound, and F is strictly stronger as a statement than what RH is known to give."** That is falsifiable — exhibit an RH-conditional argument reaching polylog scale and it dies. The sentence as written substitutes "strictly harder" for "strictly stronger", which conflates logical strength with proof difficulty and is not entailed by anything above it. **Verdict: substance sound, wording an overreach; recommend the restatement, which loses no force and gains a refutation condition.**

## Q7

See below.

## Weakest branches (ranked)

**1. T2 (§4.2) — one label over two inequivalent tests.** The "equivalently, up to O(1/L)" is misplaced: `ρ_n ≥ 1` is *exactly* T1 with zero slack, while `g_n ≥ L²−L−1` is a surrogate whose error changes sign 733 times over 5899 ≤ n ≤ 52371 and reaches +8.05% at n = 100, +16.0% at p = 113, +2.74% at p = 1327 — comparable to or larger than the 5% margin §4.3 calls the conjecture's fragility, at the very cases §5.1 headlines. **What must change:** split into T2a (exact, `ρ_n = g_n/T_n ≥ 1`, note it is T1 restated, not a second test) and T2b (surrogate, explicitly not sufficient below n ≈ 5900, and marked as requiring an effective sign for `T_n − (L²−L−1)`); delete the same substitution from §3.4's objective.

**2. T1 / R1 certificate (§4.1, §1.4) — the certificate omits the index.** Nothing in `(n, p_n, p_{n+1})` + primality + no-prime-between certifies `π(p_n) = n`, and the omission fails toward a *false* refutation since `T_n` decreases in n. §1.4's "finitely certifiable" is false as written, in the sentence the document calls its most important structural fact. **What must change:** certificate becomes `(N, p_n, p_{n+1})` + endpoint primality certificates + interior compositeness witnesses + **a certified unconditional lower bound `N ≤ π(p_n)`**, with `p_{n+1}^N ≥ p_n^{N+1}`; and P4 must be drawn as a dependency of R1 in §2, not as a Branch-P leaf.

**3. P6 / P6′ (§2.4) — alarm calibrated on a non-discriminating statistic; misfiled branch.** "T decreases at 55.9% of steps" is true and is not the quantity the reduction needs. The quantity it needs is the maximum drawdown of T between a record index and any later index in the same record block. Measured: **global max drawdown over n ≥ 10 is 0.5487 (1.23% of T at that scale, at n = 206 → 214), and the number of pairs (record index m, n > m in the same block) with `T_n < T_m` is ZERO across all 21 record blocks below 3·10⁶.** So P6′ is empirically unviolated with the strongest available in-run evidence, and the document reports the statistic that makes it look most endangered while never computing the one that bears on it. **What must change:** restate P6′ in terms of the drawdown bound, report the zero-violation measurement, and move P6 into Branch R where the reduction is actually used; then re-run at larger scale where the coarse-growth-vs-drawdown ratio is the thing to track.

**4. T3 (§4.3) — sufficiency verified only where the test cannot fire.** `T_n < L_n²` is checked for 11 ≤ n ≤ 216815, a range in which `max g_n/L² = 0.703` makes a T3 breach impossible. Warrant and applicability are disjoint sets. **What must change:** prove `T_n < L_n²` unconditionally from an explicit π lower bound — the requirement reduces to `π(x) > x/log x + (log x)/2` (verified to 3 decimals at n = 11, 10⁴, 2.17·10⁵), which Dusart-type bounds clear by a factor of ~`x/L²` versus `L/2`. One inequality converts `[sufficient on a finite range]` into `[sufficient unconditionally]`.

**5. §5.1's numerical method and the `notebooks` leg (§9).** Double precision on the log-ratio is safe at 3·10⁶ by 7.3·10⁹, but the margin scales exactly as `(1−ρ_n)/n` (verified across five decades) and crosses double resolution at n ≈ 3.6·10¹⁴, p ≈ 1.2·10¹⁶ — below the recalled 4·10¹⁸ frontier and adjacent to the p ≈ 1.693·10¹⁵ record quoted in A10. `attack/probe.py` extended as §9 instructs will degrade silently. **What must change:** the search leg tracks `ρ_n` (O(1) operands) or uses exact rational/interval arithmetic on logs; §5.2's numerical-hazard note must cover the search legs, not only the Lean legs.

**6. S4 pruned by an undischarged P6′ (§3.4 + §9).** A pruned null result corroborates "F holds at record indices", not F. **What must change:** either discharge P6′ first, or require the search leg to report its reach as "record indices only" and forbid the number from being cited as a verification height.

**7. R3 and R4 tags (§2), and the missing conditional-refutation node.** R3 `[O]` has no instance; R4 `[O]` is already discharged by §3.5. The genuinely open, genuinely reachable R-side node — *a theorem "conjecture X ⟹ ¬F" for an independently motivated X* — has no slot, while its Branch-P mirror (S2) does. **What must change:** retag R3 → `[X]` or repopulate it; retag R4 → `[E]` (tension established, refutation not); add the conditional-refutation node and route the §3.0 archetype table's "Contradiction" row through it.

**8. §2's framing sentence and the absence of edges.** "Any complete resolution must pass through these nodes" is refuted by P5 and P6 (not necessary for any resolution) and by the independence outcome (passes through none). And the flat list hides that **P4 is the shared dependency of R1, T3, P6′ and L6**. **What must change:** weaken the framing sentence to "these are the nodes any resolution we can currently imagine passes through, plus an independence outcome that passes through none", and draw the four P4 edges.

**9. L5 (§6).** `Firoozbakht ↔ ∀n, g_n < T_n` re-imports `Real.exp` and the index `n = π(p_n)` into the statement that L1 was deliberately designed to keep in ℕ — and L5 is the node the entire ρ-based search rests on for its meaning. Effort is marked "medium"; it is the highest-risk node in §6 after L6. **What must change:** state L5's dependency on the index-vs-`Nat.nth` issue explicitly (the same one §5.2 identifies for L3), and size it with `lean-probe` rather than assigning "medium" by analogy with L2.

Items checked and found **sound**, so the ranking is not read as blanket criticism: the F1–F4 equivalence chain; the term-wise inversion in §1.3; Claim A's shape and its numerical convergence; the §4.3 direction correction (T3 sufficient, not weaker — re-derived independently and it holds); both §4.6 anti-test exclusions; the §5.1 tables, reproduced exactly; and the 0.9999984 figure, correct to every digit printed.
