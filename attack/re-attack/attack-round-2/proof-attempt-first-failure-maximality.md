# Proof attempt, round 2 — subquestion `first-failure-maximality`

**Molecule:** `task-20260726-56a7` (re-attack leg, subquestion `first-failure-maximality`)
**Re-attack root:** `reattack-20260726-57d1` · **Date:** 2026-07-26 · **Backend:** Lean 4 / Mathlib
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.

> **Status of `F` in this document: OPEN.** Neither assumed true nor assumed false. Nothing below
> asserts `F` or its negation. The Lean target `Firoozbakht.firoozbakht : Conjecture`
> (`lean/Firoozbakht/Statement.lean:186`) remains the single `sorry` in the development and is
> correctly open. **`lean/Firoozbakht/Statement.lean` was not touched by this leg.**

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

## 0. Perimeter — what was read, what was recomputed, what was fetched

**Read in full (round-1 inputs, pinned):**

| Artifact | Role here |
|---|---|
| `attack/faults.md` (444 lines, molecule `task-20260725-488f`) | the skeptic report; F1 is this leg's assigned BLOCKER |
| `attack/lean-probe-report.md` (279 lines, molecule `task-20260725-9975`) | the kernel report; fixes what is frozen |
| `attack/proof-attempt-0.md` (603 lines, molecule `task-20260725-a1cd`) | the round-1 attempt on this same subquestion |
| `attack/notebook-0/findings-0.md`, `attack/notebook-2/findings.md` | the two sibling legs whose headlines F1 says cannot be reconciled |
| `attack/concept-cards/` (L15, T1, D1–D7, L1–L6, T2–T5), `attack/source-ledger.md` | pinned, reused verbatim |

**Reused verbatim, not re-derived:** the concept cards and the Lean skeleton. The theorem
statement is FROZEN.

**Independently recomputed by this leg.** Every number in §3, §5, §7 and §9 was produced by code
written from the *statements*, not from any upstream code path (`attack/notebook-0/ffm_lab.py`
and `attack/notebook-2/fb_core.py` were read for their *definitions* and then closed). Scripts are
written to this molecule directory alongside this document as `r2_pred.py`, `r2_axler.py`,
`r2_final.py`, `r2_const.py`, and were re-run from it to confirm they are self-contained (all
exit 0, no network, no data files).
Sieve to `10⁹` (`π(10⁹) = 50 847 534`, matching the standard value); high-precision checks at 50–60
decimal digits with `mpmath`.

**Bounded source refresh (F3).** One source was opened, because it is load-bearing to *this*
subquestion and to no other unopened row: `axler2014newbounds`. Three documents were fetched
(§7.1). The ledger was **not** re-opened wholesale; the single affected row is amended in place.

**Round-1 faults in scope for this leg, and their disposition:**

| Fault | Severity | Disposition here |
|---|---|---|
| **F1** — `m(n)` carries three inequivalent meanings; two sibling legs publish opposite trends | BLOCKER | **RESOLVED** — §1 names and defines the three predicates, §2 settles the implication lattice, §3 **refutes** the strongest one, §5 reconciles the two headlines |
| **F2** — `(A-high)` is too weak by `≈ ℓ²` to support Theorem C(b); the quoted constant sits below the document's own criterion | BLOCKER | **REPAIRED** — §7.2 restates the lemma in its tight form; §7.4 replaces the constant with one that is *both* rigorous and sharper |
| **F3** — Theorem B's discharge called "unconditional" on an unopened source | MAJOR | **DISCHARGED for this subquestion** — Axler opened to L0 (§7.1); and §7.1 records a new provenance defect the run had not seen |
| **F7** — `proof-attempt-0.md` §9 item 7 states the P6′ predicate with the inequality reversed | MINOR | **CORRECTED** in §5's measurement table |
| **F13** — gap 6's constants need re-checking under the F2 repair | MINOR | **DONE** — §7.4 recomputes every branch constant |

Faults **F4, F5, F6, F8–F12, F14** live in `proof-attempt-1.md`, `proof-attempt-2.md` and
`notebook-1`, i.e. in the RH-conditional and verified-range subquestions. They are **out of scope
for this leg** and are named here so that silence is not read as coverage.

---

## 1. Notation, and the three predicates named

Notation follows cards **D1**, **D2**, **D5**. `p_n` is the `n`-th prime, **1-indexed**
(`p_1 = 2`); `g_n = p_{n+1} − p_n`; `L_n = log p_n`; and

```
T_n  :=  p_n (p_n^{1/n} − 1)  =  p_n (e^{L_n/n} − 1)                       (D5)
F    ⟺  ∀ n ≥ 1,  g_n < T_n                                                (L1)
```

Call `n` a **failure** if `g_n ≥ T_n`. Call `n` a **record index** (maximal-gap index) if
`g_n > g_j` for every `j < n`. Write

```
r(n)  :=  max{ j ≤ n : j is a record index }          the governing record index
µ(n)  :=  min{ j     : g_j ≥ g_n }                     the minimal dominating index
```

Both are well defined for every `n ≥ 1` (`j = 1` is a record; `j = n` dominates `n`), and

> **Fact 0.** `µ(n)` is a record index, and `µ(n) ≤ r(n) ≤ n`.
>
> *Proof.* If `µ(n)` were not a record there would be `j < µ(n)` with `g_j ≥ g_{µ(n)} ≥ g_n`,
> contradicting minimality of `µ(n)`. For the second part: the running maximum of `g` at `n` is
> attained at `r(n)`, so `g_{r(n)} ≥ g_n`, so `r(n)` belongs to the set `µ(n)` minimises over. ∎

### 1.1 The subquestion

> **(M1) — first-failure maximality.** If `F` is false, its least failure `n₀` is a **strict**
> record index: `g_j < g_{n₀}` for every `j < n₀`.

This is the target. It is the statement `decompose.md` §2.4, card **L15** and card **T5**(d) all
route through, and it is what a record-pruned counterexample search consumes.

### 1.2 The three predicates — F1 resolved by naming

The symbol `m(n)` and the phrase *"governing record index"* carry **three inequivalent meanings**
across round 1. They are named here, once and for all, and every later sentence in this document
says which one it means.

> **P6′-pair** *(the "(C)" of `faults.md` F1 — card **L15**'s prose, and `proof-attempt-0.md` §1's
> (M3))*
> ```
> ∀ m < n  such that some record index j satisfies  m ≤ j < n :   T_m ≤ T_n .
> ```
> In words: whenever `p_m` and `p_n` straddle a record gap, `T_m ≤ T_n`. **`m` is arbitrary** —
> this is exactly what "for `m < n` with `p_m, p_n` straddling a record (maximal) gap" says.

> **P6′-gov** *(the "(A)" of F1 — `attack/notebook-2/fb_core.py:181-197`, card **L15**'s
> measurement row)*
> ```
> ∀ n :  T_{r(n)} ≤ T_n .
> ```
> Vacuous at record indices (`r(n) = n`), so it is a statement about the `n` **strictly after** a
> record.

> **P6′-min** *(the "(B)" of F1 — `attack/notebook-0/ffm_lab.py:14`)*
> ```
> ∀ n :  T_{µ(n)} ≤ T_n .
> ```

And one auxiliary predicate, which round 1 never isolated and which turns out to be the hinge of
the implication lattice:

> **P6′-rec** *(record-monotonicity)*
> ```
> for consecutive record indices  j < j' :   T_j ≤ T_{j'} .
> ```

**Each predicate is a statement about a range** — "on `[1,N]`" means: for every `n ≤ N` (and, for
P6′-pair, every admissible pair with `n ≤ N`). Unqualified, it means "for every `n`".

---

## 2. Verdict

| Claim | Verdict |
|---|---|
| **P6′-pair** (card **L15**'s prose; `proof-attempt-0.md` §1's (M3)) | **REFUTED.** Two explicit witnesses, exact arithmetic (§3) |
| **P6′-gov** | **OPEN.** 0 exceptions in `50 847 533` indices (`p < 10⁹`) *(was `50 847 503` — transposition, corrected 2026-07-27)* |
| **P6′-min** | **OPEN.** 0 exceptions in `50 847 533` indices (`p < 10⁹`) *(was `50 847 503` — transposition, corrected 2026-07-27)* |
| **P6′-rec** | **OPEN.** 0 exceptions in 29 record steps (`p < 10⁹`) |
| `P6′-pair ⟹ P6′-gov` and `P6′-pair ⟹ P6′-rec` | **PROVED**, elementary (§3.1) |
| `P6′-gov ∧ P6′-rec ⟹ P6′-min` | **PROVED**, elementary (§3.1) |
| `P6′-gov ⟹ P6′-min` **without** P6′-rec | **DISPROVED** as a formal implication — explicit counter-model (§3.2). *This corrects `faults.md` F1's chain, which asserts it.* |
| `P6′-min ⟹ P6′-gov` | **DISPROVED** as a formal implication — explicit counter-model (§3.2) |
| **P6′-gov at `n₀` alone ⟹ (M1)** | **PROVED**, elementary (§3.3) |
| **P6′-min at `n₀` alone ⟹ (M1)** | **PROVED**, elementary (§3.3) — this is the weakest known sufficient hypothesis |
| **(M1)** in full, unconditionally | **NOT PROVED.** The obstruction of `proof-attempt-0.md` §7 stands, and §8 records what the refutation of P6′-pair adds to it |
| **(M1)** restricted to `p_m ≤ 0.94970·p_{n₀}` | **PROVED** unconditionally, Dusart only (§7.4, Thm C-a′) — improves round 1's `0.93961` |
| **(M1)** restricted to `p_m ≤ 0.99824·p_{n₀}` | **PROVED**, Axler now at **L0** and *edition-independent* (§7.4, Thm C-b′) — improves round 1's `0.99553` and removes its dependence on a column that exists in only one edition |
| **Monotone-bar principle** (Lemma M/M′), **Theorem A**, **Theorem B** | **PROVED** in round 1; re-derived and confirmed here (§6) |

