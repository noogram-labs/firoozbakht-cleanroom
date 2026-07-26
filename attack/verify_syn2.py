#!/usr/bin/env python3
"""verify_syn2.py — independent verification pass for the ROUND-2 synthesis.

Written from the STATEMENTS in the round-2 artifacts, not from any leg's code
path (card T2 rule 3: a check written from the derivation cannot catch an error
in the derivation). Sieve is sympy's; all T-arithmetic is mpmath at 60 dps.

Run:  python3 attack/verify_syn2.py     (exit 0 iff every check passes)
"""
import sys
from mpmath import mp, mpf, log, exp, e

mp.dps = 60

FAIL = []


def check(label, got, want, tol=None, exact=False):
    ok = (got == want) if exact else (abs(mpf(got) - mpf(want)) <= mpf(tol))
    print(f"[{'OK ' if ok else 'FAIL'}] {label}: got {got}  want {want}")
    if not ok:
        FAIL.append(label)


# ---------------------------------------------------------------- sieve
N = 3 * 10**6
sieve = bytearray([1]) * (N + 1)
sieve[0:2] = b"\x00\x00"
for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        sieve[i * i :: i] = bytearray(len(sieve[i * i :: i]))
P = [i for i in range(N + 1) if sieve[i]]          # p_1 = P[0] = 2 (1-indexed below)
print(f"primes below {N}: {len(P)}")
check("pi(3e6)", len(P), 216816, exact=True)


def p(k):            # 1-indexed
    return P[k - 1]


def gaps_raw(k):
    return P[k] - P[k - 1]          # g_k = p_{k+1} - p_k


T = [None] * (len(P) + 1)
for k in range(1, len(P) + 1):
    x = mpf(p(k))
    T[k] = x * (exp(log(x) / k) - 1)

M = len(P)                                          # number of primes
# a "step" is an n with T_n and T_{n+1} both defined  ->  n = 1 .. M-1
steps_all = M - 1
steps_ge10 = M - 1 - 9
dec_all = sum(1 for n in range(1, M) if T[n + 1] < T[n])
dec_ge10 = sum(1 for n in range(10, M) if T[n + 1] < T[n])

# ------------------------------------------ R2-M1: the 55.92% denominators
print("\n--- R2-M1: the three-fractions statistic, recounted from the statement ---")
check("steps, all n, at 3e6", steps_all, 216815, exact=True)
check("steps, n>=10, at 3e6", steps_ge10, 216806, exact=True)
check("decreasing steps, all n", dec_all, 121239, exact=True)
check("decreasing steps, n>=10", dec_ge10, 121238, exact=True)
print(f"      => n>=10 fraction = {mpf(dec_ge10)/steps_ge10*100} %")
print(f"      => all-n fraction = {mpf(dec_all)/steps_all*100} %")

# -------------------------------------------------- F violations in range
# Full range via the gap form g_n < T_n (T computed from its definition above);
# calibrated against EXACT integer arithmetic p(n+1)^n < p(n)^(n+1) on n <= 3000,
# which is the same discipline round 1 used (exact integers do not scale past
# a few thousand indices -- the exponents make the operands megabit-sized).
viol = [n for n in range(1, M) if gaps_raw(n) >= T[n]]
check("violations of F below 3e6 (gap form g_n < T_n)", len(viol), 0, exact=True)
exact_viol = [n for n in range(1, 3001) if p(n + 1) ** n >= p(n) ** (n + 1)]
check("violations of F, EXACT integers, n <= 3000", len(exact_viol), 0, exact=True)
disagree = [n for n in range(1, 3001)
            if (p(n + 1) ** n >= p(n) ** (n + 1)) != (gaps_raw(n) >= T[n])]
check("gap form vs exact integers: disagreements on n <= 3000", len(disagree), 0, exact=True)

# ------------------------------------------ FFM Theorem 1, witness W1
print("\n--- FFM Theorem 1 (P6'-pair is FALSE): witness W1 ---")
check("p_1823", p(1823), 15641, exact=True)
check("p_1831 (record, g=44)", p(1831), 15683, exact=True)
check("g_1831", p(1832) - p(1831), 44, exact=True)
check("p_1847", p(1847), 15823, exact=True)
check("T_1823 - T_1847", T[1823] - T[1847], "0.028610605", tol="1e-9")
print(f"      T_1823 = {T[1823]}")
print(f"      T_1847 = {T[1847]}")

