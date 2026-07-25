#!/usr/bin/env python3
"""
probe_rh.py — in-run verification for proof-attempt-1 (target #1, 'RH-conditional-bound').

Leg: proof-attempt__1, molecule task-20260725-5fcc, run germ-20260725-791a7c45.

Everything here is arithmetic on the primes below a sieve limit, done at 60 decimal
digits with mpmath so that no claim in the write-up rests on float rounding.

Objects (notation of concept-cards D2/D5, 1-indexed, p_1 = 2):
    L_n = ln p_n
    g_n = p_{n+1} - p_n
    T_n = p_n * (p_n^(1/n) - 1)                      Firoozbakht threshold (D5)
    B_n = (22/25) * sqrt(p_n) * ln p_n               CMS RH-conditional envelope
                                                     (Carneiro-Milinovich-Soundararajan, via
                                                     arXiv:1708.04122v2 §1.2; restated as
                                                     arXiv:1804.02500v3 Thm 1; valid n>=3, p_n>=5)

Claims checked:
  C1  sqrt(x) > (25/22) ln x for all x > 0            [=> B_n > L_n^2 for every prime]
  C2  {n : T_n >= L_n^2} = {1..7, 10}                 [card L13, re-verified here]
  C3  S := {n >= 3 : B_n < T_n} = {3}                 [the sharp statement of Theorem A;
                                                       the write-up states S with `<=` -- both
                                                       give {3}, every comparison being strict]
  C4  B_n / T_n is unbounded; report its value at the sieve edge and at p = 2^64
  C5  no violation of F in the sieved range (sanity)
"""

import sys
from mpmath import mp, mpf, log, sqrt, exp, lambertw

mp.dps = 60

LIMIT = 3_000_000
C_CMS = mpf(22) / 25


def sieve(limit):
    bs = bytearray([1]) * (limit + 1)
    bs[0] = bs[1] = 0
    i = 2
    while i * i <= limit:
        if bs[i]:
            bs[i * i:: i] = bytearray(len(bs[i * i:: i]))
        i += 1
    return [i for i in range(limit + 1) if bs[i]]


def T(p, n):
    """T_n = p*(p^(1/n) - 1), computed as p*(exp(ln p / n) - 1)."""
    return p * (exp(log(p) / n) - 1)


def B(p):
    """CMS RH-conditional envelope (22/25) sqrt(p) ln p."""
    return C_CMS * sqrt(p) * log(p)


