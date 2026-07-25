# Synthesis — panel stress-test of `attack/decompose.md`

**Molecule:** `delib-20260725-07fc` (step 3/4) · **Run:** `germ-20260725-791a7c45`
**Artifact:** `attack/decompose.md` (+ `attack/probe.py`, `attack/probe2.py`)
**Panel:** wheeler · feynman · godel · popper · knuth (auto-selected, `panel=auto`)
**Frame:** `frame.md` — 7 strates Q1..Q7, per-persona substitution hypotheses

All five ran independent numerics. Four re-sieved to `3·10⁶`; one (knuth) additionally
ran 60-digit mpmath and an exact 943 550-digit bignum check. **No panelist found a
factual error in any number the document reports.** Every finding below is about
what those numbers do not license, or about statements the document makes around them.

---

## 1. Per-persona summaries

### wheeler — *lead Q1 (completeness), Q7 (ranking)*
Attacked the shape of the tree rather than its contents. Central claim: **§2 is drawn
as a tree, but a proof is a join** — a tree expresses alternatives and refinements, it
cannot express "node A AND node B together discharge the root." Three of his four
completeness holes are conjunctions of nodes that already exist separately (notably
the **P4 ∧ P5 join** — prove for `n > N₀` with `N₀` named, machine-check below it,
which is the shape of nearly every explicit theorem in this area, and which §2.3
forecloses in one sentence that is true of P5 alone). Measured the **dip amplitude**
of `T` (0.55 falling to 0.018 across decades, against margins rising 5.3 → 47) and
concluded the document's alarm over P6′ is its **largest calibration error** — priced
as a research risk, actually a Dusart lookup. Also: `§5.1`'s headline ratio decays like
`0.9/n` and hits double epsilon near `n ≈ 4·10¹⁵`, below the frontier §9 asks the
search leg to pass.

### feynman — *lead Q5 (quiet assumptions), Q6 (verdict calibration)*
Diagnosed the meta-pattern: **the tagging discipline audits provenance, never
modelling.** Every tag answers "did I read this somewhere?"; none answers "what did I
assume to write this down?" Showed §2.4's differencing is **order-dependent** —
substitute `n = p/L` *before* differencing and you get 100% monotone increasing;
substitute after and you get 55.9% decreasing; the document performs one order and
never notes the order is load-bearing. Showed §5.1's `0.9999984` is a **1/n artifact**
that would read the same in a universe where every gap were 2. Counted the label
inflation: **31 labels over roughly 10 distinct mathematical objects** (S3=R2=T4,
S4=R1⊇T1=T2, S5=R4=T5, S1=P3, S6=L4). Strengthened P3 in the document's favour:
its `[X]` gate needs only Chebyshev, not the undischarged Claim A.

### godel — *lead Q2 (non-circularity), Q4 (classification)*
Refused the independence-of-PA substitution in Q2 as instructed, and instead cleared
all three named suspects individually: **the tree is well-founded; its defects are
edge-omissions and mis-attributions, not cycles.** Reframed S2's problem as a
**dichotomy, not circularity**: any Cramér-scale hypothesis is either limsup-type
(too weak to reach any finite `n`) or uniform-in-`n` (equal to the target); §3.2's
instruction to downstream legs points at no target because it never locates the middle.
Ran the diagnostic P6′ test the document never ran — `T_{m(n)} ≤ T_n` at **all 216 794
pairs, zero exceptions.** Found the **L1 off-by-one** (below). Found three broken
cross-references in §2's central diagram (R2→§4.2, R4→§4.4, R3→§4.3 all point at the
wrong section).

### popper — *lead Q3 (teeth), Q4 (classification)*
Did the implication check test by test rather than grading falsifiability. Verdicts:
**T1 = ONLY-IF the index is certified; T2a = YES exactly; T2b = ONLY-IF `T_n ≤ L²−L−1`,
which is false for small `n`; T3 = ONLY-IF `T_n < L_n²`; T4 = YES; T5 = NO.** Measured
the T2b sign flip: **733 flips over `5899 ≤ n ≤ 52371`** — so the surrogate is not
conservative in either direction. Sharpest single framing in the panel: **T3's warrant
and T3's applicability are disjoint sets** — sufficiency verified on `11 ≤ n ≤ 216815`,
where `max g/L² = 0.703` makes a T3 breach impossible. Turned §4.5 back on the document:
a limsup statement is invariant under every finite computation, so §4.3's reading of one
finite datum as evidence of *fragility* is the promotion §4.5 forbids, by another door.

