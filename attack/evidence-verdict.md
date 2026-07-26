# Evidence gate (pre-synthesis) — verdict

**Molecule:** `task-20260726-a94b` (leg `evidence-gate`, crew role: editor) — **ROUND 2**
**Run:** `germ-20260725-791a7c45` · **Re-attack loop:** `reattack-20260726-57d1`
**Date:** 2026-07-26
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.

This is a fail-closed gate on evidence that **already exists** in this run. It does not
audit citations (that happens later, at citation-gate, once write-paper exists) and it
does not itself judge the conjecture. Every leg below is checked against a source
artifact on disk; nothing here is assumed.

**This document supersedes the round-1 `evidence-verdict.md` of the same name in
place.** Round 1 read `germ-20260725-791a7c45` directly (`rounds_target=1`,
`rounds_run=0`, no re-attack loop existed yet). Since then a re-attack loop
(`reattack-20260726-57d1`, `rounds_target=2`) ran two full rounds and left
`attack/re-attack/reattack-verdict.json` on disk, naming round 2 as the live round.
Per the (0) LOOP-leg instruction, that file must be read first and names which round
governs — it is read below, and it is round 2, not round 1. **What changed since
round 1: both of round 1's BLOCKERs (F1, F2) are now mathematically fixed, by
independent re-derivation, not re-assertion — but round 2 introduced three new
BLOCKERs of a different species (cross-artifact reconciliation failures, not
mathematical errors). What did not change: the conjecture `F` is still OPEN, and the
gate verdict is still BLOCKED — the failing leg changes from SKEPTIC-round-1 to
SKEPTIC-round-2, and the reason for the SKEPTIC failure changes from "unrepaired
math defects" to "unreconciled repairs," but the gate outcome (BLOCKED) is unchanged.**

---

## VERDICT: **BLOCKED**

**Failing leg: SKEPTIC (round 2).** Three residual BLOCKERs in
`attack/re-attack/attack-round-2/faults.md` are unresolved (repairs are named in the
document but explicitly not applied within this run). Per the gate rule, one failing
applicable leg is sufficient to block, regardless of the other three legs.

**The conjecture `F` remains OPEN.** Nothing in this evidence base proves or refutes
it, and every artifact read below — round 1's and round 2's alike — says so
explicitly of itself.

---

## 0. LOOP leg — which round is live

Source: `attack/re-attack/reattack-verdict.json` (this molecule's own worktree copy,
read directly — not a mirror).

```json
"verdict": "BLOCKED",
"rounds_run": 2,
"rounds_target": 2,
"exit_reason": "rounds-exhausted",
"final_round": { "round": 2, "kernel": "UNPROVABLE_IN_BUDGET", "skeptic": "blockers" }
```

The file is present and well-formed (not absent, not malformed) — the first
fail-closed check passes. `rounds_target = 2` and `rounds_run = 2`: the re-attack loop
ran to its cap without the strict stop condition (kernel PROVED AND skeptic clean, same
round) ever holding. `final_round.artifacts` names the live-round sources:

- `faults`: `attack-round-2/faults.md`
- `unproved`: `attack-round-2/unproved.md`
- `attempts`: `attack-round-2/proof-attempt-{first-failure-maximality,RH-conditional-bound,unconditional-verified-range}.md`

The kernel leg's own report path is `attack-round-2/lean-probe-report.md` (named in
the round-2 skeptic's perimeter section, consistent with `final_round.kernel`).
All paths resolve under this worktree's `attack/re-attack/` tree — confirmed by
directory listing. **LOOP leg resolved: live round = round 2, read from
`attack/re-attack/attack-round-2/` and `attack/re-attack/reattack-verdict.json`.**

Round 1's `faults.md` / `lean-probe-report.md` (top-level `attack/`) are **not** the
live sources for this gate — they are superseded inputs, read by the round-2 skeptic
for calibration but not authoritative for this verdict.

---

## 1. KERNEL leg — `attack/re-attack/attack-round-2/lean-probe-report.md`

`formal_backend = 'lean'` (not `'none'`) — the DEGRADED carve-out does not apply; this
leg must PASS outright or the leg is failing.

