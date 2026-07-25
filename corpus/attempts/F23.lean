/- Red-team corpus — ATTEMPT file `F23`.

Expected verdict: **rejected**. `lake env lean` on this file MUST exit non-zero.
The claim is false (proved false in `../refutations/`, theorem `F23_refuted`)
or the file is ill-formed; the proof below is the most plausible attempt a
careless author would write. If this file ever compiles, the checker is broken.
-/

import Firoozbakht.Statement
import Firoozbakht.FiniteCheck

namespace Firoozbakht.RedTeamAttempt

open Firoozbakht

/- Evaluation cheat, harder: `native_decide` would also add the compiler and
the runtime to the trusted base even if it worked. It does not work here —
`Nat.nth` is noncomputable. -/

theorem F23_attempt : F3 1 := by native_decide

end Firoozbakht.RedTeamAttempt
