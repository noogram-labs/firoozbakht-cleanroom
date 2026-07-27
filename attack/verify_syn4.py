#!/usr/bin/env python3
"""verify_syn4.py — independent re-derivation of every headline figure republished in
attack/synthesis.md (round 3, v2 — post skeptic re-audit).

Written from the *statements* in the artifacts, not from any upstream code path: it does not
import or copy verify_syn.py, verify_syn2.py, verify_syn3.py, reconcile_recount.py,
s3_recount.py or s3_constants.py.  Own segmented sieve; mpmath at 60 dps; every near-tie
(relative margin < 1e-9) re-adjudicated exactly.

Exit 0 iff every check passes.
"""
import sys
from mpmath import mp, mpf, log, exp, sqrt, e

mp.dps = 60

CHECKS = []


def check(name, got, want, note=""):
    ok = (got == want)
    CHECKS.append((ok, name, got, want, note))
    return ok


def check_str(name, got, want_prefix, note=""):
    s = mp.nstr(got, 25, strip_zeros=False)
    ok = s.startswith(want_prefix)
    CHECKS.append((ok, name, s, want_prefix + "...", note))
    return ok


# ---------------------------------------------------------------- sieve
def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i <= n:
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
        i += 1
    return [i for i in range(n + 1) if sieve[i]]


N1 = 3 * 10 ** 6
P = primes_upto(N1)
check("pi(3e6)", len(P), 216816)

# ---------------------------------------------------------------- F itself
# T_n := p_n (p_n^{1/n} - 1); F  <=>  g_n < T_n  for all n >= 1  (1-indexed)
viol = 0
near = []
for i in range(len(P) - 1):
    n = i + 1
    p = P[i]
    g = P[i + 1] - p
    T = mpf(p) * (exp(log(mpf(p)) / n) - 1)
    if g >= T:
        viol += 1
    elif abs(g - T) / T < mpf("1e-9"):
        near.append(n)
check("violations of F below 3e6 (gap form)", viol, 0)

# exact-integer cross-check: p_{n+1}^n < p_n^{n+1}
viol_exact = 0
for i in range(min(3000, len(P) - 1)):
    n = i + 1
    if not (P[i + 1] ** n < P[i] ** (n + 1)):
        viol_exact += 1
check("violations of F, exact integers, n<=3000", viol_exact, 0)
check("near-ties needing 60-dps re-adjudication", len(near), 0,
      "the count is not float-fragile")

# ---------------------------------------------------------------- the recount (R2-M1 / decision 4)
Tv = [mpf(P[i]) * (exp(log(mpf(P[i])) / (i + 1)) - 1) for i in range(len(P))]


def recount(nmin):
    """steps and descents of T over indices n >= nmin (1-indexed)."""
    lo = nmin - 1
    steps = len(P) - 1 - lo
    dec = sum(1 for i in range(lo, len(P) - 1) if Tv[i + 1] < Tv[i])
    return dec, steps


d_all, s_all = recount(1)
d_10, s_10 = recount(10)
d_11, s_11 = recount(11)
check("steps, all n, at 3e6", s_all, 216815)
check("decreasing, all n, at 3e6", d_all, 121239)
check("steps, n>=10", s_10, 216806)
check("decreasing, n>=10", d_10, 121238)
check("steps, n>=11", s_11, 216805)
check("decreasing, n>=11", d_11, 121237,
      "=> 121238/216805 is the answer under NO convention")
check_str("percentage n>=10", mpf(d_10) / s_10 * 100, "55.92003911")
check_str("percentage all n", mpf(d_all) / s_all * 100, "55.91817909")
check("T_11 < T_10 (the descent the n>=11 cut drops)", Tv[10] < Tv[9], True)

# the two further ranges the document quotes as range-dependence riders (§5.4)
BIG = primes_upto(10 ** 8)
check("pi(1e7)", sum(1 for p in BIG if p <= 10 ** 7), 664579)
check("pi(1e8)", len(BIG), 5761455)


