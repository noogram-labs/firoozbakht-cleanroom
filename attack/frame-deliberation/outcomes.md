# Recommendation — Firoozbakht attack-surface decomposition: frame deliberation

**Commissioned by:** the `germ-20260725-791a7c45` MATH-ATTACK DAG, as the frame gate
upstream of `source-ledger` and the rest of the attack.
**Artifact under review:** `attack/decompose.md` (with `attack/probe.py`,
`attack/probe2.py`), produced by molecule `task-20260725-c062`, leg `decompose`.
**Panel:** wheeler · feynman · godel · popper · knuth (auto-selected; `panel=auto`).
**Supporting artifacts:** `attack/frame-deliberation/frame.md` (7 strates Q1–Q7 and the
substitution hypotheses), `attack/frame-deliberation/synthesis.md` (convergences,
divergences, coverage table), `attack/frame-deliberation/responses/*.md` (raw).

---

## Verdict

**Proceed — but repair six things first, and re-price two legs before compute is spent.**
The decomposition's *mathematics* survived the panel essentially intact: five independent
re-derivations confirmed the F1–F4 equivalence chain, Claim A's shape, the T3 direction
correction the document made to itself, both §4.6 anti-test exclusions, and the P3 gate;
and no panelist found a factual error in any number `attack/decompose.md` §5.1 reports —
including a 943 550-digit exact-integer check of the tightest in-run case, which holds.
What did not survive is a layer of **meta-statements made around that mathematics**: an
exhaustiveness claim (`attack/decompose.md` §2) that is false, a difficulty ordering
against RH (§2.1) that does not exist, a "genuine theorem" ranking (§6) that inverts the
Lean priorities, an alarm over P6′ (§2.4, §9) calibrated on a statistic that does not bear
on it, an empirical finding (§5.1 finding 3) that is a script's print truncation, and —
most expensively — an anchor definition (§6, L1) that formalizes a **strictly weaker
conjecture** than the one under attack. The pattern is consistent and it is the panel's
central finding: the artifact's tagging discipline audits *provenance* (`[self-contained]`
/ `[needs-anchor]` / tiers L1/L3) and never audits *modelling* — every tag answers "where
did this come from?", none answers "what did I assume?". Two corrections run in the
artifact's **favour** and must not be lost: P3's `[X]` gate needs only Chebyshev rather
than the undischarged Claim A, and P6′ is empirically unviolated by every measurement that
actually bears on it. The decomposition is a sound place to spend compute once the
adjustments below are made; it is not a sound place to spend compute as it stands, because
two of its recommended legs (`lean-skeleton`, `skeptic`/`notebooks` on P6′) would be
working against a mis-stated target.

---

## Recommended adjustments to the decomposition / falsifiability tests

Ordered by (severity × cheapness). Each names the branch, the change, and the panel
finding behind it. Locators are paired with their file throughout.

### Tier 0 — blocking. Do not dispatch the named leg until these land.

**1. Fix the L1 off-by-one before any Lean leg runs.**
*Branch:* L1 (`attack/decompose.md` §6), and through it L2, L3, L5.
*Finding:* godel and knuth, independently, with matching algebra
(`attack/frame-deliberation/synthesis.md` C1). Mathlib's `Nat.nth` is 0-indexed
(`Nat.nth_prime_zero_eq_two`), so `p n := Nat.nth Nat.Prime n` makes the document's `p n`
equal its own `p_{n+1}`. L1 as written asserts `p_{m+1}^{m−1} < p_m^{m}` — exponent ratio
`1 + 1/(m−1)` where F needs `1 + 1/m`. Since `1 + 1/(m−1) > 1 + 1/m`, **the formalized
proposition is strictly weaker than Firoozbakht**, and it additionally drops `m = 1`. A
Lean development could go green having proved a different conjecture.
*What must change:* restate as `∀ n, (p (n+1))^(n+1) < (p n)^(n+2)`, or redefine
`p n := Nat.nth Nat.Prime (n-1)`; state the indexing convention explicitly beside §1.1's
`p_1 = 2`; add a compile-time guard lemma `p 1 = 2`. Widen §6's `[needs-anchor]` scope
from *API names* to *names and indexing* — this is semantics and survives any name check.
*Blocks:* `lean-skeleton`, `lean-probe`.

