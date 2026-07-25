#!/usr/bin/env python3
"""Verification harness for proof-attempt-2 (target: unconditional-verified-range).

Checks, in-run and from scratch:
  V1  the exact equivalence F(n) <=> g_n < T_n on an integer sieve (exact integer form
      cross-checked against the float form)
  V2  Lemma A: for p_n >= 60184, T_n > L^2 - 1.1 L      (the Dusart-derived floor)
  V3  monotonicity of B1(p) = L^2 - 1.1 L
  V4  the first-occurrence reduction: for every gap value g occurring below the sieve
      bound, S(g) = exp((1.1 + sqrt(1.21 + 4g))/2), and the set of (g, p) pairs with
      p < max(S(g), 60184) that therefore still need a direct check
  V5  the criterion evaluated at the published record CSG point (p = 1693182318746371,
      g = 1132) and at the 2^64 frontier
  V6  margin of the criterion against the true bar T_n (cost of the reduction)
"""
import math
from decimal import Decimal, getcontext

N = 20_000_000
X0 = 60184  # Dusart validity threshold for pi(x) <= x/(log x - 1.1)


def sieve(n):
    b = bytearray([1]) * (n + 1)
    b[0] = b[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if b[i]:
            b[i * i :: i] = bytearray(len(b[i * i :: i]))
    return [i for i in range(n + 1) if b[i]]


primes = sieve(N)
print(f"sieve to {N}: {len(primes)} primes, largest {primes[-1]}")

# ---------------------------------------------------------------- V1
# exact integer form p_{n+1}^n < p_n^{n+1} for n = 1..400, vs float form
bad_int = []
for i in range(400):
    n = i + 1
    if primes[i + 1] ** n >= primes[i] ** (n + 1):
        bad_int.append(n)
print(f"V1a exact-integer violations of F, n<=400: {bad_int or 'none'}")

viol = []
maxratio, maxratio_n = 0.0, None
for i in range(len(primes) - 1):
    n = i + 1
    p, q = primes[i], primes[i + 1]
    L = math.log(p)
    T = p * math.expm1(L / n)
    g = q - p
    if g >= T:
        viol.append(n)
    r = g / T
    if n >= 10 and r > maxratio:
        maxratio, maxratio_n = r, n
print(f"V1b violations of g_n < T_n, n<={len(primes)-1}: {viol or 'none'}")
print(f"V1c max rho = g/T (n>=10): {maxratio:.7f} at n={maxratio_n}, "
      f"p={primes[maxratio_n-1]}, g={primes[maxratio_n]-primes[maxratio_n-1]}")

# ---------------------------------------------------------------- V2
# Lemma A: T_n > L^2 - 1.1 L for p_n >= 60184.  Check directly on the sieve.
fails = []
worst = None
for i in range(len(primes) - 1):
    n = i + 1
    p = primes[i]
    if p < X0:
        continue
    L = math.log(p)
    T = p * math.expm1(L / n)
    B1 = L * L - 1.1 * L
    slack = T - B1
    if slack <= 0:
        fails.append((n, p, T, B1))
    if worst is None or slack < worst[0]:
        worst = (slack, n, p, T, B1)
print(f"V2 Lemma A failures (p>=60184, sieve range): {len(fails)}")
print(f"   tightest slack T - B1 = {worst[0]:.6f} at n={worst[1]}, p={worst[2]} "
      f"(T={worst[3]:.4f}, B1={worst[4]:.4f})")

# also check the *derivation* step pi(p_n) <= p_n/(log p_n - 1.1) directly
dusart_fail = [ (i+1, primes[i]) for i in range(len(primes))
                if primes[i] >= X0 and (i + 1) > primes[i] / (math.log(primes[i]) - 1.1) ]
print(f"V2b Dusart pi(x) <= x/(log x - 1.1) failures on sieve (x>=60184): {len(dusart_fail)}")

# ---------------------------------------------------------------- V3
B1f = lambda p: math.log(p) ** 2 - 1.1 * math.log(p)
mono_fail = 0
prev = None
x = 2.0
while x < 1e19:
    v = B1f(x)
    if prev is not None and v <= prev:
        mono_fail += 1
    prev = v
    x *= 1.05
print(f"V3 B1 monotonicity failures over [2, 1e19] (geometric grid): {mono_fail}")
# analytic: d/dL (L^2 - 1.1 L) = 2L - 1.1 > 0 for L > 0.55 i.e. p > e^0.55 = 1.733
print(f"   analytic: 2L-1.1>0 iff p > e^0.55 = {math.exp(0.55):.4f}")

# ---------------------------------------------------------------- V4
S = lambda g: math.exp((1.1 + math.sqrt(1.21 + 4 * g)) / 2)
first_occ = {}
for i in range(len(primes) - 1):
    g = primes[i + 1] - primes[i]
    if g not in first_occ:
        first_occ[g] = (i + 1, primes[i])
print(f"V4 distinct gap values below {N}: {len(first_occ)}")
need_direct = [(g, n, p) for g, (n, p) in sorted(first_occ.items())
               if p < max(S(g), X0)]
print(f"   gap values whose FIRST occurrence sits below max(S(g), 60184): {len(need_direct)}")
print(f"   largest such first-occurrence prime: {max(p for _, _, p in need_direct)}")
# and: for every n in sieve range, is g_n <= B1(p_n) once p_n >= max(S(g_n), X0)?
bad = 0
for i in range(len(primes) - 1):
    p, g = primes[i], primes[i + 1] - primes[i]
    if p >= max(S(g), X0) and g > B1f(p):
        bad += 1
print(f"   consistency (p >= max(S(g),X0) implies g <= B1(p)): {bad} violations")
print("   S(g) samples:", {g: f"{S(g):.4g}" for g in (100, 300, 1000, 1132, 1476, 1550, 1920)})

# ---------------------------------------------------------------- V5
getcontext().prec = 60
for p, g, label in [(1693182318746371, 1132, "record CSG ratio (OEIS A111943 / Nicely)"),
                    (1425172824437699411, 1476, "first occurrence of gap 1476 (recalled)"),
                    (18361375334787046697, 1550, "maximal gap 1550 (recalled)")]:
    L = math.log(p)
    B1 = L * L - 1.1 * L
    print(f"V5 {label}: p={p} L={L:.6f} B1={B1:.4f} g={g} "
          f"-> {'SAFE' if g <= B1 else 'NOT SAFE'} (margin {(B1-g)/B1*100:.3f}%)")
L64 = math.log(2**64)
print(f"V5b at p = 2^64: L={L64:.6f}, B1={L64**2-1.1*L64:.3f}; "
      f"largest g provably safe everywhere below 2^64 via S(g)<=2^64: "
      f"{max(g for g in range(2, 4000, 2) if S(g) <= 2**64)}")

# ---------------------------------------------------------------- V6
# cost of the reduction: B1 vs Kourbatov's L^2-L-1.17 vs the true bar T
for p, n in [(primes[-1], len(primes) - 1), (1693182318746371, None)]:
    L = math.log(p)
    B1 = L * L - 1.1 * L
    KB = L * L - L - 1.17
    asym = L * L - L - 1
    print(f"V6 p={p}: B1={B1:.4f}  Kourbatov(L^2-L-1.17)={KB:.4f}  "
          f"L^2-L-1={asym:.4f}  B1 deficit vs Kourbatov = {KB-B1:.4f} "
          f"({(KB-B1)/KB*100:.4f}%)")

# ---------------------------------------------------------------- V7
G0 = max((primes[i + 1] - primes[i], primes[i]) for i in range(len(primes) - 1)
         if primes[i] < X0)
LX = math.log(X0)
print(f"V7 max gap with p_n < {X0}: g={G0[0]} at p={G0[1]}; "
      f"B({X0}) = {LX*LX - 1.1*LX:.4f}  -> dominates: {G0[0] < LX*LX - 1.1*LX}")
# exact-integer base case
bad0 = [i + 1 for i in range(len(primes) - 1) if primes[i] < X0
        and primes[i + 1] ** (i + 1) >= primes[i] ** (i + 2)]
print(f"V7b exact-integer base case, all p_n < {X0} "
      f"({sum(1 for p in primes if p < X0)} indices): {bad0 or 'NO VIOLATIONS'}")

# ---------------------------------------------------------------- V8
h = lambda p: p - 25 * math.log(p) ** 3 * (math.log(p) - 1.1)
lo, hi = 4e5, 1e7
for _ in range(200):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if h(mid) < 0 else (lo, mid)
print(f"V8 sign change of h(p) = p - 25 log^3 p (log p - 1.1): p* = {lo:.3f}")
print(f"   h(396738) = {h(396738):.1f} (<0, window open); h(1e6) = {h(1e6):.1f} (>0, closed)")
hprime = lambda p: 1 - (25 / p) * (4 * math.log(p) ** 3 - 3.3 * math.log(p) ** 2)
print(f"   h'(4e5) = {hprime(4e5):.4f} > 0 (h increasing on [4e5, inf))")
