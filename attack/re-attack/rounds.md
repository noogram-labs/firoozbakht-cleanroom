# rounds.md — re-attack round ledger

**Molecule:** `reattack-20260726-57d1` (formula `converge-math-attack`)
**Subject:** Firoozbakht's conjecture — `p(n+1)^(1/(n+1)) < p(n)^(1/n)` for all `n≥1`
**rounds (target):** 2
**subquestions:** `first-failure-maximality`, `RH-conditional-bound`, `unconditional-verified-range`
**formal_backend:** `lean`

**Pinned artifacts re-used every round (never re-opened):**
- `attack/decompose.md`, `attack/source-ledger.md`, `attack/concept-cards/` — proof-obligation tree, bibliography, concept cards
- `lean/` — the FROZEN lean-skeleton (`Firoozbakht/Statement.lean` signatures unchanged across all legs)
- red-team corpus (`attack/notebook-*`, `attack/skeptic-checks/`) — tests the STATEMENT, not proof progress

**Prior run of this same formula:** `reattack-20260725-4db5` ran with `rounds=1` (the early-exit path — no re-attack round nucleated) and collapsed `BLOCKED` / `rounds-exhausted`, with the explicit recommendation: *"Re-germinate with rounds>=2 ... so a re-attack round can apply the two named repairs (F1, F2) before the skeptic re-runs."* This molecule is that re-germination.

| round | attempt ids | probe id | skeptic id | kernel | skeptic | converged? |
|---|---|---|---|---|---|---|
| 1 | (upstream, pinned spore nodes — not nucleated by this loop) | `task-20260725-9975` (lean-probe) | `task-20260725-488f` (skeptic) | UNPROVABLE_IN_BUDGET | blockers (2) | **NO** |
| 2 | `task-20260726-56a7` (first-failure-maximality), `task-20260726-b335` (RH-conditional-bound), `task-20260726-2035` (unconditional-verified-range) | `task-20260726-8ba0` (lean-probe) | `task-20260726-7211` (skeptic) | UNPROVABLE_IN_BUDGET | blockers (3) | **NO** |

## Round 1 — read from upstream (never re-run)

Source: `attack/faults.md` (skeptic leg, molecule `task-20260725-488f`, run `germ-20260725-791a7c45`) and `attack/lean-probe-report.md` (lean-probe leg, molecule `task-20260725-9975`, same run).

**Kernel verdict — UNPROVABLE_IN_BUDGET (not PROVED).** `lake build` exit 0, grep-clean of `axiom`/`native_decide`/`unsafe`/`@[implemented_by]`, but **one live `sorry`** remains: `Firoozbakht.firoozbakht : Conjecture` (`Statement.lean:186`) — the conjecture itself, correctly never attempted (it is the open problem). Four of five skeleton `sorry`s were discharged (equivalence-chain lemmas), promoting six further declarations to `sorryAx`-clean. Since a residual `sorry` remains, this does **not** meet the fail-closed PROVED bar (`lake build` exit 0 **AND** grep-clean of sorry/axiom).

**Skeptic verdict — blockers (not clean).** `attack/faults.md` reports **2 BLOCKER**, 4 MAJOR, 8 MINOR findings. Non-empty BLOCKER set ⇒ not clean.

- **F1 (BLOCKER):** the index `m(n)` / "governing record index" carries **three inequivalent definitions** across `notebook-0` (definition B), `notebook-2` (definition A), and card `L15`'s prose (definition C). `(C) ⟹ (A) ⟹ (B)` strictly; the search-pruning route actually consumes (B), the weakest. Two sibling legs publish opposite headline trends for what they call the same quantity because they measured different predicates. Repair (named by the skeptic, not applied): name the three predicates explicitly (`P6′-pair`, `P6′-gov`, `P6′-min`), state which measurement used which, and amend card `L15`'s prose to match its own measurement row.
- **F2 (BLOCKER):** `proof-attempt-0.md` Theorem C(b)'s cited bound **(A-high)** — `T_n ≤ (ℓ²−ℓ−1−1/ℓ)(1+ℓ⁴/x)` — does not follow from its stated justification (`v < ℓ²` gives `v(1+ℓ²/x)`, not `v(1+ℓ⁴/x)`). As printed the theorem is false by a factor ≈38 over part of its range (required `d` at `ℓ=ℓ₁` is `0.16934`, not the claimed `0.004479`). The theorem's **conclusion is independently true** under the corrected tight bound `T_n ≤ v(1+v/x)` with `v := ℓ²−ℓ−1−1/ℓ` (true max required `d* = 0.0043629 < 0.004479` at `ℓ=ℓ₁`). Repair (named, not applied): restate (A-high) with `v(1+v/x)`, replace `ℓ⁴/p_m` by `v²/p_m` in §6.2's criterion, re-run the numeric check against the corrected expression.
- MAJOR findings F3–F6 (not carried forward per the formula's bounded-scope instruction — only BLOCKERs gate round 2's fix list; MAJORs remain visible in `attack/faults.md` for any downstream synthesis leg).

