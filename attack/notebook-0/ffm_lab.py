"""
ffm_lab -- computational laboratory for the Firoozbakht *first-failure-maximality* target.

Target under stress (attack/concept-cards/L15, decompose.md P6'):

    FFM.  If F fails, it fails first at an index whose gap is a *record* (maximal) gap.

The standard argument for FFM is:  let n* be the least failing index and suppose g_{n*}
is not a record.  Then some m < n* has g_m >= g_{n*}.  F holds at m (minimality), so

        T_{n*} <= g_{n*} <= g_m < T_m ,

which is a contradiction *provided* T_m <= T_{n*}.  The whole content of FFM is therefore
the inequality T_m <= T_n for the *governing* index m = m(n) := min{ m : g_m >= g_n }.
That index is always a record index, so FFM is *implied by* a finite, checkable predicate
on every n.  The converse fails -- FFM is vacuous wherever F holds -- so the predicate, not
FFM and not the conjecture, is what this module measures.

Everything here is exact-integer or numerically stable float; see `margin_F` for the
cancellation-free form of the Firoozbakht test.  No claim in this module is a proof.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np

# ---------------------------------------------------------------------------
# 1. Prime generation -- segmented sieve, streams (p_n, g_n) without holding all primes
# ---------------------------------------------------------------------------


def base_primes(limit: int) -> np.ndarray:
    """Odd primes <= limit by a plain sieve (limit is small: sqrt of the main bound)."""
    if limit < 2:
        return np.zeros(0, dtype=np.int64)
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return np.flatnonzero(sieve).astype(np.int64)


def prime_blocks(n_max: int, block: int = 1 << 26):
    """Yield successive numpy int64 arrays of the primes <= n_max, in increasing order.

    Segmented, odds-only.  Memory is O(block); total work is the usual N log log N.
    """
    bp = base_primes(int(n_max**0.5) + 1)
    yield np.array([2], dtype=np.int64)
    lo = 3
    while lo <= n_max:
        hi = min(lo + block - 1, n_max)
        if hi % 2 == 0:
            hi -= 1
        if hi < lo:
            break
        size = (hi - lo) // 2 + 1  # odd numbers lo, lo+2, ..., hi
        seg = np.ones(size, dtype=bool)
        for p in bp:
            if p == 2:
                continue
            if p * p > hi:
                break
            start = max(p * p, ((lo + p - 1) // p) * p)
            if start % 2 == 0:
                start += p
            if start > hi:
                continue
            seg[(start - lo) // 2 :: p] = False
        yield lo + 2 * np.flatnonzero(seg).astype(np.int64)
        lo = hi + 2


def gap_stream(n_max: int, block: int = 1 << 26):
    """Yield (idx0, p, g) chunks: p[i] = p_{idx0+i}, g[i] = p_{idx0+i+1} - p_{idx0+i}.

    Indices are 1-based (p_1 = 2), matching the concept cards.  Every consecutive pair
    below n_max is emitted exactly once, including the pair straddling a block boundary.
    """
    idx = 1
    carry: int | None = None
    for blk in prime_blocks(n_max, block):
        if blk.size == 0:
            continue
        if carry is not None:
            blk = np.concatenate(([carry], blk))
        if blk.size < 2:
            carry = int(blk[-1])
            continue
        p = blk[:-1]
        g = np.diff(blk)
        yield idx, p, g
        idx += p.size
        carry = int(blk[-1])


# ---------------------------------------------------------------------------
# 2. The two central quantities
# ---------------------------------------------------------------------------


def threshold_T(p: np.ndarray, n: np.ndarray) -> np.ndarray:
    """T_n = p_n (p_n^{1/n} - 1) = p_n * expm1(log p_n / n).   [card D5]

    expm1 keeps full relative precision when log(p)/n is tiny, which it always is.
    """
    p = np.asarray(p, dtype=np.float64)
    n = np.asarray(n, dtype=np.float64)
    return p * np.expm1(np.log(p) / n)


def margin_F(p: np.ndarray, g: np.ndarray, n: np.ndarray) -> np.ndarray:
    """D_n = (n+1) log p_n - n log p_{n+1}, computed *without* cancellation.

    F holds at n  <=>  p_{n+1}^n < p_n^{n+1}  <=>  D_n > 0.

    The naive form subtracts two numbers of size ~10^10 to get a result of size ~20,
    losing ten digits.  The identity

        D_n = log p_n - n * log1p(g_n / p_n)

    evaluates both terms at their own scale; log1p is accurate to 1 ulp, so the absolute
    error of D_n is ~10^-14 even at n ~ 5*10^8.  [card T2: search design and precision]
    """
    p = np.asarray(p, dtype=np.float64)
    g = np.asarray(g, dtype=np.float64)
    n = np.asarray(n, dtype=np.float64)
    return np.log(p) - n * np.log1p(g / p)


def margin_F_exact(p_n: int, g_n: int, n: int, dps: int = 60) -> float:
    """Same margin at `dps` decimal digits, for auditing the float64 sweep."""
    import mpmath as mp

    with mp.workdps(dps):
        return float(mp.log(p_n) - n * mp.log1p(mp.mpf(g_n) / p_n))


def threshold_T_exact(p_n: int, n: int, dps: int = 60) -> float:
    import mpmath as mp

    with mp.workdps(dps):
        return float(p_n * mp.expm1(mp.log(p_n) / n))


# ---------------------------------------------------------------------------
# 3. The sweep
# ---------------------------------------------------------------------------


@dataclass
class Sweep:
    """Result of one pass over all n with p_n <= n_max."""

    n_max: int
    n_last: int = 0
    p_last: int = 0

    # --- Firoozbakht itself
    violations: list = field(default_factory=list)          # (n, p, g)  -- F fails
    audit_queue: list = field(default_factory=list)         # (n, p, g, D) -- |D| small
    tightest: list = field(default_factory=list)            # (rho, n, p, g, T) top cases

    # --- records (maximal gaps)
    records: list = field(default_factory=list)             # (n, p, g, T_n)

    # --- FFM / P6' predicate
    ffm_exceptions: list = field(default_factory=list)      # (n, p, g, T_n, m, T_m)
    ffm_min_margin: float = math.inf
    ffm_argmin: tuple = ()
    ffm_by_decade: dict = field(default_factory=dict)       # decade -> (min margin, n, ...)

    # --- shape of T
    t_dip_max: float = 0.0                                  # max (running max T) - T_n
    t_dip_argmax: tuple = ()
    t_dip_by_decade: dict = field(default_factory=dict)
    t_down_steps: int = 0                                   # count of T_{n+1} < T_n
    t_steps: int = 0

    # --- per-decade census
    decade_rows: list = field(default_factory=list)

    # --- P6' tolerance budget, measured in primes
    slack_min: float = math.inf                             # min over n of (n_allowed - n)
    slack_argmin: tuple = ()
    slack_by_decade: dict = field(default_factory=dict)
    # relative form: (n_allowed - n) / (n - m)  -- the density overshoot that would break it
    relslack_min: float = math.inf
    relslack_argmin: tuple = ()
    relslack_by_decade: dict = field(default_factory=dict)
    # unconditional Brun-Titchmarsh certificate:  m + 2y/log y <= n_allowed
    bt_certified: int = 0
    bt_total: int = 0
    bt_by_decade: dict = field(default_factory=dict)         # decade -> (certified, total)


def _decade(p: int) -> int:
    return int(math.floor(math.log10(max(p, 2))))


def run_sweep(
    n_max: int,
    block: int = 1 << 26,
    audit_eps: float = 1e-6,
    keep_tightest: int = 40,
    compute_slack: bool = True,
    progress=None,
) -> Sweep:
    """One streaming pass computing every statistic this notebook needs.

    Deliberately single-pass: the sieve dominates, so all predicates ride along with it.
    """
    S = Sweep(n_max=n_max)

    rec_g: list[int] = []       # record gap values, strictly increasing
    rec_T: list[float] = []     # T at the record index
    rec_n: list[int] = []
    rec_p: list[int] = []
    rec_gap_arr = np.zeros(0, dtype=np.int64)
    rec_T_arr = np.zeros(0, dtype=np.float64)

    best_g = 0
    run_max_T = -math.inf
    prev_T = None
    tight: list[tuple] = []

    for idx0, p, g in gap_stream(n_max, block):
        n = np.arange(idx0, idx0 + p.size, dtype=np.int64)
        T = threshold_T(p, n)
        D = margin_F(p, g, n)

        # -- F itself -------------------------------------------------------
        bad = np.flatnonzero(D <= 0)
        for i in bad:
            S.violations.append((int(n[i]), int(p[i]), int(g[i])))
        near = np.flatnonzero(np.abs(D) < audit_eps)
        for i in near:
            S.audit_queue.append((int(n[i]), int(p[i]), int(g[i]), float(D[i])))

        # -- tightest rho = g/T ---------------------------------------------
        rho = g / T
        k = min(keep_tightest, rho.size)
        top = np.argpartition(-rho, k - 1)[:k]
        for i in top:
            tight.append((float(rho[i]), int(n[i]), int(p[i]), int(g[i]), float(T[i])))
        tight.sort(reverse=True)
        del tight[keep_tightest:]

        # -- shape of T ------------------------------------------------------
        S.t_steps += T.size - 1 + (1 if prev_T is not None else 0)
        if prev_T is not None:
            S.t_down_steps += int(T[0] < prev_T)
        S.t_down_steps += int(np.count_nonzero(np.diff(T) < 0))
        prev_T = float(T[-1])

        cummax = np.maximum.accumulate(np.maximum(T, run_max_T))
        dip = cummax - T
        j = int(np.argmax(dip))
        if dip[j] > S.t_dip_max:
            S.t_dip_max = float(dip[j])
            S.t_dip_argmax = (int(n[j]), int(p[j]), float(T[j]), float(cummax[j]))
        run_max_T = float(cummax[-1])

        # per-decade dip
        dec = np.floor(np.log10(p.astype(np.float64))).astype(np.int64)
        for d in np.unique(dec):
            sel = dec == d
            v = float(dip[sel].max())
            cur = S.t_dip_by_decade.get(int(d), (0.0, 0))
            if v > cur[0]:
                jj = int(np.flatnonzero(sel)[int(np.argmax(dip[sel]))])
                S.t_dip_by_decade[int(d)] = (v, int(n[jj]))

        # -- records (maximal gaps) -----------------------------------------
        # a new record is any i with g[i] > max(g[:i], best_g)
        run = np.maximum.accumulate(np.maximum(g, best_g))
        newrec = np.flatnonzero(g >= run) if g.size else np.zeros(0, dtype=np.int64)
        # g >= run marks the *first* attainment of each running max
        seen = best_g
        for i in newrec:
            if g[i] > seen:
                seen = int(g[i])
                rec_g.append(int(g[i]))
                rec_T.append(float(T[i]))
                rec_n.append(int(n[i]))
                rec_p.append(int(p[i]))
                S.records.append((int(n[i]), int(p[i]), int(g[i]), float(T[i])))
        # NOTE: records discovered *inside this block* must be visible to the FFM test
        # below for indices later in the same block.  Handled by building the arrays
        # after the record scan and using searchsorted on the *final* list, which is
        # correct because m(n) <= n always and record values are strictly increasing.
        best_g = seen
        rec_gap_arr = np.array(rec_g, dtype=np.int64)
        rec_T_arr = np.array(rec_T, dtype=np.float64)

        # -- FFM / P6' -------------------------------------------------------
        # m(n) = min{ m : g_m >= g_n }.  Record values are strictly increasing and every
        # gap size that ever occurs is <= the current record, so m(n) is the index of the
        # first record whose value is >= g_n.
        j = np.searchsorted(rec_gap_arr, g, side="left")
        valid = j < rec_gap_arr.size
        Tm = np.full(g.shape, -np.inf)
        Tm[valid] = rec_T_arr[j[valid]]
        marg = T - Tm                       # FFM/P6' needs marg >= 0
        # an index that *is itself* the governing record has marg == 0 by construction
        strict = valid & (marg < 0)
        for i in np.flatnonzero(strict):
            S.ffm_exceptions.append(
                (int(n[i]), int(p[i]), int(g[i]), float(T[i]),
                 int(rec_n[int(j[i])]), float(Tm[i]))
            )
        # An index that *is* its own governing record has marg == 0 by construction; it
        # carries no information about P6'.  Exclude it explicitly (not by sign, which
        # would presuppose the answer).
        rec_n_arr = np.array(rec_n, dtype=np.int64)
        nonself = valid & (rec_n_arr[j] != n)
        if np.any(nonself):
            ii = int(np.flatnonzero(nonself)[int(np.argmin(marg[nonself]))])
            if float(marg[ii]) < S.ffm_min_margin:
                S.ffm_min_margin = float(marg[ii])
                S.ffm_argmin = (int(n[ii]), int(p[ii]), int(g[ii]),
                                float(T[ii]), float(Tm[ii]))
            for d in np.unique(dec[nonself]):
                sel = nonself & (dec == d)
                kk = int(np.flatnonzero(sel)[int(np.argmin(marg[sel]))])
                v = float(marg[kk])
                cur = S.ffm_by_decade.get(int(d))
                if cur is None or v < cur[0]:
                    S.ffm_by_decade[int(d)] = (v, int(n[kk]), int(p[kk]), int(g[kk]))

        # -- the tolerance budget, in primes ---------------------------------
        # T(p_n, .) is strictly decreasing, so there is a unique real n_allowed with
        # T(p_n, n_allowed) = T_m.  P6' at n  <=>  n <= n_allowed.  The difference is the
        # entire safety budget, and its currency is a prime count.
        if compute_slack and np.any(nonself):
            pn = p.astype(np.float64)
            n_allowed = np.log(pn) / np.log1p(Tm / pn)      # -inf-safe: Tm finite when valid
            slack = n_allowed - n
            pm_arr = np.array(rec_p, dtype=np.float64)[j]
            m_arr = np.array(rec_n, dtype=np.float64)[j]
            window = pn - pm_arr
            count = n - m_arr                              # primes in (p_m, p_n]
            with np.errstate(divide="ignore", invalid="ignore"):
                relslack = np.where(count > 0, slack / count, np.inf)
                bt = np.where(window > 3.0, 2.0 * window / np.log(np.maximum(window, 4.0)),
                              np.inf)
            certified = nonself & (m_arr + bt <= n_allowed)

            ii = int(np.flatnonzero(nonself)[int(np.argmin(slack[nonself]))])
            if float(slack[ii]) < S.slack_min:
                S.slack_min = float(slack[ii])
                S.slack_argmin = (int(n[ii]), int(p[ii]), int(g[ii]), int(m_arr[ii]),
                                  int(pm_arr[ii]), float(count[ii]))
            kk = int(np.flatnonzero(nonself)[int(np.argmin(relslack[nonself]))])
            if float(relslack[kk]) < S.relslack_min:
                S.relslack_min = float(relslack[kk])
                S.relslack_argmin = (int(n[kk]), int(p[kk]), int(g[kk]), int(m_arr[kk]),
                                     int(pm_arr[kk]), float(count[kk]), float(slack[kk]))
            S.bt_certified += int(np.count_nonzero(certified))
            S.bt_total += int(np.count_nonzero(nonself))
            for d in np.unique(dec[nonself]):
                sel = nonself & (dec == d)
                a = int(np.flatnonzero(sel)[int(np.argmin(slack[sel]))])
                cur = S.slack_by_decade.get(int(d))
                if cur is None or float(slack[a]) < cur[0]:
                    S.slack_by_decade[int(d)] = (float(slack[a]), int(n[a]), int(p[a]),
                                                 int(g[a]))
                b = int(np.flatnonzero(sel)[int(np.argmin(relslack[sel]))])
                cur = S.relslack_by_decade.get(int(d))
                if cur is None or float(relslack[b]) < cur[0]:
                    S.relslack_by_decade[int(d)] = (float(relslack[b]), int(n[b]),
                                                    int(p[b]), int(g[b]))
                c0, t0 = S.bt_by_decade.get(int(d), (0, 0))
                S.bt_by_decade[int(d)] = (c0 + int(np.count_nonzero(certified & sel)),
                                          t0 + int(np.count_nonzero(sel)))

        S.n_last = int(n[-1])
        S.p_last = int(p[-1])
        if progress:
            progress(S)

    S.tightest = tight
    return S


# ---------------------------------------------------------------------------
# 3b. Anatomy of a P6' margin -- why does T_n exceed T_m at all?
# ---------------------------------------------------------------------------


def excess_to_break(p_n: int, n: int, T_m: float) -> float:
    """How many *extra* primes below p_n would be needed to make T_n < T_m.

    T_n = p_n * expm1(log p_n / n) is strictly decreasing in n at fixed p_n (card D5,
    fact 1).  So there is a unique real delta with T(p_n, n + delta) = T_m:

        delta = log(p_n) / log1p(T_m / p_n)  -  n.

    delta > 0 is the *entire* safety budget of P6' at this index, expressed in the only
    currency an arithmetic theorem can pay in: a count of primes.  Breaking FFM at n
    requires pi(p_n) to exceed its true value by delta -- i.e. it requires an interval
    holding delta more primes than it does.
    """
    return math.log(p_n) / math.log1p(T_m / p_n) - n


def window_anatomy(p_m: int, m: int, p_n: int, n: int, T_m: float, T_n: float) -> dict:
    """Decompose the margin T_n - T_m over the window (p_m, p_n]."""
    import mpmath as mp

    with mp.workdps(30):
        expected = float(mp.li(p_n) - mp.li(p_m))
    observed = n - m
    return {
        "p_m": p_m, "m": m, "p_n": p_n, "n": n,
        "dp": p_n - p_m,
        "primes_observed": observed,
        "primes_expected_li": expected,
        "density_excess": observed - expected,
        "T_m": T_m, "T_n": T_n, "margin": T_n - T_m,
        "margin_rel": (T_n - T_m) / T_m,
        "excess_to_break": excess_to_break(p_n, n, T_m),
        "safety_factor": (excess_to_break(p_n, n, T_m) / (observed - expected))
        if observed - expected > 0 else math.inf,
    }


# ---------------------------------------------------------------------------
# 4. The synthetic model -- what FFM would need if arithmetic did not intervene
# ---------------------------------------------------------------------------


def firoozbakht_holds(q: list[int]) -> list[int]:
    """Indices n (1-based) of the sequence `q` at which the Firoozbakht predicate FAILS.

    The predicate is the definition applied verbatim to an arbitrary increasing sequence:
    q_{n+1}^n < q_n^{n+1}.  Evaluated in exact integer arithmetic -- no floats, so the
    witness below cannot be blamed on rounding.
    """
    out = []
    for i in range(len(q) - 1):
        n = i + 1
        if q[i + 1] ** n >= q[i] ** (n + 1):
            out.append(n)
    return out


def toy_ffm_witness(p_head: list[int], G: int, K: int, g2: int) -> dict:
    """An explicit increasing sequence whose FIRST Firoozbakht failure is at a NON-record gap.

    Shape:  p_head (a genuine prime prefix)  ->  one jump of size G (a record for the
    sequence)  ->  K jumps of size 2  ->  one jump of size g2 < G.

    Nothing here is claimed to be prime.  That is the entire point: FFM is *not* a formal
    consequence of the definition of T together with minimality of the first failure.  It
    needs an arithmetic input -- an upper bound on how many terms an interval may contain.
    This function exhibits the counter-model that such an input has to exclude.
    """
    q = list(p_head)
    q.append(q[-1] + G)
    for _ in range(K):
        q.append(q[-1] + 2)
    q.append(q[-1] + g2)
    fails = firoozbakht_holds(q)
    gaps = [q[i + 1] - q[i] for i in range(len(q) - 1)]
    first = fails[0] if fails else None
    is_record = None
    if first is not None:
        gf = gaps[first - 1]
        is_record = all(gaps[i] < gf for i in range(first - 1))
    return {
        "sequence_len": len(q), "gaps": gaps, "first_failure_index": first,
        "first_failure_gap": gaps[first - 1] if first else None,
        "first_failure_is_record": is_record,
        "ffm_broken": (first is not None) and (is_record is False),
        "all_failures": fails[:10],
        "q_head": q[:6], "q_tail": q[-4:],
    }


def dense_run_required(p0: int, G: int, g2: int) -> dict:
    """At real scale: how dense would primes have to be for the toy witness to be real?

    Sitting at a record gap G ending at p0 with index n0 ~ p0/(log p0 - 1), how many extra
    terms K must be packed in before a later gap of size g2 <= G can beat its own T?  The
    answer is compared with the Montgomery-Vaughan / Brun-Titchmarsh cap

        pi(x + y) - pi(x)  <=  2y / log y        (y >= 2),

    which is unconditional.  The ratio is the factor by which reality would have to be
    violated for FFM to fail by this mechanism.
    """
    L0 = math.log(p0)
    n0 = max(int(p0 / (L0 - 1)), 2)
    T_m = p0 * math.expm1(L0 / n0)
    # binary search the smallest K making T at the later index drop to <= g2
    lo, hi = 0, 1
    def T_after(K: int) -> float:
        p1 = p0 + G + 2 * K
        n1 = n0 + 1 + K
        return p1 * math.expm1(math.log(p1) / n1)
    while T_after(hi) > g2 and hi < 1 << 62:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if T_after(mid) <= g2:
            hi = mid
        else:
            lo = mid + 1
    K = lo
    W = G + 2 * K
    cap = 2 * W / math.log(W) if W > 3 else float("inf")
    return {
        "p0": p0, "n0": n0, "G": G, "g2": g2, "T_m": T_m,
        "K_required": K, "window_length": W, "terms_in_window": K + 1,
        "MV_cap": cap, "violation_factor": (K + 1) / cap if cap else math.inf,
        "T_after": T_after(K),
    }


# ---------------------------------------------------------------------------
# 5. An effective sufficient criterion for P6' -- can explicit pi(x) bounds close it?
# ---------------------------------------------------------------------------
#
# T_n is strictly decreasing in n at fixed p (card D5, fact 1).  So:
#   * an UPPER bound on pi(p) yields a LOWER bound on T at p   -> T_lo
#   * a LOWER bound on pi(p) yields an UPPER bound on T at p   -> T_hi
# P6' at a record m with gap G is implied by   T_lo(p_m + G) >= T_hi(p_m),
# because every index n governed by m has p_n >= p_m + G and T_lo is increasing.
#
# Bound sources (card T1, all with their validity ranges):
#   Dusart 2010 Thm 6.9 (6.6):  pi(x) <= x/(ln x - 1.1)      x >= 60184     [L0]
#                               pi(x) >= x/(ln x - 1)        x >= 5393      [L0]
#   Axler 2014 Cor. 3.5:        pi(x) <  x/(ln x - 1 - 1.17/ln x)
#                                                            x >= 2634800823 [L2_strong,
#                                                                             NOT OPENED]
#   Axler 2014 Cor. 3.6:        pi(x) >  x/(ln x - 1 - 1/ln x - 1/ln^2 x)
#                                                            x >= 1772201    [L2_strong,
#                                                                             NOT OPENED]

PI_BOUNDS = {
    "dusart": {
        "upper": (lambda x: x / (math.log(x) - 1.1), 60184),
        "lower": (lambda x: x / (math.log(x) - 1.0), 5393),
        "tier": "L0 (dusart2010estimates Thm 6.9 eq. 6.6)",
    },
    "axler": {
        "upper": (lambda x: x / (math.log(x) - 1 - 1.17 / math.log(x)), 2634800823),
        "lower": (lambda x: x / (math.log(x) - 1 - 1 / math.log(x)
                                 - 1 / math.log(x) ** 2), 1772201),
        "tier": "L2_strong, UNOPENED (axler2014newbounds Cor. 3.5/3.6)",
    },
}


def T_lo(p: float, variant: str) -> float:
    """Lower bound on T at the prime p, from an upper bound on pi(p)."""
    f, _ = PI_BOUNDS[variant]["upper"]
    return p * math.expm1(math.log(p) / f(p))


def T_hi(p: float, variant: str) -> float:
    """Upper bound on T at the prime p, from a lower bound on pi(p)."""
    f, _ = PI_BOUNDS[variant]["lower"]
    return p * math.expm1(math.log(p) / f(p))


def p6_criterion(p_m: float, G: float, variant: str) -> float:
    """T_lo(p_m + G) - T_hi(p_m).  Non-negative  =>  P6' certified at this record."""
    return T_lo(p_m + G, variant) - T_hi(p_m, variant)


def G_min(p_m: float, variant: str, hi: float = 1e9) -> float:
    """Smallest record gap G at p_m for which the effective criterion certifies P6'."""
    if p6_criterion(p_m, 0.0, variant) >= 0:
        return 0.0
    lo, h = 0.0, 2.0
    while h < hi and p6_criterion(p_m, h, variant) < 0:
        h *= 2
    if h >= hi:
        return math.inf
    for _ in range(200):
        mid = (lo + h) / 2
        if p6_criterion(p_m, mid, variant) < 0:
            lo = mid
        else:
            h = mid
    return h
