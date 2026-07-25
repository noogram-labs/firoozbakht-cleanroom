/- Red-team corpus — ATTEMPT file `F13`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F13_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F13_attempt : ∀ n : ℕ, 1 ≤ n → T n < (g n : ℝ) := by
  intro n hn
  simp [T, g]
  norm_num

end Firoozbakht.RedTeamAttempt
