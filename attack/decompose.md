# Firoozbakht's Conjecture — Attack-Surface Decomposition

**Molecule:** `task-20260725-c062` (leg: `decompose`, crew role: concept-writer)
**Run:** `germ-20260725-791a7c45`
**Formal backend requested:** Lean 4 / Mathlib
**Status of the conjecture in this document:** **OPEN — neither assumed true nor assumed false.**
Every statement below is tagged with its epistemic status. Nothing downstream may
build an obligation on an untagged assumption.

---

## 0. Perimeter and provenance (v5.1 clause)

**Inputs admitted to this decomposition:**

1. The problem statement as given in the molecule brief:
   `p(n+1)^(1/(n+1)) < p(n)^(1/n)` for all `n ≥ 1`.
2. Declared literature anchors: **none.** The brief's `Origin/context` field was
   empty and no anchor list was supplied.

**Consequence of (2), stated plainly:** every bibliographic reference in §7 is
recalled from the author's own background knowledge, *not* from a declared or
supplied source. None has been checked against a copy of the cited work in this
run. They are therefore **candidate anchors at tier L3 (unverified recall)** and
MUST be resolved by the downstream `source-ledger` / `citation-gate` legs before
any proof obligation is allowed to rest on them. Obligations in §2 are marked
`[self-contained]` when their justification is derived in this document and
`[needs-anchor]` when it is not.

**External prior art present in the working tree:** none. At the time of writing
the repository at `/Users/eserie/galaxies/firoozbakht-cleanroom` contained only
`.cosmon/` (orchestrator state and formulas) and `.gitleaks.toml`. There is no
mathematical file, note, or draft in the tree. No obligation below is built on
any pre-existing tree content.

**Computational evidence generated in this run:** a sieve to `3·10⁶`
(216 816 primes, 216 815 consecutive pairs checked) executed locally. Outputs are
reported in §5.1 and reproduced by the two scripts committed alongside this file
(`attack/probe.py`, `attack/probe2.py`). This is *own* evidence, tier L1
(verified in-run), and is the only empirical claim in this document that does not
need the citation gate.

---

## 1. Formal restatement

### 1.1 Notation

`p_n` = the n-th prime, `p_1 = 2`. `L_n := log p_n` (natural log).
`g_n := p_{n+1} − p_n` (the n-th prime gap). `π(x)` = prime-counting function;
note `π(p_n) = n` exactly — the threshold couples the gap at `p_n` to the *count*
below it, which is what makes the problem harder than a pure gap bound
(used essentially in §1.3 and §3.9).

### 1.2 The conjecture, four equivalent forms

**(F1) Original (real-analytic).**
> For all `n ≥ 1`:  `p_{n+1}^{1/(n+1)} < p_n^{1/n}`.

Equivalently: the sequence `n ↦ p_n^{1/n}` is strictly decreasing.

**(F2) Logarithmic.**
> For all `n ≥ 1`:  `n · log p_{n+1} < (n+1) · log p_n`,
> i.e. the sequence `n ↦ (log p_n)/n` is strictly decreasing.

**(F3) Purely arithmetic — no reals, no logarithms.**
> For all `n ≥ 1`:  `p_{n+1}^{\,n} < p_n^{\,n+1}`.

**(F4) Gap form.**
> For all `n ≥ 1`:  `g_n < T_n`, where `T_n := p_n·(e^{L_n/n} − 1)`.

**Derivation of the equivalences.** `[self-contained]`
All quantities are positive reals `> 1`, and `t ↦ t^{n(n+1)}` is strictly
increasing on `(0,∞)`; raising (F1) to the power `n(n+1)` gives
`p_{n+1}^{n} < p_n^{n+1}`, which is (F3), and the step is reversible — so
(F1) ⟺ (F3). Taking `log` of (F3) gives (F2), and `log` is strictly increasing,
so (F2) ⟺ (F3). For (F4): (F2) says `log p_{n+1} < log p_n · (1 + 1/n)`, i.e.
`p_{n+1} < p_n·e^{L_n/n}`, i.e. `p_n + g_n < p_n + p_n(e^{L_n/n}−1)`. ∎

**Why (F3) matters for the Lean backend.** (F3) is a statement about natural
numbers only. It needs no `Real.rpow`, no `Real.log`, no analysis import, and it
is *decidable for each fixed n*. This is the form the formalization should take
as its primary definition (§6), with (F1) proved equivalent as a corollary rather
than taken as the definition. Making (F1) primitive would drag `Real.rpow`
monotonicity lemmas into every downstream proof for no gain.

### 1.3 The asymptotic shape of the threshold `T_n`

**Claim A.** `[self-contained, derivation below; numerically confirmed §5.1]`
> `T_n = L_n² − L_n − 1 + O(1/L_n)` as `n → ∞`.

