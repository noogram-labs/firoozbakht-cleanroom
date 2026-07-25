import Firoozbakht

/-! Axiom audit. After the `lean-probe` leg exactly **one** declaration in this
development depends on `sorryAx`: `Firoozbakht.firoozbakht`, the open conjecture.
Everything else — including the four `L1` equivalence steps, which were skeleton
stubs before the probe — must print only `[propext, Classical.choice, Quot.sound]`.

Run: `lake env lean audit.lean`. -/

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

-- Discharged by the `lean-probe` leg (these five were `sorry`-free helpers or
-- `sorry` stubs in the skeleton; all must now be clean):
#print axioms Firoozbakht.p_pos_real
#print axioms Firoozbakht.n_pos_real
#print axioms Firoozbakht.F3_iff_F2
#print axioms Firoozbakht.F1_iff_F3
#print axioms Firoozbakht.F2_iff_F1'
#print axioms Firoozbakht.F1'_iff_F4
#print axioms Firoozbakht.F1_iff_F2
#print axioms Firoozbakht.F1_iff_F1'
#print axioms Firoozbakht.F1_iff_F4
#print axioms Firoozbakht.F3_iff_F4
#print axioms Firoozbakht.conjecture_iff_real
#print axioms Firoozbakht.conjecture_iff_gap
#print axioms Firoozbakht.F1_le_four
#print axioms Firoozbakht.F4_le_four
#print axioms Firoozbakht.F1'_le_four

-- Declared open — the target of the attack. This one, and only this one, must
-- show `sorryAx`:
#print axioms Firoozbakht.firoozbakht
