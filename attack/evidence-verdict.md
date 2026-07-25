# Evidence gate (pre-synthesis) — verdict

**Molecule:** `task-20260725-093d` (leg `evidence-gate`, crew role: editor)
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-25
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.

This is a fail-closed gate on evidence that **already exists** in this run. It does not
audit citations (that happens later, at citation-gate, once write-paper exists) and it
does not itself judge the conjecture. Every leg below is checked against a source
artifact on disk; nothing here is assumed.

---

## VERDICT: **BLOCKED**

**Failing leg: SKEPTIC.** Two residual BLOCKERs in `skeptic/faults.md` are unresolved
(repairs are proposed in the document but explicitly **not applied**). Per the gate rule,
one failing applicable leg is sufficient to block, regardless of the other three legs.

**The conjecture `F` remains OPEN.** Nothing in this evidence base proves or refutes it,
and every artifact read below says so explicitly of itself.

---

## 0. LOOP leg — which round is live

Source: `attack/re-attack/reattack-verdict.json` (mirrored identically at
`.cosmon/state/fleets/default/molecules/reattack-20260725-4db5/reattack-verdict.json`).

```json
"verdict": "BLOCKED", "rounds_run": 0, "rounds_target": 1,
"exit_reason": "rounds-exhausted"
```

`reattack-verdict.json` is present and well-formed (not absent, not malformed) — the
first fail-closed check passes. `rounds_target = 1` and `rounds_run = 0`: no re-attack
round was ever nucleated. Per the file's own `escalation.reason`, this is by design —
"`rounds=1` means round 1 (the spore's pinned v3.x single shot) IS the whole attack";
the live round is round 1, read directly, exactly as v3.x did. `final_round.artifacts`
names:

- `faults`: `.cosmon/state/spore-runs/germ-20260725-791a7c45/skeptic/faults.md`
- `unproved`: `.cosmon/state/spore-runs/germ-20260725-791a7c45/lean-probe/lean-probe-report.md`

Both paths resolve under this same germ run — confirmed by directory listing. **LOOP leg
resolved: live round = round 1, read from `germ-20260725-791a7c45` directly.**

---

## 1. KERNEL leg — `lean-probe/lean-probe-report.md`

`formal_backend = 'lean'` (not `'none'`) — the DEGRADED carve-out does not apply; this
leg must PASS or the leg is failing.

| Check | Result | Source |
|---|---|---|
| `lake build` exit code | **0** | report line 43: `Build completed successfully (1984 jobs)` |
| build warnings | **1** — `Statement.lean:185`, the declared open target | report line 44 |
| `lake env lean audit.lean` / `audit_exhaustive.lean` exit code | **0 / 0** | report lines 45–46 |
| `sorryAx` dependents (exhaustive, list-free audit over 60 declarations) | **exactly 1**: `Firoozbakht.firoozbakht` — the conjecture itself | report lines 47–48, 64–67 |
| live `sorry` tokens in `.lean` sources | **1** — `Statement.lean:186`, the tactic block of the theorem on line 185 | report line 49 |
| `native_decide` / `axiom` / `@[implemented_by]` / `unsafe` | **none** (grep-clean) | report line 50 |