*Derivation.* Write `x = p_n`, `L = log x`, so `n = π(x)`. By the standard
asymptotic expansion of `π`, `π(x) = (x/L)(1 + 1/L + 2/L² + O(L^{-3}))`, hence

```
L/n = L²/x · (1 + 1/L + 2/L² + O(L⁻³))⁻¹
    = L²/x · (1 − 1/L − 1/L² + O(L⁻³)).
```

Then `T_n = x(e^{L/n} − 1) = x(L/n + (L/n)²/2 + …)`. The second term contributes
`x·(L²/x)²/2 = L⁴/(2x) → 0`, and all later terms are smaller still. So

```
T_n = x · L/n + o(1) = L² − L − 1 + O(1/L).   ∎
```

**Corollary A1 (the Cramér-scale reading).** `[self-contained]`
Firoozbakht at index `n` is, up to an `O(1/L)` correction, exactly the assertion

```
g_n < (log p_n)² − log p_n − 1.
```

So the conjecture is a **Cramér-type gap bound in disguise**, and in particular
it implies `limsup_n g_n/(log p_n)² ≤ 1`. This single implication drives almost
the whole strategic picture in §3 and the primary refutation route in §4.

> **Note on an attribution.** A gap bound of exactly this shape
> (`g_n < log²p_n − log p_n − 1` for `n ≥ 10`) is, to the author's recollection,
> stated in the literature as a consequence of Firoozbakht. The derivation above
> is independent of that recollection and is what this document relies on. The
> literature form — in particular the precise index threshold `n ≥ 10` and the
> exact constant — is `[needs-anchor]` (see §7, A3/A4). **Do not** propagate
> "for n ≥ 10" downstream as established; propagate Claim A + Corollary A1,
> which are self-contained but asymptotic.

### 1.4 Negation (what a refutation must exhibit)

`¬F` is a **Σ₁ statement**: there exists `n` with `p_{n+1}^n ≥ p_n^{n+1}`.
A refutation is therefore *finitely certifiable* — a single integer `n` plus the
two primes, with primality certificates, settles it. A proof is Π₁ and admits no
finite certificate. This asymmetry is the single most important structural fact
about the problem and is the reason §3's feasibility verdicts are so lopsided.

---

## 2. Proof-obligation tree

Any complete resolution must pass through these nodes. Status codes:
`[E]` established here or elementary; `[O]` open but plausibly reachable;
`[X]` out of reach with current technology; `[C]` computational.

```
ROOT — Decide F: ∀n≥1, p_{n+1}^n < p_n^{n+1}
│
├── BRANCH P — PROVE F
│   ├── P1 [E]  Equivalence of forms F1–F4                                     §1.2
│   ├── P2 [E]  Threshold asymptotics T_n = L² − L − 1 + O(1/L)                §1.3
│   ├── P3 [X]  Unconditional bound g_n = O(log² p_n)                          §2.1
│   │   ├── P3a [X] beats Baker–Harman–Pintz (g_n ≪ p_n^0.525) by a huge margin
│   │   ├── P3b [X] beats the RH-conditional bound (g_n ≪ √p_n · log p_n)
│   │   └── P3c [X] ⇒ P3 is strictly stronger than RH-conditional technology
│   ├── P4 [O]  Effective, explicit version of P2 (constants, not O-notation)  §2.2
│   ├── P5 [C]  Verification on an initial segment                             §2.3
│   ├── P6 [O]  Reduction of P5 to maximal (record) gaps — NOT trivial         §2.4
│   └── P7 [X]  A mechanism forcing g_n < T_n at *every* n, not on average     §2.5
│
└── BRANCH R — REFUTE F
    ├── R1 [C]  Exhibit n with p_{n+1}^n ≥ p_n^{n+1}  (Σ₁ certificate)         §4.1
    ├── R2 [X]  Prove limsup g_n/log²p_n > 1                                   §4.2
    │   └── R2a [X] current best large-gap results are ≪ log²p_n (§3.3)
    ├── R3 [O]  Refute a *consequence* of F that is easier to attack           §4.3
    └── R4 [O]  Show F contradicts an accepted-but-unproved model              §4.4
                (Cramér–Granville heuristic — refutes F only heuristically)
```

### 2.1 P3 — the load-bearing obstruction

**Obligation.** Any proof of F yields `g_n < L_n² − L_n − 1 + O(1)`, hence
`g_n = O(log² p_n)` unconditionally.

**Why this is `[X]`.** `[needs-anchor for the specific bounds; the comparison
itself is arithmetic and self-contained]` The best known unconditional upper
bound on prime gaps is of the form `g_n ≪ p_n^θ` with `θ ≈ 0.525`
(Baker–Harman–Pintz — §7 A5). Under the Riemann Hypothesis the bound improves
only to roughly `g_n ≪ √p_n · log p_n`. Both are *powers of `p_n`*; the
Firoozbakht requirement is *polylogarithmic in `p_n`*. The gap between
`√p_n log p_n` and `log² p_n` is not a matter of sharpening constants — it is
the difference between square-root-scale and log-scale, which no known method in
analytic number theory bridges even conditionally on RH.

