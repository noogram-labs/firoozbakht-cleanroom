/- Red-team corpus — ATTEMPT file `F21`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F21_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.

`cast_g` in `Equivalence.lean` is exactly this shape with the subtraction the
right way round and the `1 ≤ n` guard present. This is what it looks like
without either.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

theorem F21_attempt :
    ∀ n : ℕ, ((p n - p (n + 1) : ℕ) : ℝ) = (p n : ℝ) - (p (n + 1) : ℝ) := by
  intro n
  push_cast
  ring

end Firoozbakht.RedTeamAttempt
