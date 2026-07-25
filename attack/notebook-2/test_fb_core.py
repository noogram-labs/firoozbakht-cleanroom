"""
test_fb_core — the assertions the notebook's claims rest on, runnable headless.

    python3 test_fb_core.py          # exits non-zero on any failure

Deliberately dependency-light: plain asserts, no pytest required (it works under
pytest too). Every test corresponds to a claim made in notebook-2.ipynb.
"""
import math
import sys
from decimal import Decimal, localcontext

import numpy as np

import fb_core as fb

FAILS = []


def check(name, cond, detail=""):
    print(f"{'ok  ' if cond else 'FAIL'}  {name}{('  -- ' + detail) if detail else ''}")
    if not cond:
        FAILS.append(name)


# --------------------------------------------------------------------------
# 1. Sieve correctness against known prime counts.
# --------------------------------------------------------------------------
def test_sieve():
    known = {10**5: 9592, 10**6: 78498, 10**7: 664579}
    for N, pi in known.items():
        cnt = sum(len(c) for c in fb.sieve_segments(N, seg=10**6))
        check(f"pi({N:,}) == {pi:,}", cnt == pi, f"got {cnt:,}")


# --------------------------------------------------------------------------
# 2. The exact criterion is the ground truth, and the Decimal path matches it.
# --------------------------------------------------------------------------
def test_exact_vs_certified():
    pr = np.concatenate(list(fb.sieve_segments(60_000)))
    bad = []
    for i in range(3000):
        n = i + 1
        e = fb.exact_verdict(int(pr[i]), int(pr[i + 1]), n)
        c, _ = fb.certified_verdict(int(pr[i]), int(pr[i + 1]), n)
        if e != c:
            bad.append(n)
    check("exact integer verdict == Decimal-certified verdict, n=1..3000",
          not bad, f"disagreements: {bad}")
    check("F holds exactly at every n=1..3000",
          all(fb.exact_verdict(int(pr[i]), int(pr[i + 1]), i + 1) for i in range(3000)))


def test_certified_refuses_undecided():
    # A synthetic pair whose margin is far below the error budget must RAISE,
    # never return a verdict. This is the anti-silent-pass guarantee.
    try:
        fb.certified_verdict(1327, 1361, 217, prec=3)
    except ArithmeticError:
        check("certified_verdict raises rather than guess at low precision", True)
    else:
        check("certified_verdict raises rather than guess at low precision", False)


# --------------------------------------------------------------------------
# 3. Reproduction of the figures already recorded in the run's concept cards.
# --------------------------------------------------------------------------
def test_reproduces_cards():
    r = fb.scan(3 * 10**6, verbose=False)
    check("card D6: max rho (n>=10) == 0.7604709 at n=217, p=1327, g=34",
          abs(r["top"][0][0] - 0.7604709) < 5e-7 and r["top"][0][1] == 217
          and r["top"][0][2] == 1327 and r["top"][0][3] == 34,
          f"got {r['top'][0]}")
    check("card D6: runner-up rho == 0.7590821 at p=2010733",
          abs(r["top"][1][0] - 0.7590821) < 5e-7 and r["top"][1][2] == 2010733,
          f"got {r['top'][1]}")
    check("card T2: max c (n>=10) == 0.70257 at p=2010733",
          abs(r["max_c"][0] - 0.7025656) < 5e-7 and r["max_c"][2] == 2010733,
          f"got {r['max_c']}")
    check("decompose 5.1: max F2 margin == 0.9999984",
          abs(r["max_f2"][0] - 0.9999984) < 5e-7, f"got {r['max_f2'][0]}")
    check("no violation of F below 3e6", r["violations"] == [])
    check("only escalations below 3e6 are n=2 and n=4",
          [e[0] for e in r["escalations"]] == [2, 4], f"got {r['escalations']}")


# --------------------------------------------------------------------------
# 4. Lemma A and its corollaries.
# --------------------------------------------------------------------------
def test_lemma_A():
    r = fb.scan(10**7, verbose=False)
    check("Lemma A: T_n >= L(L-1.1) at every p_n in [60184, 1e7]",
          r["lemmaA_min_slack"] > 0, f"min slack {r['lemmaA_min_slack']:+.6f}")

    # Corollary A1's constant.
    L = math.log(fb.DUSART_XMIN)
    check("Corollary A1: L(L-1.1) at x=60184 exceeds 108",
          L * (L - 1.1) > 108, f"{L*(L-1.1):.5f}")

    # The validity range is load-bearing: below e^10 the bound is FALSE.
    for x in (10**3, 10**4, 20000):
        Lx = math.log(x)
        check(f"Lemma A's bound would be false at x={x:,} (outside its range)",
              Lx * (Lx - 1.1) > Lx * Lx - Lx - 1,
              f"L(L-1.1)={Lx*(Lx-1.1):.4f} vs L^2-L-1={Lx*Lx-Lx-1:.4f}")


