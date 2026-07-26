"""Round-2 verification for the subquestion `unconditional-verified-range`.

Molecule reattack-20260726-57d1 / leg proof-attempt (round 2), worker
task-20260726-2035.

DISCIPLINE (this is the point of the file).  Every routine below is written from
the *statement* it checks, never from the derivation that produced the statement.
That is the exact discipline whose absence let `proof-attempt-0.md` §9 item 15
reproduce the F2 error instead of catching it: a check written from the
derivation cannot falsify the derivation.

Concretely: `required_d_*` never evaluates a sufficient condition.  It goes back
to Lemma W's hypothesis  C(p_m) <= A(p_{n0})  and solves for the separation
d = L_{n0} - L_m at which it first holds, with p_m = e^l.  The sufficient
conditions (`sufficient_d_*`) are evaluated separately and are only ever
*compared* against the solved requirement.

Run:  python3 verify-uvr-round2.py
"""

import math

from mpmath import mp, mpf, exp, log, sqrt, findroot

mp.dps = 50

# --- validity ranges, copied from the source statements (T1 / ledger) ---------
X0 = mpf(60184)             # Dusart Thm 6.9 eq. (6.6) upper bound  pi(x) <= x/(log x - 1.1)
X_DHIGH = mpf(5393)         # Dusart Thm 6.9 eq. (6.6) lower bound  pi(x) >= x/(log x - 1)
X_AHIGH = mpf(1772201)      # Axler Cor. 3.6
X_ALOW = mpf(2634800823)    # Axler Cor. 3.5
L0 = log(X0)
L1 = log(X_AHIGH)


def v_ax(l):
    """v := l^2 - l - 1 - 1/l   (the Axler-side coefficient)."""
    return l * l - l - 1 - 1 / l


def v_du(l):
    """v := l^2 - l         (the Dusart-side coefficient)."""
    return l * l - l


# --- the three candidate upper bars C(p_m) on T_m ----------------------------
def C_ahigh_printed(l):
    """(A-high) EXACTLY AS PRINTED in proof-attempt-0.md 6.1:  v (1 + l^4/x)."""
    return v_ax(l) * (1 + l ** 4 / exp(l))


def C_ahigh_repaired(l):
    """(A-high*) REPAIRED:  v (1 + v/x)."""
    return v_ax(l) * (1 + v_ax(l) / exp(l))


def C_dhigh(l):
    """(D-high):  (l^2-l)(1 + (l^2-l)/x).  Unchanged by the repair."""
    return v_du(l) * (1 + v_du(l) / exp(l))


# --- the two candidate lower bars A(p_{n0}) on T_{n0} ------------------------
def lam_from_alow(C):
    """least lam with lam^2 - lam - 1.17 >= C   ((A-low), Axler)."""
    return (1 + sqrt(1 + 4 * (C + mpf("1.17")))) / 2


def lam_from_dlow(C):
    """least lam with lam^2 - 1.1 lam >= C     ((D-low), Dusart)."""
    return (mpf("1.1") + sqrt(mpf("1.21") + 4 * C)) / 2


# --- REQUIRED separation: solved from Lemma W's hypothesis, not from a formula
def required_d_b_printed(l):
    return lam_from_alow(C_ahigh_printed(l)) - l


def required_d_b_repaired(l):
    return lam_from_alow(C_ahigh_repaired(l)) - l


def required_d_a(l):
    return lam_from_dlow(C_dhigh(l)) - l


# --- SUFFICIENT conditions displayed in the documents ------------------------
def sufficient_d_b_printed(l):
    """PA-0 6.2 as displayed:  d >= (0.17 - 1/l + l^4/p_m)/(2l-1)."""
    return (mpf("0.17") - 1 / l + l ** 4 * exp(-l)) / (2 * l - 1)


def sufficient_d_b_repaired(l):
    """REPAIRED 6.2:  d >= (0.17 - 1/l + v^2/p_m)/(2l-1)."""
    return (mpf("0.17") - 1 / l + v_ax(l) ** 2 * exp(-l)) / (2 * l - 1)


def phi(l):
    """The closed-form majorant of the repaired sufficient d*:
       phi(l) := (0.17 + E(l1) - 1/l)/(2l-1),  E(l) := v(l)^2 e^{-l}."""
    E1 = v_ax(L1) ** 2 * exp(-L1)
    return (mpf("0.17") + E1 - 1 / l) / (2 * l - 1)