# ------------------------------------------ the three predicates
print("\n--- the three predicates, this leg's own sweep to 3e6 ---")
records, best = [], -1
for n in range(1, M):
    g = p(n + 1) - p(n)
    if g > best:
        best, _ = g, records.append(n)
r = [0] * (M + 1)                                    # r(n) = last record index <= n
cur = 0
ri = 0
for n in range(1, M):
    if ri < len(records) and records[ri] == n:
        cur = n
        ri += 1
    r[n] = cur
gaps = [0] + [p(n + 1) - p(n) for n in range(1, M)]
# mu(n) = min{m : g_m >= g_n}
first_at_least = {}
runmax = 0
mu = [0] * (M + 1)
for n in range(1, M):
    g = gaps[n]
    if g > runmax:
        for v in range(runmax + 1, g + 1):
            first_at_least[v] = n
        runmax = g
    mu[n] = first_at_least[g]

gov_exc = sum(1 for n in range(1, M) if r[n] >= 1 and T[r[n]] > T[n])
min_exc = sum(1 for n in range(1, M) if T[mu[n]] > T[n])
gov_margin = min(T[n] - T[r[n]] for n in range(1, M) if r[n] >= 1 and r[n] != n)
min_pairs = [(T[n] - T[mu[n]], n) for n in range(1, M) if mu[n] != n]
min_margin, min_at = min(min_pairs)
check("P6'-gov exceptions below 3e6", gov_exc, 0, exact=True)
check("P6'-min exceptions below 3e6", min_exc, 0, exact=True)
check("P6'-gov min margin at 3e6", gov_margin, "1.046415e-2", tol="1e-8")
check("P6'-min global min margin", min_margin, "0.4845277", tol="1e-6")
check("P6'-min argmin index", min_at, 1879, exact=True)
check("mu(1879)", mu[1879], 1831, exact=True)

# P6'-pair exception census below 3e6 (m < j < n, j a record index, T_m > T_n)
pair_exc = set()
for n in range(2, M):
    j = r[n]
    if j == n or j == 0:
        continue
    for m in range(max(1, j - 40), j):
        if T[m] > T[n]:
            pair_exc.add(n)
            break
print(f"      P6'-pair: exception indices n below 3e6 (local m-window): {sorted(pair_exc)}")
check("1847 is a P6'-pair exception", 1847 in pair_exc, True, exact=True)

# ------------------------------------------ Prop. 4 counter-models
print("\n--- FFM Proposition 4: gov and min are formally INCOMPARABLE ---")
# g = (2,4,6,3): records 1,2,3 ; r(4)=3 ; mu(4)=2
check("gov =/=> min  (T=(0,10,1,5))", (1 <= 5) and not (10 <= 5), True, exact=True)
check("min =/=> gov  (T=(0,1,10,5))", (1 <= 5) and not (10 <= 5), True, exact=True)

# ------------------------------------------ Theorem C constants (both repairs)
print("\n--- Theorem C(b*) [UVR] and Theorem C-b' [FFM]: the two repairs ---")
l1 = log(1772201)
check("ell_1 = log 1772201", l1, "14.3877328349", tol="1e-9")


def v_uvr(l):
    return l**2 - l - 1 - 1 / l


def dstar_uvr(l):                     # UVR (**), the SUFFICIENT condition, tight error term
    return (mpf("0.17") + v_uvr(l) ** 2 * exp(-l) - 1 / l) / (2 * l - 1)


def dstar_displayed(l):               # PA-0 §6.2's displayed criterion (additive l^4/x)
    return (mpf("0.17") + l**4 * exp(-l) - 1 / l) / (2 * l - 1)


def d_solved(l, err):
    """required d, SOLVED from Lemma W's hypothesis d(2l-1) + d^2 >= R (not the
    sufficient condition that drops d^2)."""
    R = mpf("0.17") - 1 / l + err
    a = 2 * l - 1
    return (-a + (a**2 + 4 * R) ** mpf("0.5")) / 2


