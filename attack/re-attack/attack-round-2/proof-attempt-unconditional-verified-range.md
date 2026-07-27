# Proof attempt — round 2, subquestion `unconditional-verified-range`

**Molecule:** `task-20260726-2035` (leg `proof-attempt`, round 2, crew role: proofsmith)
**Parent loop:** `reattack-20260726-57d1` (formula `converge-math-attack`, `rounds = 2`)
**Date:** 2026-07-26 · **Formal backend:** Lean 4 / Mathlib (no Lean written by this leg)
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.

> **Status of `F` in this document: OPEN.** Not assumed true, not assumed false. Nothing below
> proves or refutes `F`, and nothing below may be quoted as evidence in either direction.

> ### 🔗 Round-3 reconciliation banner — read this before quoting anything below
>
> A **reconciliation leg** (`task-20260727-264e`, 2026-07-27, round 3) owned the seams between the
> four round-2 artifacts. Its decisions are recorded in **`attack/reconciliation.md`** and are
> **binding on this document**, which has been amended in place where they touch it. The four
> round-2 artifacts, and where each stands after reconciliation:
>
> | artifact | role | status after round 3 |
> |---|---|---|
> | `proof-attempt-first-failure-maximality.md` (FFM) | P6′ predicates, Theorem C-a′/C-b′ | **carries the designated Theorem C-b′**; §4 denominators corrected, §5 gov/min ordering corrected, C-a′ header corrected |
> | `proof-attempt-unconditional-verified-range.md` (UVR) | Lemma H, (A-high\*), Theorem 2, the unconditional range | **Theorem C(b\*) retired to a remark**; Axler tier corrected L2_strong → **L0** |
> | `proof-attempt-RH-conditional-bound.md` (RH) | the RH route, five theorems | unchanged; its §10 sieve count `216 815` is the **correct** one and corroborates decision 4 |
> | `lean-probe-report.md` | the kernel leg + the barrier | clean; §4's slack table annotated (constants restored) |
>
> **The five decisions in one line each.** (1) The corpus's single repaired Theorem C(b) is
> **Theorem C-b′**, `p_m ≤ 0.998244·p_{n₀}`, off the Axler row `(2.1,0,0,0)/6 690 557` present in
> **both** editions; C(b\*) and the constants `0.99553`/`0.99565` are retired. (2)
> `axler2014newbounds` is **L0**, everywhere, with a standing ⚠ that the `(1,0,0,0)/1 772 201` row
> is **preprint-only**. (3) The ledger amendment **had already landed**; R2-B2's "never made" is
> stale, verified against the tree. (4) The `55.92 %` denominators are `216 806` (`n ≥ 10`) and
> `216 815` (all `n`) — a fourth independent recount, against FFM's original table and against both
> prior skeptics. (5) R2-M2, R2-M3, R2-m1, R2-m2 and R2-m4 are applied in place.
>
> **`F` remains OPEN.** Nothing in round 3 moves it; reconciliation removes ambiguity, not
> obstruction.

---

## 0. Perimeter

**Admitted inputs — exhaustively:**

| Input | Provenance |
|---|---|
| `attack/faults.md` (444 lines, read in full) | leg `skeptic`, molecule `task-20260725-488f` |
| `attack/lean-probe-report.md` (279 lines, read in full) | leg `lean-probe`, molecule `task-20260725-9975` |
| `attack/proof-attempt-2.md` (461 lines, read in full) | leg `proof-attempt` #2, molecule `task-20260725-909e` |
| `attack/proof-attempt-0.md` (603 lines, read in full — §6 is where F2 lives) | leg `proof-attempt` #0, molecule `task-20260725-a1cd` |
| `attack/concept-cards/` (pinned, re-used verbatim; `T1`, `L1`, `L4`, `L6`, `D1`–`D5` read at the locator) | leg `concept-cards`, molecule `task-20260725-068e` |
| `attack/source-ledger.md` (rows `dusart2010estimates`, `axler2014newbounds` re-read; ledger **not** re-opened wholesale) | leg `source-ledger`, molecule `task-20260725-d320` |
| `lean/` (FROZEN; inspected read-only, **not modified**) | leg `lean-skeleton`, molecule `task-20260725-5fd9` |
| in-run computation performed **by this leg** | §5; script `attack-round-2/verify-uvr-round2.py` |

**Nothing else was read. No source PDF was opened by this leg.** Every external mathematical fact
is used at the tier the run's own ledger assigned it and is named with that tier at the point of
use. `lean/Firoozbakht/Statement.lean` was **not touched** — the theorem statement is the fidelity
anchor and is frozen for the whole loop.

**Round-1 state this leg inherits.**

- Kernel (`lean-probe-report.md`): **UNPROVABLE_IN_BUDGET**. `lake build` exit 0, grep-clean of
  `axiom` / `native_decide` / `unsafe` / `@[implemented_by]`, exhaustive audit over 60
  declarations, **one** residual `sorry`: `Firoozbakht.firoozbakht : Conjecture`
  (`Statement.lean:186`) — the conjecture itself, correctly open and correctly never attempted.
  This leg does not change that and does not claim to.
- Skeptic (`faults.md`): **2 BLOCKER**, 4 MAJOR, 8 MINOR. This leg's assignment is **F2**.

---

## 1. What this leg was asked to do, and one correction to the framing

The brief assigns this leg the repair of **F2** on the ground that it "touches Theorem C(b), whose
small-`p_m` branch this subquestion's unconditional verification range depends on".

**The dependency runs the other way, and saying so is part of the work.** Stated precisely:

- **The unconditional verified-range theorem does not depend on Theorem C(b), or on Theorem C at
  all.** The chain is `proof-attempt-2.md` Lemma 1 → Lemma 2 (Dusart) → Lemma 3 → Lemma 4 →
  Theorem 2. It uses exactly one external inequality — Dusart Thm 6.9 eq. (6.6), upper half, tier
  **L0** — and it never mentions `(A-high)`, Axler, or `T_m ≤ T_n`. §4 re-audits the whole chain
  line by line against F2 and finds no contact point. Theorem C(b) is, moreover, **Axler-based and
  therefore not unconditional**; it could not be a dependency of an *unconditional* range even if
  the chain did touch it.
- **Theorem C(b)'s small-`p_m` branch depends on a verified-range-shaped object**: an exhaustive
  maximal-gap computation over an initial segment of the primes. That is the real contact point,
  and it is a dependency of C(b) *on* this subquestion's technology, not the reverse.
- **The repair matters to this subquestion for exactly one reason, and it is a sharp one.** The
  size of that finite computation is set by where the analytic branch of C(b) takes over. Under
  the repaired lemma it takes over at `p_m = 1 772 201`. Under the lemma **as printed** it does not
  take over until `p_m = 1.332·10⁹` (§3.7, recomputed here) — a finite obligation **751× longer**,
  with a different governing constant (`288`, not `132`). F2 is therefore, from this
  subquestion's seat, a question about *how much computation a theorem silently orders*.

The concern is recorded; the assigned work is delivered in full. §3 is the F2 repair, §4 is the
verified-range theorem re-audited and restated, §5 is the in-run verification.

**Scope discipline.** F1 (the `m(n)` three-way definition collision) is **not** this leg's
assignment and is not touched. It is also not load-bearing here: nothing below quantifies over a
"governing record index", and §4.6 records that the unconditional range is independent of P6′ under
all three of F1's readings.

---

## 2. Notation and the one elementary primitive

