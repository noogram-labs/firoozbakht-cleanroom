/- Red-team corpus — ATTEMPT file `F10`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F10_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F10_attempt : ∀ n : ℕ, 1 ≤ n → (p n) ^ (n + 1) < (p (n + 1)) ^ n := by
  intro n hn
  norm_num

end Firoozbakht.RedTeamAttempt
