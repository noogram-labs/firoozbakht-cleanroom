# Frame — Stress-test of the Firoozbakht attack-surface decomposition

**Molecule:** `delib-20260725-07fc` (formula `deep-think-inline`, step 1/4)
**Crew role:** skeptic
**Run:** `germ-20260725-791a7c45`
**Artifact under review:** `attack/decompose.md` (produced by `task-20260725-c062`,
leg `decompose`; also mirrored at `<run_dir>/decompose/decompose.md`). Supporting
scripts: `attack/probe.py`, `attack/probe2.py`.
**Panel selection mode:** `panel=auto` → auto-selected from the worker's own
available Claude Code subagents by topic match.

---

## 0. What is being asked, precisely

The commissioning prompt is **not** "is Firoozbakht's conjecture true?". It is:

> Before any downstream compute is spent, is `decompose.md` a *sound frame* for a
> PROVE-or-REFUTE attack on `p_{n+1}^{1/(n+1)} < p_n^{1/n}` (∀ n ≥ 1)?

Three named attack axes in the brief — (a) completeness and non-circularity of the
proof-obligation tree, (b) whether the falsifiability tests have teeth, (c) what
the decomposition quietly assumes. These are **not** three questions; they
decompose into seven orthogonal strates below.

The deliverable is a *recommendation* (weakest branches + what must change),
**not** a mathematical result and **not** nucleated molecules.

---

## 1. Strate-count — SEVEN sub-questions (Q1..Q7)

Two orthogonal properties in one sentence are two strates. The brief's axis (a)
bundles completeness and non-circularity — orthogonal, so Q1 and Q2. Axis (b)
bundles "has teeth" (does failure refute?) with "is the classification right"
(decidable / sufficient / not-a-test) — orthogonal, so Q3 and Q4. Axis (c) is
Q5. Two strates are implied but unstated by the brief and are added because a
recommendation naming "the weakest branches" is unanswerable without them: the
correctness of the difficulty verdicts (Q6) and the ranking itself (Q7).

**Q1 — COMPLETENESS.** Is the proof-obligation tree in §2 exhaustive? Is there a
route to PROVING or REFUTING F that does not pass through any listed node
(P1–P7, R1–R4)? Concretely: does the taxonomy table in §3.0 (Direct /
Contrapositive / Contradiction / Construction / Counterexample / weakening) close
the space of attacks, or is there a legitimate archetype — e.g. probabilistic
method, transfer to an equivalent problem, computational-verification-plus-
structure-theorem, reverse-mathematics / independence — that the tree has no
node for?

**Q2 — NON-CIRCULARITY.** Does any obligation's discharge presuppose F, or
presuppose another obligation that depends on it? Named suspects, to be
adjudicated not merely repeated: (i) §3.2's own admission that a hypothesis
strong enough for S2 may be "a disguised restatement of the target"; (ii) P6′,
whose repair route uses effective `π(x)` bounds (P4) to control `T`'s oscillation
— does that repair anywhere assume the very bound `g_n < T_n` it is meant to
enable checking?; (iii) Corollary A1 is used both to define the search objective
(§3.4) and to justify the refutation route (§3.3, §4.4) — is that a single
derivation used twice, or a loop?

**Q3 — TEETH.** For each of T1–T5 (§4): if the test *fails* (i.e. the sought
object is found / the sought statement proved), does F actually become REFUTED —
with no escape hatch? Equivalently: is each test's refutation-implication a
theorem of the document, or an inference the document asserts? Specifically
adjudicate whether T2 (`ρ_n ≥ 1`) is *exactly* equivalent to T1 or only
equivalent up to the `O(1/L)` in Claim A — because an `O(1/L)`-sized slack is
precisely the width of the margin the document itself calls the conjecture's
fragility (§4.3: bar ≈ 0.971 vs. record ≈ 0.92).