**2. Re-price P6′ and redirect the legs pointed at it.**
*Branch:* P6/P6′ (`attack/decompose.md` §2.4), plus §5.1 finding 3 and §9's `notebooks`
and `skeptic` rows.
*Finding:* four panelists ran the measurement the reduction actually needs, four different
ways, all clean (`synthesis.md` C7): max dip of `T` below its running maximum decays
0.55 → 0.018 across decades while the margin grows 5.3 → 47 (wheeler); `T_{m(n)} ≤ T_n`
at **all 216 794 pairs, zero exceptions** (godel); **zero** violating (record, later)
pairs across all 21 record blocks, max drawdown 1.23% of `T` (popper). Meanwhile the
evidence the document *does* offer is non-diagnostic: ρ at a fixed gap value is maximal at
that value's first occurrence **because** `T` grows coarsely — the uncontested half of
P6′ — verified 59/59, and the "six tightest are records" figure is exactly
`attack/probe2.py:13`'s `best[:6]` print truncation, breaking at 8/10 and collapsing to
15/100 (knuth).
*What must change:* (a) strike "the empirical support is good" from §2.4 and rewrite §5.1
finding 3 to say the observation restates coarse T-growth and carries **zero** weight for
the fine-scale premise; (b) restate P6′ as a **drawdown bound** or, better, as the
pointwise envelope `|T_n − (L_n² − L_n − 1)| ≤ c/L_n` with `c` explicit — `T_n` depends
only on `(n, p_n)`, so the comparison needs no record structure and no path (godel,
wheeler); (c) demote P6′ in §9 from "one of the two places this decomposition is most
likely wrong" to a Dusart lookup; (d) move P6 into Branch R, where the reduction is
actually used (popper).
*Blocks:* the `notebooks` and `skeptic` briefs as currently written in §9.

**3. Stop the only live search from being pruned by its own undischarged lemma.**
*Branch:* S4 (`attack/decompose.md` §3.4) against the gate in §2.4.
*Finding:* four panelists (`synthesis.md` C6). §2.4 forbids citing "it suffices to check
maximal gaps" without discharging P6′; §3.4 then does exactly that ("once discharged, **or
heuristically meanwhile**"). Consequence the document never states: a null result from a
pruned S4 establishes "F holds at **record indices**", not F — and if that null is later
reported as a verification height, the undischarged assumption has been laundered into
evidence for the search design that assumed it.
*What must change:* either run S4 unpruned, or require every null result to be reported as
"no violation **at record indices** in range" and forbid the figure from being cited as a
verification frontier. This is a one-sentence contract on the `notebooks` leg and it
prevents a claim that cannot be walked back.

### Tier 1 — repair before the corresponding test or claim is used downstream.

**4. Split T2 into two tests and stop calling them equivalent.**
*Branch:* T2 (`attack/decompose.md` §4.2) and the search objective in §3.4.
*Finding:* unanimous on the exactness, with the slack quantified by three personas
(`synthesis.md` D1). `ρ_n = g_n/T_n ≥ 1` is *exactly* ¬F at `n` — an identity via (F4),
with **no `O(1/L)` anywhere in it**. The `O(1/L)` attaches only to the apposed clause
`g_n ≥ log²p_n − log p_n − 1`, which is a **third, inequivalent test**. Its error changes
sign **733 times** over `5899 ≤ n ≤ 52371` (popper), so it is conservative in neither
direction; it is `+16.0%` at `p = 113`, `+2.74%` at `p = 1327`, `−0.087%` at
`p = 2·10⁶`, and reorders the top-8 leaderboard (wheeler).
*What must change:* label them **T2a** (exact; note it is T1 restated, not a second test)
and **T2b** (surrogate; explicitly *not* sufficient below `n ≈ 5900`); delete the
"equivalently, up to `O(1/L)`" from §3.4's objective; mandate that no breach is ever
certified from T2b. Drop T2's `n ≥ 10` cut — (F4) is exact at every `n ≥ 1`, and the cut
is the exact propagation §1.3 forbids in bold. Dropping it also surfaces `ρ = 0.912` at
`p = 7` and `0.911` at `p = 3`, the two largest ρ values known (godel), which means
**ρ is nowhere near monotone in `p`** and any "the record ratio creeps toward 1" narrative
is reading a trend into a statistic whose global maximum sits at the fourth prime.

