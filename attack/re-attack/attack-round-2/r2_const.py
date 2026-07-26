"""Rigorous constants for Theorem C, round 2.

For each branch the required separation is d >= psi(l)/(2l - c), and psi is
majorised on each cell [a,b] by evaluating each monotone piece at its worst
endpoint.  The maximum over a partition is therefore a PROOF, not a sweep.
"""
import mpmath as mp
mp.mp.dps = 40

def cell_max_axler(a, b, alpha):
    """max over l in [a,b] of  (0.17 - alpha/l + l^4 e^-l)/(2l-1),  majorised.
    0.17 - alpha/l increasing -> use b.  l^4 e^-l decreasing (l>4) -> use a.
    1/(2l-1) decreasing -> use a."""
    a, b = mp.mpf(a), mp.mpf(b)
    num = mp.mpf('0.17') - mp.mpf(alpha)/b + a**4*mp.e**(-a)
    return num/(2*a - 1)

def cell_max_dusart(a, b):
    """max over [a,b] of (0.1 l + l^4 e^-l)/(2l-1.1), majorised.
    0.1*l increasing -> b ; l^4 e^-l decreasing -> a ; 1/(2l-1.1) decr -> a."""
    a, b = mp.mpf(a), mp.mpf(b)
    return (mp.mpf('0.1')*b + a**4*mp.e**(-a))/(2*a - mp.mpf('1.1'))

def sup_over(lo, hi, step, f, tail_fun=None):
    best = (None, mp.mpf(-1))
    x = mp.mpf(lo)
    h = mp.mpf(step)
    while x < hi:
        y = min(x+h, mp.mpf(hi))
        v = f(x, y)
        if v > best[1]: best = (x, v)
        x = y
    return best

L2 = mp.log(6690557)      # Axler a=2.1 both editions
L1 = mp.log(1772201)      # Axler a=1  arXiv only
L0 = mp.log(468049)       # Axler a=0  both editions
LD = mp.log(10**8)        # Dusart branch, cut-off raised to 1e8

print("=== Axler a=2.1 (both editions), l >= log(6690557) =", mp.nstr(L2,8))
b = sup_over(L2, 300, '0.01', lambda a,bb: cell_max_axler(a,bb,'2.1'))
print("   partition max on [l2,300]:", mp.nstr(b[1],8), "at cell starting", mp.nstr(b[0],8))
tail = (mp.mpf('0.17') + mp.mpf(300)**4*mp.e**(-mp.mpf(300)))/(2*300-1)
print("   tail bound l>=300      :", mp.nstr(tail,8))
CB = max(b[1], tail); print("   => rigorous constant d >=", mp.nstr(CB,8),
                            " i.e. p_m <=", mp.nstr(mp.e**(-CB),9), "p_n0")

print("\n=== Axler a=1 (arXiv-only column), l >= log(1772201) =", mp.nstr(L1,8))
b1 = sup_over(L1, 300, '0.01', lambda a,bb: cell_max_axler(a,bb,'1'))
print("   partition max:", mp.nstr(b1[1],8), "at", mp.nstr(b1[0],8))
C1 = max(b1[1], tail); print("   => d >=", mp.nstr(C1,8), " p_m <=", mp.nstr(mp.e**(-C1),9),"p_n0")

print("\n=== Axler a=0 (both editions), l >= log(468049) =", mp.nstr(L0,8))
b0 = sup_over(L0, 300, '0.01', lambda a,bb: cell_max_axler(a,bb,'0'))
print("   partition max:", mp.nstr(b0[1],8), "at", mp.nstr(b0[0],8))
C0 = max(b0[1], tail); print("   => d >=", mp.nstr(C0,8), " p_m <=", mp.nstr(mp.e**(-C0),9),"p_n0")

print("\n=== Dusart only, l >= log(1e8) =", mp.nstr(LD,8))
bd = sup_over(LD, 1000, '0.01', cell_max_dusart)
print("   partition max on [ld,1000]:", mp.nstr(bd[1],8), "at", mp.nstr(bd[0],8))
tailD = (mp.mpf('0.1')*mp.mpf(10**6) )  # placeholder, handled analytically below
# analytic tail: (0.1 l + eps)/(2l-1.1) < 0.1 l/(2l-1.1) + eps/(2l-1.1);
# 0.1l/(2l-1.1) is DECREASING in l with limit 0.05, so on [1000,inf) it is < value at 1000
t1 = (mp.mpf('0.1')*1000 + mp.mpf(1000)**4*mp.e**(-mp.mpf(1000)))/(2*1000-mp.mpf('1.1'))
print("   tail bound l>=1000 (0.1l/(2l-1.1) decreasing):", mp.nstr(t1,8))
CD = max(bd[1], t1); print("   => d >=", mp.nstr(CD,8), " p_m <=", mp.nstr(mp.e**(-CD),9),"p_n0")

print("\n=== sanity: exact d* at the maximising l (solving the quadratic)")
def dstar_ax(l, alpha):
    l=mp.mpf(l); v=l*l-l-1-mp.mpf(alpha)/l; C=v*(1+v/mp.e**l)
    return (1+mp.sqrt(1+4*(C+mp.mpf('1.17'))))/2 - l
def dstar_du(l):
    l=mp.mpf(l); v=l*l-l; C=v*(1+v/mp.e**l)
    return (mp.mpf('1.1')+mp.sqrt(mp.mpf('1.21')+4*C))/2 - l
print("   Axler a=2.1 exact max ~", mp.nstr(max(dstar_ax(L2+mp.mpf(i)/100,'2.1') for i in range(0,4000)),8))
print("   Dusart      exact max ~", mp.nstr(max(dstar_du(LD+mp.mpf(i)/100) for i in range(0,4000)),8))
print("\n   T_n0 lower bound at p_n0 = 2^64:  lam =", mp.nstr(mp.log(mp.mpf(2)**64),10),
      " lam^2-1.1lam =", mp.nstr(mp.log(mp.mpf(2)**64)**2 - mp.mpf('1.1')*mp.log(mp.mpf(2)**64),10))