### knuth — *lead Q5, Q6, Q3*
Did the code audit *and* carried it into the verdicts. Extended Claim A one term:
**`T_n = L² − L − 1 − 3/L + O(1/L²)`** — the `O(1/L)` has known sign and coefficient,
and at `L ≈ 35` it is `8·10⁻⁵` in `g/L²` units, **625× smaller than the 5% margin.**
Conclusion that reverses a priority: *the margin is anchor-limited (A10), not
analysis-limited.* Gave the record in the right unit: `ρ = 0.9485`, not `0.92`.
Proved `T_n < L_n²` unconditionally for `x ≥ 599` from Rosser–Schoenfeld/Dusart in four
lines. Found the **L1 off-by-one** independently. Found that **`Nat.nth` is
`noncomputable`**, not merely slow — which changes §5.2's proposed fix, not just its
wording. Found three §5.1 rows that no committed script produces (all three true when
independently verified) and that `probe.py:27` prints a number matching no table row.

---

## 2. Convergences — where the panel agrees

Ordered by force. "n/5" counts personas that reached the finding independently.

**C1 — L1 is off-by-one against Mathlib's 0-indexed `Nat.nth`, and the formalized
proposition is strictly weaker than Firoozbakht. (2/5: godel, knuth — independently,
with matching algebra.)**
`Nat.nth Nat.Prime 0 = 2`, so the document's `p n` is its own `p_{n+1}`. L1 as written
asserts `p_{m+1}^{m−1} < p_m^{m}`, i.e. exponent ratio `1 + 1/(m−1)` where F needs
`1 + 1/m`. Since `1 + 1/(m−1) > 1 + 1/m`, **a Lean development could go green having
formalized a different, weaker conjecture**, and it additionally drops `m = 1`. §6's
`[needs-anchor]` is scoped to API *names*; this is *semantics* and survives any name
check. L1 is the anchor object L2, L3, L5 all import. **Only 2/5 found it because only
2/5 audited §6 at that depth — the two who did agree exactly. Highest severity in the
deliberation.**