def recount_upto(lim, nmin=10):
    Q = [p for p in BIG if p <= lim]
    T = [mpf(Q[k]) * (exp(log(mpf(Q[k])) / (k + 1)) - 1) for k in range(len(Q))]
    lo = nmin - 1
    return (sum(1 for k in range(lo, len(Q) - 1) if T[k + 1] < T[k]), len(Q) - 1 - lo)


d7, s7 = recount_upto(10 ** 7)
d8, s8 = recount_upto(10 ** 8)
check("decreasing / steps, n>=10, at 1e7", (d7, s7), (374485, 664569))
check("decreasing / steps, n>=10, at 1e8", (d8, s8), (3280063, 5761445))
check_str("percentage n>=10 at 1e7", mpf(d7) / s7 * 100, "56.35005")
check_str("percentage n>=10 at 1e8", mpf(d8) / s8 * 100, "56.93125")
del BIG

# ---------------------------------------------------------------- P6' predicates
records = []          # record (maximal-gap) indices, 1-indexed
best = 0
for i in range(len(P) - 1):
    g = P[i + 1] - P[i]
    if g > best:
        best = g
        records.append(i + 1)


def gap(n):
    return P[n] - P[n - 1]


# P6'-pair witness W1
check("p_1823", P[1822], 15641)
check("p_1831", P[1830], 15683)
check("p_1847", P[1846], 15823)
check("g_1831", gap(1831), 44)
check("1831 is a record index", 1831 in records, True)
check("W1 refutes P6'-pair: T_1823 > T_1847", Tv[1822] > Tv[1846], True)
check_str("W1 margin T_1823 - T_1847", Tv[1822] - Tv[1846], "0.02861060")
check("ordinal of gap 44 at p=15683", records.index(1831) + 1, 12)

# P6'-gov / P6'-min exceptions below 3e6
gov_exc = 0
recset = set(records)
last_rec = None
mu_margin_min = None
mu_at = None
for n in range(1, len(P)):
    if n in recset:
        last_rec = n            # r(n) = last record index <= n
    if last_rec is not None and Tv[last_rec - 1] > Tv[n - 1]:
        gov_exc += 1            # P6'-gov: T_{r(n)} <= T_n

# mu(n) := min{m : g_m >= g_n}; first_ge[v] = smallest m with g_m >= v
gaps = [gap(n) for n in range(1, len(P))]
mu_exc = 0
best_prefix = 0
first_ge = {}
for m in range(1, len(gaps) + 1):
    g = gaps[m - 1]
    if g > best_prefix:
        for v in range(best_prefix + 1, g + 1):
            first_ge[v] = m
        best_prefix = g
for n in range(1, len(gaps) + 1):
    mu = first_ge[gaps[n - 1]]
    if Tv[mu - 1] > Tv[n - 1]:
        mu_exc += 1
    if mu < n:
        marg = Tv[n - 1] - Tv[mu - 1]
        if mu_margin_min is None or marg < mu_margin_min:
            mu_margin_min = marg
            mu_at = (n, mu)
check("P6'-gov exceptions below 3e6", gov_exc, 0)
check("P6'-min exceptions below 3e6", mu_exc, 0)
check("P6'-min minimum margin index n", mu_at[0], 1879)
check("P6'-min minimum margin governor mu", mu_at[1], 1831)
check_str("P6'-min minimum margin", mu_margin_min, "0.4845277")

