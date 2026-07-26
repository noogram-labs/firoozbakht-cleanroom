#!/usr/bin/env python3
"""
probe_rh2.py -- round-2 in-run verification for proof-attempt-RH-conditional-bound.

Leg: proof-attempt (RE-ATTACK round 2), molecule task-20260726-b335.

DISCIPLINE (faults.md sec.6 item 2): every check below is written from the STATEMENT it
tests, not from round 1's derivation or round 1's code (`attack/proof-attempt-1/probe_rh.py`
was NOT read as a source for any formula here).  A check written from a derivation cannot
catch an error in that derivation.

Notation (concept-cards D1/D2/D5, 1-indexed, p_1 = 2):
    L_n = ln p_n
    g_n = p_{n+1} - p_n
    T_n = p_n * (p_n^(1/n) - 1)
    B_n = (22/25) * sqrt(p_n) * ln p_n          (CMS envelope; hypothesis p_n > 3, i.e. n >= 3)

Checks:
  R1  min_x ( sqrt(x) - (25/22) ln x ) > 0
  R2  { n : T_n >= L_n^2 }                                    (card L13 exception set)
  R3  the full low table n = 1..10 of B_n, T_n                (F4: n=1,2 rows are the fix)
  R4  S_all := { n >= 1 : B_n < T_n }  and  S_3 := { n >= 3 : B_n < T_n }
  R5  min_{n>=4} B_n/T_n ; B/T at the sieve edge ; B/T at 2^64
  R6  max_x ln x / sqrt(x) = 2/e ; the C-table endpoints and prime counts
  R7  notebook-1 F2 reconciliation: p*(C) under the reading 2 <= p <= P
  R8  F8: the Visser-unconditional shortfall against 2^64, in primes
  R9  F9: Dusart eq.(6.6) bracket width vs the counter-model's pi-displacement
  R10 Theorem E counter-model rows, recomputed from the construction's statement
  R11 sanity: violations of F in the sieved range (must be 0; evidence about nothing)
"""

import sys
from mpmath import mp, mpf, log, sqrt, exp, lambertw, e

mp.dps = 50
N = 3_000_000


def sieve(n):
    bs = bytearray([1]) * (n + 1)
    bs[0] = bs[1] = 0
    i = 2
    while i * i <= n:
        if bs[i]:
            bs[i * i:: i] = bytearray(len(bs[i * i:: i]))
        i += 1
    return [i for i in range(n + 1) if bs[i]]


P = sieve(N)
print(f"sieve limit {N}: {len(P)} primes, largest {P[-1]}, {len(P)-1} consecutive pairs")


def T(p, n):          # p_n * (p_n^(1/n) - 1)
    p = mpf(p)
    return p * (exp(log(p) / n) - 1)


def B(p):             # (22/25) sqrt(p) ln p
    p = mpf(p)
    return mpf(22) / 25 * sqrt(p) * log(p)


# precompute L_n and T_n once (the multi-pass version was too slow to iterate on)
LL = [log(mpf(p)) for p in P]
TT = [mpf(p) * (exp(LL[i] / (i + 1)) - 1) for i, p in enumerate(P)]
BB = [mpf(22) / 25 * sqrt(mpf(p)) * LL[i] for i, p in enumerate(P)]

out = []
w = out.append

# ---------- R1 ----------------------------------------------------------------
k = mpf(25) / 22
xstar = (2 * k) ** 2
hstar = sqrt(xstar) - k * log(xstar)
w(f"[R1] x* = {xstar}  h(x*) = sqrt(x*)-(25/22)ln x* = {hstar}   >0 : {hstar > 0}")

# ---------- R2 ----------------------------------------------------------------
exc = [n for n in range(1, len(P) + 1) if TT[n - 1] >= LL[n - 1] ** 2]
w(f"[R2] {{n : T_n >= L_n^2}} in sieve = {exc}")

# ---------- R3 / R4 -----------------------------------------------------------
w("[R3] n, p_n, T_n, B_n, B_n<T_n")
for n in range(1, 11):
    p = P[n - 1]
    w(f"      {n:2d} {p:4d}  T={mp.nstr(TT[n-1],11)}  B={mp.nstr(BB[n-1],11)}  "
      f"B<T: {BB[n-1] < TT[n-1]}")

S_all = [n for n in range(1, len(P) + 1) if BB[n - 1] < TT[n - 1]]
S_3 = [n for n in S_all if n >= 3]
S_le = [n for n in range(1, len(P) + 1) if BB[n - 1] <= TT[n - 1]]
w(f"[R4] S_all = {{n>=1 : B_n <  T_n}} = {S_all}")
w(f"[R4] S_3   = {{n>=3 : B_n <  T_n}} = {S_3}")
w(f"[R4] with <= instead of < : {S_le}   (identical => all comparisons strict)")

# ---------- R5 ----------------------------------------------------------------
best, bestn = None, None
for n in range(4, len(P) + 1):
    r = BB[n - 1] / TT[n - 1]
    if best is None or r < best:
        best, bestn = r, n
