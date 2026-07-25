"""
fb_core — computational substrate for notebook-2 (target: `unconditional-verified-range`).

Scope
-----
Firoozbakht's conjecture (`F`):   p_{n+1}^{1/(n+1)} < p_n^{1/n}   for all n >= 1.

Epistemic status of everything in this module: **computation**. Nothing here
proves `F`. Two things it *can* do rigorously:

1. decide `F` at a given index `n`, exactly, by an integer comparison;
2. evaluate an *unconditional* sufficient condition (Lemma A below) whose only
   external input is Dusart's explicit bound on `pi(x)`.

Naming follows the run's concept cards:
    D5   T_n := p_n * (p_n^{1/n} - 1)          the exact bar
    D6   rho_n := g_n / T_n ;  F fails at n  <=>  rho_n >= 1   (exact, no error term)
    D7   c_n := g_n / log^2 p_n                 the CSG surrogate (sufficient, not necessary)
    T1   Dusart 2010 Thm 6.9 eq. (6.6): pi(x) <= x/(log x - 1.1) for x >= 60184
    T3   verification consumes an *upper* bound on the index; refutation a *lower* one.

Author: leg `notebooks__2`, molecule task-20260725-09a7, run germ-20260725-791a7c45.
"""

from __future__ import annotations

import math
import time
from decimal import Decimal, getcontext, localcontext

import numpy as np

# --------------------------------------------------------------------------
# 0.  The constant that the whole unconditional half rests on
# --------------------------------------------------------------------------

# Dusart (2010), "Estimates of some functions over primes without R.H.",
# arXiv:1002.0442, Theorem 6.9, eq. (6.6), upper half:
#         pi(x) <= x / (log x - 1.1)        for  x >= 60184.
# Ledger tier L0 (opened and read) per concept card T1. This module treats the
# *statement* as an input, not as something it verifies; it does verify every
# consequence it draws from it.
DUSART_C = Decimal("1.1")
DUSART_XMIN = 60184


# --------------------------------------------------------------------------
# 1.  Sieve
# --------------------------------------------------------------------------