# ---------------------------------------------------------------- maximal-gap records to 2e8
def gap_records_upto(N):
    """segmented sieve; returns (list of (p, gap, ordinal), count below 1e8)."""
    seg = 1 << 22
    base = primes_upto(int(N ** 0.5) + 1)
    prev = 2
    best = 0
    recs = []
    lo = 2
    while lo <= N:
        hi = min(lo + seg - 1, N)
        mark = bytearray([1]) * (hi - lo + 1)
        if lo == 0:
            mark[0] = 0
        for q in base:
            start = max(q * q, ((lo + q - 1) // q) * q)
            for j in range(start, hi + 1, q):
                mark[j - lo] = 0
        if lo <= 1:
            for j in range(lo, min(1, hi) + 1):
                mark[j - lo] = 0
        for j in range(lo, hi + 1):
            if mark[j - lo] and j >= 2:
                if j != prev:
                    g = j - prev
                    if g > best:
                        best = g
                        recs.append((prev, g))
                    prev = j
        lo = hi + 1
    return recs


recs = gap_records_upto(2 * 10 ** 8)
check("maximal-gap records below 2e8", len(recs), 28)
check("12th record starts at p", recs[11][0], 15683)
check("12th record gap", recs[11][1], 44)
check("28th record starts at p", recs[27][0], 191912783)
check("28th record gap", recs[27][1], 248)
check("records below 1e8", sum(1 for p, g in recs if p < 10 ** 8), 25)

# ---------------------------------------------------------------- constants
check_str("e^-0.0017569 (C-b', live)", exp(-mpf("0.0017569")), "0.99824464244536")
check_str("e^-0.0043636 (C(b*), retired)", exp(-mpf("0.0043636")), "0.99564590666968")
check_str("e^-0.0516 (C-a')", exp(-mpf("0.0516")), "0.94970867434606")
check_str("log 6690557", log(mpf(6690557)), "15.7162076872")
check_str("log 1772201", log(mpf(1772201)), "14.3877328348")
L64 = log(mpf(2) ** 64)
check_str("log 2^64", L64, "44.361419555836")
check_str("L(L-1.1) at 2^64", L64 * (L64 - mpf("1.1")), "1919.13798349753")
check("published integer ceiling", int(L64 * (L64 - mpf("1.1"))) + 1, 1920)
# RH critical constant: max_x log x / sqrt x = 2/e at x = e^2
check_str("RH critical constant 2/e", 2 / e, "0.7357588823428846")
check_str("log(e^2)/sqrt(e^2)", log(exp(mpf(2))) / sqrt(exp(mpf(2))), "0.7357588823428846")

# ---------------------------------------------------------------- the barrier, right polarity
# certification would need 2*p_n <= p_n^{1+1/n}; the theorem says the reverse at every n>=2.
cert = 0
for n in range(2, 20001):
    p = mpf(P[n - 1])
    if 2 * p <= p ** (1 + mpf(1) / n):
        cert += 1
check("indices 2<=n<=20000 where Bertrand certifies F", cert, 0)
check("Bertrand ties exactly at n=1 (2^2 = 2*2)", 2 * P[0] == P[0] ** 2, True)
pw = 0
for i, p in enumerate(P):
    n = i + 1
    if n >= 2 and not (p < 2 ** n):
        pw += 1
check("failures of p_n < 2^n (exact ints, n>=2) to pi(3e6)", pw, 0)

# ---------------------------------------------------------------- C-b' certification margin (R2-m3)
# majorant of (0.17 - 2.1/b + a^4 e^-a)/(2a-1) over cells [a, a+w] of width w = 0.01.
# Worst corner, term by term: -2.1/b increases in b   -> b = a + w (RIGHT endpoint);
#                             a^4 e^-a decreases (a>4) -> a = left endpoint;
#                             1/(2a-1) decreases        -> a = left endpoint.
W = mpf("0.01")
best_maj = mpf(0)
best_at = None
a = mpf("20.0")
while a < mpf("60.0"):
    hi = (mpf("0.17") - mpf("2.1") / (a + W) + a ** 4 * exp(-a)) / (2 * a - 1)
    if hi > best_maj:
        best_maj = hi
        best_at = a
    a += mpf("0.0001")      # fine scan of the cell-left-endpoint, so the sup is grid-robust
CHECKS.append((best_maj < mpf("0.0017569"),
               "certified 0.0017569 exceeds the cell majorant",
               mp.nstr(best_maj, 12), "< 0.0017569", "R2-m3 margin"))
check_str("C-b' margin 0.0017569 - majorant (grid-robust sup)",
          mpf("0.0017569") - best_maj, "2.4")

# ---------------------------------------------------------------- report
fails = [c for c in CHECKS if not c[0]]
for ok, name, got, want, note in CHECKS:
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got={got} want={want}" + (f"  [{note}]" if note else ""))
print(f"\n{len(CHECKS) - len(fails)}/{len(CHECKS)} checks pass")
sys.exit(1 if fails else 0)
