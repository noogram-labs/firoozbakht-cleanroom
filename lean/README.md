# Firoozbakht's conjecture — Lean 4 skeleton

The **fidelity anchor** of the formal leg. Its job is to say, unambiguously and
machine-checkably, *what is being attacked* — so that no downstream leg can go
green having formalized a different conjecture.

## The statement

```lean
noncomputable def p (n : ℕ) : ℕ := Nat.nth Nat.Prime (n - 1)   -- 1-indexed: p 1 = 2

def F3 (n : ℕ) : Prop := (p (n + 1)) ^ n < (p n) ^ (n + 1)

def Conjecture : Prop := ∀ n : ℕ, 1 ≤ n → F3 n

theorem firoozbakht : Conjecture := by sorry     -- OPEN
```

Four equivalent forms are stated (`F1` real-analytic as posed, `F1'` Kourbatov's,
`F2` logarithmic, `F3` arithmetic, `F4` gap form `g_n < T_n`); `F3` is primary
because it is a statement about natural numbers only.

## Why the `- 1` is the whole point

The literature is **1-indexed** (`p_1 = 2`); Mathlib is **0-indexed**
(`Nat.nth Nat.Prime 0 = 2`). Writing the conjecture directly against
`Nat.nth Nat.Prime n` produces `p_{m+1}^{m-1} < p_m^m` — an exponent ratio of
`1 + 1/(m-1)` where Firoozbakht needs `1 + 1/m` — which is **strictly weaker**,
and silently drops the case `m = 1`.

The two families cannot be told apart by truth value: every case of both holds
in any range anyone can check. `FiniteCheck.lean` therefore pins both to their
numerals so the difference is visible and kernel-checked.

## Layout

| File | Card | Contents |
|---|---|---|
| `Firoozbakht/Statement.lean` | `D1 D2 D4 D5` | the anchor: `p`, `g`, `L`, `T`, `F1`–`F4`, `Conjecture`, the open target |
| `Firoozbakht/Equivalence.lean` | `L1` | the equivalence chain `F1 ↔ F1' ↔ F2 ↔ F3 ↔ F4` |
| `Firoozbakht/FiniteCheck.lean` | `D1 T4` | indexing fidelity checks + `Conjecture` for `1 ≤ n ≤ 4` |
| `audit.lean` | — | `#print axioms` for every declaration |
| `STATUS.md` | — | build result, axiom audit, every `sorry` justified, non-deliveries |

## Build

```
lake exe cache get     # Mathlib v4.29.0 from the shared cache
lake build             # green; warnings are the five declared sorries only
lake env lean audit.lean
```

See `STATUS.md` for the honest report: what is proven, what is `sorry`-ed and
why, and what this leg deliberately did **not** deliver.
