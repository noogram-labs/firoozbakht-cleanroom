"""Round-2 final battery: predicates to 1e9, corrected Theorem C constants."""
import numpy as np, mpmath as mp
mp.mp.dps = 50

def sieve(N):
    s = np.ones(N+1, bool); s[:2]=False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i]=False
    return np.flatnonzero(s)

N = 1_000_000_000
print(f"sieving to {N:.0e} ...", flush=True)
P = sieve(N).astype(np.int64); K=len(P)
print(f"pi({N:.0e}) = {K}", flush=True)
Pf=P.astype(np.float64); n=np.arange(1,K+1,dtype=np.float64)
T = Pf*np.expm1(np.log(Pf)/n)
g = np.diff(P).astype(np.int64); M=K-1
runmax=np.maximum.accumulate(g)
is_rec=np.empty(M,bool); is_rec[0]=True; is_rec[1:]=g[1:]>runmax[:-1]
rec=np.flatnonzero(is_rec); recvals=g[rec]
print(f"records={len(rec)}, largest gap={g.max()} at p={P[int(np.argmax(g))]}")

gov=np.zeros(M,np.int64); cur=-1; ptr=0
for k in range(M):
    if ptr<len(rec) and rec[ptr]==k: cur=rec[ptr]; ptr+=1
    gov[k]=cur
pos=np.searchsorted(recvals,g,side='left'); mmin=rec[pos]
lastrec=np.full(M,-1,np.int64); cur=-1; ptr=0
for k in range(M):
    lastrec[k]=cur
    if ptr<len(rec) and rec[ptr]==k: cur=rec[ptr]; ptr+=1
pref=np.maximum.accumulate(T[:M])

idx=np.arange(M)
okA = gov<idx; mA=T[:M]-T[gov]
jA=int(np.argmin(np.where(okA,mA,np.inf)))
print(f"(A) P6'-gov  exc={int(((mA<0)&okA).sum())}/{int(okA.sum())} min={mA[jA]:.6e} at n={jA+1} p={P[jA]}")
okB = mmin<idx; mB=T[:M]-T[mmin]
jB=int(np.argmin(np.where(okB,mB,np.inf)))
print(f"(B) P6'-min  exc={int(((mB<0)&okB).sum())}/{int(okB.sum())} min={mB[jB]:.6e} at n={jB+1} p={P[jB]} m={mmin[jB]+1} p_m={P[mmin[jB]]}")
okC = lastrec>=0; mC=T[:M]-np.where(okC,pref[np.maximum(lastrec,0)],-np.inf)
exc=np.flatnonzero((mC<0)&okC); jC=int(np.argmin(np.where(okC,mC,np.inf)))
print(f"(C) P6'-pair exc={len(exc)}/{int(okC.sum())} min={mC[jC]:.6e} at n={jC+1} p={P[jC]}")
print(f"    exception indices n={[int(x)+1 for x in exc]}")
print(f"(R) T along records: decreasing steps = {int((np.diff(T[rec])<0).sum())}/{len(rec)-1}")
print(f"    T_mmin > T_gov at {int((T[mmin]>T[gov]).sum())} of {M} indices")

# per-decade minima of the (A) and (B) margins
print("\ndecade    min (A)-margin            min (B)-margin")
for e in range(3,10):
    lo,hi=10**(e-1),10**e
    sel=(Pf[:M]>=lo)&(Pf[:M]<hi)
    a=np.where(sel&okA,mA,np.inf).min(); b=np.where(sel&okB,mB,np.inf).min()
    print(f"1e{e:<2d}   {a: .6e}        {b: .6e}")

for X in (468049, 6690557, 10**8, 10**9):
    sel=Pf[:M]<X
    if sel.sum(): print(f"max gap below {X:>12}: {int(g[sel].max())} at p={int(P[:M][sel][int(np.argmax(g[sel]))])}")

# ---- corrected Theorem C sweeps
print("\n### corrected Theorem C separations (mpmath, 50 dps)")
def d_axler(l, a):
    l=mp.mpf(l); v=l*l-l-1-mp.mpf(a)/l
    C=v*(1+v/mp.e**l)
    return (1+mp.sqrt(1+4*(C+mp.mpf('1.17'))))/2 - l
def d_dusart(l):
    l=mp.mpf(l); v=l*l-l
    C=v*(1+v/mp.e**l)
    # need lam^2 - 1.1 lam >= C
    return (mp.mpf('1.1')+mp.sqrt(mp.mpf('1.21')+4*C))/2 - l
for tag, f, l0 in [("Dusart-only, l>=log(1e8)", d_dusart, mp.log(10**8)),
                   ("Dusart-only, l>=log(60184)", d_dusart, mp.log(60184)),
                   ("Axler a=2.1, l>=log(6690557)", lambda l: d_axler(l,2.1), mp.log(6690557)),
                   ("Axler a=2.1, l>=log(1e8)", lambda l: d_axler(l,2.1), mp.log(10**8)),
                   ("Axler a=1 (arXiv only), l>=log(1772201)", lambda l: d_axler(l,1.0), mp.log(1772201)),
                   ("Axler a=0, l>=log(468049)", lambda l: d_axler(l,0.0), mp.log(468049))]:
    best=(None,mp.mpf(-1))
    l=l0
    while l < 1000:
        d=f(l)
        if d>best[1]: best=(l,d)
        l += mp.mpf(1)/100
    print(f"  {tag:42s} max d* = {mp.nstr(best[1],8)} at l={mp.nstr(best[0],8)}"
          f"   ratio p_m/p_n0 <= {mp.nstr(mp.e**(-best[1]),9)}")
