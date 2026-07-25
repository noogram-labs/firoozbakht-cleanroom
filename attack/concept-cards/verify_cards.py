#!/usr/bin/env python3
"""Reproduce every in-run number quoted on the concept cards.

Leg: concept-cards, molecule task-20260725-068e, run germ-20260725-791a7c45.
Written by this leg; independent of attack/probe.py and attack/probe2.py.

Indexing is 1-based throughout: p(1) = 2.  Run:  python3 verify_cards.py
"""

import math

LIMIT = 3_000_000


def sieve(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i :: i] = bytearray(len(s[i * i :: i]))
    return [i for i in range(n + 1) if s[i]]


P = sieve(LIMIT)
M = len(P)


def p(n):
    """1-indexed n-th prime."""
    return P[n - 1]


def T(n):
    """The Firoozbakht threshold  T_n = p_n (p_n^(1/n) - 1).   [card D5]"""
    x = p(n)
    return x * math.expm1(math.log(x) / n)


def rho(n):
    """rho_n = g_n / T_n.  rho_n >= 1  iff  F fails at n.   [card D6]"""
    return (p(n + 1) - p(n)) / T(n)


def csg(n):
    """c_n = g_n / log^2 p_n.   [card D7]"""
    return (p(n + 1) - p(n)) / math.log(p(n)) ** 2


def main():
    out = []
    add = out.append
    add(f"primes <= {LIMIT}: {M}   largest: {P[-1]}")

    # --- D6 / T2 : violations and the rho record -------------------------
    viol = [n for n in range(1, M) if n * math.log(p(n + 1)) >= (n + 1) * math.log(p(n))]
    add(f"[D6] violations of F for 1 <= n <= {M-1}: {len(viol)}")

    top = sorted((rho(n), n, p(n)) for n in range(10, M))[-2:]
    for r, n, x in reversed(top):
        add(f"[D6] rho = {r:.7f} at n = {n}, p_n = {x}, g = {p(n+1)-x}")

    c, n, x = max((csg(n), n, p(n)) for n in range(10, M))
    add(f"[D7] max c_n (n>=10) = {c:.7f} at n = {n}, p_n = {x}")

    # --- D5 / L15 : T is not monotone, but the record-block test is clean -
    dec = sum(1 for n in range(10, M - 1) if T(n + 1) < T(n))
    tot = M - 11
    add(f"[D5] steps with T_(n+1) < T_n (n>=10): {dec} / {tot} = {100*dec/tot:.2f}%")

    recs, mx = [], 0
    for n in range(1, M):
        g = p(n + 1) - p(n)
        if g > mx:
            mx, _ = g, recs.append(n)
    add(f"[L15] record (maximal) gaps in range: {len(recs)}")

    import bisect

    bad = pairs = 0
    for n in range(1, M):
        i = bisect.bisect_right(recs, n) - 1
        if i < 0:
            continue
        pairs += 1
        if T(recs[i]) > T(n):
            bad += 1
    add(f"[L15] T_m > T_n for m = governing record index: {bad} exceptions in {pairs} pairs")

    # --- L13 : the exception set of  T_n < L_n^2 -------------------------
    exc = [n for n in range(1, 200) if T(n) >= math.log(p(n)) ** 2]
    add(f"[L13] {{n : T_n >= L_n^2}} = {exc}          p_109 = {p(109)}")

    # --- L2 : the asymptotic surrogate and its -3/L refinement -----------
    add("[L2] n / p_n / T_n / L^2-L-1 / L^2-L-1-3/L")
    for n in (10_000, 100_000, 216_815):
        x, L = p(n), math.log(p(n))
        add(f"     {n:>7} {x:>9} {T(n):10.4f} {L*L-L-1:10.4f} {L*L-L-1-3/L:10.4f}")

    # --- D5 : substitution error of the surrogate ------------------------
    add("[D5] substitution error  T_n/(L^2-L-1) - 1:")
    for x in (113, 1327, 2010733, 2999957):
        n = P.index(x) + 1
        L = math.log(x)
        add(f"     p = {x:>9}   {100*(T(n)/(L*L-L-1) - 1):+8.4f} %")

    # --- D5 : the T-increase rule's threshold is L-2, not L --------------
    add("[D5] misclassification of the T-increase rule, by threshold:")
    for th in (0, 1, 2, 3):
        bad = sum(
            1
            for n in range(10, M - 1)
            if (T(n + 1) > T(n)) != ((p(n + 1) - p(n)) > math.log(p(n)) - th)
        )
        add(f"     g > L-{th}:  {100*bad/(M-11):.3f} %")

    # --- L14 : where the smooth-model bracket changes sign ---------------
    f = lambda x: 1 + 1 / math.log(x) - math.log(x) - math.log(math.log(x))
    lo, hi = 4.0, 4.1
    for _ in range(80):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if f(m) > 0 else (lo, m)
    add(f"[L14] bracket sign change at x = {lo:.6f}   (f(4) = {f(4):+.5f}, f(5) = {f(5):+.5f})")

    # --- L7 : the all-primes record, in both units -----------------------
    Prec, grec = 1693182318746371, 1132
    L = math.log(Prec)
    c = grec / L ** 2
    r = c * L ** 2 / (L ** 2 - L - 1)
    add(f"[L7] p = {Prec}, g = {grec}, L = {L:.6f}")
    add(f"     c = {c:.8f}   ceiling 1-1/L = {1-1/L:.8f}   margin {100*(1-1/L-c)/(1-1/L):.3f} %")
    add(f"     rho = {r:.8f}  ceiling 1                 margin {100*(1-r):.3f} %")

    print("\n".join(out))


if __name__ == "__main__":
    main()
