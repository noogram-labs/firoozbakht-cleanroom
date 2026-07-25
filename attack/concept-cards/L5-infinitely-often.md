# L5 — Unconditional: the Firoozbakht inequality holds for infinitely many `n`

**Kind:** theorem (published, **unconditional**)
**Verdict:** **PROVEN.** Read at the locator, proof given in full in the source.
**Rests on:** `ferreira2017consequences` (L0) **Theorem 5.2**, verbatim: *"There are infinitely
many `n ∈ N` such that `ⁿ√p_n > ⁿ⁺¹√p_{n+1}`."* Proof given in full, "(Following [12])" =
Ferreira's 2016 USP PhD thesis. It consumes `ferreira2017consequences` **Theorem 5.1**
(attributed to Zhang: `liminf g_n < ∞`, *Ann. of Math.* **179** (2014), 1121–1174).

---

## Statement

```
#{ n ≥ 1 : p_{n+1}^{1/(n+1)} < p_n^{1/n} }  =  ∞
```

unconditionally — no hypothesis, no `n₀`.

## Proof sketch (as given in the source)

Bounded gaps (Zhang) supplies infinitely many `n` with `g_n ≤ B` for a fixed `B`. At such an `n`,
the threshold `T_n ≈ log²p_n − log p_n − 1` grows without bound while `g_n` stays `≤ B`, so
`g_n < T_n` holds at all but finitely many of them. By **L1**, that is the Firoozbakht inequality.

## Role in the proof-obligation tree

**This is the only unconditional theorem in the entire source ledger that says something positive
about the conjecture itself.** Everything else on the proof side is either a finite verification
(**L6**), a conditional criterion (**L4**), or a consequence (**L3**). The `decompose` leg did not
have it. It belongs in the final paper.

## Dependencies

**D4**, **L1**, **L2** (for the growth of `T_n`), and Zhang's bounded-gaps theorem.

## Used by

The framing of the paper's "what is actually known" section. It is not consumed by any other card
— which is itself worth noticing: it is a genuine theorem with no downstream leverage.

## Hazards

1. **"Infinitely often" is not "eventually".** The statement is fully compatible with infinitely
   many *failures*. It does not say `F` holds for large `n`, and it does not shrink the space
   where a counterexample can live by a single index. Do not let it drift.
   (`source-ledger.md` §4.5, §2.5.)
2. The proof is Ferreira's own, following his thesis; Zhang is the only external input and is
   itself cited rather than read in this run. The theorem statement is at L0; Zhang's is at
   attribution level.
3. Note the direction of the inequality in the source: `ⁿ√p_n > ⁿ⁺¹√p_{n+1}` is `F1` written
   right-to-left. Same statement.

## Declared gap

Zhang (2014) was not fetched in this run. It is universally known and not in dispute, but the
ledger has no row for it — the only external theorem this card consumes is cited at second hand
through `ferreira2017consequences` ref. [20]. **Flagged: if the paper states L5, it should carry a
Zhang row.**
