# Lean probe — round 2 report

**Molecule:** `task-20260726-8ba0` (leg `lean-probe`, RE-ATTACK round 2)
**Parent loop:** `reattack-20260726-57d1` (formula `converge-math-attack`, `rounds = 2`)
**Date:** 2026-07-26 · **Backend: `lean`** — not skipped.
**Round-1 input read in full:** `attack/lean-probe-report.md` (279 lines, molecule
`task-20260725-9975`).

---

## 0. Headline — the verdict, stated once

> **`Firoozbakht.firoozbakht : Conjecture` — UNPROVABLE_IN_BUDGET.**
> No proof was found. This is **not** a claim that the conjecture is false, and
> not a claim that it is unprovable in principle. It is the honest statement that
> this leg, with this substrate and this budget, did not produce a proof term the
> kernel accepts.

The conjecture has been open since 1982. `UNPROVABLE_IN_BUDGET` was the expected
outcome and is the reported outcome. Nothing was weakened, no axiom was added, no
`native_decide` was used, and the statement file was not touched.

**What round 2 does add** is a machine-checked account of *why* the substrate
cannot reach the target — `lean/Firoozbakht/Barrier.lean`, three `sorry`-free
theorems (§3). "No proof was found" is now backed by a theorem about the tools,
not only by a paragraph.

---

## 1. The gates, verbatim

```
$ lake exe cache get       # Mathlib v4.29.0 from the shared cache      → exit 0
$ lake build                                                            → exit 0
warning: Firoozbakht/Statement.lean:185:8: declaration uses `sorry`
Build completed successfully (2208 jobs).
$ lake env lean audit.lean                                              → exit 0
$ lake env lean audit_exhaustive.lean                                   → exit 0
declarations scanned: 63
depending on sorryAx: [Firoozbakht.firoozbakht]
```

| gate | result |
|---|---|
| `lake build` exit code | **0** |
| build warnings | **1** — `Statement.lean:185`, the open target, nothing else |
| `lake env lean audit.lean` exit code | **0** |
| `lake env lean audit_exhaustive.lean` exit code | **0** |
| declarations scanned (exhaustive audit) | **63** (was 60; +3 barrier theorems) |
| declarations depending on `sorryAx` | **1** — `Firoozbakht.firoozbakht` |
| live `sorry` tokens in `.lean` sources | **1** — `Statement.lean:186` |
| `native_decide` / `axiom` / `@[implemented_by]` / `unsafe` | **none** — only prose mentions in docstrings (`Statement.lean:61`, `Equivalence.lean:18`, `Barrier.lean:12`) |
| PROVED bar (`exit 0` **and** grep-clean of `sorry`) | **NOT MET** — one `sorry` remains, by design |

- Toolchain `leanprover/lean4:v4.29.0`; Mathlib tag `v4.29.0`, rev
  `8a178386ffc0f5fef0b77738bb5449d50efeea95` — `lean-toolchain` and
  `lake-manifest.json` unchanged from round 1.

### The frozen anchor — diff-verified before and after

`Firoozbakht/Statement.lean` was hashed before the leg began and again after
every edit:

```
$ shasum -a 256 Firoozbakht/Statement.lean     # before AND after
6528868823c0637dd182c914e2ef43a7455f851335cafaba6cee934802e004c1
$ diff Statement.before.lean Firoozbakht/Statement.lean
   → no output (byte-identical, not merely signature-identical)
```

Round 1 could only claim *signature*-identity (it edited a docstring). Round 2
claims the stronger property: **not one byte of the fidelity anchor changed.**
`lean-toolchain` and `lake-manifest.json` are likewise untouched.

### The audit detector was re-tested against a planted failure

An audit that cannot fail is worth nothing, and the audit now scans a larger
tree than the one round 1 tested it on. So the self-test was re-run:

```
theorem planted_sorry_selftest : (1:Nat) = 1 := by sorry   -- added to Barrier.lean
$ lake env lean audit_exhaustive.lean
declarations scanned: 64
depending on sorryAx: [Firoozbakht.firoozbakht, Firoozbakht.planted_sorry_selftest]
```

The plant was then deleted; the tree returns to `scanned: 63`, one name. It is
not in the committed sources.

---

## 2. What was actually attempted, and what Lean said

Every route below was *run*, not reasoned about. The failures are Lean's own
words, reproduced from a scratch file (`probe_attempt.lean`, deleted before the
leg closed — it was never part of the `Firoozbakht` library target).

| # | Route | Outcome |
|---|---|---|
| A1 | `exact?` on `⊢ p (n+1) ^ n < p n ^ (n+1)` | `` `exact?` could not close the goal. Try `apply?` to see partial suggestions. `` |
| A2 | `aesop` on the same goal | `` tactic 'aesop' failed, made no progress `` |
| A3 | `decide` on the single instance `F3 1` | `` Tactic `decide` failed … reduction got stuck at the `Decidable` instance `` |
| B | Bertrand's postulate — the strongest prime-gap bound in Mathlib | **available and provable, but provably too weak at every `n ≥ 2`** (§3) |
| C | Sharper gap bounds (BHP `p^0.525`, RH-conditional `√p log p`, Cramér `(log p)²`) | **not in Mathlib at all** — no formalization to invoke (§4) |

