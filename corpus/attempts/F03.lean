/- Red-team corpus — ATTEMPT file `F03`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F03_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F03_attempt : Function.Injective p := by
  intro a b h
  simp [p] at h
  omega

end Firoozbakht.RedTeamAttempt
