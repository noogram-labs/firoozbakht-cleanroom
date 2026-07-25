/-
# Exhaustive axiom audit

`audit.lean` prints `#print axioms` for a **hand-maintained list** of
declarations. That is a hazard, not a check: a `sorry` in a declaration nobody
thought to add to the list would never appear. This file removes the list. It
walks the whole environment, keeps every non-internal declaration in the
`Firoozbakht` namespace, and reports those that depend on `sorryAx`.

The invariant this development must satisfy:

    depending on sorryAx: [Firoozbakht.firoozbakht]

— one name, and that name is the open conjecture. Anything else is a bug or a
fabrication. Run:

    lake env lean audit_exhaustive.lean
-/

import Firoozbakht

open Lean Elab Command

run_cmd do
  let env ← getEnv
  let mut scanned : Nat := 0
  let mut bad : Array Name := #[]
  for (n, _) in env.constants.toList do
    if (`Firoozbakht).isPrefixOf n && !n.isInternal then
      scanned := scanned + 1
      let axs ← liftCoreM (Lean.collectAxioms n)
      if axs.contains ``sorryAx then
        bad := bad.push n
  logInfo m!"declarations scanned: {scanned}"
  logInfo m!"depending on sorryAx: {bad.qsort Name.lt}"