**Verdict this forces.** *Proving Firoozbakht is strictly harder than proving the
Riemann Hypothesis is useful for prime gaps.* Any downstream leg that proposes a
"direct proof" strategy must explicitly say how it clears P3, or it is proposing
something already known to be beyond the field. **This is a hard gate on Branch P.**

### 2.2 P4 — effectivity

The `O(1/L)` in Claim A is asymptotic. Turning §1.3 into a usable tool at finite
`n` requires explicit two-sided bounds on `π(x)` (Dusart-type explicit estimates,
§7 A6) with named validity ranges. Reachable, and a genuine sub-task: it is what
makes P6 and any finite-range verification rigorous rather than numerical.

### 2.3 P5 — verified initial segment

Purely computational; establishes nothing about the general case, but bounds
where a counterexample can live. Own verification in this run reaches
`n ≤ 216 815` (§5.1). Published verification reaches much further —
recollection says `p < 4·10¹⁸` — `[needs-anchor]` (§7 A2).

### 2.4 P6 — the maximal-gap reduction is a real obligation, not a triviality

**The tempting shortcut.** "A violation needs a huge gap, so it suffices to check
`n` at which `g_n` is a *record* (maximal) gap." The intended argument: if `m < n`
is the record index with `g_m ≥ g_n`, and the check passes at `m`, then
`g_n ≤ g_m < T_m ≤ T_n`, done.

**The hidden premise.** That chain needs `T_m ≤ T_n` for `m < n`, i.e. `T`
nondecreasing in `n`.

**`T` is not monotone.** `[self-contained + verified in-run, §5.1]`
Differencing `T_n ≈ p_n·L_n/n` along one step (`p` increases by `g_n`, `n` by 1),
and using `n ≈ p_n/L_n`:

```
T_{n+1} − T_n  ≈  (L+1)/n · g_n  −  p·L/n²  ≈  (L²/p)·(g_n − L).
```

So `T` **increases exactly when the gap exceeds the local average `L = log p_n`,
and decreases otherwise.** Since roughly half of all gaps are below average, `T`
decreases at a constant proportion of steps. The in-run sieve confirms this
directly: **`T` decreases at 121 238 of 216 805 consecutive steps (55.9%)** for
`n ≥ 10`. Monotonicity is false, flatly.

**What survives.** The reduction is still repairable, because `T` grows on the
*coarse* scale (`T ≈ L² − L − 1`, increasing in `p`) even while oscillating on
the fine scale, and record gaps are far apart. The obligation is therefore:

> **P6′.** Prove `T_m ≤ T_n` whenever `m < n` and `p_m, p_n` straddle a record
> gap — using explicit `π(x)` bounds (P4) to control the oscillation — or replace
> the reduction with a direct argument over the full range.

**This node is flagged as a live correctness risk.** Any downstream leg (notably
`lean-skeleton`, `proof-attempt`, `re-attack`) that cites "it suffices to check
maximal gaps" without discharging P6′ is importing an unproved lemma. The
empirical support is good — all six tightest cases found in-run occur *at* record
gaps (§5.1) — but empirical support is not the reduction.

### 2.5 P7 — no induction mechanism

F is a statement about *every* `n`, and `g_n` at index `n` is not determined by,
nor meaningfully constrained by, `g_1 … g_{n−1}`. There is no telescoping and no
self-propagating structure: knowing F up to `n` gives no leverage at `n+1` beyond
locating `p_n`. Any proposed inductive proof must first supply that missing
mechanism. Recording this explicitly so the strategy legs do not rediscover it as
a dead end.

---

## 3. Candidate strategies

### 3.0 Coverage against the standard proof taxonomy

The brief names five archetypes. Mapping, so no archetype is silently skipped:

| Archetype | Strategies below | Verdict |
|---|---|---|
| Direct | S1, S2, S6 | S1/S2 blocked by P3; **S6 viable** |
| Contrapositive | **S8** (necessary conditions on any counterexample) | **viable — and it prunes S4** |
| Contradiction | S3, S5 | S3 blocked; S5 heuristic only, not a proof |
| Construction | **S9** (build a counterexample) | blocked — constructions fall short of `log²` |
| Counterexample search | S4 | viable, not expected to be decisive |
| *(weakening)* | S7 | viable — most likely source of an actual theorem |

### 3.1 S1 — Direct proof (unconditional)
**Route.** Prove `g_n < T_n` for all `n` from prime-distribution estimates.
**Blocked by.** P3. Requires `g_n = O(log² p_n)` unconditionally.
**Verdict: not viable.** Would be a landmark result in analytic number theory,
far exceeding what RH delivers. Listed for completeness and as the gate other
strategies must route around.

