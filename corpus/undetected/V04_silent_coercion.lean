/- Red-team corpus — AUDIT-EVASION file `V04`.

Expected verdict: **accepted, and NOTHING automated flags it.** Exit 0, no
warning, and `#print axioms` shows only `[propext, Classical.choice, Quot.sound]`
— a perfectly clean audit.

## How this entry was found

It was authored as a *rejection* entry: "state a ℕ-valued fact with an ℝ-valued
right-hand side and watch the elaborator reject the type error." It did not get
rejected. Lean inserted `Nat.cast` and elaborated `p 1 = (2 : ℝ)` as
`((p 1 : ℕ) : ℝ) = (2 : ℝ)`, which is **true**, and `norm_num` proved it. The
corpus runner reported `THE CHECKER ACCEPTED A FALSE CLAIM`, and the corpus was
wrong, not the checker.

## The finding, stated plainly

**There is no "typing cheat" failure mode in Lean of the kind a red team
instinctively looks for.** Unification does not fail on a ℕ/ℝ mismatch; it
repairs it by coercion. What the kernel then checks is whether the *repaired*
proposition is true. So a fidelity error at the level of types becomes either

  (a) a true statement that means something other than what was written —
      **this file**, undetectable by any gate in the run; or
  (b) a false statement — `F07`, `F21` — which is caught, but caught as
      *arithmetic*, not as *typing*.

The dangerous case is (a), and it is dangerous exactly where a cast crosses
`ℕ`-subtraction, because there the coercion is not merely invisible, it is not
even the map the reader assumes: `((a - b : ℕ) : ℝ) ≠ (a : ℝ) - (b : ℝ)`.

## The gate that would catch it

Not the kernel. Reading the *elaborated* statement, with coercions printed:

    set_option pp.coercions true in
    #check @F1'_iff_F4

and, structurally, the discipline `Statement.lean` already follows — keep the
primary form (`F3`) in `ℕ` with no casts at all, and confine every cast to one
audited lemma (`cast_g`), which carries its `1 ≤ n` guard explicitly.

**This entry is the corpus's answer to the brief's "universe / typing cheats"
category: the category is real, but it does not fail the way it is expected to,
and a red-team corpus that only collected rejections would have missed it.**
-/

import Firoozbakht.Statement

namespace Firoozbakht.RedTeamAudit4

open Firoozbakht

/-- Written as if `p 1` were a real number. Accepted: silently elaborated to
`((p 1 : ℕ) : ℝ) = (2 : ℝ)`. -/
theorem coerced_silently : p 1 = (2 : ℝ) := by norm_num

-- set_option pp.coercions true in
-- #check @coerced_silently   ⇒ ↑(p 1) = 2
-- #print axioms coerced_silently ⇒ [propext, Classical.choice, Quot.sound]

end Firoozbakht.RedTeamAudit4
