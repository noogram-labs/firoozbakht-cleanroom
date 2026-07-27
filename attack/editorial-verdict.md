# editorial-verdict.md — fail-closed editorial gate on the Firoozbakht paper

**Molecule:** `review-20260727-2c6d` (formula `temp-review`, crew role: **reviewer**) — **ROUND 3**
**Run:** `germ-20260725-791a7c45` · **Date:** 2026-07-27
**Target:** `paper/paper.tex` (2733 l.) + `paper/references.bib` (22 entries) + `paper/paper.pdf`
**Conjecture (`F`):** `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`. **`F` is OPEN.**
Nothing in this verdict proves or refutes it, and nothing in the paper claims to.

> **This document supersedes, in place, the round-2 `editorial-verdict.md`** (molecule
> `review-20260726-7d55`, commit `42f023a`, on the 2460-line round-2 paper). The galaxy ends with
> exactly one current editorial verdict. **§5 states plainly what changed since round 2 — read it
> before quoting either document.**

**Author ≠ scorer.** This leg wrote no line of `paper.tex`, and no line of any gate artifact it
scores. Where a claim must change, that is a REWRITE instruction for the author, not an edit made
here.

---

## VERDICT: **REWRITE**

**One dispositive check fails, and two secondary ones.**

1. **The evidence gate is BLOCKED.** `attack/evidence-verdict.md` (round 3 v2, molecule
   `task-20260727-2fee`) reads `VERDICT: BLOCKED`, failing leg **SKEPTIC**, on the two BLOCKERs
   of `attack/faults.md` (S3-B1, S3-B2). **This is not an honest DEGRADED**: the DEGRADED
   carve-out exists for a degraded *kernel* leg, and the kernel leg here passes **outright**
   (`formal_backend = 'lean'`, not `'none'`; `lake build` exit 0 over 2208 jobs from a cold cache;
   `lake env lean audit_exhaustive.lean` exit 0; exactly one `sorryAx` dependent over 63
   declarations, namely the conjecture). Fail-closed rule: SHIP requires the evidence gate at PASS
   or honest DEGRADED. **This alone forecloses SHIP, independently of everything below.**

2. **One OVERCLAIM row about the corpus's own state — G7-a.** §9.5 states that what remains
   outstanding is "a re-audit against the round-3 state." That re-audit has run
   (`cite-20260727-df58`, commit `327ba72`) and returned **PASS** — and it **superseded
   `attack/verification-report.md` in place**, so the figures §9.5 quotes (22 citekeys, 91 `\cite`
   instances, 59 locator pairs) no longer exist at the path §9.5 sends the reader to, which now
   reads 21 and 94. This is the S3-B2 species again, in the same section, for the third
   consecutive round.

3. **One UNSUPPORTED-CITATION row — G7-b — against the *gate*, not the paper.**
   `attack/verification-report.md` returns PASS on "**21/21** citekeys" and "grep → 21 unique
   keys… no citekey in `paper.tex` lacks a ledger row." **The paper has 22.**
   `ferreira2017consequences` — 9 `\cite` instances, tied for most-cited, five distinct locators,
   the sole support for the paper's `thm:io` — is absent from the audit's per-citekey table, whose
   own instance counts sum to **85** of the **94** it claims to have checked. The nine locators
   were checked here, one by one, against `source-ledger.md:343` and **all resolve**, so the paper
   itself carries no unsupported citation; what is unsupported is the gate's claim of complete
   coverage.

Plus one narrow OVERCLAIM inside the paper (**V-abstract**, §1 row below) — one clause, and the
smallest item on this list.

**Zero UNADDRESSED-FAULT.** Both round-3 BLOCKERs, both MAJORs and all five MINORs are named in
`\S`\ref{sec:defects}, at the right altitude, without softening. **The mathematics survived every
check this leg could run**, including nine constants re-derived here from the statements — see §2.

**Delivery posture is not this gate's call.** REWRITE is a verdict on the artifact against the
gate rule, not a recommendation about whether or where the operator stages this paper.

---

## 1. Per-claim verdict table