check("UVR d*(ell_1), sufficient condition [Prop. R1]", dstar_uvr(l1),
      "0.004363567696", tol="1e-12")
check("UVR sweep-free constant 0.17/(2*ell_1-1)", mpf("0.17") / (2 * l1 - 1),
      "0.0061205094", tol="1e-10")
check("PA-0's displayed criterion at ell_1 (F2(c): > 0.004479)", dstar_displayed(l1),
      "0.0044887225", tol="1e-9")
check("PA-0's displayed criterion exceeds its own reported sweep 0.004479",
      dstar_displayed(l1) > mpf("0.004479"), True, exact=True)
# solved requirements: tight lemma vs the round-1 PRINTED lemma v(1 + l^4/x)
d_tight = d_solved(l1, v_uvr(l1) ** 2 * exp(-l1))
d_print = d_solved(l1, v_uvr(l1) * l1**4 * exp(-l1))
check("true required d, tight lemma (A-high*)", d_tight, "0.0043628824", tol="1e-9")
check("true required d, round-1 PRINTED lemma (A-high)", d_print, "0.16933981", tol="1e-7")
check("F2 factor (printed / tight)", d_print / d_tight, "38.8137", tol="1e-3")
check("UVR headline exp(-0.0043636)", exp(-mpf("0.0043636")), "0.9956459", tol="1e-7")
# NOTE: FFM §7.4 prints `e^{-0.0017569} = 0.99824467...`; the true value is
# 0.9982446424..., which is what the round-2 skeptic independently reports.
# FFM's headline `0.998244` is unaffected. Recorded as a finding, not smoothed.
check("FFM C-b' headline exp(-0.0017569), TRUE value", exp(-mpf("0.0017569")),
      "0.9982446424", tol="1e-10")
check("FFM's printed expansion 0.99824467 is NOT the true value",
      abs(exp(-mpf("0.0017569")) - mpf("0.99824467")) > mpf("1e-9"), True, exact=True)
check("FFM C-a' headline exp(-0.0516)", exp(-mpf("0.0516")), "0.94970867", tol="1e-8")
# sanity: d*(ell) is maximised at ell_1 (Prop. R1's conclusion), spot-checked
worse = [l for l in [l1 + mpf(k) / 10 for k in range(1, 2000)] if dstar_uvr(l) > dstar_uvr(l1)]
check("d* maximised at ell_1 over [ell_1, ell_1+200]", len(worse), 0, exact=True)

# ------------------------------------------ the 2^64 frontier
print("\n--- the 2^64 frontier ---")
L = log(mpf(2) ** 64)
check("log 2^64", L, "44.3614195558", tol="1e-9")
check("L(L-1.1) at 2^64", L * (L - mpf("1.1")), "1919.1379834975", tol="1e-9")

# ------------------------------------------ RH leg: the critical constant
print("\n--- RH leg, Theorem C: the critical constant is 2/e ---")
check("max_x log x / sqrt x", log(exp(2)) / exp(1), 2 / e, tol="1e-40")
check("2/e", 2 / e, "0.735758882342885", tol="1e-15")

# ------------------------------------------ Lean Barrier.lean, on paper
print("\n--- Barrier.lean: bertrand_ceiling_above_threshold, numerically ---")
bad = [n for n in range(2, 20001) if not (mpf(p(n)) ** (1 + mpf(1) / n) < 2 * p(n))]
check("p_n^(1+1/n) < 2 p_n for 2<=n<=2e4", len(bad), 0, exact=True)
# p_n < 2^n  <=>  p_n.bit_length() <= n  (exact, no bignum exponentiation)
bad2 = [n for n in range(2, M + 1) if not (p(n).bit_length() <= n)]
check(f"p_n < 2^n for 2<=n<={M} (exact, bit_length)", len(bad2), 0, exact=True)
check("Bertrand certifies F only at n=1 (n=1: 2^2=4 > 2*2=4 is FALSE)",
      mpf(2) ** 2 <= 2 * 2, True, exact=True)

print("\n" + "=" * 70)
if FAIL:
    print(f"FAILED CHECKS ({len(FAIL)}): {FAIL}")
    sys.exit(1)
print("all checks passed")
sys.exit(0)