**5. Add the index certificate to T1, and re-scope §1.4.**
*Branch:* T1/R1 (`attack/decompose.md` §4.1) and §1.4.
*Finding:* three panelists (`synthesis.md` C2). §4.1's certificate — the two primes, their
primality proofs, and "no prime strictly between" — **omits `π(p_n) = n`**. The exponents
*are* the index. Primality has succinct certificates; primality **rank** does not, and
verification costs a full sieve or `Õ(x^{2/3})`. The omission fails in the dangerous
direction: `T_n` decreases in `n`, so an overstated index *lowers* the bar. §1.4's "a
single integer `n` plus the two primes, with primality certificates, settles it" is false
as written, in the sentence the document calls its most important structural fact — it
conflates **finite** witness (Σ₁, true) with **short** witness (false).
*What must change:* certificate schema becomes `(N, p_n, p_{n+1})` + endpoint primality +
interior compositeness witnesses + **a certified unconditional lower bound `N ≤ π(p_n)`**
with `p_{n+1}^N ≥ p_n^{N+1}` — lowering the index only raises the bar, so a Dusart-type
lower bound suffices at negligible cost (popper). Draw the resulting **R1 → P4** edge in
§2. Propagate two consequences: extending the ρ table is an **exhaustive-sieve project**,
not a spot search (the recalled `4·10¹⁸` frontier in A2/A12 is an *enumeration* limit);
and L3's cost is linear in `p_N`, not `N`.

**6. Fix the numerical instrument before `notebooks` extends the sieve.**
*Branch:* `attack/decompose.md` §5.1's headline statistic, §5.2's hazard note,
`attack/probe.py`.
*Finding:* four panelists (`synthesis.md` C10, D5). The reported `0.9999984` is correct to
every digit printed at `3·10⁶` (agreement to `2.2·10⁻¹⁷`; safety factor `1.8·10⁹`) — but
it is a **`1/n` artifact** that would read the same in a universe where every gap were 2
(feynman), and the margin scales as `(1−ρ_n)/n`, verified across five decades by two
personas. Crossover into noise: `p ≈ 2·10¹⁵` (most conservative estimate) — **below** the
frontier §9 asks the search to pass, with roughly one significant figure of headroom at
the A10 record itself and pure noise at `4·10¹⁸`. The failure is **silent in the
verification direction**: `attack/probe.py` breaks only on a detected violation, so a
masked true violation produces a false "verified".
*What must change:* retire the ratio row or replace it with `n·(1 − ratio)`; make `ρ_n`
(operands `O(1)`) the reported statistic everywhere; state the `p ≈ 2·10¹⁵` crossover
explicitly in §4.1 and §5.2 and mandate exact rational or interval arithmetic above it —
§5.2 currently flags hazards for the *Lean* legs and none for the *search* leg, which is
the one that will actually run. Also verify that A2's `4·10¹⁸` frontier was not itself
established in doubles.

**7. Correct the T3 tag and prove its side condition unconditionally.**
*Branch:* T3 (`attack/decompose.md` §4.3).
*Finding:* four panelists computed the same exception set (`synthesis.md` C5).
`T_n ≥ L_n²` at exactly `n ∈ {1,…,7, 10}` — `n = 8, 9` pass and `n = 10` fails, so
`n ≥ 11` is **not** a monotone crossing and a Lean induction will not find a base case
where it looks. T3 as stated is **satisfied right now at `n = 1, 2, 4`** by a conjecture
that holds there. And popper's framing: **warrant and applicability are disjoint** — the
range where sufficiency was verified (`11 ≤ n ≤ 216815`, where `max g/L² = 0.703`) is
precisely the range where T3 cannot fire, so the finite check contributes zero.
*What must change:* tag becomes `[decidable per instance; semi-decidable to find;
sufficient for n ≥ 11]`. Insert the four-line unconditional proof: `T_n < L_n²` reduces to
`π(x) > x/L + L`, which Rosser–Schoenfeld/Dusart's `π(x) ≥ (x/L)(1 + 1/L)` gives for
`x ≥ 599` (i.e. `n ≥ 109`), with `11 ≤ n ≤ 108` by finite check (knuth). Draw the
**T3 → P4** edge in §2. This discharges a piece of P4 at zero cost and is the template for
adjustment 2.

