/- Red-team corpus — ATTEMPT file `F18`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F18_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F18_attempt : ∀ n : ℕ, 1 ≤ n → T (n + 1) < T n := by
  intro n hn
  simp [T]
  norm_num

end Firoozbakht.RedTeamAttempt
