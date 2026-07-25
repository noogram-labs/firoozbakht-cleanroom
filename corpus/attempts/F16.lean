/- Red-team corpus — ATTEMPT file `F16`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F16_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F16_attempt : ∃ N : ℕ, ∀ n : ℕ, N ≤ n → (p n : ℝ) ^ (1 / (n : ℝ)) < 1 :=
  ⟨1, fun n hn => by norm_num⟩

end Firoozbakht.RedTeamAttempt