def test_safe_bound_is_a_root():
    # S(g) must solve L(L-1.1) = g, and be rounded in the conservative direction.
    for g in (112, 210, 354, 1476, 1920):
        L = math.log(float(fb.safe_bound_S(g)))
        check(f"S({g}) solves L(L-1.1)=g", abs(L * (L - 1.1) - g) < 1e-6 * g,
              f"L(L-1.1)={L*(L-1.1):.6f}")
    # The rounding direction is what makes a "safe" verdict conservative. Compare
    # against the same quantity computed at higher precision WITHOUT inflation --
    # a float64 reference would be 30 decades too coarse to see the difference.
    with localcontext() as ctx:
        ctx.prec = 80
        S_true = ((Decimal("1.21") + 4 * Decimal(112)).sqrt() + Decimal("1.1")) / 2
        S_true = S_true.exp()
        Lx = Decimal(10**9).ln()
        need_true = Lx * (Lx - Decimal("1.1"))
    check("safe_bound_S rounds up (conservative for a 'safe' verdict)",
          fb.safe_bound_S(112) > S_true,
          f"{fb.safe_bound_S(112)} vs {S_true}")
    check("gap_needed rounds down (conservative in the same direction)",
          fb.gap_needed(10**9) < need_true,
          f"{fb.gap_needed(10**9)} vs {need_true}")


def test_p6_prime():
    # Card L15's P6': T_{m(n)} <= T_n for m(n) the governing maximal-gap index.
    # Two independent things are asserted: the record table itself (21 records
    # below 3e6, per the card), and P6' having no exception in range.
    r = fb.scan(3 * 10**6, verbose=False)
    check("card L15: 21 maximal-gap records below 3e6",
          len(r["records"]) == 21, f"got {len(r['records'])}")
    check("P6' has no exception below 3e6", r["p6_n_exceptions"] == 0,
          f"got {r['p6_n_exceptions']}")

    # Segment size must not change the answer -- the record carry-over across
    # segment boundaries is the easy place to get this wrong.
    a = fb.scan(10**7, seg=10**7, verbose=False)
    b = fb.scan(10**7, seg=10**6, verbose=False)
    check("record table is invariant under segment size",
          a["records"] == b["records"], f"{len(a['records'])} vs {len(b['records'])}")
    check("P6' margin is invariant under segment size",
          a["p6_min_slack"] == b["p6_min_slack"])

    # The finding of section 6b: the margin shrinks with range.
    c = fb.scan(10**8, verbose=False)
    check("P6' still has no exception below 1e8", c["p6_n_exceptions"] == 0)
    check("P6' minimum margin SHRINKS from 3e6 to 1e8",
          c["p6_min_slack"][0] < r["p6_min_slack"][0],
          f"{r['p6_min_slack'][0]:.3e} -> {c['p6_min_slack'][0]:.3e}")


def test_1920():
    v = fb.gap_needed(2**64)
    check("L(L-1.1) at 2^64 lands on the published 1920 threshold",
          1919 < float(v) < 1920, f"got {float(v):.4f}")


# --------------------------------------------------------------------------
# 5. The route-(b) certificate, on data we own.
# --------------------------------------------------------------------------
def test_certificate():
    r = fb.scan(10**8, verbose=False)
    cert = fb.lemma_A_certificate(r["first_occ"], 10**8)
    check("route (b) certificate is SETTLED below 1e8",
          cert["verdict"] == "SETTLED", f"unsettled: {cert['unsettled']}")
    check("minimum safety factor is 5.337 at g=112",
          abs(cert["min_ratio"] - 5.3371) < 1e-3 and cert["min_ratio_gap"] == 112,
          f"got {cert['min_ratio']:.4f} at g={cert['min_ratio_gap']}")
    wins = fb.window_certificate(r["records"], 10**8, n_windows=20)
    check("every geometric window below 1e8 is certified by the record table",
          all(w["ok"] for w in wins), f"{sum(1 for w in wins if not w['ok'])} failed")


if __name__ == "__main__":
    for fn in [test_sieve, test_exact_vs_certified, test_certified_refuses_undecided,
               test_reproduces_cards, test_lemma_A, test_safe_bound_is_a_root,
               test_p6_prime, test_1920, test_certificate]:
        print(f"\n--- {fn.__name__}")
        fn()
    print()
    if FAILS:
        print(f"{len(FAILS)} FAILURE(S): {FAILS}")
        sys.exit(1)
    print("all checks passed")