**8. Propagate the T3 correction to T4 / R2 / S3 — the twin error §8.8 missed.**
*Branch:* T4 (`attack/decompose.md` §4.4), R2, S3 (§3.3).
*Finding:* knuth. §4.3 corrected T3's bar from `L²` to `T_n ≈ L² − L − 1` and recorded the
correction in §8.8. The identical error remains in T4/R2/S3, which ask for
`limsup g_n/log²p_n > 1`. But F is refuted by `g_n > T_n` **once** — so those set the bar
`O(L)` too high *and* demand infinitely-often where a single index suffices. This is
exactly the failure mode §4.3 warns against ("could step straight over a genuine
counterexample"), left in place two subsections later.
*What must change:* restate T4 as "prove `g_n > T_n` for at least one `n`,
non-constructively", noting that `limsup g/L² > 1` is a sufficient but `O(L)`-conservative
special case — the same sentence §4.3 already wrote for T3. The practical verdict on S3 is
unchanged (large-gap technology is a full power of `log` short), but the classification is
wrong and will be inherited.

### Tier 2 — structural repairs to the tree and its notation.

**9. Weaken §2's exhaustiveness claim and add the five missing archetypes.**
*Branch:* `attack/decompose.md` §2's framing sentence and §3.0's table.
*Finding:* unanimous (`synthesis.md` C8). "Any complete resolution must pass through these
nodes" is false — P5 and P6 are not necessary for any resolution, and an independence
outcome passes through none. Missing archetypes, by count of panelists who named them:
**independence as a route to establishing F** (4/5 — for a Π₁ sentence, independence from
a sound theory entails truth in ℕ, and §1.4 supplies the premise in its own words without
drawing the inference); **conditional refutation `H ⇒ ¬F` for a rigorous `H`** (4/5 —
Branch P has a conditional node, Branch R has only unconditional and heuristic; this is
plausibly the most attainable non-trivial R-side result); **the P4 ∧ P5 join** (3/5 —
prove for `n > N₀` with `N₀` named, machine-check below; §2.3 forecloses it in a sentence
true of P5 alone); **strengthening for inductive traction** (3/5 — the standard cure for
the exact diagnosis that makes P7 `[X]`; §3.0 has "weakening" with no mirror);
**non-constructive single witness** (3/5 — R1 is constructive, R2 is asymptotic, the middle
is empty).
*What must change:* change the framing sentence from a claim of exhaustiveness to a claim
of coverage; add the five nodes even at `[X]`; **draw edges** — the tree is currently a
flat two-level enumeration, which hides that **P4 is the shared dependency of R1, T3, P6′
and L6** while appearing as a Branch-P leaf. Wheeler's structural point is the one to
adopt: a tree expresses disjunction and refinement and **cannot express conjunction**, and
three of the five missing archetypes are conjunctions of nodes that already exist
separately.

**10. Retag P3, P7, R3, R4 and fix three broken cross-references.**
*Branch:* `attack/decompose.md` §2's diagram and §2.1.
*Findings:* (a) **"strictly harder than RH" is an overreach — 5/5, unanimous**
(`synthesis.md` C3). The *strength* comparison is sound (F yields an unconditional polylog
gap bound not known to follow from RH); the *difficulty* ordering does not exist — F and
RH are incomparable and no partial order is supplied. Replace with: *"any proof of F
entails an unconditional gap bound not obtainable from RH by any known method"*, a
statement about technique that loses no force and gains a refutation condition. Note the
cost wheeler identifies: §2.1 elevates this to "a hard gate on Branch P" and the
**asymptotic** gate is then used to prune the **finite-range** P4∧P5 join it does not
touch. Scope the gate explicitly to gap-estimate-based routes. (b) P3 is a *consequence*
of F, not a prerequisite — a strategy clears it by succeeding — so the demand that
downstream legs "say how they clear P3" is not well-formed; and its `[X]` is more robust
than its own argument, since `T_n = O(L²)` follows from **Chebyshev**, not from the
undischarged Claim A. (c) P7 `[X]` is a category error: the absence of a technique is not
a proposition that could be out of reach. (d) R3 is empty — it names no consequence of F
other than the gap bound, and refuting that is R2 `[X]`; every T3 witness is a T1 witness
at a *higher* bar, so R3-via-§4.3 is a strictly harder R1 tagged as an easier route.
(e) R4 is `[E]`, not `[O]` — §3.5 executes it in five lines. (f) Three cross-references in
the diagram point at the wrong sections: `R2 → §4.2` (should be §4.4/§3.3),
`R4 → §4.4` (should be §4.5/§3.5), `R3 → §4.3` (maps an `[O]` node onto a decidable
search test).

**11. Extend the status alphabet.** `[E] [O] [X] [C]` cannot express "non-probative in
principle" (R4, T5), cannot distinguish a terminating finite check (P5) from a
semi-decidable search (R1) though both carry `[C]`, and cannot distinguish downward
obligations (P4) from upward consequences (P3). §9 already fears that `synthesize` will
lose the "S5-is-not-a-proof" distinction under compression; the cause is notational, and a
tree whose notation cannot state the status of its own non-probative nodes will lose them.

**12. Correct S9, §4.6's heading, and §2.4's differencing.**
(a) **S9 is blocked for one reason, not two** (3/5, `synthesis.md` C11). Magnitude is
fatal; localization is not — `T_n` depends on the index only through `L/n`, which is
pinned by `x` to within precisely the error §4.6 computes and dismisses. **The document's
own anti-test dissolves its own second blocking reason.** Collapse S9 into S3 as a remark
and correct §3.0's table, which shows two archetypes covered where one obstruction
operates. (b) **§4.6's estimate is correct and its heading over-scopes** (`synthesis.md`
C12): it bounds the effect on the *right* side of `g_n < T_n` and is titled "what does NOT
bear on F" — prime-deficit regions correlating with large `g_n` are untouched. Retitle to
"irrelevant to the threshold `T_n`". Note also that the same computation is **half of a
lemma P4 needs**, currently filed under "dead end". (c) **§2.4's "T increases *exactly*
when the gap exceeds `L`" is false** and the derivation cannot support any threshold: the
document's `L` misclassifies 7.07% of steps, `L−1` 2.79%, `L−2` **0.29%** — and the three
predict decrease-fractions 62.99% / 58.71% / 55.63% against the document's own measured
**55.9%**, so the rule offered predicts 63% and the figure reported as its confirmation
matches `L−2` instead (knuth; feynman independently reached `L−1`). Because `n ≈ p_n/L_n`
carries relative error `1/L ≈ 7%` — the same order as the disputed terms — **the smooth
derivation cannot resolve these at all** (feynman). Replace it with the exact discrete
measurement and state the real cause: `n` increments by 1 while `p` jumps by `g`, a
**discreteness** phenomenon no smooth model can deliver — note §3.6's smooth model says
the opposite (100% monotone increasing) and the tension is never seen. The 55.9% figure
itself is sound and computed on the true `T_n`; keep it, fix the explanation under it.

