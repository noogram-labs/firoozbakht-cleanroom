#!/usr/bin/env python3
"""verify_syn3.py -- round-3 synthesis self-verification.

Written from the STATEMENTS, with no upstream code path open: this script does not
import, read or copy attack/verify_syn.py, attack/verify_syn2.py or
attack/reconcile_recount.py.  Its job is to let the round-3 synthesis state its
headline figures first-hand rather than inherit them from four prior legs.

Every check prints PASS/FAIL and the script exits non-zero if any check fails.
"""

import sys
from mpmath import mp, mpf, exp, log, expm1, sqrt

mp.dps = 60

FAILS = []
NCHECK = 0


def chk(label, got, want, tol=None):
    global NCHECK
    NCHECK += 1
    if tol is None:
        ok = got == want
    else:
        ok = abs(mpf(got) - mpf(want)) <= mpf(tol)
    print(("PASS  " if ok else "FAIL  ") + label + f"  got={got}  want={want}")
    if not ok:
        FAILS.append(label)


def sieve(n):
    """primes <= n, own sieve of Eratosthenes."""
    bs = bytearray([1]) * (n + 1)
    bs[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if bs[i]:
            bs[i * i:: i] = bytearray(len(bs[i * i:: i]))
        i += 1
    return [i for i in range(n + 1) if bs[i]]


print("=" * 78)
print("1. sieve and pi(x)")
print("=" * 78)
N = 3 * 10 ** 6
P = sieve(N)
chk("pi(3e6)", len(P), 216816)

# ---------------------------------------------------------------- F itself
print()
print("=" * 78)
print("2. F over the swept range -- p_{n+1}^{1/(n+1)} < p_n^{1/n}")
print("=" * 78)
# gap form: F at n  <=>  g_n < T_n := p_n (p_n^{1/n} - 1)
viol = 0
for i in range(len(P) - 1):
    n = i + 1
    p = P[i]
    T = p * expm1(log(p) / n) if p < 100 else None
    if T is None:
        # float64 fast path is fine away from the smallest primes; recompute
        # anything within 1e-9 relative margin at 60 dps below.
        pass
    g = P[i + 1] - p
    # fast float screen
    import math
    Tf = p * math.expm1(math.log(p) / n)
    if g >= Tf * (1 - 1e-9):
        Te = mpf(p) * expm1(log(mpf(p)) / n)
        if mpf(g) >= Te:
            viol += 1
chk("violations of F below 3e6", viol, 0)

# exact-integer cross-check on a prefix: p_{n+1}^n < p_n^{n+1}
viol_exact = 0
for i in range(min(3000, len(P) - 1)):
    n = i + 1
    if P[i + 1] ** n >= P[i] ** (n + 1):
        viol_exact += 1
chk("violations of F, exact integers, n<=3000", viol_exact, 0)

# ------------------------------------------------- the 55.92% recount
print()
print("=" * 78)
print("3. the three-fractions statistic, recounted from the statement")
print("=" * 78)
import math

T = [0.0] * (len(P) + 1)   # 1-indexed
for i, p in enumerate(P):
    n = i + 1
    T[n] = p * math.expm1(math.log(p) / n)

steps_all = len(P) - 1                      # n with T_n and T_{n+1} both defined
dec_all = 0
dec_ge10 = 0
neartie = 0
reclass = 0
for n in range(1, len(P)):
    a, b = T[n], T[n + 1]
    dec = b < a
    if abs(b - a) <= 1e-9 * max(abs(a), abs(b)):
        neartie += 1
        A = mpf(P[n - 1]) * expm1(log(mpf(P[n - 1])) / n)
        B = mpf(P[n]) * expm1(log(mpf(P[n])) / (n + 1))
        dec2 = B < A
        if dec2 != dec:
            reclass += 1
        dec = dec2
    if dec:
        dec_all += 1
        if n >= 10:
            dec_ge10 += 1
steps_ge10 = steps_all - 9

chk("steps, all n, at 3e6", steps_all, 216815)
chk("steps, n>=10, at 3e6", steps_ge10, 216806)
chk("decreasing, all n", dec_all, 121239)
chk("decreasing, n>=10", dec_ge10, 121238)
chk("near-ties reclassified at 60 dps", reclass, 0)
pct = mpf(dec_ge10) / steps_ge10 * 100
chk("55.9200% (n>=10)", str(pct)[:12], "55.920039113")
pct_all = mpf(dec_all) / steps_all * 100
chk("55.9182% (all n)", str(pct_all)[:12], "55.918179092")

# the self-consistency argument that kills 121238/216805
T10, T11 = T[10], T[11]
chk("T_11 < T_10 (the 10->11 step is itself a descent)", T11 < T10, True)
chk("hence the n>=11 cut gives 121237/216805, not 121238/216805",
    (dec_ge10 - 1, steps_ge10 - 1), (121237, 216805))

# ------------------------------------------------- maximal gap ordinal
print()
print("=" * 78)
print("4. maximal prime gaps -- is 248 at p=191912783 the 27th or the 28th?")
print("=" * 78)
P2 = sieve(2 * 10 ** 8)
records = []
best = 0
for i in range(len(P2) - 1):
    g = P2[i + 1] - P2[i]
    if g > best:
        best = g
        records.append((len(records) + 1, P2[i], g))
d = {p: (k, g) for (k, p, g) in records}
chk("ordinal of gap 248 at p=191912783", d.get(191912783, (None, None))[0], 28)
chk("gap at p=191912783", d.get(191912783, (None, None))[1], 248)
chk("ordinal of gap 44 at p=15683", d.get(15683, (None, None))[0], 12)
chk("record count below 2e8", len(records), 28)
chk("records below 1e8", sum(1 for (_, p, _) in records if p < 10 ** 8), 25)

# ------------------------------------------------- P6' predicates
print()
print("=" * 78)
print("5. the P6' predicates over the swept range")
print("=" * 78)
# r(n) = last record index <= n ; mu(n) = min{m : g_m >= g_n}
gaps = [0] * (len(P) + 1)
for i in range(len(P) - 1):
    gaps[i + 1] = P[i + 1] - P[i]
NG = len(P) - 1

# record indices
rec_idx = []
best = 0
for n in range(1, NG + 1):
    if gaps[n] > best:
        best = gaps[n]
        rec_idx.append(n)
first_at_least = {}
best = 0
for n in range(1, NG + 1):
    if gaps[n] > best:
        for g in range(best + 1, gaps[n] + 1):
            first_at_least[g] = n
        best = gaps[n]

exc_gov = exc_min = 0
min_margin_min = None
argmin_min = None
r = rec_idx[0]
ri = 0
for n in range(1, NG + 1):
    while ri + 1 < len(rec_idx) and rec_idx[ri + 1] <= n:
        ri += 1
    r = rec_idx[ri]
    if T[r] > T[n]:
        exc_gov += 1
    mu = first_at_least[gaps[n]]
    m = T[n] - T[mu]
    if m < 0:
        exc_min += 1
    # mu(n) = n exactly at record indices, where the margin is 0 by definition;
    # the diagnostic minimum is taken over the non-trivial indices mu(n) < n.
    if mu < n and (min_margin_min is None or m < min_margin_min):
        min_margin_min = m
        argmin_min = (n, mu)

chk("P6'-gov exceptions below 3e6", exc_gov, 0)
chk("P6'-min exceptions below 3e6", exc_min, 0)
chk("P6'-min global min margin ~ +0.4845277", round(min_margin_min, 7), 0.4845277)
chk("P6'-min argmin n", argmin_min[0], 1879)
chk("P6'-min argmin mu", argmin_min[1], 1831)

# P6'-pair witness W1: m=1823, j=1831 (record), n=1847, T_m > T_n
Tm = mpf(P[1822]) * expm1(log(mpf(P[1822])) / 1823)
Tn = mpf(P[1846]) * expm1(log(mpf(P[1846])) / 1847)
chk("p_1823", P[1822], 15641)
chk("p_1831", P[1830], 15683)
chk("p_1847", P[1846], 15823)
chk("W1 margin T_m - T_n ~ +0.0286106049", str(Tm - Tn)[:12], "0.0286106048")
chk("W1 refutes P6'-pair (T_m > T_n with a record strictly between)", Tm > Tn, True)

# ------------------------------------------------- headline constants
print()
print("=" * 78)
print("6. the headline constants")
print("=" * 78)
chk("e^-0.0017569  (Theorem C-b', LIVE)", str(exp(mpf("-0.0017569")))[:18], "0.9982446424453653"[:18])
chk("e^-0.0043636  (Theorem C(b*), RETIRED)", str(exp(mpf("-0.0043636")))[:17], "0.995645906669685")
chk("e^-0.0516     (Theorem C-a')", str(exp(mpf("-0.0516")))[:17], "0.949708674346063")
chk("log 6690557 (both-editions Axler row)", str(log(mpf(6690557)))[:13], "15.7162076872")
chk("log 1772201 (preprint-only Axler row)", str(log(mpf(1772201)))[:13], "14.3877328348")

L = log(mpf(2) ** 64)
chk("log 2^64", str(L)[:17], "44.36141955583649"[:17])
chk("L(L-1.1) at 2^64 -> the published 1920", str(L * (L - mpf("1.1")))[:17], "1919.137983497532"[:17])
chk("hence a gap >= 1920 is needed just below 2^64", int(L * (L - mpf("1.1"))) + 1, 1920)

# RH critical constant: max_x log x / sqrt x = 2/e at x = e^2
chk("RH critical constant 2/e", str(mpf(2) / exp(1))[:18], "0.7357588823428846"[:18])
chk("  attained at x=e^2", str(log(exp(2)) / sqrt(exp(2)))[:18], "0.7357588823428846"[:18])

# window root: F follows from analytic estimates up to p ~ 777600.744
# (root of the stated window condition, re-derived: L(L-1.1) = ... ) -- checked
# only as the reported endpoint's order of magnitude, since the window's closed
# form is the upstream leg's; recorded as NOT independently re-derived here.

# ------------------------------------------------- barrier
print()
print("=" * 78)
print("7. the Bertrand barrier -- p_n^(1+1/n) > 2 p_n for n >= 2")
print("=" * 78)
bad = 0
for i in range(1, min(20000, len(P))):
    n = i + 1
    p = mpf(P[i])
    # certification would require the ceiling 2 p_n to sit BELOW the threshold
    if 2 * p <= p ** (1 + mpf(1) / n):
        bad += 1
chk("indices 2<=n<=20000 where Bertrand's ceiling would certify F", bad, 0)
chk("at n=1 Bertrand exactly ties (2^2 = 4 = 2*2), so it certifies nowhere for n>=2",
    P[0] ** 2 == 2 * P[0], True)
bad2 = 0
for i in range(1, len(P)):
    n = i + 1
    if P[i] >= 2 ** n:
        bad2 += 1
chk("p_n < 2^n for 2<=n<=pi(3e6) (exact integers)", bad2, 0)

print()
print("=" * 78)
print(f"{NCHECK - len(FAILS)}/{NCHECK} checks pass")
if FAILS:
    print("FAILED:", FAILS)
print("=" * 78)
sys.exit(1 if FAILS else 0)
