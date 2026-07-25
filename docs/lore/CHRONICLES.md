# Chronicles — firoozbakht-cleanroom Decision Journal

Read this file first when starting a session.

---

## 2026-07-25 — the label that only answers "where," never "what did I assume"

**Principle inscribed: a tagging system that records provenance and never records assumptions will let a careful proof carry careless sentences about itself — and the two will look equally trustworthy from outside.**

The DAG spent a whole molecule (`delib-20260725-07fc`) putting five independent readers — a
Wheeler, a Feynman, a Gödel, a Popper, a Knuth — on one document before any expensive compute was
allowed to run against it. Picture a kitchen where every ingredient has a little card stapled to
it saying which shop it came from. That's what the document's tags did: `[self-contained]`,
`[needs-anchor]`, tier L1/L3 — every one of them answers "where did this come from?" None of them
answers "what did I assume when I wrote this line down?"

The five readers re-derived the actual mathematics by hand — the core inequality chain, the key
numeric claims, a correction the document had already made to itself — and found no errors. What
they found broken was the layer of sentences sitting *around* the mathematics: a claim that the
proof tree covered every possible route (it didn't — whole strategies had no branch at all); a
claim about which of six sub-lemmas was the "one genuine theorem" (three others were also
genuine theorems); and, most expensive of all, one formal statement that — because of a silent
off-by-one in how "the n-th prime" was indexed — encoded a conjecture *weaker* than the one under
attack. A machine proof could have gone green having proved the wrong thing, and nothing in the
tagging system would have said so, because indexing is a *modelling* choice, not a *provenance*
fact, and the tags only ever audited provenance.

**How to apply:** when a pipeline (or a person) tags claims for trust — sourced/unsourced,
verified/unverified, cited/uncited — ask whether the tag set has any slot for "what did this
step assume that isn't written elsewhere." If every tag answers "where," and none answers
"what," the system will keep passing careful arithmetic wrapped in careless framing, and nobody
downstream will know to look.

---

## 2026-07-25 — honesty, scored the moment after it stops being true

**Principle inscribed: a gate that snapshots a state into prose, then re-runs the real check later, will punish the author who wrote the state down honestly harder than the author who said nothing — and that is a fault in the pipeline's ordering, not in the author.**

The paper (`edit-20260725-37f8`) said, plainly, in two places: "the citation audit for this paper
has not been run." That sentence was true the moment it was written — the citation-gate molecule
hadn't run yet. Then the citation-gate *did* run (`cite-20260725-9eef`), found two citations with
no matching source, and returned BLOCKED. The paper's sentence was now false — not because the
author lied, but because the pipeline runs "write the paper" *before* "check the paper," and asks
the paper to describe a future it cannot see.

The editorial reviewer (`review-20260725-4b9d`) caught this and, instead of quietly shrugging it
off, wrote it into the verdict as dissent: imagine two authors. One hides the gap. One names it
three separate times, in three separate places, in loving detail — which sources are missing,
why, and where the disclosure is duplicated. Score them both against a gate that only reads
final state, and they get the *same* grade, because the gate can't see conduct, only the
document. Worse: under that rule, the honest author's extra disclosure is pure downside — every
sentence about your own gate state is a hostage you handed the grader, for zero credit if it goes
stale. That is exactly backwards from what you want a pipeline to reward.

**How to apply:** if a document must describe the state of a check that runs *after* the document
is written, don't let a human (or model) type that state into prose by hand. Generate that one
paragraph from the actual check's output at the moment of judgment, so the document can't go
stale between being written and being read. This is a fix to the pipeline's shape, not a note to
future authors to "be more careful" — no amount of care removes a race between writing and
checking.

---

## 2026-07-25 — a check built from the wrong turn will bless the wrong turn

**Principle inscribed: a numerical check that is derived from the same steps as the theorem it is meant to test can only ever agree with that theorem — even when the theorem is wrong. A check has to be built from the original statement, independent of the path used to reach it, or it isn't testing anything.**

The red-team leg (`task-20260725-488f`) read every proof attempt and every notebook hunting for
places where a "PASS" print was quietly reproducing its own mistake instead of catching one.
Picture grading your own exam using an answer key you wrote by copying your own work — every
answer will match, because you copied it from the same place twice. That is what happened once
in this corpus: one proof attempt's in-run numerical sweep was built from the very derivation it
was supposed to be checking, so when that derivation took a wrong turn, the check inherited the
same wrong turn and reported PASS. It looked like independent corroboration. It was an echo.

Note what this is *not*: the red-team leg found no assumed conclusions, no circular reasoning,
and no sieve-to-a-million result quietly dressed up as a general theorem — eighteen separate
claims came back clean, independently re-derived. This single finding was narrower and, for that
reason, easy to miss: a check that agrees with its own source isn't evidence, it's a mirror.

**How to apply:** when writing a numeric or computational check meant to corroborate a derivation,
build the check from the *statement* being tested, not from the intermediate expressions the
derivation produced along the way. If the check and the theorem share a step, the check cannot
see an error in that step — it can only ever agree with it.
