# Red-team corpus — coverage report

**Leg:** `red-team-corpus` (crew role: red-team-mathematician)
**Molecule:** `task-20260725-3ef3` · **Germ:** `germ-20260725-791a7c45`
**Backend:** `lean` — every verdict below is a real `lake env lean` run against
`leanprover/lean4:v4.29.0` + Mathlib `8a178386ff`, not a prose judgement.

## What this corpus is for

The formal leg of this attack rests on one claim: *the checker rejects what it
should reject*. That claim was, until now, untested. A green `lake build` on
`lean/` proves the skeleton is well-formed; it says nothing about whether the
kernel would have caught a wrong statement.

So: 27 statements, every one of them false or ill-formed, run through the same
toolchain. If the checker had accepted any of them, the formal leg's authority
would have been fiction.

Result: **27/27 behaved as specified.** But three of them were "accepted", one
was accepted *and* passed a clean axiom audit, and that is the report's main
finding — see §4.

## 1. The scoreboard

```
$ bash corpus/run_corpus.sh
CORPUS GREEN — every entry behaved as specified.
```

| Evidence class | Count | What it means |
|---|---:|---|
| **refuted** | 20 | the *negation* is proven in `corpus/refutations/`, no `sorry`. Not "an attempt failed" — **no attempt can succeed** |
| **rejected** | 3 | ill-formed or unprovable-by-any-means; the attempt file fails to elaborate |
| **accepted-but-unsound** | 3 | `lake build` exits **0**. Caught only by `#print axioms` |
| **undetected** | 1 | `lake build` exits 0 **and** the axiom audit is clean. No gate in this run fires |

Every entry also carries an **attempt file** — the most plausible wrong proof a
careless author would write — compiled in isolation, one file per entry so no
failure can be masked by a neighbour. All 23 attempt files were rejected with a
genuine `error`, never a warning.

## 2. Coverage against the brief's categories

| Brief category | Entries | Deepest instance |
|---|---|---|
| near-miss variants | `F09` `F10` `F13` `F14` | `F14` — Kourbatov's `p_{k+1} < p_k^(1+1/k)` with the exponent's denominator shifted to `k+1`. A *strengthening*, and it dies at `n = 1`: `3 < 2^(3/2) = 2.828…` |
| wrong quantifier order | `F15` `F16` `F19` | `F16` — `∃N ∀n≥N, p_n^(1/n) < 1`. Confuses "strictly decreasing" with "goes below its limit". The sequence approaches 1 **from above** |
| dropped hypotheses | `F03` `F04` `F05` `F18` | `F18` — card `L16`(c) says `T_n` decreases in `n` **at fixed `p_n`**. Drop those four words and you get `T(n+1) < T n`, false at once: `T 1 = 2`, `T 2 = 3^(3/2) − 3 = 2.196…` |
| universe / typing cheats | `F17` `F20` `V04` | `V04` — see §4. The category does not fail the way a red team expects it to |
| indexing fidelity (added) | `F01` `F02` | `F02` — the missing `−1`. Card `D1`'s highest-severity hazard, made kernel-checkable |
| ℕ-subtraction (added) | `F06` `F07` `F08` `F21` | `F21` — `cast_g`'s exact shape with the subtraction reversed and the guard gone. Card `T4` node N5 |
| false bounds (added) | `F11` `F12` | `F12` — `g_n < log p_n`. The true threshold is *quadratic* in `L = log p_n` (card `L2`), not linear |
| method cheats (added) | `F22` `F23` | `decide` and `native_decide` on `F3 1`. Both fail: `Nat.nth` is noncomputable (card `T4` Fact 1) |
| audit evasion (added) | `V01` `V02` `V03` | `V03` — two contradictory `sorry`s make a third theorem prove `0 = 1` **with no `sorry` of its own** |

The last five rows are additions to the brief. Each was chosen because a
concept card names the corresponding hazard: `D1` (indexing), `D2`/`T4` node N5
(ℕ-subtraction), `L2` (threshold scale), `T4` Fact 1 (noncomputability), and
`STATUS.md`'s own axiom audit.

## 3. The three entries that matter most

**`F02` — the missing `−1`.** Card `D1` says the 1-indexed and 0-indexed
families of the conjecture *cannot be told apart by truth value*: every case of
both holds in any range anyone can check. A development could go fully green
having formalized a different conjecture. `F02` is the separation that **is**
available — at the level of numerals (`nth Prime 1 = 3` versus `p 1 = 2`), not
propositions. It is the only kernel-checkable defence against that failure, and
it now exists.

**`F18` — four dropped words.** `L16`(c)'s repair — that a certified *lower*
bound on a prime's rank suffices for a refutation certificate — runs
`N ≤ n ⟹ T_N ≥ T_n`. That implication needs monotonicity **at fixed `p_n`**. A
reader who takes the card's "strictly decreasing" as decreasing in `n` alone
gets the inequality backwards, and the whole refutation-certificate argument
inverts. `T 1 = 2 < 2.196… = T 2` is now on record.