### Tier 3 — reprioritisations for the legs named in §9.

**13. Reprioritise the Lean legs: promote L2 and L5, keep L4 with corrected billing.**
"L4 is the only node that is a genuine theorem" is **false, 5/5 unanimous**
(`synthesis.md` C4, D4): L2, L5 and L6 are theorems. Three panelists add the structural
kill — **L4 contains no primes**; it is a calculus lemma that would be true if primes did
not exist, and **no other node in §6 can consume it**, because the bridge from
`(x log x)^{1/x}` to `p_n^{1/n}` is itself a missing node (add it: an effective
`p_n = n(log n + log log n − 1) + E_n` with a bound on `E_n`, since F's entire content
lives in `E_n`). §6's own "honest expectation (ii)" — a machine-checked equivalence chain
so no leg silently uses a wrong reformulation — names **L2**, which the same section
demotes to non-theorem two paragraphs later; the wrong side won. *What must change:*
promote L2 and L5 to primary deliverables; keep L4 and restate its billing as feynman
frames it — *the only node whose content is independent of F*, the only mathematics that
survives whichever way the conjecture goes, which is a real argument for keeping it and
not the one §6 makes. Caveat from popper: L5 re-imports `Real.exp` and the index into the
statement L1 was designed to keep in ℕ, so its "medium" effort tag is assigned by analogy
and must be sized by `lean-probe`, not assumed.

**14. Correct §5.2's Lean blocker diagnosis — right conclusion, wrong reason, different
fix.** `Nat.nth` is **`noncomputable`**, not merely inefficient to kernel-reduce (knuth).
`decide` cannot reduce it at all; there is no efficiency dial, which is why Mathlib
hand-proves `nth_prime_zero_eq_two` … `nth_prime_four_eq_eleven` and stops at index 4.
Consequences: the proposed workaround (prime literals + `Nat.Prime` certificates) is
necessary but **not sufficient** — you additionally need `Nat.count ↔ Nat.nth` bridging
lemmas, and that per-`n` cost is what caps `N` in L3, not `norm_num`'s bignum speed; and
the total cost is linear in `p_N`, not `N`, because "no prime strictly between" requires
compositeness of every integer in each gap. Note this is §8.8's second self-caught
correction being itself corrected — §5.2 writes the non-reducibility point as *superseding*
the digit-size point, when both bite at different `N`.

