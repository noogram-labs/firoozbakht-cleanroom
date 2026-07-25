"""F2: independent check of proof-attempt-0 Theorem C(a) and C(b).

Written from the *statements* in proof-attempt-0.md sections 6.1/6.2, not from
its scripts.  For each l = L_m it solves for the true minimal separation
d = L_{n0} - L_m at which Lemma W's hypothesis  C(p_m) <= A(p_{n0})  first holds,
with p_m = e^l, and compares against the constants the document quotes.
"""
import numpy as np, math

l0 = math.log(60184)      # Dusart (D-high) validity range
l1 = math.log(1772201)    # Axler  (A-high) validity range


def v_axler(l):
    return l * l - l - 1 - 1 / l


def need_a(l):
    """Theorem C(a): (D-high) at m, (D-low) at n0.  Bar: lam^2 - 1.1 lam."""
    C = (l * l - l) * (1 + (l * l - l) / math.exp(l))
    lam = (1.1 + math.sqrt(1.21 + 4 * C)) / 2
    return lam - l


def need_b_written(l):
    """(A-high) exactly as printed in 6.1:  T <= v (1 + l^4/x)."""
    C = v_axler(l) * (1 + l ** 4 / math.exp(l))
    lam = (1 + math.sqrt(1 + 4 * (C + 1.17))) / 2
    return lam - l


def need_b_tight(l):
    """(A-high) in the tight form 6.2's algebra actually assumes: T <= v (1 + v/x)."""
    C = v_axler(l) * (1 + v_axler(l) / math.exp(l))
    lam = (1 + math.sqrt(1 + 4 * (C + 1.17))) / 2
    return lam - l


def pa0_formula(l):
    """The sufficient condition displayed in 6.2:  d(2l-1) + d^2 >= 0.17 - 1/l + l^4/p_m."""
    return (0.17 - 1 / l + l ** 4 * math.exp(-l)) / (2 * l - 1)


if __name__ == "__main__":
    ls = np.linspace(l0, 400, 600_000)
    da = np.array([need_a(x) for x in ls])
    print("C(a) true max required d = %.6f at l=%.5f   [PA-0 quotes 0.0623]  OK=%s"
          % (da.max(), ls[da.argmax()], da.max() <= 0.0623))

    ls = np.linspace(l1, 300, 600_000)
    bw = np.array([need_b_written(x) for x in ls])
    bt = np.array([need_b_tight(x) for x in ls])
    pf = np.array([pa0_formula(x) for x in ls])
    print("C(b) with (A-high) AS PRINTED : max required d = %.6f at l=%.5f  -> 0.004479 OK=%s"
          % (bw.max(), ls[bw.argmax()], bw.max() <= 0.004479))
    print("C(b) with (A-high) TIGHTENED  : max required d = %.7f at l=%.5f  -> 0.004479 OK=%s"
          % (bt.max(), ls[bt.argmax()], bt.max() <= 0.004479))
    print("PA-0's own displayed criterion: max          = %.7f at l=%.5f  -> quoted 0.004479 covers it=%s"
          % (pf.max(), ls[pf.argmax()], 0.004479 >= pf.max()))