**Q4 — CLASSIFICATION.** Is each test's tag (`[decidable, Σ₁]`,
`[decidable, sufficient]`, `[not decidable]`, `[not a refutation]`) correct? In
particular: §4.3's own claim that it *reversed its direction mid-draft* (T3 is
sufficient, not weaker) is a self-declared near-miss. Re-derive it. Is T3's
sufficiency argument valid **unconditionally** or only on the finite range where
`T_n < L_n²` was checked (`n ≥ 11` up to 216 815)? And is the §4.6 anti-test
(Littlewood oscillation is irrelevant) correctly excluded, or does the
`O(L²·log log log x/√x)` estimate hide a case?

**Q5 — QUIET ASSUMPTIONS.** What does the decomposition assume without tagging?
It has an explicit tagging discipline (`[self-contained]` / `[needs-anchor]` /
tiers L1/L3) — audit whether the discipline is *applied to itself*. Candidate
untagged premises to test: that the smooth surrogate `(x log x)^{1/x}` is the
right model of `p_n` (§3.6); that `n ≈ p_n/L_n` may be substituted inside the
differencing in §2.4; that double-precision arithmetic suffices for the §5.1
table (max ratio reported as `0.9999984` — 7 significant figures from a float
comparison of logs); that `π(x)`'s asymptotic expansion may be inverted term-wise
in §1.3; and the meta-assumption that decomposing into a tree is the right
epistemic move at all.

**Q6 — VERDICT CALIBRATION.** Are the status codes `[E] [O] [X] [C]` correctly
assigned? Is P3 truly `[X]` (out of reach) rather than `[O]`, and is the strong
claim it forces — *"proving Firoozbakht is strictly harder than proving RH is
useful for prime gaps"* (§2.1) — a valid inference or a rhetorical overreach? Is
S9 truly blocked "for two independent reasons"? Is L4 really "the only node that
is a genuine theorem"?

**Q7 — RANKING.** Given Q1–Q6, which branches / tests are **weakest**, in an
order that tells the downstream DAG where NOT to spend compute? This is the
strate the outcomes.md verdict must answer; it is not satisfied by a list of
observations without a priority order and a "what must change" clause per item.

---

## 2. Panel — five personas (auto-selected)

| Persona | Subagent | Disposition required by the brief | Assigned lead strates |
|---|---|---|---|
| **Wheeler** | `wheeler` | question-framing (à la Wheeler) | Q1, Q7 |
| **Feynman** | `feynman` | first-principles (à la Feynman) | Q5, Q6 |
| **Gödel** | `godel` | formal-limits (à la Gödel) | Q2, Q4 |
| **Popper** | `popper` | falsifiability (adds teeth-testing the brief demands) | Q3, Q4 |
| **Knuth** | `knuth` | algorithmic/derivational rigor (audits the in-run numerics) | Q5, Q6, Q3 |

Every persona is asked to *touch all seven* strates and to say "no comment" where
it has none — lead assignment governs depth, not coverage. This is the
anti-silence device: a Q is only marked **Silent** in step 3 if all five declined
without rationale.

---

## 3. Per-persona substitution hypotheses (the falsifiers for step 3)

For each panelist, the most likely EASIER question it answers instead of the hard
one — its known gravitational pull. Step 3 checks each response against its own
row; a match is marked `Substituted (*)` in the coverage table.

**Wheeler — pull: reframing over auditing.**
Substitution hypothesis: instead of asking *"is this tree complete?"* (Q1),
Wheeler proposes a **more beautiful alternative framing** of the whole problem —
"the real question is not whether `p_n^{1/n}` decreases but what information the
prime counting function carries" — and never adjudicates the existing tree.
Secondary pull: auditing *vocabulary* (`T_n`, `ρ_n`, "obligation") rather than
*coverage*. A naming critique is not a completeness verdict.