Full ledger: `attack/claims-ledger.md` (62 rows, committed at `78e26f4`). Reproduced here: every
non-CONFIRMED row, plus the load-bearing CONFIRMED rows a reader needs in order to see what the
REWRITE does **not** touch.

| Claim | Tag | Evidence |
|---|---|---|
| **G1 / V1** — the corpus's evidence gate stands at BLOCKED, and the paper reports it accurately (abstract l.96; §9.3; §9.3 box l.2513) | **gate failure** (not a claim defect) | `attack/evidence-verdict.md`: `VERDICT: BLOCKED`, failing leg SKEPTIC round 3, on S3-B1 + S3-B2. Kernel leg passes **outright**, so the honest-DEGRADED carve-out does not apply. The paper's *reporting* of the gate is exact; the *gate* is what fails. |
| **G7-a** — §9.5: "what is outstanding is therefore a re-audit against the round-3 state"; and the quoted round-2 audit figures 22 / 91 / 59 | **OVERCLAIM** — false statement about the corpus's own state, understating the paper's provenance | The round-3 re-audit exists: `attack/verification-report.md`, molecule `cite-20260727-df58`, commit `327ba72`, **verdict PASS**, and it **superseded the round-2 report in place**. A reader following §9.5's own pointer finds 21 citekeys and 94 instances where the paper says 22 / 91 / 59, with no supersession note. Direction of error is the same as round 2's V2: the paper claims *less* clearance than it has. It is nonetheless a false assertion inside the one section whose entire purpose is accurate provenance reporting. |
| **G7-b** — the citation gate's own coverage claim: "21 unique citekeys", "21/21 citekeys: OK", "no citekey in `paper.tex` lacks a ledger row" | **UNSUPPORTED-CITATION** (against `attack/verification-report.md`, not against `paper.tex`) | Independent extraction here: `grep -oE '\\cite[a-zA-Z]*(\[[^]]*\])?\{[^}]+\}' paper/paper.tex`, comma-expanded → **22** distinct citekeys, **94** instances. `ferreira2017consequences` (9 instances: §1, Thm.2.2 ×2, Lem.3.2, Cons.3.3, Thm.4.5, Thm.5.1, Thm.5.2, bare) is missing from the audit's table, and that table's per-key counts sum to 85 = 94 − 9. The report's stated explanation for differing from round 2's "22" (four camelCase/underscore renames) does not account for it — those four appear in both counts. **Mitigating, so the REWRITE is correctly sized:** the omitted key is at ledger tier **L0** with a full statement table, and all nine locators were verified here to match it exactly. No citation in the paper is fabricated, mis-located, or ledger-less. |
| **V-abstract** — abstract l.85: "first-failure maximality now holds against all primes below `0.94970 p_{n₀}` **on Dusart alone**" | **OVERCLAIM** (narrow) | `thm:Ca` carries `𝒫·s`, and the paper's own `haz:uncond` is the finding that *this exact phrasing* is the defect it faults upstream (FFM l.751, "unconditionally, on Dusart alone"), because the weakest link is the `2⁶⁴` verification height — which rests on `oliveira2014goldbach`, **never opened** — and not Dusart. The clause asserts the source basis without the height, in the one place where the confidence codes are not visible. Round 2's V3 was the same failure mode in the same place. One clause to fix. |
| **S1** — `F` is open; neither proved nor refuted in any round (abstract; §1.3; §1.4 box; §10) | **CONFIRMED** | `evidence-verdict.md` §0; `faults.md` §6; `reattack-verdict.json` `kernel: UNPROVABLE_IN_BUDGET`. The paper says so in the abstract, in a boxed statement, in the conclusion and in the colophon. |
| **S3** — the narrowed vocabulary rule: no statement asserted above its code; *machine-checked* reserved for `𝒦` | **CONFIRMED** | All 10 occurrences of "machine-checked" grep-verified here: title, abstract, §1.2, §1.4, §1.5, `lem:reduction`, §3 heading ×2, conclusion ×2 — every one refers to `lem:reduction` or the §3 barrier theorems. Round 2's over-wide promise is explicitly **withdrawn** at l.347–350 rather than quietly broken. |
| **K1–K4** — the kernel leg: reduction machine-checked; three `sorry`-free barrier theorems; 63 declarations, one `sorryAx` | **CONFIRMED** | Evidence-gate KERNEL leg **PASS**, re-executed from a cold cache by the round-3 skeptic (`faults.md` §1), not read from a report. `Statement.lean` SHA-256 `6528868…04e004c1` reproduced by two independent legs. **Passing the kernel leg is not "proved", and the paper says so in its own box (§9.3 l.2516).** |
| **M10, M11, M17, M19** — `B(2⁶⁴) = 1919.13798349753288…` (so `g ≥ 1920`); `p* = 777 600.744…`; `A = {n : B_n < T_n} = {1,2,3}` (both `<` and `≤`); critical constant `= 2/e` | **CONFIRMED — re-derived here** | `mpmath` at 40 dps, written from the paper's statements: `log 2⁶⁴ = 44.36141955583649980…`, `B(2⁶⁴) = 1919.1379834975328856…`, largest even `g` with `S♯(g) ≤ 2⁶⁴` is **1918**, `p* = 777 600.7442975646…`, `A = {1,2,3}` both ways, `2/e = 0.7357588823428846431…`. All identical to the paper. |
| **M3** — the second refuting witness is the **28th** maximal gap | **CONFIRMED — re-derived here** | Own running-maximum enumeration to `2·10⁸`: **28** records, 12th at `15 683` (`g = 44`), 28th at `191 912 783` (`g = 248`), **25** below `10⁸`. Round 1's "27th" is correctly retired. |
| **M12–M15** — `thm:Ca` (`0.94970`), `thm:Cb` (`0.998244`, designated), the retired repair, and the thin `2.4·10⁻⁸` margin | **CONFIRMED** | Constants re-derived from the statements by `faults.md` §1 (`s3_constants.py`): majorants `0.0515990267` / `0.00175687590387`, tails, exact requirements, margin `2.41·10⁻⁸` — all match. `faults.md` §5 attacked the designation and the theorem and **could not break either**. The retired constants were hunted corpus-wide: no surviving live use. |
| **C1** — exhaustive sweep to `10¹¹`, 4 118 054 812 pairs, no violation, `max_{n≥10} g_n/T_n = 0.8318` | **CONFIRMED** (not re-run at full range here) | Own sieve to `10⁹`: **0 violations**, `max_{n≥10} g_n/T_n = 0.78960` at `n = 1 319 945` — consistent with the record being attained above `10⁹`. `π(10¹¹) = 4 118 054 813` ⇒ 4 118 054 812 consecutive pairs ✓. §9.6 correctly forbids reading the sweep as a verification of `F`. |
| **G6** — the ledger is 22 rows: 13 L0 / 4 L1 / 3 L2_strong / 2 L2_weak / 0 L3 | **CONFIRMED — recounted here** | Counted directly from `source-ledger.md`'s 22 row headers: exactly 13 / 4 / 3 / 2, zero L3. The 22 ledger rows are in bijection with the 22 citekeys. **The paper's count is right and the audit's is not.** |
| **G3, G4, G5** — the paper's restatements of S3-B1, S3-B2 and all seven sub-blocking findings | **CONFIRMED — zero UNADDRESSED-FAULT** | Every BLOCKER and MAJOR in `attack/faults.md` is named in §9.3 at the blocking level, and all five MINORs immediately below it, including the two — S3-M1's quotable paragraph and S3-M2's mis-credited script — that reflect badly on the corpus. Neither BLOCKER names `paper/paper.tex` as a site needing correction; the paper is the artifact that *reports* them. G4 additionally records the paper's **own** round-2 edition as the origin of S3-B2. |
| **G10** — `rem:structural`: three rounds have failed at the same step, and the round-2 one-leg estimate was wrong and should be discounted | **CONFIRMED** | The verdict trail bears it out, and this leg adds a fourth instance (G7-a/G7-b). Self-criticism at this altitude is rare and is the paper's strongest editorial feature. |
| **G11** — "This paper is an honest report on a blocked corpus. It is not a seal." | **CONFIRMED** | Accurate. It is the sentence that makes the rest of the paper safe to read. |

