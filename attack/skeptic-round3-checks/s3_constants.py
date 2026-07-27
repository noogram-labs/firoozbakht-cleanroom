#!/usr/bin/env python3
"""Independent re-derivation of the constants of the DESIGNATED Theorem C-b'
and of Theorem C-a' from the statements in FFM 7.4, plus the finite-branch gap
facts and an empirical test of the two Axler lower-bound rows.
Written from the statements; no upstream script opened."""
import numpy as np, math
from mpmath import mp, mpf, exp, log
mp.dps = 50

lA = float(math.log(6690557)); lD = math.log(1e8)
print(f"l_A = {lA:.10f}   l_D = {lD:.10f}", flush=True)

# --- C-b' : need d >= psi(l)/(2l-1),  psi = 0.17 - 2.1/l + v^2 e^-l, v = l^2-l-1-2.1/l
l = np.arange(lA, 300, 1e-6)
v = l*l - l - 1 - 2.1/l
f = (0.17 - 2.1/l + v*v*np.exp(-l))/(2*l-1)
k = int(f.argmax())
print(f"C-b' EXACT max required d = {f[k]:.12g} at l = {l[k]:.6f}", flush=True)

# cell majorant, width 0.01
a = np.arange(lA, 300, 0.01); b = a + 0.01
m = (0.17 - 2.1/b + a**4*np.exp(-a))/(2*a-1)
j = int(m.argmax())
print(f"C-b' cell MAJORANT max = {m[j]:.12g} on cell starting l = {a[j]:.6f}", flush=True)
print(f"     0.0017569 - majorant = {0.0017569 - m[j]:.4g}", flush=True)
print(f"     tail l>=300 bound = {(0.17+300**4*math.exp(-300))/599:.8g}", flush=True)

# --- C-a' : need d >= (0.1 l + eps)/(2l-1.1), eps = (l^2-l)^2 e^-l
l = np.arange(lD, 1000, 1e-6); v = l*l - l
f = (0.1*l + v*v*np.exp(-l))/(2*l-1.1)
k = int(f.argmax())
print(f"C-a' EXACT max required d = {f[k]:.12g} at l = {l[k]:.6f}", flush=True)
a = np.arange(lD, 1000, 0.01); b = a+0.01
m = (0.1*b + a**4*np.exp(-a))/(2*a-1.1)
j = int(m.argmax())
print(f"C-a' cell MAJORANT max = {m[j]:.12g} on cell starting l = {a[j]:.6f}", flush=True)
print(f"     tail l>=1000 bound = {(100+1000**4*math.exp(-1000))/1998.9:.8g}", flush=True)

# --- finite branches
def sieve(n):
    s=np.ones(n+1,dtype=bool); s[:2]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i::i]=False
    return np.flatnonzero(s)
p = sieve(10**8); g = np.diff(p)
for lim in (60184, 468049, 1772201, 6690557, 10**8):
    msk = p[:-1] < lim
    gg = np.where(msk, g, 0); k = int(gg.argmax())
    print(f"max gap below {lim:,} = {int(gg.max())} at p = {int(p[k]):,}", flush=True)

# --- Axler lower rows: pi(x) > x/(log x - 1 - 1/log x - a/log^2 x) for x >= x0
def check_row(a, x0):
    i0 = int(np.searchsorted(p, x0)); bad = 0
    idx = np.arange(i0, len(p), 1)
    x = p[idx].astype(np.float64); L = np.log(x)
    lhs = (idx+1).astype(np.float64)          # pi(p_n) = n (1-indexed)
    rhs = x/(L - 1 - 1/L - a/(L*L))
    return int((lhs <= rhs).sum())
print("Axler row a=1   (x0=1 772 201): failures below 1e8 =", check_row(1.0, 1772201), flush=True)
print("Axler row a=2.1 (x0=6 690 557): failures below 1e8 =", check_row(2.1, 6690557), flush=True)