**Feynman — pull: "is it simple?" over "is it assumed?".**
Substitution hypothesis: instead of surfacing untagged premises (Q5), Feynman
re-derives §1.3 or §3.6 himself, finds them fine, and concludes the document is
sound — answering *"is the visible math correct?"* (easier, and largely already
done by the document's own verification pass) instead of *"what is invisible?"*.
Secondary pull: declaring the whole tree over-elaborate and proposing "just
compute more primes" — a taste verdict, not an assumption audit.

**Gödel — pull: importing incompleteness where it does not bite.**
Substitution hypothesis: instead of auditing this document's actual circularity
(Q2), Gödel answers the adjacent and far more comfortable question *"could
Firoozbakht be independent of PA/ZFC?"* — true-ish, unfalsifiable here, and not
what was asked. Note the document already establishes ¬F is Σ₁ (§1.4); an
independence discussion that stops at "Π₁ statements can be independent" adds
nothing. Secondary pull: formalizing the tree in a logic and declaring it
well-founded — a restatement, not an audit.

**Popper — pull: grading falsifiability instead of testing implication.**
Substitution hypothesis: instead of checking whether each test's failure
*actually entails* ¬F (Q3 — a mathematical implication check), Popper ranks the
tests by *how falsifiable they feel* and praises §4.5/§4.6 for honesty. The
document is already Popper-shaped (it labels T5 "not a refutation" itself);
agreeing with its self-labelling is the easy question. The hard one is whether
T2's equivalence to T1 survives the `O(1/L)` slack.

**Knuth — pull: code review instead of premise audit.**
Substitution hypothesis: instead of Q5/Q6, Knuth audits `probe.py`/`probe2.py`
for sieve correctness and floating-point hygiene, returns a clean numerics
report, and never reaches the strategic verdicts. Sieve correctness is necessary
and welcome — but if that is the *whole* answer, it is a substitution. Secondary
pull: proposing a better algorithm for extending the search (that is the
`notebooks` leg's job, not this deliberation's).

---

## 4. Anti-substitution constraints (per strate: what the answer must NOT be)

- **Q1** — must NOT be a proposed alternative framing of Firoozbakht, and must
  NOT be "the tree looks thorough." It must either name a concrete attack route
  with no node, or state affirmatively that the space is closed and say why.
- **Q2** — must NOT be a general remark that mathematics is subject to
  incompleteness. It must cite a specific node pair (X presupposes Y) or clear
  the three named suspects individually.
- **Q3** — must NOT be a restatement of the document's own tags. Each of T1–T5
  needs a verdict of the form *"failure of this test entails ¬F: YES / NO /
  ONLY-IF ⟨condition⟩"*, with the entailment checked, not quoted.
- **Q4** — must NOT accept §4.3's corrected direction on the document's word. It
  must be re-derived. Range-of-validity (finite check vs. all `n`) must be stated.
- **Q5** — must NOT list assumptions the document has already tagged
  `[needs-anchor]` or listed in §8. Those are declared, hence not *quiet*. Credit
  only for premises the document does not know it is making.
- **Q6** — must NOT defer to the document's own confidence. A verdict of "P3 is
  correctly `[X]`" needs the comparison re-argued; a verdict of "overreach" needs
  the weaker true statement written out.
- **Q7** — must NOT be an unordered list. Ranked, with a "what must change"
  clause per item, and each item must be attributable to a Q1–Q6 finding.

---

## 5. Shared preamble (prepended to every persona prompt)

> You are on a five-member adversarial panel convened **before any compute is
> spent** on a mathematical attack. The artifact under review is
> `attack/decompose.md` in the repository at
> `/Users/eserie/galaxies/firoozbakht-cleanroom/.worktrees/delib-20260725-07fc`
> (read it in full; also read `attack/probe.py` and `attack/probe2.py` if you
> need the numerics). It decomposes **Firoozbakht's conjecture** —
> `p_{n+1}^{1/(n+1)} < p_n^{1/n}` for all `n ≥ 1`, equivalently `p_n^{1/n}`
> strictly decreasing — into a proof-obligation tree, nine candidate strategies,
> and five falsifiability tests.
>
> **The conjecture is OPEN.** You are not asked to decide it. You are asked to
> stress-test the *frame*: is this decomposition a sound place to spend the next
> weeks of compute?
>
> The document is unusually self-aware — it tags its own unverified claims, lists
> its own gaps in §8, and records two direction errors it caught in its own
> verification pass. **This is a hazard for you**: agreeing with its self-critique
> is the easy answer and is worth nothing. Your value is entirely in what it does
> *not* already say about itself. Anything you find that is already in §0, §7 or
> §8 does not count as a finding — say so explicitly and move on.
>
> Address ALL SEVEN questions below. Where you have nothing to add, write
> `Q_k: no comment` — explicitly, so the synthesis can distinguish silence from
> abstention. Depth is expected on your lead strates.
>
> ⟨Q1..Q7 verbatim from §1 above⟩
>
> Return markdown with a `## Qk` heading per question, then a final
> `## Weakest branches (ranked)` section naming concretely which decomposition
> branches (P1–P7, R1–R4, S1–S9, T1–T5, L1–L6) you judge weakest and what must
> change. Use relative paths, never absolute. Pair any locator (`§3.2`, `P6′`)
> with the file it lives in. Do not propose new molecules. Do not write
> "Firoozbakht is true" or "Firoozbakht is false".

## 6. Per-persona tails (appended to the shared preamble)

**wheeler** — *"Your lead strates are Q1 (completeness) and Q7 (ranking). The
temptation you must resist is explicit: do not propose a more beautiful framing
of Firoozbakht, and do not audit the notation. The question is whether §2's tree
and §3.0's archetype table CLOSE the space of attacks. If you believe an
archetype is missing, name it and name the node it would need. If you believe the
space is closed, say so affirmatively and defend it — 'looks thorough' is not an
answer. On Q7, your ranking is the panel's spine."*

**feynman** — *"Your lead strates are Q5 (quiet assumptions) and Q6 (verdict
calibration). The temptation you must resist is re-deriving §1.3 and §3.6 and
reporting they are correct — the document already did that and lists its own
slips in §8. Hunt for the premises it does not know it is making. Start where the
substitutions happen: `n ≈ p_n/L_n` inside the differencing in §2.4; the
term-wise inversion of the `π(x)` expansion in §1.3; the reported
`0.9999984` from a double-precision comparison of logs in §5.1. On Q6, is
'strictly harder than RH is useful for prime gaps' (§2.1) a valid inference?"*