### 3.2 S2 — Conditional proof (RH or stronger)
**Route.** Assume RH, or a strong Hardy–Littlewood / short-interval hypothesis,
and derive the gap bound.
**Blocked by.** P3b — RH gives `g_n ≪ √p_n log p_n`, still square-root scale.
**Verdict: not viable under RH.** *Possibly* viable under a hypothesis strong
enough to pin gaps at log² scale — but such a hypothesis is essentially a
restatement of Cramér's conjecture, making the proof circular unless the
hypothesis is independently motivated. **If a downstream leg proposes S2, its
first obligation is to name the hypothesis and show it is not a disguised
restatement of the target.**

### 3.3 S3 — Refutation via a proved large-gap lower bound
**Route.** Prove `limsup g_n/log² p_n > 1`; by Corollary A1 this refutes F.
**Blocked by.** The best known unconditional large-gap results (Ford–Green–
Konyagin–Maynard–Tao lineage, §7 A7) produce infinitely many gaps of size
roughly `log n · log log n · log log log log n / log log log n` — larger than
`log n` by an iterated-log factor, but *asymptotically smaller than `log² n`*.
The shortfall is a full power of `log`.
**Verdict: not viable now.** This is the honest "believed" refutation route and
the one to revisit if large-gap technology ever reaches `log²`-scale.

### 3.4 S4 — Counterexample search (the only computationally live route)
**Route.** Search for `n` with `g_n ≥ T_n`, i.e. `g_n/T_n ≥ 1`.
**Design consequences derived here:** `[self-contained]`
- The search target is not "large gaps" but **large normalized ratio
  `ρ_n := g_n/T_n`**, equivalently `g_n/(L² − L − 1)` up to `O(1/L)`.
- By P6′ (once discharged, or heuristically meanwhile) the search may focus on
  record gaps — an enormous pruning, since record gaps are extremely sparse
  (only 21 below `3·10⁶`, §5.1).
- The search is **not** a search for the largest gap: the ratio `ρ` weights by
  `log² p`, so a moderately large gap at a small prime can beat a huge gap at a
  large prime. In-run, the tightest case is `ρ = 0.7605` at `p = 1327` (gap 34),
  narrowly ahead of `ρ = 0.7591` at `p = 2 010 733` (gap 148) — 3 orders of
  magnitude apart in `p` yet essentially tied in `ρ`. **Ratio, not gap size, is
  the search objective.**
**Verdict: viable but almost certainly not decisive.** The known verified range
already extends far past what this run can reach, and the record `ρ` values grow
extremely slowly. A search leg should aim to *reproduce and extend the ratio
table*, not to expect a hit.

### 3.5 S5 — Contradiction with an accepted heuristic model
**Route.** The Cramér random model, in Granville's corrected form, predicts
`limsup g_n/log² p_n ≥ 2e^{−γ} ≈ 1.1229 > 1` (§7 A8/A9). By Corollary A1 this
is **incompatible with Firoozbakht.**
**Verdict: this is the strongest reason to believe F is FALSE — and it is not a
proof.** It is a heuristic prediction contradicting a numerically robust
conjecture. Both cannot be right. Downstream legs must handle this with care:
- It does **not** license writing "Firoozbakht is false."
- It **does** license writing "Firoozbakht contradicts the Cramér–Granville
  heuristic, and one of the two must fail."
- The constant `2e^{−γ}` and its attribution are `[needs-anchor]` (§7 A9). The
  *structure* of the tension — heuristic limsup `> 1` versus Firoozbakht's
  implied limsup `≤ 1` — is self-contained given Corollary A1.
**This is the single most important item for the `skeptic` and `red-team-corpus`
legs.**

### 3.6 S6 — Separate the smooth part from the fluctuation part
**Route.** Show the conjecture is *provable for the smooth model* and isolate
exactly what the fluctuations must not do.
**Own derivation.** `[self-contained]` For the smooth surrogate
`f(x) = (x log x)^{1/x}` (the PNT first-order model of `p_n`):

```
d/dx [ (log x + log log x)/x ] = [1 + 1/log x − log x − log log x] / x²  <  0
```

for all `x ≥ 5`. (The bracket is checked in-run: `+0.0084` at `x = 4`,
`−0.0193` at `x = 4.05`, `−0.464` at `x = 5` — the sign change sits just above
`x = 4`, so `x ≥ 5` is the safe stated range, **not** `x ≥ 4`.) So **the smooth
model of Firoozbakht is true and elementary.**
**Verdict: viable and valuable — as a *decomposition*, not a proof.** It cleanly
localizes the entire difficulty: F is true for the mean behaviour of `p_n` and
can only fail through fluctuation. It converts the problem into "how large can
the fluctuation of `p_n` around `n log n` be at a single index", which is exactly
P3 again — but it makes precise *which* part is hard, and it gives the
formalization a genuinely provable target (§6, L4).

