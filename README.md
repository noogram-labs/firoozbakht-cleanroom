# firoozbakht-cleanroom — an agent fleet attacking an open conjecture, published exactly as it was generated

This repository **is** the working directory the fleet ran in. Nothing was copied
here, nothing was staged, nothing was scrubbed. The agents wrote into this tree,
committed on their own branches, and `cs done` merged them — 75 commits, 22 nodes,
zero collapses. Publishing it was one `git push`.

That is the claim being demonstrated, and it is worth stating plainly because
[the first run of this same spore could not make it](https://github.com/noogram-labs/firoozbakht):
there, every deliverable landed in a git-ignored state directory, so the galaxy's
tree stayed empty and publication needed a hand-built copy with a scrubbing pass.
Here the deliverables are tracked artifacts of the run itself.

## What was attacked

**Firoozbakht's conjecture** — that `p(n+1)^(1/(n+1)) < p(n)^(1/n)` for every
`n ≥ 1`, equivalently that `p_n^(1/n)` is strictly decreasing. It is open.

**It is still open.** Nothing here proves or refutes it, and nothing here claims
to. What the run produced is a precise account of *where* the obstruction sits,
what can be established unconditionally, and what a machine kernel would and
would not certify.

## The result, stated the way the run stated it

| Gate | Verdict |
|---|---|
| Evidence gate (kernel + skeptic + corpus, pre-synthesis) | **BLOCKED** — skeptic leg: two residual objections, repairs proposed but not applied |
| Citation gate (post-write audit against the source ledger) | **BLOCKED** — two citekeys unresolved |
| Editorial verdict (independent reviewer, fail-closed) | **REWRITE** |

Three of the four evidence legs pass. The Lean kernel builds clean — the single
remaining `sorry` is the declared open target, not a gap this run introduced. The
adversarial corpus is substantive, with 109/109 verification checks green. The
exhaustive computational sweep to `10^11` — 4 118 054 812 consecutive-prime pairs,
zero violations, `max ρ = 0.8318` — is confirmed along two independent code paths.

A blocked run is the honest outcome on an open conjecture. The gates exist to
refuse, and here they refused.

### The reviewer caught the paper misreporting itself

The most useful thing in this repository is a failure. The paper stated, in its
abstract and in §10.3, that *"the citation audit for this paper has not been run,
and no citation clearance is claimed."* The audit **had** run, and had returned
BLOCKED, naming two citekeys. A different model, on a different formula, compared
the prose against the verdict that actually existed on disk and filed it as an
overclaim.

That is what author-≠-scorer separation is for. A lone model grading its own
write-up has no way to catch this, because the sentence is locally plausible and
only wrong relative to an artifact the author did not re-read.

## Clean room

The fleet read no prior attack on this conjecture. That constraint is deliberate,
and it exists because the [first run](https://github.com/noogram-labs/firoozbakht)
did not have it: a solo-model attempt was committed into that galaxy's working
tree, at its root, under a generic filename, while the fleet was running. The
fleet found it and folded it in — it audited the document rather than swallowing
it, and no result rested on it, but a run that has read a baseline can no longer
be compared against that baseline.

Here the working tree contained nothing but the spore's own output. Audited: no
reference to any prior or parallel attempt appears in any deliverable.

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

Machine paths and internal molecule identifiers appear throughout, because this
is the tree as it was written. The identifiers are not incidental: they are what
lets you cross-reference `trace/` against the deliverables and check that the
recorded hashes belong to the files actually shipped. The sibling repository
scrubbed them; that was a consequence of republishing through a staging copy, not
a rule this run needed to follow.

Every node ran on a model pinned by its formula — 22 of 22 model selections
resolved from a formula pin, none from a silent adapter default. The pins live in
`.cosmon/formulas/`, tracked here, so the model allocation is auditable rather
than asserted.

## How it was built

A comparative study of this run against the same problem handed to a single
strong model working alone —
[*Firoozbakht: a solo strong model against a clean-room fleet*](https://github.com/noogram/sporarium/blob/main/docs/reports/2026-07-25-firoozbakht-codex-cleanroom-comparison.md)
— audits the artifacts below and reaches the honest conclusion: both recovered
the same mathematical core independently, and what the fleet added was not
insight but **cumulability** — formal equivalences, reproducible computation,
dead routes with obituaries, an audited bibliography, standing objections.

The [`math-attack` spore](https://github.com/noogram/sporarium) from sporarium,
germinated with `cs spore run` and drained by a resident cosmon runtime. The
spore's README documents the recipient flow, the clean-room discipline, and the
tracked-delivery contract this run exercises.

---

*Built by a Noogram agent fleet. Licensing: see [`LICENSES.md`](LICENSES.md).*
