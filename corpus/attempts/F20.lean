/- Red-team corpus — ATTEMPT file `F20`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F20_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

/- Universe cheat. `∀ α : Type, α` inhabits `Type 1`, not `Prop`, so it cannot
appear under `¬` — and `def U : Type := Type` is a universe error outright.
Both are here; either alone must make the file fail. -/

def U : Type := Type

theorem F20_attempt : ¬ (∀ α : Type, α) := fun h => (h Empty).elim

end Firoozbakht.RedTeamAttempt