### 3.7 S7 — Prove a weakened variant
**Route.** Prove something strictly weaker but non-vacuous, e.g.:
- (a) F holds for all `n` outside a set of density 0;
- (b) F holds with `1/(n+c)` in place of `1/(n+1)` for some `c > 1`;
- (c) `p_n^{1/n}` is decreasing *on average* / in the Cesàro sense.
**Verdict: viable, and the most likely source of an actual theorem from this
attack.** Variant (c) is close to S6 and probably provable from PNT with
effective error terms. Variants (a) and (b) need care: they must be checked for
non-vacuity — a weakening that follows from PNT alone with no gap input is a
restatement of S6, not a new result. **Obligation for any leg pursuing S7:
state the weakening and prove it is not implied by the smooth model alone.**

### 3.8 S8 — Contrapositive: constrain any counterexample before hunting it
**Route.** Do not try to prove or refute F. Instead assume a minimal
counterexample `n₀` exists and derive necessary structural conditions on it.
**What is already forced** `[self-contained, from §1.3 + §5.1]`:
- `g_{n₀} ≥ T_{n₀} = L² − L − 1 + O(1/L)` — so `n₀` sits at a gap of
  Cramér scale, i.e. `ρ_{n₀} ≥ 1` where the observed maximum below `3·10⁶` is
  `0.7605` and the recalled record over all known primes is `≈ 0.92` (A10).
- The interval `(p_{n₀}, p_{n₀}+T_{n₀})` is prime-free, so the residues of
  `p_{n₀}+1, …` must cover every small prime modulus — a Jacobsthal-function
  condition. This is a strong sieve-theoretic constraint, not a mild one.
- By §5.1, empirically every tight case sits **at a record gap**; if P6′ is
  discharged this becomes a proof that `n₀` is a record index.
**Verdict: viable, and the highest-leverage item on the refutation side that is
actually actionable now.** It produces no theorem by itself, but it converts S4
from a blind sweep into a targeted search and it is the natural bridge between
the analytic and computational legs. **Recommended as a `proof-attempt` target
alongside L4.**

### 3.9 S9 — Construction of an explicit counterexample
**Route.** Build, rather than find, a long prime-free interval: CRT/Jacobsthal
constructions choose residues to sieve out an interval near a primorial,
guaranteeing a gap of prescribed length.
**Blocked by.** The same wall as S3, from the other side: the best known
constructions (the FGKMT lineage, §7 A7) certify prime-free intervals of length
`≍ log n · log log n · log log log log n / log log log n` — an iterated-log
factor above `log n`, but **a full power of `log` below** the `log² n` a
counterexample needs. Worse, these constructions place the gap at an
*unspecified* location and give no control over the index `n`, whereas F needs
the gap and the count `π(p_n) = n` at the *same* point (§1.1).
**Verdict: not viable.** Recorded because "just construct a big gap" is the
obvious first idea and it fails for two independent reasons — magnitude and
localization — both worth knowing before a leg spends effort on it.

---

## 4. Falsifiability tests

Tests whose *failure* refutes the conjecture, ordered by decidability.

### 4.1 T1 — Direct arithmetic certificate `[decidable, Σ₁]`
> Find `n` with `p_{n+1}^{\,n} ≥ p_n^{\,n+1}`.

A single such `n` refutes F outright. Certificate = `(n, p_n, p_{n+1})` plus
primality proofs for both and a proof that no prime lies strictly between them.
Checkable in Lean by `decide`/`norm_num` for small `n`; for large `n` compare
`n·log p_{n+1}` against `(n+1)·log p_n` in interval arithmetic with certified
error bounds (the naive integer powers are astronomically large — see §5.2).
**Status: no such `n` known. Not found in-run up to `n = 216 815`.**

### 4.2 T2 — Normalized-ratio breach `[decidable]`
> Find `n ≥ 10` with `ρ_n = g_n/T_n ≥ 1`, equivalently (up to `O(1/L)`)
> `g_n ≥ log² p_n − log p_n − 1`.

Equivalent to T1 by §1.2 (F4) but numerically stable and the right form for a
search. **Status: max `ρ` observed in-run = 0.7605 at `p = 1327`.**

### 4.3 T3 — Cramér–Shanks–Granville ratio breach `[decidable, sufficient]`
> Find `n` with `g_n/log² p_n ≥ 1`.

**Direction, stated carefully** (this is easy to get backwards, and an earlier
draft of this document did): since `T_n = L² − L − 1 + O(1/L) < L²` for all large
`n` — verified in-run to hold at every `n ≥ 11` up to `216 815` — a T3 breach
gives `g_n ≥ L² > T_n`, i.e. it **implies** a T2 breach and
therefore **does refute F**. So T3 is *stronger* (harder to satisfy) than T2, not
weaker — it is a **sufficient but not necessary** refutation criterion, and a
conservative one: F can fail without T3 ever being breached, because the true bar
is `T_n`, which sits `≈ L + 1` *below* `L²`.