**C2 — T1's certificate omits `π(p_n) = n`, and §1.4's "finitely certifiable" is false
as written. (3/5: popper, godel, knuth.)**
The exponents *are* the index. Primality has succinct certificates; primality **rank**
has none known — verification costs a full sieve or `Õ(x^{2/3})`. The omission fails in
the dangerous direction: `T_n` decreases in `n`, so an overstated index *lowers the bar*.
§1.1 states the reason ("`π(p_n) = n` exactly — the threshold couples the gap to the
count") and §4.1 forgets it three sections later. Popper supplies the repair the
document misses: **a certified lower bound `N ≤ π(p_n)` suffices**, because lowering the
index only raises the bar — so `R1/T1 depends on P4`, an edge §2 does not draw.
Consequence nobody in the document drew: extending the ρ table is an **exhaustive-sieve
project**, not a spot search.

**C3 — "Proving Firoozbakht is strictly harder than proving RH is useful for prime gaps"
is an overreach. (5/5, unanimous.)**
All five accept the *strength* comparison (F yields an unconditional polylog gap bound
not known to follow from RH) and all five reject the *difficulty* ordering. F and RH are
incomparable; no partial order is supplied; "strictly" would additionally require
knowing no easier route exists. Feynman: the classic error of treating
implication-strength as proof-difficulty. Wheeler adds the cost — §2.1 elevates this to
"a hard gate on Branch P" and the asymptotic gate is then used to prune a **finite-range**
route (the P4∧P5 join) it does not touch.

**C4 — "L4 is the only genuine theorem in L1–L6" is false, and the priority it sets is
inverted. (5/5, unanimous on false; 4/5 on the priority.)**
L2, L5 and L6 are theorems. Wheeler, godel and knuth converge that **L4 contains no
primes at all** — it is a calculus lemma that would be true if primes did not exist —
and knuth adds the structural kill: **no other node in §6 can consume it**, because the
bridge from `(x log x)^{1/x}` to `p_n^{1/n}` is itself a missing node. §6's own "honest
expectation (ii)" — a machine-checked equivalence chain — names L2, which the same
section demotes to non-theorem two paragraphs later. **Divergence on the replacement is
recorded in D3.**

**C5 — T3's `[decidable, sufficient]` tag is wrong as stated, the exception set is
`{1..7, 10}`, and the fix is four lines. (4/5: feynman, wheeler, godel, knuth — all four
computed the same exception set independently.)**
`T_n ≥ L_n²` at exactly `n ∈ {1,…,7, 10}`; note `n = 8, 9` pass and `n = 10` fails, so
`n ≥ 11` is not a monotone crossing and an induction from a base case will not find one
where it looks. godel adds that T3 as written is **satisfied right now at `n = 1, 2, 4`**
by a conjecture that holds there. Popper's framing is sharpest: **warrant and
applicability are disjoint** — the range where sufficiency is verified is the range where
the test cannot fire. Knuth supplies the complete unconditional proof (`π(x) > x/L + L`
suffices; Rosser–Schoenfeld gives it for `x ≥ 599`, i.e. `n ≥ 109`; `11 ≤ n ≤ 108` by
finite check). **T3's sufficiency is a P4 client, and §2 draws no edge.**

**C6 — The document's only computationally live search is pruned by its own undischarged
lemma, in violation of its own gate. (4/5: feynman, wheeler, godel, popper.)**
§2.4 says any leg citing "it suffices to check maximal gaps" without discharging P6′
"is importing an unproved lemma." §3.4 then writes "by P6′ (once discharged, **or
heuristically meanwhile**)". Consequence nobody in the document states: **a null result
from a pruned S4 establishes "F holds at record indices", not F.** Popper names the
laundering risk — if that null is later reported as a verification height, the
undischarged assumption has been converted into evidence for the search design that
assumed it. Wheeler adds the evidential loop: the pruning rule and the search it prunes
draw on the same sieve range, over which the answer is already known.

**C7 — P6′ is over-alarmed, and the evidence offered for it is non-diagnostic.
(4/5: wheeler, godel, popper, knuth — via four different measurements, all clean.)**
The document reports "T decreases at 55.9% of steps" and calls P6′ "a live correctness
risk" and one of "the two places this decomposition is most likely wrong." Four
panelists measured the quantity the reduction actually needs:

| persona | measurement | result |
|---|---|---|
| wheeler | max dip of `T` below its running max, per decade | 0.55 → 0.018, decays as `O(1/L)` while margin grows as `L` |
| godel | `T_{m(n)} ≤ T_n` for `m(n)` the governing record index | **0 exceptions in 216 794 pairs** |
| popper | pairs (record `m`, later `n` in block) with `T_n < T_m` | **0 across all 21 record blocks**; max drawdown 0.5487 = 1.23% of `T` |
| knuth | is "6 tightest ρ are records" informative? | **no — 59/59 structural**; ρ at fixed gap is maximal at first occurrence *because* `T` grows coarsely, i.e. the observation restates the uncontested half of P6′ |

Knuth also shows the "six" is `probe2.py:13`'s `best[:6]` cutoff — it breaks at 8/10 and
collapses to 15/100. **So: the document's stated evidence carries zero weight, and the
evidence it never gathered is strong.** Wheeler's verdict — "a Dusart lookup, not a
research leg" — is the panel's position.