A3 is worth keeping: it is card `T4` Fact 1 turning up as a live error rather
than a documentation claim. `Nat.nth` is `noncomputable`, so there is no kernel
reduction — `decide` cannot evaluate `p 1` even at the smallest index. The
substrate cannot brute-force even one case, let alone all of them.

---

## 3. The barrier — new, `sorry`-free, in the tree

`lean/Firoozbakht/Barrier.lean` (new file; `Statement.lean` untouched). Three
theorems, all `[propext, Classical.choice, Quot.sound]` in the audit:

| Theorem | Statement |
|---|---|
| `bertrand_gap (n) (1 ≤ n)` | `p (n+1) ≤ 2 * p n` — Bertrand, ported to this development's **1-indexed** `p` |
| `p_lt_two_pow (n) (2 ≤ n)` | `p n < 2 ^ n` — induction on `bertrand_gap`, base `p 2 = 3 < 4` |
| `bertrand_ceiling_above_threshold (n) (2 ≤ n)` | `(p n : ℝ) ^ (1 + 1/n) < 2 * (p n : ℝ)` |

**Read the third one carefully — the direction of the inequality is the point.**
Firoozbakht in Kourbatov's form (`F1'`) needs `p_{n+1} < p_n ^ (1 + 1/n)`.
Bertrand supplies `p_{n+1} ≤ 2 p_n`. For Bertrand to certify `F1' n`, its ceiling
would have to sit *below* the threshold. The theorem proves it sits strictly
*above* it, **at every `n ≥ 2`**. So the route is closed at every index but the
first — not "hard", *closed* — and that is now a kernel-checked fact rather than
an impression.

The mechanism, in one line: Bertrand supplies a constant multiplicative slack
`2`, while the threshold's slack `p_n ^ (1/n) = exp((log p_n)/n)` tends to `1`.
Certification would need `2 ^ n ≤ p_n`; the primes grow like `n log n`, so
`p_n < 2 ^ n` for every `n ≥ 2` — which is `p_lt_two_pow`, itself proven *from*
Bertrand. The best available tool proves its own insufficiency.

This is a **negative-capability** result. It says nothing about whether
Firoozbakht is true. It says the one prime-gap input Mathlib carries cannot
decide it.

---

## 4. Why no sharper route was available — named, not waved at

The gap form (`F4`, `conjecture_iff_gap`, already kernel-checked in round 1) is
`g_n < T_n`, and `T_n = p_n^{1+1/n} - p_n ≈ (log p_n)²`. So Firoozbakht is a
Cramér-strength prime-gap bound. What exists, and what it would give:

| Bound | Slack it certifies | Enough? | In Mathlib? |
|---|---|---|---|
| Bertrand `p_{n+1} ≤ 2 p_n` | constant `2` | **no** — §3, at every `n ≥ 2` | **yes** (the only one) |
| Baker–Harman–Pintz `g_n ≪ p^{0.525}` | `1 + p^{-0.475}` | no — needed slack is `≈ (log p)²/p`, smaller by a power | **no** |
| RH-conditional `g_n ≤ (22/25)√p log p` (CMS) | `1 + log p/√p` | no | **no** |
| Cramér `g_n = O((log p)²)` | right order | would be enough with the right constant — but is itself conjectural | **no** |

The "enough?" column is asymptotic, and the crossover was computed rather than
asserted (`sympy`, exact primes; needed slack `p_n^{1/n} - 1`):

| `n` | `p_n` | needed slack | BHP slack `p^{-0.475}` | RH slack `log p/√p` |
|---|---|---|---|---|
| 100 | 541 | 0.06496 | 0.05032 | 0.2706 |
| **245** | **1553** | **0.03045** | **0.03049** | — |
| 1 000 | 7919 | 0.00902 | 0.01407 | 0.1009 |
| 100 000 | 1 299 709 | 0.000141 | 0.001247 | 0.01235 |

So BHP's slack overtakes what is needed from `n = 245` on, and RH's from `n = 3`
on — both are insufficient exactly where it matters (all large `n`), and the
tables' "no" is a statement about the tail, not about every index. The same run
confirms `T_n ≈ (log p_n)²` to within ~10% across `n = 10 … 10⁵`
(`n = 10⁵`: `T = 182.98`, `(log p)² = 198.18`).

The two middle rows are examined on paper by this round's sibling legs and found
insufficient there too — `proof-attempt-RH-conditional-bound.md` Theorems B and C
refute (1b) and (1c): no `C·p^θ(log p)^A` envelope with `θ > 0`, and no
`C√p log p` envelope, certifies Firoozbakht beyond finitely many `n`. That is an
independent, paper-side confirmation that the missing input is not "a sharper
version of an existing Mathlib lemma" but a Cramér-strength theorem nobody has.

**So the honest ordering is:** the obstruction is mathematical first and
formalization-budget second. Even a perfect formalization of every published
unconditional *and* RH-conditional prime-gap bound would not discharge this
`sorry`.

