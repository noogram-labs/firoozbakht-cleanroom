/- Red-team corpus — AUDIT-EVASION file `V01`.

Expected verdict: **accepted by `lake build`, caught by the axiom audit.**

This is the corpus's most important entry, because it is the one the naive
checker misses. The claim "this file establishes Firoozbakht's conjecture" is
FALSE, and yet `lake env lean` on it exits **0** with no warning at all —
quieter than a `sorry`, which at least prints one.

The gate that catches it is `#print axioms`, which is exactly what
`../../lean/audit.lean` runs. `firoozbakht_smuggled` depends on
`Firoozbakht.RedTeamAudit.firoozbakht_axiom`, a name that is not in
`[propext, Classical.choice, Quot.sound]`.

**Consequence for the run:** a green `lake build` is NOT the acceptance
criterion for the formal leg. The acceptance criterion is a green build **plus**
an axiom audit whose only entries are the three standard ones plus a declared,
enumerated `sorryAx` list. Any leg that reports "build green" without the audit
output has reported nothing.
-/

import Firoozbakht.Statement

namespace Firoozbakht.RedTeamAudit

open Firoozbakht

/-- The smuggled assumption. Lean accepts new axioms silently by design. -/
axiom firoozbakht_axiom : Conjecture

/-- "Proved." Zero warnings, exit 0. -/
theorem firoozbakht_smuggled : Conjecture := firoozbakht_axiom

-- The audit is what fires. Uncomment to see it:
-- #print axioms firoozbakht_smuggled
--   ⇒ 'firoozbakht_smuggled' depends on axioms:
--     [Firoozbakht.RedTeamAudit.firoozbakht_axiom]

end Firoozbakht.RedTeamAudit