**unproved-1** (still-`sorry`'d theorems, from `lean-probe-report.md`):
- `Firoozbakht.firoozbakht : Conjecture` (`Statement.lean:186`) — the conjecture itself. Correctly open; this is not a gap introduced by any leg.

**faults-1** (BLOCKER + MAJOR findings from `faults.md`):
- BLOCKER: F1 (`m(n)` three-way definition collision), F2 (Theorem C(b)'s (A-high) bound off by factor ≈38, conclusion independently true under corrected bound)
- MAJOR: F3 (Theorem B's discharge mislabelled "unconditional" on an unread L2_strong source), F4 (PA-1's "at no other index whatsoever" false as stated — the `n≥3` CMS restriction is load-bearing and dropped), F5 (three mutually incompatible fractions circulate for the `55.92%` statistic), F6 (`notebook-1`'s `p*(C)` definition contradicts its own table)

**Round 1 converged?** NO — kernel is UNPROVABLE_IN_BUDGET (not PROVED) and skeptic carries 2 BLOCKERs (not clean). Per the loop's stop condition ("kernel PROVED and skeptic clean, same round"), round 1 does not hold the fixpoint. Proceeding to round 2 with `${rounds}=2`, feeding round 2 exactly F1 and F2 (the BLOCKER set) plus `unproved-1` and the bounded source-anchor refresh the skeptic flagged missing.

## Round 2 — nucleated forward by this loop (strictly acyclic)

Three proof-attempts (one per subquestion), one lean-probe (fork discipline: fed only `unproved-1`, not blocked-by the attempts), and one skeptic (blocked-by all four). Artifacts at `attack-round-2/` under this molecule's dir.

**Kernel verdict — UNPROVABLE_IN_BUDGET (not PROVED).** `task-20260726-8ba0` re-ran `lake build` (exit 0, 2208 jobs, `Built Firoozbakht.Barrier`), `audit_exhaustive.lean` (exit 0, 63 declarations scanned). Exactly one live `sorry`: `Firoozbakht.firoozbakht : Conjecture` (`Statement.lean:186`) — attempted this round (unlike round 1, which declined) and failed honestly: `exact?`/`aesop`/`decide` all fail as expected; Bertrand's postulate is *provably insufficient* (new theorem `bertrand_ceiling_above_threshold`, sorry-free); BHP/RH-conditional/Cramér bounds are either unformalized or shown insufficient on paper by this round's own `proof-attempt-RH-conditional-bound.md`. `Statement.lean` re-verified byte-identical (SHA-256 unchanged). No regression: `unproved-2` = `unproved-1` (still exactly one entry).

**Skeptic verdict — blockers (not clean), and worse than round 1 by count.** `task-20260726-7211`'s `attack-round-2/faults.md` reports **3 BLOCKER**, 3 MAJOR, 7 MINOR. Round-1 BLOCKER disposition, confirmed by independent re-derivation (not a reading of upstream numbers):
- **F1 (round 1): FIXED, not re-worded.** The three predicates (P6′-pair/P6′-gov/P6′-min) are named explicitly, a fourth (P6′-rec) added, every measurement assigned to its predicate, both notebooks' opposite headlines reconciled, and P6′-pair is *refuted* with two independently-reproduced witnesses.
- **F2 (round 1): FIXED as mathematics, by both legs independently — which is exactly the new problem.** Both `proof-attempt-unconditional-verified-range.md` and `proof-attempt-first-failure-maximality.md` correctly restated the bound as the tight `v(1+v/x)` form and re-derived (not re-swept) the constant. Both derivations are independently verified correct. But they repaired it to **two different theorems** (different Axler rows, different constants: `0.99565` vs `0.998244`), neither citing the other (→ **R2-B1**, BLOCKER).

New round-2 BLOCKERs (none touch `F`, none are math errors — the skeptic's own words: *"a seam, not a step"*):
- **R2-B1:** two legs ship two incompatible repairs of the same round-1 F2, under different theorem names/constants, off different Axler rows — F1's own failure mode (fan-out with no reconciliation) reproduced one round later, on the very artifact meant to fix it.
- **R2-B2:** the two legs assign the source `axler2014newbounds` contradictory tiers (L0 vs L2_strong-NOT-OPENED) on the same day; the ledger amendment one leg reports as landed was checked directly and **never made** (`source-ledger.md` and the concept card still read the old tier).
- **R2-B3:** the repair resting on the L0-tier claim cites an Axler table column (`x₀=1 772 201`) that the skeptic independently verified (byte-level PDF fetch, MD5-pinned) exists **only in the arXiv preprint, not in the published journal version** — an edition-fragile citation, unflagged.

New MAJORs: **R2-M1** (a three-fractions statistic dispute the round-2 skeptic itself "settled" is inverted — recomputed denominators show round 2's adjudication is wrong, not round 1's); **R2-M2** (round-1 F3's exact pattern — an "unconditional" label resting on an unopened/partially-opened source — reappears in the one branch round 1 had passed clean); **R2-M3** (P6′-gov and P6′-min are proved *incomparable* by the round-2 attempt's own Proposition 4, yet its prose calls P6′-min strictly weaker and drops P6′-gov from the obligation list).

**Round 2 converged?** NO — kernel is UNPROVABLE_IN_BUDGET (not PROVED, and honestly so: this is Firoozbakht's conjecture, open since 1982) and skeptic carries 3 BLOCKERs (not clean, and a higher BLOCKER count than round 1's 2). `round = 2 = ${rounds}` — the loop's target is exhausted. Per the `while` discipline, the loop terminates here: `round < rounds` is now false (`2 < 2` is false), so no round 3 is nucleated. The stop condition (kernel PROVED **and** skeptic clean, same round) never held in either round. Exit: **rounds-exhausted → BLOCKED** (never a silent pass).

**Trajectory, honestly read:** the unproved list did **not shrink** (`unproved-1` = `unproved-2`, one entry, unchanged — expected, since it is the open conjecture itself). The BLOCKER set changed *kind* but not *count downward*: round 1's 2 BLOCKERs were genuine mathematical/definitional defects inside individual artifacts; round 2 closed both of those specific defects (confirmed FIXED by independent re-derivation) but **introduced 3 new BLOCKERs of a different species — reconciliation failures across a widened fan-out**, exactly the failure mode round 1's own skeptic (§6) predicted would recur. The loop is not converging on the reconciliation axis; per the round-2 skeptic's explicit recommendation, round 3 (were it to run) would need a reconciliation leg, not another fan-out — this loop's `rounds=2` cap does not fund that leg.

---

## Round 3 — the reconciliation leg, run outside this loop's `rounds = 2` cap

This loop exited `rounds-exhausted / BLOCKED` and recorded that *"round 3 (were it to run) would need
a reconciliation leg, not another fan-out — this loop's `rounds=2` cap does not fund that leg."*
**That leg was funded separately and ran on 2026-07-27:** molecule `task-20260727-264e`, artifact
**`attack/reconciliation.md`**. It was not a fan-out: one leg, five decisions, no new mathematics
opened.

**Disposition of this loop's three round-2 BLOCKERs, as seams:**

- **R2-B1 — CLOSED by designation.** **Theorem C-b′** (`p_m ≤ 0.998244·p_{n₀}`, Axler row
  `(2.1,0,0,0)/6 690 557`) is the corpus's single repaired Theorem C(b); **Theorem C(b\*)**
  (`0.99565`, row `(1,0,0,0)/1 772 201`) is retired to a remark. The deciding ground is R2-B3's own
  finding — the `1 772 201` row is preprint-only — which the ledger had already recorded as a
  standing downstream rule that nobody propagated. Both theorems remain mathematically correct;
  the choice is documentary. Round 1's `0.99553` and round 2's `0.99565` are retired.
- **R2-B2 — limb 1 is STALE; limb 2 is CLOSED.** The claim *"the ledger amendment … was checked
  directly and **never made**"* recorded above is **wrong**: the reconciliation leg checked the
  committed tree and found `source-ledger.md`'s Axler row at **L0** with the full fetch record,
  §6 gap 3 marked `CLOSED 2026-07-26`, and card `T1` amended to match. The skeptic's line numbers
  resolve only in a worktree branched before commit `61689d0`. What genuinely had not landed was
  the propagation of the L0 tier into the **sibling** document (UVR), and that is what round 3
  landed. `axler2014newbounds` is **L0** at every site, with a standing ⚠ that its
  `(1,0,0,0)/1 772 201` row is preprint-only.
- **R2-B3 — CLOSED by retirement.** The theorem that consumed the edition-fragile row is retired,
  and the edition ⚠ is now written into the document that consumed it as well as into card `T1`.

**MAJORs:** R2-M1 recounted from the statement — the denominators are `216 806` (`n ≥ 10`) and
`216 815` (all `n`); FFM's table was one low at every range under both conventions, and
`proof-attempt-0.md`'s figure was right all along. Five independent counts now agree, one of them
(the round-2 RH leg's own §11 item 15, **unread for a full round**) with a self-consistency argument
showing `121 238 / 216 805` is impossible under *any* convention. R2-M2 and R2-M3 applied in place,
as are all seven MINORs.

**What round 3 did NOT do.** It cleared no gate, opened no source, wrote no Lean, re-ran no `lake`,
and proved nothing. **`F` remains OPEN and the evidence gate remains BLOCKED.** The reconciliation
leg's own §8 item 1 is *re-run the skeptic against the amended tree* — that is the next step, and it
is not done. Closing the seams is not the same as a clean skeptic run, and the leg says so in those
words.
