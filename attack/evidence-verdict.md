# Evidence gate (pre-synthesis) — verdict

**Molecule:** `task-20260727-30dc` (leg `evidence-gate`, crew role: editor) — **ROUND 3**
**Run:** `germ-20260725-791a7c45` · **Re-attack loop:** `reattack-20260726-57d1` (rounds 1–2) ·
**Reconciliation leg:** `task-20260727-264e` (round 3, `attack/reconciliation.md`)
**Date:** 2026-07-27
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.

This is a fail-closed gate on evidence that **already exists** in this run. It does not
audit citations (that happens later, at citation-gate, once write-paper exists) and it
does not itself judge the conjecture. Every leg below is checked against a source
artifact on disk; nothing here is assumed.

**This document supersedes the round-2 `evidence-verdict.md` of the same name in
place.** Round 2 read `attack/re-attack/reattack-verdict.json` directly and named round 2
as the live re-attack round (`rounds_target=2`, `rounds_run=2`, `exit_reason:
rounds-exhausted`). Since then, a **reconciliation leg** (`task-20260727-264e`, round 3,
`attack/reconciliation.md`) ran — not another proof-attempt fan-out, but the single
seam-owning leg round 2's own skeptic asked for — and amended the round-2 artifacts in
place. Per this molecule's own (0) LOOP-leg instruction: `reattack-verdict.json` is read
first and still names round 2 as `final_round`; the reconciliation leg does not create a
`round: 3` entry inside that JSON (it is not a re-attack-loop round), so this gate reads
round 2's artifacts **as amended by round 3's reconciliation**, per
`attack/re-attack/rounds.md`'s own "Round 3" addendum, which records exactly this
resolution order. **What changed since round 2: the three round-2 BLOCKERs (R2-B1,
R2-B2, R2-B3) are each discharged *as seams* by the reconciliation leg — one repaired
theorem designated, one bibliographic tier settled, one already-landed ledger amendment
verified against the tree rather than re-applied. What did not change: no skeptic leg has
re-run against the amended tree, `faults.md` itself still lists a non-empty BLOCKER set
verbatim, and the reconciliation leg says explicitly, twice, that it has no standing to
clear the gate. The conjecture `F` is still OPEN, and the gate verdict is still
BLOCKED.**

---

## VERDICT: **BLOCKED**