**One-sentence result.** *The strongest of the three predicates that round 1 conflated under the
name P6′ — the one card **L15** states in prose and `proof-attempt-0.md` adopts as (M3) — is
false, with witnesses at two different scales; the two weaker ones survive `5·10⁷` indices, each of
them alone implies first-failure maximality, and the weakest of them is precisely the one whose
empirical margin does **not** decay — which reverses `notebook-2` §3's consequence 3 without
contradicting a single number `notebook-2` measured.*

---

## 3. Theorem 1 — **P6′-pair is false** — and the implication lattice around it

> **Theorem 1.** There exist indices `m < j < n` with `j` a record index and `T_m > T_n`.
> Consequently **P6′-pair is false**, and it is false already on `[1, 1847]`.

*Proof.* Two witnesses, exhibited. Both were computed in `mpmath` at 60 decimal digits from the
definition `T_k = p_k(e^{log p_k / k} − 1)` with `p_k` read off an independent sieve.

**Witness W1.**

| | index | prime | value |
|---|---:|---:|---|
| `m` | 1823 | 15 641 | `T_m = 83.0807167192698…` |
| `j` (record) | 1831 | 15 683 | `g_j = 44` — the 12th maximal prime gap |
| `n` | 1847 | 15 823 | `T_n = 83.0521061144139…` |

`m < j < n`, and `p_m = 15 641 < 15 683 = p_j < p_{j+1} = 15 727 < 15 823 = p_n`, so `p_m` and
`p_n` straddle the record gap in the strictest available sense: the whole gap interval
`(p_j, p_{j+1})` lies between them. And

```
T_m − T_n  =  0.028610605…  >  0 .
```

**Witness W2** (to show W1 is not a small-prime artefact).

| | index | prime | value |
|---|---:|---:|---|
| `m` | 10 655 449 | 191 912 639 | `T_m = 343.5112716866658…` |
| `j` (record) | 10 655 462 | 191 912 783 | `g_j = 248` — the **28th** maximal prime gap |
| `n` | 10 655 590 | 191 915 033 | `T_n = 343.5112358945690…` |

```
T_m − T_n  =  3.5792097·10⁻⁵  >  0 .
```

∎

**The witnesses are not floating-point.** W1's margin is `2.9·10⁻²` against a `T ≈ 83`, whose
float64 ulp is `2⁻⁴⁶ = 1.4·10⁻¹⁴`: the margin is `2·10¹²` ulps. W2's margin is `3.6·10⁻⁵` against
`T ≈ 343.5`, whose ulp is `2⁻⁴⁴ = 5.7·10⁻¹⁴`: `6.3·10⁸` ulps. Both were nevertheless recomputed at
60 digits, because card **T2** Rule 3's hazard (*the silent failure is in the verification
direction*) applies here with the sign flipped — a *false* exception would be the reassuring
outcome for the run, and this leg is the one reporting it.

**Complete exception census, `p < 10⁹`** (this leg): **17** *indices* `n` carry a violation of
P6′-pair (the underlying violating `(m,n)` **pairs** number **20** below `3·10⁸` — `n = 1847`,
`n = 10 655 564` and `n = 10 655 590` each carry two violating `m`; amended 2026-07-27 per
`faults.md` R2-m2, decision 5). The census is complete as a list of `n`; it is **not** a pair count,
and the denominators in §9 items 3/5/7 are index counts too, so no ratio here may be read as a
density over admissible pairs — the true admissible-pair count below `10⁹` is `Σ_n r(n−1) ≈ 10¹⁵`.
The 17 indices sit in exactly two clusters — `n ∈ {1836, 1837, 1840, 1844, 1845, 1846, 1847}` and
`n ∈ {10 655 562, …, 10 655 594}` (10 indices). Both clusters sit a few indices *after* a maximal
gap, which is the structural spot `notebook-2` §3 identified for a different statistic. The
minimum over all admissible pairs is `−2.861·10⁻²`, attained at W1.

**What Theorem 1 does and does not do.**

- It **refutes card `L15`'s stated lemma** and **`proof-attempt-0.md` §1's (M3)**. `L15` is
  currently marked *"OPEN … empirically unviolated by every measurement that bears on it"*. That
  is now false as stated: the measurement that bears on the *prose* had never been run, and it
  violates it 17 times below `10⁹`.
- It **does not** touch P6′-gov, P6′-min or P6′-rec. Both W1 and W2 have `m` a **non-record**
  index, so no instance of P6′-gov or P6′-rec is implicated.
- It **does not** touch `F`, and it **does not** touch (M1). `F` is verified through `10⁹` in this
  leg's own sieve and (M1) is vacuous there.
- It **does not** invalidate the pruning route. §3.3 shows the pruning never needed P6′-pair.

---

### 3.1 The implications that hold

> **Proposition 2.** `P6′-pair ⟹ P6′-gov`, and `P6′-pair ⟹ P6′-rec`.
>
> *Proof.* **(gov)** Fix `n`. If `r(n) = n` then P6′-gov at `n` is `T_n ≤ T_n`. Otherwise put
> `m := r(n)` and `j := r(n)`; then `m < n` and `m ≤ j < n`, so the pair `(m,n)` is admissible for
> P6′-pair, which gives `T_{r(n)} ≤ T_n`.
> **(rec)** Let `j < j'` be consecutive record indices. Put `m := j`, `n := j'`; then `m ≤ j < n`,
> admissible, so `T_j ≤ T_{j'}`. ∎

> **Proposition 3.** `P6′-gov ∧ P6′-rec ⟹ P6′-min`.
>
> *Proof.* Fix `n`. By Fact 0, `µ(n)` is a record index and `µ(n) ≤ r(n)`. Both are record
> indices, so iterating P6′-rec along the record indices from `µ(n)` up to `r(n)` gives
> `T_{µ(n)} ≤ T_{r(n)}`. P6′-gov at `n` gives `T_{r(n)} ≤ T_n`. Chain. ∎

So the round-1 chain, corrected:

```
        P6′-pair   ⟹   P6′-gov  ∧  P6′-rec   ⟹   P6′-min
        (REFUTED)          (open)   (open)            (open)
```

### 3.2 The implications that do **not** hold — and this corrects `faults.md` F1

`faults.md` F1 states *"(C) ⟹ (A) ⟹ (B) as obligations, and the implications are strict."* The
first link is Proposition 2. **The second link is not valid as stated**: it needs P6′-rec.

> **Proposition 4.** In the abstract setting in which all four predicates are stated — a strictly
> increasing integer sequence with gap sequence `(g_k)` and an arbitrary real bar `(T_k)` —
> `P6′-gov ⟹ P6′-min` is **false**, and `P6′-min ⟹ P6′-gov` is **false**.
>
> *Proof.* Both by counter-model on four indices with gap sequence `g = (2, 4, 6, 3)`. The record
> indices are `1, 2, 3`; `r(4) = 3` and `µ(4) = 2` (the least `j` with `g_j ≥ 3`), so index 4
> separates the two predicates.
>
> **(a) `P6′-gov ⇏ P6′-min`.** Take `T = (0, 10, 1, 5)`. P6′-gov is vacuous at `n = 1,2,3`
> (record indices) and at `n = 4` reads `T_3 = 1 ≤ 5 = T_4` ✓. P6′-min at `n = 4` reads
> `T_2 = 10 ≤ 5 = T_4` ✗.
>
> **(b) `P6′-min ⇏ P6′-gov`.** Take `T = (0, 1, 10, 5)`. P6′-min is trivial at `n = 1,2,3`
> (`µ(n) = n` there) and at `n = 4` reads `T_2 = 1 ≤ 5 = T_4` ✓. P6′-gov at `n = 4` reads
> `T_3 = 10 ≤ 5 = T_4` ✗. ∎

**Why this matters and is not pedantry.** P6′-gov is *vacuous at every record index*, so it says
nothing whatsoever about how `T` moves from one record to the next — which is exactly the step
Proposition 3 needs. The run has been carrying "(A) ⟹ (B)" as though it were free; it is not, and
the missing ingredient (P6′-rec) is a fourth statement nobody has been measuring under its own
name. This leg measures it: **0 exceptions in 29 record steps below `10⁹`** (§9), and
`T_{µ(n)} ≤ T_{r(n)}` at **all** `50 847 533` indices below `10⁹`. So Proposition 3's hypothesis is
empirically available on the swept range — which is the honest statement, and is not a proof.