**Reading.** The build is green and the axiom/`sorry` surface is grep-clean of
everything **except** the one declared open target — which is the conjecture under
attack itself, correctly never attempted (report: "By instruction, and because it is
open"). An attack on an open `Π₁` conjecture cannot ever reach zero `sorry`; the
honest end-state is exactly one, on the declared target, and nothing else. Four of the
original five `sorry`s (the equivalence-chain lemmas) were discharged with real proof
terms and independently signature-diffed against the skeleton anchor (report lines
179–207), so the reduction `Conjecture ↔ ConjectureReal ↔ (∀ n ≥ 1, g_n < T_n)` is now
machine-checked rather than asserted.

**KERNEL leg: PASS**, read as "grep-clean of sorry/axiom" meaning clean of every
*stray* sorry/axiom — the one sorry present is the declared, correctly-unattempted
open target, not a proof gap introduced by this run.

---

## 2. SKEPTIC leg — `skeptic/faults.md`

Artifact exists (445 lines), verdict table at §1:

| Severity | Count | Findings |
|---|---|---|
| **BLOCKER** | **2** | F1, F2 |
| MAJOR | 4 | F3–F6 |
| MINOR | 8 | F7–F14 |

**F1 (BLOCKER):** `m(n)` / "governing record index" carries three inequivalent
definitions across `notebook-0`, `notebook-2`, and card `L15`; the run currently
publishes two contradictory headline sentences ("the empirical case weakens" vs. "the
margin does not decay") about the same named quantity, unreconciled. Repair named
(§2, "name the three predicates… state which one each measurement used") but the
document is explicit: **"Repair (not applied by this leg)."**

**F2 (BLOCKER):** `proof-attempt-0.md` Theorem C(b)'s cited bound (A-high) does not
follow from its stated justification; as printed, the theorem is false by a factor
`≈ ℓ²` over part of its stated validity range. The theorem's *conclusion* is
independently confirmed true under the corrected (tight) bound — this is a derivation
defect, not an error about `F` — but the artifact as written is what a downstream
`write-paper`/`synthesize` leg would read and propagate. Repair is a one-line
restatement, and the document is again explicit: it is **not applied**.

Both BLOCKERs are repairable and neither touches the conjecture `F` (faults.md §6:
"Neither BLOCKER touches `F`. `F` remains OPEN"). That does not clear the gate — the
gate is on the state of the artifacts, and the state, as of this run, has a non-empty
BLOCKER set.

**SKEPTIC leg: FAIL.** Zero residual BLOCKERs is the bar; two are present and
unresolved.

---

## 3. CORPUS leg — `red-team-corpus/coverage-report.md`

Artifact present (250 lines), backend `lean`, non-empty and specific:

- 27 adversarial statements (all false/ill-formed by construction) run through
  `lake env lean` against the same toolchain as the anchor. **27/27 behaved as
  specified** (20 refuted with no `sorry`, 3 rejected at elaboration, 3
  accepted-but-caught-by-axiom-audit, 1 undetected-by-any-automated-gate and named as
  such — `V04`, a true-but-differently-meant statement produced by ℕ→ℝ coercion, not a
  false one slipping through).
- Verification pass (§7): `corpus/verify_corpus.py`, **109/109 green**, including a
  self-check that closed a real gap (refutation files were re-audited to confirm none
  depend on the open target's `sorryAx`).
- Coverage against the brief's categories is itemized (§2) across 8 rows spanning near-
  miss variants, quantifier-order errors, dropped hypotheses, typing cheats, indexing
  fidelity, ℕ-subtraction, false bounds, method cheats, and audit evasion.
- What the corpus does **not** cover is stated plainly (§6, 5 items) rather than
  omitted.

**CORPUS leg: PASS** — present, and its coverage report is substantive, not a stub.

---

## 4. Verdict logic applied

| Leg | Status |
|---|---|
| LOOP (round resolution) | resolved — round 1 is live, read directly |
| KERNEL | PASS (`lake build` 0, grep-clean of every sorry/axiom but the declared open target) |
| SKEPTIC | **FAIL** — 2 residual BLOCKERs, repairs proposed but not applied |
| CORPUS | PASS — present, non-empty, substantive coverage |

Rule: *PASS only if all applicable legs pass (DEGRADED if the kernel leg is honestly
degraded and the rest pass), else BLOCKED with the failing leg named.* KERNEL is not
degraded (backend is `lean`, not `none`) and passes outright; SKEPTIC fails.

**⇒ VERDICT: BLOCKED. Failing leg: SKEPTIC (2 unresolved BLOCKERs: F1 vocabulary
collision on `m(n)`; F2 mis-derived bound in Theorem C(b)). Conjecture `F` remains
OPEN — neither this gate nor any leg it reads claims otherwise.**

Downstream `synthesize` / `write-paper` legs must not treat this run's corpus as
seal-ready until F1 and F2 are repaired (each has a named, one-paragraph repair already
on record in `skeptic/faults.md` §2) and the skeptic leg re-confirms a zero-BLOCKER
state.

---

*Artifact of leg `evidence-gate`, molecule `task-20260725-093d`, run
`germ-20260725-791a7c45`. Sources read: `attack/re-attack/reattack-verdict.json`,
`skeptic/faults.md`, `lean-probe/lean-probe-report.md`,
`red-team-corpus/coverage-report.md`. No number in this document was invented; every
figure traces to the cited source file and line range.*