Consequence for a search leg: **track `ρ_n = g_n/T_n`, not `g_n/L²`.** Using the
CSG ratio as the objective would set the bar too high by `O(L)` and could step
straight over a genuine counterexample.

Calibration. Max `g_n/L²` observed in-run for `n ≥ 10`: `0.70` at
`p = 2 010 733`. Recollection places the record over all known primes near `0.92`
`[needs-anchor, §7 A10]`. The T2 bar expressed in the same units is
`1 − 1/L − 1/L²`, which at `L ≈ 35` is `≈ 0.971`. *If the 0.92 figure is
confirmed, the conjecture survives with a margin of roughly 5%, which is the
strongest available empirical argument that it is fragile.*

### 4.4 T4 — Asymptotic breach `[not decidable, requires a theorem]`
> Prove `limsup g_n/log² p_n > 1`.

Refutes F non-constructively via Corollary A1. Currently out of reach (§3.3).

### 4.5 T5 — Heuristic breach `[not a refutation]`
> The Cramér–Granville prediction `limsup ≥ 2e^{−γ} > 1` contradicts F.

**Explicitly listed as NOT a falsification test** so no downstream leg promotes
it into one. It is evidence about which way to bet, nothing more. Recorded here
because a decomposition that omitted it would misrepresent the state of belief in
the field, and one that promoted it would misrepresent the state of knowledge.

### 4.6 Anti-test — what does NOT bear on F
Recorded to prevent wasted downstream effort:
- **Littlewood oscillation of `π(x) − li(x)` is irrelevant to the threshold.**
  `[self-contained]` Since `T_n` depends on `n = π(p_n)` exactly, one might hope
  the sign changes of `π(x) − li(x)` (amplitude `≈ √x·log log log x/log x`) shift
  the threshold. They do not: writing `L/n = L/(li(x)+Δ) ≈ (L/li(x))(1 − Δ/li(x))`,
  the induced change in `T_n` is `O(L²·log log log x/√x) → 0`. The oscillation is
  far too small to matter at `log²`-scale. **This closes an otherwise attractive
  line of attack.**
- Bertrand's postulate (`p_{n+1} < 2p_n`) is useless here: it implies F only when
  `2 ≤ p_n^{1/n}`, i.e. `p_n ≥ 2^n`, which holds **only at `n = 1`** (`p_1 = 2`)
  and fails for every `n ≥ 2` (`p_2 = 3 < 4`). `p_n^{1/n} → 1`, so the available
  multiplicative room shrinks to nothing.

---

## 5. Evidence generated in this run

### 5.1 In-run computation `[tier L1 — verified here]`

Sieve of Eratosthenes to `3·10⁶`, giving 216 816 primes (largest `2 999 999`),
`n` indexed from `p_1 = 2`. Checks performed on `n·log p_{n+1} < (n+1)·log p_n`
in double precision, and on `ρ_n = g_n/T_n`.

| Quantity | Result |
|---|---|
| Violations of F found | **none**, for `1 ≤ n ≤ 216 815` |
| max `n·log p_{n+1} / ((n+1)·log p_n)` | `0.9999984` at `n = 149 689`, `p_n = 2 010 733` |
| max `ρ_n = g_n/T_n` (`n ≥ 10`) | `0.7605` at `n = 217`, `p_n = 1327`, `g = 34` |
| runner-up `ρ_n` | `0.7591` at `n = 149 689`, `p_n = 2 010 733`, `g = 148` |
| max `g_n/log²p_n` (`n ≥ 10`) | `0.703` at `p_n = 2 010 733` |
| record (maximal) gaps in range | 21 |
| steps where `T` **decreases** (`n ≥ 10`) | **121 238 / 216 805 = 55.9%** |
| (F3) checked as *exact integer* arithmetic | holds for `n = 1 … 59` |
| six tightest `ρ` cases (`p_n` = 113, 1327, 31397, 370261, 492113, 2010733) | **all six verified to be record gaps** |
| `T_n < L_n²` (used in §4.3) | holds at every `n ≥ 11` in range |

Convergence of Claim A, `T_n` vs `L² − L − 1`:

| `n` | `p_n` | `T_n` | `L²−L−1` |
|---|---|---|---|
| 100 | 541 | 35.142 | 32.314 |
| 10 000 | 104 729 | 121.128 | 121.054 |
| 100 000 | 1 299 709 | 182.981 | 183.103 |
| 216 815 | 2 999 957 | 206.366 | 206.517 |