Proposition 4 is the same species of finding as `notebook-0` R1 ("FFM does not follow from the
definitions"): the separation is *structural*, visible without any arithmetic input, and it means
that any proof of `P6′-gov ⟹ P6′-min` must consume a property of the primes.

### 3.3 Each of the two survivors implies the subquestion — and needs only one instance

> **Theorem 2.** Suppose `F` is false and let `n₀` be its least failure. If **either**
> `T_{r(n₀)} ≤ T_{n₀}` (P6′-gov **at `n₀`**) **or** `T_{µ(n₀)} ≤ T_{n₀}` (P6′-min **at `n₀`**),
> then `g_j < g_{n₀}` for every `j < n₀` — i.e. **(M1) holds**.
>
> *Proof (P6′-min branch).* Put `m := µ(n₀)`, so `g_m ≥ g_{n₀}` by definition. Suppose `m < n₀`.
> By minimality of `n₀`, `m` is not a failure, so `g_m < T_m`. Then
> ```
> g_{n₀}  ≤  g_m  <  T_m  =  T_{µ(n₀)}  ≤  T_{n₀}  ≤  g_{n₀},
> ```
> the last step because `n₀` *is* a failure. This is `g_{n₀} < g_{n₀}` — a contradiction. Hence
> `m = n₀`, i.e. `min{ j : g_j ≥ g_{n₀} } = n₀`, i.e. `g_j < g_{n₀}` for every `j < n₀`. ∎
>
> *Proof (P6′-gov branch).* If `r(n₀) = n₀` then `n₀` is a record index and the conclusion is the
> definition of "record". Otherwise `r(n₀) < n₀`, so by minimality of `n₀`,
> `g_{r(n₀)} < T_{r(n₀)} ≤ T_{n₀} ≤ g_{n₀}`. For any `j < n₀`, `g_j ≤ g_{r(n₀)}` because `r(n₀)`
> carries the running maximum of `g` on `[1, n₀]`. Chaining, `g_j ≤ g_{r(n₀)} < g_{n₀}`. ∎

Three things this theorem fixes:

1. **The pruning never needed P6′-pair.** Theorem 1 refutes the strongest predicate and the
   consumer is untouched, because the consumer runs on either of the two weaker ones.
2. **P6′-min is a sufficient obligation, and by Theorem 2 the right one to work.** *(Amended
   2026-07-27, R2-M3: it is **not** "the weakest of the three". Proposition 4 proves `P6′-gov` and
   `P6′-min` **incomparable**; the only order relations proved here are `pair ⟹ gov`, `pair ⟹ rec`
   and `gov ∧ rec ⟹ min`. `P6′-min` is preferred because its margin does not decay and because
   Theorem 2 consumes it at a single index — not because it is weaker.)*
3. **A single instance suffices.** Both branches use the predicate only at `n₀`. This is the
   same shape as Lemma M (§6): the conclusion is forced at the *first* failure and says nothing
   about later ones.

---

## 4. Why Lemma M does not settle (M1) — restated, with the numbers corrected

Apply the monotone-bar principle (Lemma M, §6) with `B = T`. The hypothesis fails: **`T` is not
nondecreasing.** This leg's own count, at three ranges and under both conventions:

> ⚠ **AMENDED 2026-07-27 by the round-3 reconciliation leg (`task-20260727-264e`), decision 4.**
> Every **denominator** in the table as this leg originally printed it was **one too low**, at every
> range and under both conventions; every numerator was right. The corrected table is below and the
> adjudication paragraph under it is **reversed**. See `attack/reconciliation.md` §4 for the recount
> and `attack/synthesis.md` §5.4 for the third and fourth concurring counts.

| range | `T_{n+1} < T_n`, `n ≥ 10` | `T_{n+1} < T_n`, all `n` |
|---|---|---|
| `3·10⁶` | `121 238 / 216 806` = **55.9200 %** | `121 239 / 216 815` = 55.9182 % |
| `10⁷` | `374 485 / 664 569` = **56.3501 %** | `374 486 / 664 578` = 56.3494 % |
| `10⁸` | `3 280 063 / 5 761 445` = **56.9313 %** | `3 280 064 / 5 761 454` = 56.9312 % |

**Counting convention, stated so the table is reproducible.** A *step* is an index `n` for which
both `T_n` and `T_{n+1}` are defined from the sieve, i.e. `1 ≤ n ≤ π(N) − 1`. At `N = 3·10⁶`,
`π(N) = 216 816`, so there are `216 815` steps, and `216 806` of them have `n ≥ 10`. The figures
this leg first printed (`216 814 / 216 805`) come from differencing a `T`-array that had been
truncated to the *gap*-array length `π(N) − 1` **before** differencing — an implementation artefact,
not a counting convention.

**The adjudication, corrected.** This table does **not** settle the three-fractions dispute in the
direction first stated. `proof-attempt-0.md` §9 item 18's **`121 238 / 216 806` is the correct
`n ≥ 10` count** — round 1's `faults.md` F5 called it an off-by-one and this leg re-affirmed that
verdict; both were wrong. Likewise `notebook-1` §2's `374 485 / 664 569` at `10⁷` is correct, not
"denominator off by one". Card **L15**'s `121 238 / 216 805` and `notebook-0` R4's
`121 239 / 216 814` are each one too low and have been corrected in the tree. Corroboration from
inside this same round: the sibling leg's `proof-attempt-RH-conditional-bound.md` §10 states
`216 815 consecutive pairs` — the larger number. **The `55.92 %` figure is range-dependent**
(`notebook-0` R4 is right about that) and must never be quoted without both its bound and its
convention.

The statistic is nevertheless **not diagnostic for any of the three predicates** — it measures
single steps, and every predicate here compares an index to a governor many steps back. That is
card **L15** hazard 4, and this leg confirms it: the single-step down-fraction rises from
`55.92 %` to `56.93 %` across two decades while the P6′-min margin does not move at all (§5).

---

## 5. F1 dissolved — the two headlines reconciled

This is the resolution the BLOCKER asks for. Every measurement in the run that has been reported
under the name `min(T_n − T_{m(n)})` is listed with **the predicate it actually measures**.

| source | statistic reported | **predicate** | reproduced here? |
|---|---|---|---|
| `notebook-0` §2 finding 3 — *"The margin does not decay"* | `min(T_n − T_{µ(n)})` per decade; global min `0.485` at `n = 1879` | **P6′-min** | **yes, exactly**: `+0.4845277` at `n = 1879`, `p = 16 141`, `µ = 1831`, `p_µ = 15 683` — unmoved at `3·10⁶`, `10⁷`, `10⁸`, `10⁹` |
| `notebook-2` §3 — *"the empirical case … weakens"* | `min(T_n − T_{r(n)})` per range, decaying `≈ p^{−0.83}` | **P6′-gov** | **yes, exactly**: `+1.046415·10⁻²` (`3·10⁶`), `+6.060476·10⁻³` (`10⁷`), `+1.111812·10⁻³` (`10⁸`), `+1.120382·10⁻⁴` (`10⁹`) — matching every digit `notebook-2` quotes |
| card **L15** measurement row — *"0 exceptions in 216 815 pairs"* | exception count for `r(n)` | **P6′-gov** (denominator `216 794` once the 21 trivial self-pairs are excluded — which is godel's "slightly narrower pair convention" the card already notes) | **yes**: 0 exceptions, `216 794` admissible pairs at `3·10⁶` |
| card **L15** *prose* — *"for `m < n` straddling a record gap, `T_m ≤ T_n`"* | — | **P6′-pair** | **REFUTED**, §3 |
| `proof-attempt-0.md` §9 item 7 — *"`T_n < T_{m(n)}` … 0 exceptions"* | inequality printed **reversed** (`faults.md` F7) | intended **P6′-gov** | the corrected row is `T_{r(n)} ≤ T_n`, 0 exceptions in `216 794` admissible pairs |
| `proof-attempt-0.md` §1 (M3) | stated as P6′-pair | **P6′-pair** | **REFUTED**, §3 |

**The two headlines are both true, of different predicates, and neither needs retracting.**

- `notebook-0` measured **P6′-min**. Its margin is flat: the global minimum `0.4845277` at
  `n = 1879` is set in the fourth decade and is never approached again through `10⁹` (this leg) or
  `10¹¹` (`notebook-0`). Per-decade minima of the P6′-min margin, this leg: **`1.354`** (`10³`),
  `3.05` (`10⁴`), `0.4845` (`10⁵`), `1.68` (`10⁶`), `3.81` (`10⁷`), `1.70` (`10⁸`), `3.89` (`10⁹`)
  — no trend. *(The `10³` entry read `2.42`; corrected 2026-07-27 to the round-2 skeptic's
  independently recomputed `1.35373` at `p = 5` — `faults.md` **R2-m7**. The discrepancy is confined
  to indices below `n = 10`, where every criterion in this corpus is out of range; the section's
  claim — no trend, global minimum `0.4845277` at `n = 1879`, never approached again — is
  unaffected, and the skeptic reproduces the other six entries exactly. This leg's own recount was
  not re-run for this row: the correction rests on the skeptic, and is labelled as such.)*
- `notebook-2` measured **P6′-gov**. Its margin decays like `p^{−0.83}`.

Both are correct because `µ(n) ≤ r(n)` (Fact 0) and `T` grows along records, so the P6′-gov margin
is the *smaller* of the two at every index — this leg confirms `T_{µ(n)} ≤ T_{r(n)}` at all
`50 847 533` indices below `10⁹`, with 0 exceptions.

> ⚠ **AMENDED 2026-07-27 (round-3 reconciliation, decision 5; `faults.md` R2-M3).** The sentence
> that stood here — *"P6′-gov is the harder obligation … P6′-min is the easier obligation"* —
> contradicted this document's own **Proposition 4**, which proves `P6′-gov ⇏ P6′-min` **and**
> `P6′-min ⇏ P6′-gov`. The two predicates are formally **incomparable**. What is true is the
> **empirical** statement just made: on the swept range `T_{µ(n)} ≤ T_{r(n)}` at every index, so
> *on that range* the P6′-gov margin is the smaller of the two and gov ⟹ min — which is a
> measurement, not a proof, and must not be spent as one. The correct standing form:

**P6′-gov and P6′-min are incomparable (Proposition 4). P6′-min is the one Theorem 2 needs and the
one whose margin does not decay; P6′-gov is the one that decays and is empirically the tighter of
the two on `p < 10⁹`. Since Theorem 2 shows *either* predicate at `n₀` suffices, both stay on the
obligation list, alongside P6′-rec (Proposition 3 needs it). Dropping `gov` would be strictly
lossy.**

### 5.1 The two consequences `faults.md` F1 flags, resolved

**Consequence 2 — the float64 noise-floor alarm (`notebook-2` §3 point 2).** The alarm is derived
from the P6′-gov margin's `p^{−0.83}` decay: extrapolated to `2⁶⁴` it is `4.457·10⁻¹³` against a
`T ≈ 1919`. *(⚠ Amended 2026-07-27, `faults.md` **R2-m6**: `0.83` is **not** a constant exponent.
From the four margins in this very section the local per-decade exponents are `0.4536`, `0.7365`,
`0.9967` — monotonically **rising** toward `≈ 1`. At the last measured exponent the extrapolated
margin at `2⁶⁴` is `≈ 6.1·10⁻¹⁵`, smaller by a factor `≈ 55`. The direction is **safe** — the alarm
gets stronger, not weaker — and nothing downstream moves, but a nine-decade extrapolation of a
visibly drifting exponent must carry that fact. Figures from the round-2 skeptic, which reproduced
all four margins to every digit; not independently re-derived by the round-3 leg.)* That is a **correct warning about P6′-gov** and this leg does not soften it. It
**does not apply to P6′-min**: the P6′-min margin at its global minimum is `0.4845277`, and one
float64 ulp of `T = 1919.14` (which lies in `[1024, 2048)`) is `2⁻⁴² = 2.2737·10⁻¹³`, so the
margin stands `2.1·10¹²` ulps clear at the published frontier. (`faults.md` F10 is right that
`notebook-2`'s `4.269·10⁻¹³` is `eps·T`, i.e. about two ulps, not one; the correction moves
`notebook-2`'s crossover ratio from `1.04` to `≈1.96` and changes nothing qualitative.)

**Consequence 3 — *"the route to discharging P6′ must therefore be the analytic one"*.** This is
an inference from the mis-scoped premise and **does not survive it**, in the following exact
sense: no computation can *prove* any of these predicates, all of which are `Π₁`; but the claim
`notebook-2` actually makes is the sharper one that *"the computational route is running out of
resolution rather than accumulating confidence"*, and that is **false for P6′-min**, which is the
predicate Theorem 2 consumes. A float64 sweep of P6′-min at `2⁶⁴` would have twelve orders of
magnitude of headroom. **The reversal is recorded here as a cosmon-ward correction to `notebook-2`
§3's cosmon-ward observation, not applied quietly.**

### 5.2 What card **L15** must become

`L15` currently states P6′-pair in prose, measures P6′-gov in its table, and is marked **OPEN**.
After this leg:

| line | current | must become |
|---|---|---|
| "The claim" | P6′-pair, **OPEN** | **P6′-pair, FALSE** (§3, two witnesses), with the note that its refutation costs the run nothing |
| measurement row | "`T_{m(n)} ≤ T_n` for `m(n)` = governing record index — 0 exceptions in 216 815 pairs" | "**P6′-gov** — 0 exceptions in **216 794** admissible pairs at `3·10⁶`; margin decays `≈ p^{−0.83}` (`notebook-2` §3)" |
| "Why it is nevertheless very likely true" | dip statistics | must separate: the dip statistics measure `T`'s excursion below its own running maximum and bear on **P6′-rec**, not on P6′-gov or P6′-min |
| verdict | "the single most tractable open obligation" | **P6′-min *and* P6′-gov** stay on the obligation list — they are incomparable (Prop. 4) and Theorem 2 accepts either at `n₀`, so dropping `gov` is strictly lossy *(amended 2026-07-27, R2-M3)*; neither is a Dusart lookup (`proof-attempt-0.md` §7 and §8 below), and P6′-rec must be listed alongside them because Proposition 3 needs it |

---

## 6. The positive round-1 results, re-derived

These were audited clean by the skeptic (`faults.md` §5 item 1) and are restated because §7 and §8
consume them. They are re-derived here rather than quoted.

> **Lemma M (monotone-bar principle).** Let `B` be real-valued and **nondecreasing** in `p`. Call
> `k` a `B`-breach if `g_k ≥ B(p_k)`. If a `B`-breach exists, the least one, `k₀`, is a strict
> record index.
>
> *Proof.* Let `m < k₀`. Then `p_m < p_{k₀}`, so `B(p_m) ≤ B(p_{k₀})`. By minimality `m` is not a
> breach, so `g_m < B(p_m)`. Hence `g_m < B(p_m) ≤ B(p_{k₀}) ≤ g_{k₀}`. ∎

> **Lemma M′ (truncated form).** `B` nondecreasing, `1 ≤ N₁ ≤ N₂`. If (i) `g_m < B(p_m)` for every
> record index `m ∈ [N₁, N₂]`, and (ii) `max{ g_j : j < N₁ } < B(p_{N₁})`, then `g_k < B(p_k)` for
> every `k ∈ [N₁, N₂]`.
>
> *Proof.* Let `k₀` be least in `[N₁,N₂]` with `g_{k₀} ≥ B(p_{k₀})`, and `m < k₀`. If `m ≥ N₁`,
> minimality gives `g_m < B(p_m) ≤ B(p_{k₀}) ≤ g_{k₀}`. If `m < N₁`, (ii) and monotonicity give
> `g_m ≤ max{g_j : j < N₁} < B(p_{N₁}) ≤ B(p_{k₀}) ≤ g_{k₀}`. Either way `g_m < g_{k₀}`, so `k₀` is
> a record index in `[N₁,N₂]` breaching `B` — contradicting (i). ∎

> **Theorem A (record-scan completeness).** Immediate from Lemma M′.

With `S(x) := log²x − log x − 1.17` (card **L4**, Kourbatov's sufficient bar): `S` is strictly
increasing on `x > e^{1/2}` since `S′(x) = (2 log x − 1)/x`. Lemma M′(ii) at `N₁ = 10` is the
finite fact `max{g_j : j ≤ 9} = 6 < 6.80139 = S(29) = S(p_10)`, verified here. Theorem B then
follows exactly as in `proof-attempt-0.md` §4 — and its Axler input is now **L0** (§7.1), which
closes `faults.md` F3 for this subquestion. This leg's independent sieve confirms the `S`-breaches
below `10⁹` are exactly `k ∈ {1,2,3,4,6,9}`, all `≤ 9`, of which `k = 3` and `k = 6` are **not**
record indices — Lemma M's sharpness made concrete.

---

## 7. F2 repaired, and Axler opened

### 7.1 `axler2014newbounds` promoted to **L0** — and a provenance defect the run had not seen

Three documents fetched by this leg on 2026-07-26:

| document | URL | MD5 | what it is |
|---|---|---|---|
| Axler, arXiv:1409.1780**v3** (17 Mar 2015) | `https://arxiv.org/pdf/1409.1780v3` | `f4cde1df54cf3d6987c1ece2f7b0ebeb` | the preprint |
| Axler, *Integers* **16** (2016), A22, 15 pp. | `math.colgate.edu/~integers/cgi-bin/get.cgi` (`q22=pdf`) | `29a92c5e7cacb5269e4d7be68ac939bf` | the published paper |
| Corrigendum, dated 18 Jan 2018 | same endpoint (`q22=errata`) | `4817ba687df1c16d163c94e29b55d1c4` | the corrigendum |

**Finding A — the corollary numbering differs between the two editions, and the run's locators are
the preprint's while the corrigendum it cites is the journal's.**

| statement | arXiv v3 | *Integers* 16 (2016) A22 |
|---|---|---|
| upper bounds on `π(x)`, incl. `π(x) < x/(log x − 1 − 1.17/log x)` | **Corollary 3.5** | **Corollary 3.4** (p. 8) |
| lower-bound family `π(x) > x/(log x − 1 − 1/log x − a/log²x − …)` | **Corollary 3.6** | **Corollary 3.5** |

The corrigendum reads, verbatim and in full:

> *"In Corollary 3.4 on page 8, replace "If `x ≥ 5.43`" by "If `x ≥ 2 634 800 823`"."*

So it targets **Corollary 3.4**, i.e. the *published* numbering, while card **T1** and
`source-ledger.md` both cite the statement as **Corollary 3.5** and then attach the corrigendum to
it. **Both point at the same inequality, so no mathematical error propagated** — but the locator
as written matches no single edition, and card **T1** hazard 1's own lesson ("a validity range is
part of a bound") applies to edition numbering as well. The ledger row is amended in §7.5.

**Finding B — the exact bound `proof-attempt-0.md` §6.1 uses exists in the preprint only.** The
lower-bound corollary is a table of `(a,b,c,d,x₀)` rows. The instance the run consumes is
`(a,b,c,d) = (1,0,0,0)` with `x₀ = 1 772 201`:

```
π(x) > x/(log x − 1 − 1/log x − 1/log²x)   for  x ≥ 1 772 201 .
```

That column is present in arXiv v3's Corollary 3.6 (14 columns) and **absent from the published
Corollary 3.5** (12 columns; the published table also drops the `(2.65, 11.6, 0, 0)` /
`166 219 973` column). The published table's neighbours are `(2.1,0,0,0)` with `x₀ = 6 690 557` and
`(0,0,0,0)` with `x₀ = 468 049`.

**Consequence, stated as a defect and then repaired.** Round 1's Theorem C(b) — the run's headline
`0.99553` constant — rests on a bound whose *stated range* `x ≥ 1 772 201` appears only in the
preprint. Since the preprint is a legitimate L0 source that was read at the locator, the constant
is not wrong; but a paper that cites the *journal* version and quotes `x ≥ 1 772 201` would be
citing something the journal does not contain. §7.4 removes the exposure entirely by rebuilding the
theorem on the `(2.1, 0, 0, 0)` / `6 690 557` column, **which is present in both editions and is
strictly stronger**, and the resulting constant is *better*.

**Finding C — the pre-corrigendum range is not merely unproved, it is false, and this leg exhibits
that directly.** Testing `π(x) < x/(log x − 1 − 1.17/log x)` at `x = p_n` (so `π(x) = n` exactly)
over the primes below `10⁸`: **4 987 066 counterexamples**, the smallest at `p = 59 753`
(`n = 6041`) and the largest below `10⁸` at `p = 99 999 989`. Every one of them lies below the
corrigendum's `2 634 800 823`, so the corrected range is **not contradicted**. This independently
corroborates the corrigendum, and it independently corroborates
`proof-attempt-0.md` §9 item 10 (largest `n` with `T_n ≤ S(p_n)` below `3·10⁶` at `p = 2 875 681`
— reproduced here) as a *range* phenomenon rather than a defect.

**Finding D — the three bounds this subquestion consumes, all verified in-range.** Tested at
`x = p_n` over the primes below `10⁸`:

| bound | edition | range | failures |
|---|---|---|---|
| `π(x) > x/(ℓ − 1 − 1/ℓ − 1/ℓ²)` | arXiv v3 Cor. 3.6 only | `x ≥ 1 772 201` | **0** |
| `π(x) > x/(ℓ − 1 − 1/ℓ − 2.1/ℓ²)` | **both** (arXiv Cor. 3.6 / *Integers* Cor. 3.5) | `x ≥ 6 690 557` | **0** |
| `π(x) > x/(ℓ − 1 − 1/ℓ)` | **both** | `x ≥ 468 049` | **0** |

### 7.2 The bars, with F2's derivation error repaired

Write `x = p_n`, `ℓ = L_n`, `u = ℓ/π(x)`, so that `T_n = x(e^u − 1)` exactly (card **D3**:
`n = π(p_n)`). Two elementary facts:

> **Fact E1.** `x(e^{t/x} − 1) > t` for `t > 0`. *(From `e^s > 1 + s`.)*
>
> **Fact E2.** `x(e^{t/x} − 1) ≤ t(1 + t/x)` for `0 < t ≤ x`.
> *Proof.* `x(e^{t/x} − 1) = t + t·Σ_{k≥2} (t/x)^{k−1}/k!`, and for `0 < t/x ≤ 1` the sum is at most
> `Σ_{k≥2} 1/k! = e − 2 = 0.71828… < 1`. ∎

**(D-low)** `T_n > ℓ² − 1.1ℓ` for `x ≥ 60 184`. From Dusart Thm 6.9 eq. (6.6) (`dusart2010estimates`,
L0): `π(x) ≤ x/(ℓ − 1.1)`, so `u ≥ ℓ(ℓ − 1.1)/x`, and Fact E1 gives `T_n > ℓ(ℓ − 1.1)`. ∎

**(D-high)** `T_n ≤ v(1 + v/x)` with `v := ℓ² − ℓ`, for `x ≥ 5393`. From Dusart eq. (6.6):
`π(x) ≥ x/(ℓ − 1)`, so `u ≤ ℓ(ℓ − 1)/x = v/x`; Fact E2, whose side condition `0 < v ≤ x` holds
throughout (`v = 65.2` at `x = 5393`, and `ℓ² − ℓ ≤ x` for every `x ≥ 2`). ∎

**(A-low)** `T_n > ℓ² − ℓ − 1.17` for `x ≥ 2 634 800 823`. From Axler Cor. 3.4 (*Integers*) =
Cor. 3.5 (arXiv), **as corrected by the corrigendum**: `log x − 1 − 1.17/log x < x/π(x)`, so
`u = ℓ/π(x) > (ℓ² − ℓ − 1.17)/x`; Fact E1. **[Now L0 — §7.1.]** ∎

**(A-high′) — this is the F2 repair.** For `x ≥ 6 690 557`:

```
T_n  ≤  v(1 + v/x)        with  v := ℓ² − ℓ − 1 − 2.1/ℓ .
```

*Proof.* Axler Cor. 3.5 (*Integers*) = Cor. 3.6 (arXiv), row `(a,b,c,d) = (2.1,0,0,0)`,
`x₀ = 6 690 557` — **present in both editions**: `π(x) > x/(ℓ − 1 − 1/ℓ − 2.1/ℓ²)`. Hence
`u = ℓ/π(x) < ℓ(ℓ − 1 − 1/ℓ − 2.1/ℓ²)/x = (ℓ² − ℓ − 1 − 2.1/ℓ)/x = v/x`, and `v ≤ x` throughout the range
(`v = 230.1` at `x = 6 690 557`), so Fact E2 applies. ∎

> **What was wrong in round 1, precisely.** `proof-attempt-0.md` §6.1 states
> `(A-high): T_n ≤ (ℓ² − ℓ − 1 − 1/ℓ)(1 + ℓ⁴/x)`, justified as "`T_n ≤ v(1 + v/x) ≤ v(1 + ℓ⁴/x)`
> using `v < ℓ²`". The step `v(1 + v/x) ≤ v(1 + ℓ⁴/x)` requires `v ≤ ℓ⁴`, which is true, but the
> resulting bound is weaker by an additive `v(ℓ⁴ − v)/x ≈ ℓ⁶/x`, not the `v²/x` the algebra of
> §6.2 silently assumes. `faults.md` F2(b) quantifies the damage and this leg reproduces it to
> every digit: under the printed lemma the required separation at `ℓ₁ = 14.3877` is `0.169340`
> (not `0.004479`), at `ℓ = 16` it is `0.060196`, at `ℓ = 18` it is `0.017191`, at `ℓ = 20` it is
> `0.006280`, and it only meets the printed constant at `ℓ ≈ 44.36`. The repair is **not** to
> re-insert `ℓ⁴` correctly — it is to keep `v²/x` and never introduce `ℓ⁴` at all, which is what
> (A-high′) does.

### 7.3 Lemma W (sandwich) — unchanged

> **Lemma W.** Suppose `A(x) ≤ T_n ≤ C(x)` at `x = p_n` for all `n` with `p_n ≥ X₀`. Let `n₀` be
> the least failure of `F`. Then for every `m < n₀` with `p_m ≥ X₀` and `C(p_m) ≤ A(p_{n₀})`, one
> has `g_m < g_{n₀}`.
>
> *Proof.* `T_m ≤ C(p_m) ≤ A(p_{n₀}) ≤ T_{n₀}`. Since `m < n₀` and `n₀` is least,
> `g_m < T_m ≤ T_{n₀} ≤ g_{n₀}`. ∎
>
> No monotonicity of `A` or `C` is used. Monotonicity re-enters only when `C(p_m) ≤ A(p_{n₀})` is
> converted into a uniform separation.

### 7.4 Theorem C, round-2 form

Throughout: `n₀` is the least failure of `F`; by card **L6**, `p_{n₀} > 2⁶⁴`, so
`λ := L_{n₀} > log 2⁶⁴ = 44.3614195…` and, by (D-low),

```
T_{n₀}  >  λ² − 1.1λ  >  1919.1379834…   and hence   g_{n₀} ≥ T_{n₀} > 1919 .
```

*(`λ = 44.3614195558…` and `1919.1379834975…`; the latter is `notebook-2` §1.6's constant,
reproduced.)*

> **Theorem C-a′ (Dusart-only *analytics*; the finite branch consumes card `L6` and an in-run
> gap sieve).** *(Header corrected 2026-07-27, round-3 reconciliation, `faults.md` R2-M2. The
> header formerly read "no source outside `dusart2010estimates`, L0", which is false of the small
> branch: it consumes `g_{n₀} > 1919`, i.e. `p_{n₀} > 2⁶⁴` — card **L6**, tier **L2_weak, NOT
> OPENED** — and the in-run fact `max{g_m : p_m < 10⁸} = 220`. The **analytics** are Dusart-only
> and L0; the theorem is not "unconditional" in the citation sense. Its honest label:
> **unconditional given the published `2⁶⁴` verification height (L6) and a finite in-run gap
> computation** — both named inputs, neither an analytic hypothesis. Note the improvement from
> round 1's `0.93961` comes **entirely** from raising the small-branch cutoff to `10⁸`, so the `L6`
> dependence is the source of the headline, not incidental to it. UVR §4.4 builds the correct
> "what may be called unconditional" table; read it alongside this header.)*
> Let `m < n₀`. If `p_m ≤ p_{n₀}·e^{−0.0516}`, i.e. `p_m ≤ 0.94970·p_{n₀}`, then `g_m < g_{n₀}`.
>
> *Proof.* **Small branch.** If `p_m < 10⁸` then `g_m ≤ 220` (the largest prime gap below `10⁸`,
> attained at `p = 47 326 693`; computed in-run, §9) and `220 < 1919 < g_{n₀}`.
>
> **Main branch.** Let `p_m ≥ 10⁸`, so `ℓ := L_m ≥ ℓ_D := log 10⁸ = 18.4206807…` and both
> (D-high) at `m` (needs `p_m ≥ 5393` ✓) and (D-low) at `n₀` (needs `p_{n₀} ≥ 60 184` ✓) apply.
> Put `d := λ − ℓ ≥ 0` and `v := ℓ² − ℓ`, `ε := v²/p_m`. By Lemma W it suffices that
> `v(1 + v/p_m) ≤ λ² − 1.1λ`. Expanding `λ = ℓ + d`:
> ```
> λ² − 1.1λ − v  =  2ℓd + d² − 1.1d − 0.1ℓ ,
> ```
> so it suffices that `2ℓd + d² − 1.1d ≥ 0.1ℓ + ε`, for which `d(2ℓ − 1.1) ≥ 0.1ℓ + ε` suffices,
> i.e. `d ≥ d*(ℓ) := (0.1ℓ + ε)/(2ℓ − 1.1)`.
>
> Since `p_m = e^ℓ`, `ε(ℓ) = (ℓ² − ℓ)² e^{−ℓ} ≤ ℓ⁴ e^{−ℓ}`, and `ℓ ↦ ℓ⁴e^{−ℓ}` is decreasing for
> `ℓ > 4`. Partition `[ℓ_D, ∞)`. On any cell `[a,b]`, `0.1ℓ ≤ 0.1b`, `ℓ⁴e^{−ℓ} ≤ a⁴e^{−a}` and
> `1/(2ℓ − 1.1) ≤ 1/(2a − 1.1)`, so
> ```
> sup_{[a,b]} d*(ℓ)  ≤  (0.1b + a⁴e^{−a}) / (2a − 1.1) .
> ```
> This is a **majorant, not a sample**, so the maximum over a partition is a proof. Over
> `[ℓ_D, 1000]` in cells of width `0.01` the majorant is largest on the first cell, where it equals
> **`0.051599027`**. For `ℓ ≥ 1000`: `0.1ℓ/(2ℓ − 1.1)` is decreasing in `ℓ` with limit `0.05`, so
> the majorant there is at most `(100 + 1000⁴e^{−1000})/1998.9 = 0.050028`. Hence
> `d* ≤ 0.051599 < 0.0516` throughout, and `d ≥ 0.0516` suffices. Finally
> `e^{−0.0516} = 0.94970867…`. ∎

> **Theorem C-b′ (with Axler, now L0, and edition-independent).**
> Let `m < n₀`. If `p_m ≤ p_{n₀}·e^{−0.0017569}`, i.e. `p_m ≤ 0.998244·p_{n₀}`, then
> `g_m < g_{n₀}`.
>
> *Proof.* **Small branch.** If `p_m < 6 690 557` then `g_m ≤ 154` (largest prime gap below
> `6 690 557`, attained at `p = 4 652 353`; computed in-run, §9) and `154 < 1919 < g_{n₀}`.
>
> **Main branch.** Let `p_m ≥ 6 690 557`, so `ℓ := L_m ≥ ℓ_A := log 6 690 557 = 15.7162077…`, and
> (A-high′) applies at `m`. (A-low) applies at `n₀` because `p_{n₀} > 2⁶⁴ > 2 634 800 823`. With
> `v := ℓ² − ℓ − 1 − 2.1/ℓ` and `λ = ℓ + d`, Lemma W's hypothesis `v(1 + v/p_m) ≤ λ² − λ − 1.17`
> expands to
> ```
> d(2ℓ − 1) + d²  ≥  0.17 − 2.1/ℓ + v²/p_m  =:  ψ(ℓ) ,
> ```
> so `d ≥ ψ(ℓ)/(2ℓ − 1)` suffices (and `d = 0` suffices wherever `ψ(ℓ) ≤ 0`). As before
> `v²/p_m ≤ ℓ⁴e^{−ℓ}`, decreasing; `0.17 − 2.1/ℓ` is increasing; `1/(2ℓ − 1)` is decreasing. So on a
> cell `[a,b]`,
> ```
> sup_{[a,b]} ψ(ℓ)/(2ℓ−1)  ≤  (0.17 − 2.1/b + a⁴e^{−a}) / (2a − 1) .
> ```
> Over `[ℓ_A, 300]` in cells of width `0.01` this majorant is largest on the cell starting at
> `ℓ = 24.40621`, where it equals **`0.0017568759`**. For `ℓ ≥ 300` it is at most
> `(0.17 + 300⁴e^{−300})/599 = 0.00028381`. Hence `d ≥ 0.0017569` suffices, and
> `e^{−0.0017569} = 0.9982446424…` *(printed `0.99824467…` before 2026-07-27; corrected per
> `attack/synthesis.md` §5.6 item 1 — the headline `0.998244` is unaffected)*. ∎
>
> ⚠ **Certification margin, recorded 2026-07-27 (`faults.md` R2-m3).** The certified constant
> `0.0017569` clears its own majorant `0.00175687590387` by **`2.4·10⁻⁸`** — `≈ 1.4·10⁻⁵` in
> relative terms. At 50 dps this is safe and both the round-2 skeptic and this leg confirm it, but
> **these checks are 50-digit floating point, not interval arithmetic** (UVR §9 G6 records the same
> limitation for its own constants; this document carried no counterpart). Any Lean leg discharging
> `M-7`/`M-8` by `norm_num` on the quadratic **without directed rounding** has far less headroom
> here than elsewhere in the corpus. Carry the margin next to the constant.

**Comparison with round 1** — every constant recomputed by this leg, `mpmath` at 40–50 digits:

| branch | round 1 (`proof-attempt-0.md`) | round 2 | source tier |
|---|---|---|---|
| Dusart only | `d ≥ 0.0623` → `p_m ≤ 0.93961 p_{n₀}` | **`d ≥ 0.0516` → `p_m ≤ 0.94970 p_{n₀}`** | L0 both rounds |
| with Axler | `d ≥ 0.004479` → `p_m ≤ 0.99553 p_{n₀}`, from a lemma that does not support it | **`d ≥ 0.0017569` → `p_m ≤ 0.998244 p_{n₀}`** | round 1: L2_strong, unopened, arXiv-only column. **round 2: L0, both editions** |

> ✅ **DESIGNATED — round-3 reconciliation leg, decision 1, 2026-07-27.** Round 2 shipped two
> incompatible repairs of round-1 F2: **Theorem C-b′** here (`d ≥ 0.0017569`, `0.998244·p_{n₀}`,
> Axler row `(2.1,0,0,0) / x₀ = 6 690 557`) and **Theorem C(b\*)** in
> `proof-attempt-unconditional-verified-range.md` §3.5 (`d ≥ 0.0043636`, `0.99565·p_{n₀}`, row
> `(1,0,0,0) / x₀ = 1 772 201`). Both are mathematically correct — verified independently at 40–50
> dps by the round-2 skeptic. **Theorem C-b′ is the designated carry-forward form**, on the ground
> that decides it and is not a matter of taste: its Axler row is present in **both** the arXiv
> preprint and *Integers* **16** (2016) A22, whereas `1 772 201` is **absent from the journal**
> (`faults.md` R2-B3, confirmed twice by independent PDF fetch with matching MD5s, and recorded on
> the `axler2014newbounds` ledger row as a standing downstream rule). C-b′ is additionally the
> sharper statement. **Theorem C(b\*) is retired to a remark** — see UVR §3.5, amended in place.
> The three constants that circulated for one theorem name resolve to one: `0.998244`. Round 1's
> `0.99553` and UVR's `0.99565` are **retired** and may appear only as history. See
> `attack/reconciliation.md` §1.

The Dusart branch improves only because the small-branch cutoff is raised from `60 184` to `10⁸`
(licensed by `g_m ≤ 220 < 1919`, which needs `p_{n₀} > 2⁶⁴` — card **L6** — and nothing else). It
cannot improve much further: `d*(ℓ) → 0.05` as `ℓ → ∞`, so the Dusart-only sliver is pinned near
`5 %` at every scale.

Three sanity anchors, all reproduced by this leg and reported so the repair is not overstated:
the *exact* required separations (solving the quadratic rather than majorising) are
`0.051493457` (Dusart, `ℓ ≥ ℓ_D`) and `0.0017560603` (Axler, `ℓ ≥ ℓ_A`) — both **below** the
constants proved above, as a majorant must be; and under round 1's tight-form reading the Axler
`a = 1` maximum is `0.0043628824`, exactly `faults.md` F2's `0.0043629`.

**Reading of Theorem C, round 2.** *If Firoozbakht first fails at `n₀`, then `g_{n₀}` exceeds
every gap between primes below `0.94970·p_{n₀}` — unconditionally, on Dusart alone — and below
`0.998244·p_{n₀}` on Axler, whose corollaries this run has now read at the locator in both
editions. The residual sliver has relative width `0.176 %` at `2⁶⁴`.*

### 7.5 Ledger amendment (bounded, one row)

`attack/source-ledger.md`'s `axler2014newbounds` row is amended in place: tier **L2_strong →
L0**, with the fetch record of §7.1, the edition-numbering finding, and the note that the
`(1,0,0,0)/1 772 201` column is preprint-only. `attack/concept-cards/T1-effective-pi-bounds.md`
hazard 2 is amended correspondingly. **No other ledger row was reopened** — this is the bounded
refresh the brief authorises and nothing more.

> ✅ **VERIFIED LANDED — round-3 reconciliation leg (`task-20260727-264e`), decision 3, 2026-07-27.**
> `faults.md` **R2-B2** reported this amendment as *"never made"*. That finding is **STALE**, and
> the reconciliation leg checked the tracked tree rather than either report:
> `attack/source-ledger.md` line 412 reads *"tier **L0** (promoted from L2_strong on 2026-07-26 by
> the re-attack leg `task-20260726-56a7`)"*, carries the three MD5s, the edition-numbering table,
> and the ⚠ on the preprint-only `(1,0,0,0)/1 772 201` row with the downstream rule *"do not quote
> `x ≥ 1 772 201` against the journal citation"*; §6 gap 3 reads *"~~Axler was not opened~~ —
> **CLOSED 2026-07-26**"*; `attack/concept-cards/T1-effective-pi-bounds.md` lines 4–5 and 17–24
> carry the same promotion, both editions' numbering, and the same ⚠. The skeptic's line numbers
> (`406`, `642`) resolve only in the pre-merge tree — it read a worktree branched before commit
> `61689d0`. §11 items 8 and 9 are therefore **accurate as written**. What did *not* land, and what
> the reconciliation leg has now landed, is the propagation of the new tier into the **sibling
> leg's** document (`proof-attempt-unconditional-verified-range.md`) — R2-B2 limb 2. See
> `attack/reconciliation.md` §2–§3.

---

## 8. The obstruction — unchanged, and what Theorem 1 adds to it

`proof-attempt-0.md` §7 isolates the obstruction and this leg does not move it. Restated:

Inside the residual window `p_m ∈ (p_{n₀}e^{−d*}, p_{n₀})` the sandwich is useless by construction.
Attacking `T_m ≤ T_n` directly, the exact first-order criterion is

> `T_m ≤ T_n` holds exactly when the interval `(p_m, p_n]` contains at most `≈ y/(L − 2)` primes,
> `y := p_n − p_m` — i.e. when the average gap over the block is at least about `L − 2`.

What is required is an **upper** bound on `π(p_m + y) − π(p_m)` within a factor `1 + 2/L` of the
truth, for `y ≍ x/log x`. What is available unconditionally is Brun–Titchmarsh, `≤ 2y/log y` —
short by a factor `2.23` at `2⁶⁴`, `2.06` at `L = 200`. Narrowing the sandwich instead requires an
absolute accuracy in `T_n` of order `x^{−1+o(1)}`, i.e. a two-sided `π(x)` estimate accurate to
`O(1)` primes, far beyond RH. Both routes are the same wall.

**What Theorem 1 adds.** The refutation of P6′-pair is a *hard* obstruction, not an
effective-constants one, and it is visible far below `2⁶⁴`:

- Any proof strategy that proceeds by establishing `T_m ≤ T_n` for **all** record-straddling pairs
  is now dead, not merely unproved. W1 kills it at `p ≈ 15 800`.
- The surviving predicates are exactly the ones that pin `m` to a *specific* index determined by
  `n` (`r(n)` or `µ(n)`). So any successful argument must be **index-selective**, not
  pair-uniform, and this is a structural constraint the run did not have.
- W2 sits at `p ≈ 1.919·10⁸`, which is precisely the index where the P6′-gov margin attains its
  `10⁹`-range minimum (`n = 10 655 590`, margin `1.120382·10⁻⁴`). The same configuration — a few
  indices after a large record gap, in a locally prime-rich stretch — is simultaneously the
  tightest case for P6′-gov and an outright violation for P6′-pair. **The two facts are one fact
  seen at two strengths**, and that is the cleanest available statement of where the difficulty of
  this subquestion actually lives.

**Heuristic calibration, quarantined.** `[HEURISTIC. Rests on cards L9/L10, statements about the
Cramér model, not about the primes. Not evidence about `F` or about (M1).]` Under the Cramér model
the residual window of Theorem C-b′ is expected to contain `≈ 0.231/L²` competing indices —
`1.2·10⁻⁴` at `L = 44.36` — so (M1) is heuristically true and the unproved part is the part the
model says almost never happens. **This does not license writing "(M1) holds"**: the same model
predicts `limsup g_n/log²p_n ≥ 2e^{−γ} > 1` (**L10**), which is incompatible with `F` itself
(**L3**), so the model is known to disagree with something this run cares about. Using it here and
refusing it there would be selective.

---

## 9. Verification performed by this leg

Sieve of Eratosthenes to `10⁹` (`π(10⁹) = 50 847 534`, the standard value), 1-indexed, plus
independent runs at `3·10⁶`, `10⁷`, `10⁸`, `2·10⁸`. High-precision arithmetic in `mpmath` at 50–60
decimal digits. Scripts: `r2_pred.py`, `r2_axler.py`, `r2_final.py`, `r2_const.py`, in this
directory. **Every number in this document is produced by one of them; nothing is
quoted from an upstream artifact without being recomputed here.**

| # | Check | Result |
|---|---|---|
| 1 | Failures of `F`, `p < 10⁹` | **none** |
| 2 | Maximal-gap record indices | 21 (`3·10⁶`), 22 (`10⁷`), 25 (`10⁸`), **30** (`10⁹`); largest gap `282` at `p = 436 273 009` |
| 3 | **P6′-pair exception *indices***, `p < 10⁹` | **17** indices in `50 847 533` swept indices (**20** violating `(m,n)` pairs below `3·10⁸`); min margin `−2.861060·10⁻²` at `n = 1847`. *Index count, not a pair count — amended 2026-07-27, R2-m2.* |
| 4 | P6′-pair witnesses at 60 dps | W1 `T_m − T_n = 0.028610605`; W2 `T_m − T_n = 3.5792097·10⁻⁵` |
| 5 | **P6′-gov exceptions**, `p < 10⁹` | **0** in `50 847 533` indices *(was `50 847 503` — transposition, corrected 2026-07-27; `π(10⁹) = 50 847 534`, hence `50 847 533` steps)* |
| 6 | P6′-gov min margin | `+1.046415·10⁻²` (`3·10⁶`), `+6.060476·10⁻³` (`10⁷`), `+1.111812·10⁻³` (`10⁸`), `+1.120382·10⁻⁴` (`10⁹`) — reproduces `notebook-2` §3 to every digit quoted |
| 7 | **P6′-min exceptions**, `p < 10⁹` | **0** in `50 847 533` indices *(was `50 847 503` — same transposition, corrected 2026-07-27)* |
| 8 | P6′-min min margin | `+0.4845277` at `n = 1879`, `p = 16 141`, `µ = 1831`, `p_µ = 15 683` — **identical at `3·10⁶`, `10⁷`, `10⁸`, `10⁹`**; reproduces `notebook-0` finding 3 |
| 9 | **P6′-rec exceptions** (`T` decreasing between consecutive records) | **0** in 29 record steps |
| 10 | `T_{µ(n)} ≤ T_{r(n)}` (Proposition 3's hypothesis, pointwise) | **0** exceptions in `50 847 533` indices |
| 11 | `T_{n+1} < T_n`, `n ≥ 10` | `121 238/216 806` = 55.9200 % (`3·10⁶`); `374 485/664 569` = 56.3501 % (`10⁷`); `3 280 063/5 761 445` = 56.9313 % (`10⁸`) — **denominators corrected 2026-07-27, §4 and `attack/reconciliation.md` §4** |
| 12 | `S`-breaches (`g_k ≥ L² − L − 1.17`), `p < 10⁹` | exactly `k ∈ {1,2,3,4,6,9}`; none with `k > 9`; `k = 3, 6` are not records |
| 13 | Lemma M′(ii) at `N₁ = 10` | `max{g_j : j ≤ 9} = 6 < S(29) = 6.80139` ✓ |
| 14 | Largest `n` with `T_n ≤ L² − L − 1.17` | `n = 208 494`, `p = 2 875 681` at `3·10⁶` — below Axler's corrected range, so (A-low) is not contradicted (reproduces `proof-attempt-0.md` §9 item 10) |
| 15 | (D-low) failures for `p ≥ 60 184` / (D-high) for `p ≥ 5393`, `p < 10⁸` | **0** / **0** |
| 16 | **(A-high′)** tight form, failures for `p ≥ 6 690 557`, `p < 10⁸` | **0** |
| 17 | Axler Cor. 3.4 (published) last clause at the **pre**-corrigendum range `x ≥ 5.43` | **4 987 066 counterexamples** below `10⁸`, smallest at `p = 59 753`; all below `2 634 800 823` |
| 18 | Axler lower-bound rows `(1,0,0,0)/1 772 201`, `(2.1,0,0,0)/6 690 557`, `(0,0,0,0)/468 049` | **0** failures each, `p < 10⁸` |
| 19 | Largest prime gap below `468 049` / `6 690 557` / `10⁸` / `10⁹` | `112` / `154` / `220` / `282` (at `p = 370 261` / `4 652 353` / `47 326 693` / `436 273 009`) |
| 20 | Theorem C-a′ majorant over `[log 10⁸, 1000]`, cells of `0.01`, + analytic tail | `0.051599027` (cell at `ℓ_D`); tail `0.050028` |
| 21 | Theorem C-b′ majorant over `[log 6 690 557, 300]`, cells of `0.01`, + tail | `0.0017568759` (cell at `ℓ = 24.40621`); tail `0.00028381` |
| 22 | Exact required separations (quadratic solved, no majorant) | Dusart `0.051493457`; Axler `a=2.1` `0.0017560603`; Axler `a=1` `0.0043628824` (= `faults.md` F2's `0.0043629`) |
| 23 | `λ² − 1.1λ` at `p = 2⁶⁴` | `1919.137983…` (reproduces `notebook-2` §1.6) |
| 24 | Round-1 printed-`(A-high)` required separations | `0.1693398` (`ℓ₁`), `0.06019567` (16), `0.01719111` (18), `0.006280319` (20), `0.001680966` (44.36) — reproduces `faults.md` F2(b) to every digit |

**Scale disclaimer, restated because it is easy to lose.** `10⁹` is **9.3 orders of magnitude**
below the published frontier `2⁶⁴` (card **L6**), and `notebook-0`/`notebook-2` reach `10¹¹`, still
`8.3` decades short. Items 1–19 are probes on *statements*; they are **not** verification of `F`
and are cited as such nowhere. Items 20–24 evaluate closed-form expressions and carry no range
limitation. Every hypothesis in §7.4 begins above `10⁶` and the small-branch facts (item 19) are
the only in-sieve inputs the theorems consume.

**One check that could not be run.** Neither Theorem C branch can be exercised at `n₀`, because no
`n₀` is known to exist. Items 14–18 are the closest available: they confirm each bar fails *only
below* its stated range. That is consistency, not confirmation.

---

## 10. Declared gaps

Stated so nothing downstream mistakes silence for coverage.

1. **(M1) is not proved.** Theorem C-b′ proves it outside a sliver of relative width
   `0.176 %`; the sliver is not closed, and `proof-attempt-0.md` §7.3 argues it cannot be closed by
   sharper effective constants. This leg agrees and adds §8's structural reason.
2. **P6′-gov, P6′-min and P6′-rec are all unproved.** Only P6′-pair has been settled, and settled
   *negatively*. Theorem 2 shows either of the first two would suffice for (M1); neither is proved
   here and this leg did not attempt an analytic proof of either — §8 explains why it would meet
   the same wall.
3. **Proposition 3's use of P6′-rec is not discharged.** `faults.md` F1's chain "(A) ⟹ (B)" is
   corrected here to "(A) ∧ (rec) ⟹ (B)", and P6′-rec is a *new named obligation* that no leg has
   proved. Its empirical base is thin by count — **29 record steps below `10⁹`** — even though it
   has zero exceptions. A statement with 29 data points should not be described as robust.
4. **Theorem 1 is a refutation of a lemma, not of the conjecture.** It says nothing about `F` and
   nothing about (M1). Any downstream text that lets "P6′ is false" drift toward "the conjecture is
   in trouble" would be a fabrication.
5. **Theorem 1's witnesses are exhaustive only below `10⁹`.** The 17-exception census is this
   leg's range; there is no claim that the clusters are the only ones.
6. **Brun–Titchmarsh and the second Hardy–Littlewood conjecture remain unsourced in this run.**
   Both are used only to *name* the obstruction (§8), never to support a positive claim. They stay
   on the citation gate's list, as `proof-attempt-0.md` §10.3 already recorded.
7. **`oliveira2014goldbach` remains unopened**, so `p_{n₀} > 2⁶⁴` (card **L6**) is still mediated
   through Kourbatov. Theorem C uses it only to make `T_{n₀} > 1919` available for the small
   branches; if the frontier were smaller, the constants `154` and `220` would need re-checking
   against a smaller `T_{n₀}`. *(This is `faults.md` F13, now recomputed for the round-2 cutoffs.)*
8. **The first-order criterion in §8 is quoted from round 1 and was not re-verified here** at the
   `19 980/19 980` level. Nothing in §1–§7 depends on it; it is diagnosis, not proof.
9. **No Lean was written.** §11 records what should be formalised. Card **D1**'s off-by-one
   correction (Mathlib's `Nat.nth` is 0-indexed) is **not** applied in this document, which is
   uniformly 1-indexed. Every threshold — `N₁ = 10`, `k > 9`, `µ`, `r` — must be re-indexed on
   transcription.
10. **The Axler promotion covers one row only.** Ribenboim, Oliveira e Silva–Herzog–Pardi,
    Granville's pagination, Dusart 2018 and Farhadian–Jakimczuk are untouched and remain exactly as
    `source-ledger.md` §6 leaves them.

---

## 11. What this changes upstream

| # | Upstream statement | Correction |
|---|---|---|
| 1 | Card **L15** "The claim": P6′-pair, **OPEN**, *"empirically unviolated by every measurement that bears on it"* | **FALSE.** §3, two witnesses at 60 dps, 17 exceptions below `10⁹`. The measurement that bears on the card's own prose had never been run. |
| 2 | `proof-attempt-0.md` §1 (M3), and its chain "(M3) ⟹ (M1) ⟹ (M2)" | (M3) is P6′-pair and is **refuted**; the chain now runs from a false premise. Replace with Theorem 2: **P6′-gov at `n₀`, or P6′-min at `n₀`, each implies (M1)**. |
| 3 | `faults.md` F1: *"(C) ⟹ (A) ⟹ (B) as obligations"* | First link correct (Proposition 2). **Second link is not valid**: it needs P6′-rec (Propositions 3–4, with counter-models). F1's repair instruction is otherwise adopted verbatim and is what §1 and §5 implement. |
| 4 | `notebook-2` §3 consequence 3 (a *cosmon-ward observation*): *"the computational route is running out of resolution"* | **True of P6′-gov, false of P6′-min**, which is the predicate Theorem 2 consumes and whose margin is flat at `0.4845277` across seven decades — `2.1·10¹²` float64 ulps clear at `2⁶⁴`. Recorded here as a cosmon-ward correction, not applied quietly. |
| 5 | `notebook-0` §2 finding 3 vs `notebook-2` §3 — the two headlines `faults.md` F1 says cannot be reconciled | **Reconciled without retracting either.** Different predicates (§5 table); both reproduced here to every digit quoted, from an independent code path. |
| 6 | `proof-attempt-0.md` §6.1 (A-high) and §6.2's constant `0.004479` | Lemma restated as (A-high′) with `v²/x` and the `(2.1,0,0,0)` Axler row; constant replaced by **`0.0017569`**, which is both rigorous and sharper. *(`faults.md` F2.)* |
| 7 | `proof-attempt-0.md` §2 verdict row: *"the search-pruning … DISCHARGED unconditionally by Thm A + Thm B"*, and §11 correction 1's directive to **retire** P6′ | The "unconditional" label is now **earned** for the Axler input (opened to L0, §7.1) — but the directive to retire P6′ is still wrong, for a new reason: Theorem A/B discharge the pruning **against the surrogate bar `S`**, not against the exact bar `T`. A search pruned against `T` still consumes P6′-min. Retire *P6′-pair* (it is false); keep *P6′-min* and add *P6′-rec*. |
| 8 | Card **T1** hazard 2 (*"the Axler corollaries were never opened"*, Priority 1 for the citation gate) | **Discharged.** Both editions and the corrigendum read at the locators. Replaced by a new hazard: **the corollary numbering differs between the preprint and the journal, and the corrigendum uses the journal's** (§7.1 Finding A). |
| 9 | `source-ledger.md` §6 gap 3 / §7 priority 1 (`axler2014newbounds`) | **Closed**, tier `L2_strong → L0`, with the preprint-only-column finding (§7.1 Finding B) recorded on the row. |
| 10 | `proof-attempt-0.md` §9 item 7 (`T_n < T_{m(n)}`, inequality reversed — `faults.md` F7) | Corrected row: **`T_{r(n)} ≤ T_n`, 0 exceptions in `216 794` admissible pairs at `3·10⁶`** (`216 815` minus the 21 trivial self-pairs). |
| 11 | Card **T5**(d): *"if L15 were discharged this would become a proof that `n₀` is a record index"* | L15-as-stated cannot be discharged. Restate as: *`n₀` is a record among primes below `0.94970·p_{n₀}` (unconditional, Dusart); below `0.998244·p_{n₀}` (Axler, L0); the residual is open, and either P6′-gov or P6′-min at `n₀` would close it.* |

---

## 12. Notes for the Lean legs

`lean/Firoozbakht/Statement.lean` is **frozen** and was not touched. The nodes below are additions
in the spirit of `proof-attempt-0.md` §12, re-scoped by this leg's results. All are order theory —
no number-theoretic input, no `Real` analysis beyond the bar's codomain.

| Node | Content | Effort | Depends on |
|---|---|---|---|
| **M-1** | Lemma M: `Monotone B → IsLeast {k | B (p k) ≤ g k} k₀ → ∀ m < k₀, g m < g k₀` | low | `D1` (fixed indexing) |
| **M-2** | Lemma M′ (truncated, with the `N₁` side condition) | low | M-1 |
| **M-3** | `S x = log²x − log x − 1.17` is `Monotone` for `x ≥ 2` | low | Mathlib `Real.log` |
| **M-4** | Theorem A (record-scan completeness) | low | M-2, M-3 |
| **N-1** | `def govIdx`, `def minDomIdx`; **Fact 0** (`minDomIdx n` is a record and `≤ govIdx n`) | low | `D1` |
| **N-2** | **Theorem 2**, P6′-min branch — the cleanest of the two, five rewrites | **low** | N-1 |
| **N-3** | **Theorem 2**, P6′-gov branch | low | N-1 |
| **N-4** | **Proposition 4**, the counter-models — `decide` on a four-element gap list with an explicit `T` | **low**, and it is the *most valuable* node: it machine-checks that `P6′-gov ⟹ P6′-min` is **not** a formal consequence, which is a claim a reader will otherwise take on trust | — |
| **N-5** | **Theorem 1** as a `Refuted`-style witness statement: `∃ m j n, m < j ∧ j < n ∧ IsRecord j ∧ T n < T m` | medium — needs `p 1823`, `p 1831`, `p 1847` as numerals, which card **T4** Fact 1 flags as the standing obstacle (`Nat.nth` is `noncomputable` with only five `@[simp]` base lemmas). **Do not report this node as done without the `Nat.count`↔`Nat.nth` bridge**; asserting the prime values would be a fabrication of exactly the kind `lean-probe-report.md` was built to prevent | T4 bridge |
| **M-7/M-8** | Lemma W, and Theorem C-a′'s arithmetic (`d = 0.0516`) | medium — `norm_num` on the quadratic; the `ε` bookkeeping is the fiddly part | M-7 + Dusart as hypotheses |

**N-2 and N-4 are the recommended first deliverables.** They are order theory over a `List ℕ`,
they are *used* by everything above, and N-4 in particular converts a claim about what does **not**
follow into a kernel-checked fact — the one shape a paper argument is worst at.

**The indexing hazard is acute.** Every threshold here is 1-indexed. Under Mathlib's 0-indexed
`Nat.nth Nat.Prime` all of `N₁ = 10`, `k > 9`, `p ≥ 29`, and the witness indices `1823/1831/1847`
shift by one. See cards **D1**, **T4**, and `lean-probe-report.md`'s fidelity-anchor discipline.

---

## 13. Standing instruction, restated

The conjecture is **OPEN**. Nothing above asserts `F`, nothing above asserts `¬F`, and nothing
above asserts (M1). `Firoozbakht.firoozbakht` remains the single `sorry` in the Lean development,
and `Statement.lean` was not modified.

The defensible sentences produced by this leg:

> *The maximal-gap reduction, in the pair-uniform form in which it has been stated — "for `m < n`
> whose primes straddle a record gap, `T_m ≤ T_n`" — is **false**, with the least witness at
> `p_m = 15 641`, record gap 44 at `p = 15 683`, `p_n = 15 823`, and a second at
> `p_m = 191 912 639`. Two strictly weaker index-selective forms survive `5·10⁷` indices, and
> either one, at the first failure alone, implies that the first failure carries a record gap.*

> *If Firoozbakht's conjecture fails, its first failure occurs at a gap larger than every gap
> between primes below `0.94970·p_{n₀}` — on Dusart's L0 analytics, given the published `2⁶⁴`
> verification height (card `L6`, L2_weak, unopened) and a finite in-run gap computation — and below
> `0.998244·p_{n₀}` on Axler's
> effective `π(x)` corollaries — now read at the locator in both the preprint and the journal, and
> in a form present in both. Whether the first failure is a record outright is open, and closing it
> requires a short-interval prime count beyond Brun–Titchmarsh.*

---

*Artifact of the re-attack leg on subquestion `first-failure-maximality`, molecule
`task-20260726-56a7`, re-attack root `reattack-20260726-57d1`. Verification scripts:
`r2_pred.py`, `r2_axler.py`, `r2_final.py`, `r2_const.py`, in this directory.
**The conjecture remains OPEN.***