**Tally: 2 OVERCLAIM (G7-a, V-abstract) · 1 UNSUPPORTED-CITATION (G7-b, against the gate
artifact) · 0 UNADDRESSED-FAULT · all other rows CONFIRMED.**

---

## 2. What the REWRITE does *not* touch

Stated because a bare "REWRITE" reads as a judgement on the mathematics, and it is not.

- **No mathematical error was found, in this round or the last.** Every constant this leg could
  re-derive independently — nine of them, at 40 dps or by its own sieve — matched. The round-3
  skeptic re-derived the rest from the statements with scripts it wrote before opening anyone
  else's, and it attacked the designated theorem specifically and could not break it.
- **The kernel leg is clean and was re-executed, not read**, twice, from a cold cache.
- **No citation in the paper is fabricated, orphaned or mis-located.** 22 citekeys, 22 ledger
  rows, one-to-one in both directions; zero at the recall tier. The one key the gate failed to
  audit was audited here instead, and passes.
- **The two remaining OVERCLAIM rows both understate the work.** Neither inflates `F`'s status,
  neither touches a theorem, and neither would change a number.
- **`F` is untouched.** It is open. No round moved it, and the paper never says otherwise.

The REWRITE is carried, in order of size, by: a gate that is BLOCKED for bookkeeping reasons in
*other* artifacts; a provenance section that went stale within minutes of being written for the
third round running; a citation audit that checked 21 of 22 keys while reporting complete
coverage; and one clause in the abstract.