**C8 — The tree is not exhaustive; §2's framing sentence is false. (5/5.)**
Archetypes with no node, by count: **independence as a route to establishing F** (4/5 —
for a Π₁ sentence, independence from a sound theory entails truth in ℕ, and §1.4 supplies
the premise in its own words without drawing the inference); **conditional refutation
`H ⇒ ¬F` for a rigorous `H`** (4/5 — Branch P has a conditional node, Branch R has only
unconditional and heuristic; this is plausibly the most attainable non-trivial R-side
result); **the P4 ∧ P5 join** (3/5); **strengthening for inductive traction** (3/5 — the
standard cure for the exact diagnosis that makes P7 `[X]`, and §3.0 has "weakening" with
no mirror); **non-constructive single witness** (3/5 — R1 is constructive, R2 is
asymptotic, the middle is empty, and refuting a Π₁ statement needs one witness, not a
limsup). Feynman and knuth independently reach the structural cause: F is one inequality
with **no internal structure to decompose** (P7 concedes it), so a tree over it
triple-counts — 31 labels over ~10 objects.

**C9 — R3 is empty and R4 is already discharged. (5/5 on R3 being unsupported; 4/5 on
R4 being `[E]` not `[O]`.)**
R3 names no consequence of F other than the gap bound, and refuting *that* is R2 `[X]`.
Feynman adds that every T3 witness is a T1 witness at a *higher* bar, so R3-via-§4.3 is a
strictly harder version of R1 tagged as an easier route. R4 is executed in §3.5 in five
lines; what remains open is its epistemic weight, which is T5's business. Together these
inflate Branch R from one-wide to three-wide.

**C10 — Double precision dies below the frontier §9 asks the search to reach.
(4/5: wheeler, popper, knuth on the crossover; feynman on the metric being meaningless.)**
Unanimous that the reported `0.9999984` is correct to every digit printed at `3·10⁶`
(knuth: agreement to `2.2·10⁻¹⁷`; safety factor `1.8·10⁹`). Unanimous that it does not
survive: the margin scales as `(1−ρ_n)/n`, verified across five decades by two personas
independently. Crossover estimates: wheeler `n ≈ 4·10¹⁵`, popper `p ≈ 1.2·10¹⁶`, knuth
`p ≈ 2·10¹⁵` (with `1.16` sig-figs of headroom at the A10 record itself and pure noise at
`4·10¹⁸`). All three land **below the recalled published frontier.** Feynman adds the
orthogonal point: the statistic is a `1/n` artifact that would read `0.9999984` in a
universe where every gap were 2, so a leg extending the sieve will report `0.9999999…`
and read it as the conjecture tightening. `ρ_n` has neither problem — `O(1)` operands.
**The failure is silent in the verification direction** (`probe.py` breaks only on a
detected violation), which is the dangerous one.

**C11 — S9 is blocked for one reason, not two. (3/5: feynman, wheeler, popper.)**
Magnitude is fatal. Localization is not: `T_n` depends on the index only through `L/n`,
which is pinned by `x` to within precisely the error §4.6 computes and dismisses as
negligible. **The document's own anti-test dissolves its own second blocking reason.**
Wheeler adds that S9 and S3 are then the same wall from two sides, so §3.0's table shows
two archetypes covered where one obstruction operates.

**C12 — §4.6's Littlewood exclusion is correct and its heading over-scopes. (4/5 verified
the estimate; 2/5 flagged the scope.)** All who checked re-derived
`O(L²·logloglog x/√x) → 0` and agree. Godel: the estimate bounds the effect on the
**right** side of `g_n < T_n` and the heading claims "what does NOT bear on F" —
prime-deficit regions correlating with large `g_n` are untouched. Popper: the same
computation is **half of a lemma P4 needs**, filed under "dead end."

**C13 — The tagging discipline is not applied to itself. (5/5, with disjoint instances.)**
`[E] [O] [X] [C]` carry no epistemic tag (popper: `[X]` is a forecast about a research
field, forbidding no observation). Claim A is tagged `[self-contained]` while importing a
three-term π expansion (godel). P2 is `[E]` in §2 and an axiomatization candidate in §6
(godel). §3.8 conflates `g/T` and `g/L²` units in one clause — `0.7605` against `0.92` —
and §3.8 is a recommended `proof-attempt` target (godel; knuth gives the conversion:
A10 in ρ units is **0.9485**). Three §5.1 rows are produced by no committed script, and
`probe.py:27` prints a number matching no table row (knuth; all rows true when checked).

---

## 3. Divergences — and what they decide

