"""Round-2: (i) direct test of Axler's upper bound Cor 3.4 last clause in both
its pre- and post-corrigendum ranges; (ii) T along record indices; (iii) the
corrected Theorem C(b) separation sweep."""
import numpy as np, mpmath as mp
mp.mp.dps = 50

def sieve(N):
    s = np.ones(N+1, bool); s[:2]=False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i]=False
    return np.flatnonzero(s)

N = 100_000_000
P = sieve(N).astype(np.int64); K=len(P)
Pf = P.astype(np.float64); n = np.arange(1,K+1,dtype=np.float64)
L = np.log(Pf)
T = Pf*np.expm1(L/n)

print("### 1. Axler Cor 3.4 (published) / 3.5 (arXiv), last clause:")
print("###    pi(x) < x/(log x - 1 - 1.17/log x)   -- arXiv range x>=5.43, corrigendum x>=2634800823")
# test at x = p (pi(p)=n). Bound is an upper bound on pi.
den = L - 1 - 1.17/L
rhs = Pf/den
bad = np.flatnonzero((den>0) & (n >= rhs) & (Pf>=5.43))
print(f"  counterexamples to the x>=5.43 form, x=p_n <= 1e8 : {len(bad)}")
if len(bad):
    print(f"  smallest p : {P[bad[0]]} (n={bad[0]+1});  largest p <=1e8 : {P[bad[-1]]} (n={bad[-1]+1})")
print(f"  => the pre-corrigendum range 5.43 is FALSE; the corrigendum's 2634800823 is not contradicted"
      f" (all counterexamples below it: {bool(P[bad].max() < 2_634_800_823) if len(bad) else 'n/a'})")

print("\n### 2. Axler Cor 3.5 (published) / 3.6 (arXiv), lower bounds, tested at x=p_n<=1e8")
for a,x0,tag in [(1.0,1772201,'a=1  (arXiv-only column)'),
                 (2.1,6690557,'a=2.1 (both editions)'),
                 (0.0, 468049,'a=0  (both editions)')]:
    d = L - 1 - 1/L - a/(L*L)
    f = np.flatnonzero((Pf>=x0) & (d>0) & (n <= Pf/d))
    print(f"  {tag:26s} x0={x0:>9d} : failures={len(f)}")

print("\n### 3. Is T nondecreasing along maximal-gap record indices?")
g = np.diff(P).astype(np.int64); M=K-1
runmax=np.maximum.accumulate(g)
is_rec=np.empty(M,bool); is_rec[0]=True; is_rec[1:]=g[1:]>runmax[:-1]
rec=np.flatnonzero(is_rec)
Tr = T[rec]
drops = np.flatnonzero(np.diff(Tr) < 0)
print(f"  records={len(rec)}; T decreasing between consecutive records at {len(drops)} of {len(rec)-1} steps")
for i in rec[:0]: pass
print("  T at records:", " ".join(f"{x:.4g}" for x in Tr))

print("\n### 4. Does (A) imply (B) pointwise, i.e. T_{m_min(n)} <= T_{gov(n)} always?")
recvals=g[rec]
pos=np.searchsorted(recvals,g,side='left'); mmin=rec[pos]
gov=np.zeros(M,np.int64); cur=-1; ptr=0
for k in range(M):
    if ptr<len(rec) and rec[ptr]==k: cur=rec[ptr]; ptr+=1
    gov[k]=cur
viol = np.flatnonzero(T[mmin] > T[gov])
print(f"  indices with T_{{m_min}} > T_{{gov}} : {len(viol)} / {M}")
print(f"  (so on this range (A) at n plus this fact gives (B) at n)")

print("\n### 5. Theorem C(b): required separation d*(l), corrected (tight) lemma")
print("    T_n <= v(1+v/x), v = l^2-l-1-a/l  from Axler lower bd with parameter a")
print("    T_n0 > lam^2-lam-1.17 (Axler Cor 3.4 post-corrigendum, x>=2634800823)")
def dstar(lam_l, a):
    """minimal d>0 with v(1+v/e^l) <= (l+d)^2-(l+d)-1.17 ; v=l^2-l-1-a/l"""
    l = mp.mpf(lam_l); v = l*l-l-1-mp.mpf(a)/l
    C = v*(1+v/mp.e**l)
    # solve (l+d)^2-(l+d)-1.17 = C
    disc = 1+4*(C+mp.mpf('1.17'))
    lam = (1+mp.sqrt(disc))/2
    return lam-l
for a,x0,tag in [(1.0,1772201,'a=1  arXiv-only'),
                 (2.1,6690557,'a=2.1 both editions'),
                 (0.0, 468049,'a=0  both editions')]:
    l0 = mp.log(x0)
    # also must be >= log(2634800823) for the n0 side? no: l is L_m, lam=L_n0>44.36
    best=None
    ls = [l0 + mp.mpf(i)/50 for i in range(0, 40000)]
    for l in ls:
        d = dstar(l,a)
        if best is None or d>best[1]: best=(l,d)
    print(f"  {tag:22s} l1=log({x0})={float(l0):.5f} : max d* = {mp.nstr(best[1],8)} at l={mp.nstr(best[0],8)}"
          f"  -> p_m <= {mp.nstr(mp.e**(-best[1]),8)} p_n0")

print("\n### 6. PA-0's printed (A-high) with the l^4/x factor -- required d*")
def dstar_printed(lam_l):
    l = mp.mpf(lam_l); v = l*l-l-1-1/l
    C = v*(1+l**4/mp.e**l)
    disc = 1+4*(C+mp.mpf('1.17'))
    return (1+mp.sqrt(disc))/2 - l
l1 = mp.log(1772201)
for l in [l1, mp.mpf(16), mp.mpf(18), mp.mpf(20), mp.mpf('44.36')]:
    print(f"  l={mp.nstr(l,7)}  printed-lemma d* = {mp.nstr(dstar_printed(l),7)}   tight d* = {mp.nstr(dstar(l,1.0),7)}")
