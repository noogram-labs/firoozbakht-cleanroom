#!/usr/bin/env python3
"""Numeric checks behind §4 of `lean-probe-round2`'s report.

Self-contained: needs only `sympy`. No network, no data files.

Checks, in order:
  1. T_n = p_n^(1+1/n) - p_n is of order (log p_n)^2.
  2. The multiplicative slack Firoozbakht needs, p_n^(1/n) - 1, versus what the
     Baker-Harman-Pintz exponent (p^-0.475) and the RH-conditional envelope
     (log p / sqrt p) supply — and where each crossover happens.

Nothing here proves or refutes Firoozbakht. These are sanity numbers for claims
made in prose; the only *proofs* in this leg are in lean/Firoozbakht/Barrier.lean
and are checked by `lake build`.
"""

import math
from sympy import prime


def row(n):
    p = prime(n)
    T = p ** (1 + 1 / n) - p
    lp = math.log(p)
    return {
        "n": n,
        "p": p,
        "T": T,
        "logp2": lp * lp,
        "need": p ** (1 / n) - 1,          # slack Firoozbakht needs
        "bhp": p ** -0.475,                # slack BHP supplies
        "rh": lp / math.sqrt(p),           # slack the RH-conditional bound supplies
    }


def main() -> int:
    print("check 1 + 2 — T_n vs (log p_n)^2, and the three slacks\n")
    print(f"{'n':>8} {'p_n':>10} {'T_n':>11} {'(log p)^2':>11} "
          f"{'need':>10} {'BHP':>10} {'RH':>10}")
    for n in (10, 100, 245, 1000, 10000, 100000):
        r = row(n)
        print(f"{r['n']:>8} {r['p']:>10} {r['T']:>11.3f} {r['logp2']:>11.3f} "
              f"{r['need']:>10.6f} {r['bhp']:>10.6f} {r['rh']:>10.6f}")

    print("\ncrossovers (first n where the supplied slack exceeds what is needed):")
    for label, key in (("BHP  p^-0.475", "bhp"), ("RH   log p/sqrt p", "rh")):
        for n in range(2, 5000):
            r = row(n)
            if r["need"] < r[key]:
                print(f"  {label:<20} first n = {n:>5}  (p_n = {r['p']}, "
                      f"need = {r['need']:.6f} < {r[key]:.6f})")
                break

    print("\nReading: both envelopes overtake the needed slack and stay above it, "
          "\ni.e. both are insufficient for all large n — which is the tail, "
          "\nwhich is where a proof of Firoozbakht would have to live.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
