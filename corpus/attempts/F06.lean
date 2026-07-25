/- Red-team corpus — ATTEMPT file `F06`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F06_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F06_attempt : ∀ n : ℕ, (p n - p (n + 1)) + p (n + 1) = p n := by
  intro n
  omega

end Firoozbakht.RedTeamAttempt