**godel** — *"Your lead strates are Q2 (non-circularity) and Q4 (test
classification). The temptation you must resist is naming: do not spend this
response on whether Firoozbakht could be independent of PA or ZFC — §1.4 already
fixes ¬F as Σ₁ and the question was not asked. Adjudicate the three named
circularity suspects individually (S2's hypothesis, P6′'s use of P4, Corollary
A1's double duty). On Q4, re-derive §4.3's T3⇒T2 direction from scratch and state
whether it holds for all `n` or only on the checked range."*

**popper** — *"Your lead strates are Q3 (teeth) and Q4 (classification). The
temptation you must resist is grading the tests for falsifiability-as-virtue and
praising §4.5/§4.6 — the document already labels T5 a non-test. Your job is the
implication check: for each of T1..T5, does FAILURE of the test ENTAIL ¬F? Answer
YES / NO / ONLY-IF ⟨condition⟩ and show the entailment. Give special attention to
whether T2 is exactly equivalent to T1 or only equivalent modulo the `O(1/L)` in
Claim A — and whether that slack is smaller or larger than the ~5% margin §4.3
calls the conjecture's fragility."*

**knuth** — *"Your lead strates are Q5, Q6 and Q3. The temptation you must resist
is stopping at a code review of `attack/probe.py` and `attack/probe2.py` — audit
them, yes, but a clean numerics report alone is a failed answer. Carry the
numerics into the strategic verdicts: does the §5.1 evidence actually support
'55.9% of steps decrease' as stated (is that statistic computed on the true `T_n`
or on its asymptotic surrogate?), and does 'all six tightest ρ cases are record
gaps' at n≤216815 carry any weight at all for P6′, or is it a small-sample
artifact? On Q6, is L4 really the only genuine theorem in §6's L1–L6?"*

---

## 7. Step-3 contract

`synthesis.md` must carry the coverage table over exactly Q1..Q7, one mark each
(Treated / Substituted / Declined-with-rationale / Silent), with substitutions
attributed to the persona and matched against §3 above. A **Silent** mark on any
Q is the alarm signal and must be surfaced in `outcomes.md` as a follow-up
recommendation.
