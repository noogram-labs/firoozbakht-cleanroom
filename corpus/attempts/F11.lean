/- Red-team corpus — ATTEMPT file `F11`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F11_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F11_attempt : ∀ n : ℕ, 1 ≤ n → g n ≤ 2 := by
  intro n hn
  simp [g]
  omega

end Firoozbakht.RedTeamAttempt