---

## 3. Named REWRITE reasons — what has to change, and where

| # | Reason | Owner | Fix |
|---|---|---|---|
| R1 | Evidence gate **BLOCKED** (S3-B1: Axler tier L0 propagated to 1 of 7 sites — five concept cards, `INDEX.md` in two places, one round-2 proof attempt; S3-B2: four false tree-state claims in `reconciliation.md` §6–§8, re-published in `synthesis.md` §0/§7/§8/§9) | corpus, not the paper | Amend the six sites to L0 with the two standing ⚠; correct the four claims against `git log`; strike `INDEX.md`'s next-action 2. `faults.md` §2 names every site. **Then re-run the evidence gate.** No mathematics is involved. |
| R2 | **G7-a** — §9.5's "outstanding re-audit" is done, and the report it quotes was superseded in place | paper author | Replace the paragraph with the round-3 audit's actual result (PASS, `327ba72`) and its actual figures, and note that the round-2 figures live only in that report's own "what changed since round 2" section. Reasons 2 and 3 of §9.5 ("a PASS that carries caveats is not a clearance of them"; two load-bearing sources under-opened) survive verbatim and should stay. |
| R3 | **G7-b** — the citation gate reports coverage it does not have | citation-audit leg | Add `ferreira2017consequences` to the per-citekey table (tier L0; nine locators, all verified here against `source-ledger.md:343`), correct the headline to 22 citekeys, and reconcile the table's instance sum with its own headline count. Then re-issue. **This is a re-issue, not a re-audit: the substance passes.** |
| R4 | **V-abstract** — "on Dusart alone" asserts above `thm:Ca`'s `𝒫·s` code where the codes are invisible | paper author | One clause: "…on Dusart alone, given the published `2⁶⁴` verification height…". `haz:uncond` already contains the wording. |
| R5 | *(carried, not blocking)* S3-M1's two surviving upstream sites still label `thm:Ca` "unconditional, Dusart only" | corpus | The paper already records this at §9.3 and `haz:uncond`. Named here so the next round's brief does not have to rediscover it. |

R2, R3 and R4 are between one clause and one table row each. R1 is the one that costs a leg — and
none of it is mathematics.

---

## 4. DISSENT

*Required, non-empty, and not a formality: the most interesting tension in the work.*

**The dissent is against this galaxy's own theory of its problem — including the theory this
verdict has just used to size its REWRITE.**

`faults.md` §6 states the structural reading the whole corpus has adopted: *"the corpus's problem
has moved from mathematics to bookkeeping, and bookkeeping is now the cheaper thing to get
right."* The paper endorses it (`rem:structural`), the evidence gate endorses it, and §3 above
prices four of its five REWRITE reasons as one-clause edits on that basis. **The round-3 evidence
disconfirms it, and this leg is the fourth consecutive data point.**

