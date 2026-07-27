# Evidence gate (pre-synthesis) — verdict

**Molecule:** `task-20260727-2fee` (leg `evidence-gate`, crew role: editor) — **ROUND 3, re-verdicted
against the fresh post-reconciliation skeptic audit**
**Run:** `germ-20260725-791a7c45` · **Re-attack loop:** `reattack-20260726-57d1` (rounds 1–2) ·
**Reconciliation leg:** `task-20260727-264e` (round 3, `attack/reconciliation.md`) ·
**Skeptic re-audit leg:** `task-20260727-5096` (round 3, `attack/faults.md`)
**Date:** 2026-07-27
**Conjecture under attack (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`.

This is a fail-closed gate on evidence that **already exists** in this run. It does not audit
citations (that happens later, at citation-gate, once `write-paper` exists) and it does not itself
judge the conjecture. Every leg below is checked against a source artifact on disk; nothing here is
assumed.

**This document supersedes the prior `evidence-verdict.md` (dated the same day, molecule
`task-20260727-30dc`) in place.** That prior version was itself correct as of its own writing: it
named the missing step precisely — *"a fresh skeptic run against the amended tree"* — and blocked on
its absence. **That missing step has since run.** `attack/faults.md` (molecule `task-20260727-5096`,
leg `skeptic`, round 3) is exactly the audit the prior verdict called for: it re-checked every
round-2 finding against the reconciled tree by re-deriving numbers itself, not by reading reports,
and it explicitly supersedes both `attack/faults-round-1.md` and
`attack/re-attack/attack-round-2/faults.md` (both preserved, not deleted, both banner-stamped as
superseded). **What changed since the prior verdict: the SKEPTIC leg is no longer stale — it is a
live, fresh audit — and it closed 12 of round 2's 13 findings (all 3 BLOCKERs, all 3 MAJORs, all 7
MINORs) by independent re-derivation. What did not change: the artifact of record for the SKEPTIC leg
still has a non-empty BLOCKER set — 2 new findings (S3-B1, S3-B2), of a different species than
round 2's, both cross-artifact seam failures rather than mathematical errors. The conjecture `F` is
still OPEN, and the gate verdict is still BLOCKED.**

---

## VERDICT: **BLOCKED**

**Failing leg: SKEPTIC (round 3, `attack/faults.md`, fresh — not stale).**
`attack/faults.md` §0 states, as of the live commit: *"The BLOCKER set is non-empty. Round 3 is NOT
clean, and the evidence gate stays BLOCKED"* — 2 BLOCKERs (S3-B1, S3-B2). Unlike the prior verdict,
this is not a stale artifact being read past its shelf life: this skeptic leg audited the
reconciliation leg (`attack/reconciliation.md`, `task-20260727-264e`) directly, re-executed the Lean
gates itself rather than reading a report, and re-derived every disputed number from source
statements with its own scripts (`attack/skeptic-round3-checks/s3_recount.py`,
`…/s3_constants.py`). One failing applicable leg is sufficient to block, regardless of the other two.

**The conjecture `F` remains OPEN.** Nothing in this evidence base, across three rounds, proves or
refutes it, and every artifact read below says so explicitly of itself.

---

## 0. LOOP leg — which round is live

Source: `attack/re-attack/reattack-verdict.json`, read first, directly (not a mirror).

```json
"verdict": "BLOCKED",
"rounds_run": 2,
"rounds_target": 2,
"exit_reason": "rounds-exhausted",
"final_round": { "round": 2, "kernel": "UNPROVABLE_IN_BUDGET", "skeptic": "blockers" }
```

The file is present and well-formed — the first fail-closed check passes. Its `final_round` still
names round 2's own artifacts (`attack-round-2/faults.md`, `attack-round-2/lean-probe-report.md`,
three proof attempts); the JSON is the re-attack loop's own terminal record and is correctly
unedited by anything downstream of it. Per this molecule's brief, at rounds beyond what the loop's
own JSON tracked, the live artifacts are named by the task-level resumption, not by re-opening the
JSON: **this galaxy ran the loop's two rounds, then a reconciliation leg
(`task-20260727-264e`, `attack/reconciliation.md`) that the round-2 skeptic itself asked for, then a
fresh post-reconciliation skeptic re-audit (`task-20260727-5096`, `attack/faults.md`), which
supersedes round 2's `faults.md` in place** (banner in both `attack/faults.md` and
`attack/re-attack/attack-round-2/faults.md` records the supersession explicitly). This gate reads the
round-3 skeptic's artifact as the current SKEPTIC leg, and the round-3 reconciliation as the current
state of the theorem/ledger artifacts it repaired.

---

## 1. KERNEL leg — re-executed by the round-3 skeptic, not merely read

`formal_backend = 'lean'` (not `'none'`) — the DEGRADED carve-out does not apply; this leg must PASS
outright or the leg is failing. Source: `attack/faults.md` §1, which states the checks were
independently re-run, not read from `attack/lean-probe-report.md` or
`attack/re-attack/attack-round-2/lean-probe-report.md`:

| Check | Result | Source |
|---|---|---|
| `lake exe cache get` | exit 0 | `faults.md` §1 |
| `lake build` exit code | **0** (2208 jobs, "Build completed successfully") | `faults.md` §1 |
| `lake env lean audit_exhaustive.lean` exit code | **0** | `faults.md` §1 |
| declarations scanned (exhaustive) | **63** | `faults.md` §1 |
| `sorryAx` dependents | **exactly 1**: `Firoozbakht.firoozbakht` — the conjecture itself | `faults.md` §1 |
| fidelity anchor (`Statement.lean`) SHA-256 | recorded (`6528868823c0637dd182c914e2ef43a7455f851335cafaba6cee934802e004c1`) | `faults.md` §1 |

**Reading.** The build is green and the axiom/`sorry` surface is grep-clean of everything except the
one declared open target (`Firoozbakht.firoozbakht`), consistent with `attack/lean-probe-report.md`'s
original headline (*"four of the five `sorry`s are discharged; the fifth is the conjecture itself"*)
and with round 2's own re-run. The round-3 reconciliation leg wrote no Lean and re-ran none
(`attack/reconciliation.md` header: *"no Lean written or re-run by this leg"*) — the round-3 skeptic
is the first leg since round 2 to touch the toolchain directly, and it reproduces the same result.

**KERNEL leg: PASS.**

---

## 2. SKEPTIC leg — `attack/faults.md` (round 3, fresh audit of the reconciliation)

Artifact exists, is dated 2026-07-27, audits `attack/reconciliation.md` directly, and states its own
verdict first:

| Severity | Count | Findings |
|---|---:|---|
| **BLOCKER** | **2** | S3-B1, S3-B2 |
| MAJOR | 2 | S3-M1, S3-M2 |
| MINOR | 5 | S3-m1 … S3-m5 |

**What closed (12 of round 2's 13 findings), each verified by the round-3 skeptic against the tree,
not against either prior report:**
- **R2-B1** (two incompatible repairs of one theorem) — **CLOSED**. Theorem C-b′ is designated
  (`✅ DESIGNATED`), Theorem C(b*) retired (`⛔ RETIRED`), no concept card carries a Theorem C
  constant at all (grep-verified: zero hits), and the round-3 skeptic independently re-derived the
  designated theorem's constants from its statement — all match to the stated precision.
- **R2-B2** (ledger amendment claimed never made) — **CLOSED**. `source-ledger.md:426` carries tier
  `L0` with the three-document fetch table; `git log` places the promotion at `61689d0` (07-26
  19:22), merged `4526b27` (19:26) — before round 2's `faults.md` was even committed (20:46, on a
  pre-merge branch), which is why the stale line numbers appeared stale.
- **R2-B3** (repair resting on a preprint-only Axler row) — **CLOSED** by retirement, with the
  underlying `π(x)` bound independently re-verified (0 failures below `10⁸`).
- **R2-M1** (55.92% denominators) — **CLOSED**. Recounted from the raw statement with a fresh script
  (`s3_recount.py`); the round-3 skeptic agrees with the reconciliation's figure, not with either
  prior skeptic's.
- **R2-M3**, all seven MINORs — **CLOSED**, each independently re-derived (28 maximal-gap records
  below `2·10⁸`, census-counts-indices wording, the `2.4·10⁻⁸` margin, the lean-probe slack-table
  annotation, the write-perimeter question, the `p^{−0.83}` local-exponent correction, the `10³`
  per-decade entry).

**What did not close — the 2 new BLOCKERs, of a different species than round 2's (cross-artifact
seam failures, not mathematical errors):**

- **S3-B1** — decision 2 of the reconciliation states `axler2014newbounds` is tier L0 *"at every site
  in the corpus"*; **six sites still assert L2_strong / unopened** (five concept cards —
  `L2-threshold-asymptotics.md`, `L3-necessary-condition.md`, `L4-sufficient-condition.md`,
  `D3-pi-and-count-index-identity.md`, `INDEX.md` — plus the round-2
  `proof-attempt-RH-conditional-bound.md`, which the reconciliation's own §6 table calls *"banner
  only — nothing … needed correcting"*, which the tree contradicts: two of its flag blocks gate a
  live numeral on the stale tier). `R2-B2`'s limb 2 (tier propagation) is therefore **not** actually
  closed — only propagated to one sibling document out of seven.
- **S3-B2** — the reconciliation's own *"what is still open"* section (§6–§8) makes four claims about
  the tree that `git log` and the tracked files contradict: (a) it says `paper/paper.tex` still needs
  rewriting against round 2 — it was rewritten on 2026-07-26 (`d33dfe0`); (b) it says `paper.tex`
  still asserts Axler unopened — it asserts the opposite, retrospectively, at four sites; (c) it
  claims `0.99553` is still live in the paper — it appears once, already labelled superseded; (d) it
  claims **no citation audit has run on the round-2 corpus** — `attack/verification-report.md` is
  exactly that audit (round 2, commit `51756c5`, **verdict PASS**), committed 11 minutes after the
  paper rewrite. This is the same species of error the reconciliation leg exists to prevent
  (unverified claims about tree state), and it has already propagated into `attack/synthesis.md`
  (§0, §7, §8, §9), which now republishes the false "no round-2 audit exists" claim as the corpus's
  headline gate status — a false statement about a **file** has become a false statement about a
  **gate**, in the document a `write-paper` leg reads first.

**Why the SKEPTIC leg still fails.** Zero residual BLOCKERs is the bar the brief sets. This is a
fresh, independently-re-derived audit — not a stale one being read past its currency, as the prior
verdict correctly declined to accept — and it still finds 2. The findings are narrower than round 2's
three (both are cross-artifact propagation/accuracy failures, not open mathematical disputes; the
underlying theorems, ledger tier decision, and citation audit are all independently confirmed
correct by this same skeptic pass), but "narrower" is not "zero."

**SKEPTIC leg: FAIL.**

---

## 3. CORPUS leg — `attack/coverage-report.md`

Artifact present (249 lines), backend `lean`, non-empty and specific. Untouched by round 3 — neither
`attack/reconciliation.md`'s edit table nor `attack/faults.md` flags it as stale or contradicted:

- 27 adversarial statements (all false/ill-formed by construction) run through `lake env lean`
  against the same toolchain as the anchor. 27/27 behaved as specified (20 refuted, 3 rejected, 3
  accepted-but-unsound caught by axiom audit, 1 undetected — named as the report's own main finding).
- Verification pass: `corpus/verify_corpus.py`, 109/109 green.
- Coverage against the brief's categories itemized across 8 rows; gaps stated plainly.

**CORPUS leg: PASS.**

---

## 4. Verdict logic applied

| Leg | Prior verdict (superseded) | This verdict (round 3, live) |
|---|---|---|
| LOOP (round resolution) | round 2's artifacts, read as amended by reconciliation | round 2's artifacts, as amended by reconciliation **and** re-audited fresh by round-3 skeptic |
| KERNEL | PASS (second-hand, unre-run since round 2) | **PASS** — re-executed directly by the round-3 skeptic, same result |
| SKEPTIC | FAIL — stale round-2 `faults.md` never re-run against the amended tree | **FAIL** — fresh round-3 `faults.md` now exists and *is* the re-run the prior verdict called for; it closes 12/13 round-2 findings but opens 2 new BLOCKERs of a different species |
| CORPUS | PASS | **PASS**, unchanged, not touched by round 3 |

Rule: *PASS only if all applicable legs pass (DEGRADED if the kernel leg is honestly degraded and the
rest pass), else BLOCKED with the failing leg named.* KERNEL is not degraded and passes outright;
CORPUS passes unchanged; SKEPTIC fails — not for the prior reason (staleness), but because the fresh
audit itself surfaced 2 residual BLOCKERs.

**⇒ VERDICT: BLOCKED. Failing leg: SKEPTIC — `attack/faults.md` (round 3) lists 2 BLOCKERs (S3-B1:
an Axler citation-tier promotion propagated to only 1 of 7 sites that need it; S3-B2: the
reconciliation leg's own "what is still open" section makes four false claims about tree state,
already republished as gate status in `attack/synthesis.md`). Conjecture `F` remains OPEN — neither
this gate, nor the reconciliation leg, nor the skeptic re-audit, nor any leg either reads, claims
otherwise.**

Downstream `synthesize` / `write-paper` legs must not treat this run's corpus as seal-ready, and
`attack/synthesis.md` in particular carries a now-identified false claim (S3-B2, item (d) above) that
should not propagate further. The repairs are named precisely by `attack/faults.md` itself (§2, each
BLOCKER's own "Repair" subsection): propagate the L0 tier to the six named sites, and correct the
four tree-state claims in `reconciliation.md` §6–§8 and `synthesis.md` §0/§7/§8/§9 against `git log`.
Neither repair touches the conjecture or any theorem's mathematics.

---

*Artifact of leg `evidence-gate`, molecule `task-20260727-2fee`, run `germ-20260725-791a7c45`,
re-attack loop `reattack-20260726-57d1`, reconciliation leg `task-20260727-264e`, skeptic re-audit
leg `task-20260727-5096`. Sources read: `attack/re-attack/reattack-verdict.json`,
`attack/faults.md`, `attack/reconciliation.md`, `attack/coverage-report.md`,
`attack/re-attack/attack-round-2/faults.md` (superseded, read for the disposition table only). No
number in this document was invented; every figure traces to the cited source file and section. This
document supersedes the prior `evidence-verdict.md` (molecule `task-20260727-30dc`) of the same name
in place.*