def sweep(f, lo, hi, n):
    best, arg = None, None
    for i in range(n + 1):
        l = lo + (hi - lo) * mpf(i) / n
        y = f(l)
        if best is None or y > best:
            best, arg = y, l
    return best, arg


# ---------------------------------------------------------------- primes -----
def primes_upto(n):
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
    return [i for i in range(n + 1) if sieve[i]]


def max_gap_below(limit, seg=1 << 24):
    """Largest g = p_{k+1} - p_k with p_k < limit, by segmented sieve (numpy)."""
    import numpy as np

    base = [int(p) for p in primes_upto(int(limit ** 0.5) + 1000)]
    best, best_p, prev = 0, 0, 2
    lo = 3
    stop = False
    while not stop:
        hi = lo + seg
        s = np.ones(seg, dtype=bool)
        s[(1 if lo % 2 else 0)::2] = False        # kill even numbers
        for p in base:
            if p == 2 or p * p >= hi:
                continue
            start = max(p * p, ((lo + p - 1) // p) * p)
            if start % 2 == 0:
                start += p                        # odd multiples only
            if start < hi:
                s[start - lo:: 2 * p] = False
        idx = np.flatnonzero(s)
        if idx.size:
            qs = idx + lo
            allq = np.concatenate(([prev], qs))
            gaps = np.diff(allq)
            starts = allq[:-1]
            mask = starts < limit
            if mask.any():
                j = int(np.argmax(gaps[mask]))
                gm = int(gaps[mask][j])
                if gm > best:
                    best, best_p = gm, int(starts[mask][j])
            prev = int(qs[-1])
            if prev >= limit:
                stop = True
        lo = hi
    return best, best_p


# ================================================================== report ===
def main():
    print("=" * 78)
    print("PART 1 — the F2 repair:  (A-high) as printed vs (A-high*) repaired")
    print("=" * 78)
    print("l1 = log 1772201 = %s" % mp.nstr(L1, 10))
    print("v(l1) = %s ,  v(l1)^2/p_m = %s ,  l1^4/p_m = %s"
          % (mp.nstr(v_ax(L1), 10),
             mp.nstr(v_ax(L1) ** 2 * exp(-L1), 10),
             mp.nstr(L1 ** 4 * exp(-L1), 10)))
    print("  -> the printed factor is larger by  l1^4/v(l1)^2 = %s"
          % mp.nstr(L1 ** 4 / v_ax(L1) ** 2, 8))

    print("\nrequired separation d (solved from Lemma W's hypothesis):")
    print("  %-12s %-16s %-16s %-16s" % ("l", "p_m", "d, AS PRINTED", "d, REPAIRED"))
    for l in [L1, mpf(16), mpf(18), mpf(20), mpf("44.36"), mpf(100)]:
        print("  %-12s %-16s %-16s %-16s"
              % (mp.nstr(l, 7), mp.nstr(exp(l), 6),
                 mp.nstr(required_d_b_printed(l), 6),
                 mp.nstr(required_d_b_repaired(l), 6)))

    m_p, a_p = sweep(required_d_b_printed, L1, mpf(300), 20000)
    m_r, a_r = sweep(required_d_b_repaired, L1, mpf(300), 20000)
    s_r, b_r = sweep(sufficient_d_b_repaired, L1, mpf(300), 20000)
    s_p, b_p = sweep(sufficient_d_b_printed, L1, mpf(300), 20000)
    print("\n  max required d, AS PRINTED  = %s at l = %s   (<= 0.004479? %s)"
          % (mp.nstr(m_p, 8), mp.nstr(a_p, 8), m_p <= mpf("0.004479")))
    print("  max required d, REPAIRED    = %s at l = %s   (<= 0.004479? %s)"
          % (mp.nstr(m_r, 8), mp.nstr(a_r, 8), m_r <= mpf("0.004479")))
    print("  max PA-0 displayed criterion = %s at l = %s   (<= 0.004479? %s)"
          % (mp.nstr(s_p, 8), mp.nstr(b_p, 8), s_p <= mpf("0.004479")))
    print("  max REPAIRED criterion d*    = %s at l = %s   (<= 0.004479? %s)"
          % (mp.nstr(s_r, 8), mp.nstr(b_r, 8), s_r <= mpf("0.004479")))
    print("  factor by which the printed lemma inflates the requirement at l1: %s"
          % mp.nstr(required_d_b_printed(L1) / required_d_b_repaired(L1), 6))

    print("\n  closed-form majorant phi:")
    print("    phi(l1)      = %s" % mp.nstr(phi(L1), 10))
    print("    d*_rep(l1)   = %s   (equal by construction)" % mp.nstr(sufficient_d_b_repaired(L1), 10))
    mphi, aphi = sweep(phi, L1, mpf(4000), 40000)
    print("    max phi on [l1, 4000] = %s at l = %s" % (mp.nstr(mphi, 10), mp.nstr(aphi, 8)))
    print("    phi decreasing on the grid: %s"
          % all(phi(L1 + (mpf(4000) - L1) * mpf(i) / 4000) >
                phi(L1 + (mpf(4000) - L1) * mpf(i + 1) / 4000) for i in range(4000)))
    print("    monotonicity certificate  4/l - 1/l^2 < 0.381406  at l=l1: %s < %s -> %s"
          % (mp.nstr(4 / L1 - 1 / L1 ** 2, 8), "0.381406",
             (4 / L1 - 1 / L1 ** 2) < mpf("0.381406")))
    print("    E(l) = v^2 e^-l decreasing certificate  v - 2v' > 0 at l=l1: %s"
          % mp.nstr(v_ax(L1) - 2 * (2 * L1 - 1 + 1 / L1 ** 2), 8))

    print("\n  sweep-free branch (drop -1/l, bound E by E(l1)):")
    print("    repaired : 0.17/(2*l1-1)          = %s" % mp.nstr(mpf("0.17") / (2 * L1 - 1), 8))
    print("    PA-0     : (0.17+l1^4 e^-l1)/(2*l1-1) = %s"
          % mp.nstr((mpf("0.17") + L1 ** 4 * exp(-L1)) / (2 * L1 - 1), 8))

    print("\n  the three bars at l = l1 (p_m = 1 772 201), decomposed:")
    E1 = v_ax(L1) ** 2 * exp(-L1)
    print("    v                          = %s" % mp.nstr(v_ax(L1), 12))
    print("    v + v^2/x   (A-high*)      = %s" % mp.nstr(v_ax(L1) + E1, 12))
    print("    v + l^4/x   (honest weak.) = %s" % mp.nstr(v_ax(L1) + L1 ** 4 * exp(-L1), 12))
    print("    v(1 + l^4/x)  (as printed) = %s" % mp.nstr(C_ahigh_printed(L1), 12))
    print("    printed error term / corrected error term = %s"
          % mp.nstr((C_ahigh_printed(L1) - v_ax(L1)) / E1, 8))

    print("\n" + "=" * 78)
    print("PART 2 — what the printed lemma would have cost (closes F13)")
    print("=" * 78)
    # self-test of the segmented sieve against a plain sieve
    ref = primes_upto(3_000_000)
    bg, bp, prev = 0, 0, 2
    for q in ref[1:]:
        if prev < 2_000_000 and q - prev > bg:
            bg, bp = q - prev, prev
        prev = q
        if prev >= 2_000_000:
            break
    sg, sp = max_gap_below(2_000_000)
    print("  sieve self-test  max gap below 2e6: plain=(%d at %d) segmented=(%d at %d)  agree=%s"
          % (bg, bp, sg, sp, (bg, bp) == (sg, sp)))
    lx = findroot(lambda l: required_d_b_printed(l) - mpf("0.004479"), (L1, mpf(40)),
                  solver="anderson")
    print("  required_d_printed(l) = 0.004479 at l = %s, i.e. p_m = %s"
          % (mp.nstr(lx, 10), mp.nstr(exp(lx), 8)))
    lx2 = findroot(lambda l: sufficient_d_b_printed(l) - mpf("0.004479"), (L1, mpf(40)),
                   solver="anderson")
    print("  PA-0 displayed criterion = 0.004479 at l = %s, i.e. p_m = %s"
          % (mp.nstr(lx2, 10), mp.nstr(exp(lx2), 8)))
    lim = int(exp(lx)) + 1
    g132, p132 = max_gap_below(1772201)
    print("  max prime gap below 1 772 201            = %d at p = %d" % (g132, p132))
    gbig, pbig = max_gap_below(lim)
    print("  max prime gap below %d = %d at p = %d" % (lim, gbig, pbig))
    print("  (T_{n0} > 1919 must dominate it: 1919 > %d ? %s)" % (gbig, 1919 > gbig))

    print("\n" + "=" * 78)
    print("PART 3 — Theorem C(a) is untouched by the repair")
    print("=" * 78)
    ma, aa = sweep(required_d_a, L0, mpf(400), 20000)
    print("  max required d for C(a) = %s at l = %s  (PA-0 quotes 0.0623: covers? %s)"
          % (mp.nstr(ma, 8), mp.nstr(aa, 8), ma <= mpf("0.0623")))
    print("  (D-high) bar is v(1+v/x) with v = l^2-l  -> already tight, no l^4 anywhere")
    print("  epsilon(l0) = (l0^2-l0)^2 e^{-l0} = %s  (PA-0 quotes 0.20145)"
          % mp.nstr(v_du(L0) ** 2 * exp(-L0), 8))

    print("\n" + "=" * 78)
    print("PART 4 — the unconditional verified-range chain (Dusart only)")
    print("=" * 78)
    B = lambda p: log(p) ** 2 - mpf("1.1") * log(p)
    S = lambda g: exp((mpf("1.1") + sqrt(mpf("1.21") + 4 * g)) / 2)
    ps = primes_upto(2_000_000)
    # Lemma 3 slack, exact-integer base case, G0
    worst, worst_p = None, None
    for i, p in enumerate(ps[:-1]):
        if p < 60184:
            continue
        n = i + 1                      # 1-indexed
        L = log(p)
        T = mpf(p) * (exp(L / n) - 1)
        s = T - B(p)
        if worst is None or s < worst:
            worst, worst_p = s, p
    print("  Lemma 3  min (T_n - B(p_n)) on [60184, 2e6] = %s at p = %d"
          % (mp.nstr(worst, 8), worst_p))
    bad = 0
    G0, G0p = 0, 0
    for i, p in enumerate(ps[:-1]):
        q = ps[i + 1]
        n = i + 1
        if p < 60184:
            if q - p > G0:
                G0, G0p = q - p, p
            if not q ** n < p ** (n + 1):
                bad += 1
    print("  (H1) exact integer p_{n+1}^n < p_n^{n+1} for all p_n < 60184: violations = %d" % bad)
    print("  G0 = max gap below 60184 = %d at p = %d ;  B(60184) = %s"
          % (G0, G0p, mp.nstr(B(X0), 8)))
    print("  B monotone (dB/dL = 2L-1.1 > 0 for L > 0.55; e^0.55 = %s < 2)"
          % mp.nstr(exp(mpf("0.55")), 6))
    g = 2
    last = None
    while S(g) <= mpf(2) ** 64:
        last = g
        g += 2
    print("  largest even g with S(g) <= 2^64 : %d   (S(%d) = %s, S(%d) = %s, 2^64 = %s)"
          % (last, last, mp.nstr(S(last), 8), last + 2, mp.nstr(S(last + 2), 8),
             mp.nstr(mpf(2) ** 64, 8)))
    # Dusart pi(x) <= x/(log x - 1.1) at every prime in [60184, 2e6]
    fails = 0
    for i, p in enumerate(ps):
        if p >= 60184:
            if not (mpf(i + 1) <= mpf(p) / (log(p) - mpf("1.1"))):
                fails += 1
    print("  Lemma 2 (Dusart eq. 6.6 upper) at every prime in [60184, 2e6]: failures = %d" % fails)


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------- PART 5 -----
def part5():
    """Checks added by the step-2 verification pass, because §4.5/§4.7 of the
    artifact asserted them and PART 4 did not actually compute them."""
    print("\n" + "=" * 78)
    print("PART 5 — Reading (B) window, Kourbatov's bar, and pi(60184)")
    print("=" * 78)
    h = lambda p: p - 25 * log(p) ** 3 * (log(p) - mpf("1.1"))
    print("  h(396738)  = %s" % mp.nstr(h(mpf(396738)), 8))
    print("  h(777600)  = %s   h(777601) = %s"
          % (mp.nstr(h(mpf(777600)), 8), mp.nstr(h(mpf(777601)), 8)))
    pstar = findroot(h, (mpf(700000), mpf(900000)), solver="anderson")
    print("  sign change p* = %s" % mp.nstr(pstar, 10))
    dh = lambda p: 1 - (25 / p) * (4 * log(p) ** 3 - mpf("3.3") * log(p) ** 2)
    print("  min h' on a grid over [4e5, 1e7] = %s"
          % mp.nstr(min(dh(mpf(400000) + (mpf(10000000) - 400000) * mpf(i) / 2000)
                        for i in range(2001)), 8))
    # Kourbatov's sharper bar  S_K(p) = L^2 - L - 1.17
    SK = lambda g: exp((1 + sqrt(1 + 4 * (g + mpf("1.17")))) / 2)
    g, last = 2, None
    while SK(g) <= mpf(2) ** 64:
        last = g
        g += 2
    print("  largest even g with S_K(g) <= 2^64 (Kourbatov's bar) : %d  (S_K(%d)=%s, S_K(%d)=%s)"
          % (last, last, mp.nstr(SK(last), 8), last + 2, mp.nstr(SK(last + 2), 8)))
    ps = primes_upto(60184)
    print("  pi(60184) = %d   -> base-case indices n with p_n < 60184 : %d"
          % (len(ps), len([p for p in ps if p < 60184])))


part5()


# ---------------------------------------------------------------- PART 6 -----
def part6():
    """The FOUR bars that circulate in proof-attempt-0.md 6.1/6.2/9 under the
    single name (A-high).  Each 'required d' is solved from Lemma W's
    hypothesis, never from a sufficient condition."""
    print("\n" + "=" * 78)
    print("PART 6 — the four bars named (A-high), and what each one costs")
    print("=" * 78)
    bars = [
        ("0  v(1+v/x)      TIGHT (A-high*)", lambda l: v_ax(l) * (1 + v_ax(l) / exp(l))),
        ("1  v(1+l^2/x)    6.1's stated justification", lambda l: v_ax(l) * (1 + l ** 2 / exp(l))),
        ("2  v + l^4/x     additive weakening (= 6.2's criterion)", lambda l: v_ax(l) + l ** 4 * exp(-l)),
        ("3  v(1+l^4/x)    6.1 AS PRINTED", lambda l: v_ax(l) * (1 + l ** 4 / exp(l))),
    ]
    print("  %-52s %-14s %-14s %-8s" % ("bar", "err at l1", "max req d", "<=0.004479"))
    for name, C in bars:
        best, arg = sweep(lambda l: lam_from_alow(C(l)) - l, L1, mpf(300), 20000)
        print("  %-52s %-14s %-14s %-8s"
              % (name, mp.nstr(C(L1) - v_ax(L1), 9), mp.nstr(best, 9),
                 str(best <= mpf("0.004479"))))
    print("  (every max above is attained at l = l1 = %s)" % mp.nstr(L1, 10))


part6()


# ---------------------------------------------------------------- PART 7 -----
def part7():
    """Constants quoted in Corollary R1.1's proof (step-2 verification pass:
    the artifact cited them, so the committed script must produce them)."""
    print("\n" + "=" * 78)
    print("PART 7 — Corollary R1.1 constants")
    print("=" * 78)
    print("  psi(l1) = l1^5 e^-l1              = %s   (< 1 ? %s)"
          % (mp.nstr(L1 ** 5 * exp(-L1), 10), L1 ** 5 * exp(-L1) < 1))
    print("  true    l1*E(l1)                  = %s" % mp.nstr(L1 * v_ax(L1) ** 2 * exp(-L1), 10))
    print("  majorant cost psi(l1)/(l1 E(l1))  = %s"
          % mp.nstr(L1 ** 5 * exp(-L1) / (L1 * v_ax(L1) ** 2 * exp(-L1)), 6))
    print("  0.17/(2*l1-1)                     = %s" % mp.nstr(mpf("0.17") / (2 * L1 - 1), 10))
    print("  denominator of Axler Cor. 3.6 at l1: l1-1-1/l1-1/l1^2 = %s"
          % mp.nstr(L1 - 1 - 1 / L1 - 1 / L1 ** 2, 8))
    print("  lambda lower bound: log(2^64) = %s ; lam^2-1.1*lam = %s  (> 1919 ? %s)"
          % (mp.nstr(log(mpf(2) ** 64), 10),
             mp.nstr(log(mpf(2) ** 64) ** 2 - mpf("1.1") * log(mpf(2) ** 64), 10),
             log(mpf(2) ** 64) ** 2 - mpf("1.1") * log(mpf(2) ** 64) > 1919))
    for c in ["0.0043635677", "0.004479"]:
        print("  e^-%s = %s  -> sliver %s %%"
              % (c, mp.nstr(exp(-mpf(c)), 8), mp.nstr(100 * (1 - exp(-mpf(c))), 6)))


part7()
