/- Red-team corpus — AUDIT-EVASION file `V03`.

Expected verdict: **accepted by `lake build` (warnings only), catastrophic.**

This is the attack the skeleton's `README`/`STATUS.md` say it defends against,
made concrete so the defence is testable rather than asserted.

Two `sorry`-ed theorems that contradict each other let *any* later declaration
close *any* goal. Below, `0 = 1` is "proved" — with no `sorry` of its own, so a
reviewer grepping for `sorry` on the final theorem sees nothing. The build is
green. Every downstream proof in such a development is void.

**The defence, in `Statement.lean`:** the refutation branch is *not* a second
`sorry`-ed theorem. It is `def Refuted : Prop := ¬ Conjecture` plus
`refuted_of_witness`, which is proven. This corpus entry is what makes that
design decision load-bearing rather than stylistic.

**Gate:** the audit must check not just *how many* `sorry`s exist but whether
any two sorried declarations are contradictory — in practice, that no
`sorry`-ed statement and its negation both appear. Enumerating the `sorry` list
as `STATUS.md` does is exactly what makes this checkable by eye.
-/

import Firoozbakht.Statement

namespace Firoozbakht.RedTeamAudit3

open Firoozbakht

/-- Sorried: the conjecture. -/
theorem yes : Conjecture := by sorry

/-- Sorried: its negation. Each is individually as defensible as the other;
together they are lethal. -/
theorem no : ¬ Conjecture := by sorry

/-- **No `sorry` on this declaration.** It is nevertheless nonsense, and a
`grep sorry` on the file that contains the *final result* would find nothing. -/
theorem anything_at_all : (0 : ℕ) = 1 := absurd yes no

end Firoozbakht.RedTeamAudit3
