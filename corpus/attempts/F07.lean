/- Red-team corpus — ATTEMPT file `F07`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F07_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F07_attempt :
    ∀ n : ℕ, ((p n - p (n + 1) : ℕ) : ℤ) = (p n : ℤ) - (p (n + 1) : ℤ) := by
  intro n
  push_cast
  ring

end Firoozbakht.RedTeamAttempt
