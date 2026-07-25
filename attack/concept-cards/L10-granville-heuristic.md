# L10 — Granville's corrected heuristic: `limsup c_n ⪆ 2e^{−γ} ≈ 1.12292` — and the tension

**Kind:** heuristic prediction (not a theorem, not a test)
**Verdict:** **NEITHER PROVEN NOR REFUTED.** The *source content* is confirmed verbatim; the
*status* of the prediction is heuristic. It is the strongest reason to doubt `F` and it is not
evidence in the logical sense.
**Rests on:** `granville1995cramer` (**tier L1** — preprint pagination, journal copy not obtained):
- **preprint p. 2**, after eq. (2): *"…implies that we expect there to be `∼ 2e^{−γ} x/log x`
  primes ≤ x, where `2e^{−γ} ≈ 1.12292…"*
- **preprint p. 10, eq. (14)**: *"`max_{p_n ≤ x}(p_{n+1} − p_n) ∼ log² x`. This statement (or the
  weaker `O(log²x)`) is known as 'Cramér's Conjecture.'"*
- **preprint p. 12**, after eq. (20), verbatim: *"Moreover, with our new model above, Cramér's
  arguments suggest that `max_{p_n≤x}(p_{n+1} − p_n) ⪆ 2e^{−γ} log² x`, **which contradicts
  Cramér's conjecture (14)!**"*
- **preprint p. 12** — the mechanism: Maier's theorem exploits the inconsistency between the sieve
  heuristic and Cramér's model, "a severe blow to Cramér's model."

---

## Statement of the tension, in the only form that is defensible

```
L3  (proven, conditional on F) :   F  ⟹  limsup c_n ≤ 1
L10 (heuristic)                :   the corrected Cramér model suggests  limsup c_n ⪆ 2e^{−γ} ≈ 1.12292
```

Therefore:

> **Firoozbakht's conjecture and the Cramér–Granville heuristic are incompatible. At least one of
> the two must fail, and no current technique can say which.**

That sentence is the honest headline of this attack. It is the sentence to defend.

## Role in the proof-obligation tree

`L10` is the **entire refutation-side argument**. Everything else on that side is either
computational (no hit) or a theorem nobody can prove (**L12**). Remove `L10` and the case against
`F` is empty.

## Dependencies

**D7**, **L3** (the `limsup ≤ 1` half), **L9** (the model being corrected).

## Used by

The paper's framing. **T2** (it is the reason a search is worth running at all).

## What must NOT be written

- ❌ "Firoozbakht is false."
- ❌ "The Cramér model refutes Firoozbakht." (A heuristic refutes nothing.)
- ❌ Treating `L10` as a falsifiability test. It forbids no observation; no finite computation can
  breach or confirm a `limsup`.
- ✅ "Firoozbakht contradicts the Cramér–Granville heuristic, and one of the two must fail."

`decompose` §4.5 gets this exactly right and is, by the panel's unanimous assessment, the
best-calibrated paragraph in the upstream artifact. Preserve it verbatim through compression.

## Hazards

1. **`⪆` in the source means "suggests", not "proves".** Granville's own framing is that Cramér's
   *arguments under a corrected model* suggest this. (`source-ledger.md` §2.2.)
2. **Tier is L1, and the reason is pagination, not content.** The fetched file is the author's
   preprint, paginated 1–16; the journal (*Scand. Actuarial J.* **1995**, no. 1) is paginated
   12–28. **Every locator above is a preprint page and cannot currently be mapped to a journal
   page.** Either mark all Granville citations "preprint pagination" or re-locate against the
   journal copy. **Priority 2 for the citation gate.** (`source-ledger.md` §6.4, §7.2.)
3. **The constant and the direction were the highest-risk recall in the upstream `decompose` leg
   (its §7 A9, tagged HIGH).** Both are **CONFIRMED VERBATIM**. The refutation-side argument
   stands. (`source-ledger.md` §3 A9.)
4. **Do not smuggle `L10` in through the back door.** Reading **L7**'s finite 5% margin as
   evidence of fragility is the same promotion by another route — a `limsup` is invariant under
   every finite computation. (`synthesis.md` §4.2.)

## Declared gap

Journal pagination unresolved. Maier's theorem, the mechanism Granville leans on, has **no ledger
row** — it is quoted through Granville's prose and was not fetched.
