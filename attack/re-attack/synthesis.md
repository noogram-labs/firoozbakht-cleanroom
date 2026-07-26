# synthesis.md — round-by-round trajectory of the re-attack loop

**Molecule:** `reattack-20260726-57d1` (formula `converge-math-attack`, `rounds=2`)
**Subject:** Firoozbakht's conjecture — `p(n+1)^(1/(n+1)) < p(n)^(1/n)` for all `n≥1`
**Final verdict:** **BLOCKED** (`rounds-exhausted`). Full detail in `reattack-verdict.json`.

## The conjecture, throughout

`F` is stated OPEN at the start of round 1 and remains OPEN at the end of round 2. Nothing in
either round moves it in either direction. This is the honest, expected outcome for a `Π₁`
statement open since 1982, and every leg in both rounds says so explicitly rather than asserting
or assuming it.

## Round 1 (upstream, pinned — read, never re-run)

The spore's original `skeptic` (`task-20260725-488f`) and `lean-probe` (`task-20260725-9975`)
legs. Kernel: `UNPROVABLE_IN_BUDGET` — four of five skeleton `sorry`s discharged (the equivalence
chain), one live `sorry` remaining (the conjecture itself, correctly untouched). Skeptic: 2
BLOCKERs.

- **F1** — the index `m(n)` / "governing record index" carried three inequivalent definitions
  across three artifacts, with two siblings publishing opposite-looking headline trends because
  they measured different things under the same name.
- **F2** — `proof-attempt-0.md` Theorem C(b)'s cited bound (A-high) did not follow from its stated
  justification and was false by a factor `≈38` over part of its range, though its *conclusion*
  was independently true under a corrected (tight) bound.

A prior run of this exact formula (`reattack-20260725-4db5`) ran with `rounds=1` (the early-exit
path), read this same round-1 state, and collapsed `BLOCKED` with the explicit recommendation to
re-germinate with `rounds≥2`. This molecule is that re-germination.

## Round 2 (nucleated by this loop)

Three proof-attempts (one per subquestion, fed round 1's faults + the still-unproved list), one
lean-probe (fork discipline: fed only the unproved list, run in parallel with the attempts, not
blocked by them), one skeptic (blocked by all four). One worker (`task-20260726-8ba0`, the
lean-probe) started with an idle tmux session that never received its prompt — recovered by
resending the briefing manually; a subsequent transient `cs done` trunk-lock race resolved itself
on retry with no data loss (verified via `git worktree list`/`git log` — the branch merged
cleanly, nothing was left uncommitted).

**What round 2 fixed, mathematically — genuinely, not by re-wording:**

- **F1 is FIXED.** The `first-failure-maximality` attempt names the three predicates explicitly
  (`P6′-pair`, `P6′-gov`, `P6′-min`), adds a fourth the run had never isolated (`P6′-rec`), assigns
  every circulating measurement to the predicate it actually measures, reconciles both
  notebooks' headlines without retracting either, and goes further than repair — it *refutes*
  `P6′-pair` outright with two independently-reproduced numerical witnesses. The round-2 skeptic
  independently re-derived every witness and margin and confirms this is a genuine mathematical
  advance (new Theorem 1, new Proposition 4 proving `gov` and `min` are formally incomparable),
  not a rewording.
- **F2 is FIXED as mathematics — by both legs independently, which is exactly the new problem.**
  Both the `unconditional-verified-range` and the `first-failure-maximality` attempts correctly
  restated the bound in its tight form and *re-derived* (not re-swept) the corrected constant. The
  round-2 skeptic independently re-derived all three steps of each repair at 50 decimal digits and
  confirms both are correct as mathematics.

**What round 2 could not close: reconciliation across a widened fan-out.** The skeptic's
verdict is 3 BLOCKERs, all of the same species — none of them a mathematical error, all of them a
seam between artifacts that nobody owned:

- Two legs repaired the same BLOCKER (F2) into two *different* theorems, with different
  constants, off different bibliographic rows, and neither cites the other (R2-B1).
- The two legs assign the same source contradictory bibliographic tiers on the same day, and the
  ledger amendment one of them reports as landed was checked directly and never made (R2-B2).
- One repair's citation was independently shown (byte-level PDF fetch, MD5-pinned) to exist only
  in a preprint edition, absent from the published journal version — an edition-fragile citation,
  unflagged (R2-B3).

Three further MAJORs point the same direction: the round-2 skeptic's own adjudication of an
inherited statistic dispute is itself inverted (R2-M1); round-1's exact "unconditional-label" fault
pattern reappears in a branch round 1 had passed clean (R2-M2); and one attempt's own proof
disproves an ordering its own prose still asserts (R2-M3).

## Did the unproved list shrink, or churn?

**It did not shrink — expected, since the one remaining `sorry` is the conjecture itself.**
`unproved-1` = `unproved-2`, unchanged, one entry. What changed is the *quality* of the attempt:
round 1 declined to attempt the conjecture; round 2 attempted it and failed honestly (`exact?`,
`aesop`, `decide` all fail as expected on an open `Π₁` problem), and went further — it *proved* that
the one classical route available in Mathlib (Bertrand's postulate) is provably insufficient at
every `n ≥ 2` (new sorry-free theorem `bertrand_ceiling_above_threshold`), closing off a route
rather than merely failing to walk it. That is real, if modest, progress on the kernel leg, even
though the sorry count itself is unchanged.

**Did the BLOCKER set shrink, or churn?** Neither, cleanly — it changed **species**. The 2
round-1 BLOCKERs (concrete mathematical/definitional defects inside individual artifacts) were
both genuinely fixed. But the fan-out that fixed them **widened** (two legs now both touch
Theorem C(b) where one did before) and introduced 3 new BLOCKERs of a **different kind**
(cross-artifact reconciliation failures) that a fan-out-only architecture cannot close by
construction — round 1's own skeptic predicted exactly this failure mode (§6: *"the predictable
failure mode of a fan-out with no reconciliation stage"*), and round 2 confirmed the prediction on
itself.

## Why the loop stops here, not because it gave up early

`rounds_target = 2`. Round 2 is the last round this loop is authorized to run. The stop condition
(kernel PROVED **and** skeptic clean, in the same round) never held in round 1 or round 2. The
`while round < rounds` guard is now false (`2 < 2`), so no round 3 was nucleated — this is the cap
working as designed, not silent exhaustion: `reattack-verdict.json` records `exit_reason:
"rounds-exhausted"` and names every unconverged finding explicitly.

## Escalation — what a round 3 (if funded) should be

Both the round-2 skeptic (`faults.md` §7) and this synthesis agree: **round 3 must not be another
fan-out.** More proof-attempts would likely widen the reconciliation debt further, not close it.
What is missing is a single reconciliation leg: designate one repaired Theorem C(b) — the
mathematics favors `Theorem C-b'` (`0.998244`, Axler row `x₀=6690557`, present in both editions of
the source) over `Theorem C(b*)` (`0.99565`, row `x₀=1772201`, preprint-only) — land the
`axler2014newbounds` tier amendment in `source-ledger.md` and `concept-cards/T1` exactly once,
recount the disputed `55.92%` three-fractions statistic from the raw statement (this round's own
skeptic disputed round 2's own count), and make the four round-2 artifacts cite each other. None of
that is new research; all of it is what a downstream `write-paper` or `synthesize` leg would
otherwise have to guess at. **The conjecture `F` itself remains OPEN, unaffected by any of this —
neither this loop nor a hypothetical round 3 bears on whether Firoozbakht's conjecture is true.**