Consider what actually happened in round 3, in order. A reconciliation leg was funded *specifically*
to stop legs from describing a tree they had not checked. It closed every seam it was pointed at
— and then described the tree from memory in its own §6–§8, wrongly, four times. A skeptic leg
caught that, and correctly called it "the same fault the leg was created to fix." A paper was then
written that names the failure, diagnoses its origin as an eleven-minute-stale snapshot in its own
predecessor, and rewrites §9.5 to be the refresh — **and §9.5 went stale again, within minutes,
in the same way, about the same gate.** A citation-audit leg then ran, correctly found that the
paper no longer carries the false claim, returned PASS — **and in the same document asserted
"21/21 citekeys, no citekey lacks a ledger row" about a file with 22, its own table summing to 85
of the 94 instances it claimed to check.** Four legs, four rounds of explicit warning, one
identical failure: *an unchecked assertion about the state of a countable thing, made inside the
document whose job was to check it.*

If that failure were bookkeeping, four consecutive warnings would have suppressed it. They did not
suppress it once. So the honest reading is the *opposite* of the corpus's: this is not residual
tidying that one more careful leg clears — it is a **structural property of a pipeline in which
every leg's verification budget is spent on the mathematics it owns and none on the sentences it
writes about other legs' artifacts**, while the artifacts move underneath it between commit and
read. Note the shape of the evidence: **every mathematical claim in this corpus that anyone
re-derived, held** — nine here, a dozen in `faults.md` §1, the designated theorem under direct
attack. **Every claim about the state of a file, made without running `git log` or a `grep -c`,
failed.** The corpus is measurably better at hard mathematics than at counting its own citekeys,
and it has been for three rounds, and it does not believe this about itself.

There is a second, sharper edge, and it is the one that should worry the next brief most. Round 3's
BLOCKERs and this leg's G7-b share a *direction*: every one of them is a **false negative fact** —
"no audit exists," "Axler is unopened," "no citekey lacks a ledger row," "what is outstanding is a
re-audit." Negative facts are exactly the assertions a reader cannot spot-check by reading forward,
and exactly the ones that cost a downstream leg a funded round when wrong (`faults.md` S3-B2 item 3
makes this argument about `INDEX.md`, and then the corpus made the same error twice more). Yet no
brief in three rounds — including this one's — has required a leg to *enumerate before asserting a
negative*. `grep -c` is cheaper than every re-derivation in this document. **The missing discipline
is not another reconciliation pass; it is a rule that no leg may assert a negative fact about an
artifact it has not just counted.** That rule would have caught S3-B1, S3-B2, G7-a and G7-b — all
four — and it costs seconds.

And the dissent turns finally on this verdict itself. §3 prices R2, R3 and R4 as one-clause fixes.
On the argument above, that price is the same optimism the corpus has been wrong about three times
running, and this leg should be discounted the way `rem:structural` asks the reader to discount
round 2's estimate. **The paper is the strongest artifact in this galaxy** — it is more accurate
about the corpus than the corpus is, it named its own edition as the origin of the corpus's worst
defect, and it holds `F` open in four separate places. It is being blocked by the bookkeeping of
documents that are downstream of nothing. If the operator ever decides the gate rule is measuring
the wrong artifact, this is the round where that argument became available — and it is *not* this
gate's call to make. Fail-closed means fail-closed: **REWRITE**.

---

## 5. What changed since round 2

