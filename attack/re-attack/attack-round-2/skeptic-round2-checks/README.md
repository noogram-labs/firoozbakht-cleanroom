# skeptic-round2-checks

Independent verification scripts for `attack-round-2/faults.md` (leg `skeptic`, round 2,
molecule `task-20260726-7211`).

Every script is written **from the statements** in the round-2 proof attempts, never from
their own scripts (`r2_*.py`, `verify-uvr-round2.py`, `probe_rh2.py` were not opened while
writing these). Self-contained: no network, no data files, `numpy` + `mpmath` only.

| script | what it checks |
|---|---|
| `chk_analytic.py` | all analytic constants: the four (A-high) bars, required `d` solved from Lemma W (never from a sufficient condition), Prop. R1's three certificates, C-a′/C-b′ cell-majorants and tails, Lemma A.1, `S(g)` / `S_K(g)` at `2⁶⁴`, Prop. 3's window, the F8 shortfall |
| `chk_sieve.py` | sieve to `2·10⁸`: witnesses W1/W2, maximal-gap record list, P6′-gov / P6′-min / P6′-rec margins and exception counts, the `T_{n+1} < T_n` fractions, small-branch gap constants, `S`-breaches, the RH `Theorem A°` table and `p*(C)` |
| `chk_more.py` | segmented sieve to `1.4·10⁹`: the `288 @ 1 294 268 491` constant of UVR §3.7 |
| `chk_pairs.py` | sieve to `3·10⁸`: P6′-pair violating **pairs** vs violating **indices** (R2-m2), `{n : T_n ≥ L_n²}`, step-count denominators (R2-M1) |
| `chk_bounds.py`* | Axler upper/lower rows, (D-low)/(D-high)/(A-high′)/(A-high\*) at every prime `< 10⁸`, `G₀`, `π(60 184)`, Lemma 3 slack |
| `chk_final.py` | per-decade P6′-min minima (R2-m7), the smallest Axler-upper counterexample, the record ordinal of `191 912 783` (R2-m1) |

`*` `chk_bounds.py` is included with its output.

**Source fetches** (for R2-B2 / R2-B3), MD5-verified against `proof-attempt-first-failure-maximality.md` §7.1:

```
arXiv:1409.1780v3            f4cde1df54cf3d6987c1ece2f7b0ebeb
Integers 16 (2016) #A22      29a92c5e7cacb5269e4d7be68ac939bf
Corrigendum (18 Jan 2018)    4817ba687df1c16d163c94e29b55d1c4
```

**Lean gates re-executed** (not read): `lake exe cache get` → 0; `lake build` → 0,
`Build completed successfully (2208 jobs)`; `lake env lean audit_exhaustive.lean` → 0,
`declarations scanned: 63`, `depending on sorryAx: [Firoozbakht.firoozbakht]`;
`shasum -a 256 lean/Firoozbakht/Statement.lean` =
`6528868823c0637dd182c914e2ef43a7455f851335cafaba6cee934802e004c1`.