**D1 — How big is the `O(1/L)` slack, and does it endanger the 5% margin?
feynman says yes; knuth and popper say no, with numbers.**
Feynman: `O(1/L)` at `L ≈ 35` is "a 3% error against a claimed 5% margin" — "the single
most dangerous sentence-level defect." Knuth extended the expansion and measured it:
`T_n = L² − L − 1 − 3/L + O(1/L²)`, so in `g/L²` units the slack is `8.03·10⁻⁵` at
`L ≈ 35` — **625× smaller than the 5% margin**, and the correction *widens* the margin.
Popper independently reaches `≈ 2·10⁻³ %` at that scale.

**Resolution: knuth and popper are right about the regime that matters, and feynman is
right about the regime the document talks about.** The two are not in conflict once
separated by scale — the substitution error is `+16.0%` at `p = 113`, `+2.74%` at
`p = 1327`, `−0.087%` at `p = 2·10⁶`, and negligible at `L ≈ 35`. Five of the document's
six headline tightest cases sit at `p < 5·10⁵`. **So the slack is larger than the
fragility margin exactly where the document's rhetoric lives, and negligible exactly
where a counterexample would live.** Decision-relevant consequence, which no single
panelist stated alone: *the 5% margin is anchor-limited (A10), not analysis-limited* —
the citation gate matters here, further asymptotics do not.

**D2 — What is the correct threshold in §2.4's differencing: `L`, `L−1`, or `L−2`?
feynman says `L−1`; knuth says `L−2`.**
Both agree the document's "**exactly** when the gap exceeds `L`" is false. Feynman kept
the `(1+1/L)` term the document drops and got `g > L − 1`, measuring 97.21% sign
agreement against the document's 92.93%. Knuth went further and found the answer depends
on which surrogate for `n` you insert — `n = p/L` gives `L − 1`, the correct first-order
`n = p/(L−1)` gives `L − 2` — and measured all four: misclassification `7.07%` (`L`),
`2.79%` (`L−1`), **`0.29%` (`L−2`)**, `7.19%` (`L−3`). Knuth's decisive corroboration:
the three thresholds predict decrease-fractions `62.99% / 58.71% / 55.63%`, and the
document's own measured figure is **55.9%** — which the document reports as confirmation
of the rule that predicts 63%.

**Resolution: knuth's `L − 2` is better supported.** But feynman's deeper point survives
both and is the one that should propagate: `n ≈ p/L` carries relative error `1/L ≈ 7%`,
the same order as the terms being disputed, so **the derivation cannot resolve `L` from
`L−1` from `L−2` at all.** The right move is not a better constant — it is to drop the
smooth derivation and cite the exact discrete measurement. The non-monotonicity of `T`
is true *by measurement*, and it is a **discreteness** phenomenon (`n` increments by 1
while `p` jumps by `g`) that no smooth model can deliver — feynman notes §3.6's smooth
model says the opposite (100% monotone increasing) and the tension is never seen.

**D3 — Is S2 dead, or is there an unexamined middle? knuth says dead; godel says middle.**
Knuth: **no limsup or tail hypothesis can imply F**, because F is for-all-`n` with no
tail-tolerance; any sufficient `H` literally contains F-for-large-`n`. Therefore S2 is
closed and §3.2's obligation on downstream legs is unsatisfiable, not merely demanding.
Feynman reaches the same conclusion from Corollary A1. Godel agrees with the dichotomy
(limsup-type = too weak; uniform-in-`n` = the target) but insists a legitimate hypothesis
could live **in the gap** — a *density* or *short-interval* hypothesis that is uniform
but not pointwise — and that §3.2's failure is not locating that gap.

**Not resolved by the panel, and it changes what the DAG does.** Under knuth's reading
S2 is retagged "not viable" and closed. Under godel's, S2 stays open with a *named*
target (uniform-not-pointwise hypotheses). **Recommendation: adopt godel's reading,
because it is strictly weaker and costs nothing** — retag S2 "not viable via limsup or
pointwise hypotheses; open only for uniform-not-pointwise forms, which must be exhibited
before any effort is spent." That closes the unsatisfiable obligation without asserting
a closure the panel did not establish.

