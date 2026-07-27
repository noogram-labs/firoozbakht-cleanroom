#!/usr/bin/env python3
"""
reconcile_recount.py — round-3 reconciliation leg, decision 4.

Recount the `55.92 %` non-monotonicity statistic FROM THE STATEMENT, with no
reference to any prior derivation, script or reported figure in this galaxy.

STATEMENT USED (and nothing else):
  p_1 < p_2 < ... are the primes, 1-indexed (p_1 = 2).
  T_n := p_n * (p_n^(1/n) - 1).
  A "step" is an index n such that BOTH T_n and T_{n+1} are defined from the
  sieve, i.e. both p_n and p_{n+1} are known, i.e. n <= pi(N) - 1.
  The statistic is  #{ steps n : T_{n+1} < T_n }  /  #{ steps }.
  Two conventions circulate: all n >= 1, and n >= 10.

Method: own sieve of Eratosthenes; float64 pass; every comparison whose
relative margin is within 1e-9 is re-adjudicated with mpmath at 60 dps.
No number below is read from an upstream artifact.
"""
import sys
import numpy as np
from mpmath import mp, mpf, log as mlog, expm1 as mexpm1

mp.dps = 60


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.flatnonzero(s)


def T_exact(p, n):
    return mpf(p) * mexpm1(mlog(mpf(p)) / mpf(n))


def recount(N):
    p = primes_upto(N)
    pi = len(p)
    idx = np.arange(1, pi + 1, dtype=np.float64)
    pf = p.astype(np.float64)
    # T_n in float64
    T = pf * np.expm1(np.log(pf) / idx)
    # steps: n = 1 .. pi-1
    lo, hi = T[:-1], T[1:]
    dec = hi < lo
    # re-adjudicate near-ties at 60 dps
    denom = np.maximum(np.abs(lo), 1.0)
    tight = np.flatnonzero(np.abs(hi - lo) / denom < 1e-9)
    fixed = 0
    for k in tight:
        n = int(k) + 1
        exact = T_exact(int(p[k + 1]), n + 1) < T_exact(int(p[k]), n)
        if bool(exact) != bool(dec[k]):
            dec[k] = exact
            fixed += 1
    steps_all = pi - 1                      # n = 1 .. pi-1
    dec_all = int(dec.sum())
    steps_ge10 = pi - 10                    # n = 10 .. pi-1
    dec_ge10 = int(dec[9:].sum())
    return dict(N=N, pi=pi, largest=int(p[-1]),
                steps_all=steps_all, dec_all=dec_all,
                steps_ge10=steps_ge10, dec_ge10=dec_ge10,
                near_ties=len(tight), reclassified=fixed)


def main():
    rows = []
    for N in (3 * 10 ** 6, 10 ** 7, 10 ** 8):
        r = recount(N)
        rows.append(r)
        print(f"N = {N:>12,}  pi(N) = {r['pi']:>10,}  largest = {r['largest']:>11,}")
        print(f"    steps (all n)   = {r['steps_all']:>10,}   decreasing = {r['dec_all']:>10,}"
              f"   = {100.0*r['dec_all']/r['steps_all']:.6f} %")
        print(f"    steps (n >= 10) = {r['steps_ge10']:>10,}   decreasing = {r['dec_ge10']:>10,}"
              f"   = {100.0*r['dec_ge10']/r['steps_ge10']:.6f} %")
        print(f"    near-ties re-adjudicated at 60 dps: {r['near_ties']} examined,"
              f" {r['reclassified']} reclassified")
        sys.stdout.flush()

    # 10^9 sweep size, for card L15's `50 847 5xx` figure: pi(10^9) - 1.
    # Computed by a segmented count rather than a full boolean array.
    print()
    print("pi(10^9) by segmented sieve (for the L15 sweep-size figure):")
    N = 10 ** 9
    base = primes_upto(int(N ** 0.5) + 1)
    seg = 1 << 22
    count = 0
    start = 2
    while start <= N:
        stop = min(start + seg - 1, N)
        block = np.ones(stop - start + 1, dtype=bool)
        for q in base:
            if q * q > stop:
                break
            first = max(q * q, ((start + q - 1) // q) * q)
            if first <= stop:
                block[first - start::q] = False
        if start <= 1:
            block[:2 - start] = False
        count += int(block.sum())
        start = stop + 1
    print(f"    pi(10^9) = {count:,}   consecutive steps = {count - 1:,}")
    return rows


if __name__ == "__main__":
    main()
