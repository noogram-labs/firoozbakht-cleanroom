import Firoozbakht

/-! Axiom audit. Every declaration that depends on `sorryAx` is a *declared*
open target or a declared skeleton stub; everything else must be clean. Run:
`lake env lean audit.lean`. -/

open Firoozbakht

-- Sorry-free (must print only the three standard axioms):
#print axioms Firoozbakht.p_one
#print axioms Firoozbakht.p_five
#print axioms Firoozbakht.p_succ
#print axioms Firoozbakht.prime_p
#print axioms Firoozbakht.p_lt_p_succ
#print axioms Firoozbakht.refuted_of_witness
#print axioms Firoozbakht.cast_g
#print axioms Firoozbakht.p_pow_ne
#print axioms Firoozbakht.strict_iff_nonstrict
#print axioms Firoozbakht.F3_one
#print axioms Firoozbakht.F3_four
#print axioms Firoozbakht.firoozbakht_le_four

-- Declared open / skeleton (must show `sorryAx`):
#print axioms Firoozbakht.firoozbakht
#print axioms Firoozbakht.F3_iff_F2
#print axioms Firoozbakht.F1_iff_F3
#print axioms Firoozbakht.F2_iff_F1'
#print axioms Firoozbakht.F1'_iff_F4
#print axioms Firoozbakht.conjecture_iff_real
#print axioms Firoozbakht.conjecture_iff_gap