| Check | Result | Source |
|---|---|---|
| `lake build` exit code | **0** (2208 jobs) | report §1, line 34–36 |
| build warnings | **1** — `Statement.lean:185`, the declared open target | report §1 line 46 |
| `lake env lean audit.lean` / `audit_exhaustive.lean` exit code | **0 / 0** | report §1 lines 37–41, 47–48 |
| declarations scanned (exhaustive) | **63** (was 60 in round 1; +3 barrier theorems) | report §1 line 49 |
| `sorryAx` dependents | **exactly 1**: `Firoozbakht.firoozbakht` — the conjecture itself | report §1 line 50 |
| live `sorry` tokens in `.lean` sources | **1** — `Statement.lean:186` | report §1 line 51 |
| `native_decide` / `axiom` / `@[implemented_by]` / `unsafe` | **none** (grep-clean, only docstring mentions) | report §1 line 52 |
| fidelity anchor (`Statement.lean`) byte-identical before/after | **yes**, SHA-256 `6528868823c0…` matches before and after | report §1 lines 59–69 |
| independently re-run by round-2 skeptic (not merely read) | **yes** — `faults.md` §1 line 72–77 reproduces every gate exit code and the SHA-256 | round-2 `faults.md` §1 |

**Reading.** The build is green and the axiom/`sorry` surface is grep-clean of
everything **except** the one declared open target. Round 2 adds
`lean/Firoozbakht/Barrier.lean`: three new `sorry`-free theorems proving Bertrand's
postulate, ported to this development's indexing, sits strictly **above** the
Firoozbakht threshold at every `n ≥ 2` — a machine-checked negative-capability result
(the strongest prime-gap bound in Mathlib is proven insufficient), not a step toward
a proof of `F`. The `sorry` count is unchanged at 1 (round 1 took it 5 → 1; round 2
holds it at 1 → 1, which is the honest state of an open problem).

**KERNEL leg: PASS**, read as "grep-clean of sorry/axiom" meaning clean of every
*stray* sorry/axiom — the one sorry present is the declared, correctly-unattempted
open target. `kernel: UNPROVABLE_IN_BUDGET` in `reattack-verdict.json` is consistent
with this reading: PASS-of-the-gate-check is not the same claim as PROVED, and the
report is explicit that it is not claiming the latter.

---

## 2. SKEPTIC leg — `attack/re-attack/attack-round-2/faults.md`

Artifact exists (493 lines), verdict table at §0:

| Severity | Count | Findings |
|---|---|---|
| **BLOCKER** | **3** | R2-B1, R2-B2, R2-B3 |
| MAJOR | 3 | R2-M1, R2-M2, R2-M3 |
| MINOR | 7 | R2-m1 … R2-m7 |

**Both round-1 BLOCKERs are disposed of first (faults.md §5, item by item):**

- **F1 (round-1 BLOCKER) → FIXED.** `proof-attempt-first-failure-maximality.md`
  names the three inequivalent `m(n)` predicates in symbols (P6′-pair / P6′-gov /
  P6′-min), adds a fourth (P6′-rec), assigns every circulating measurement to the
  predicate it actually measures, and refutes the strongest with two exhibited
  witnesses — independently reproduced by the round-2 skeptic.
- **F2 (round-1 BLOCKER) → FIXED as a derivation**, by `proof-attempt-unconditional-
  verified-range.md`: the lemma is re-derived in closed form (not re-swept), the
  constant recomputed at 50 dps, matching the round-2 skeptic's independent
  recomputation to the digit.

**Neither F1 nor F2 reopens. But F2's fix is delivered twice, into two incompatible
theorems, and that collision is the source of round 2's own new BLOCKERs:**

**R2-B1 (BLOCKER):** two round-2 legs both repaired F2, into two different theorems
(`Theorem C(b*)` at constant `0.99565` vs `Theorem C-b'` at `0.998244`), off two
different Axler table rows, with neither leg citing the other. Both theorems are
independently verified mathematically correct by the round-2 skeptic — the defect is
that the corpus now carries three constants for one theorem name and no rule for
choosing among them.

**R2-B2 (BLOCKER):** the two round-2 legs assign the same source
(`axler2014newbounds`) contradictory bibliographic tiers on the same day
(`L2_strong, NOT OPENED` vs `L0, opened`), and the ledger amendment one leg reports as
landed (`source-ledger.md` tier promotion) was checked directly by the round-2
skeptic against the committed tree and **was never made** — `source-ledger.md:406`
and `concept-cards/T1-effective-pi-bounds.md:15` still read the old tier.

**R2-B3 (BLOCKER):** the `Theorem C(b*)` repair's load-bearing Axler citation (arXiv
v3 Corollary 3.6, row `x0=1772201`) was independently verified via byte-level PDF
fetch (MD5-pinned) to exist only in the preprint edition and be absent from the
published *Integers* 16 (2016) #A22 — an edition-fragile citation, unflagged in the
artifact that depends on it three further times (headline constant, finite branch,
counterfactual pricing).

