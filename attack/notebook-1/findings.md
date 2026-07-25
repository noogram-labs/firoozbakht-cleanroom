# Findings — notebook-1, target `RH-conditional-bound`

**Molecule:** `task-20260725-c885` (leg `notebooks__1`, crew role: coder)
**Run:** `germ-20260725-791a7c45`
**Artifact:** `notebook-1.ipynb` (executed, all outputs stored), `figure-1-rh-vs-bar.png`,
`summary.json`
**Status of the conjecture in this document:** **OPEN.** Nothing below assumes F true or false.

---

## 0. What was asked, and what a notebook is allowed to conclude

The target is `RH-conditional-bound` — the claim carried by `decompose` §2.1 (P3b) and §3.2 (S2),
and by card `L11`, that assuming the Riemann Hypothesis does **not** deliver the prime-gap bound
Firoozbakht requires.

Firoozbakht's conjecture, in the three forms used throughout:

```
F :  p_{n+1}^{1/(n+1)} < p_n^{1/n}   ⟺   p_{n+1}^n < p_n^{n+1}   ⟺   g_n < T_n := p_n(p_n^{1/n} − 1)
```

The middle form is an **exact integer predicate** — that is the one the notebook decides where it
claims to decide. `F` is Π₁: **no finite computation proves it.** `¬F` is Σ₁: a single index would
refute it. Every verdict below is placed on the correct side of that asymmetry.

---

## 1. Headline findings

### F1 — No counterexample below `10^7`. `[self-contained]`

664 579 primes, 664 578 consecutive pairs, checked three independent ways:

| method | scope | violations |
|---|---|---|
| `float64` screen on `ρ_n = g_n/T_n` | all pairs | 0 |
| 50-digit recomputation of `n·log p_{n+1}` vs `(n+1)·log p_n` | all pairs | 0 |
| exact integer `pow(p_{n+1},n) < pow(p_n,n+1)` | all `n ≤ 10 000`, plus the 40 largest-`ρ` indices anywhere in range | 0 |

Minimum relative margin at 50 digits: `6.34·10⁻⁷`, i.e. **~44 orders of magnitude above the
arithmetic noise floor**. The decision is not being made inside the error bars.

**This corroborates F on the range and refutes nothing.** It bounds where a counterexample can
live — nowhere below `10^7` — which is the only general statement a finite run may make about a Π₁
sentence. The published verification range is far larger (`p < 4·10^18`, `[L3-recall]`,
`[needs-anchor]` per `decompose` §2.3 A2; **not sourced in this run**).

Tightest approach observed: `ρ = 0.760471` at `n = 217`, `p = 1327`, `g = 34`, over `n ≥ 10`.
Over **all** `n` the maximum is `ρ = 0.91199` at `n = 4` (`p = 7`) — the `n ≥ 10` convention is
inherited from `decompose` §4.2 and the notebook discloses what it excludes rather than dropping it
silently.

### F2 — The target claim survives, and in a **stronger** form than it was stated. `[self-contained]`

`decompose` asserts RH does not reach Firoozbakht, using the recalled bound `g_n ≪ √p_n·log p_n`.
The notebook tests the **shape** rather than the attribution. Write `B_C(p) = C·√p·log p`. A bound
of that shape certifies F at `p` only if `B_C(p) < T(p)` — a decidable numerical predicate.

Define `p*(C)` = the largest `P` such that `B_C(p) < T(p)` for all `10 ≤ p ≤ P`:

| `C` | certified range `p*(C)` |
|---|---|
| 1 | **`p ≤ 3`** (exact bar; first failure at `p = 5`) |
| 22/25 `[L3-recall]` | `p ≤ 5` |
| 4/π `[L3-recall]` | `p ≤ 2` |
| 1/(8π) `[L3-recall]` | `p ≤ 62 869` |
| `10⁻²` | `≈ 1.77·10⁶` |
| `10⁻⁴` | `≈ 5.6·10^10` |
| `10⁻⁶` | `≈ 1.1·10^15` |
| `10⁻⁸` | `≈ 1.9·10^19` |

And in the other direction — the largest constant that certifies F all the way to a target `P`:

