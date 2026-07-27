# firoozbakht-cleanroom — an agent fleet attacking an open conjecture, published exactly as it was generated

This repository **is** the working directory the fleet ran in. Nothing was copied here, nothing was staged, nothing was scrubbed. The agents wrote into this tree, committed on their own branches, and `cs done` merged them — 129 commits across three rounds. Publishing it was one `git push`.

That is the claim being demonstrated, and it is worth stating plainly because [the first run of this same spore could not make it](https://github.com/noogram-labs/firoozbakht): there, every deliverable landed in a git-ignored state directory, so the galaxy's tree stayed empty and publication needed a hand-built copy with a scrubbing pass. Here the deliverables are tracked artifacts of the run itself.

## What was attacked

**Firoozbakht's conjecture** — that `p(n+1)^(1/(n+1)) < p(n)^(1/n)` for every `n ≥ 1`, equivalently that `p_n^(1/n)` is strictly decreasing. It is open.

**It is still open.** Nothing here proves or refutes it, and nothing here claims to. What the run produced is a precise account of *where* the obstruction sits, what can be established unconditionally, and what a machine kernel would and would not certify.

## The result, stated the way the run stated it

**This galaxy has run two rounds.** Round 1 attacked the conjecture; its loop refused to pass and named two repairable defects. Round 2 was then run **on this same galaxy, resuming from round 1's own artifacts** — nothing was re-germinated, nothing was copied. Everything below is the round-2 state, which supersedes round 1 in place.

| Gate | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| Evidence gate | **BLOCKED** — 2 skeptic blockers | **BLOCKED** — 3 *new* blockers | **BLOCKED** — 2 blockers, both clerical |
| Citation gate | **BLOCKED** — 2 citekeys | **PASS** | **PASS** — held through a full rewrite |
| Editorial verdict | **REWRITE** | **REWRITE** | **REWRITE** |

**Round 2 fixed round 1's defects and produced new ones.** Both round-1 blockers were closed by independent re-derivation — including a theorem whose printed bound was false by a factor ~38 while its conclusion was true. But three new blockers appeared and the count went 2 → 3. The list churned rather than shrank.

**Round 2's skeptic diagnosed why, and it is the sharpest observation in the repository.** All three new blockers were **seams, not steps** — not one was an error inside a proof. They were two legs repairing the same fault differently, two legs assigning one source opposite tiers, and one leg's repair resting on a citation the other leg had already shown to be edition-only. Round 1 had predicted exactly this failure mode: *"a fan-out with no reconciliation stage … nobody owned the seams."* Round 2 doubled the fan-out and still had no reconciliation stage. *"The loop is not converging on this axis; it is widening."*

**Round 3 was therefore not another fan-out.** It was a single reconciliation leg with five decisions and no new research — pick one repaired theorem, pick one tier, land one ledger amendment, recount one disputed statistic from the statement, make the artifacts cite each other — followed by an independent skeptic re-audit.

What that produced:

- Of the seven inherited findings, **five closed and two remain**, each with exact file and line.
- One "blocker" turned out **not to exist**: the ledger amendment round 2 reported as never landed *had* landed. Round 2's `faults.md` was committed on a branch cut before the merge, so its line numbers only resolved in the pre-merge tree. A seam manufactured by branch timing.
- The disputed statistic was **recounted from the statement** by three separate parties. The reconciliation and the round-3 skeptic agree with each other and **disagree with both earlier skeptics** — the correct figure had been in the original proof attempt all along, corrupted by round 1's skeptic and then "confirmed" by round 2's, which reproduced the wrong document faithfully. Agreement with a predecessor is not correctness.
- The two survivors are **propagation work**, not mathematics: a tier decision that reached one sibling artifact and not five others.

So the blocker trajectory is 2 → 3 → 2, and the kind changed. That is what a reconciliation stage buys, and what a third fan-out would not have.

The conjecture is neither proved nor refuted, across all three rounds.

### The reviewer caught the paper misreporting itself

The most useful thing in this repository is a failure. The paper stated, in its abstract and in §10.3, that *"the citation audit for this paper has not been run, and no citation clearance is claimed."* The audit **had** run, and had returned BLOCKED, naming two citekeys. A different model, on a different formula, compared the prose against the verdict that actually existed on disk and filed it as an overclaim.

That is what author-≠-scorer separation is for. A lone model grading its own write-up has no way to catch this, because the sentence is locally plausible and only wrong relative to an artifact the author did not re-read.

## Resuming a run from its own traces

Round 2 was not a new run. It was started **on this galaxy, months of context later, with no re-germination and no hand-carried state** — a fresh set of workers picked up where the previous ones stopped, because everything they needed was already on disk and tracked: round 1's faults, its Lean probe report, its proof attempts, its loop verdict naming exactly what to repair.

That is the practical meaning of tracked delivery. A run whose deliverables live only in a scratch directory can be *finished* but not *continued*: the next worker has nothing to read. Here the loop nucleated five round-2 legs forward, each tagged `reattack-round:2`, wrote them under `attack-round-2/`, and left the round-1 fidelity anchor frozen so the Lean statement could not drift between rounds. Every artifact remains attributable to the round that produced it.

## Clean room

The fleet read no prior attack on this conjecture. That constraint is deliberate, and it exists because the [first run](https://github.com/noogram-labs/firoozbakht) did not have it: a solo-model attempt was committed into that galaxy's working tree, at its root, under a generic filename, while the fleet was running. The fleet found it and folded it in — it audited the document rather than swallowing it, and no result rested on it, but a run that has read a baseline can no longer be compared against that baseline.

Here the working tree contained nothing but the spore's own output. Audited: no reference to any prior or parallel attempt appears in any deliverable.

## Layout

| Path | Contents |
|---|---|
| `attack/` | The scientific chain: decomposition, source ledger, concept cards, three proof attempts, three notebooks, skeptic faults, Lean probe report, red-team coverage, both gate verdicts, the editorial verdict, the synthesis |
| `paper/` | `paper.tex` (LaTeX article — amsthm + biblatex), `references.bib`, the compiled `paper.pdf`, and an authoring log |
| `lean/` | The Lean 4 formalisation — the fidelity anchor and the discharged probe |
| `corpus/` | The adversarial corpus: false statements the kernel must reject, plus its verifier |
| `trace/` | Append-only sidecar: raw lifecycle events, every node's briefing, content hashes for every artifact |
| `docs/lore/` | The chronicle the fleet folded from its own run |

## Provenance, published rather than trimmed

Machine paths and internal molecule identifiers appear throughout, because this is the tree as it was written. The identifiers are not incidental: they are what lets you cross-reference `trace/` against the deliverables and check that the recorded hashes belong to the files actually shipped. The sibling repository scrubbed them; that was a consequence of republishing through a staging copy, not a rule this run needed to follow.

Every node ran on a model pinned by its formula — 22 of 22 model selections resolved from a formula pin, none from a silent adapter default. The pins live in `.cosmon/formulas/`, tracked here, so the model allocation is auditable rather than asserted.

## How it was built

A comparative study of this run against the same problem handed to a single strong model working alone — [*Firoozbakht: a solo strong model against a clean-room fleet*](https://github.com/noogram/sporarium/blob/main/docs/reports/2026-07-25-firoozbakht-codex-cleanroom-comparison.en.md) — audits the artifacts below and reaches the honest conclusion: both recovered the same mathematical core independently, and what the fleet added was not insight but **cumulability** — formal equivalences, reproducible computation, dead routes with obituaries, an audited bibliography, standing objections.

The [`math-attack` spore](https://github.com/noogram/sporarium) from sporarium, germinated with `cs spore run` and drained by a resident cosmon runtime. The spore's README documents the recipient flow, the clean-room discipline, and the tracked-delivery contract this run exercises.

---

*Built by a Noogram agent fleet. Licensing: see [`LICENSES.md`](LICENSES.md).*
