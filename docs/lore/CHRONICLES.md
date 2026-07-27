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

---

## 2026-07-26 — two roommates fix the same crooked shelf, neither knowing the other is home

**Principle inscribed: independently repairing the same fault is not the same as repairing it once. A fan-out with no reconciliation stage doesn't converge on a second try — it doubles the number of answers, and each new answer is individually correct.**

Round 1's own skeptic (`task-20260725-488f`) warned that a pipeline which forks work into parallel
attempts, with nobody assigned to reconcile them afterward, would eventually fork the *same* repair
twice. Round 2 (`reattack-20260726-57d1`) did exactly that: two proof attempts were both handed the
same broken bound to fix. Picture two roommates, each noticing the same crooked shelf, each fixing
it while the other is out — one wedges a matchbook under the left leg, the other planes down the
right leg. Come home and the shelf is level *twice*, in two incompatible ways, and neither roommate
knows the other one touched it. Both fixes were checked by hand, digit by digit, and both are
correct: one attempt derived a bound of `0.99565`, the other `0.998244`, off two different rows of
the same 2014 reference table, and neither document so much as mentions the other exists. A reader
handed both has no rule for choosing, because nothing in the process ever asked the two fixes to
meet.

The same shape repeated one layer down: two attempts filed the *same* source under two contradictory
trust tiers on the same day, and the record-keeping change one of them announced ("the ledger entry
is now updated") had, when checked directly against the actual file, never happened at all — like
two people each telling a shared calendar a different time for the same meeting, and one of them
telling you they'd already fixed the clash when they hadn't opened the calendar again to check.

**How to apply:** when a pipeline fans a hard problem out into parallel independent attempts,
"parallel" cannot mean "silent" — build a reconciliation step into the plan from the start, not
as an afterthought once a collision is noticed. A round that only adds more attempts without adding
a leg whose job is to make the attempts talk to each other will look like progress (more things got
fixed!) while actually widening, not narrowing, the number of live disagreements. This is the failure
mode round 1 named in the abstract and round 2 produced in the concrete — the clearest possible
confirmation that the fix belongs in the pipeline's shape, not in asking each attempt to try harder.

---

## 2026-07-26 — the referee who grades against last week's answer key

**Principle inscribed: "I reproduced the earlier verdict exactly" is evidence of agreement, not of correctness. A checker that measures itself against the previous checker's output, rather than against the thing being checked, will faithfully re-certify an old mistake and call the faithfulness a pass.**

Round 2's skeptic (`task-20260726-7211`, artifact `attack-round-2/faults.md`) re-ran a disputed
prime-counting statistic that round 1 had flagged as unsettled, reproduced round 1's own numbers
digit for digit, and declared the dispute *"settled"* — case closed, matches the file. But round 2's
own hypha, working this same molecule one step later, recomputed that statistic from scratch, from
the original definition, independent of both prior answers — and found every one of round 1's and
round 2's shared numbers were off by exactly one, in the unsafe direction, because a script had
silently dropped the last data point before counting. Picture a substitute teacher grading a pop
quiz by comparing every answer sheet to last week's, rather than to the textbook: a student who
copies last week's mistake gets full marks, because the grading is checking for *agreement*, not for
*truth*. The round-2 skeptic's phrase for its own work — "this reproduces the earlier finding
exactly" — is precisely that kind of grading, and it is nobody's fault in particular: matching a
prior answer is a natural, cheap sanity check, and it is easy to let it stand in for the harder
question of whether the prior answer was ever right.

**How to apply:** a verification step that only checks internal consistency with an earlier step's
output (as opposed to re-deriving the answer independently from the original statement) is not
exempt from the same discipline it enforces on everyone else. When a check reports "matches the
earlier result," ask separately whether anyone has recomputed that earlier result from scratch —
matching is not a substitute for re-derivation, and a checker's own numbers deserve the same
adversarial reproduction its findings demand of others.

---

## 2026-07-26 — a fire alarm with only two settings

**Principle inscribed: a gate with exactly two verdicts cannot tell "I am blocked, and I am telling you plainly" from "I am blocked, and I am hiding it" — and will hand both the identical, worse-sounding verdict.**

The round-2 editorial gate (`review-20260726-7d55`) had to score a paper that does something
unusual: it states, in its abstract, in a boxed paragraph, and in its acknowledgements, that the
underlying evidence gate is BLOCKED — and explains exactly why, in detail a reader can act on. The
gate rule has only two words, SHIP and REWRITE, and BLOCKED forces REWRITE regardless of how the
paper talks about it. So this careful, three-times-repeated disclosure scores *identically* to what
a paper would score if it quietly deleted all three mentions and said nothing. Picture a fire alarm
that only has "all clear" and "evacuate" — it cannot ring one way for "there's a small kitchen fire
and I want you to know exactly where it is" and another way for "the building already burned down
and nobody told you." Both are "not all clear," so both alarms sound the same, even though one of
them is the more useful building to be in.

The reviewer noticed this and refused to let the gate's silence stand — writing it into a dissent
section rather than quietly padding the verdict, since a rule that bends for a gracious paper stops
being a rule at all.

**How to apply:** when a binary gate (ship/block, pass/fail, green/red) scores an artifact that is
itself *reporting on* the thing the gate checks, check whether the gate has a way to distinguish
honest disclosure from concealment. If it doesn't, the fix is not to soften the gate for artifacts
that disclose well — that turns the gate into a popularity contest — the fix is to add a third
word: something like "the artifact is correct about a real failure elsewhere," scored differently
from "the artifact is wrong." Two verdicts is enough for a system that only ever fails one way; it
is not enough for one that can fail *and* be honest about it, or fail and hide it.

---

## 2026-07-27 — round 3: the doctor caught everyone's cold but its own

**Principle inscribed: a step built specifically to catch "you described a file without checking
it" is itself a step that describes files — and unless something checks the checker the same
unforgiving way, it will make its own signature mistake, in public, and nobody will notice, because
nobody thought to suspect the doctor of carrying the cold.**

Round 2 ended with a name for its own disease: nobody owned the seams between parallel fixes, so
the same crooked shelf got mended twice, differently, by two roommates who never spoke (chronicle
above, 2026-07-26). Round 3's answer was to hire a seam-owner: a reconciliation leg
(`task-20260727-264e`), whose entire job was to stop anyone from describing the state of a file
from memory instead of reading it. It did that job well — it closed real contradictions, reversed
a wrong denominator, corrected a stale ledger tier. Then, in its own closing section, it typed four
sentences about what was "still open" in the tree — from memory, not from `git log` — and got all
four wrong. The round-3 skeptic (`task-20260727-5096`) caught it and named the shape precisely:
*"a leg's claim about the state of a file is not evidence about the state of that file"* — which is
the reconciliation leg's own founding lesson, now failed by the leg that exists to teach it.

It did not stop there. The synthesis fold (`task-20260727-4709`) read the reconciliation and
republished its four wrong sentences as settled fact. The paper (`edit-20260727-ace7`) wrote a
section — §9.5 — whose entire purpose was to report the citation audit's *current* state, so that
this exact error could never happen to a reader. The citation gate then ran, passed, and
superseded the very report §9.5 was quoting — and §9.5 went stale within minutes of being written,
for the third round running. Then the citation gate itself (`cite-20260727-df58`), auditing 22
citations, wrote "21/21 citekeys: OK, no citekey lacks a ledger row" — and had, in its own table,
checked 21. Four different legs, four different documents, one identical mistake: stating a
*negative* — "nothing is missing," "nothing is still open," "no citekey lacks a row" — without
first counting. Every one of the hard mathematical claims this round touched was independently
re-derived and held up (nine constants, a Lean kernel rebuilt from a cold cache, a sieve to a
billion). Every one of the easy countable claims — how many files say a fact, how many citekeys a
table checked — was asserted from memory and was wrong. Picture a school where the hardest exam
questions all get double-checked with a calculator and the attendance sheet gets marked by
guessing who was probably there: the guess is wrong exactly when it matters, because nobody thought
counting heads needed a calculator too.

**How to apply:** when you add a verification step whose purpose is "catch claims made without
checking," budget for the fact that the step's own prose is also a claim, made by a leg, under the
same time pressure as everyone else's. Do not exempt the checker from the rule it enforces. And
more generally: treat every *negative* assertion about a countable artifact — "nothing is
unresolved," "every X has a Y," "no Z lacks a row" — as a claim that costs one `grep -c` to verify,
where every wrong instance of it costs a full downstream round to undo. The fix is not another
reconciliation pass on top of this one; it is a rule that a leg may not assert a negative fact about
an artifact it has not just counted. Four consecutive rounds warned about exactly this and the
warning did not suppress it once — which means the fix belongs in what a leg is required to run
before it types the sentence, not in adding a fifth leg to check the fourth.

**What changed since round 2 (this chronicle's own bookkeeping):** round 2's chronicle entries
(above) describe a corpus whose failures were still reachable by "add a reconciliation stage" and
"re-derive instead of matching." Round 3 built exactly that reconciliation stage — and the failure
mode did not go away, it moved one level up, into the reconciliation stage itself and everything
downstream of it. The conjecture `F` is unchanged: still open, still numerically robust, still
incompatible with the standard heuristic. What moved is where the corpus's actual risk lives —
from "is the math right" (repeatedly confirmed, all three rounds) to "did anyone count before
claiming nothing was missing" (failed, all three rounds, escalating in scope each time).