**`V03` — the green build that voids everything.** Two `sorry`-ed theorems
stating `Conjecture` and `¬ Conjecture` let a later declaration prove `0 = 1`
carrying no `sorry` itself. `lake build` is green; a reviewer grepping the
result file for `sorry` finds nothing. This is precisely why `Statement.lean`
states the refutation branch as `def Refuted : Prop := ¬ Conjecture` plus a
**proven** `refuted_of_witness`, rather than as a second `sorry`-ed theorem.
That design decision was documented; it is now load-bearing and tested.

## 4. The finding: what the checker does *not* catch

Three entries compile. One compiles **and** passes a clean axiom audit.

| id | `lake build` | `#print axioms` | caught by |
|---|---|---|---|
| `V01` axiom smuggled | exit 0, **no warning** | `firoozbakht_axiom` | the audit |
| `V02` `sorry` | exit 0, warning | `sorryAx` | the audit + a `sorry` census |
| `V03` contradictory `sorry`s | exit 0, warnings | `sorryAx` | the audit, *if* someone reads the pair |
| `V04` silent coercion | exit 0, no warning | **clean** | **nothing automated** |

### `V01` — a smuggled axiom is quieter than a `sorry`

`axiom firoozbakht_axiom : Conjecture` followed by
`theorem firoozbakht_smuggled : Conjecture := firoozbakht_axiom` exits 0 with
*no warning at all*. A `sorry` at least prints one.

**Therefore: a green `lake build` is not the acceptance criterion for the formal
leg.** The criterion is a green build **plus** an axiom audit whose only entries
are `[propext, Classical.choice, Quot.sound]` plus a declared, enumerated
`sorryAx` list. `lean/STATUS.md` already reports exactly this. Any downstream
leg that reports "build green" without the audit output has reported nothing,
and this corpus is the proof of that sentence.

### `V04` — the typing cheat that isn't

`V04` was authored as a rejection entry: state a ℕ-valued fact with an ℝ-valued
right-hand side, `p 1 = (2 : ℝ)`, and watch the elaborator reject the type
error. **It did not get rejected.** Lean inserted `Nat.cast`, elaborated the
statement as `((p 1 : ℕ) : ℝ) = (2 : ℝ)` — which is true — and `norm_num` proved
it. The corpus runner printed `THE CHECKER ACCEPTED A FALSE CLAIM`, and the
corpus, not the checker, was wrong.

The result was kept rather than deleted, because it is the honest answer to the
brief's "universe / typing cheats" category:

> There is no typing-cheat failure mode of the kind a red team instinctively
> looks for. Unification does not *fail* on a ℕ/ℝ mismatch; it *repairs* it by
> coercion, and the kernel then checks the repaired proposition.

So a fidelity error at the level of types becomes one of two things:

- **a true statement that means something other than what was written** — `V04`,
  invisible to every gate in this run; or
- **a false statement** — `F07`, `F21` — caught, but caught as *arithmetic*,
  never as *typing*.

The dangerous case is the first, and it is at its most dangerous exactly where a
cast crosses ℕ-subtraction, because there the inserted coercion is not merely
invisible — it is not even the map the reader assumes:
`((a − b : ℕ) : ℝ) ≠ (a : ℝ) − (b : ℝ)`. That is card `T4`'s node N5, the
highest-risk node of the Lean plan, and `F1'_iff_F4` is still `sorry`-ed.

**Recommendation to the proof leg:** when `F1'_iff_F4` is discharged, print the
elaborated statement with `set_option pp.coercions true` and read it, and keep
`Statement.lean`'s existing discipline — primary form in ℕ with no casts, every
cast confined to `cast_g`, which carries its `1 ≤ n` guard explicitly. No
automated gate substitutes for this.

## 5. Near-misses that could NOT become entries

A corpus for an **open** conjecture has a boundary a corpus for a settled
theorem does not: an adjacent statement may be false, true, or *exactly as open
as `F` itself*. Only the first kind can be an entry. Four attractive candidates
were dropped, and the reasons are machine-checked in
`corpus/rejected-candidates/WhyNotInCorpus.lean` (compiles, no `sorry`):

| candidate | why it is not an entry |
|---|---|
| **R1** `∀ n, F3 n` — the conjecture with the `1 ≤ n` guard dropped | `F3` is **true** at the junk index: `1 < 2`. Proven, along with the equivalence to `Conjecture`. Refuting it would settle Firoozbakht |
| **R2** `strict_iff_nonstrict` unguarded | **true**, and proven unguarded. The guard on `p_pow_ne` is needed; the guard on this corollary is inherited, not required |
| **R3** `(∃ n≥1, ¬F3 n) ↔ (∀ n≥1, ¬F3 n)` — "fails somewhere" vs "fails everywhere" | the RHS is provably false (`F3 1` holds), so the biconditional **implies** `Conjecture` — proven. Refuting this near-miss is exactly as hard as proving Firoozbakht |
| **R4** the 0-indexed weakening claimed pointwise-equivalent | card `D1`: both families hold at every checkable index. Refuting the equivalence means settling `F` on one branch |