**D4 — What replaces L4 as the primary Lean deliverable?**
Wheeler: **L5**, because it pins the object every leg reasons about and is where a wrong
reformulation does damage. Godel and knuth: **L2 and L5**, because §6's own stated value
proposition is the machine-checked equivalence chain. Feynman: keep L4's priority but fix
its billing — L4 is "the only node whose content is independent of F", the only
mathematics that survives whichever way the conjecture goes, and that is a real argument.
Popper: L5 is the **highest-risk** node in §6 after L6 and its "medium" effort tag is
assigned by analogy, not by probe.

**Resolution: promote L2 and L5; keep L4, restate its billing as feynman frames it.**
The three positions are compatible once "primary" is separated from "valuable". Popper's
caveat binds: L5 re-imports `Real.exp` and the index into the statement L1 was designed
to keep in ℕ, so it must be sized by `lean-probe`, not assumed.

**D5 — Where exactly do doubles die?** wheeler `n ≈ 4·10¹⁵`; popper `p ≈ 1.2·10¹⁶`;
knuth `p ≈ 2·10¹⁵`. Different definitions of "die" (epsilon crossing vs. one significant
figure remaining). **Not decision-relevant — all three are below the recalled `4·10¹⁸`
frontier, which is the only fact the search leg needs.** Adopt the most conservative
(`p ≈ 2·10¹⁵`) as the stated crossover.

**D6 — Is the tree the right instrument at all?** Feynman argues no: F does not factor
(P7 concedes it), so the honest artifact is a **ledger of what is known and a bound on
what is reachable**, not a DAG; building a tree over a non-decomposable object
manufactures the appearance of parallel workstreams. Wheeler argues the tree is
salvageable but needs to express **joins**. Godel and popper argue for edges and a richer
status alphabet. **Nobody defends the current form.** The panel's centre of gravity is
wheeler's: keep the structure, add conjunction, draw the edges (P4 is the shared
dependency of R1, T3, P6′ and L6, and appears as a Branch-P leaf).

---

## 4. Surprising insights

1. **Two independent corrections run in the artifact's favour.** P3's `[X]` gate needs
   only Chebyshev, not the undischarged Claim A (feynman) — it is more robust than its own
   argument. And P6′ is empirically unviolated by every measurement that bears on it
   (C7) — it is better supported than the document claims, using evidence the document
   never gathered. A stress-test that only subtracted would have missed both.
2. **The document's most careful passage undermines its own strategy elsewhere.** §4.5's
   refusal to promote T5 into a test is unanimously the best-calibrated paragraph in the
   file — and §4.3 then reads one finite datum (record ρ at `L ≈ 35`) as evidence of
   *fragility*, which is the same promotion by another door, since a limsup statement is
   invariant under every finite computation (popper).
3. **§4.6's anti-test refutes §3.9's second blocking reason** (C11) and simultaneously
   contains half of a lemma P4 needs (popper) — a section written to prevent wasted effort
   is doing two kinds of work it does not know about.
4. **The `[:6]` cutoff.** §5.1's finding 3 — "all six tightest ρ cases are record gaps" —
   is exactly `probe2.py:13`'s print truncation. It breaks at 8/10 and collapses to
   15/100 (knuth). A script's display parameter became a stated empirical finding.
5. **`Nat.nth` is `noncomputable`, not slow** (knuth). §5.2's correction — which the
   document is proud of, listing it in §8.8 — has the right conclusion for the wrong
   reason, and the wrong reason changes the fix: you need `Nat.count ↔ Nat.nth` bridging
   lemmas, and the per-`n` cost is linear in `p_N`, not `N`.
6. **§1.4 conflates "finite witness" with "short witness"** (C2), and this single
   conflation is what makes L3 expensive, what makes the ρ-table extension an
   exhaustive-sieve project, and what undercuts §1.4's own claim that the Σ₁/Π₁ asymmetry
   makes §3's verdicts "so lopsided". They are less lopsided than stated: refutation is
   cheap in logical form and expensive in computational form.

---

## 5. Frame-question coverage table

Every Q from `frame.md` accounted for, exactly one mark each. A Q is **Treated** if at
least one persona answered it as framed *and* at least three engaged it substantively.

