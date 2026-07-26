"""Skeptic round-2: independent sieve-based recomputation.  Own code path."""
import numpy as np
from mpmath import mp, mpf, log, exp
mp.dps = 60

N = 2*10**8
print("sieving to", N, "...", flush=True)
s = np.ones(N//2, dtype=bool); s[0] = False          # odds: index i <-> 2i+1
for i in range(1, int(N**0.5)//2+1):
    if s[i]:
        p = 2*i+1
        s[(p*p)//2::p] = False
P = np.empty(int(s.sum())+1, dtype=np.int64)
P[0] = 2; P[1:] = 2*np.nonzero(s)[0].astype(np.int64)+1
del s
print("pi(2e8) =", len(P), flush=True)   # 1-indexed: p_n = P[n-1]
G = np.diff(P)                            # G[n-1] = g_n, defined for n=1..len(P)-1

def p(n): return int(P[n-1])
def T(n):
    x = mpf(int(P[n-1])); return x*(exp(log(x)/n)-1)

print("\n=== FFM Theorem 1 witnesses ===")
for n in (1823,1831,1847,1879,10655449,10655462,10655590):
    print(f"  p_{n} = {p(n)}  g={int(G[n-1])}  T={mp.nstr(T(n),16)}")
print("  W1 T_1823 - T_1847 =", mp.nstr(T(1823)-T(1847),12), "(claim 0.028610605)")
print("  W2 T_10655449 - T_10655590 =", mp.nstr(T(10655449)-T(10655590),12), "(claim 3.5792097e-5)")

# ---- records / maximal gaps ----
run = np.maximum.accumulate(G)
isrec = np.empty(len(G), dtype=bool); isrec[0]=True; isrec[1:] = G[1:] > run[:-1]
rec_idx = np.nonzero(isrec)[0]+1        # 1-indexed record indices
print("\n=== records (maximal gaps) ===")
for lim in (3*10**6, 10**7, 10**8, 2*10**8):
    k = int(np.searchsorted(P[rec_idx-1], lim))
    print(f"  # records with p < {lim:>12}: {k}")
print("  list (index, prime, gap):")
for j,i in enumerate(rec_idx, start=1):
    print(f"    #{j:2d}  n={i:<9d} p={p(int(i)):<12d} g={int(G[i-1])}")

# ---- float64 T for bulk statistics ----
n_all = np.arange(1, len(P)+1, dtype=np.float64)
Pf = P.astype(np.float64)
Tf = Pf*np.expm1(np.log(Pf)/n_all)

M = len(G)   # indices n = 1..M have a gap
# governing record index r(n)
rec_pos = np.searchsorted(rec_idx, np.arange(1, M+1), side='right')-1
r = rec_idx[rec_pos]
# minimal dominating index mu(n) = min{j : g_j >= g_n}; it is a record index
recg = G[rec_idx-1]
mu = rec_idx[np.searchsorted(recg, G[:M], side='left')]

print("\n=== P6'-gov / P6'-min margins (float64) ===")
for lim in (3*10**6, 10**7, 10**8, 2*10**8):
    k = int(np.searchsorted(P[:M], lim))
    idx = np.arange(1, k+1)
    govm = Tf[idx-1] - Tf[r[:k]-1]
    minm = Tf[idx-1] - Tf[mu[:k]-1]
    nz = r[:k] != idx     # non-record indices (gov non-trivial)
    a = govm[nz].min(); ia = idx[nz][govm[nz].argmin()]
    b = minm.min();     ib = idx[minm.argmin()]
    print(f"  p<{lim:>11}: gov min = {a:.10g} at n={ia} (p={p(int(ia))}), exceptions={int((govm[nz]<0).sum())}"
          f" | min-pred min = {b:.10g} at n={ib} (p={p(int(ib))}, mu={int(mu[ib-1])}), exceptions={int((minm<0).sum())}")

# ---- P6'-pair : for each n, max_{m <= r(n-1)} T_m  vs T_n ----
print("\n=== P6'-pair exception census (float64 screen, mpmath confirm) ===")
runmaxT = np.maximum.accumulate(Tf)
# admissible m for n : exists record j with m <= j < n  <=>  m <= R(n) := last record index < n
Rn = np.empty(M+1, dtype=np.int64)
prev = 0
recset = set(int(i) for i in rec_idx)
last = 0
Rlist = np.zeros(M+2, dtype=np.int64)
for n in range(1, M+1):
    Rlist[n] = last
    if n in recset: last = n
adm = Rlist[1:M+1]
ok = adm > 0
ns = np.nonzero(ok)[0]+1
bad = ns[runmaxT[adm[ok]-1] > Tf[ns-1]]
print("  admissible n (p<2e8):", int(ok.sum()), " violating n:", len(bad))
print("  violating n:", [int(x) for x in bad])
if len(bad):
    worst = None
    for n in bad:
        n = int(n); m = int(np.argmax(Tf[:adm[n-1]]))+1
        d = T(m)-T(n)
        if worst is None or d > worst[0]: worst = (d, m, n)
    print("  worst margin (mpmath):", mp.nstr(worst[0],10), "at m=",worst[1],"n=",worst[2])

# ---- P6'-rec ----
Trec = Tf[rec_idx-1]
print("\n=== P6'-rec (T along consecutive records) ===")
print("  record steps:", len(rec_idx)-1, " decreasing steps:", int((np.diff(Trec)<0).sum()))
print("  T_mu <= T_r exceptions:", int((Tf[mu-1] > Tf[r-1]).sum()), "of", M)

# ---- 55.92% statistic ----
print("\n=== T_{n+1} < T_n fractions ===")
dec = Tf[1:] < Tf[:-1]
for lim in (3*10**6, 10**7, 10**8):
    k = int(np.searchsorted(P, lim))          # primes below lim
    steps_all = k-1
    print(f"  N={lim:>11}: pi={k}  all-n {int(dec[:steps_all].sum())}/{steps_all}"
          f" = {100*dec[:steps_all].sum()/steps_all:.4f}%   n>=10 {int(dec[9:steps_all].sum())}/{steps_all-9}"
          f" = {100*dec[9:steps_all].sum()/(steps_all-9):.4f}%")

# ---- max prime gaps below thresholds ----
print("\n=== max prime gap g_m over p_m < X ===")
for X in (468049, 1772201, 6690557, 10**8, 2*10**8):
    k = int(np.searchsorted(P[:M], X))
    j = int(G[:k].argmax())
    print(f"  X={X:>11}: g={int(G[j])} at p={p(j+1)}")

# ---- S-breaches ----
Lf = np.log(Pf[:M]); S = Lf*Lf - Lf - 1.17
br = np.nonzero(G >= S)[0]+1
print("\n=== S-breaches (g_k >= L^2-L-1.17), p<2e8 ===", [int(x) for x in br])
print("  max{g_j : j<=9} =", int(G[:9].max()), " S(29)=", mp.nstr(log(mpf(29))**2-log(mpf(29))-mpf('1.17'),8))

# ---- largest n with T_n <= S(p_n) ----
k3 = int(np.searchsorted(P[:M], 3*10**6))
w = np.nonzero(Tf[:k3] <= S[:k3])[0]
print("  largest n with T_n <= L^2-L-1.17 below 3e6: n=", int(w[-1])+1, " p=", p(int(w[-1])+1))

# ---- RH doc: Theorem A table, C_n, ratios, p*(C) ----
print("\n=== RH Theorem A-degree table ===")
for n in (1,2,3,4,5,6,7,8,9,10):
    x = mpf(p(n)); L = log(x); Tn = T(n); Bn = mpf(22)/25*mp.sqrt(x)*L
    print(f"  n={n:2d} p={p(n):3d} T={mp.nstr(Tn,11)} B={mp.nstr(Bn,11)} L^2={mp.nstr(L*L,11)}"
          f" T<L^2:{Tn<L*L} B<T:{Bn<Tn} C_n={mp.nstr(Tn/(mp.sqrt(x)*L),8)}")
k3 = int(np.searchsorted(P, 3*10**6))
Bf = 0.88*np.sqrt(Pf[:k3])*np.log(Pf[:k3])
ratio = Bf/Tf[:k3]
sub = ratio[3:]
print("  min B/T over 4<=n<=pi(3e6):", f"{sub.min():.12f}", "at n=", int(sub.argmin())+4, " (pi(3e6)=",k3,")")
print("  steps n>=4 with ratio falling:", int((np.diff(ratio[3:])<0).sum()), "of", len(ratio)-4)
Cn = Tf[:k3]/(np.sqrt(Pf[:k3])*np.log(Pf[:k3]))
for C,lab in ((1.0,'1'),(0.88,'22/25'),(4/np.pi,'4/pi'),(1/(8*np.pi),'1/(8pi)'),(1e-2,'1e-2')):
    fail = np.nonzero(Cn <= C)[0]
    m = int(fail[0]) if len(fail) else k3   # first index failing; prefix is 1..m
    print(f"  p*({lab}) = {p(m) if m>0 else None}  (prefix size {m})")