Notation follows cards **D1**, **D2**, **D3**, **D5** and is 1-indexed (`p_1 = 2`); Mathlib's
`Nat.nth` is 0-indexed (**D1** correction #1), which matters only in §7.

```
p_n   the n-th prime, p_1 = 2                                   (D1)
g_n   := p_{n+1} − p_n                                          (D2)
π(x)  prime-counting function,  π(p_n) = n                      (D3)
L_n   := log p_n   (natural log);  ℓ, λ denote such logs
T_n   := p_n (p_n^{1/n} − 1) = p_n (e^{L_n/n} − 1)              (D5)
```

Every effective bound in this attack is produced by one and the same manoeuvre: write
`T_n = x(e^{u} − 1)` with `x = p_n`, `u = ℓ/π(x)`, replace `π(x)` by an effective two-sided bound,
and read off a statement in `ℓ` alone (card **T1**). The manoeuvre needs a two-sided envelope for
`x(e^{t/x} − 1)`, and **the whole of F2 is a failure inside that envelope**. So it is stated once,
proved, and used everywhere below.

> **Lemma H (envelope).** Let `x > 0`.
> **(H-lo)** For every `t > 0`: `x(e^{t/x} − 1) > t`.
> **(H-hi)** For every `t` with `0 < t ≤ x`: `x(e^{t/x} − 1) ≤ t(1 + t/x)`.
> Moreover `t ↦ x(e^{t/x} − 1)` is strictly increasing on `t > 0`.

*Proof.* Put `s := t/x > 0`. (H-lo) is `e^s − 1 > s`, i.e. `e^s > 1 + s`, true for `s > 0` by
strict convexity of `exp` at `0`. For (H-hi), `s ≤ 1` and

```
e^s − 1 − s  =  Σ_{k≥2} s^k/k!  ≤  s² Σ_{k≥2} 1/k!  =  (e − 2)·s²  <  s² ,
```

using `s^k ≤ s²` for `k ≥ 2`, `0 < s ≤ 1`. Multiplying by `x` gives
`x(e^s − 1) ≤ x(s + s²) = t + t²/x = t(1 + t/x)`. Monotonicity is monotonicity of `exp`. ∎

**Two remarks that are the entire content of §3.** (H-hi) has two equivalent shapes, and each
admits its own legitimate weakening, with *different* error terms:

1. **Factored shape** `t(1 + t/x)`. Substituting `t → w` inside the second factor is legitimate
   when `t ≤ w`, and yields `t(1 + w/x)`, whose error term is **`t·w/x`**.
2. **Additive shape** `t + t²/x`. Substituting `t² → w` is legitimate when `t² ≤ w`, and yields
   `t + w/x`, whose error term is **`w/x`**.

The two weakenings are different statements, and their error terms differ by the factor `t`.
Choosing shape 1 while importing shape 2's justification (`t² ≤ w`, i.e. an exponent doubled)
produces a bound weaker than either by that factor. **That composition is exactly the F2 defect**
(§3.1), and it is the only defect: no other step of `proof-attempt-0.md` §6 is affected.

`proof-attempt-2.md` Lemma 3 uses (H-lo); `proof-attempt-0.md` (D-high) and (A-high) use (H-hi).
Both are now instances of one lemma with one proof, which is the smallest structural gain of this
round and the one a Lean transcription benefits from most (§7).

---

## 3. The F2 repair

### 3.1 The defect, diagnosed exactly

`proof-attempt-0.md` §6.1 states

> **(A-high)** `T_n ≤ (ℓ² − ℓ − 1 − 1/ℓ)(1 + ℓ⁴/x)` for `x ≥ 1 772 201`,
> justified as "`T_n ≤ v(1 + v/x) ≤ v(1 + ℓ⁴/x)` using `v < ℓ²`".

The skeptic (F2(a)) is right that `v < ℓ²` yields `v(1 + ℓ²/x)`, not `v(1 + ℓ⁴/x)`. **Round 2
sharpens the diagnosis in a way that changes how the fault should be read**, so the sharper form is
given first and the repair is built on it.

Write `v := ℓ² − ℓ − 1 − 1/ℓ`, `ℓ₁ := log 1 772 201 = 14.3877328349`, `v(ℓ₁) = 191.549619639`.
**Four** distinct upper bars circulate in `proof-attempt-0.md` §6.1 / §6.2 / §9 under the one name
(A-high). Each row's "required `d`" is *solved from Lemma W's hypothesis*, never from a sufficient
condition (§5, V1 / V3 / V3c):

| # | bar | where it appears | true / false | error term at `ℓ₁` | max required `d` | `0.004479` sufficient? |
|---|---|---|---|---|---|---|
| 0 | `v(1 + v/x)` — **tight** | nowhere in PA-0; **(A-high\*)** here | **true** | `0.0207037784` | **0.0043628824** | **yes** |
| 1 | `v(1 + ℓ²/x)` — what §6.1's *stated justification* (`v < ℓ²`) actually produces | §6.1's prose | **true** | `0.0223744850` | **0.0044230138** | **yes** |
| 2 | `v + ℓ⁴/x` — the *additive* weakening (`v² < ℓ⁴`) | implicitly, §6.2's displayed criterion | **true** | `0.0241800103` | **0.0044879973** | **no**, by `9.7·10⁻⁶` |
| 3 | `v(1 + ℓ⁴/x)` — **as printed** | §6.1's displayed lemma | true but ruinous | **4.6316718** | **0.16933981** | **no**, by 38× |

Three consequences, and the first is the one round 2 adds:

1. **Had §6.1's displayed formula matched §6.1's own stated justification, Theorem C(b) would have
   been correct as printed.** Row 1 gives `max d = 0.0044230 < 0.004479`. The defect is a single
   exponent — `ℓ²` written as `ℓ⁴` — in the conclusion of a line whose justification is sound. It
   is not a wrong idea; it is a wrong character, and it costs a factor **38.81**.
2. **§6.1 and §6.2 do not state the same bound.** §6.2's displayed criterion
   `d(2ℓ−1) + d² ≥ 0.17 − 1/ℓ + ℓ⁴/p_m` is row **2** — the *additive* weakening — whose maximum
   required `d` is `0.0044880`, above the quoted `0.004479` by `9.7·10⁻⁶`. **That, precisely, is
   F2(c)**: the constant is not below "the document's own criterion" by accident, it is below a
   criterion derived from a *different* bar than the one §6.1 displays. Three of the four rows
   above appear in one document under one name.
3. **The printed lemma's error term is `223.71×` the tight one** (`4.6317` vs `0.0207`), attenuated
   by `1/(2ℓ − 1)` into the factor `38.81` on the required separation (§3.6).

The repair therefore does not choose between rows 1–3: it goes to row **0**, which needs no
weakening at all (§3.2), and re-derives everything downstream from it.

### 3.2 (A-high\*) — the repaired lemma

> **(A-high\*)** Let `x = p_n ≥ 1 772 201`, `ℓ = log x`, and `v := ℓ² − ℓ − 1 − 1/ℓ`. Then
> ```
> T_n  <  v (1 + v/x)  =  v + v²/x .
> ```
> `[rests on axler2014newbounds Cor. 3.6 (= *Integers* Cor. 3.5), tier **L0** — the source was`
> `fetched, MD5-pinned and read at the locator on 2026-07-26 by the sibling leg`
> `task-20260726-56a7; the ledger row was amended the same day. Tier label corrected in place`
> `2026-07-27 by the round-3 reconciliation leg, decision 2 — it read "L2_strong, NOT OPENED",`
> `which was true when this document was written and is false now.` **⚠ EDITION HAZARD: the**
> **`(1,0,0,0) / x₀ = 1 772 201` row this lemma consumes is present in the arXiv preprint ONLY and**
> **is absent from *Integers* 16 (2016) A22. Do not quote `x ≥ 1 772 201` against the journal**
> **citation.** `See §3.5's retirement notice and attack/source-ledger.md's axler2014newbounds row.]`

*Proof.* Card **T1** quotes Axler Cor. 3.6: `x/(ℓ − 1 − 1/ℓ − 1/ℓ²) < π(x)` for `x ≥ 1 772 201`.
The denominator is positive on that range: at `ℓ = ℓ₁` it equals
`14.3877 − 1 − 0.069504 − 0.004831 = 13.313 > 0`, and `ℓ − 1 − 1/ℓ − 1/ℓ²` is increasing in `ℓ` for
`ℓ > 0`. Hence, with `u := ℓ/π(x)`,

```
u  <  ℓ (ℓ − 1 − 1/ℓ − 1/ℓ²) / x  =  (ℓ² − ℓ − 1 − 1/ℓ)/x  =  v/x .
```

Now `T_n = x(e^u − 1)`, and `t ↦ x(e^{t/x} − 1)` is strictly increasing (Lemma H), so
`T_n < x(e^{v/x} − 1)`. Apply (H-hi) with `t = v`, which requires `0 < v ≤ x`: `v > 0` since
`v(ℓ₁) = 191.5496 > 0` and `v` is increasing for `ℓ ≥ ℓ₁`; and `v < ℓ² < e^ℓ = x`, the last
inequality holding for every `ℓ > 0` because `min_{ℓ>0} e^ℓ/ℓ² = e²/4 = 1.847 > 1`. Therefore
`T_n < x(e^{v/x} − 1) ≤ v(1 + v/x)`. ∎

**No step of this proof weakens anything.** It is (H-hi) applied at the natural `t`, and the whole
of F2(a) is the observation that a weakening was applied there and did not need to be.

### 3.3 The corrected criterion

`proof-attempt-0.md` Lemma W (sandwich) is unaffected by F2 and is restated for completeness; the
skeptic's §5 item 1 confirms it, and this leg re-derived it independently.

> **Lemma W.** Suppose `A(x) ≤ T_n ≤ C(x)` at `x = p_n` for all `n` with `p_n ≥ X₀`. Let `n₀` be
> the least failure of `F` (i.e. least `n` with `g_n ≥ T_n`). Then for every `m < n₀` with
> `p_m ≥ X₀` and `C(p_m) ≤ A(p_{n₀})`, one has `g_m < g_{n₀}`.
>
> *Proof.* `T_m ≤ C(p_m) ≤ A(p_{n₀}) ≤ T_{n₀}`. Since `m < n₀` and `n₀` is *least*, `m` is not a
> failure, so `g_m < T_m`. Chaining, `g_m < T_m ≤ T_{n₀} ≤ g_{n₀}`, the last step because `n₀`
> *is* a failure. ∎

Instantiate `C =` (A-high\*) at `m` and `A =` (A-low) at `n₀`, where (A-low) is
`T_{n₀} > λ² − λ − 1.17` for `p_{n₀} ≥ 2 634 800 823` (Axler Cor. 3.5, `[unopened]`; this is
`proof-attempt-0.md` Fact S2, whose derivation is (H-lo) and is correct). Write `ℓ := L_m`,
`λ := L_{n₀} = ℓ + d` with `d ≥ 0`, and `p_m = e^ℓ`. Lemma W's hypothesis is

```
v + v²/p_m  ≤  λ² − λ − 1.17 .
```

Expanding `λ = ℓ + d` and subtracting `v = ℓ² − ℓ − 1 − 1/ℓ`:

```
λ² − λ − 1.17 − v  =  (ℓ² + 2ℓd + d² − ℓ − d − 1.17) − (ℓ² − ℓ − 1 − 1/ℓ)
                   =  2ℓd + d² − d − 0.17 + 1/ℓ .
```

Hence the hypothesis is **exactly**

```
d(2ℓ − 1) + d²  ≥  0.17 − 1/ℓ + v²/p_m .                                     (★)
```

This is `proof-attempt-0.md` §6.2's displayed criterion **with `ℓ⁴/p_m` replaced by `v²/p_m`**,
which is the replacement the skeptic's repair line prescribes. The left side is increasing in
`d ≥ 0`, so a sufficient condition is

```
d  ≥  d*(ℓ)  :=  ( 0.17 − 1/ℓ + E(ℓ) ) / (2ℓ − 1) ,        E(ℓ) := v(ℓ)² e^{−ℓ} .   (★★)
```

(Using `p_m = e^ℓ` as an identity — `ℓ` *is* `log p_m` — not as the inequality
`p_m ≥ max(e^ℓ, 1 772 201)` that §6.2 wrote.)

### 3.4 Proposition R1 — the uniform constant, in closed form, with no numerical sweep

`proof-attempt-0.md` obtained its sharp constant from a sweep (§9 item 15). The skeptic's F2(ii)
is that this sweep *reproduced* the error instead of catching it, because it was written from the
derivation. The repair therefore replaces the sweep by a proof; the sweep survives only as an
independent check written from the statement (§5).

> **Proposition R1.** On `[ℓ₁, ∞)`, `ℓ₁ = log 1 772 201 = 14.3877328349`, the function `d*` of (★★)
> is bounded by its value at `ℓ₁`:
> ```
> d*(ℓ)  ≤  d*(ℓ₁)  =  0.004363567696…   <  0.004479 .
> ```

*Proof, in three steps.*

**(1) `E(ℓ) = v(ℓ)² e^{−ℓ}` is strictly decreasing on `[ℓ₁, ∞)`.**
`(log E)'(ℓ) = 2v'/v − 1` with `v' = 2ℓ − 1 + 1/ℓ²`, so `(log E)' < 0 ⟺ v − 2v' > 0`. Now

```
q(ℓ) := v − 2v' = ℓ² − 5ℓ + 1 − 1/ℓ − 2/ℓ² .
```

`q(ℓ₁) = 135.98903 > 0` (§5, V2). And `q` is strictly increasing on `[2.5, ∞)`: `ℓ² − 5ℓ + 1` has
derivative `2ℓ − 5 > 0` there, and `−1/ℓ`, `−2/ℓ²` are both increasing. Since `ℓ₁ > 2.5`, `q > 0`
throughout `[ℓ₁, ∞)`. Hence `E` is strictly decreasing. ∎

**(2) A majorant.** By (1), `E(ℓ) ≤ E(ℓ₁) = 0.0207037784` for `ℓ ≥ ℓ₁`, so

```
d*(ℓ)  ≤  φ(ℓ)  :=  ( 0.17 + E(ℓ₁) − 1/ℓ ) / (2ℓ − 1)  =  ( 0.1907037784 − 1/ℓ ) / (2ℓ − 1) ,
```

with **equality at `ℓ = ℓ₁`**.

**(3) `φ` is strictly decreasing on `[ℓ₁, ∞)`.** With `K := 0.17 + E(ℓ₁) = 0.1907037784`,

```
φ'(ℓ)  =  [ (1/ℓ²)(2ℓ − 1) − 2(K − 1/ℓ) ] / (2ℓ − 1)² ,
```

so `φ' < 0 ⟺ 2/ℓ − 1/ℓ² < 2K − 2/ℓ ⟺ 4/ℓ − 1/ℓ² < 2K = 0.3814075568`. The left side is strictly
decreasing for `ℓ > 1/2` (its derivative is `−4/ℓ² + 2/ℓ³ < 0` for `ℓ > 1/2`), and at `ℓ = ℓ₁` it
equals `0.27318386 < 0.38140756` (§5, V2). So the inequality holds throughout `[ℓ₁, ∞)`. ∎

Combining, `d*(ℓ) ≤ φ(ℓ) ≤ φ(ℓ₁) = d*(ℓ₁) = 0.004363567696…` for all `ℓ ≥ ℓ₁`. ∎

> **Corollary R1.1 (sweep-free branch, improved).** For `ℓ ≥ ℓ₁`, `E(ℓ) < 1/ℓ`, hence
> `d*(ℓ) ≤ 0.17/(2ℓ − 1) ≤ 0.17/(2ℓ₁ − 1) = 0.0061205094`.
>
> *Proof.* `v = ℓ² − ℓ − 1 − 1/ℓ < ℓ²`, so `E(ℓ) = v²e^{−ℓ} < ℓ⁴e^{−ℓ}` and hence
> `ℓE(ℓ) < ψ(ℓ) := ℓ⁵e^{−ℓ}`. Now `(log ψ)'(ℓ) = 5/ℓ − 1 < 0` for `ℓ > 5`, and `ℓ₁ = 14.3877 > 5`,
> so `ψ` is strictly decreasing on `[ℓ₁, ∞)`. Therefore
> `ℓE(ℓ) < ψ(ℓ₁) = 0.3478955285 < 1` for every `ℓ ≥ ℓ₁`, i.e. `E(ℓ) < 1/ℓ`, and the numerator of
> (★★) is `< 0.17`. The final step is monotonicity of `0.17/(2ℓ − 1)`. ∎
> *(For calibration: the true value is `ℓ₁E(ℓ₁) = 0.2978804323`; the majorant `ψ` costs a factor
> `1.168` and buys a one-line monotonicity proof.)*

This **improves** `proof-attempt-0.md`'s sweep-free constant from `0.006992` to `0.0061205`, and it
is a strict improvement rather than a repair of an error: `0.006992` is a *valid* bound derived
from the printed lemma's error term `ℓ₁⁴e^{−ℓ₁} = 0.02418`, which the repair replaces by
`E(ℓ₁) = 0.020704` and then discharges against `1/ℓ` entirely.

### 3.5 Theorem C(b\*) — the repaired theorem, **RETIRED TO A REMARK**

> ⛔ **RETIRED — round-3 reconciliation leg (`task-20260727-264e`), decision 1, 2026-07-27.**
> Round 2 repaired round-1's F2 **twice**, in two legs that never cited each other
> (`faults.md` **R2-B1**). This theorem is one of the two; the other is **Theorem C-b′** in
> `attack/re-attack/attack-round-2/proof-attempt-first-failure-maximality.md` §7.4
> (`d ≥ 0.0017569`, `p_m ≤ 0.998244·p_{n₀}`, off the Axler row `(2.1,0,0,0) / x₀ = 6 690 557`).
> **Theorem C-b′ is designated as the corpus's single repaired Theorem C(b). Theorem C(b\*) below
> is retired to a remark and must not be quoted as the run's result.**
>
> **Why C-b′ and not this one — the ground that decides it, not taste.** The Axler row this theorem
> consumes, `(a,b,c,d) = (1,0,0,0)` with `x₀ = 1 772 201`, exists **only in arXiv:1409.1780v3** and
> is **absent from the published *Integers* **16** (2016) A22** (the journal's table has 12 columns,
> the preprint's 14). That was established by two independent byte-level fetches with matching MD5s
> (FFM §7.1 Finding B; `faults.md` R2-B3 confirming it) and is now a standing downstream rule on the
> `axler2014newbounds` row of `attack/source-ledger.md`: *"do not quote `x ≥ 1 772 201` against the
> journal citation. The `(2.1,0,0,0)/6 690 557` row is present in **both** editions and is strictly
> stronger; use it."* C-b′ uses exactly that row. C-b′ is additionally the sharper theorem
> (`0.998244` vs `0.99565`). **This leg wrote its own document; the row it happened to pick is
> edition-fragile, and nothing in the theorem's mathematics is wrong** — the round-2 skeptic
> verified both theorems at 40–50 dps and both stand.
>
> **What this theorem is still good for, and why it is kept rather than deleted.** It is the
> cleanest proof that round 1's conclusion *survived its own broken derivation*: it is the sharp
> statement of what round 1's printed lemma would have ordered, and it shows the printed constant
> `0.004479` was sufficient after all. Read §3.5–§3.7 as **history and calibration**, not as the
> live theorem.
>
> **Every appearance of `0.99565` / `0.9956459` / `0.0043636` in this document, and the finite pair
> `1 772 201 / 132`, is retired with it.** The live constants are `0.998244` / `0.0017569` and the
> finite pair `6 690 557 / 154`. Three constants had been circulating under one theorem name
> (`0.99553` round 1, `0.99565` here, `0.998244` in C-b′); **there is now one: `0.998244`.**
> See `attack/reconciliation.md` §1.

> **Theorem C(b\*).** Suppose `F` is false and let `n₀` be its least failure. By card **L6**,
> `p_{n₀} > 2⁶⁴`, hence `λ = L_{n₀} > 44.3614` and, by (D-low), `T_{n₀} > λ² − 1.1λ > 1919`.
> Let `m < n₀`. Then `g_m < g_{n₀}` whenever
>
> ```
> log p_{n₀} − log p_m  ≥  0.0043636 ,      i.e.      p_m ≤ 0.9956459 · p_{n₀} ,
> ```
>
> and more sharply whenever (★) holds with `ℓ = L_m`. A fortiori the constant `0.004479` quoted by
> `proof-attempt-0.md` Theorem C(b) is sufficient, and the sweep-free constant `0.0061205` needs no
> optimisation at all.
> `[rests on axler2014newbounds Cor. 3.5 and 3.6 (= *Integers* Cor. 3.4 and 3.5), tier **L0**`
> `— fetched, MD5-pinned and read at the locator 2026-07-26; tier corrected in place 2026-07-27,`
> `decision 2. The instruction below is RESCOPED, not struck: it was over-strict on TIER grounds`
> `(the source is open) and exactly right on ROW grounds.]`
> **This theorem is RETIRED (see the notice above) and, if quoted at all, must carry the edition
> hazard: its Axler row `(1,0,0,0) / 1 772 201` is preprint-only. It may not be quoted inside a
> sentence containing the word "unconditional" — not because the source is unopened, but because
> the finite-range unconditional result of §4 does not use Axler at all and must not be conflated
> with it (§4.4).**

*Proof.* Two cases on `p_m`.

- **`p_m < 1 772 201`.** Then `g_m ≤ 132`, the largest prime gap `g_k = p_{k+1} − p_k` with
  `p_k < 1 772 201`, attained at `p = 1 357 201` (§5, V4 — segmented sieve, self-tested against an
  independent plain sieve). Since `g_{n₀} ≥ T_{n₀} > 1919 > 132`, `g_m < g_{n₀}` outright. No
  analytic input is used in this branch.
- **`p_m ≥ 1 772 201`.** Then `ℓ = L_m ≥ ℓ₁`, so (A-high\*) applies at `m`. And
  `p_{n₀} > 2⁶⁴ = 1.8446744·10¹⁹ > 2 634 800 823`, so (A-low) applies at `n₀`. Lemma W's hypothesis
  `C(p_m) ≤ A(p_{n₀})` is (★); by Proposition R1 it is implied by `d ≥ 0.0043636`. Lemma W then
  gives `g_m < g_{n₀}`. ∎

**Comparison with the printed theorem.** The repaired uniform constant `0.0043636` is *smaller*
than the printed `0.004479`, so the repaired theorem is very slightly **stronger**: the excluded
sliver has relative width `0.43541 %` instead of `0.44690 %`. The headline "`p_m ≤ 0.99553·p_{n₀}`"
becomes "`p_m ≤ 0.99565·p_{n₀}`". Nothing downstream of `proof-attempt-0.md` §13 needs to weaken;
the numbers move in the safe direction.

### 3.6 What was wrong with the printed constant, and what is right now (F2(c))

The skeptic's F2(c): `proof-attempt-0.md` §9 item 15 reports `max d* = 0.004479 at ℓ = ℓ₁` while
the criterion displayed one line above has maximum `0.0044887` — the reported sweep is **below**
the document's own formula, i.e. it errs *unsafely*. This leg reproduces both numbers (§5, V3) and
adds the identification that explains them: **§6.2's displayed criterion is row 2 of §3.1's table**
— the *additive* weakening `v + ℓ⁴/p_m` — not row 3, the factored lemma §6.1 displays. Solving
Lemma W's hypothesis under row 2 gives `0.0044880`, and the sufficient condition derived from it
gives `0.0044887`; the two differ only by the discarded `d²`. So §6.2's algebra was carried out
against a *different and much better* bar than §6.1's statement, which is why the document's own
numerical apparatus reported values near `0.00448` rather than near `0.169`.

| expression | max over `ℓ ≥ ℓ₁` | at | `≤ 0.004479`? |
|---|---|---|---|
| PA-0's displayed criterion `(0.17 − 1/ℓ + ℓ⁴/p_m)/(2ℓ−1)` | **0.0044887225** | `ℓ₁` | **no** |
| PA-0's reported sweep value | 0.004479 | `ℓ₁` | — |
| repaired criterion (★★) `(0.17 − 1/ℓ + v²/p_m)/(2ℓ−1)` | **0.0043635677** | `ℓ₁` | **yes** |
| true required `d`, solved from Lemma W with (A-high\*) | **0.0043628824** | `ℓ₁` | **yes** |
| true required `d`, solved from Lemma W with (A-high) as printed | **0.16933981** | `ℓ₁` | **no** |

Three things follow, and all three are stated rather than left implicit.

1. **The repaired criterion is `0.0043636`, and it is now *proved* (Prop. R1), not swept.** The
   sweep in §5 is an independent check written from Lemma W's hypothesis, not from (★★); it
   agrees to `7·10⁻⁷` (the gap between the solved requirement `0.0043628824` and the sufficient
   condition `0.0043635677` is the discarded `d²` term, `d² ≈ 1.9·10⁻⁵` divided by `2ℓ₁−1`).
2. **F2(c) is dissolved rather than patched.** `0.004479` was too small for the printed formula and
   is comfortably larger than the repaired one, so the discrepancy the skeptic found no longer has
   anything to be a discrepancy with. The document should quote `0.0043636` (proved) and may
   continue to quote `0.004479` only as a rounded-up sufficient constant.
3. **The 38.81× factor is confirmed.** `0.16933981 / 0.0043628824 = 38.8137`. The skeptic's
   "false by a factor of 38" is exact, and the mechanism is the `×223.71` inflation of the error
   term (§3.1) attenuated by the `1/(2ℓ−1)` in (★★).

### 3.7 What the printed lemma would have ordered (closes MINOR F13)

F13 asks that the repair not be applied half-way: if the printed (A-high) were *retained* rather
than tightened, the small-`p_m` branch would have to be extended and the constant `132` replaced.
This leg computes both numbers rather than leaving them named.

Solving `required_d_printed(ℓ) = 0.004479` (§5, V5) gives `ℓ = 21.00996466`, i.e.
`p_m = 1.332023·10⁹`. So under the printed lemma:

- the analytic branch of C(b) is available only for `p_m ≥ 1.332·10⁹`;
- the finite branch must cover `p_m < 1.332·10⁹`, whose governing constant is the largest prime gap
  below `1.332·10⁹` — **`288`, attained at `p = 1 294 268 491`** (§5, V4);
- `288 < 1919 < T_{n₀} ≤ g_{n₀}`, so the branch **still closes**. The printed theorem was
  therefore *repairable-by-enlargement* as well as repairable-by-tightening.

The cost of choosing enlargement over tightening is the point: the finite obligation grows from
`1.77·10⁶` to `1.33·10⁹`, a factor **751**, and the constant a Lean formalisation would have to
certify grows from `132` to `288`. **The repair taken here (tighten the lemma) is the one that
leaves the computation where the mathematics actually puts it.** F13 is closed by this paragraph:
the constants are `1 772 201 / 132` under (A-high\*), and the alternative is priced.

> ⚠ **Retired pricing — round-3 reconciliation, decision 1, 2026-07-27.** The reasoning of this
> section (tighten the lemma rather than enlarge the finite obligation) is **correct and stands**;
> the *constants* do not. With Theorem C(b\*) retired (§3.5), the live finite pair is
> **`6 690 557 / 154`** (Theorem C-b′, FFM §7.4), not `1 772 201 / 132`. The `288` at
> `1.332·10⁹` is unchanged as the counterfactual price of the alternative repair. Any Lean leg
> should certify the gap table below **`6 690 557`** (`g ≤ 154`), not below `1 772 201`.

*(A second reading of F13's warning, recorded because it is the sharper one: a defective analytic
lemma does not usually announce itself as a false theorem — it announces itself as a **larger
computation**. That is why F2 was invisible from inside `proof-attempt-0.md`, whose §9 never ran
the finite branch at scale.)*

### 3.8 Why Theorem C(a) is unaffected — audited, not assumed

The brief asks that this be recorded with its reason. The reason is structural, not lucky.

**(D-high)** reads `T_n ≤ (ℓ² − ℓ)(1 + (ℓ² − ℓ)/x)` for `x ≥ 5393`. That is **verbatim
Lemma H (H-hi) with `t = v_D := ℓ² − ℓ`** — the tight form. No substitution of any kind is
performed inside the second factor, and `proof-attempt-0.md`'s bookkeeping variable
`ε := (ℓ² − ℓ)²/p_m` **is** the `t²/x` of (H-hi), correctly squared. The proof of C(a) then runs
`2ℓd + d² − 1.1d − 0.1ℓ ≥ ε` with `ε(ℓ) = (ℓ²−ℓ)²e^{−ℓ}` decreasing — the same monotone-error-term
argument as Prop. R1, and it is carried out correctly there.

**Why the slip landed only on the Axler side.** `v_D = ℓ² − ℓ` is already a clean polynomial;
there is no temptation to simplify it. `v = ℓ² − ℓ − 1 − 1/ℓ` carries a non-polynomial term, and
the invitation to "replace `v` by `ℓ²`" is exactly where the error entered — and it entered in the
one place (inside the second factor of (H-hi)) where the replacement changes the *shape* of the
bound rather than merely its size. This is a reusable failure mode and is stated here so the
`skeptic` leg of round 2 can test for it elsewhere: **any occurrence of `t(1 + w/x)` with `w ≠ t`
in this corpus is a place to check whether `t ≤ w` was proved and whether the additive form
`t + w/x` was meant instead.**

Independent recomputation (§5, V6): the true maximal required separation for C(a), solved from
Lemma W with (D-high) at `m` and (D-low) at `n₀`, is **`0.062079811` at `ℓ = log 60 184 = 11.005162`**,
which `proof-attempt-0.md`'s quoted `0.0623` covers. `ε(ℓ₀) = 0.20144665`, matching PA-0's
`0.20145`. **C(a) stands exactly as printed**, and it is the only branch of Theorem C that is
unconditional in the citation sense (Dusart only, tier L0).

---

## 4. The subquestion itself: the unconditional verified range

### 4.1 What "unconditional verified range" asserts — two readings, carried forward

`proof-attempt-2.md` §1 split the target into two readings. This leg adopts them unchanged (they
are correct and the skeptic confirmed both, §5 items 9–11 of `faults.md`) and re-audits their
proofs against F2.

**Reading (A) — the finite-range theorem.** There is an explicit `X` and an explicit finite object
`C` (a table) such that `F` holds at every `n` with `p_n ≤ X`, and `C ⟹ (F on [1, X])` is a theorem
requiring no unproved hypothesis.

**Reading (B) — the table-free range.** There is an explicit `X` such that `F` holds at every `n`
with `p_n ≤ X`, proved from unconditional analytic estimates alone.

### 4.2 The chain, restated with Lemma H as its primitive

> **Lemma 1 (exact reformulation).** For every `n ≥ 1`: `F` at `n` ⟺ `p_{n+1}^n < p_n^{n+1}` ⟺
> `g_n < T_n`. *(Card **L1**; re-derived in `proof-attempt-2.md` §2.2; **machine-checked** in
> round 1 — `conjecture_iff_gap` is `sorryAx`-free per `lean-probe-report.md`.)*

> **Lemma 2 (the analytic input) — CITED, tier L0.** `π(x) ≤ x/(log x − 1.1)` for `x ≥ 60 184`.
> Source: `dusart2010estimates` (arXiv:1002.0442) **Thm 6.9, eq. (6.6)**, read at the locator by
> the `source-ledger` leg and recorded on card **T1** at tier **L0**.
> **This is the only external mathematical input to Theorem 2.**

> **Lemma 3 (explicit floor).** Put `B(p) := (log p)² − 1.1·log p`. For every `n` with
> `p_n ≥ 60 184`: `T_n > B(p_n)`.
>
> *Proof.* By (H-lo) with `t = p_n·L_n/n` — i.e. `T_n = p_n(e^{L_n/n} − 1) > p_n·L_n/n`. By **D3**
> `n = π(p_n)`, and by Lemma 2 at `x = p_n ≥ 60 184`, `n ≤ p_n/(L_n − 1.1)` with `L_n − 1.1 > 0` on
> that range. Hence `p_n/n ≥ L_n − 1.1` and `T_n > L_n(p_n/n) ≥ L_n(L_n − 1.1) = B(p_n)`. ∎
>
> *(Identical to `proof-attempt-2.md` §2.4; the only change is that `e^t − 1 > t` is now cited as
> Lemma H (H-lo) rather than re-proved inline — one primitive, two consumers.)*

> **Lemma 4 (monotonicity).** `B` is strictly increasing on `[e^{0.55}, ∞) ⊇ [2, ∞)`.
> *Proof.* `dB/dL = 2L − 1.1 > 0` for `L > 0.55`, and `p ↦ log p` is strictly increasing;
> `e^{0.55} = 1.73325 < 2`. ∎

> **Theorem 2 (unconditional finite-range verification).** Let `X ≥ X₀ := 60 184`. Suppose
> **(H1)** `p_{n+1}^n < p_n^{n+1}` for every `n` with `p_n < X₀`;
> **(H2)** a table lists, for every gap value `g` occurring as `g_n` for some `n` with `p_n ≤ X`,
> the first occurrence `q(g) := min{ p_n : g_n = g }`;
> **(H3)** for every `g` in that table with `q(g) ≥ X₀`: `g ≤ B(q(g))`.
> Then `F` holds at every `n` with `p_n ≤ X`.
>
> *Proof.* Let `p_n ≤ X`. If `p_n < X₀`, Lemma 1 and (H1) give `F` at `n`. Otherwise put `g := g_n`
> and `q := q(g) ≤ p_n`.
> If `q ≥ X₀`: (H3) gives `g ≤ B(q)`; Lemma 4 and `q ≤ p_n` give `B(q) ≤ B(p_n)`; Lemma 3 gives
> `B(p_n) < T_n`. So `g_n < T_n`, and Lemma 1 gives `F` at `n`.
> If `q < X₀ ≤ p_n`: the first occurrence of `g` lies below `X₀`, so
> `g ≤ G₀ := max{ g_k : p_k < X₀ } = 72` (§5, V7, exact integer arithmetic over 6 076 gaps), and
> `B(X₀) = B(60 184) = 109.00791 > 72 ≥ g`, whence `g ≤ G₀ < B(X₀) ≤ B(p_n) < T_n` by Lemma 4 and
> Lemma 3. `F` at `n`. ∎

> **Decision procedure.** With `S(g) := exp((1.1 + √(1.21 + 4g))/2)` — the unique `p` with
> `B(p) = g` — one has `g ≤ B(p) ⟺ p ≥ S(g)`, so (H3) reads `q(g) ≥ S(g)`, and Theorem 2 says:
> *a gap of size `g` occurring at a prime `p ≥ max(S(g), 60 184)` cannot violate `F`.*

### 4.3 F2-audit of the chain — the finding

Every step above was re-read against F2. The audit is exhaustive because the chain is short.

| step | uses (H-hi)? | uses `v(1 + w/x)` with `w ≠ v`? | uses Axler? | uses Theorem C? | touched by F2? |
|---|---|---|---|---|---|
| Lemma 1 | no | no | no | no | **no** |
| Lemma 2 | — (cited) | no | **no** — Dusart eq. (6.6) | no | **no** |
| Lemma 3 | no — uses (H-lo) | no | no | no | **no** |
| Lemma 4 | no | no | no | no | **no** |
| Theorem 2 | no | no | no | no | **no** |
| Corollary 2.1 (`g ≤ 1918` at `2⁶⁴`) | no | no | no | no | **no** |
| Prop. 3 / Prop. 4 (Reading B) | no | no | no — Dusart Prop. 6.8 | no | **no** |

> **Finding (recorded so no downstream leg re-derives it).** *The unconditional verified-range
> theorem is untouched by F2.* F2 lives entirely in the (H-hi)-with-substitution step of
> `proof-attempt-0.md` §6.1, and the verified-range chain never takes an **upper** bound on `T_n`
> at all — it takes a **lower** bound, which needs (H-lo) and an **upper** bound on `π`. The
> asymmetry is not an accident: a verified range needs the bar `T_n` to be *large*, and Theorem C
> needs it to be *sandwiched*. Only the sandwich has an upper side, and only the upper side has a
> place for the defect to live.

This is a positive result of the audit and it should be read as one: **the round-1 BLOCKER does not
propagate into the subquestion this leg owns.** What propagates is the *cost* accounting of §3.7.

### 4.4 What is unconditional, and what merely sounds it

The word does two jobs in this corpus and the skeptic's F3 is about the collision. Stated for this
subquestion, once:

| statement | unproved *hypothesis*? | unopened *source*? | may be called "unconditional"? |
|---|---|---|---|
| Lemma 1, Lemma 4 | none | none | **yes** — and Lemma 1 is machine-checked |
| Lemma 3, Theorem 2, Cor. 2.1, Prop. 3, Prop. 4 | none | Dusart eq. (6.6) / Prop. 6.8, tier **L0**, read at the locator by the ledger leg, **not re-opened by this leg** | **yes**, in the mathematical sense, with the L0 provenance named |
| Theorem C(a) | none | Dusart only, tier L0 | **yes** |
| Theorem C(b\*) *(RETIRED, §3.5)*, (A-high\*), (A-low), Fact S2, Theorem B | none | Axler Cor. 3.5/3.6, tier **L0** *(corrected 2026-07-27, decision 2 — was "L2_strong, NOT OPENED")*; ⚠ but (A-high\*)'s row `(1,0,0,0)/1 772 201` is **preprint-only** | **no** — for a *different* reason than when this table was written: not an unopened source, but (i) an edition-fragile locator and (ii) the fact that §4's unconditional range does not use Axler at all and must not be conflated with it. The live Axler-based theorem is **C-b′** (FFM §7.4), which uses the both-editions row |

"Unconditional" here means *no unproved hypothesis*, never *no computation* (Prop. 4 proves the
computation cannot be removed) and never *no citation*. **The repaired Theorem C(b\*) is not part
of the unconditional verified range and must not be quoted as if it were.** That is F3's warning
applied to this leg's own output before anyone else has to apply it.

### 4.5 Reading (B): the window, and its permanent closure

Carried forward unchanged from `proof-attempt-2.md` §3, and re-verified here (§5, V11):

> **Proposition 3.** `F` holds at every `n` with `396 738 ≤ p_n ≤ 777 600`, with no computational
> input beyond two cited explicit estimates.
> *Proof.* Dusart Prop. 6.8 (**T1**, L0) gives `g_n ≤ p_n/(25L²)` for `p_n ≥ 396 738`; Lemma 3
> gives `T_n > L² − 1.1L`. It suffices that `p ≤ 25L³(L − 1.1)`. With
> `h(p) := p − 25(log p)³(log p − 1.1)`, `h(396 738) = −2.35·10⁵ < 0`, `h' (p) = 1 − (25/p)(4L³ −
> 3.3L²) > 0` on `[4·10⁵, ∞)`, and the unique sign change is at `p* = 777 600.744…`. ∎

> **Proposition 4 (obstruction).** For `p > p*`, Dusart Prop. 6.8 does not imply `F`, and the
> shortfall `p/(25L³(L−1.1)) → ∞`. A table-free proof on `[X₀, X]` needs an unconditional explicit
> gap bound of quality `O(log² p)`; every known unconditional bound is a *power of `p`*
> (Dusart's `p/(25log²p)`; Baker–Harman–Pintz `p^{0.525}`, card **L11**). **Reading (B) is dead
> above `7.776·10⁵`** and stays dead until unconditional prime-gap technology reaches `log²` scale
> — which is the strength proving `F` itself requires.

*Corollary, restated so no downstream leg re-derives it:* **no amount of analysis will eliminate
the computational input from a verified-range claim.** The verified range is irreducibly a
computation plus a theorem about the computation.

### 4.6 Independence from P6′ — under all three of F1's readings

`proof-attempt-2.md` §2.5 found that target #2 does not depend on L15/P6′. F1 (the other round-1
BLOCKER, not this leg's assignment) shows that "P6′" names three inequivalent predicates. The
independence claim must therefore be re-checked against all three, and it survives all three for
one reason: **Lemma 4 is a monotonicity statement about `B`, a function of `p` alone.** No
comparison between two different indices of the non-monotone object `T` occurs anywhere in §4.2 —
grep-level check: `T` appears in Lemma 1, Lemma 3 and Theorem 2 only ever at a *single* index.
Whatever `m(n)` means, it does not appear. Independence therefore does not depend on how F1 is
repaired, which is worth one sentence because F1's repair is still in flight.

### 4.7 What Theorem 2 yields at the published frontier — unchanged, and still conditional

Applying Theorem 2 with `X = 2⁶⁴`: the largest **even** `g` with `S(g) ≤ 2⁶⁴` is **1918**
(`S(1918) = 1.8208685·10¹⁹ ≤ 2⁶⁴ = 1.8446744·10¹⁹ < S(1920) = 1.8629095·10¹⁹`; §5, V9), agreeing
with Kourbatov's published "gaps of size `g < 1920` cannot violate (1)" since every gap after
`g_1 = 1` is even.

**The agreement is corroboration and is worth exactly what it is worth**, and `faults.md` F11
strikes one of the two mitigations `proof-attempt-2.md` attached to it. Applied here:

- The agreement establishes that no sign error, inverted inequality or transcription slip separates
  the two constant-chains. That mitigation **stands**.
- The agreement does **not** detect a wrong validity range for Dusart eq. (6.6), because
  Kourbatov's own criterion yields `1922` (§5, V9b), so his published `1920` is conservative
  relative to it by an unquantified margin, and a conservative threshold cannot detect an error of
  unknown sign. That mitigation is **struck** (F11 applied).

`G2` is unchanged and remains the single largest dependency of any claim about the range to `2⁶⁴`:
hypothesis (H2), the complete first-occurrence gap table below `2⁶⁴`, rests on
`oliveira2014goldbach`, tier **L2_weak, NOT OPENED** (AMS returned HTTP 403; ledger §6.2).
**If that table is incomplete, Corollary 2.1 says nothing.**

---

## 5. In-run verification

Script: `attack-round-2/verify-uvr-round2.py` (committed alongside this file), `mpmath` at 50
decimal digits for every analytic quantity, exact Python integers for the base case, `numpy`
segmented sieve for the gap statistics.

**Discipline, stated because it is the point.** `faults.md` §6 item 2 diagnoses that
`proof-attempt-0.md` §9 item 15 *reproduced* the F2 error rather than catching it, because it
evaluated an expression derived from the same wrong step. Every routine in this leg's script is
written **from the statement it checks, never from the derivation**: the `required_d_*` functions
do not evaluate (★) or (★★) at all — they go back to Lemma W's hypothesis `C(p_m) ≤ A(p_{n₀})`,
solve the resulting quadratic for `λ`, and return `λ − ℓ`. The sufficient conditions are evaluated
separately and only ever *compared* against the solved requirement. A disagreement between the two
columns would be a derivation error; a disagreement between either and the theorem would be a
statement error. Both comparisons are made.

| ID | Check | Result |
|---|---|---|
| V1 | the four bars named (A-high) at `ℓ₁` (`v = 191.549619639`) | tight `v(1+v/x) = 191.570323417`; §6.1's stated justification `v(1+ℓ²/x) = 191.571994124`; additive `v + ℓ⁴/x = 191.573799649`; **as printed** `v(1+ℓ⁴/x) = 196.18129142`. Printed error term is **223.71×** the tight one |
| V3c | max required `d` (solved from Lemma W) for each of the four bars, `ℓ ∈ [ℓ₁, 300]` | `0.00436288239` / `0.00442301381` / `0.00448799729` / `0.169339813`; sufficient against `0.004479`: **yes / yes / no / no**; every max attained at `ℓ = ℓ₁` |
| V2 | Prop. R1 certificates | `q(ℓ₁) = v − 2v' = 135.98903 > 0` (⟹ `E` decreasing); `4/ℓ₁ − 1/ℓ₁² = 0.27318386 < 0.38140756 = 2K` (⟹ `φ` decreasing); `φ(ℓ₁) = d*(ℓ₁) = 0.004363567696`; `φ` decreasing on a 4 000-point grid over `[ℓ₁, 4000]`: **0 exceptions** |
| V3 | max over `ℓ ∈ [ℓ₁, 300]` (20 000 points) of: true required `d` under (A-high\*) / under (A-high) as printed / PA-0's displayed criterion / repaired criterion (★★) | **0.0043628824** / **0.16933981** / **0.0044887225** / **0.0043635677**, all attained at `ℓ = ℓ₁`; ratio printed:repaired = **38.8137** |
| V3b | is `0.004479` sufficient? | under (A-high\*): **yes**; under (A-high) as printed: **no**; against PA-0's own displayed criterion: **no** (`0.0044887 > 0.004479`) — reproduces F2(c) |
| V4 | max prime gap below `1 772 201` / below `1 332 022 974` | **132** at `p = 1 357 201` / **288** at `p = 1 294 268 491`; both `< 1919` |
| V4b | segmented-sieve **self-test** against an independent plain sieve, max gap below `2·10⁶` | plain `(132, 1 357 201)` = segmented `(132, 1 357 201)` — **agree** |
| V5 | `ℓ` at which the printed lemma's required `d` falls to `0.004479` | `ℓ = 21.00996466`, i.e. `p_m = 1.332023·10⁹` (reproduces the skeptic's `≈1.33·10⁹`) |
| V6 | **Theorem C(a)**: true max required `d`, solved from Lemma W with (D-high)/(D-low) | **0.062079811** at `ℓ = 11.005162`; PA-0's `0.0623` covers it. `ε(ℓ₀) = 0.20144665` (PA-0: `0.20145`) |
| V7 | **(H1)** exact **integer** `p_{n+1}^n < p_n^{n+1}` for every `n` with `p_n < 60 184` (`π(60 184) = 6 076` indices, counted here) | **0 violations**. `G₀ = 72` at `p = 31 397`; `B(60 184) = 109.00791 > 72` |
| V8 | **Lemma 3** `T_n > B(p_n)` on `[60 184, 2·10⁶]` | **0 failures**; tightest slack `+0.079891473` at `p = 155 893` |
| V8b | **Lemma 2** (Dusart eq. 6.6 upper) at every prime in `[60 184, 2·10⁶]` | **0 failures** |
| V9 | largest even `g` with `S(g) ≤ 2⁶⁴` | **1918**; `S(1918) = 1.8208685·10¹⁹`, `S(1920) = 1.8629095·10¹⁹`, `2⁶⁴ = 1.8446744·10¹⁹` |
| V9b | same under Kourbatov's sharper bar `L² − L − 1.17` | **1922** (`S_K(1922) = 1.8361954·10¹⁹ ≤ 2⁶⁴ < S_K(1924) = 1.8785332·10¹⁹`) — his published `g < 1920` is conservative relative to his own criterion (F11) |
| V10 | Lemma 4 certificate | `dB/dL = 2L − 1.1 > 0` for `L > 0.55`; `e^{0.55} = 1.73325 < 2` |
| V12 | constants quoted inside the §3 proofs | Axler Cor. 3.6 denominator at `ℓ₁`: `13.313398 > 0`; `ψ(ℓ₁) = ℓ₁⁵e^{−ℓ₁} = 0.3478955285 < 1`; true `ℓ₁E(ℓ₁) = 0.2978804323` (majorant cost `1.1679`); `0.17/(2ℓ₁−1) = 0.006120509446`; `log(2⁶⁴) = 44.36141956` with `λ²−1.1λ = 1919.137983 > 1919`; `e^{−0.0043635677} = 0.99564594` (sliver `0.435406 %`) vs `e^{−0.004479} = 0.99553102` (sliver `0.446898 %`) |
| V11 | **Prop. 3 / Prop. 4** (Reading (B) window) with `h(p) = p − 25(log p)³(log p − 1.1)` | `h(396 738) = −234 735.02 < 0`; `h(777 600) = −0.51996212 < 0 < 0.17863233 = h(777 601)`; sign change at `p* = 777 600.7443`; `min h'` over a 2 001-point grid on `[4·10⁵, 10⁷]` is `+0.49774303 > 0` |

**Numbers reproduced from round 1 rather than carried over.** V6, V7, V8, V8b, V9, V9b, V11 were
recomputed here from scratch and agree with `proof-attempt-2.md` §4 and `faults.md` §5 to every
digit quoted. V3's `0.16934` and `0.0043629` agree with `faults.md` F2's independent
recomputation. **No number in this document is copied from an upstream artifact.**

**One cross-check that is NOT evidence.** The value `288` at `p = 1 294 268 491` matches this
worker's recollection of OEIS A005250 (maximal prime gaps). That recollection is **tier L3,
unsourced in this run**, and is recorded as a smell test only; the load-bearing witness is V4
together with the self-test V4b.

**Scale disclaimer.** The analytic sieve reaches `2·10⁶`; the gap sieve reaches `1.332·10⁹`. These
are ≈13 and ≈10 orders of magnitude below `2⁶⁴`. **They verify the lemmas, not the range**, and
must never be cited as a verification of `F`.

---

## 6. Bounded source refresh

The brief permits adding **only** anchors the round-1 skeptic flagged as missing, folded into
existing ledger rows; the ledger is not re-opened.

**Anchors the skeptic flagged, that bear on this subquestion — the complete list:**

1. **`axler2014newbounds` (Cor. 3.5, Cor. 3.6) — tier L0.** *(Amended 2026-07-27, decision 2. As
   written: "tier L2_strong, NOT OPENED … not resolved by this leg" — accurate for this leg, which
   fetched no PDF, and **superseded** by the sibling leg `task-20260726-56a7`, which fetched the
   arXiv v3, the *Integers* 16 (2016) A22 and the 2018 corrigendum the same day, MD5-pinned all
   three, read them at the locator, and landed the ledger promotion L2_strong → L0. The round-2
   skeptic re-fetched independently and reproduced all three MD5s.)* The residual exposure is **not**
   tier but **edition**: (A-high\*)'s row `(1,0,0,0)/1 772 201` is preprint-only, which is why
   Theorem C(b\*) is retired (§3.5) in favour of FFM's Theorem C-b′.
2. **`oliveira2014goldbach` — tier L2_weak, NOT OPENED** (AMS HTTP 403; ledger §6.2). Hypothesis
   (H2) of Theorem 2 at `X = 2⁶⁴`. **Not resolved.** Remains G2.
3. **`faults.md` F11 — the mitigation to be struck.** Applied in §4.7: `proof-attempt-2.md` G1's
   second mitigation (threshold agreement with Kourbatov's `g < 1920`) is withdrawn; G1 keeps one
   mitigation, the 1.27 M-prime numerical check, which this leg re-ran at its own scale (V8b).

**Anchors added: none.** No new ledger row is opened, and no row's tier is changed. The two
unsourced statements `proof-attempt-0.md` §10.3 lists (Brun–Titchmarsh; the status of the second
Hardy–Littlewood conjecture) belong to §7 of that document — the obstruction discussion — and are
not used anywhere in this leg, so no anchor is owed for them here.

---

## 7. Lean 4 / Mathlib facing statements

`lean/Firoozbakht/Statement.lean` is **FROZEN and was not touched**. No Lean was compiled by this
leg; what follows is obligation shape for the round-2 `lean-probe` leg, offered as a *sketch*, with
`Nat.nth`'s 0-indexing (**D1** correction #1) noted but not applied in the display below.

**The node list `proof-attempt-0.md` §12 hands to the Lean legs changes in exactly one place, and
it is the place F2(iii) named.** A faithful transcription of §6.1 as printed makes `M-8` /
Theorem C(b) **unprovable** — the hypothesis handed over does not imply the goal. With (A-high\*)
it is provable, and the arithmetic is easier than before because Prop. R1 replaced a sweep with
three monotonicity facts.

| node | content | effort | change from round 1 |
|---|---|---|---|
| **M-0** *(new)* | `Lemma H`: `∀ x t, 0 < t → t ≤ x → x*(exp (t/x) − 1) ≤ t*(1 + t/x)`, and the `>` half | low — `Real.add_one_le_exp` for (H-lo); (H-hi) from `Real.exp_bound` or a two-term Taylor estimate | **new**; shared by `M-8`, `M-9` and PA-2's Lemma 3, replacing three inline re-derivations |
| **M-8** | Theorem C(a) with `d = 0.0623` | medium | unchanged — C(a) is untouched (§3.8) |
| **M-9** *(new)* | (A-high\*) as an **explicit hypothesis** (Axler is not in Mathlib) + Prop. R1 + Theorem C(b\*) | medium — R1 is three `deriv`-sign arguments and two `norm_num` evaluations at `ℓ₁` | **new**; supersedes the unprovable transcription of §6.1 |
| PA-2 `lemma3` / `lemma4` / `verified_range` | unchanged | low / low / bookkeeping | now consume `M-0` rather than an inline `e^t − 1 > t` |

```lean
-- shared envelope (M-0); x t : ℝ
theorem envelope_hi (x t : ℝ) (hx : 0 < x) (ht : 0 < t) (htx : t ≤ x) :
    x * (Real.exp (t / x) - 1) ≤ t * (1 + t / x) := sorry
theorem envelope_lo (x t : ℝ) (hx : 0 < x) (ht : 0 < t) :
    t < x * (Real.exp (t / x) - 1) := sorry

-- (A-high*), as a hypothesis-shaped statement.  `axler36` must be axiomatised:
--   axler36 : ∀ x : ℝ, 1772201 ≤ x → x / (Real.log x - 1 - 1/Real.log x - 1/(Real.log x)^2) < π x
noncomputable def vAx (l : ℝ) : ℝ := l^2 - l - 1 - 1/l

theorem A_high_star (axler36 : ∀ x : ℝ, 1772201 ≤ x → …)
    (n : ℕ) (hn : (1772201 : ℝ) ≤ p n) :
    T n < vAx (Real.log (p n)) * (1 + vAx (Real.log (p n)) / (p n : ℝ)) := sorry
```

**Fidelity warning, repeated from `proof-attempt-2.md` §7 because it still applies.** The base case
`(H1)` is the real engineering obstacle and this leg does not claim it is feasible at
`X₀ = 60 184`: `Nat.nth Nat.Prime` is **noncomputable** (card **T4**), so `decide` cannot produce
`p n`, and the base case needs 6 076 prime literals with certificates plus a
"no prime strictly between" lemma per consecutive pair, discharged by reflection over a certified
list. `X₀` cannot be traded away — lowering it is forbidden by Lemma 2's validity range, raising it
only enlarges the base case.

**A round-2 note the probe leg should have.** §3.7 prices the alternative repair: had (A-high) been
kept as printed, `M-9`'s finite branch would need `max{g_k : p_k < 1.332·10⁹} = 288` certified in
Lean instead of `132` below `1 772 201` — a 751× larger certified gap table for no mathematical
gain. The tightening is the cheaper formalisation by a wide margin.

> ⚠ **Amended 2026-07-27 (decision 1 + 5).** The Lean sketch above axiomatises the Axler row
> `1772201`, which is **preprint-only**. Since Theorem C(b\*) is retired in favour of Theorem C-b′
> (FFM §7.4), a Lean leg should axiomatise the **both-editions** row instead —
> `axler35 : ∀ x, 6690557 ≤ x → x / (log x - 1 - 1/log x - 2.1/(log x)^2) < π x` — and certify
> `max{g_k : p_k < 6 690 557} = 154`. See `attack/re-attack/attack-round-2/lean-probe-report.md`
> §M-7/§M-8 and `attack/reconciliation.md` §5.

---

## 8. What this document does NOT establish

Stated at length, because a document with "verified" in its title is the one that gets over-quoted.

1. **`F` is not proved.** Theorem 2 proves `F` on a bounded initial segment given a table. `F` is a
   statement about all `n`; a verified range of any finite size contributes **zero** to the general
   case (card **L6** hazard 4).
2. **`F` is not refuted**, and nothing here bears on which way it resolves. Theorem C(b\*) is a
   conditional whose antecedent ("`F` is false") is Σ₁ and is not asserted.
3. **This leg did not verify `F` to `2⁶⁴`.** It sieved analytically to `2·10⁶` and for gaps to
   `1.332·10⁹`. Corollary 2.1's hypothesis (H2) is **not** discharged in this run (G2).
4. **F2 is repaired as a derivation, not as a citation.** (A-high\*) still rests on an unopened
   Axler corollary. **The BLOCKER's mathematical content is closed; its provenance content is
   not**, and the two must not be conflated when round 2's skeptic asks whether F2 was "actually
   FIXED or merely re-worded".
5. **F1 is untouched by this leg** and is not claimed to be fixed here.
6. **The kernel verdict is unchanged.** `Firoozbakht.firoozbakht` remains `sorry` at
   `Statement.lean:186`. Nothing in this document is a Lean artifact, and this leg wrote no Lean.
7. **"Unconditional" never means "no computation".** Prop. 4 proves the computation cannot be
   removed; any sentence of the form "`F` is unconditionally true below `X`" must carry the table.
8. **Theorem C(b\*) is not part of the unconditional range** (§4.4) and may not be quoted as if it
   were.

---

## 9. Declared gaps

| # | Gap | Severity | Where it bites |
|---|---|---|---|
| **G1** | **Dusart Thm 6.9 eq. (6.6) was not read from the source by this leg** — tier L0 via card **T1** / the ledger leg. If the constant `1.1` or the range `x ≥ 60 184` is mis-transcribed upstream, Lemma 3 and everything above it moves. | **MAJOR** — **one** mitigation, not two: the numerical check at every prime in `[60 184, 2·10⁶]` (V8b, 0 failures) would expose a wrong constant. The Kourbatov-threshold mitigation is **struck** per F11 (§4.7). Neither is a substitute for opening the paper. | §4.2 |
| **G2** | **(H2) — the first-occurrence gap table below `2⁶⁴` — is not verified in this run**; `oliveira2014goldbach` unopened (L2_weak, HTTP 403). | **BLOCKER for Corollary 2.1**, not for Theorem 2 (an implication). Unchanged from round 1. | §4.7 |
| **G3** | ~~**Axler Cor. 3.5 / 3.6 unopened** (L2_strong)~~ — **CLOSED as a tier gap 2026-07-27** (decision 2): the source was fetched, MD5-pinned and read at the locator on 2026-07-26 by the sibling leg, and the ledger row is **L0**. **REPLACED by G3′ — an *edition* gap:** (A-high\*) and Theorem C(b\*) consume the Axler row `(1,0,0,0)/x₀ = 1 772 201`, which exists in **arXiv:1409.1780v3 only** and is absent from *Integers* **16** (2016) A22. | G3: **closed**. G3′: **MAJOR** for `(A-high\*)`/`C(b\*)` — and discharged the only way it can be, by **retiring** them (§3.5) in favour of FFM's Theorem C-b′, which uses the `(2.1,0,0,0)/6 690 557` row present in both editions. Neither ever was a gap in the unconditional range, which does not use Axler (§4.3). | §3, §6, `attack/reconciliation.md` §1–§2 |
| **G4** | **`ε`/`E` monotonicity in Prop. R1 step (1) and Cor. R1.1 is argued by sign of the log-derivative plus a monotone majorant, not by a formal proof of unimodality.** The endpoints are evaluated exactly and the grid check V2 found 0 exceptions over 4 000 points. | MINOR — the argument is a two-line derivative computation and the constants are checked at the binding endpoint `ℓ₁`. | §3.4 |
| **G5** | **`G₀ = 72` and the `132` / `288` gap constants are this leg's own sieve facts.** Exact integer arithmetic, and V4b self-tests the segmented implementation against a plain sieve at `2·10⁶`; the `288` figure at `1.332·10⁹` has **no** second implementation behind it (only an L3 recollection of A005250, which is not evidence). | MINOR for `72` / `132`; **MAJOR-if-load-bearing** for `288`, which is used **only** in §3.7's counterfactual pricing and in no theorem. | §3.7, §4.2 |
| **G6** | **The floating-point / `mpmath` checks are 50-digit, not interval arithmetic.** The binding margins are `+0.0799` (V8) and `0.004479 − 0.0043636 = 1.15·10⁻⁴` (V3) — both astronomically clear of 50-digit noise, but the computation does not claim to be certified. | MINOR | §5 |
| **G7** | **Strict vs non-strict in Lemma 1** is handled by using `<` throughout rather than by proving `T_n ∉ ℤ`. Unchanged from round 1. | MINOR | §4.2 |
| **G8** | **Prop. 3's `h' > 0` on `[4·10⁵, ∞)` is a one-line derivative computation, and the sign change's uniqueness is not formally proved.** Carried forward from `proof-attempt-2.md` G4. | MINOR — the interval endpoints are checked directly. | §4.5 |

---

## 10. Verdict

| Item | Verdict |
|---|---|
| **F2 (BLOCKER) — the derivation defect** | **FIXED.** (A-high) is restated as (A-high\*) `T_n < v(1 + v/x)`, `v := ℓ²−ℓ−1−1/ℓ`, proved from Lemma H with no weakening step (§3.2). `ℓ⁴/p_m` is replaced by `v²/p_m` in the displayed criterion (★) (§3.3). The uniform constant is **re-derived, not re-quoted**: `0.0043636`, now **proved in closed form** (Prop. R1) rather than swept, and independently re-solved from Lemma W's hypothesis (§5, V3). |
| **F2(c) — the quoted constant below its own criterion** | **DISSOLVED.** The repaired criterion's maximum is `0.0043636 < 0.004479`; the printed criterion's `0.0044887 > 0.004479` no longer has a formula to disagree with. |
| **F2 — provenance** | **FIXED, by the sibling leg, not by this one.** *(Amended 2026-07-27, decision 2. As written: "NOT fixed, and not claimed … tier L2_strong, unopened".)* Axler is **L0** — fetched, MD5-pinned, read at the locator 2026-07-26 by `task-20260726-56a7`; the ledger row and card `T1` carry the promotion. What survives is not a tier gap but an **edition** gap (G3′): (A-high\*)'s row is preprint-only, which is why Theorem C(b\*) is retired in favour of Theorem C-b′. |
| **Theorem C(b\*)** | **PROVED and RETIRED.** The mathematics stands (independently verified at 40–50 dps by the round-2 skeptic): `p_m ≤ 0.99565·p_{n₀}`, sweep-free branch improved from `0.006992` to `0.0061205`. **It is nevertheless retired to a remark** (§3.5, decision 1) because its Axler row is preprint-only; the corpus's single repaired Theorem C(b) is **Theorem C-b′** (`p_m ≤ 0.998244·p_{n₀}`), FFM §7.4. `0.99565` may appear only as history. |
| **Theorem C(a)** | **UNAFFECTED** by the repair, and the reason is recorded (§3.8): (D-high) is Lemma H at its natural `t`, with no substitution inside the second factor. Independently re-verified: true max required `d = 0.062079811 ≤ 0.0623`. |
| **F13 (MINOR)** | **CLOSED.** Had the printed lemma been retained, the finite branch would run to `1.332·10⁹` with governing constant `288` (not `132`), still `< 1919`, so the theorem was repairable either way — at 751× the computation. |
| **Subquestion `unconditional-verified-range`, Reading (A)** | **PROVED** (Theorem 2, §4.2), constants explicit, **one** cited inequality (Dusart eq. 6.6, L0), independent of P6′ under all three of F1's readings (§4.6), and **audited step-by-step to be untouched by F2** (§4.3). |
| **Subquestion, Reading (B)** | **PROVED for `396 738 ≤ p_n ≤ 777 600`**; **PROVED impossible to extend by Dusart Prop. 6.8** beyond `p* = 777 600.744…`; *argued from the state of the literature* — not proved — that no known unconditional gap bound can extend it (§4.5). |
| **`F` at the published frontier `2⁶⁴`** | **CONDITIONAL** on an unopened first-occurrence table (G2). Not established by this run. |
| **`F` itself** | **OPEN.** Untouched. Not proved, not refuted. |

**The defensible sentences this leg supports:**

> *There is a clean theorem — needing exactly one explicit estimate on `π(x)`, no unproved
> hypothesis, and no property of the non-monotone bar `T` — that converts a table of
> first-occurrence prime gaps into a proof that Firoozbakht's inequality holds up to that table's
> reach; and it can never be made to work without the table.*

> *The round-1 BLOCKER in Theorem C(b) was a substitution made inside the error term of an
> elementary exponential envelope, not a mistake about the primes. Repairing it makes the theorem
> marginally stronger, replaces a numerical sweep by a closed-form bound, and shrinks the finite
> computation the theorem silently orders from `1.3·10⁹` to `1.8·10⁶`. The unconditional
> verified-range theorem never used the defective bound and is unchanged.*

---

*Emitted by leg `proof-attempt` (subquestion `unconditional-verified-range`, round 2), molecule
`task-20260726-2035`, parent `reattack-20260726-57d1`. Verification script:
`attack-round-2/verify-uvr-round2.py`. `lean/Firoozbakht/Statement.lean` unmodified.
**The conjecture remains OPEN.***
