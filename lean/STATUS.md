# Lean skeleton — status

Leg: `lean-skeleton` (kernel-engineer), molecule `task-20260725-5fd9`,
germ `germ-20260725-791a7c45`. Backend: **lean** (not skipped).

## Build

```
$ lake build
Build completed successfully (1984 jobs).
```

- Toolchain: `leanprover/lean4:v4.29.0` (pinned in `lean-toolchain`).
- Mathlib: `leanprover-community/mathlib4` tag `v4.29.0`,
  rev `8a178386ffc0f5fef0b77738bb5449d50efeea95` (pinned in `lake-manifest.json`).
- The build is **green with warnings only** — the warnings are the five declared
  `sorry`s listed below and nothing else.

This closes card `T4` hazard 1, which flagged that the run's Lean facts were
documentation snapshots rather than a pinned-toolchain check. They are now a
pinned-toolchain check: `Nat.nth`, `Nat.nth_lt_nth`, `Nat.nth_mem_of_infinite`,
`Nat.infinite_setOf_prime` and the five `nth_prime_*` base lemmas all resolved
against the toolchain above.

## Axiom audit

`lake env lean audit.lean` prints the dependency of each declaration. Reproduced
verbatim:

| Declaration | `sorryAx`? |
|---|---|
| `p_one`, `p_five`, `p_succ` | no |
| `prime_p`, `p_lt_p_succ` | no |
| `refuted_of_witness` | no |
| `cast_g` | no |
| `p_pow_ne`, `strict_iff_nonstrict` | no |
| `F3_one`, `F3_four`, `firoozbakht_le_four` | no |
| `firoozbakht` | **yes** — the open target |
| `F3_iff_F2`, `F1_iff_F3`, `F2_iff_F1'`, `F1'_iff_F4` | **yes** — L1 steps, skeleton |
| `conjecture_iff_real`, `conjecture_iff_gap` | **yes** — inherited from the four above |

Everything else is `[propext, Classical.choice, Quot.sound]` only.

## The five `sorry`s, and why each is there

| # | Declaration | File:line | Status |
|---|---|---|---|
| 1 | `firoozbakht : Conjecture` | `Statement.lean:182` | **Open problem.** This is the point. Never to be discharged by anything but mathematics. |
| 2 | `F3_iff_F2` | `Equivalence.lean:28` | Card `L1`, PROVEN on paper; Lean proof is `Real.log` API work, budgeted to the proof leg (card `T4`, node N2). |
| 3 | `F1_iff_F3` | `Equivalence.lean:33` | idem, `Real.rpow` monotonicity. |
| 4 | `F2_iff_F1'` | `Equivalence.lean:37` | idem. |
| 5 | `F1'_iff_F4` | `Equivalence.lean:47` | idem — and card `T4` names this the **highest-risk node** (N5): it re-imports `rpow` and ℕ-subtraction into a statement the anchor keeps in ℕ. Its one ℕ-subtraction step, `cast_g`, is proven. |

Sorries 2–5 correspond to a card (`L1`) whose paper proof is complete and
corroborated at two L0 locators. They are *unformalized*, not *unproven*. Sorry 1
is genuinely unproven by anybody.

## What is actually proven here (no `sorry`)

- `p 1 = 2` … `p 5 = 11` — the 1-indexed sequence agrees with the paper convention.
- `prime_p : ∀ n, Nat.Prime (p n)`.
- `p_lt_p_succ : 1 ≤ n → p n < p (n+1)`.
- `p_succ : p (k+1) = Nat.nth Nat.Prime k` — the 0↔1 index bridge, in one place.
- `p_pow_ne` / `strict_iff_nonstrict` — Visser's `≤` form and Kourbatov's `<`
  form define the same conjecture, at every `n ≥ 1` (card `D4` hazard 1, which
  the cards asserted from unique factorisation; now machine-checked, via
  `p_{n+1} ∣ p_n^{n+1} → p_{n+1} = p_n`).
- `cast_g : 1 ≤ n → (g n : ℝ) = p (n+1) - p n` — truncated subtraction is genuine.
- `refuted_of_witness` — the `Σ₁` refutation shape (card `L16`).
- `firoozbakht_le_four` — the conjecture holds for `1 ≤ n ≤ 4`.

## Deliberate non-deliveries, stated plainly

**Verified range is `n ≤ 4`, not `n ≤ 10⁴`.** Card `T4` Fact 1: `Nat.nth` is
`noncomputable` and has *no* kernel reduction, so `decide` cannot produce `p n`;
card `T4` Fact 2: Mathlib's prime-specific `nth` API is exactly five `@[simp]`
base lemmas, `nth Prime 0 = 2` through `nth Prime 4 = 11`. Four is therefore the
entire reach of this project without new machinery (`Nat.count`↔`Nat.nth`
bridging, cost linear in `p_N`). The limit is not integer size — `p_51^52` has
124 digits. Extending the range is a separate, budgeted leg; claiming a larger
`N` here would be a fabrication.

**Node N4 (the smooth model, card `L14`) is not formalized.** Out of scope for a
statement leg, and the panel demoted it from primary (card `T4`, node table).

**Node N6 (the `limsup` corollary, card `L3`) is not formalized.** It needs
effective `π(x)` bounds (card `T1`) which are not assumed present in Mathlib
(card `T4` hazard 4); it would have to enter as an explicit flagged hypothesis.

**`Nat.bertrand` was neither used nor confirmed.** Card `L17` establishes it is
useless for `F` anyway.

## The refutation branch is not a second `sorry`

Two contradictory `sorry`-ed theorems (`firoozbakht` and `not_firoozbakht`) in
one namespace would let any later file close any goal via
`absurd firoozbakht not_firoozbakht`, silently voiding every other proof in the
development. The refutation branch is therefore `def Refuted : Prop := ¬ Conjecture`
plus `refuted_of_witness`, which is **proven**.
