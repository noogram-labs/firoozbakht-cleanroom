#!/usr/bin/env python3
"""
s3_recount.py -- round-3 skeptic, independent recount.

Written from the STATEMENT only:
  p_1 < p_2 < ... primes, 1-indexed.  T_n := p_n * (p_n^(1/n) - 1).
  A step is n with p_n, p_{n+1} both below the sieve bound N.
  Statistic: #{steps n : T_{n+1} < T_n} / #{steps}, under conventions
  "all n >= 1" and "n >= 10" (and, for the self-consistency test, "n >= 11").
Also: maximal-gap record enumeration (ordinal of g=248 at p=191912783),
and the four headline exponentials at 40 dps.
No upstream script was opened before writing this file; comparison with the
reconciliation leg's output happens only after this runs.
"""
import numpy as np
from mpmath import mp, mpf, log as mlog, expm1 as mexpm1, exp as mexp

mp.dps = 60

def sieve(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i*i::i] = False
    return np.flatnonzero(s)

def Tex(p, n):
    return mpf(int(p)) * mexpm1(mlog(mpf(int(p))) / mpf(int(n)))

def count(N):
    p = sieve(N); pi = len(p)
    n = np.arange(1, pi + 1, dtype=np.float64)
    pf = p.astype(np.float64)
    T = pf * np.expm1(np.log(pf) / n)
    dec = T[1:] < T[:-1]
    # exact re-adjudication of near ties
    rel = np.abs(T[1:] - T[:-1]) / np.maximum(np.abs(T[:-1]), 1.0)
    flips = 0
    for k in np.flatnonzero(rel < 1e-9):
        k = int(k); i = k + 1                     # step index n = i
        ex = Tex(p[k+1], i+1) < Tex(p[k], i)
        if bool(ex) != bool(dec[k]):
            dec[k] = ex; flips += 1
    out = {}
    for cut in (1, 10, 11):
        out[cut] = (int(pi - cut), int(dec[cut-1:].sum()))
    return pi, out, flips

for N in (3*10**6, 10**7, 10**8):
    pi, out, flips = count(N)
    print(f"N={N:,}  pi={pi:,}  near-tie flips={flips}")
    for cut in (1, 10, 11):
        s, d = out[cut]
        print(f"   n>={cut:<3} steps={s:,}  decreasing={d:,}  {100.0*d/s:.6f} %")

# maximal prime gap records
p = sieve(2*10**8)
g = np.diff(p)
rec, best, ordinal = [], 0, 0
for i, gi in enumerate(g):
    if gi > best:
        best = int(gi); ordinal += 1
        rec.append((ordinal, int(p[i]), best))
print(f"\nmaximal-gap records below 2e8: {len(rec)}")
for o, pp, gg in rec:
    if gg in (44, 248) or o in (12, 27, 28):
        print(f"   #{o}: p={pp:,} g={gg}")

print("\nexponentials at 40 dps:")
mp.dps = 40
for x in ("0.0017569", "0.0043636", "0.0516"):
    print(f"   e^-{x} = {mexp(-mpf(x))}")
print(f"   log 6690557 = {mlog(mpf(6690557))}")
print(f"   log 1772201 = {mlog(mpf(1772201))}")