def base_primes(limit: int) -> np.ndarray:
    """All primes <= limit, plain sieve of Eratosthenes."""
    s = np.ones(limit + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if s[i]:
            s[i * i:: i] = False
    return np.nonzero(s)[0].astype(np.int64)


def sieve_segments(N: int, seg: int = 10**7):
    """Yield int64 arrays of the primes in successive windows covering [2, N]."""
    bp = base_primes(int(N**0.5) + 1)
    lo = 2
    while lo <= N:
        hi = min(lo + seg, N + 1)
        mask = np.ones(hi - lo, dtype=bool)
        for p in bp:
            if p * p >= hi:
                break
            start = max(p * p, ((lo + p - 1) // p) * p)
            mask[start - lo:: p] = False
        yield np.nonzero(mask)[0].astype(np.int64) + lo
        lo = hi


# --------------------------------------------------------------------------
# 2.  The bulk scan  (float64 — a *screen*, not a certificate)
# --------------------------------------------------------------------------

def scan(N: int, seg: int = 10**7, topk: int = 40, escalate: float = 0.90,
         nmin_stats: int = 10, verbose: bool = True) -> dict:
    """
    Sieve [2, N] and compute, for every consecutive prime pair below N:

        g_n   = p_{n+1} - p_n
        T_n   = p_n * expm1(log(p_n)/n)          (D5)
        rho_n = g_n / T_n                        (D6)

    Returns the statistics that matter, never the prime list (memory).

    Float64 is used deliberately and only as a *screen*: every pair with
    rho_n >= `escalate` is recorded for re-decision in exact/certified
    arithmetic (`certified_verdict`).  rho_n has O(1) operands, so it carries
    none of the 1/n cancellation that kills the "F2 margin" statistic
    (concept card T2, Rule 3) -- that statistic is computed here too, purely
    to exhibit the artefact.

    `nmin_stats` restricts the *summary* statistics (top-k rho, max c, max F2)
    to n >= nmin_stats, matching the convention of cards D6 / T2, which set it
    at 10 because rho_2 = 0.9107 and rho_4 = 0.9120 are small-index outliers
    that would otherwise dominate every table.  Violation and escalation
    detection is NEVER filtered: those run over every n >= 1.
    """
    t0 = time.time()
    n = 0
    prev = None
    first_occ: dict[int, tuple[int, int]] = {}   # gap -> (prime, index)
    records: list[tuple[int, int, int]] = []     # (n, p_n, g) maximal gaps
    rec = 0
    top: list[tuple[float, int, int, int]] = []  # (rho, n, p, g)
    escalations: list[tuple[int, int, int, float]] = []
    violations: list[tuple[int, int, int, float]] = []
    max_f2 = (0.0, 0, 0)
    max_c = (0.0, 0, 0, 0)
    lemmaA_min_slack = None   # min over p_n >= 60184 of  T_n - L(L-1.1)
    # P6' (card L15): T_{m(n)} <= T_n for m(n) the governing record index.
    cur_Tm = None
    p6_exceptions: list[tuple[int, float]] = []
    p6_min_slack = None

    for chunk in sieve_segments(N, seg):
        if prev is not None:
            arr = np.concatenate(([prev], chunk))
            n0 = n
        else:
            arr = chunk
            n0 = 0
        if len(arr) < 2:
            continue
        g = np.diff(arr)
        p = arr[:-1]
        idx = np.arange(n0 + 1, n0 + len(p) + 1, dtype=np.int64)
        pf = p.astype(np.float64)
        L = np.log(pf)
        T = pf * np.expm1(L / idx)
        rho = g / T

        for i in np.nonzero(rho >= escalate)[0]:
            escalations.append((int(idx[i]), int(p[i]), int(g[i]), float(rho[i])))
        for i in np.nonzero(rho >= 1.0)[0]:
            violations.append((int(idx[i]), int(p[i]), int(g[i]), float(rho[i])))

        stats = idx >= nmin_stats
        if stats.any():
            rho_s, idx_s, p_s, g_s, L_s = rho[stats], idx[stats], p[stats], g[stats], L[stats]
            k = min(topk, len(rho_s))
            part = np.argpartition(-rho_s, k - 1)[:k]
            top.extend((float(rho_s[i]), int(idx_s[i]), int(p_s[i]), int(g_s[i]))
                       for i in part)
            top.sort(reverse=True)
            del top[topk:]

            # D7 surrogate, for the L13 / D7 comparison
            c = g_s / (L_s * L_s)
            j = int(np.argmax(c))
            if c[j] > max_c[0]:
                max_c = (float(c[j]), int(idx_s[j]), int(p_s[j]), int(g_s[j]))

            # T2 Rule 2: the 1/n artefact, exhibited on purpose
            f2 = (idx_s * np.log((p_s + g_s).astype(np.float64))) / ((idx_s + 1) * L_s)
            j = int(np.argmax(f2))
            if f2[j] > max_f2[0]:
                max_f2 = (float(f2[j]), int(idx_s[j]), int(p_s[j]))

        for gg in np.unique(g):
            gg = int(gg)
            if gg not in first_occ:
                i = int(np.argmax(g == gg))
                first_occ[gg] = (int(p[i]), int(idx[i]))

        # Maximal-gap records, and P6' checked against them in one pass.
        # `prev_max[i]` is the largest gap strictly before position i (carrying
        # `rec` in from earlier segments); position i is a record iff it beats it.
        prev_max = np.maximum(rec, np.concatenate(([0], np.maximum.accumulate(g)[:-1])))
        rec_pos = np.nonzero(g > prev_max)[0]
        for i in rec_pos:
            rec = int(g[i])
            records.append((int(idx[i]), int(p[i]), rec))

        # Split the segment at the record positions; inside each piece the
        # governing record index -- and hence T_m -- is constant.
        bounds = list(rec_pos) + [len(g)]
        start = 0
        for b in bounds:
            if cur_Tm is not None and b > start:
                piece = T[start:b] - cur_Tm
                j = int(piece.argmin())
                m = float(piece[j])
                if p6_min_slack is None or m < p6_min_slack[0]:
                    p6_min_slack = (m, m / cur_Tm, int(idx[start + j]),
                                    int(p[start + j]), float(cur_Tm))
                for i in np.nonzero(piece < 0)[0]:
                    p6_exceptions.append((int(idx[start + i]), float(piece[i])))
            if b < len(g):
                cur_Tm = float(T[b])
                start = b + 1     # skip the record index itself (T_m - T_m = 0)

        # Lemma A slack, over the range where Dusart's bound is licensed
        sel = p >= DUSART_XMIN
        if sel.any():
            slack = T[sel] - L[sel] * (L[sel] - 1.1)
            m = float(slack.min())
            lemmaA_min_slack = m if lemmaA_min_slack is None else min(lemmaA_min_slack, m)

        n = n0 + len(p)
        prev = int(arr[-1])

    if verbose:
        print(f"N={N:,}  primes={n+1:,}  pairs={n:,}  {time.time()-t0:.1f}s")
    return dict(N=N, n_primes=n + 1, pairs=n, last_prime=prev,
                first_occ=first_occ, records=records, top=top,
                escalations=escalations, violations=violations,
                max_f2=max_f2, max_c=max_c,
                lemmaA_min_slack=lemmaA_min_slack,
                p6_exceptions=p6_exceptions[:200], p6_n_exceptions=len(p6_exceptions),
                p6_min_slack=p6_min_slack,
                seconds=time.time() - t0)


# --------------------------------------------------------------------------
# 3.  Exact and certified verdicts at a single index
# --------------------------------------------------------------------------

def exact_verdict(p_n: int, p_next: int, n: int) -> bool:
    """
    Decide `F` at index n by an *exact integer comparison*, no floating point:

        p_{n+1}^{1/(n+1)} < p_n^{1/n}   <=>   p_{n+1}^n < p_n^{n+1}

    (both sides positive integers; raise both to the power n(n+1)).
    Returns True iff `F` holds at n.  Cost is O(n * log p) digits -- usable
    only for modest n.
    """
    return p_next**n < p_n**(n + 1)


def certified_verdict(p_n: int, p_next: int, n: int, prec: int = 60) -> tuple[bool, Decimal]:
    """
    Decide `F` at index n in Decimal arithmetic with an explicit error budget.

        F holds at n  <=>  n*ln(p_{n+1}) < (n+1)*ln(p_n)

    CPython's `Decimal.ln()` is correctly rounded to the working precision, so
    each logarithm carries relative error <= 10^(1-prec).  We compare the
    margin against a slack `10^(3-prec) * max(|lhs|,|rhs|)`, three decades of
    head-room over that bound.  Returns (verdict, margin) and *raises* if the
    margin falls inside the slack -- an undecided case must never be silently
    reported as a pass (concept card T2, Rule 3: the silent failure direction
    is the verification direction).
    """
    with localcontext() as ctx:
        ctx.prec = prec
        N = Decimal(n)
        lhs = N * Decimal(p_next).ln()
        rhs = (N + 1) * Decimal(p_n).ln()
        margin = rhs - lhs
        slack = max(abs(lhs), abs(rhs)) * Decimal(10) ** (3 - prec)
        if abs(margin) <= slack:
            raise ArithmeticError(
                f"undecided at n={n}, p_n={p_n}: |margin|={margin} <= slack={slack}; "
                f"raise prec or fall back to exact_verdict")
        return margin > 0, margin


# --------------------------------------------------------------------------
# 4.  Lemma A — the unconditional safe bound
# --------------------------------------------------------------------------
#
#   Lemma A.  Let n be such that x := p_n >= 60184 and set L := log x.  Then
#
#                       T_n  >=  L * (L - 1.1).
#
#   Proof.  T_n = x*(e^{L/n} - 1) with n = pi(x) (card D3).  Dusart's bound
#   gives n <= x/(L - 1.1), hence L/n >= L(L-1.1)/x.  Since u |-> x*(e^u - 1)
#   is increasing and e^u - 1 >= u for all real u,
#           T_n >= x*(e^{L(L-1.1)/x} - 1) >= x * L(L-1.1)/x = L(L-1.1).   []
#
#   Corollary A1.  For p_n >= 60184, if g_n <= 108 then F holds at n.
#      (L(L-1.1) at x = 60184 is 109.007..., and L(L-1.1) increases in x.)
#
#   Corollary A2 (the safe bound).  A gap of size g can violate F only at a
#   prime p_n <= S(g), where S(g) := exp( (1.1 + sqrt(1.21 + 4g)) / 2 ) is the
#   root of L(L-1.1) = g -- valid as stated for p_n >= 60184; below that,
#   enumerate.
#
#   This is an in-run re-derivation of the *method* behind the published
#   verification (card L6): the published result checks first occurrences of
#   each gap size against a bound of exactly this shape.  Constants differ
#   because the published argument keeps more of the exponential.

def safe_bound_S(g: int, prec: int = 50) -> Decimal:
    """
    Rigorous UPPER bound on S(g) = exp((1.1 + sqrt(1.21 + 4g))/2).

    Rounded up deliberately: the downstream test is `P1(g) > S(g)`, so
    overstating S(g) can only make a reported "safe" verdict more conservative.
    """
    with localcontext() as ctx:
        ctx.prec = prec
        d = (Decimal("1.21") + 4 * Decimal(g)).sqrt()
        L = (DUSART_C + d) / 2
        S = L.exp()
        return S * (1 + Decimal(10) ** (5 - prec))   # inflate: round up


def gap_needed(p: int, prec: int = 50) -> Decimal:
    """
    L(L-1.1) at p -- the smallest gap that could possibly violate F at a prime
    of this size, per Lemma A.  Rounded DOWN (conservative in the same
    direction).  Valid for p >= 60184.
    """
    with localcontext() as ctx:
        ctx.prec = prec
        L = Decimal(p).ln()
        v = L * (L - DUSART_C)
        return v * (1 - Decimal(10) ** (5 - prec))


def lemma_A_certificate(first_occ: dict[int, tuple[int, int]], X: int) -> dict:
    """
    Given a *complete* first-occurrence table for every gap size occurring
    below X, decide whether Lemma A settles `F` on [60184, X].

    Returns per-gap rows and an overall verdict.  The verdict is:

        F holds at every n with 60184 <= p_n < X
            <==  for every even g occurring below X with S(g) >= 60184,
                 the first occurrence P1(g) satisfies P1(g) > S(g).

    Gaps with S(g) < 60184 need nothing: Lemma A already excludes them
    everywhere in range (Corollary A1 is the g <= 108 case of this).
    """
    rows = []
    unsettled = []
    for g in sorted(first_occ):
        P1 = first_occ[g][0]
        S = safe_bound_S(g)
        if S < DUSART_XMIN:
            rows.append(dict(g=g, P1=P1, S=S, status="excluded-by-range",
                             ratio=None))
            continue
        ok = Decimal(P1) > S
        rows.append(dict(g=g, P1=P1, S=S, status="safe" if ok else "UNSETTLED",
                         ratio=float(Decimal(P1) / S)))
        if not ok:
            unsettled.append(g)
    live = [r for r in rows if r["ratio"] is not None]
    return dict(rows=rows, unsettled=unsettled,
                n_live=len(live),
                min_ratio=min((r["ratio"] for r in live), default=None),
                min_ratio_gap=min(live, key=lambda r: r["ratio"])["g"] if live else None,
                verdict="SETTLED" if not unsettled else "NOT SETTLED",
                X=X)


def window_certificate(records: list[tuple[int, int, int]], X: int,
                       n_windows: int = 40) -> list[dict]:
    """
    The certificate that scales: split [60184, X] into geometric windows and
    check, per window [a, b), that the maximal gap inside is < L(L-1.1)
    evaluated at `a` (the worst point of the window).

    This is the form that needs only a *maximal-gap record table*, not a full
    sieve -- i.e. the shape in which the published frontier is actually
    certified.  `records` must be the complete list of maximal-gap records
    below X, as (index, prime, gap).
    """
    out = []
    lo = float(DUSART_XMIN)
    ratio = (X / lo) ** (1.0 / n_windows)
    while lo < X:
        hi = min(lo * ratio, float(X))
        # largest gap whose first occurrence is < hi  ==  max gap in [2, hi)
        gmax = max((g for (_, p, g) in records if p < hi), default=0)
        need = gap_needed(int(lo))
        out.append(dict(lo=int(lo), hi=int(hi), gmax=gmax, need=float(need),
                        ok=Decimal(gmax) < need))
        lo = hi
    return out


# --------------------------------------------------------------------------
# 5.  Convenience
# --------------------------------------------------------------------------

def rho(p_n: int, p_next: int, n: int) -> float:
    L = math.log(p_n)
    return (p_next - p_n) / (p_n * math.expm1(L / n))