**15. Redirect the citation gate's priority — and do not stop at existence.**
Two adjustments. (a) **A9 stays the priority, and A10 joins it.** The panel reversed one
of §4.3's implicit priorities: the `O(1/L)` in Claim A has known sign and coefficient
(`T_n = L² − L − 1 − 3/L + O(1/L²)`) and is `8·10⁻⁵` in `g/L²` units at `L ≈ 35` —
**625× smaller than the 5% margin** (knuth; popper independently `≈ 2·10⁻³ %`). So *the
margin is anchor-limited, not analysis-limited*: A10's record figure is what the fragility
narrative rests on, and further asymptotics buy nothing. Also correct the unit — §3.8
conflates `g/T` (`0.7605`) with `g/L²` (`0.92`) in a single clause, and §3.8 is a
recommended `proof-attempt` target. In ρ units the recalled record is **`ρ = 0.9485`** at
`p = 1693182318746371`, `g = 1132`; carry that number, not 0.92. (b) **Add a node for
auditing the heuristic, not just its citation** (godel). §9 dispatches only a check that
A9 exists. A leg that confirms A9 verbatim will have confirmed nothing about whether the
tension in S5 is *real* at log-power scale — which is precisely the scale where the
Cramér model is a known-unreliable guide, and the historical reason Granville corrected
it. That is an archetype gap, not a citation gap, and §7's risk table cannot see it
because it grades attribution only.

**16. Retag S2, adopting the weaker of the two panel readings.**
The panel divided (`synthesis.md` D3). knuth and feynman: S2 is **dead** — no limsup or
tail hypothesis can imply a for-all-`n` statement with no tail-tolerance, so any
sufficient `H` literally contains F-for-large-`n`, and §3.2's obligation on downstream
legs is *unsatisfiable*, not merely demanding. godel: the dichotomy is right (limsup-type
= too weak; uniform-in-`n` = the target) but a legitimate hypothesis could live **in the
gap** — a density or short-interval hypothesis that is uniform but not pointwise — and
§3.2's real failure is not locating that gap. *Recommendation: adopt godel's reading,
because it is strictly weaker and costs nothing.* Retag S2: *"not viable via limsup or
pointwise hypotheses; open only for uniform-not-pointwise forms, which must be exhibited
before any effort is spent."* This retires the unsatisfiable obligation without asserting
a closure the panel did not establish. Note the panel did **not** resolve this; the
recommendation is a conservative default, not a verdict.

**17. Repair the provenance of §5.1 and the committed scripts.**
Three §5.1 rows are produced by **no committed script** — the exact-integer check for
`n = 1…59` (no bignum arithmetic in either file), the `T_n < L_n²` check, and the
record-intersection for the six tightest ρ. All three are **true** when independently
verified (knuth ran the 943 550-digit comparison at `n = 149689`; it holds). And
`attack/probe.py:27` computes `max g/log²p` over all `n` and prints `2.081 at p = 2`,
whereas the table reports `0.703 at p = 2010733` for `n ≥ 10` — a re-runner sees a number
matching no table row. These are provenance defects, not factual errors, but a tier-L1
"verified in-run" label on a row no artifact produces is exactly what §0 exists to
prevent. *What must change:* restrict `probe.py:27`'s generator to `i ≥ 9`; add the three
missing checks to the committed scripts, or downgrade those rows from tier L1.

---

## What must NOT change

Recorded because a stress-test that only subtracts is miscalibrated, and because §9 is
right that compression will attack these first.

- **The F1–F4 equivalence chain (§1.2)** — independently re-derived by four panelists,
  correct.
- **Claim A's shape and its numerical convergence (§1.3, §5.1)** — correct; the term-wise
  inversion of the π expansion verified independently by three panelists.
- **The T3 direction correction (§4.3, §8.8)** — re-derived from scratch by three
  panelists without reference to the document. **T3 is sufficient, not weaker.** The
  correction stands; only its range and tag need work (adjustment 7).
- **The `x ≥ 5` domain in §3.6** — verified; the sign change sits just above `x = 4`.
- **§4.5's refusal to promote T5 into a falsification test** — unanimously the
  best-calibrated paragraph in the file. But see the caution below.