| round-2 finding (`editorial-verdict.md`, commit `42f023a`) | round-3 status |
|---|---|
| **V1** — evidence gate BLOCKED on R2-B1 / R2-B2 / R2-B3 | **Still BLOCKED, entirely different reasons.** All three round-2 BLOCKERs are **closed**, each verified by the round-3 skeptic against the tree rather than against a report; 12 of round 2's 13 findings closed by independent re-derivation. Two new BLOCKERs opened (S3-B1, S3-B2), both cross-artifact bookkeeping, neither mathematical, neither touching `F`. |
| **V2** — the paper asserted four times that no citation audit existed | **FIXED**, and honestly: §9.5 states the audit exists, returned PASS, and names its own false assertion as the first item of the revision. **But the same section has gone stale again — G7-a.** |
| **V3** — the "*proved* is reserved for `𝒦` without exception" promise had ≥5 breaches, the first in the abstract | **FIXED.** The promise is explicitly **withdrawn** (§1.4 l.347–350) and replaced by a narrower rule the paper keeps; verified here across all 10 "machine-checked" sites. **Residue: one abstract clause — V-abstract.** |
| citation gate | round 2 **PASS** (22/22, 91 instances). round 3 **PASS**, **but 21 of 22 audited** — a *new* defect, found by this leg (G7-b), not by the gate. |
| **New in round 3** | A reconciliation leg and an independent post-reconciliation skeptic re-audit both ran and are both read as authoritative here. `faults.md` and `verification-report.md` each superseded their predecessors **in place**; so do `claims-ledger.md` and this document. |
| paper | 2460 → 2733 lines. Every round-3 decision applied at its point of use: the corrected ordinal, the index/pair census, the retired repair, the recorded `2.4·10⁻⁸` margin, the requalified decay exponent, the vindicated denominators, and a rewritten §9.3/§9.5. |
| verdict | round 2 **REWRITE** (2 checks failing) → round 3 **REWRITE** (1 dispositive + 2 secondary). The two round-2 claim defects are fixed; the gate is still shut, for reasons that have moved one more step away from the mathematics. |

---

## 6. Fail-closed rule, applied

| Check | Required for SHIP | Actual | Pass? |
|---|---|---|---|
| Evidence-gate verdict | PASS or honest DEGRADED | **BLOCKED** (failing leg SKEPTIC; kernel passes outright, so DEGRADED does not apply) | ❌ |
| Citation-gate `verification-report.md` | **PASS**, present | **PASS**, present — but its coverage claim is false (21 of 22) | ⚠ present + PASS, so the *presence* condition holds; **G7-b** is scored as a named UNSUPPORTED-CITATION row |
| OVERCLAIM count | 0 | **2** (G7-a, V-abstract) | ❌ |
| UNSUPPORTED-CITATION count | 0 | **1** (G7-b) | ❌ |
| UNADDRESSED-FAULT count | 0 | **0** | ✅ |
| Paper artifact present, non-empty, tracked | yes | yes (2733 l., committed) | ✅ |
| Evidence-verdict present | yes | yes | ✅ |
| Verification-report present | yes | yes | ✅ |
| DISSENT section non-empty | yes | §4 | ✅ |

**⇒ REWRITE.** Never SHIP on absent evidence — and never SHIP on a BLOCKED gate. The evidence
here is present and abundant; it says the corpus is not clean.

### Tracked-delivery contract, verified across the whole run

`git ls-files attack paper trace` → **140 tracked files**, including `paper/paper.tex`,
`paper/references.bib`, `paper/paper.pdf` (a LaTeX toolchain was present), `trace/briefs.md`,
`trace/events.jsonl`, `trace/hashes.tsv`, `trace/build_trace.py`, and the full `attack/` tree.
`git status --short attack paper trace` → **empty**. Every deliverable of every leg is committed
in the galaxy's own history. **The contract held; it is not a REWRITE reason.**

---

*Artifact of leg `review`, round 3, molecule `review-20260727-2c6d`, run `germ-20260725-791a7c45`.
Supersedes the round-2 `attack/editorial-verdict.md` (molecule `review-20260726-7d55`, commit
`42f023a`) in place. Sources read: `paper/paper.tex`, `paper/references.bib`,
`attack/evidence-verdict.md`, `attack/verification-report.md`, `attack/faults.md`,
`attack/reconciliation.md`, `attack/source-ledger.md`, `attack/coverage-report.md`,
`attack/re-attack/reattack-verdict.json`. Independent recomputation: own segmented sieve to `10⁹`
and `mpmath` at 40 dps; own citekey extraction over `paper/paper.tex`. No line of `paper.tex` was
edited by this leg. **`F` remains OPEN.***
