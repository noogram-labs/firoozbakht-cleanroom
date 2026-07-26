import numpy as np
from mpmath import mp, mpf, log, exp
mp.dps = 40

# ---- (1) segmented sieve: max prime gap below 1.4e9 ----
LIM = 1_400_000_000
base = int(LIM**0.5)+1
sb = np.ones(base//2+1, dtype=bool); sb[0]=False
for i in range(1, int(base**0.5)//2+1):
    if sb[i]:
        p=2*i+1; sb[(p*p)//2::p]=False
small = np.concatenate(([2], 2*np.nonzero(sb)[0].astype(np.int64)+1))
print("base primes:", len(small), small[-1])

SEG = 20_000_000
prev = 2; best=(0,0); recs=[]
lo = 3
while lo < LIM:
    hi = min(lo+SEG, LIM)
    n = (hi-lo)//2                      # odds lo, lo+2, ...
    seg = np.ones(n, dtype=bool)
    for p in small[1:]:
        if p*p >= hi: break
        st = max(p*p, ((lo+p-1)//p)*p)
        if st % 2 == 0: st += p
        if st < hi: seg[(st-lo)//2::p] = False
    pr = lo + 2*np.nonzero(seg)[0].astype(np.int64)
    if len(pr):
        allp = np.concatenate(([prev], pr))
        g = np.diff(allp)
        j = int(g.argmax())
        if g[j] > best[0]: best = (int(g[j]), int(allp[j]))
        # running maximal-gap records
        for k in np.nonzero(g > np.maximum.accumulate(np.concatenate(([0],g[:-1]))))[0]:
            pass
        prev = int(pr[-1])
    lo = hi
print("max prime gap with p < 1.4e9 :", best, " (UVR claims 288 at 1294268491 below 1.332e9)")

# recompute max gap restricted to p < 1332022974
LIM2 = 1_332_022_974
prev=2; best2=(0,0); lo=3
while lo < LIM2:
    hi = min(lo+SEG, LIM2)
    n=(hi-lo)//2; seg=np.ones(n,dtype=bool)
    for p in small[1:]:
        if p*p>=hi: break
        st=max(p*p, ((lo+p-1)//p)*p)
        if st%2==0: st+=p
        if st<hi: seg[(st-lo)//2::p]=False
    pr = lo+2*np.nonzero(seg)[0].astype(np.int64)
    if len(pr):
        allp=np.concatenate(([prev],pr)); g=np.diff(allp); j=int(g.argmax())
        if g[j]>best2[0]: best2=(int(g[j]), int(allp[j]))
        prev=int(pr[-1])
    lo=hi
print("max prime gap with p < 1 332 022 974 :", best2)