---

## 5. What this leg changed

| File | Change |
|---|---|
| `lean/Firoozbakht/Statement.lean` | **nothing — byte-identical**, SHA-256 verified before and after |
| `lean/Firoozbakht/Barrier.lean` | **new** — `bertrand_gap`, `p_lt_two_pow`, `bertrand_ceiling_above_threshold`; no `sorry`, no `axiom` |
| `lean/Firoozbakht.lean` | one added import line (`Firoozbakht.Barrier`) |
| `lean/audit.lean` | three added `#print axioms` lines for the barrier theorems |
| `attack-round-2/verify-lean-probe-round2.py` (+ `.out.txt`) | **new** — the §4 numerics, self-contained, exit 0 |
| `lean/STATUS.md` | updated to the post-round-2 state (build job count, audit count 60 → 63, the barrier, the frozen-anchor hash) |
| `lean/Firoozbakht/Equivalence.lean`, `FiniteCheck.lean`, `lean-toolchain`, `lake-manifest.json`, `audit_exhaustive.lean` | untouched |

The scratch file `probe_attempt.lean` (where routes A1–A3 and the first drafts of
the barrier were run) was **deleted**; it was never in the library target and is
not committed.

---

## 6. Gaps and honesty notes

- **The barrier is about Bertrand, not about all of mathematics.** It proves one
  named route closed. Routes through bounds Mathlib lacks are argued closed in §4
  by citing this round's paper legs, at their tier — *not* re-derived in Lean here.
- **`F3_iff_F2` and friends were not re-verified** by this leg; they were
  kernel-green in round 1 and the build replays them unchanged.
- **The verified finite range is still `n ≤ 4`.** Card `T4` Fact 1 (no kernel
  reduction for `Nat.nth`) is unchanged, and A3 above is a live demonstration of
  it. Reporting a larger `N` would be a fabrication.
- **`p_lt_two_pow` is not new mathematics.** It is a two-line induction that any
  number theorist would call obvious. Its value here is that it makes the
  insufficiency of Bertrand *machine-checked* rather than asserted.
- **The `sorry` count is 1 and stayed 1.** Round 1 took 5 → 1. Round 2 takes
  1 → 1. That is the honest state of an open problem, and the loop's convergence
  test should read it as **kernel: UNPROVABLE_IN_BUDGET, not PROVED.**

---

## 7. Verification pass (step 2) — what was re-checked, and what it changed

The artifact was re-audited against its own brief. Four claims were load-bearing
and, in the first draft, asserted rather than tested.

**1. "The build is green" could have been a stale replay.** `lake build` replays
cached olean files, so a green line proves nothing about the sources. **Checked**
— `.lake/build/lib/lean/Firoozbakht*` was deleted and the four modules rebuilt
from source: exit 0, `Built Firoozbakht.Barrier (4.4s)`, same single warning at
`Statement.lean:185`.

**2. "`T_n ≈ (log p_n)²`" and the slack comparison in §4.** Asserted from the
asymptotics. **Checked** — `verify-lean-probe-round2.py` (in this directory,
exit 0, output in `verify-lean-probe-round2.out.txt`) computes both against exact
primes. `T_n` tracks `(log p_n)²` to within ~10% over `n = 10 … 10⁵`.

**3. The §4 table said "no" without saying "no, where".** That is the same
mistake round 1's sibling leg was faulted for (F4: *"at no other index
whatsoever"*, false as stated). **Fixed** — the crossovers are now computed and
printed: BHP's slack overtakes the needed slack at `n = 245`, RH's at `n = 3`.
Both envelopes are insufficient **for all large `n`**, which is the honest claim;
"insufficient at every index" would have been false.

**4. "`refuted_of_witness` is proven" (claimed in `unproved.md`).** Carried
forward from round 1's report rather than observed. **Checked** —
`lake env lean audit.lean` prints
`'Firoozbakht.refuted_of_witness' depends on axioms: [propext, Classical.choice, Quot.sound]`.

One smaller correction: the scratch file's first draft of `bertrand_gap` claimed
the strict `p_{n+1} < 2 * p_n`. Bertrand gives a prime in `(m, 2m]` — non-strict
— and `omega` refused the strict form. The theorem is stated with `≤`, which is
what the source supports and what the barrier needs. The strict version is true
(`2 p_n` is even and `> 2`, hence composite) but is not proven here and is not
claimed.

---

## 8. Reproduce

```
cd lean
lake exe cache get
lake build                        # exit 0, one warning: Statement.lean:185
lake env lean audit.lean          # exit 0
lake env lean audit_exhaustive.lean
                                  # declarations scanned: 63
                                  # depending on sorryAx: [Firoozbakht.firoozbakht]
shasum -a 256 Firoozbakht/Statement.lean
                                  # 6528868823c0637dd182c914e2ef43a7455f851335cafaba6cee934802e004c1
```

```
cd .cosmon/.../attack-round-2
python3 verify-lean-probe-round2.py     # the §4 numerics, exit 0
```

The LLM emitted proof terms only. `lake build` was the sole verdict.