**Failing leg: SKEPTIC (round 2, not re-run since reconciliation).**
`attack/re-attack/attack-round-2/faults.md` §0 still reads, verbatim, in the tracked
tree: *"The BLOCKER set is non-empty. Round 2 is NOT clean"* — 3 BLOCKERs. The
reconciliation leg amended the artifacts the BLOCKERs point at and recorded a
disposition for each (§1–§3 of `attack/reconciliation.md`), but it explicitly declined to
rewrite `faults.md`'s own verdict table (`attack/reconciliation.md` §6: *"the red-team
report is not rewritten; its findings' dispositions live here and in the amended
artifacts"*), and it explicitly declined to claim gate authority (`attack/
reconciliation.md` §7: *"Still BLOCKED, and this leg has no standing to clear it … That
is not the same as a clean skeptic run … The honest next step is item 1 of §8: re-run
the skeptic against the amended tree"*). Per the gate rule, the artifact of record for
the SKEPTIC leg (`faults.md`) has not reached a zero-BLOCKER state, and the leg that
could certify otherwise (a fresh skeptic pass) has not run. One failing applicable leg is
sufficient to block, regardless of the other three legs.

**The conjecture `F` remains OPEN.** Nothing in this evidence base, before or after
reconciliation, proves or refutes it, and every artifact read below says so explicitly of
itself.

---

## 0. LOOP leg — which round is live

Source: `attack/re-attack/reattack-verdict.json` (this molecule's own worktree copy, read
directly — not a mirror).

```json
"verdict": "BLOCKED",
"rounds_run": 2,
"rounds_target": 2,
"exit_reason": "rounds-exhausted",
"final_round": { "round": 2, "kernel": "UNPROVABLE_IN_BUDGET", "skeptic": "blockers" }
```

The file is present and well-formed — the first fail-closed check passes.
`final_round.artifacts` still names round 2's sources (`attack-round-2/faults.md`,
`attack-round-2/lean-probe-report.md`, the three `attack-round-2/proof-attempt-*.md`
files); the JSON has not been and should not be edited by a reconciliation leg — it is
the re-attack loop's own terminal record, and the loop exited before reconciliation
existed. **The live round for this gate is round 2, read as amended by round 3's
reconciliation** — confirmed by `attack/re-attack/rounds.md`'s own "Round 3" section
(added 2026-07-27), which states the reconciliation leg "ran outside this loop's
`rounds = 2` cap" and records the same three-BLOCKER disposition read in §2 below.
Round 1's `faults.md` / `lean-probe-report.md` (top-level `attack/`) remain superseded
inputs, not authoritative for this verdict.

---

## 1. KERNEL leg — `attack/re-attack/attack-round-2/lean-probe-report.md`

`formal_backend = 'lean'` (not `'none'`) — the DEGRADED carve-out does not apply; this
leg must PASS outright or the leg is failing. **Unchanged by reconciliation** — the
reconciliation leg's own declared write perimeter states *"no Lean written or re-run by
this leg"* (`attack/reconciliation.md` header) and *"it did not re-run the Lean gates
… the kernel leg's status is reported at the exit codes the round-2 skeptic
re-executed, and is labelled as second-hand"* (§0). So this leg's evidence is exactly
round 2's:

| Check | Result | Source |
|---|---|---|
| `lake build` exit code | **0** (2208 jobs) | report §1, line 34–36 |
| build warnings | **1** — `Statement.lean:185`, the declared open target | report §1 line 46 |
| `lake env lean audit.lean` / `audit_exhaustive.lean` exit code | **0 / 0** | report §1 lines 37–41, 47–48 |
| declarations scanned (exhaustive) | **63** (round 1 had 60; +3 barrier theorems) | report §1 line 49 |
| `sorryAx` dependents | **exactly 1**: `Firoozbakht.firoozbakht` — the conjecture itself | report §1 line 50 |
| live `sorry` tokens in `.lean` sources | **1** — `Statement.lean:186` | report §1 line 51 |
| `native_decide` / `axiom` / `@[implemented_by]` / `unsafe` | **none** (grep-clean, only docstring mentions) | report §1 line 52 |
| fidelity anchor (`Statement.lean`) byte-identical before/after | **yes**, SHA-256 matches | report §1 lines 59–69 |
| independently re-run by round-2 skeptic (not merely read) | **yes** | round-2 `faults.md` §1 |

**Reading.** The build is green and the axiom/`sorry` surface is grep-clean of
everything except the one declared open target (`Firoozbakht.firoozbakht`). Round 2's
`Barrier.lean` proves Bertrand's postulate insufficient for `F` at every `n ≥ 2` — a
machine-checked negative-capability result, not a step toward a proof.

**KERNEL leg: PASS**, unchanged since round 2. `kernel: UNPROVABLE_IN_BUDGET` in
`reattack-verdict.json` is consistent with this reading — PASS-of-the-gate-check is not
the same claim as PROVED.

---

## 2. SKEPTIC leg — `attack/re-attack/attack-round-2/faults.md`, read with `attack/reconciliation.md`

Artifact exists, now carrying a round-3 reconciliation banner (`faults.md` header) but
**its own §0 verdict table is unchanged and unstruck**:

| Severity | Count | Findings |
|---|---|---|
| **BLOCKER** | **3** | R2-B1, R2-B2, R2-B3 |
| MAJOR | 3 | R2-M1, R2-M2, R2-M3 |
| MINOR | 7 | R2-m1 … R2-m7 |

`faults.md` §0 still reads, verbatim: *"The BLOCKER set is non-empty. Round 2 is NOT
clean."* This is the artifact of record for the SKEPTIC leg, and it has not been zeroed.

**What the reconciliation leg (`attack/reconciliation.md`, molecule `task-20260727-264e`)
did to each BLOCKER, read directly from that document (not from a summary):**

- **R2-B1 — designated, not adjudicated by a skeptic.** §1: `Theorem C-b′`
  (`p_m ≤ 0.998244·p_{n₀}`, Axler row `(2.1,0,0,0)/6 690 557`, present in both editions)
  is named the corpus's single repaired Theorem C(b); `Theorem C(b*)` (`0.99565`, row
  `(1,0,0,0)/1 772 201`, preprint-only) is retired to a remark. Both theorems remain
  independently verified mathematically correct by the round-2 skeptic; the choice
  between them is documentary, made by a reconciler, not re-adjudicated by a fresh
  skeptic pass.
- **R2-B2 — limb 1 found stale, limb 2 closed.** §3: the claim that the ledger
  amendment "was never made" is **false against the committed tree** — the
  reconciliation leg found `source-ledger.md`'s Axler row already at tier **L0** (landed
  commit `61689d0`), and the skeptic's cited line numbers resolve only in a
  pre-merge worktree. What had genuinely not landed — propagation of the L0 tier into
  the sibling document (`proof-attempt-unconditional-verified-range.md`) — is what §2
  of the reconciliation leg lands.
- **R2-B3 — closed by retirement.** §1: the theorem consuming the edition-fragile
  `1 772 201` row is retired; the edition warning is now written into the document that
  had consumed it and into card `T1`.

**Why this does not zero the SKEPTIC leg for this gate.** The reconciliation leg is
explicit, in its own words, that this is not the same act as a skeptic clearing its
findings: *"That is not the same as a clean skeptic run. Clearing a skeptic finding is a
skeptic's job; a reconciler who marked its own work clean would be committing the exact
error `faults.md` §7 diagnoses. The honest next step is item 1 of §8: re-run the skeptic
against the amended tree"* (`attack/reconciliation.md` §7). No such re-run exists on
disk as of this molecule. `faults.md`'s own BLOCKER table is unedited by design
(reconciliation §6: *"the red-team report is not rewritten"*), so the artifact this gate
is instructed to check — *"the live round's faults.md exists and has zero residual
BLOCKERs"* — still reads 3, not 0.

Three MAJORs (R2-M1, R2-M2, R2-M3) are likewise **applied in the amended artifacts** by
the reconciliation leg but not re-certified by a skeptic pass; they do not change the
BLOCKER count either way.

**SKEPTIC leg: FAIL.** Zero residual BLOCKERs is the bar. `faults.md` reads 3, and no
fresh skeptic run has re-read the amended tree and reported otherwise — the
reconciliation leg itself names this exact gap and declines to fill it.

---

## 3. CORPUS leg — `attack/coverage-report.md`

Artifact present (249 lines), backend `lean`, non-empty and specific. **Untouched by
round 3** — the reconciliation leg's file-by-file edit table (`attack/reconciliation.md`
§6) does not list `attack/coverage-report.md`, and nothing in `attack/reconciliation.md`
flags it as stale or contradicted:

- 27 adversarial statements (all false/ill-formed by construction) run through
  `lake env lean` against the same toolchain as the anchor. 27/27 behaved as specified.
- Verification pass: `corpus/verify_corpus.py`, 109/109 green.
- Coverage against the brief's categories itemized across 8 rows; gaps stated plainly.

**CORPUS leg: PASS** — unchanged since round 2.

---

## 4. Verdict logic applied

| Leg | Round 2 (superseded) | Round 3 (live, this document) |
|---|---|---|
| LOOP (round resolution) | round 2 is live (`rounds_run=2` of `rounds_target=2`) | still round 2's artifacts, now read **as amended** by the round-3 reconciliation leg (`task-20260727-264e`), per `rounds.md`'s own "Round 3" section |
| KERNEL | PASS | **PASS**, unchanged — no Lean written or re-run by the reconciliation leg |
| SKEPTIC | FAIL — 3 BLOCKERs (R2-B1, R2-B2, R2-B3) | **FAIL** — same 3 BLOCKERs, each *discharged as a seam* by reconciliation but **not re-certified by a skeptic pass**; `faults.md`'s own verdict table is still unstruck at 3 |
| CORPUS | PASS | **PASS**, unchanged, not touched by round 3 |

Rule: *PASS only if all applicable legs pass (DEGRADED if the kernel leg is honestly
degraded and the rest pass), else BLOCKED with the failing leg named.* KERNEL is not
degraded and passes outright; SKEPTIC fails, for a narrower reason than round 2's (the
BLOCKERs have documented, agreed-on repairs) but fails nonetheless, because the leg with
standing to certify "zero residual BLOCKERs" — a skeptic pass against the amended tree —
has not run.

**⇒ VERDICT: BLOCKED. Failing leg: SKEPTIC — `faults.md` still lists 3 BLOCKERs
verbatim; the round-3 reconciliation leg (`attack/reconciliation.md`) discharged each as
a cross-artifact seam and said so precisely, but also said precisely that this is not a
gate clearance and that a fresh skeptic run is the missing step. Conjecture `F` remains
OPEN — neither this gate, nor the reconciliation leg, nor any leg either reads, claims
otherwise.**

Downstream `synthesize` / `write-paper` legs must not treat this run's corpus as
seal-ready. The single remaining action that would flip this leg is named by the
reconciliation leg itself (`attack/reconciliation.md` §8, item 1): **re-run the skeptic
against the amended tree**, feeding it `attack/reconciliation.md` so it audits the five
decisions, not just the arithmetic. That leg has not been funded by this molecule.

---

*Artifact of leg `evidence-gate`, molecule `task-20260727-30dc`, run
`germ-20260725-791a7c45`, re-attack loop `reattack-20260726-57d1`, reconciliation leg
`task-20260727-264e`. Sources read: `attack/re-attack/reattack-verdict.json`,
`attack/re-attack/attack-round-2/faults.md`, `attack/re-attack/attack-round-2/
lean-probe-report.md`, `attack/coverage-report.md`, `attack/reconciliation.md`,
`attack/re-attack/rounds.md`. No number in this document was invented; every figure
traces to the cited source file and section. This document supersedes the round-2
`evidence-verdict.md` of the same name in place.*
