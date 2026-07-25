/- Red-team corpus — ATTEMPT file `F15`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F15_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F15_attempt : ∃ n : ℕ, 1 ≤ n ∧ ∀ m : ℕ, 1 ≤ m → p m ≤ p n :=
  ⟨1, by omega, fun m hm => by simp⟩

end Firoozbakht.RedTeamAttempt