w(f"[R5] min_{{n>=4}} B_n/T_n = {best} at n={bestn}, p={P[bestn-1]}")
ne = len(P)
w(f"[R5] B/T at sieve edge n={ne}, p={P[-1]}: {BB[-1]/TT[-1]}")
p64 = mpf(2) ** 64
L64 = log(p64)
w(f"[R5] B/T at p=2^64 with T ~ L^2-L-1 surrogate (card L2): "
  f"{B(p64)/(L64**2 - L64 - 1)}")

# ---------- R6 ----------------------------------------------------------------
w(f"[R6] max_x ln x/sqrt(x) = {log(exp(2))/sqrt(exp(2))} at x=e^2={exp(2)} ; 2/e={2/e}")
import bisect
for C in [mpf(22)/25, mpf(21)/25, mpf(1)/2, mpf('0.1'), mpf('0.01')]:
    arg = -C / 2
    if arg < -1 / e:
        w(f"[R6] C={C}: no real branch -> empty")
        continue
    xm = exp(-2 * lambertw(arg, 0))
    xp = exp(-2 * lambertw(arg, -1))
    cnt = bisect.bisect_right(P, float(xp)) - bisect.bisect_left(P, float(xm))
    w(f"[R6] C={C}: x in ({xm}, {xp}) -> {cnt} primes below sieve limit")

# ---------- R7 : notebook-1 reconciliation -----------------------------------
w("[R7] p*(C) = largest P such that B_C(p) < T(p) for ALL primes 2 <= p <= P "
  "(notebook-1 F2, read with the corrected lower endpoint -- faults.md F6)")
for name, C in [("1", mpf(1)), ("22/25", mpf(22)/25), ("4/pi", 4/mp.pi),
                ("1/(8pi)", 1/(8*mp.pi)), ("1e-2", mpf('0.01'))]:
    star = None
    for n in range(1, len(P) + 1):
        p = P[n - 1]
        if C * sqrt(mpf(p)) * LL[n - 1] < TT[n - 1]:
            star = p
        else:
            break
    ncert = 0 if star is None else bisect.bisect_right(P, star)
    w(f"      C={name:8s} p*(C)={star}   ({ncert} certified primes, i.e. indices 1..{ncert})")

# ---------- R8 : F8 -----------------------------------------------------------
uncond = mpf('1.836e19')
w(f"[R8] 2^64 = {p64}; Visser sec.7 unconditional range {uncond}; "
  f"shortfall {p64-uncond} = {(p64-uncond)/p64*100}% ; "
  f"~{(p64-uncond)/log(p64)} primes in the shortfall window")

# ---------- R9 : F9 -----------------------------------------------------------
for x in [mpf('1e6'), mpf('1e12'), p64]:
    Lx = log(x)
    w65 = mpf('0.2762') * x / Lx**2
    w66 = x / (Lx - mpf('1.1')) - x / (Lx - 1)
    drift = Lx * log(Lx)
    w(f"[R9] x={mp.nstr(x,4)}: Dusart(6.5) width~{mp.nstr(w65,6)}  "
      f"(6.6) width={mp.nstr(w66,6)}  log x*loglog x={mp.nstr(drift,6)}  "
      f"ratio (6.6)/drift={mp.nstr(w66/drift,6)}")

# ---------- R10 : Theorem E counter-model ------------------------------------
# statement-level reconstruction: n_k := least n >= 2^(2^k) with g_n <= 2 L_n;
# J_k := ceil( (ln q_{n_k})^2 ) - g_{n_k};  q_n := p_n + sum_{k : n_k < n} J_k.
w("[R10] counter-model rows (n_k, q, J_k, gap, T^{(q)}, (ln q)^2, violates F?)")
shift = 0
rows = []
for kk in range(0, 6):
    start = 2 ** (2 ** kk)
    if start > len(P):
        break
    nk = None
    for n in range(start, len(P)):
        p, pn1 = P[n - 1], P[n]
        if pn1 - p <= 2 * log(mpf(p)):
            nk = n
            break
    if nk is None:
        break
    q = P[nk - 1] + shift
    g = P[nk] - P[nk - 1]
    lq2 = log(mpf(q)) ** 2
    J = int(mp.ceil(lq2)) - g
    Tq = T(q, nk)
    rows.append((nk, q, J, g + J, Tq, lq2, (g + J) >= Tq))
    shift += J
for r in rows:
    w(f"      n_k={r[0]:7d} q={r[1]:9d} J={r[2]:5d} gap={r[3]:5d} "
      f"T^q={mp.nstr(r[4],9)} (ln q)^2={mp.nstr(r[5],9)} violates={r[6]}")
w(f"[R10] total drift q_n - p_n at sieve edge = {shift}")

# ---------- R11 ---------------------------------------------------------------
rho = sorted(range(1, len(P)), key=lambda n: -float((mpf(P[n]) - P[n - 1]) / TT[n - 1]))[:40]
idx = sorted(set(list(range(1, 10001)) + rho))
bad = [n for n in idx if pow(P[n], n) >= pow(P[n - 1], n + 1)]
w(f"[R11] exact-integer violations of p_{{n+1}}^n < p_n^{{n+1}} over n<=10000 plus the "
  f"40 largest-rho indices ({len(idx)} indices): {len(bad)}")

print("\n".join(out))
