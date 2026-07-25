# T4 — Technique: the Lean 4 / Mathlib formalization substrate

**Kind:** technique (what the formal backend can and cannot do)
**Verdict:** **PROVEN** on the two facts that matter (`Nat.nth` is `noncomputable`; the prime-`nth`
API is five base lemmas). Both read at L0 documentation locators. **Everything else about the
toolchain is unverified** — names drift and no pinned-toolchain check was run.
**Rests on:**
- `mathlib_nat_nth` (L0), fetched 2026-07-25 — `noncomputable def Nat.nth (p : ℕ → Prop) (n : ℕ) : ℕ`;
  `Nat.nth_lt_nth`; `Nat.count_nth`; `Nat.nth_count`.
- `mathlib_nat_prime_nth` (L0), fetched 2026-07-25 — the module contains **exactly five**
  `@[simp]` lemmas: `nth_prime_zero_eq_two`, `..._one_eq_three`, `..._two_eq_five`,
  `..._three_eq_seven`, `..._four_eq_eleven`.

---

## Two hard facts

### Fact 1 — `Nat.nth` is `noncomputable`

`decompose` §5.2 says `Nat.nth Nat.Prime n` "is not efficiently kernel-reducible", so `decide`
stalls on *producing* `p_n`. **The situation is stronger than inefficiency: there is no kernel
reduction at all.** The proposed workaround — prime literals + `Nat.Prime` certificates + an
explicit "no prime strictly between" lemma + `norm_num` — is therefore not merely faster, it is
**mandatory**. And the fix needs `Nat.count ↔ Nat.nth` bridging lemmas that the document does not
budget for, with per-`n` cost linear in `p_N`, not in `N`.
(`source-ledger.md` §2.7, §4.7; `synthesis.md` §4.5.)

### Fact 2 — the prime-specific `nth` API is five base cases and nothing else

No `p_n` growth bound, no `π`/`nth` bridge specialised to primes, no gap lemmas. **Any Lean leg
must budget for building that scaffolding itself.** `decompose` §6's "honest expectation" is, if
anything, generous. (`source-ledger.md` §2.7.)

## The off-by-one — the highest-severity defect in the run

See **D1**. Mathlib is **0-indexed** (`nth Prime 0 = 2`); this attack is **1-indexed**. The
statement `∀ n ≥ 1, (nth Prime (n+1))^n < (nth Prime n)^(n+1)` formalizes
`p_{m+1}^{m−1} < p_m^{m}` — a **strictly weaker** conjecture that additionally drops `m = 1`.
**Fix once, in the statement file.** Every literature threshold (`k > 9`, `n ≥ 10`, `n ≥ 5`,
`n > 4`, `n ≥ 3645`) is 1-indexed and shifts with it.

## Node plan, with the priority the panel corrected

| Node | Content | Verdict |
|---|---|---|
| **N1 Statement** | `p n := Nat.nth Nat.Prime (n−1)`; `F := ∀ n ≥ 1, (p (n+1))^n < (p n)^(n+1)`. Arithmetic only — no `rpow`, no `log`. | **Anchor. Get the index right or nothing downstream means anything.** |
| **N2 Equivalence** | F3 ⟺ F2 ⟺ F1 (**L1**), via `Real.log`/`Real.rpow` monotonicity. | **Promote to primary.** §6's own value proposition names it. |
| **N3 Finite check** | `∀ n, 1 ≤ n ≤ N → …` by literals + certificates + `norm_num`. | Low effort, small `N`. **`N` must be sized by probe, not guessed** — and it is limited by Fact 1, not by integer size (`p_51^52` has 124 digits). |
| **N4 Smooth model** | **L14**. | Keep, **demote from "primary"**, rebill: it is the only content independent of `F`'s truth. |
| **N5 Gap reformulation** | `F ↔ ∀n, g n < T n` (**L1** F4). | **Promote to primary** (it pins the object every leg reasons about) — **and it is the highest-risk node**, because it re-imports `Real.exp` and the index into a statement N1 was designed to keep in ℕ. Size by probe. |
| **N6 Corollary** | `F → limsup g_n/log²p_n ≤ 1` (**L3**). | High effort; needs **T1** as an explicit hypothesis. Declare the hypothesis openly. |

`decompose` §6 made N4 the primary deliverable on the grounds that it is "the only genuine
theorem". **Unanimously rejected by the panel** — N2, N5 and N6 are theorems, and N4 contains no
primes and has no consumer (**L14** hazards 1–2). (`synthesis.md` §2 C4, §3 D4.)

## Role in the proof-obligation tree

Lean **cannot decide this conjecture.** Its value is (i) an unambiguous statement, (ii) a
machine-checked equivalence chain so no leg silently uses a wrong reformulation, and (iii) N4 as
`F`-independent mathematics. Any leg reporting "Lean progress on Firoozbakht" must say which node
it means.

## Dependencies

**D1**, **D4**, **D5**, **L1**, **L3**, **L14**, **L16** (why N3 is expensive), **T1**, **T3**.

## Used by

Nothing downstream — Lean is a leaf of this attack, by design.

## Hazards

1. **The ledger's Lean rows are documentation snapshots, not a pinned-toolchain check** (fetched
   2026-07-25). Names drift. A probe leg must re-confirm against the toolchain actually pinned.
   (`source-ledger.md` §6.10.)
2. `Nat.nth_lt_nth` needs an `Infinite` hypothesis — `Nat.infinite_setOf_prime` must be threaded
   through. (`source-ledger.md` §2.7.)
3. `Nat.bertrand` is named in `decompose` §6 and was **not** confirmed in the ledger. See **L17**
   — it is useless for `F` anyway.
4. **PNT with error terms is not assumed available in Mathlib.** If N6 needs it, it must come from
   the PNT+ development or be axiomatized as an explicit, flagged hypothesis.

## Declared gap

No toolchain was probed in this run. Every effort estimate above is by analogy, not measurement —
including N5's, which is the one the panel singled out as unjustified.
