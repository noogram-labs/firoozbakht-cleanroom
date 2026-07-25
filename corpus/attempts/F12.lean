/- Red-team corpus — ATTEMPT file `F12`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F12_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F12_attempt : ∀ n : ℕ, 1 ≤ n → (g n : ℝ) < Real.log (p n) := by
  intro n hn
  simp [g]
  norm_num

end Firoozbakht.RedTeamAttempt