**Three findings worth carrying downstream:**
1. Claim A converges fast — agreement to 4 significant figures by `n = 10⁴`.
2. `T` is **not** monotone (55.9% of steps decrease), so P6′ is a live obligation.
3. All six tightest `ρ` cases occur *at record gaps*, supporting (not proving) the
   maximal-gap reduction.

### 5.2 Numerical hazard for the Lean/verification legs

Form (F3) `p_{n+1}^n < p_n^{n+1}` is the clean *statement*, but a poor *bulk
computation*: at `n = 10⁵` both sides carry `> 6·10⁵` decimal digits. Large-scale
verification must instead use (F2) with certified interval arithmetic on
logarithms, or exact rational bounds on `log`.

**Correction to an easy over-statement** (caught in this run's verification pass):
the integer form is *not* the binding constraint at small `n`. Checked in-run,
(F3) holds as an exact integer comparison for `n = 1 … 59`, and `p_51^52` has
only 124 digits — trivial for bignum arithmetic. For the Lean legs the real
obstacle is different and must not be confused with size: **`Nat.nth Nat.Prime n`
is not efficiently kernel-reducible**, so `decide` stalls on *producing `p_n`*,
not on comparing the powers. The workaround is to supply the primes as literals
with `Nat.Prime` certificates and an explicit "no prime strictly between" lemma,
then let `norm_num` do the comparison. Sizing the feasible `N` in L3 is a job for
the `lean-probe` leg against the pinned toolchain, not a number to guess here.

---

## 6. Lean 4 / Mathlib formalization plan

Available primitives (`[needs-anchor]` — Mathlib API names must be checked
against the pinned toolchain by the `lean-probe` leg before use; names drift):
`Nat.nth Nat.Prime` for `p_n`, `Nat.Prime`, `Nat.bertrand`, `Real.log`,
`Real.rpow`. PNT with error terms is *not* assumed available in Mathlib proper;
if needed it must be sourced from the PNT+ development or axiomatized explicitly
as a hypothesis (and flagged as such).

Formalization targets, in dependency order:

- **L1 — Statement.** Define `p n := Nat.nth Nat.Prime n` and
  `Firoozbakht : Prop := ∀ n ≥ 1, (p (n+1))^n < (p n)^(n+1)`. Arithmetic only.
  *Effort: low. This is the anchor object every other leg must import.*
- **L2 — Equivalence (F3) ⟺ (F2) ⟺ (F1).** Via `Real.rpow` monotonicity and
  `Real.log` strict monotonicity. *Effort: low-medium. Pure API work.*
- **L3 — Finite verification.** `∀ n, 1 ≤ n → n ≤ N → …` for small `N`, via
  prime literals + `Nat.Prime` certificates + `norm_num` (see the §5.2
  correction — the blocker is reducing `Nat.nth`, not the integer sizes).
  *Effort: low. `N` to be sized by `lean-probe`; do not oversell the reach.*
- **L4 — The smooth model (S6).** Formalize: `x ↦ (log x + log log x)/x` is
  strictly decreasing on `[5,∞)`. Real analysis, fully within Mathlib's reach.
  *Effort: medium. **This is the only node here that is a genuine theorem
  rather than a definition or a finite check** — it should be the primary
  deliverable of the Lean legs.*
- **L5 — Gap reformulation (F4).** `Firoozbakht ↔ ∀ n, g n < T n`.
  *Effort: medium.*
- **L6 — Corollary A1 as a conditional.** `Firoozbakht → limsup g_n/log²p_n ≤ 1`.
  Needs effective `π(x)` bounds (P4) — likely must be taken as an explicit
  hypothesis rather than proved. *Effort: high; declare hypotheses openly.*

**Honest expectation.** Lean cannot decide this conjecture. Its value in this
attack is (i) an unambiguous statement, (ii) a machine-checked equivalence chain
so no leg silently uses a wrong reformulation, and (iii) L4. Any leg reporting
"Lean progress on Firoozbakht" must say which of L1–L6 it means.

---

## 7. Candidate literature anchors — ALL UNVERIFIED (tier L3)

**Read §0 before using any of these.** No anchors were declared in the brief;
the following are recalled, not sourced. Each must be resolved (existence,
authorship, year, venue, and — critically — that the cited statement actually
appears at the cited locator) by the `source-ledger` / `citation-gate` legs.
Where a claim is used above, the `[needs-anchor]` tag points here.

| ID | Recalled attribution | What it is claimed to support | Risk if wrong |
|---|---|---|---|
| A1 | Firoozbakht (1982), reported in Ribenboim, *The Little Book of Bigger Primes* (2nd ed., 2004) | Origin and standard statement of the conjecture | Low — statement is given in the brief |
| A2 | Kourbatov, verification of Firoozbakht for primes to `4·10¹⁸` (2015) | The verified range in P5 | Medium — affects claimed search frontier only |
| A3 | Sun / Kourbatov | `Firoozbakht ⇒ g_n < log²p_n − log p_n − 1` for `n ≥ 10` | Low — §1.3 derives the asymptotic form independently; only the explicit index threshold depends on this |
| A4 | — | Converse-direction gap criteria implying Firoozbakht | Medium — do not build on until sourced |
| A5 | Baker, Harman, Pintz (2001), *The difference between consecutive primes, II* | `g_n ≪ p_n^{0.525}`, used in P3a | Low — the qualitative point (power of `p`, not log) is robust to the exact exponent |
| A6 | Dusart, explicit estimates for `π(x)` | Effectivity in P4 | Medium — needed for rigour, not for the strategic picture |
| A7 | Ford, Green, Konyagin, Maynard, Tao — large prime gaps | S3's blocking bound | Low — qualitative point (below `log²`) is robust |
| A8 | Cramér (1936) | `limsup g_n/log²p_n = 1` conjecture | Low |
| A9 | Granville (1995), *Harald Cramér and the distribution of prime numbers* | Corrected heuristic `limsup ≥ 2e^{−γ} ≈ 1.1229` — **the whole of S5/T5** | **HIGH — this is the load-bearing citation of the refutation-side argument. If the constant or its direction is misremembered, S5 collapses.** |
| A10 | — | Record CSG ratio `≈ 0.9206` (gap 1132 at `p ≈ 1.693·10¹⁵`) | Medium — quoted only as "recollection" in §4.3 |
| A11 | Nicholson, Farhadian | Named strengthenings of Firoozbakht | **Statements deliberately omitted** — recalled too vaguely to state safely |
| A12 | Oliveira e Silva, Herzog, Pardi (2014) | Primes enumerated to `4·10¹⁸` (basis for A2) | Low |

**A9 is the priority for the citation gate.** Everything else can be
downgraded to "qualitative" without damaging the decomposition; A9 cannot.

---

## 8. Declared gaps in this decomposition

Stated so no downstream leg mistakes silence for coverage.

1. **No anchors were supplied and none were verified in-run.** §7 is recall.
2. **P6′ (maximal-gap reduction) is open and was found to be non-trivial here.**
   Empirically supported, not proved. Treat as a hypothesis.
3. **Claim A's `O(1/L)` is not made effective.** P4 is stated, not discharged.
4. **The `n ≥ 10` threshold in the literature gap-form is not established here** —
   only the asymptotic form is.
5. **A11's strengthenings are omitted rather than guessed.** A decomposition that
   guessed them would look more complete and be less true.
6. **The in-run sieve reaches only `3·10⁶`** — about *twelve* orders of magnitude
   short of the recalled published frontier (`4·10¹⁸`, A2). It is a sanity probe,
   not a verification, and must never be cited as one.
7. **No claim is made about which way the conjecture resolves.** The heuristic
   evidence (S5) points to false; the numerical evidence points to true; both are
   reported, neither is adopted.
8. **Two sign/direction errors were caught by this document's own verification
   pass and are recorded rather than hidden:** the T3-vs-T2 implication direction
   (§4.3 — T3 is *sufficient*, not weaker) and the domain of the smooth-model
   derivative (§3.6 — `x ≥ 5`, not `x ≥ 4`). Both are the kind of slip that
   survives review because it reads plausibly. Downstream legs should re-derive
   rather than trust §1.3, §3.6 and §4.3 on sight.

---

## 9. Recommended next legs

| Leg | Task | Rationale |
|---|---|---|
| `source-ledger` / `citation-gate` | Resolve §7, **A9 first**, then A2/A3/A10 | S5 and the verified-range claim rest on them |
| `lean-skeleton` | L1, L2, L3 | Pins the statement so no leg drifts |
| `lean-probe` | Confirm Mathlib API names on the pinned toolchain | §6 names are unverified |
| `proof-attempt` | **L4 (smooth model)**, S7(c), and **S8 (constrain any counterexample)** | The only nodes with a realistic result at the end |
| `notebooks` | Extend the `ρ_n` record table past `3·10⁶`; test P6′ empirically at scale | Directly attacks the two live obligations |
| `skeptic` / `red-team-corpus` | Attack S5's framing and P6′ | The two places this decomposition is most likely wrong |
| `synthesize` | Must preserve the P3 gate and the S5-is-not-a-proof distinction | The two claims most likely to be lost in compression |

**Standing instruction to all downstream legs:** the conjecture is **open**.
Do not write "Firoozbakht is true" (no proof exists, and P3 shows none is near)
and do not write "Firoozbakht is false" (S5 is a heuristic, T5 is not a test).
The defensible sentence is: *Firoozbakht's conjecture is numerically robust over
the verified range and simultaneously incompatible with the standard
Cramér–Granville heuristic; at least one of the two must fail, and no current
technique can say which.*
