# findings-0 — computational stress of **first-failure-maximality** (target #0)

**Leg:** `notebooks__0` (crew role: coder) · molecule `task-20260725-9727`
**Artifacts:** `notebook-0.ipynb` (executed, 34 cells, all outputs live), `ffm_lab.py`,
`deep_run.py`, `deep_run_1e11.json`, `build_notebook.py`
**Runtime:** notebook re-executes in ≈25 s; the headline sweep (`deep_run.py 1e11`) took 633 s.

---

## 0. What was under test, and what a notebook can do to it

**F (Firoozbakht).** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`; equivalently
`g_n < T_n` with `T_n = p_n(p_n^{1/n} − 1)` (cards **D4**, **D5**, **L1**).

**Target #0 (FFM).** *If F fails, the least failing index carries a record (maximal) gap.*
This is `decompose.md` §2.4's **P6′** and card **L15**, marked **OPEN**: the sole pruning
rule of the only computationally live route, unproved by anyone.

Computation is a Σ₁ instrument. It can refute F, refute a *derivation*, and bound where a
counterexample is not. It cannot prove a Π₁ statement. Nothing below is offered as a proof,
and the notebook's §11 restates the limits.

---

## 1. The reduction that made the target checkable

FFM is about a first failure that may not exist, so it cannot be checked directly — it is
vacuously true on every range where F holds, which is every range anyone has swept. The
notebook removes the vacuity by sharpening the governing index. Let

```
m(n) := min{ m : g_m ≥ g_n }        (always a record index, by construction)
```

Then the standard argument goes through **iff** `T_{m(n)} ≤ T_n`, so:

> **FFM holds on [1,N] ⟺ `T_{m(n)} ≤ T_n` for every n ≤ N.**

This is sharper than the upstream statement of P6′ ("`T_m ≤ T_n` whenever `m < n` and
`p_m, p_n` straddle a record gap"), which quantifies over pairs and does not say *which* `m`
the argument needs. The sharpened form is a predicate at each single index, and it is what
was measured.

---

## 2. What the computation supports

| # | Finding | Scale |
|---|---|---|
| 1 | **F unrefuted.** No index with `g_n ≥ T_n`; none within `10⁻⁶` of the boundary either. | `p ≤ 10¹¹`, **4 118 054 812** indices |
| 2 | **FFM predicate: zero exceptions.** `T_{m(n)} ≤ T_n` at every index. | same — vs `n ≤ 216 815` upstream |
| 3 | **The margin does not decay.** `min(T_n − T_{m(n)})` per decade: `0.485` at `10⁴`, then `1.68, 3.81, 1.70, 3.89, 2.37, 16.53` through `10¹⁰`. The global minimum is at `n = 1879` and is never approached again. | 11 decades |
| 4 | **The threat decays.** Max dip of `T` below its running max: `0.549` at `10³` → `5.0·10⁻⁵` at `10¹⁰`, a factor ≈4 per decade. | 11 decades |
| 5 | **The tolerance obeys a law.** P6′ at `n` ⟺ `π(p_n) ≤ log p_n / log(1 + T_m/p_n)`. Expressed relatively, the window `(p_m, p_n]` may hold at most `(1 + c/log p_n)×` its expected count, with **c ≈ 2.2 flat across five decades** (2.85, 2.28, 2.34, 2.43, 2.25). | `p ≤ 10⁸` |
| 6 | **Brun–Titchmarsh settles 99.861 %** of governed indices unconditionally, coverage improving monotonically (92.6 % at `10³` → 99.907 % at `10⁷`). | `p ≤ 10⁸` |
| 7 | **Mechanism identified.** The worst cases from `10⁵` up sit `10⁴`–`10⁹` primes past their governor, with safety factors 76–250 or infinite (window *poorer* than li). Near-record gaps are rare, recur late, and sit in locally sparse stretches — exactly where `T` runs above trend. | 11 decades |

Finding 5 is the one to carry forward: it turns P6′ from a qualitative worry into a single
number that a theorem must beat.

---

## 3. What the computation refutes

**R1 — FFM does not follow from the definitions.** §9 exhibits an explicit increasing
integer sequence (real primes to 1327, then a jump of 40, then 100 jumps of 2, then a jump
of 38) whose **first** Firoozbakht failure is at index 323 on a gap of 38 — not a record.
Verified in exact integer arithmetic; no floats, so rounding cannot be blamed. Consequence:
**any proof of FFM that does not consume an arithmetic density input is wrong**, because the
statement is false for sequences that satisfy everything except primality.

The same section quantifies how far that counter-model is from reality: the dense run it
needs exceeds the Montgomery–Vaughan cap `2y/log y` by a factor that **grows** with scale —
1.41 at `p ≈ 10³`, 4.18 at `4·10⁸`, 9.13 at `10¹⁸`. So the counter-model is excluded
unconditionally, and increasingly comfortably. Both halves matter: FFM needs an arithmetic
input, and a weak one suffices *for this mechanism*.

**R2 — the independent two-sided π-bound route to P6′ cannot work.** Bounding `T_m` from
above and `T_n` from below with explicit `π(x)` estimates at the two endpoints separately
requires a record gap `G` of at least `5.3·10⁴` at `p=10⁶` (Dusart) or `3.7·10³` (Axler),
against actual records of size `≈ log²p ≈ 176`; past `≈10¹¹` the criterion is unsatisfiable
at any `G`. The bound spread (`≈0.1·L` for Dusart, `≈0.17` for Axler) dwarfs the quantity
being resolved. **No sharpening of constants rescues this route.**

**R3 — "P6′ is a Dusart lookup, not a research leg" is half wrong.** Card **L15** records
that as the panel's position (`synthesis.md` §2 C7) and concurs with it. The measurement
splits it:

| regime | settled by | status |
|---|---|---|
| typical windows | Brun–Titchmarsh | unconditional, 99.861 % of indices |
| the extremal configuration | short-interval count sharp to `1 + 2.2/log p` | **open, Cramér strength** |

Brun–Titchmarsh permits a `2×` density overshoot; P6′ tolerates `1 + 2.2/log p`. The gap is
a factor `≈ log p / 2.2` and it **widens** with scale even as empirical coverage improves.
A pruning rule is worth its worst case, not its average case — so P6′ retains a hard core
that no lookup reaches.

**R4 — two upstream numbers corrected.**

- The extremum of `ρ = g/T` over eleven decades is at **n = 4** (`p=7`, `g=4`, `T=4.386`,
  `ρ = 0.911985`), then `n = 2` (`ρ = 0.910684`). Both sit below the `n ≥ 10` cutoff that
  `probe2.py` imposes, so `decompose.md` §5.1's "tightest cases" are the tightest cases *of
  a truncated list*. Card **L15** hazard 3 already flags that list as a display artefact;
  the true extremum is recorded here. (No third case in eleven decades reaches `ρ = 0.84`.)
- The **55.92 %** single-step statistic is reproduced *exactly* at its own bound
  (121 239 / 216 814 steps at `3·10⁶`) but is **range-dependent**: it is **57.88 %** at
  `10⁹`. It must never be quoted without its bound. It remains uninformative about P6′,
  as **L15** hazard 4 says.

---

## 4. Directive for the downstream legs

**For `proof-attempt__0` / `lean-skeleton`.** Do not attack P6′ by bounding `π` at both
endpoints (R2 — unsatisfiable at every scale). Write `n = m + k` with `k = π(p_n) − π(p_m)`
the exact local count and bound the **single** index `m`; the π-uncertainty then cancels
between the two sides. In that form the worst case (`k = 1`, empty window, `p_n = p_m + G`)
reduces to `G ≳ log p_m − 2`, which record gaps clear by a factor 11–41, and the general
case reduces to the density statement of finding 5. The notebook evaluates this route at
60 digits and finds it positive at every scale tested (`+1.7·10⁻²` at `1.4·10⁶` down to
`+4.3·10⁻¹⁵` at `10²¹`).

**Precision warning.** That margin is `≈10⁻¹²` at `10¹⁸` and float64 reports a flat **0** at
`10²¹`. Any rigorous version must be interval-arithmetic or symbolic. Likewise the
Brun–Titchmarsh certificate of §8 is evaluated in float64 and its inequalities are not
tight; a rigorous version needs re-derivation.

**For any leg reporting a verification height from a record-pruned search.** State that P6′
is assumed. It is not proved by this notebook and was not proved upstream (**L15** hazard 2,
the laundering risk). What this notebook adds is that the assumption is now unviolated over
4.1 billion indices and that its failure mode has a price tag: an interval holding
`1 + 2.2/log p` times its expected primes.

**Citation caveat.** The Axler constants in §10 come from card **T1**, which flags them as
**L2_strong and unopened**. Nothing above depends on Axler except the §10 comparison, whose
Dusart row (L0) carries the same verdict.

---

## 5. Honest ledger of what was run

| gate | result |
|---|---|
| `python3 build_notebook.py` | exit 0 — 34 cells written |
| `jupyter nbconvert --execute --inplace notebook-0.ipynb` | **exit 0 — zero cell errors**, all outputs in the committed file |
| exact-integer check of F, `n = 1..4000` | 0 failures; 0 disagreements between the `g<T` form and the integer form |
| stable vs naive margin, vs 80-digit reference | naive error `1.8·10⁻⁸` at `n≈2.3·10⁷`; stable error `8.9·10⁻¹⁶` |
| cross-check against upstream at `3·10⁶` | 21 record gaps, max `T`-dip `0.5487`, 55.92 % down-steps — **all three reproduced** |
| `deep_run.py 1e11` | 633 s, `n_last = 4 118 054 812`, 40 record gaps, 0 violations, 0 FFM exceptions |

**Not done / out of scope.** No search above `10¹¹`. No symbolic or interval-arithmetic
version of the §8/§10 criteria. No attempt to verify the published `4·10¹⁸` verification
height (`decompose.md` §2.3, `[needs-anchor]`) — this leg's `10¹¹` is independent and
self-contained, and is *not* an independent confirmation of that figure.