def main():
    print(f"mpmath dps = {mp.dps}, sieve limit = {LIMIT}")
    primes = sieve(LIMIT)
    print(f"primes = {len(primes)}, largest = {primes[-1]}")

    # ---- C1: minimum of h(x) = sqrt(x) - (25/22) ln x -------------------------
    k = mpf(25) / 22
    # h'(x) = 1/(2 sqrt x) - k/x = 0  <=>  sqrt(x) = 2k
    x_star = (2 * k) ** 2
    h_star = sqrt(x_star) - k * log(x_star)
    print("\n[C1] h(x) = sqrt(x) - (25/22) ln x")
    print(f"     stationary point x* = {mp.nstr(x_star, 12)}")
    print(f"     h(x*)              = {mp.nstr(h_star, 12)}   (must be > 0)")
    print(f"     verdict: {'PASS' if h_star > 0 else 'FAIL'}")

    # ---- C2 / C3 / C5 ---------------------------------------------------------
    exc_L2 = []          # n with T_n >= L_n^2
    S = []               # n >= 3 with B_n < T_n
    viol = []            # n with g_n >= T_n  (a counterexample to F)
    min_ratio_after = None
    argmin_after = None

    N = len(primes) - 1  # number of consecutive pairs
    for i in range(N):
        n = i + 1
        p = mpf(primes[i])
        g = primes[i + 1] - primes[i]
        Ln = log(p)
        Tn = T(p, n)
        if Tn >= Ln ** 2:
            exc_L2.append(n)
        if g >= Tn:
            viol.append((n, primes[i], g, Tn))
        if n >= 3:
            Bn = B(p)
            if Bn < Tn:
                S.append((n, primes[i], mp.nstr(Bn, 10), mp.nstr(Tn, 10)))
            else:
                r = Bn / Tn
                if n >= 4 and (min_ratio_after is None or r < min_ratio_after):
                    min_ratio_after = r
                    argmin_after = (n, primes[i])

    print("\n[C2] {n : T_n >= L_n^2} within sieve range")
    print(f"     = {exc_L2}")
    print(f"     expected {{1,...,7,10}} -> "
          f"{'PASS' if exc_L2 == [1, 2, 3, 4, 5, 6, 7, 10] else 'FAIL'}")

    print("\n[C3] S = {n >= 3 : B_n < T_n}  (indices the RH bound certifies)")
    for row in S:
        print(f"     n={row[0]:>3}  p={row[1]:>3}  B_n={row[2]}  T_n={row[3]}")
    print(f"     |S| = {len(S)}  -> {'PASS (S = {3})' if [r[0] for r in S] == [3] else 'FAIL'}")

    # explicit table over the small indices, incl. the L13 exception set
    print("\n[C3-table] small-index detail (n=3..12)")
    print("      n     p_n         T_n            B_n         B_n<T_n ?")
    for i in range(2, 12):
        n = i + 1
        p = mpf(primes[i])
        print(f"    {n:>3}  {primes[i]:>6}   {mp.nstr(T(p, n), 10):>14}  "
              f"{mp.nstr(B(p), 10):>13}   {B(p) < T(p, n)}")

    print("\n[C4] min over n>=4 of B_n/T_n inside the sieve")
    print(f"     min = {mp.nstr(min_ratio_after, 10)} at n={argmin_after[0]}, p={argmin_after[1]}")
    # sieve edge
    n_edge = N
    p_edge = mpf(primes[N - 1])
    print(f"     at the sieve edge n={n_edge}, p={primes[N-1]}: "
          f"B/T = {mp.nstr(B(p_edge) / T(p_edge, n_edge), 10)}")

    # at p = 2^64 (the verified frontier, card L6) -- index taken from PNT,
    # only used for the ratio, which is insensitive to n at that size
    p64 = mpf(2) ** 64
    L64 = log(p64)
    T64 = L64 ** 2 - L64 - 1          # asymptotic form (card L2); exact n unknown
    B64 = B(p64)
    print(f"\n     at p = 2^64: L = {mp.nstr(L64, 10)}")
    print(f"       T ~ L^2-L-1     = {mp.nstr(T64, 10)}")
    print(f"       B = (22/25)*sqrt(p)*L = {mp.nstr(B64, 10)}")
    print(f"       overshoot B/T   = {mp.nstr(B64 / T64, 10)}  "
          f"(~10^{mp.nstr(log(B64/T64)/log(10), 6)})")

    print("\n[C5] violations of F in the sieved range")
    print(f"     {len(viol)} found -> {'PASS (none)' if not viol else 'FAIL'}")

    # ---- C6: for which C is C*sqrt(p)*log(p) ever below L^2? ------------------
    # C sqrt(x) ln x < (ln x)^2  <=>  C < ln(x)/sqrt(x).
    # max_{x>0} ln(x)/sqrt(x) is attained at x = e^2 with value 2/e.
    crit = 2 / exp(1)
    print("\n[C6] generic envelope C*sqrt(p)*ln p vs L^2")
    print(f"     max_x ln(x)/sqrt(x) = 2/e = {mp.nstr(crit, 12)} at x = e^2 = "
          f"{mp.nstr(exp(2), 10)}")
    print(f"     CMS constant 22/25 = {mp.nstr(C_CMS, 12)}  -> "
          f"{'ABOVE critical: envelope > L^2 everywhere' if C_CMS > crit else 'below critical'}")
    for C in ['0.88', '0.7357', '0.5', '0.1', '0.01']:
        Cm = mpf(C)
        if Cm >= crit:
            print(f"     C={C:>7}: {{p : C*sqrt(p)*ln p < L^2}} is EMPTY")
            continue
        # C sqrt(x) = ln x  <=>  x = exp(-2 W(-C/2)), the two real branches of W
        lo = exp(-2 * lambertw(-Cm / 2, 0))
        hi = exp(-2 * lambertw(-Cm / 2, -1))
        print(f"     C={C:>7}: nonempty only on p in "
              f"({mp.nstr(lo.real, 10)}, {mp.nstr(hi.real, 10)}) -- a bounded interval")

    # ---- C7: the Theorem-E counter-model --------------------------------------
    # q_n := p_n + sum_{k : n_k < n} J_k, where
    #   n_k := least n >= 2^(2^k) with g_n <= 2 ln p_n      (NOT 2^(2^k) itself)
    #   J_k := ceil((ln q_{n_k})^2) - g_{n_k}               (a TOP-UP, not the whole gap)
    # so that the gap at n_k becomes exactly ceil((ln q_{n_k})^2).
    # Claim: q is strictly increasing, agrees with p to within O(log^2 n loglog n),
    # has limsup (q_{n+1}-q_n)/(ln q_n)^2 = 1, and violates Firoozbakht at every large n_k.
    # NOTE: the loop below can only reach three usable n_k (16, 256, 65536) -- 2^(2^5)
    # exceeds the sieve.  The INFINITARY claim is analytic (Claim 4), not computational.
    print("\n[C7] Theorem-E counter-model  q_n = p_n + step")
    # n_k := least n >= 2^(2^k) with g_n <= 2 ln p_n  (such n exist infinitely often;
    # see Lemma E.1 in the write-up).  J_k tops the gap up to exactly ceil((ln q)^2).
    n_ks = []
    k = 1
    while True:
        start = 2 ** (2 ** k)
        if start >= N:
            break
        nk = start
        while nk < N and (primes[nk] - primes[nk - 1]) > 2 * log(primes[nk - 1]):
            nk += 1
        n_ks.append(nk)
        k += 1
    print(f"     insertion indices n_k below the sieve edge: {n_ks}")

    offset = 0
    rows = []
    for nk in n_ks:
        q_nk = mpf(primes[nk - 1]) + offset            # 1-indexed: p_{n_k} = primes[nk-1]
        Lq = log(q_nk)
        gap_p = primes[nk] - primes[nk - 1]
        J = int(mp.ceil(Lq ** 2)) - gap_p              # top-up, >= 0 for k large
        gap_q = gap_p + J                              # == ceil((ln q_{n_k})^2)
        Tq = T(q_nk, nk)
        rows.append((nk, int(q_nk), J, gap_q, Tq, Lq ** 2, gap_q >= Tq))
        offset += J

    print("       n_k        q_{n_k}      J_k    gap_q      T^q_{n_k}     (ln q)^2   violates F?")
    for (nk, q, J, gq, Tq, L2, ok) in rows:
        print(f"    {nk:>7}  {q:>12}  {J:>7}  {gq:>7}   {mp.nstr(Tq, 8):>11}  "
              f"{mp.nstr(L2, 8):>10}   {ok}")
    # n_k <= 10 lies in the L13 exception set {1..7,10} where T_n >= L_n^2, so the
    # argument (which needs T_n < L_n^2) applies only from n_k >= 11 on -- exactly the
    # "for all sufficiently large k" of Theorem E.
    big = [r for r in rows if r[0] >= 11]
    print(f"     all n_k >= 11 violate F -> "
          f"{'PASS' if big and all(r[6] for r in big) else 'FAIL'}"
          f"   (n_k <= 10 excluded: L13 exception set)")
    print(f"     total drift q_n - p_n at the sieve edge = {offset} "
          f"(vs p = {primes[N-1]}, relative {offset/primes[N-1]:.3e})")
    # limsup check: gap_q/(ln q)^2 at the n_k, and the max elsewhere
    print("     (q_{n+1}-q_n)/(ln q_n)^2 at the n_k: "
          + ", ".join(mp.nstr(mpf(r[3]) / r[5], 6) for r in rows))


if __name__ == '__main__':
    sys.exit(main())
