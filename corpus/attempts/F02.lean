/- Red-team corpus — ATTEMPT file `F02`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F02_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F02_attempt : ∀ k : ℕ, Nat.nth Nat.Prime k = p k := by
  intro k
  simp [p]

end Firoozbakht.RedTeamAttempt
