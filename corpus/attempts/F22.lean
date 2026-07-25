/- Red-team corpus — ATTEMPT file `F22`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F22_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

/- Evaluation cheat: `decide` on a statement about `Nat.nth`, which is
`noncomputable` (card `T4`, Fact 1) — there is no kernel reduction at all.
The *statement* `F3 1` is true; the *certification* is not. -/

theorem F22_attempt : F3 1 := by decide

end Firoozbakht.RedTeamAttempt