- **Both §4.6 anti-test exclusions** — the Littlewood estimate and the Bertrand item are
  both correct as computations.
- **The P3 gate** — real, correctly placed, and *stronger* than its own argument
  (Chebyshev suffices).
- **§8.7's refusal to say which way F resolves**, and §9's standing instruction. Nothing
  the panel found bears on the truth of the conjecture.

**One caution attached to §4.5.** popper turned it against §4.3: a limsup statement is
invariant under every finite computation, so numerical corroboration — however far
extended — carries *zero* weight against the Cramér–Granville prediction; the two bodies
of evidence are not commensurable. §4.3 then reads one finite datum (record ρ at
`L ≈ 35`) as "the strongest available empirical argument that it is fragile", which
presupposes an unestimated growth law for the record-ρ envelope. That is the promotion
§4.5 forbids, arriving by another door. §8.7's even-handed "heuristic points false,
numerics point true" should say explicitly that the two are not on the same scale.

---

## Recommended follow-up molecules — ENUMERATED ONLY, NOT NUCLEATED

⚠ This formula is a leaf. **No molecules were created.** The following are proposals for
the downstream DAG to honour or discard.

| # | Topic | Kind | Blocked by | Temp | Briefing seed |
|---|---|---|---|:---:|---|
| F1 | Fix the L1 indexing defect in `attack/decompose.md` §6 and add a `p 1 = 2` guard lemma | task | — | **hot** | Mathlib `Nat.nth` is 0-indexed; L1 as written formalizes a strictly weaker conjecture. Adjustment 1. Must land before `lean-skeleton`. |
| F2 | Rewrite P6′ as a pointwise `T`-envelope and discharge it from Dusart-type explicit π bounds | task | F1 not required | **hot** | Four independent measurements say P6′ is empirically unviolated; the document's evidence for it is tautological. Adjustments 2 + 7 share a template. |
| F3 | Numerical-instrument repair: `ρ_n` as the reported statistic, exact/interval arithmetic above `p ≈ 2·10¹⁵`, fix `probe.py:27` | task | — | **hot** | Doubles die below the frontier `notebooks` is asked to pass, and the failure is silent in the verification direction. Adjustments 6 + 17. |
| F4 | Test-suite repair: split T2a/T2b, add the index certificate to T1, retag T3, propagate the bar correction to T4/R2/S3 | task | — | **hot** | Adjustments 4, 5, 7, 8 — all four are edits to `attack/decompose.md` §4 and should land together to avoid a half-corrected §4. |
| F5 | Tree structural repair: weaken §2's framing, add the five missing archetypes, draw the P4 edges, extend the status alphabet | task | F4 | warm | Adjustments 9, 10, 11. Needs F4 first so the new edges point at corrected tests. |
| F6 | Prose corrections: S9's single reason, §4.6's heading, §2.4's differencing, §5.2's `Nat.nth` diagnosis, the RH sentence | task | — | warm | Adjustments 10(a), 12, 14. Low risk, no dependencies, improves every downstream read. |
| F7 | Audit the Cramér–Granville model's applicability at log-power scale — distinct from checking that A9 exists | idea | citation-gate on A9 | warm | godel's archetype gap: confirming the citation confirms nothing about whether S5's tension is real. Adjustment 15(b). |
| F8 | Instantiate or retire R3; add the conditional-refutation node `H ⇒ ¬F` for a rigorous `H` | idea | F5 | cold | 4/5 named conditional refutation as plausibly the most attainable non-trivial R-side result, and it has no slot. |

---

## Named weakest branches — the one-line answer

For a downstream leg that reads only this section: **the weakest points of
`attack/decompose.md`, in order, are L1 (§6 — formalizes the wrong conjecture), P6′ (§2.4
— over-alarmed on a non-diagnostic statistic), the T2 "equivalently" clause (§4.2 — two
inequivalent tests under one label), T1's certificate (§4.1 — omits the index), the §5.1
numerical instrument (dies below the search frontier, silently), T3's tag (§4.3 — warrant
and applicability disjoint), and §2's exhaustiveness claim (false, and the tree cannot
express the conjunctions three missing archetypes require).** The strongest points — the
equivalence chain, Claim A, the T3 direction correction, the §4.6 exclusions, the P3 gate,
and §4.5's discipline — survived five independent attacks and must be preserved through
compression.