**Repair named for all three, not applied within this run** (`faults.md` §2, per
finding, and §7): designate `Theorem C-b'` (`0.0017569`, present in both editions) as
the kept repair, retire `Theorem C(b*)` to a remark, land the ledger amendment once,
and cross-cite the four round-2 artifacts. The document's own recommendation is that
round 3 — if funded — must be a single reconciliation leg, not another proof-attempt
fan-out; this run's `rounds_target=2` does not fund that leg.

Three MAJORs are also unresolved (R2-M1: the skeptic's own inherited "three-fractions"
adjudication is itself off-by-one and inverted; R2-M2: round-1's F3 pattern — an
"unconditional" label rest on an unopened source — reappears in a branch round 1 had
passed clean; R2-M3: `gov`/`min` obligations are proven formally incomparable yet the
prose calls one strictly weaker and drops the other from the obligation list) — these
do not change the BLOCKER count but are load-bearing for a round-3 reconciliation leg.

Every finding above is explicit that it "touches the artifacts, not `F`"
(`faults.md` §7: "Neither BLOCKER, and none of the MAJORs, touches `F`. `F` remains
OPEN"). That does not clear the gate — the gate is on the state of the artifacts, and
the state, as of round 2, has a non-empty BLOCKER set (three, not the two of round 1).

**SKEPTIC leg: FAIL.** Zero residual BLOCKERs is the bar; three are present and
unresolved — a different three than round 1's, not the same two carried forward.

---

## 3. CORPUS leg — `attack/coverage-report.md`

Artifact present (249 lines), backend `lean`, non-empty and specific. This artifact
is unchanged since round 1 — no round-2 leg was tasked with extending the red-team
corpus, and the round-2 skeptic's perimeter section does not flag it as stale or
contradicted by anything in round 2:

- 27 adversarial statements (all false/ill-formed by construction) run through
  `lake env lean` against the same toolchain as the anchor. **27/27 behaved as
  specified** (20 refuted with no `sorry`, 3 rejected at elaboration, 3
  accepted-but-caught-by-axiom-audit, 1 undetected-by-any-automated-gate and named as
  such).
- Verification pass: `corpus/verify_corpus.py`, 109/109 green.
- Coverage against the brief's categories is itemized across 8 rows.
- What the corpus does not cover is stated plainly rather than omitted.

**CORPUS leg: PASS** — present, non-empty, substantive coverage, and nothing in
round 2 contradicts or stales it.

---

## 4. Verdict logic applied

| Leg | Round 1 (superseded) | Round 2 (live, this document) |
|---|---|---|
| LOOP (round resolution) | round 1 was the whole attack (`rounds_run=0`) | round 2 is live (`rounds_run=2` of `rounds_target=2`) |
| KERNEL | PASS | **PASS** (unchanged reading; new `Barrier.lean` adds a negative-capability result, not a proof) |
| SKEPTIC | FAIL — 2 BLOCKERs (F1, F2) | **FAIL** — 3 BLOCKERs (R2-B1, R2-B2, R2-B3); F1/F2 fixed, new seam-level BLOCKERs introduced |
| CORPUS | PASS | **PASS** (unchanged artifact, still substantive) |

Rule: *PASS only if all applicable legs pass (DEGRADED if the kernel leg is honestly
degraded and the rest pass), else BLOCKED with the failing leg named.* KERNEL is not
degraded (backend is `lean`, not `none`) and passes outright; SKEPTIC fails, in round 2
as in round 1, for a different reason.

**⇒ VERDICT: BLOCKED. Failing leg: SKEPTIC, round 2 (3 unresolved BLOCKERs: R2-B1
duplicate/incompatible repair of Theorem C(b); R2-B2 contradictory bibliographic tier
plus an unlanded ledger amendment; R2-B3 an edition-fragile citation load-bearing in
one repair). Conjecture `F` remains OPEN — neither this gate nor any leg it reads
claims otherwise.**

Downstream `synthesize` / `write-paper` legs must not treat this run's corpus as
seal-ready until R2-B1/B2/B3 are reconciled (the round-2 skeptic's `faults.md` §7
recommendation: a single reconciliation leg, not another proof-attempt fan-out) and
the skeptic leg re-confirms a zero-BLOCKER state. This run's re-attack loop is
exhausted (`rounds_run = rounds_target = 2`); a round 3 is not funded by this
molecule.

---

*Artifact of leg `evidence-gate`, molecule `task-20260726-a94b`, run
`germ-20260725-791a7c45`, re-attack loop `reattack-20260726-57d1`. Sources read:
`attack/re-attack/reattack-verdict.json`, `attack/re-attack/attack-round-2/faults.md`,
`attack/re-attack/attack-round-2/lean-probe-report.md`, `attack/coverage-report.md`.
No number in this document was invented; every figure traces to the cited source file
and section.*