| Q frame | Treated | Substituted | Declined-with-rationale | Silent |
|---------|:-------:|:-----------:|:-----------------------:|:------:|
| **Q1** — completeness of the proof-obligation tree | ✅ 5/5 | — | — | — |
| **Q2** — non-circularity (3 named suspects + sweep) | ✅ 5/5 | — | — | — |
| **Q3** — teeth: does each test's failure entail ¬F | ✅ 5/5 | — | — | — |
| **Q4** — classification (T3 direction re-derived, ranges) | ✅ 5/5 | — | — | — |
| **Q5** — quiet assumptions (untagged premises) | ✅ 5/5 | — | — | — |
| **Q6** — verdict calibration ([E][O][X][C], P3, S9, L4) | ✅ 5/5 | — | — | — |
| **Q7** — ranking of weakest branches | ✅ 5/5 | — | — | — |

**No Silent marks. No Substituted marks.** All seven strates were treated by all five
personas, each with a `## Qk` heading and, where relevant, an explicit "no comment".

### Substitution-hypothesis audit (against `frame.md` §3)

Each persona is checked against the easier question the frame predicted it would answer
instead. **All five falsifiers came back negative** — but three near-misses are worth
recording, because they show the anti-substitution constraints doing work:

| persona | predicted substitution | outcome |
|---|---|---|
| wheeler | propose a more beautiful framing of Firoozbakht; audit vocabulary instead of coverage | **Not substituted.** Answered Q1 affirmatively with four named holes and the node each needs. Proposed no reframing of the conjecture. |
| feynman | re-derive §1.3/§3.6, find them fine, declare the document sound | **Near-miss, resisted.** He *did* re-derive both — and explicitly said "as instructed, I am not going to report that at length", then went past it to the order-dependence of §2.4 and the 1/n artifact in §5.1. The constraint (§4's "must NOT list assumptions already tagged") is what forced the move. |
| godel | discuss independence of PA/ZFC instead of auditing this tree's circularity | **Not substituted — and the escape is instructive.** He refused the substitution in Q2 as instructed and cleared all three suspects individually. He then raised independence in **Q1**, where it is a legitimate completeness finding rather than an evasion. The frame's constraint routed the observation to the right strate instead of suppressing it. |
| popper | grade the tests for falsifiability-as-virtue; praise §4.5/§4.6 | **Not substituted.** Delivered YES/NO/ONLY-IF per test with the entailment shown. Then turned §4.5 against §4.3 — the opposite of praising it. |
| knuth | stop at a numerics report on `probe.py`/`probe2.py` | **Near-miss, resisted.** He audited both scripts (finding the `[:6]` cutoff and the `probe.py:27` mismatch) *and* carried every finding into a strategic verdict, plus found the L1 off-by-one which is not a numerics finding at all. |

**One prompt-hygiene note, not a finding about the artifact:** the feynman run reported a
trailing `/simplify` directive instructing it to apply edits. It made none — its clearance
was read-only advisory — and nothing in `attack/` was modified by any panelist. Recorded
for the frame step's benefit; all five personas wrote their scratch numerics outside the
repository.

---

## 6. The decision-relevant tension

Compressed to one paragraph, because §9 of the artifact warns this is what compression
loses:

> The decomposition's **conclusions survive the panel almost intact** — the F1–F4
> equivalence chain, Claim A's shape, the T3 direction correction, both §4.6 exclusions,
> the P3 gate, and every number in §5.1 were independently re-derived and hold. What does
> not survive is a layer of **statements made around those conclusions**: an
> exhaustiveness claim that is false, a difficulty ordering against RH that does not
> exist, a "genuine theorem" ranking that inverts the Lean priorities, an alarm over P6′
> calibrated on a statistic that does not bear on it, an empirical finding that is a
> script's print cutoff, and — most expensively — an anchor definition (L1) that
> formalizes a weaker conjecture than the one under attack. **The pattern is consistent:
> the artifact's mathematics is careful and its meta-statements about that mathematics
> are not**, which is exactly the asymmetry its own tagging discipline was built to
> prevent and exactly the asymmetry the discipline does not cover, because every tag it
> uses answers "where did this come from?" and none answers "what did I assume?"