This is why the corpus's quantifier-order entries (`F15`, `F16`, `F19`) are
aimed at *decidable* subjects — boundedness of the primes, the limit of
`p_n^(1/n)`, the position of a guard — and never at `F` itself. Recording the
rejects matters as much as the entries: a corpus that omits them looks more
complete than it is, and the next author re-derives the same dead ends.

## 6. What this corpus does not cover

Stated plainly, so nothing here is mistaken for more than it is.

1. **No entry tests the conjecture's truth.** By construction. Every entry is
   about the *checker* and the *statement*, never about `F`. `F` remains open.
2. **The verified range is still `n ≤ 4`.** The corpus inherits `FiniteCheck`'s
   reach (card `T4` Fact 2: Mathlib's prime-specific `nth` API is five `@[simp]`
   base lemmas). Every numeric refutation lands at `n ∈ {0,1,2,4}` because those
   are the only indices this project can name. A near-miss that first fails at
   `n = 40` could not have been authored here.
3. **The four `sorry`-ed `L1` equivalences are untested by this corpus.** They
   are unformalized, not unproven; a red-team entry against them would be an
   entry against a statement nobody has yet written in Lean.
4. **No adversarial input to the *search* legs.** This corpus attacks the formal
   checker. The computational legs (cards `T2`, `T3` — search design, index
   certification) have their own failure modes — precision, `π(x)` bounds,
   off-by-one in a sieve — and are not touched here.
5. **`V04`'s gap is not closed, only named.** No automated check in this run
   catches a silently-coerced true-but-wrong statement. The mitigation offered
   in §4 is a reading discipline, not a gate.

## 7. Verification pass (step 2) — one real gap found and closed

The corpus was re-audited against its own brief. `corpus/verify_corpus.py`
now checks the claims the corpus makes *about itself*: **109/109 green.**

**The gap that mattered — refutations were never audited for axioms.** Every
file in `refutations/` imports `Statement.lean`, which contains the `sorry`-ed
open target `firoozbakht`. A refutation that leaned on it — directly, or through
any lemma that did — would prove **nothing about anything**, and would still
compile silently. That is entry `V02`'s attack, aimed at the corpus itself, and
nothing in the first pass would have caught it.

`#print axioms` now runs on all 24 theorems in `refutations/` and
`rejected-candidates/`. Result: **every one depends on nothing beyond
`[propext, Classical.choice, Quot.sound]`** — `F17_refuted` on no axioms at all.
No refutation is tainted. The corpus's own headline claim now rests on the same
gate it recommends to everyone else in §4, which is the only consistent place
for it to rest.

| check | what it asserts | result |
|---|---|---|
| **V1/V3** | every manifest entry names files that exist, one attempt file per entry | 27/27 |
| **V2** | every `refuted` entry has a theorem `<id>_refuted` really present | 20/20 |
| **V4** | every refutation theorem is axiom-clean | 24/24 + 3 file-level counts |
| **V5** | manifest `observed` agrees with `results.tsv` | 27/27 |
| **V6** | no `sorry` in `refutations/` or `rejected-candidates/` | 3/3 files |

**Two smaller findings, both checked:**

- *No rejection is spurious.* An attempt file that failed on a typo or an
  unknown name would be a fake test. All 23 logs were swept for
  `unknownIdentifier` / `unknown constant` / `unexpected token`: **none**. Every
  rejection is on the mathematical goal — `unsolved goals` (16),
  `omega could not prove the goal` (5), `failed to synthesize` (3),
  `Type mismatch` (1).
- *Every provenance citation was re-read at its source, not recalled.*
  `L16`(c) and `D5` hazard 1 both state the monotonicity of `T_n` as "at fixed
  `p_n`" (verbatim), which is what `F18` attacks; `L2` gives
  `T_n = L² − L − 1 + o(1)`, which is what makes `F12`'s linear bound absurd;
  `L12` gives the unconditional large-gap record, which is what `F11` violates.

The anchor was re-built after the corpus was written: `lake build` in `lean/`,
**green, 1984 jobs, warnings are the five declared `sorry`s and nothing else** —
the corpus adds no files to the `Firoozbakht` library and changes none.

## 8. Reproduction

```bash
cd lean && lake exe cache get && lake build     # the anchor, green
cd .. && bash corpus/run_corpus.sh              # the corpus, 30 files
python3 corpus/verify_corpus.py                 # the corpus's claims about itself
cat corpus/results.tsv
```

Runtime is 91 s wall-clock on a warm Mathlib cache (measured). Exit 0 iff every entry
behaves as `corpus/manifest.json` says it must — including the four that are
*supposed* to compile.

**Standing invariant for downstream legs:** if any file in
`corpus/refutations/` or `corpus/rejected-candidates/` ever stops compiling, a
definition in `lean/Firoozbakht/` has changed meaning. That is the alarm firing,
not a bug in the corpus.
