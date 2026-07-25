# L12 — Best unconditional lower bound on large gaps (Ford–Green–Konyagin–Tao)

**Kind:** theorem (published; the obstruction on the refutation side)
**Verdict:** **PROVEN** (by the cited authors). Tier **L1** here — abstract read, full PDF not
retrieved.
**Rests on:** `ford2016large` (L1) — *Annals of Math.* **183** (2016), 935–974; abstract read
verbatim at arXiv:1408.4505 and at the Annals page:

> *"Let `G(X)` denote the size of the largest gap between consecutive primes below `X`. Answering
> a question of Erdős, we show that
> `G(X) ≥ f(X) · log X log log X log log log log X / (log log log X)²`, where `f(X)` is a
> function tending to infinity with `X`."*

---

## Statement and the size of the shortfall

```
Known (unconditional) :   G(X)  ≥  f(X) · log X · loglog X · logloglog log X / (logloglog X)²
Needed to refute F    :   a gap  ≥  log²X − log X − 1   at a certified index
```

The known bound exceeds `log X` by an iterated-logarithmic factor. What a counterexample needs is
`log²X` — **a full power of `log` more.** Iterated logs do not close a power of a log.

## Role in the proof-obligation tree

`L12` blocks **both** refutation strategies that would produce a theorem:

1. **Prove `limsup c_n > 1`.** By **L3** that refutes `F` non-constructively. Blocked: the best
   known large-gap results are asymptotically *below* `log²`.
2. **Construct an explicit counterexample.** The CRT/Jacobsthal constructions in this lineage
   certify prime-free intervals, but of the same insufficient length.

So the only computationally live refutation route is a *search* (**T2**), not a construction.

## Dependencies

**D2**, **D7**, **L3**.

## Used by

The verdicts on the refutation-side strategies; **T5**.

## Two corrections this card forces on upstream artifacts

1. **The exponent on `logloglog X` is `2`, not `1`.** `decompose` §3.3 and §3.9 write the bound
   with `/ log log log n`; the published abstract has `/(log log log X)²`. The correction makes
   the known bound *smaller*, so the "not viable" verdict is if anything safer.
   (`source-ledger.md` §4.2.)
2. **S9 (construction) is blocked for one reason, not two.** `decompose` §3.9 gives two blocking
   reasons — magnitude and *localization* (that constructions give no control over the index `n`).
   **Magnitude is fatal; localization is not.** `T_n` depends on the index only through `L/n`,
   which is pinned by `x` to within precisely the error that `decompose` §4.6 itself computes and
   dismisses as negligible (**L19**). The document's own anti-test dissolves its own second
   blocking reason. Three panelists reached this independently (`synthesis.md` §2 C11).
   *Consequence:* `L11` and `L12` are **the same wall seen from two sides**, so a strategy table
   that lists "construction" and "large-gap theorem" as two covered archetypes is showing two
   entries where one obstruction operates.

## Hazards

1. **Abstract only.** No internal theorem numbers. Adequate for the qualitative use; inadequate if
   any constant is quoted. (`source-ledger.md` §6.5.)
2. `G(X)` is the **maximal** gap below `X`, indexed by `X`, not by `n`. Converting it into a
   statement about `g_n` at a specific `n` requires the count–index identity (**D3**) and is
   exactly where the localization question lives.
3. `f(X) → ∞` is unquantified in the abstract. Do not treat it as an effective constant.
4. **The author list is four, not five.** `decompose` §3.3/§7 A7 calls this "Ford–Green–Konyagin–
   Maynard–Tao". The *Annals* **183** (2016) paper, which is what the ledger row
   `ford2016large` records (and whose BibTeX lists exactly Ford, Green, Konyagin, Tao), is the
   **four-author** paper. Maynard obtained a comparable bound independently and contemporaneously
   in a separate paper; the five-author collaboration is a *later* joint work. **Cite the
   four-author Annals paper for this bound, or fetch the specific paper you mean.**

## Declared gap

Full text not retrieved; no internal locators. **Maynard's independent contemporaneous result has
no ledger row**, and neither does the later five-author paper — so the run cannot currently
support any sentence of the form "the FGKMT lineage shows…". Say "Ford, Green, Konyagin and Tao
(2016)" and stop there.
