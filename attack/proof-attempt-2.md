# Proof attempt #2 — target `unconditional-verified-range`

**Molecule:** `task-20260725-909e` (leg: `proof-attempt`, target #2, crew role: proofsmith)
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-25 · **Formal backend:** Lean 4 / Mathlib
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.
**Status of `F` in this document: OPEN.** Not assumed true, not assumed false. Nothing below
claims to prove or refute `F`.

---

## 0. Perimeter

**Admitted inputs — exhaustively:**

| Input | Provenance |
|---|---|
| `attack/decompose.md` | leg `decompose`, molecule `task-20260725-c062`, this run |
| `attack/source-ledger.md` | leg `source-ledger`, molecule `task-20260725-d320`, this run |
| `attack/concept-cards/` (30 cards) | leg `concept-cards`, molecule `task-20260725-068e`, this run |
| in-run computation performed **by this leg** | sieve to `2·10⁷`, §4 |

Nothing else was read. **No source PDF was opened by this leg.** Every external mathematical fact
used below is used *at the tier the run's own ledger already assigned it*, and is named with that
tier at the point of use. Where a cited fact is load-bearing, §4 re-derives its consequences
numerically from scratch so that a citation error would show up as a numerical contradiction
rather than pass silently.

**Sibling legs `proof-attempt-0` (`first-failure-maximality`) and `proof-attempt-1`
(`RH-conditional-bound`) had emitted nothing at the time this leg ran.** No result of theirs is
assumed. In particular **L15 / P6′ (the maximal-gap reduction) is treated as OPEN throughout** —
and §2.5 shows this target does not need it.

---

## 1. What target #2 asserts, stated precisely

The target name `unconditional-verified-range` is a slogan; a proof attempt needs a sentence. Two
readings are available, and they have different answers. Both are settled below.

**Reading (A) — the finite-range theorem.**
> There is an explicit `X` and an explicit finite object `C` (a table) such that
> `F` holds at every `n` with `p_n ≤ X`, and the implication `C ⟹ (F on [1, X])` is a theorem
> requiring **no unproved hypothesis** — no Riemann Hypothesis, no Cramér–Granville heuristic,
> no P6′, no conjecture of any kind.

**Reading (B) — the table-free range.**
> There is an explicit `X` such that `F` holds at every `n` with `p_n ≤ X`, proved from
> unconditional analytic estimates **alone**, with no enumeration of primes and no gap table.

**Verdicts reached in this document.**

- **Reading (A): PROVED**, with the reduction reconstructed from first principles and with
  explicit constants (§2, Theorem 2). The theorem is unconditional in the mathematical sense; its
  hypothesis `C` is a finite computation, and the honesty of the result lives entirely in stating
  which computation and who ran it (§5).
- **Reading (B): PROVED for a bounded window, and PROVED IMPOSSIBLE outside it** (§3,
  Proposition 3 and Proposition 4). The window is
  `396 738 ≤ p_n ≤ 777 600`, and it closes **permanently** at `p ≈ 7.776·10⁵` — no unconditional
  analytic estimate now known can extend it, and §3.3 says exactly which quantity would have to
  change. This is a small positive result plus a sharp obstruction, and to this leg's knowledge
  the window is not stated anywhere in the run's inputs.

Neither reading gets anywhere near `F` itself. §5 says so in the strongest terms available.

---

## 2. Reading (A): the finite-range theorem

### 2.1 Notation

`p_n` = the `n`-th prime, `p_1 = 2` (**D1**; note the 1-indexing — Mathlib's `Nat.nth` is
0-indexed, correction #1 of the card set). `L := L_n := log p_n` (natural log).
`g_n := p_{n+1} − p_n` (**D2**). `π(x)` = prime-counting function, `π(p_n) = n` (**D3**).

```
T_n  :=  p_n · (p_n^{1/n} − 1)  =  p_n · (e^{L_n/n} − 1)          (D5)
```

### 2.2 Lemma 1 (exact reformulation) — PROVED, self-contained

> For every `n ≥ 1`:  `F` holds at `n`  ⟺  `p_{n+1}^{\,n} < p_n^{\,n+1}`  ⟺  `g_n < T_n`.

*Proof.* All quantities are real and `> 1`. `t ↦ t^{n(n+1)}` is strictly increasing on `(0,∞)`,
so raising `p_{n+1}^{1/(n+1)} < p_n^{1/n}` to that power gives `p_{n+1}^n < p_n^{n+1}`, and the
step is reversible. `log` is strictly increasing, so this is `n·log p_{n+1} < (n+1)·log p_n`, i.e.
`log p_{n+1} < L_n(1 + 1/n)`, i.e. `p_{n+1} < p_n e^{L_n/n}`, i.e.
`p_n + g_n < p_n + p_n(e^{L_n/n} − 1)`. ∎

This is card **L1**, re-derived here rather than imported. It is used with the *strict* inequality
throughout. (Visser's Conjecture 3 as quoted on **D5** writes `g_n ≤ p_n(p_n^{1/n} − 1)`; the two
agree because `g_n` is an integer and `T_n` is irrational for `n ≥ 2`, but this document does not
rely on that and uses strict `<` on both sides.)

### 2.3 Lemma 2 (the analytic input) — CITED, tier L0 via the run's ledger

> `π(x) ≤ x/(log x − 1.1)` for all `x ≥ 60 184`.

**Source:** `dusart2010estimates` (arXiv:1002.0442), **Theorem 6.9, eq. (6.6)**, read at the
locator by the `source-ledger` leg and recorded on card **T1** at tier **L0**. This leg did not
re-open the paper; it re-verified the inequality numerically at every prime in `[60 184, 2·10⁷]`
(§4, V2b — 0 failures).

**This is the only external mathematical input to Theorem 2.** In particular the argument below
does **not** use Axler's Corollaries 3.5/3.6, which card **T1** hazard 2 flags as *unopened in
this run* and *Priority 1 for the citation gate*, and which sit beneath Kourbatov's Theorems 1, 3
and 5 (cards **L2**, **L3**, **L4**). Avoiding them is deliberate; see §6.1.

### 2.4 Lemma 3 (the explicit floor under the bar) — PROVED

> Define `B(p) := (log p)² − 1.1·log p`. Then for every `n` with `p_n ≥ 60 184`:
> `T_n > B(p_n)`.

*Proof.* `e^t − 1 > t` for `t > 0`, and `L_n/n > 0`, so `T_n > p_n·L_n/n`. By **D3**, `n = π(p_n)`,
and by Lemma 2 with `x = p_n ≥ 60 184`, `n ≤ p_n/(L_n − 1.1)`; note `L_n − 1.1 > 0` in this range.
Hence `p_n/n ≥ L_n − 1.1` and

```
T_n  >  p_n · L_n / n  =  L_n · (p_n/n)  ≥  L_n(L_n − 1.1)  =  B(p_n).   ∎
```

*Idea in one line:* the bar `T_n` is `p_n·(p_n^{1/n} − 1)`, whose only opaque ingredient is
`n = π(p_n)`; an **upper** bound on `π` is exactly what turns the bar into a **lower** bound in
`log p_n` alone.

**Sharpness note.** The step `e^t − 1 > t` discards `L⁴/(2p) → 0`; the loss is invisible. The
binding loss is Dusart's `1.1`. Numerically the slack `T_n − B(p_n)` is smallest near
`p = 155 893`, where it is `+0.0799` (§4, V2) — the bound is close to tight there and comfortable
everywhere else. It is **proved**, not measured; the measurement only confirms no sign error.

### 2.5 Lemma 4 (monotonicity) — PROVED

> `B` is strictly increasing on `[e^{0.55}, ∞) ⊇ [2, ∞)`.

*Proof.* With `L = log p`, `dB/dL = 2L − 1.1 > 0` for `L > 0.55`, and `L ↦ log p` is strictly
increasing. `e^{0.55} = 1.7333 < 2`. ∎

**This lemma is the whole point of the leg.** The obvious route to a verified range — "check
record gaps only, because `g_n ≤ g_m` for the governing record index `m`" — needs `T_m ≤ T_n`,
i.e. monotonicity of `T`, and **`T` is not monotone**: it decreases at `55.92 %` of steps
(card **L15**, obligation P6′, **OPEN**). Lemma 4 sidesteps this completely: `B` is a function of
`p` **alone**, not of the pair `(p_n, n)`, and it is monotone for a one-line reason. The
non-monotone object `T` never appears in a comparison between two different indices.

> **Finding for the run.** *Target #2 does not depend on L15 / P6′.* The concept-card set ranks
> "discharge P6′" as open obligation #1 and notes it "sits under the only live route" (INDEX §2).
> That is true of the *search* route (**T2**) and of target #0 (`first-failure-maximality`). It is
> **not** true of the verified range. Any downstream leg that gates the verified range on P6′ is
> importing a dependency that is not there.

### 2.6 Theorem 2 (unconditional finite-range verification) — PROVED

Let `X ≥ 60 184` and let `X₀ := 60 184`. Suppose:

- **(H1)** *(base case, finite arithmetic)* `p_{n+1}^{\,n} < p_n^{\,n+1}` for every `n` with
  `p_n < X₀`;
- **(H2)** *(gap-table completeness)* a table is available listing, for every gap value `g` that
  occurs as `g_n = g` for some `n` with `p_n ≤ X`, the **first occurrence**
  `q(g) := min{ p_n : g_n = g }`;
- **(H3)** *(per-gap check)* for every gap value `g` in that table with `q(g) ≥ X₀`:
  `g ≤ B(q(g))`.

Then **`F` holds at every `n` with `p_n ≤ X`.**

*Proof.* Let `n` satisfy `p_n ≤ X`. If `p_n < X₀`, Lemma 1 and (H1) give `F` at `n`. Otherwise
`p_n ≥ X₀`. Put `g := g_n` and `q := q(g) ≤ p_n`. Two cases.

- If `q ≥ X₀`: by (H3), `g ≤ B(q)`; by Lemma 4 and `q ≤ p_n`, `B(q) ≤ B(p_n)`; by Lemma 3,
  `B(p_n) < T_n`. Hence `g_n < T_n`, and Lemma 1 gives `F` at `n`.
- If `q < X₀ ≤ p_n`: the first occurrence of `g` lies in the base-case range, so
  `g ≤ G₀ := max{ g_k : p_k < X₀ } = 72`, attained at `p = 31 397` (§4, V7 — exact integer
  arithmetic over the 6 076 gaps below `X₀`). Since `B(X₀) = B(60 184) = 109.008 > 72 ≥ g`,
  Lemma 4 (`p_n ≥ X₀`) and Lemma 3 give `g ≤ G₀ < B(X₀) ≤ B(p_n) < T_n`. Hence `F` at `n`. ∎

The second case is why (H3) is stated only for `q(g) ≥ X₀`: gap values that first appear below
`60 184` are all small enough to be dominated by `B(X₀)` outright, so they need no per-gap check
at all.

**Restated as a decision procedure.** Define, for a gap value `g`,

```
S(g)  :=  exp( (1.1 + sqrt(1.21 + 4g)) / 2 )      — the unique p with B(p) = g
```

so that `g ≤ B(p) ⟺ p ≥ S(g)`. Then **(H3) reads `q(g) ≥ S(g)`**, and the content of Theorem 2 is:

> *A gap of size `g` occurring at a prime `p ≥ max(S(g), 60 184)` cannot violate `F`.*

The verification of a range therefore costs: one finite integer check below `60 184`, plus one
comparison `q(g) ≥ S(g)` per distinct gap value. Nothing else.

### 2.7 Corollary 2.1 (what this yields at the published frontier) — CONDITIONAL ON A TABLE

Card **L6** records, at tier L0 through `kourbatov2015verification` (2023 endnote) and
`visser2019verifying`, that `F` is verified for all `p < 2⁶⁴`, and that the first-occurrence gap
table consumed by that verification is `oliveira2014goldbach` — **which no leg of this run
opened** (**L6** hazard 3; ledger §6.2; citation-gate priority 4).

Applying Theorem 2 with `X = 2⁶⁴`:

- The largest gap value `g` for which `S(g) ≤ 2⁶⁴` is **`g = 1918`** (§4, V5b).
- Hence, *given a complete first-occurrence table below `2⁶⁴`*, every gap of size `≤ 1918`
  occurring at a prime `≥ max(S(g), 60 184)` is safe, and only the finitely many first
  occurrences sitting below their `S(g)` need direct inspection.

Kourbatov's own 2023 endnote states, verbatim on card **L6**: *"prime gaps of size `g < 1920`
cannot violate (1)"*. **This leg's independently derived constant is `1918`** — two below, exactly
as expected from having used Dusart's `x/(log x − 1.1)` where Kourbatov used the sharper Axler
route. The agreement of two independently derived thresholds to `0.1 %` is the strongest available
evidence that neither derivation carries a sign or transcription error. It is corroboration, not a
second proof: both rest on the same style of `π(x)` bound.

**What Corollary 2.1 is and is not.** It is *not* an independent verification to `2⁶⁴`. This leg
enumerated primes to `2·10⁷`, twelve orders of magnitude short. It is a **reconstruction of the
implication** — the step from "here is a first-occurrence gap table" to "`F` holds on the range" —
carried out here from first principles, with explicit constants, and resting on **one** cited
inequality (Lemma 2) instead of the unopened Axler chain.

---

## 3. Reading (B): the table-free range

Can a range be certified with **no** prime enumeration at all? Theorem 2 needs (H1)–(H3), all
computational. Reading (B) asks whether analysis alone suffices anywhere.

### 3.1 The only available lever

By Lemma 3, `F` holds at `n` as soon as `g_n ≤ B(p_n)`. A table-free proof must therefore supply
an **unconditional, explicit upper bound on `g_n`** that beats `B(p_n) ≈ L² − 1.1L`. Explicit
prime-gap upper bounds come from explicit "prime in a short interval" theorems. The one available
in the run's ledger at tier L0 is:

> **Dusart Prop. 6.8** (card **T1**): for all `x ≥ 396 738` there is a prime `p` with
> `x < p ≤ x(1 + 1/(25 ln²x))`.

which gives, for `p_n ≥ 396 738`:  `g_n ≤ p_n/(25 L_n²)`.

### 3.2 Proposition 3 (the window is non-empty) — PROVED

> `F` holds at every `n` with `396 738 ≤ p_n ≤ 777 600`, **with no computational input
> whatsoever** beyond the two cited explicit estimates.

*Proof.* For such `n`, Dusart Prop. 6.8 gives `g_n ≤ p_n/(25L²)`, and Lemma 3 gives
`T_n > L² − 1.1L`. So it suffices that

```
p / (25 L²)  ≤  L² − 1.1 L      ⟺      p  ≤  25 L³ (L − 1.1),        L = log p.
```

Let `h(p) := p − 25 (log p)³ (log p − 1.1)`. `h(396 738) = −2.35·10⁵ < 0` and
`h` has a unique sign change on `[396 738, ∞)` at `p* = 777 600.744…` (§4, V8; `h` is eventually
increasing and `h' > 0` throughout `[4·10⁵, ∞)` since `h'(p) = 1 − (25/p)(4L³ − 3.3L²) > 0`
there). Hence the displayed inequality holds on `[396 738, p*]`, so `g_n < T_n`, so `F` at `n` by
Lemma 1. ∎

### 3.3 Proposition 4 (the window closes, permanently) — PROVED, as an obstruction

> For `p > 777 601`, Dusart Prop. 6.8 does **not** imply `F`, and the shortfall grows without
> bound: `p/(25L²) ÷ (L² − 1.1L) → ∞`.

*Proof.* Immediate from §3.2: the ratio is `p / (25L³(L−1.1)) → ∞` since `p` grows faster than any
power of `log p`. ∎

**Precise statement of the obstruction.** A table-free proof of `F` on `[X₀, X]` requires an
unconditional explicit gap bound of quality `g_n = O(log² p_n)` on that range. Every known
unconditional gap bound — Dusart's `p/(25 log²p)` here, Baker–Harman–Pintz's `p^{0.525}`
(card **L11**), and everything between — is a **power of `p`**, not a power of `log p`. This is
not a matter of constants: it is the P3 wall of `decompose.md` §2.1, encountered from the
finite-range side rather than the asymptotic side. **Reading (B) is dead above `7.776·10⁵` and
will stay dead until unconditional prime-gap technology reaches `log²` scale — which is precisely
the strength that proving `F` itself requires.**

*Corollary of the obstruction, stated so no downstream leg re-derives it:* **no amount of
analysis will ever eliminate the computational input from a verified-range claim.** The verified
range is, irreducibly, a computation plus a theorem about the computation. Theorem 2 is the
theorem; §5 names the computation.

Note also that Proposition 3's window `[396 738, 777 600]` lies entirely **above** `X₀ = 60 184`
and is therefore *already covered* by (H1)+(H2)+(H3) of Theorem 2 in any real verification. Its
value is not that it extends anything; its value is that it is the **exact measure of how much
analysis alone can do**, and the measure is: one factor of about 2 in `p`, once, at `p ≈ 10⁶`.

---

## 4. In-run verification

Sieve of Eratosthenes to `2·10⁷`, 1 270 607 primes, largest `19 999 999`; 1-indexed at `p_1 = 2`.
Script: `attack/verify-pa2.py` (committed alongside this file). Every number below was recomputed
here; none was copied from an upstream card.

| ID | Check | Result |
|---|---|---|
| V1a | exact **integer** arithmetic `p_{n+1}^n < p_n^{n+1}`, all `n` with `p_n < 60 184` (6 076 indices) | **no violations** |
| V1b | `g_n < T_n` in floating point, `n ≤ 1 270 606` | **no violations** |
| V1c | `max ρ_n = g_n/T_n` (`n ≥ 10`) | `0.7604709` at `n = 217`, `p = 1327`, `g = 34` |
| V2 | **Lemma 3**: `T_n > B(p_n)` for all `p_n ∈ [60 184, 2·10⁷]` | **0 failures**; tightest slack `+0.079891` at `p = 155 893` |
| V2b | **Lemma 2** (Dusart) `π(x) ≤ x/(log x − 1.1)` at every prime in `[60 184, 2·10⁷]` | **0 failures** |
| V3 | **Lemma 4**: `B` increasing on a geometric grid over `[2, 10¹⁹]` | **0 failures**; analytic `2L − 1.1 > 0` for `p > 1.7333` |
| V4 | distinct gap values below `2·10⁷` | 80; **31** have first occurrence below `max(S(g), 60 184)`, all at `p ≤ 44 293 < X₀` |
| V4b | consistency: `p ≥ max(S(g), X₀) ⟹ g ≤ B(p)`, all sieve indices | **0 violations** |
| V5 | criterion at the published record CSG point `p = 1 693 182 318 746 371`, `g = 1132` (**L7**, OEIS A111943 at tier L0) | `B(p) = 1191.009` — **safe, margin 4.955 %** |
| V5b | largest `g` with `S(g) ≤ 2⁶⁴` | **1918** (Kourbatov's endnote: `g < 1920`) |
| V6 | cost of using Dusart rather than Axler: `B(p)` vs Kourbatov's `L²−L−1.17` | deficit `0.193 %` at `p = 2·10⁷`, `0.196 %` at `p = 1.69·10¹⁵` |
| V7 | `max{ g_k : p_k < 60 184 }` (used in Theorem 2, case 2) | **72**, at `p = 31 397`; `B(60 184) = 109.008 > 72` |
| V8 | sign change of `h(p) = p − 25(log p)³(log p − 1.1)` | `p* = 777 600.744…` |

**Sample values of `S(g)`** (§2.6): `S(100) = 3.88·10⁴`, `S(300) = 5.82·10⁷`,
`S(1000) = 9.43·10¹³`, `S(1132) = 7.12·10¹⁴`, `S(1476) = 8.43·10¹⁶`, `S(1550) = 2.18·10¹⁷`,
`S(1920) = 1.86·10¹⁹`.

**Scale disclaimer.** `2·10⁷` is **≈11.96 orders of magnitude** below `2⁶⁴`. This sieve verifies
the *lemmas*, not the *range*. It must never be cited as a verification of `F`.

---

## 5. What this document does NOT establish

Stated at length, because a document with the word "verified" in its title is exactly the one that
gets over-quoted downstream.

1. **`F` is not proved.** Theorem 2 proves `F` on a bounded initial segment. `F` is a statement
   about all `n`. A verified range of any finite size — `2⁶⁴`, `2⁶⁴⁰⁰⁰` — contributes **zero**
   to the general case. Card **L6** hazard 4 says the same and is right.
2. **`F` is not refuted**, and nothing here bears on which way it resolves. The `limsup`-scale
   tension between **L9/L10** (Cramér–Granville, heuristic) and **L3** (`F ⟹ limsup ≤ 1`) is
   untouched by a finite computation.
3. **This leg did not verify `F` to `2⁶⁴`.** It enumerated to `2·10⁷`. Corollary 2.1 is an
   implication whose hypothesis (H2) — a complete first-occurrence gap table below `2⁶⁴` — is
   **not** discharged in this run and rests on `oliveira2014goldbach`, tier **L2_weak,
   NOT OPENED** (AMS returned HTTP 403; ledger §6.2). **If that table is incomplete, Corollary 2.1
   says nothing.** This is the single largest dependency of the verified-range claim and it is the
   one nobody in this run has read.
4. **"Unconditional" means "no unproved hypothesis", not "no computation".** Proposition 4 proves
   the computation cannot be removed. Any sentence of the form "`F` is unconditionally true below
   `X`" must, to be honest, carry the table with it.
5. **The `2⁶⁴` figure is not this leg's.** It is quoted from **L6** at tier L0 and inherits **L6**
   hazard 1: three frontier figures circulate (`4·10¹⁸`, `10¹⁹`, `2⁶⁴`) and must never be quoted
   against the wrong citation.
6. **Theorem 2 is not new mathematics.** It is a from-first-principles reconstruction of the
   method card **L6** attributes to `kourbatov2015verification` §3–§4. What is new *here* is
   (i) the explicit constant chain resting on **one** L0-verified inequality rather than the
   unopened Axler corollaries, (ii) the observation that the argument is independent of P6′
   (§2.5), and (iii) the Reading (B) window and its closure (§3). Claiming more would be a
   citation failure, not a mathematical one.

---

## 6. Declared gaps

| # | Gap | Severity | Where it bites |
|---|---|---|---|
| G1 | **Lemma 2 (Dusart Thm 6.9 eq. 6.6) was not read from the source by this leg.** It is taken at tier L0 from card **T1** / the ledger, and re-verified numerically on `[60 184, 2·10⁷]` only. If the constant `1.1` or the range `x ≥ 60 184` is mis-transcribed upstream, Lemma 3 and everything above it moves. | **MAJOR** — but the numerical check at 1.27 M primes would have caught a wrong constant, and the independent agreement `1918` vs Kourbatov's `1920` (§2.7) would have caught a wrong range. | §2.3, §2.4 |
| G2 | **(H2) — the first-occurrence gap table below `2⁶⁴` — is not verified in this run.** `oliveira2014goldbach` unopened. | **BLOCKER for Corollary 2.1** (not for Theorem 2, which is an implication). | §2.7, §5.3 |
| G3 | **Dusart Prop. 6.8 was likewise not read from the source** (tier L0 via **T1**). Proposition 3's window depends on the constant `25` and the range `x ≥ 396 738`. | MINOR — Proposition 3 is a curiosity, not load-bearing; Proposition 4 (the obstruction) survives any constant. | §3 |
| G4 | **`h' > 0` on `[4·10⁵, ∞)` in Proposition 3 is asserted with a one-line derivative computation, not a formal proof of the uniqueness of the sign change.** The bisection in §4 V8 assumes unimodality. | MINOR — the interval endpoints are what matter and both are checked directly. | §3.2 |
| G5 | **Theorem 2 case 2 uses `max{g_k : p_k < 60 184} = 52`, a sieve fact of this leg.** It is exact integer arithmetic over 6 076 gaps and independently re-derivable in seconds, but it is a computation inside the *statement's proof*, not inside its hypotheses. A Lean formalization must carry it as a lemma. | MINOR | §2.6 |
| G6 | **The floating-point checks V1b/V2 are double precision.** V1a (the base case) is exact integer arithmetic; V2's tightest slack is `+0.08`, which is `~10¹²` ulps clear of zero at that magnitude, so no result here is precision-limited — but the sieve is not interval arithmetic and does not claim to be (card **T2**). | MINOR | §4 |
| G7 | **Strict vs non-strict in Lemma 1** is handled by using `<` throughout rather than by proving `T_n ∉ ℤ`. If a downstream leg needs `g_n ≤ T_n ⟹ g_n < T_n`, that irrationality argument is **not** supplied here. | MINOR | §2.2 |

---

## 7. Lean 4 / Mathlib facing statement

Offered for the `lean-skeleton` / `lean-probe` legs; **not compiled by this leg** (no Lean
toolchain was invoked). Indexing follows card **D1** correction #1: Mathlib's `Nat.nth` is
**0-indexed**, so `p n` below is `Nat.nth Nat.Prime (n-1)` for the run's 1-indexed `p_n`, and the
statement must quantify from `n = 1`.

```lean
-- p n  =  the n-th prime, 1-indexed:  p 1 = 2
noncomputable def p (n : ℕ) : ℕ := Nat.nth Nat.Prime (n - 1)

def Firoozbakht : Prop := ∀ n : ℕ, 1 ≤ n → (p (n+1))^n < (p n)^(n+1)

-- the bar (D5) and the explicit floor (Lemma 3)
noncomputable def T (n : ℕ) : ℝ := (p n : ℝ) * (Real.exp (Real.log (p n) / n) - 1)
noncomputable def B (x : ℝ)   : ℝ := (Real.log x)^2 - 1.1 * Real.log x

-- Lemma 2 — CITED, must enter as a hypothesis (not in Mathlib):
--   dusart : ∀ x : ℝ, 60184 ≤ x → (π x : ℝ) ≤ x / (Real.log x - 1.1)

theorem lemma3 (dusart : ∀ x : ℝ, 60184 ≤ x → (Nat.primeCounting ⌊x⌋₊ : ℝ)
                                              ≤ x / (Real.log x - 1.1))
    (n : ℕ) (hn : 60184 ≤ p n) : B (p n) < T n := sorry

theorem lemma4 : StrictMonoOn B (Set.Ici (2 : ℝ)) := sorry

-- Theorem 2, as an implication with its finite hypotheses explicit
theorem verified_range
    (X : ℕ) (hX : 60184 ≤ X)
    (H1 : ∀ n, 1 ≤ n → p n < 60184 → (p (n+1))^n < (p n)^(n+1))
    (H3 : ∀ n, 1 ≤ n → 60184 ≤ p n → p n ≤ X →
            ((p (n+1) - p n : ℝ)) ≤ B (firstOccurrence (p (n+1) - p n)))
    : ∀ n, 1 ≤ n → p n ≤ X → (p (n+1))^n < (p n)^(n+1) := sorry
```

**Effort assessment, honestly.** `lemma4` is a two-line `Mathlib` derivative argument. `lemma3` is
an easy consequence *once* Dusart is available as a hypothesis — and Dusart is **not** in Mathlib,
so it must be axiomatized and **declared as an axiom in any paper that quotes the result**.
`verified_range` is bookkeeping. `H1` is the real obstacle: `Nat.nth Nat.Prime` is
**`noncomputable`** (card **T4**, ledger §4.7), so `decide` cannot produce `p n` at all; the base
case must be supplied as 6 076 prime literals with `Nat.Prime` certificates plus a
"no prime strictly between" lemma for each consecutive pair. That is a `lean-probe` sizing
question, and this leg does **not** claim it is feasible at `X₀ = 60 184`.

**And `X₀` cannot be traded away.** Lowering it is forbidden by Lemma 2's validity range
(`x ≥ 60 184`); raising it only enlarges the base case. So the base case is fixed at 6 076
consecutive-prime pairs and must be discharged by a reflection tactic over a certified prime list
rather than by `decide`. **This is the single open engineering question the Lean legs inherit from
target #2**, and it is engineering, not mathematics.

---

## 8. Verdict

| Item | Verdict |
|---|---|
| **Target #2, Reading (A)** — an unconditional theorem taking a finite gap table to `F` on `[1, X]` | **PROVED** (Theorem 2, §2.6), constants explicit, one cited inequality, independent of P6′ |
| **Target #2, Reading (B)** — a range with no computational input | **PROVED for `396 738 ≤ p ≤ 777 600`; PROVED IMPOSSIBLE beyond** (Props 3 and 4, §3) |
| **`F` at the published frontier `2⁶⁴`** | **CONDITIONAL** on an unopened gap table (G2). Not established by this run. |
| **`F` itself** | **OPEN.** Untouched. Not proved, not refuted, and §3.3 explains why this line of attack cannot touch it. |

**The defensible sentence this leg supports**, in the register card INDEX §6 requires:

> *There is a clean, unconditional theorem that converts a table of first-occurrence prime gaps
> into a proof that Firoozbakht's inequality holds up to that table's reach — it needs exactly one
> explicit estimate on `π(x)`, it does not need the open maximal-gap lemma, and it can never be
> made to work without the table.*

---

*Emitted by leg `proof-attempt` (target #2), molecule `task-20260725-909e`, run
`germ-20260725-791a7c45`. The conjecture remains **OPEN**; a target reaches `proved` only through
the kernel/Lean leg downstream.*
