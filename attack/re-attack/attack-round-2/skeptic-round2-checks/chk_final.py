import numpy as np
N=2*10**8
s=np.ones(N//2,dtype=bool); s[0]=False
for i in range(1,int(N**0.5)//2+1):
    if s[i]:
        p=2*i+1; s[(p*p)//2::p]=False
P=np.empty(int(s.sum())+1,dtype=np.int64); P[0]=2; P[1:]=2*np.nonzero(s)[0].astype(np.int64)+1
del s
x=P.astype(np.float64); n=np.arange(1,len(P)+1,dtype=np.float64); L=np.log(x)
T=x*np.expm1(L/n); G=np.diff(P); M=len(G)
run=np.maximum.accumulate(G); isrec=np.empty(M,bool); isrec[0]=True; isrec[1:]=G[1:]>run[:-1]
rec=np.nonzero(isrec)[0]+1; recg=G[rec-1]
mu=rec[np.searchsorted(recg,G[:M],side='left')]
marg=T[:M]-T[mu-1]
print("per-decade min of P6'-min margin (non-trivial only):")
lo=2
for d in range(3,9):
    hi=10**d
    sel=(x[:M]>=lo)&(x[:M]<hi)&(mu!=np.arange(1,M+1))
    if sel.sum(): print(f"   [{lo},{hi}) min={marg[sel].min():.6g} at p={int(x[:M][sel][marg[sel].argmin()])}")
    lo=hi
# Axler upper CE smallest with x>=5.43
ub=x/(L-1-1.17/L); ce=np.nonzero((n>=ub)&(x>=5.43))[0]
print("Axler-upper CE with x>=5.43 below 1e8:", int(((n>=ub)&(x>=5.43)&(x<1e8)).sum()),
      " smallest p=",int(P[ce[0]]),"n=",ce[0]+1)
print("record #: 191912783 is number", int(np.searchsorted(P[rec-1],191912783))+1, "of", len(rec))