| target `P` | largest admissible `C` |
|---|---|
| `10^7` (this run's own range) | `4.76·10⁻³` |
| `10^12` | `2.66·10⁻⁵` |
| `4·10^18` (recalled published range) | `2.09·10⁻⁸` |
| `10^30` | `6.81·10⁻¹⁴` |
| `10^100` | `2.29·10⁻⁴⁸` |

Two consequences, both computed rather than asserted:

1. **The failure is uniform in the constant.** `required_C(P) ~ log P/√P → 0`, so `p*(C)` is
   **finite for every `C > 0`**. No bound of RH shape, at any positive constant, certifies F for all
   `n`. Sharpening the constant is not a route; it is a treadmill.
2. **The circulating constants do not even reach what is already computed.** One would need
   `C ≈ 2·10⁻⁸` merely to match the recalled published verification range, and `C ≈ 4.8·10⁻³` to
   match this notebook's own `10^7`. Constants of order `0.04–1` certify `p ≤ 3`, `p ≤ 5`,
   `p ≤ 62 869` — a conditional theorem weaker than a laptop.

**This conclusion does not depend on any `[L3-recall]` constant.** That matters: card `L11` records
under *Declared gap* that the RH-conditional gap bound **has no ledger row in this run**. The
strategic verdict is therefore not blocked by the missing citation — it is a statement about the
function `√p·log p`, which is elementary and self-contained.

### F3 — A distinction the write-up should keep: *scale*, not *precision*. `[self-contained]`

RH's genuinely strong consequence is not a gap bound but control of the counting error,
`|π(x) − li(x)| ≤ c√x log x` (`[L3-recall]`, Schoenfeld-type, `c = 1/8π` — **not sourced here**).
Since `T_n = p_n(p_n^{1/n} − 1)` takes `n = π(p_n)` as its only non-elementary input, one might hope
RH sharpens the bar itself. The notebook measures this by recomputing the bar with `n` perturbed by
the full RH-admissible error:

| `p` | relative shift of the bar `|ΔT|/T` |
|---|---|
| `10^4` | `3.0·10⁻²` |
| `10^8` | `1.3·10⁻³` |
| `10^12` | `2.9·10⁻⁵` |
| `10^18` | `6.7·10⁻⁸` |
| `10^24` | `1.2·10⁻¹⁰` |

The margin that actually decides F is `1 − ρ`: `0.24` in this run's range, recalled at `≈ 0.08` over
all known primes (`[L3-recall]`, `decompose` §4.3 A10). **RH's precision on the `π(x)` side is three
to ten orders of magnitude finer than the quantity in dispute.** So the honest sentence is *not*
"RH is not precise enough". It is: **RH's precision is ample and irrelevant; the obstruction is a
mismatch of scale on the gap side — `√p·log p` versus `log²p`.** This quantifies, for the RH error
term specifically, the anti-test that `decompose` §4.6 argued for the Littlewood oscillation.

How large the mismatch is, in range: `B_1(p)/T(p)` runs `1.7 → 210` between `p = 31` and `p = 10^7`,
growing like `√p/log p`. Against the actual gaps the RH-shape bound is looser still — a factor 2832
at `p = 10^7`.

---

## 2. Companion results re-tested at 3× the decompose range

Not the target, but cheap and load-bearing downstream, so they were re-run rather than inherited.

| claim (`decompose`) | reported there (`p < 3·10⁶`) | here (`p < 10^7`) | verdict |
|---|---|---|---|
| §2.4 — `T` is **not** monotone | descends at 55.9% of steps | **56.4%** (374 485 / 664 569) | **reproduced** |
| §2.4 — tight cases sit at record gaps | all 6 tightest | **8 of the 10 largest `ρ`** | reproduced, weaker than "all" |
| §4.3 — `ρ` and `g/L²` rank differently | max `ρ` at `p = 1327`, max `g/L²` at `p = 2 010 733` | identical, both reproduced | **reproduced** |
| §1.3 — `T_n = L² − L − 1 + O(1/L)` | asymptotic | ratio `0.648` at `p = 31`, `0.989` at `p ≈ 8·10³`, `1.0006` at `10^7` | holds; **bad below `p ≈ 10³`** |

The last row has a practical edge: the `L² − L − 1` surrogate must **not** be used to decide
anything at small `p`. The `C = 1` verdict in F2 is decided exactly there, so the notebook redoes it
against the exact bar `T_n` at every actual prime — that is where `p ≤ 3` comes from, versus the
surrogate's cruder "nothing at all".

**P6′ (the maximal-gap reduction) remains undischarged.** This notebook confirms the obstruction is
real — non-monotone at 56.4% of steps — and does **not** repair it. Any downstream leg citing "it
suffices to check record gaps" is still importing an unproved lemma.

---

## 3. Falsification attempts actually run

Recorded because "we found nothing" is only meaningful if the search could have found something.
Each row states what would have broken a claim made here. All nine came back as expected;
the notebook prints the table and fails loudly if any does not.

| attempt | would have refuted |
|---|---|
| `ρ_n ≥ 1` anywhere below `10^7` (float screen) | F itself |
| any violation at 50 digits over all pairs | F itself |
| exact-integer violation at `n ≤ 10 000` | F itself |
| exact-integer violation at any of the 40 largest-`ρ` indices | F itself |
| `B_1 = √p log p` certifying F beyond `p = 10` | **F2** |
| a `C = 10⁻⁸` bound certifying F beyond `10^30` | **F2** |
| `required_C(P)` failing to decay | **F2** (the uniformity argument) |
| `T` monotone in `n` | §2 (would rescue the naive record-gap reduction) |
| `ρ` and `g/L²` sharing a maximizer | §2 (would make T3 a safe search objective) |

---

## 4. Honest limits of this artifact

1. **Range.** `p < 10^7`. This is *below* the recalled published verification range by 11 orders of
   magnitude. The notebook's own verification adds no new knowledge about where a counterexample
   lives; its value is in F2/F3, which are range-independent.
2. **Exact integer arithmetic** covers `n ≤ 10 000` and the 40 tightest indices, not all 664 578
   pairs (cost: `pow` at `n ≈ 6.6·10^5` is seconds per call). Everything else rests on 50-digit
   `mpmath` logarithms with a reported margin — **mpmath's `log` is high-precision, not formally
   certified**. The margin (`6.3·10⁻⁷` against a `10⁻⁵⁰` working precision) makes a precision-induced
   error implausible; it does not make it impossible. A Lean-side or interval-arithmetic check would
   close this, and is the natural handoff to the `lean-skeleton` leg.
3. **Every literature constant is `[L3-recall]` and unsourced in this run** — `22/25`, `4/π`,
   `1/(8π)`, the `4·10^18` verification range, the `ρ ≈ 0.92` record. They are entered as *hypotheses
   about the literature*, never as citations. **No finding above depends on one**; F2 is deliberately
   constructed to be uniform in `C` precisely so the missing ledger row (card `L11`, *Declared gap*)
   cannot propagate into the verdict. Any paper quoting these numbers **must fetch a source first**.
4. **Nothing here is a proof of anything about RH.** The notebook never assumes RH, never uses it,
   and proves no statement conditional on it. It evaluates an inequality between two explicit
   elementary functions. That is all — and it is sufficient for the target, which is a claim about
   *reach*, not about truth.
5. **What computation refuted here is a hope, not a theorem**: the hope that a smaller constant, or
   RH's sharper `π(x)` input, could bring the conditional route within reach of Firoozbakht. §3.2 and
   §4 of the notebook kill that quantitatively. The conjecture itself remains open, and this run
   moves it neither way.

---

## 5. Reproduction

```bash
cd attack/notebook-1
jupyter nbconvert --to notebook --execute --inplace notebook-1.ipynb
```

Runtime ≈ 70 s on an M-series laptop (sieve 0.03 s; 50-digit pass 13 s; exact integers 51 s).
Dependencies: `numpy`, `mpmath`, `matplotlib`, `nbformat`/`jupyter`. The notebook is self-contained —
no network, no data files, no state carried in from other legs. It writes `summary.json` and
`figure-1-rh-vs-bar.png` next to itself; both are committed alongside, and `summary.json` is the
machine-readable handoff for `synthesize` / `write-paper`.
