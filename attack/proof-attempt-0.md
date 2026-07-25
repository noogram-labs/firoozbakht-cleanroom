# Proof attempt — target #0: `first-failure-maximality`

**Molecule:** `task-20260725-a1cd` (leg `proof-attempt__0`, crew role: proofsmith)
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-25 · **Backend:** Lean 4 / Mathlib
**Conjecture under attack:** `F`: `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.
**Status of `F` in this document: OPEN.** Neither assumed true nor assumed false.
Nothing below asserts `F`. A target reaches *proved* only through the kernel/Lean leg downstream.

---

## 0. Perimeter and provenance

**Admitted inputs — exhaustively:**

| Input | Provenance |
|---|---|
| `attack/concept-cards/` (30 cards, INDEX) | leg `concept-cards`, molecule `task-20260725-068e`, this run |
| `attack/source-ledger.md` (20 rows, tiers L0–L2) | leg `source-ledger`, molecule `task-20260725-d320`, this run |
| `attack/decompose.md` | leg `decompose`, molecule `task-20260725-c062`, this run |
| `attack/frame-deliberation/{frame,synthesis,outcomes}.md` | molecule `delib-20260725-07fc`, this run |
| in-run computation performed **by this leg** | sieve to `3·10⁶`, §9; scripts committed as `attack/probe_t0*.py` |

**Nothing else.** No external source was fetched by this leg. Every external statement used
below is quoted **through a concept card**, which names its ledger row and tier. Where a card
flags a source as unopened, this document inherits the flag and repeats it at the point of use —
it does not launder it.

**Tier vocabulary** is the ledger's: `L0` = primary source fetched and the statement read at the
locator; `L2_strong` = two independent attestations but **not fetched in this run**; `L3` = recall
(no claim here rests on an L3 row).

---

## 1. The target, stated precisely

The brief names the target `first-failure-maximality`. The name admits three readings. They are
not equivalent and the difference is load-bearing, so all three are written out and one is
selected.

Notation follows **D1**, **D2**, **D5**: `p_n` is the `n`-th prime (1-indexed, `p_1 = 2`),
`g_n = p_{n+1} − p_n`, `L_n = log p_n`, and

```
T_n  :=  p_n (p_n^{1/n} − 1)  =  p_n (e^{L_n/n} − 1)                       (D5)
F    ⟺  ∀ n ≥ 1,  g_n < T_n                                                (L1)
```

Call `n` a **failure** if `g_n ≥ T_n`, and call `n` a **maximal-gap index** (record index) if
`g_n > g_m` for every `m < n`.

> **(M1) — first-failure maximality (selected).**
> If `F` is false, the least failure `n₀` is a maximal-gap index.
>
> **(M2) — weak form.** If `F` is false, the least failure `n₀` satisfies `g_{n₀} ≥ g_m` for all
> `m < n₀`.
>
> **(M3) — the reduction (P6′ / card L15).** For `m < n` straddling a record gap, `T_m ≤ T_n`.

**(M3) ⟹ (M1) ⟹ (M2)**, and the reverse implications are not available. The upstream run treats
(M3) as *the* obligation (card **L15**, "the single most tractable open obligation in the
attack"; **T5**(d); `decompose` §2.4 P6′). **(M3) is strictly stronger than what any consumer of
it needs**, and that is the first substantive finding of this leg (§4).

### 1.1 Logical status of the target — read this before reading the verdict

`F` is Π₁. "`F` is false" is Σ₁. (M1) is a conditional whose antecedent is Σ₁, so:

- **If `F` is true, (M1) is vacuously true.** Since `F` is verified for all `p < 2⁶⁴` (**L6**) and
  no counterexample is known, (M1) is *not* a statement anyone can hope to refute directly:
  **refuting (M1) requires first refuting `F`, and then exhibiting a first failure that is not a
  record.** Refuting the target is therefore *strictly harder* than refuting the conjecture.
  This is recorded here because "PROVEN or REFUTED" is the brief's framing and the refutation
  door is, for this particular target, provably narrower than the proof door.
- Consequently the only *useful* form of (M1) is the **unconditional** one — proved without
  assuming anything about `F` — because its whole purpose is to license a search pruning, and a
  pruning derived from an assumption about `F` cannot certify a search for counterexamples to `F`
  (`synthesis.md` C6; **L15** hazards 1–2, the laundering risk).

---

## 2. Verdict

| Claim | Verdict |
|---|---|
| **(M3)** = P6′ as stated in **L15** | **NOT PROVED here, and shown to be the wrong obligation** (§5, §7) |
| **(M1)** in full | **NOT PROVED.** Explicit obstruction isolated (§7) |
| **(M1)** restricted to `p_m ≤ 0.939·p_{n₀}` | **PROVED** unconditionally, Dusart only (§6, Thm C-a) |
| **(M1)** restricted to `p_m ≤ p_{n₀}·e^{−0.0045}` | **PROVED**, modulo the unopened Axler source (§6, Thm C-b) |
| **Monotone-bar principle** (Lemma M) | **PROVED**, elementary, unconditional (§3) |
| **Record-scan completeness** (Thm A) | **PROVED**, elementary, unconditional (§4) |
| **The search-pruning that (M3) was wanted for** | **DISCHARGED** unconditionally by Thm A + Thm B (§4) |
| Residual window is heuristically empty | **HEURISTIC only**, `O(1/log²p)` (§8) |

**One-sentence result.** *First-failure maximality is not proved, but the obligation it was
introduced to support is discharged without it: the maximal-gap reduction fails for the exact bar
`T_n` and succeeds unconditionally for Kourbatov's monotone surrogate `L² − L − 1.17`, and against
the exact bar the first failure is provably a record among all primes below `0.939·p_{n₀}`, the
residual window being a relative `O(1/log p)` sliver in which the obstruction is an
unconditional short-interval prime count sharper than Brun–Titchmarsh by a factor of two.*

---

## 3. Lemma M — the monotone-bar principle

This is the engine of everything below. It is elementary; it is stated separately because the
entire difficulty of the target is that it *fails to apply* to `T_n`.

> **Lemma M.** Let `B` be a real-valued function of the prime `p`, **nondecreasing** in `p`.
> Say `k` is a *`B`-breach* if `g_k ≥ B(p_k)`. If a `B`-breach exists, the least one, `k₀`,
> satisfies `g_m < g_{k₀}` for every `m < k₀` — i.e. `k₀` is a **strict maximal-gap index**.

*Proof.* Let `m < k₀`. Then `p_m < p_{k₀}`, so `B(p_m) ≤ B(p_{k₀})` by monotonicity. By
minimality of `k₀`, `m` is not a `B`-breach, so `g_m < B(p_m)`. Chaining,
`g_m < B(p_m) ≤ B(p_{k₀}) ≤ g_{k₀}`. ∎

*Remarks.* (i) Only monotonicity of `B` is used — no arithmetic, no analytic input, no property
of the primes beyond `p_m < p_{k₀}`. (ii) The conclusion is *strict*, which is the difference
between (M1) and (M2): the chain ends in `<` at its first link. (iii) The lemma is sharp in the
sense that it says nothing about the *second* breach: breaches after the first need not be
records (verified in-run, §9, item 3).

### 3.1 A truncated form, because the small primes misbehave

Every explicit bar in this problem has a validity range, and the first few gaps sit outside it.
The following variant carries the range explicitly.

> **Lemma M′.** Let `B` be nondecreasing, and let `1 ≤ N₁ ≤ N₂`. Suppose
> **(i)** `g_m < B(p_m)` for every maximal-gap index `m` with `N₁ ≤ m ≤ N₂`, and
> **(ii)** `max{ g_m : m < N₁ } < B(p_{N₁})`.
> Then `g_k < B(p_k)` for every `k` with `N₁ ≤ k ≤ N₂`.

*Proof.* Suppose not, and let `k₀` be least in `[N₁, N₂]` with `g_{k₀} ≥ B(p_{k₀})`. Take any
`m < k₀`. If `m ≥ N₁`, minimality gives `g_m < B(p_m) ≤ B(p_{k₀}) ≤ g_{k₀}`. If `m < N₁`, then
`g_m ≤ max{g_j : j < N₁} < B(p_{N₁}) ≤ B(p_{k₀}) ≤ g_{k₀}` by (ii) and monotonicity. Either way
`g_m < g_{k₀}`, so `k₀` is a maximal-gap index in `[N₁, N₂]` that breaches `B` — contradicting
(i). ∎

---

## 4. What (M3) was wanted for, and its unconditional discharge

**L15** states the purpose of P6′ plainly: it is "the **sole pruning rule** of the only
computationally live route" — it is what licenses checking record indices instead of all indices.
That consumer does not need (M3). It needs Lemma M′ applied to a **monotone** bar, and such a bar
is already in the card set.

> **Theorem A (record-scan completeness).** Immediate from Lemma M′. Let `B` be nondecreasing.
> If every maximal-gap index in `[N₁, N₂]` clears `B`, and the finite condition M′(ii) holds, then
> every index in `[N₁, N₂]` clears `B`.

Now instantiate with Kourbatov's sufficient bar. Put

```
S(x)  :=  log²x − log x − 1.17.
```

> **Fact S1 (monotonicity).** `S` is strictly increasing on `x > e^{1/2}`, since
> `dS/dx = (2 log x − 1)/x > 0` there. In particular on all primes `p ≥ 2`. `[self-contained]`

> **Fact S2 (`S` is below the true bar).** `T_n > S(p_n)` for `p_n ≥ 2 634 800 823`.
> *Proof.* `n = π(p_n)` (**D3**). Axler Cor. 3.5, quoted through **T1**:
> `log x − 1 − 1.17/log x < x/π(x)` for `x ≥ 2 634 800 823`. Hence with `x = p_n`, `ℓ = L_n`,
> `π(x) < x/(ℓ − 1 − 1.17/ℓ)`, so `u := ℓ/π(x) > (ℓ² − ℓ − 1.17)/x`, and
> `T_n = x(e^u − 1) > x·u > ℓ² − ℓ − 1.17 = S(p_n)`. ∎
> **`[flag: rests on `axler2014newbounds`, tier L2_strong, NOT OPENED in this run — see T1
> hazard 2, L4 hazard 4. The validity range `x ≥ 2 634 800 823` is the corrigendum-corrected one
> and is load-bearing: in-run data at `p < 3·10⁶` shows `T_n ≤ S(p_n)` at 14 426 indices, the
> largest at `p = 2 875 681` (§9). Fact S2 is false below its range, and this is not a defect —
> it is the range doing its job.]`**

> **Theorem B (the maximal-gap reduction, repaired and unconditional).**
> Let `N₂` be any index with `p_{N₂} ≥ p_{N₁} ≥ 2 634 800 823`, `N₁ ≥ 10`. Suppose
> `g_m < S(p_m)` for every maximal-gap index `m ∈ [N₁, N₂]`, and
> `max{g_j : j < N₁} < S(p_{N₁})`. Then `F` holds at every `k ∈ [N₁, N₂]`.
>
> *Proof.* Lemma M′ with `B = S` (nondecreasing by S1) gives `g_k < S(p_k)` for all
> `k ∈ [N₁,N₂]`. Fact S2 gives `S(p_k) < T_k` in that range. So `g_k < T_k`, which is `F` at `k`
> (**L1**). ∎

**This discharges, unconditionally, the entire practical content of L15/P6′.** The run's ranked
"open obligation #1" — *"Discharge P6′. Bound `T`'s oscillation below its coarse trend with
Dusart's effective bounds"* (INDEX §5, rank 1) — asks for a proof of a statement about the
oscillation of `T`. **No consumer needs it.** The oscillation of `T` is irrelevant to the
pruning, because the pruning can be run against `S`, which does not oscillate. The obligation as
posed is not merely hard (§7) — it is *misdirected*.

**Corollary (what Kourbatov's verification actually is).** Card **L6** records that Kourbatov's
verification to `2⁶⁴` is "exactly this criterion (**L4**) run over a first-occurrence gap table".
Theorem B is the missing justification of *why* running it over a gap table is sound. The run's
card set contained **L4** (the bar `S`), the monotonicity of `S` (unstated but immediate), and
**L15** (the open obligation) — and never joined the first two, so the third stayed open. The
join is Theorem A. `[This is a correction to the run's own priority ordering; see §11.]`

**Small-index bookkeeping, verified in-run.** For `N₁ = 10`: `max{g_j : j ≤ 9} = 6` and
`S(p_10) = S(29) = 6.8014 > 6`, so M′(ii) holds at `N₁ = 10`. This is exactly where Kourbatov's
"`k > 9`, `p_k ≥ 29`" hypothesis (**L4**) comes from. In-run, the `S`-breaches over
`1 ≤ k ≤ 216 815` are exactly `k ∈ {1, 2, 3, 4, 6, 9}` — all with `k ≤ 9`, none a record index
except `k ∈ {1,2,4,9}`. **`k = 3` and `k = 6` are `S`-breaches that are not records**, which is
Lemma M's sharpness remark (iii) made concrete: only the *first* breach is forced to be a record.

---

## 5. Why Lemma M does not settle the target

Apply Lemma M with `B = T`. The hypothesis fails: **`T` is not nondecreasing.**

`T_{n+1} < T_n` at **121 238 of 216 805** steps with `n ≥ 10` (55.92 %), sieve to `3·10⁶`,
recomputed in this leg (**D5** fact 2, **L15**). The mechanism is discreteness: `p` jumps by
`g_n` while `n` increments by 1, and `T_n` is *decreasing* in `n` at fixed `p` (**D5** fact 1).
So the exact bar rises when a gap is large and falls when a gap is small — a bar that moves with
the very quantity it is supposed to bound.

This is the whole difficulty of the target, and it is worth stating in the form Lemma M makes
available:

> **(M1) would be immediate if the exact bar `T_n` were a nondecreasing function of `p_n` alone.
> It is neither a function of `p_n` alone (it depends on `n = π(p_n)`) nor nondecreasing.**

Everything in §6–§7 is an attempt to buy back enough monotonicity.

---

## 6. Theorem C — near-record maximality, proved with an explicit window

The strategy: sandwich `T` between two *monotone* bars and pay the band width in separation.

> **Lemma W (sandwich).** Suppose `A(x) ≤ T_n ≤ C(x)` at `x = p_n` for all `n` with `p_n ≥ X₀`,
> with `A, C` nondecreasing. Let `n₀` be the least failure of `F`. Then for every `m < n₀` with
> `p_m ≥ X₀` and `C(p_m) ≤ A(p_{n₀})`, one has `g_m < g_{n₀}`.
>
> *Proof.* `T_m ≤ C(p_m) ≤ A(p_{n₀}) ≤ T_{n₀}`. Since `m < n₀` and `n₀` is the least failure,
> `g_m < T_m`. Therefore `g_m < T_m ≤ T_{n₀} ≤ g_{n₀}`, the last step because `n₀` *is* a
> failure. ∎

Note the shape: Lemma W recovers, for one pair `(m, n₀)`, exactly the inequality `T_m ≤ T_n` that
(M3) asserts for all record-straddling pairs — but only when the two primes are far enough apart
to cover the band width `C − A`.

### 6.1 The two-sided bounds on `T_n`

Both are derived here from the effective `π(x)` estimates in **T1**; neither is quoted as a
finished bracket, because **L2** hazard 4 flags the published bracket `−3.83/L < f_k − (L²−L−1) < 0`
as a **locator-precision item** (it may live in Kourbatov Theorem 4 as a *hypothesis*, not as a
proved bound on `f_k`). This leg therefore re-derives what it needs and does not cite that
bracket.

Write `x = p_n`, `ℓ = L_n`, `u = ℓ/π(x)`, so `T_n = x(e^u − 1)`. Two elementary facts are used
throughout: `x(e^{v/x} − 1) > v` for `v > 0`, and `x(e^{v/x} − 1) ≤ v(1 + v/x)` for `0 < v ≤ x`.

**(D-low) `T_n > ℓ² − 1.1ℓ` for `x ≥ 60 184`.**
Dusart Thm 6.9 eq. (6.6): `π(x) ≤ x/(ℓ − 1.1)` for `x ≥ 60 184` (**T1**, L0). Hence
`u ≥ ℓ(ℓ − 1.1)/x`, so `T_n = x(e^u − 1) > ℓ(ℓ − 1.1) = ℓ² − 1.1ℓ`. ∎

**(D-high) `T_n ≤ (ℓ² − ℓ)(1 + (ℓ² − ℓ)/x)` for `x ≥ 5393`.**
Dusart Thm 6.9 eq. (6.6): `π(x) ≥ x/(ℓ − 1)` for `x ≥ 5393`. Hence `u ≤ ℓ(ℓ − 1)/x =: v/x` with
`v = ℓ² − ℓ`, and `T_n ≤ v(1 + v/x)`. ∎

**(A-low) `T_n > ℓ² − ℓ − 1.17` for `x ≥ 2 634 800 823`.** This is Fact S2. `[Axler, unopened.]`

**(A-high) `T_n ≤ (ℓ² − ℓ − 1 − 1/ℓ)(1 + ℓ⁴/x)` for `x ≥ 1 772 201`.**
Axler Cor. 3.6 (**T1**): `π(x) > x/(ℓ − 1 − 1/ℓ − 1/ℓ²)`. Hence
`u < ℓ(ℓ − 1 − 1/ℓ − 1/ℓ²)/x = (ℓ² − ℓ − 1 − 1/ℓ)/x =: v/x`, and `T_n ≤ v(1 + v/x) ≤ v(1 + ℓ⁴/x)`
using `v < ℓ²`. ∎ `[Axler, unopened.]`

All four bars are increasing in `x` on the ranges quoted (each is a polynomial in `ℓ` with
positive derivative there; checked in §9). In-run, over `p < 3·10⁶`, **(D-low)** and **(D-high)**
have **zero** failures inside their stated ranges (§9), and the two Axler-based bars fail exactly
*below* their stated ranges and nowhere above — a corroboration of the ranges, not of the bounds.

### 6.2 The window

> **Theorem C.** Suppose `F` is false and let `n₀` be its least failure. By **L6**,
> `p_{n₀} > 2⁶⁴`, hence `L_{n₀} > 44.36` and (by D-low) `T_{n₀} > 1919`.
> Let `m < n₀`. Then `g_m < g_{n₀}` in each of the following cases.
>
> **(a) [Dusart only — no unopened source]** `p_m ≤ p_{n₀} · e^{−0.0623}`, i.e.
> `p_m ≤ 0.93960 · p_{n₀}`.
>
> **(b) [with Axler]** `p_m ≤ p_{n₀} · e^{−0.004479}`, i.e. `p_m ≤ 0.99553 · p_{n₀}`; and more
> sharply, whenever `log p_{n₀} − log p_m ≥ (0.17 − 1/ℓ + ℓ⁴/p_m)/(2ℓ − 1)` with `ℓ = L_m`,
> a quantity asymptotic to `0.085/ℓ`.

*Proof of (a).* If `p_m < 60 184`, then `g_m ≤ 72` (largest gap below `60 184`, computed in-run)
while `g_{n₀} ≥ T_{n₀} > 1919`, so `g_m < g_{n₀}` outright. Otherwise `p_m ≥ 60 184 > 5393`, so
(D-high) applies at `m` and (D-low) applies at `n₀`. Put `ℓ = L_m ≥ log 60 184 = 11.005`,
`λ = L_{n₀} = ℓ + d`, `ε := (ℓ² − ℓ)²/p_m`. By Lemma W it suffices that
`(ℓ² − ℓ)(1 + (ℓ²−ℓ)/p_m) ≤ λ² − 1.1λ`, i.e.

```
2ℓd + d² − 1.1 d − 0.1 ℓ  ≥  ε .
```

The left side is increasing in `d`, so it suffices that `d ≥ (0.1ℓ + ε)/(2ℓ − 1.1)`. Since
`p_m ≥ max(e^ℓ, 60 184)`, the right side is maximised at `ℓ = 11.005` where it equals
`0.062251`; it decreases in `ℓ` thereafter (verified over `ℓ ∈ [11, 400]`, §9). Hence
`d ≥ 0.0623` suffices for every admissible `ℓ`. ∎

*Proof of (b).* Identical with (A-high) at `m` and (A-low) at `n₀`. If `p_m < 1 772 201` then
`g_m ≤ 132` (in-run) `< 1919 < g_{n₀}`. Otherwise the requirement is
`(ℓ² − ℓ − 1 − 1/ℓ)(1 + ℓ⁴/p_m) ≤ λ² − λ − 1.17`, i.e. `d(2ℓ − 1) + d² ≥ 0.17 − 1/ℓ + ℓ⁴/p_m`,
for which `d ≥ (0.17 − 1/ℓ + ℓ⁴/p_m)/(2ℓ − 1)` suffices. With `p_m ≥ max(e^ℓ, 1 772 201)` this is
maximised at `ℓ = 14.400` (`= log 1 772 201`), where it equals `0.004479`. ∎

**Reading of Theorem C.** *If Firoozbakht first fails at `n₀`, then `g_{n₀}` exceeds every gap
between any two primes below `0.9396·p_{n₀}` — unconditionally — and below `0.99553·p_{n₀}` if
Axler's corollaries are admitted. The first failure is a record among all but a thin top sliver
of the primes preceding it, and the sliver's relative width shrinks like `0.085/log p_{n₀}`.*

At `p_{n₀} ≈ 2⁶⁴` the (b)-sliver has relative width `0.168 %`; at `L = 100` it is `0.080 %`.
It never closes, and §7 says why.

---

## 7. The obstruction, stated exactly

Theorem C leaves a window `p_m ∈ (p_{n₀}e^{−d*}, p_{n₀})`. Inside it the sandwich is useless: the
band width `C − A` exceeds the increment of `A` across the window, by construction of `d*`. So
either the band must be narrowed, or `T_m ≤ T_n` must be attacked directly. Both routes end at
the same place.

### 7.1 The exact criterion

`T_n = p_n(e^{u_n} − 1)` with `u_n = L_n/n` and `n = π(p_n)`. Since `u_n ≤ L_n²/p_n · (1+o(1))`
is minuscule for `p_n > 2⁶⁴` (`u < 1.1·10⁻¹⁶`), `T_n = p_n u_n (1 + u_n/2 + O(u_n²))`, and the
correction is smaller than `10⁻¹⁶` relative. So, to that precision,

```
T_m ≤ T_n     ⟺     p_m L_m / π(p_m)  ≤  p_n L_n / π(p_n) .
```

Write `y = p_n − p_m` and `k = π(p_n) − π(p_m) = n − m`. Expanding to first order in `y/p_m`:

```
T_m ≤ T_n     ⟺     k  ≤  y · (1 + 1/L_m) · π(p_m)/p_m  ·  (1 + O(y/p_m)) .
```

**Verified in-run: the first-order criterion agrees with the exact comparison `T_m ≤ T_n` on
19 980 / 19 980 random pairs (100.0 %)** with `m ≥ 1000`, `n − m ≤ 400` (§9).

Since `π(x)/x ≈ 1/(log x − 1)`, the criterion reads, in words:

> **`T_m ≤ T_n` holds exactly when the interval `(p_m, p_n]` contains no more than
> `≈ y/(L − 2)` primes** — i.e. when the *average gap over the block is at least about `L − 2`*.

This is why `T` coarsely increases: the *local* prime density near `x` is `1/L`, while the
*running-average* density `π(x)/x` is `1/(L−1)`. The surplus `1/(L−1) − 1/L ≈ 1/L²` is the entire
drift, and it is what makes the criterion satisfiable with room to spare on average — the
required bound `y/(L−2)` sits a relative `≈ 2/L` **above** the PNT-expected count `y/L`.

*(This also settles, in passing, the `L`-versus-`L−1`-versus-`L−2` dispute recorded in
`synthesis.md` D2 and **D5** hazard 3: `L − 2` is the correct single-step threshold, and it is
correct because `π(x)/x ≈ 1/(L−1)` rather than `1/L`. The in-run misclassification rates —
7.07 % at `L`, 2.79 % at `L−1`, **0.295 % at `L−2`** — are the measurement of exactly this.)*

### 7.2 Why the window resists

Inside the window, `y ≤ p_m(e^{d*} − 1) ≈ 0.085 p_m/L`. What is required is an **upper** bound on
`π(p_m + y) − π(p_m)` that is within a factor `1 + 2/L` of the truth. What is available
unconditionally is Brun–Titchmarsh, `π(x + y) − π(x) ≤ 2y/log y`. Numerically, in the window:

| `L = L_{n₀}` | window `y` | needed `≤ y/(L−2)` | PNT `y/L` | Brun–Titchmarsh `2y/log y` | BT / needed |
|---|---|---|---|---|---|
| 44.36 (`2⁶⁴`) | `3.10·10¹⁶` | `7.314·10¹⁴` | `6.984·10¹⁴` | `1.632·10¹⁵` | **2.231** |
| 50 | `7.85·10¹⁸` | `1.635·10¹⁷` | `1.570·10¹⁷` | `3.608·10¹⁷` | **2.207** |
| 100 | `2.16·10⁴⁰` | `2.205·10³⁸` | `2.160·10³⁸` | `4.652·10³⁸` | **2.110** |
| 200 | `2.99·10⁸³` | `1.509·10⁸¹` | `1.494·10⁸¹` | `3.109·10⁸¹` | **2.060** |

> **Obstruction (stated precisely).** Closing the residual window of Theorem C requires an
> unconditional upper bound on primes in a short interval of length `y ≍ x/log x` that improves
> the Brun–Titchmarsh constant from `2` to `1 + O(1/log x)` — i.e. essentially to the truth. No
> such bound is known; removing the factor `2` from Brun–Titchmarsh is a long-standing open
> problem, and the uniform-in-`x` statement `π(x + y) − π(x) ≤ π(y)` (the second Hardy–Littlewood
> conjecture) is generally believed **false**. The required margin over the PNT-predicted count
> is only `1 + 2/L` — a `4.7 %` relative slack at `2⁶⁴`, shrinking to `1 %` at `L = 200` — so the
> needed estimate is not merely a constant improvement but an *asymptotically exact* short-interval
> count.

`[The Brun–Titchmarsh statement and the second Hardy–Littlewood conjecture are **not sourced** in
this run: no ledger row covers either. They are standard and undisputed, and they are used here
only to *name an obstruction*, never to support a positive claim. Flagged as a declared gap
(§10.3), in the same category as the six unsourced items already listed at INDEX §5 rank 5.]`

### 7.3 The same obstruction, from the other side

The alternative to attacking `T_m ≤ T_n` directly is narrowing the sandwich. The band widths
achieved above are `0.1ℓ` (Dusart) and `0.17 − 1/ℓ` (Axler). Narrowing to width `Δ` shrinks the
window to `d* ≈ Δ/(2ℓ)`, and closing it entirely (`d*` below one gap, `≈ ℓ²/x`) requires
`Δ ≲ 2ℓ³/x` — an *absolute* accuracy in `T_n` of order `x^{−1+o(1)}`, i.e. a two-sided estimate
for `π(x)` accurate to `O(1)` primes. That is far beyond RH (which gives `O(√x log x)`).
**So the sandwich route cannot close the window at any level of effective-constant improvement.**
The two routes are the same wall from two sides, and neither is a matter of sharper constants.

---

## 8. The residual, heuristically

`[HEURISTIC. Rests on L9/L10, which are statements about the Cramér model, not about the primes.
Nothing in this section is evidence about `F` or about (M1). It is recorded because a leg that
reported only the obstruction would misrepresent how much of the target is actually at risk.]`

An `m` surviving Theorem C must satisfy `g_m ≥ g_{n₀} ≥ T_{n₀} ≈ L² − L − 1.17` with
`p_m` inside a window of length `W = p_{n₀}(1 − e^{−d*})`, `d* ≈ 0.085/L`. In the Cramér model a
gap at height `x` exceeds `G` with probability `≈ e^{−G/log x}`, and the window holds `≈ W/L`
primes, so the expected number of competing indices is

```
(W/L) · e^{−(L² − L − 1.17)/L}  ≈  0.085 · e / L²  ≈  0.231 / L² .
```

Computed: `1.06·10⁻⁴` at `L = 44.36`, `8.4·10⁻⁵` at `L = 50`, `2.2·10⁻⁵` at `L = 100` (§9).

> **Heuristic reading.** Under the Cramér model the residual window is empty with probability
> `1 − O(1/log²p_{n₀})`. So (M1) is heuristically true, and *the part of it this leg failed to
> prove is the part that the model says almost never happens*. That is the honest calibration:
> the obstruction of §7 is real as mathematics and thin as risk.

**It does not license writing "(M1) holds".** The same model predicts
`limsup g_n/log²p_n ≥ 2e^{−γ} > 1` (**L10**), which is incompatible with `F` itself (**L3**), so
the model is known to disagree with at least one thing this run cares about. Using it as evidence
here and refusing it there would be selective.

---

## 9. Verification performed by this leg

Sieve of Eratosthenes to `3·10⁶` (216 816 primes, largest `2 999 999`), 1-indexed. Scripts:
`attack/probe_t0.py`, `attack/probe_t0b.py`, `attack/probe_t0c.py` — every number below is
produced by a committed script, and no number in this document is quoted from an upstream artifact
without being recomputed here.

| # | Check | Result |
|---|---|---|
| 1 | Failures of `F`, `1 ≤ n ≤ 216 815` | **none** |
| 2 | `S`-breaches (`g_k ≥ L² − L − 1.17`) | exactly `k ∈ {1, 2, 3, 4, 6, 9}` |
| 3 | Are all `S`-breaches records? | **no** — `k = 3, 6` are not; only the first (`k=1`) is forced (Lemma M sharpness) |
| 4 | `S`-breaches with `k > 9` | **none** — Kourbatov's threshold is exactly right |
| 5 | Lemma M′(ii) at `N₁ = 10` | `max{g_j : j ≤ 9} = 6 < S(29) = 6.80139` ✓ |
| 6 | Maximal-gap (record) indices in range | **21** |
| 7 | `T_n < T_{m(n)}`, `m(n)` = governing record index | **0 exceptions in 216 815 pairs** (reproduces **L15**) |
| 8 | (D-low) `T_n > L² − 1.1L` for `p_n ≥ 60 184` | **0 failures** |
| 9 | (D-high) `T_n ≤ (L²−L)(1 + (L²−L)/p_n)` for `p_n ≥ 5393` | **0 failures** |
| 10 | Largest `n` with `T_n ≤ L² − L − 1.17` | `n = 208 494`, `p = 2 875 681` — **below** Axler Cor. 3.5's range `2 634 800 823`, so (A-low) is not contradicted |
| 11 | Largest `n` with `T_n ≥ L² − L − 1` | `n = 52 370`, `p = 644 117` — **below** Axler Cor. 3.6's range `1 772 201`, so (A-high) is not contradicted |
| 12 | First-order criterion §7.1 vs exact `T_m ≤ T_n` | **19 980 / 19 980 = 100.00 %** agreement |
| 13 | Max gap below `60 184` / below `1 772 201` | `72` / `132` (used in Thm C) |
| 14 | Uniform Dusart constant `d*` | `max = 0.062251` at `ℓ = 11.005`; `d = 0.0623` valid for all `ℓ ∈ [11, 400]` |
| 15 | Uniform Axler constant `d*` | `max = 0.004479` at `ℓ = 14.400`; `→ 0.085/ℓ` asymptotically |
| 16 | Brun–Titchmarsh shortfall in the window | ratio `2.231 → 2.060` for `L = 44.36 → 200` |
| 17 | Cramér residual `0.231/L²` | `1.06·10⁻⁴` at `L = 44.36` |

**Scale disclaimer, repeated because it is easy to lose.** `3·10⁶` is ≈12.8 orders of magnitude
below the published frontier `2⁶⁴` (**L6**). Items 1–13 are sanity probes on the *statements*;
they are **not** verification of `F` and are not cited as such anywhere above. Items 14–17 are
evaluations of closed-form expressions and carry no range limitation.

**One check that could not be run.** Every theorem in §4 and §6 has hypotheses that begin above
`10⁹`; the in-run sieve cannot exercise them. Items 10 and 11 are the closest available: they
confirm that the Axler-derived bars fail *only below* their stated ranges. That is consistency,
not confirmation.

---

## 10. Declared gaps

Stated so nothing downstream mistakes silence for coverage.

1. **(M1) is not proved.** Theorem C proves it outside a window of relative width `0.0623`
   (Dusart) or `0.004479` (Axler). The window is not closed, and §7.3 argues it cannot be closed
   by sharper constants.
2. **(M3)/P6′ is not proved either, and this leg did not try after §4.** Theorem A removes its
   only known consumer. If some later leg finds a consumer that genuinely needs `T_m ≤ T_n` (and
   not merely a monotone surrogate), P6′ returns as an obligation — and §7 applies to it verbatim,
   which means the run's assessment of it as "a Dusart lookup, not a research leg"
   (`synthesis.md` C7, INDEX §5 rank 1) is **wrong**: it is a short-interval prime-counting
   problem beyond Brun–Titchmarsh. *That correction stands independently of whether anyone still
   wants the lemma.*
3. **Two statements used to name the obstruction are unsourced in this run**: Brun–Titchmarsh
   (`π(x+y) − π(x) ≤ 2y/log y`) and the status of the second Hardy–Littlewood conjecture. Both
   are standard; neither supports a positive claim here; both belong on the citation gate's
   rank-5 list alongside the six items already there (INDEX §5).
4. **Facts S2, (A-low) and (A-high) rest on `axler2014newbounds`, tier L2_strong, NOT OPENED.**
   Theorem B and Theorem C(b) inherit that. **Theorem C(a) does not** — it uses only
   `dusart2010estimates` (L0, read in full), which is why it is stated separately despite being
   14× weaker. If the citation gate cannot raise Axler to L0, C(a) is what survives, and
   Theorem B must be re-derived on a Dusart-only bar (feasible: any nondecreasing `B` with
   `B ≤ T` works, e.g. `B(x) = log²x − 1.1 log x` by (D-low) — at the cost of a bar `≈ 0.1L`
   looser than Kourbatov's, hence a weaker verification criterion).
5. **The first-order expansion in §7.1 is verified numerically, not proved with explicit error
   terms.** The *statement* of the obstruction does not depend on it (Lemma W and Theorem C are
   proved without it); §7.1 is the diagnosis of *why* the window resists, and a fully explicit
   version would need the `O(y/p_m)` term carried. Flagged rather than hidden.
6. **`n₀ > 2⁶⁴` is imported from L6**, whose provenance is Kourbatov's verification. Theorem C
   uses it only to make `T_{n₀} > 1919` available for the small-`p_m` cases; the theorem's
   substance is unaffected if the frontier were smaller (the constants `72` and `132` would need
   re-checking against a smaller `T_{n₀}`).
7. **No Lean was written.** The backend is Lean 4 / Mathlib and this leg produced no formal
   artifact; §12 records what should be formalized and in what order. Card **D1**'s off-by-one
   correction (Mathlib's `Nat.nth` is 0-indexed) has **not** been applied anywhere in this
   document, which is uniformly 1-indexed. Any transcription to Lean must re-index every
   threshold: `k > 9`, `n₀`, `N₁ = 10`.

---

## 11. What this changes upstream

| # | Upstream statement | Correction |
|---|---|---|
| 1 | **L15** / INDEX §5 rank 1: "Discharge P6′ … the single most tractable open obligation in the attack." | **Misdirected.** P6′ has one consumer (the search pruning) and that consumer is served unconditionally by Theorem A + Theorem B, which need no property of `T` at all. The obligation should be **retired**, not worked. |
| 2 | `synthesis.md` C7 / **L15**: P6′ is "a Dusart lookup, not a research leg" (wheeler, 4/5 concurrence). | **Wrong, and in the direction the panel did not consider.** §7 shows P6′ for short blocks is equivalent to a short-interval prime count sharper than Brun–Titchmarsh by a factor ≈2. The panel measured that P6′ is *empirically unviolated* — which it is — and inferred tractability from robustness. The two are unrelated. |
| 3 | **T5**(d): "if L15 were discharged this would become a proof that `n₀` is a record index." | **Now unnecessary as stated, and partly delivered.** Theorem C proves the record property against all `m` with `p_m ≤ 0.9396 p_{n₀}` without L15. T5(d) should be restated as: *`n₀` is a record among primes below `0.9396 p_{n₀}` (unconditional), `0.99553 p_{n₀}` (with Axler); the residual is open.* |
| 4 | **L6**: "Kourbatov's verification is exactly this criterion (**L4**) run over a first-occurrence gap table." | **The justification was missing and is now supplied** (Theorem B). The card set held **L4** and the monotonicity of `S` separately and never joined them; that is why L15 stayed open. |
| 5 | `synthesis.md` D2 / **D5** hazard 3: the `T`-increase threshold is `L−2` "and the derivation cannot resolve it anyway". | **It can, and the reason is structural, not numerical**: `π(x)/x ≈ 1/(L−1)` (running average) versus local density `1/L`. §7.1. The measurement `0.295 %` at `L−2` is then explained, not merely observed. |
| 6 | **L15** hazard 2 (laundering): "a pruned search that finds nothing establishes `F` holds at record indices, not `F`." | **No longer a hazard for the `S`-pruned search.** Under Theorem B a null result over record indices *is* a verification of `F` on the range, unconditionally. The hazard remains exactly for a search pruned against the exact bar `T`. The distinction is now sharp and should be stated that way in **T2**. |

---

## 12. Notes for the Lean legs

The results here are unusually Lean-friendly, and that is not an accident: Lemma M is the whole
engine and it has no analysis in it.

| Node | Content | Effort | Depends on |
|---|---|---|---|
| **M-1** | Lemma M: `Monotone B → IsLeast {k | B (p k) ≤ g k} k₀ → ∀ m < k₀, g m < g k₀` | **low** — three rewrites, no `Real` beyond `B`'s codomain | `D1` (fixed indexing) |
| **M-2** | Lemma M′ (truncated form, with the `N₁` side condition) | low | M-1 |
| **M-3** | `S(x) = log²x − log x − 1.17` is `Monotone` on `x ≥ 2` | low — `Real.log` monotone + `deriv` or direct algebra | Mathlib `Real.log` |
| **M-4** | Theorem A (record-scan completeness) | low | M-2, M-3 |
| **M-5** | Fact S2 (`S < T`) as an **explicit hypothesis**, not a proof | — | must be `axiom`/hypothesis: Axler is not in Mathlib |
| **M-6** | Theorem B | low, given M-4 + M-5 | |
| **M-7** | Lemma W (sandwich) | low | — |
| **M-8** | Theorem C(a) with the arithmetic of `d = 0.0623` | medium — `norm_num` on the quadratic; the `ε` bookkeeping is the fiddly part | M-7 + Dusart as hypotheses |

**M-1 through M-4 are provable in Mathlib today with no number-theoretic input whatsoever** — they
are order theory. That makes them a better first Lean deliverable than **L14** (the smooth model),
which `synthesis.md` C4 found unanimously over-billed and consumer-less, and arguably better than
**L2/L5**: M-1..M-4 are *used* by the rest of this document, and they are what makes a
machine-checked verification criterion (Theorem B) meaningful.

**The indexing hazard is acute here.** Every threshold in §4 (`k > 9`, `N₁ = 10`, `p ≥ 29`) is
1-indexed. Under Mathlib's 0-indexed `Nat.nth Nat.Prime` they shift by one, and Lemma M′(ii) is
exactly the kind of side condition an off-by-one silently satisfies with the wrong constant.
See **D1**, **T4**, and correction 1 of INDEX §4.

---

## 13. Standing instruction, restated

The conjecture is **OPEN**. Nothing above asserts `F`, and nothing above asserts (M1).

The defensible sentences produced by this leg:

> *The maximal-gap reduction fails for Firoozbakht's exact threshold `T_n`, which is not monotone,
> and holds unconditionally for Kourbatov's sufficient bar `log²p − log p − 1.17`, which is. A
> verification of the conjecture over an initial segment may therefore be carried out on
> maximal-gap records alone, with no unproved lemma imported.*

> *If Firoozbakht's conjecture fails, its first failure occurs at a gap larger than every gap
> between primes below `0.9396·p_{n₀}` — unconditionally — and below `0.99553·p_{n₀}` if Axler's
> effective `π(x)` corollaries are admitted. Whether the first failure is a record outright is
> open, and closing it requires a short-interval prime count beyond Brun–Titchmarsh.*
