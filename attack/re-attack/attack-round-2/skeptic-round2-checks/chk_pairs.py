import numpy as np
N=3*10**8
s=np.ones(N//2,dtype=bool); s[0]=False
for i in range(1,int(N**0.5)//2+1):
    if s[i]:
        p=2*i+1; s[(p*p)//2::p]=False
P=np.empty(int(s.sum())+1,dtype=np.int64); P[0]=2; P[1:]=2*np.nonzero(s)[0].astype(np.int64)+1
del s
print("pi(3e8)=",len(P))
Pf=P.astype(np.float64); nn=np.arange(1,len(P)+1,dtype=np.float64)
Tf=Pf*np.expm1(np.log(Pf)/nn); Lf=np.log(Pf)
G=np.diff(P); M=len(G)
run=np.maximum.accumulate(G); isrec=np.empty(M,bool); isrec[0]=True; isrec[1:]=G[1:]>run[:-1]
rec=np.nonzero(isrec)[0]+1
# last record index strictly < n
Rl=np.zeros(M+1,dtype=np.int64); last=0; rs=set(int(x) for x in rec)
for n in range(1,M+1):
    Rl[n]=last
    if n in rs: last=n
adm=Rl[1:M+1]; runmax=np.maximum.accumulate(Tf)
ok=adm>0; ns=np.nonzero(ok)[0]+1
bad=ns[runmax[adm[ok]-1]>Tf[ns-1]]
print("violating n below 3e8:",len(bad), [int(x) for x in bad])
tot=0
for n in bad:
    n=int(n); cnt=int((Tf[:adm[n-1]]>Tf[n-1]).sum()); tot+=cnt
    print("   n=",n,"admissible m up to",int(adm[n-1]),"violating m count =",cnt)
print("TOTAL violating (m,n) PAIRS below 3e8:",tot)
# T_n < L_n^2 exception set
ex=np.nonzero(Tf[:M]>=Lf[:M]*Lf[:M])[0]+1
print("n with T_n >= L_n^2 (p<3e8):",[int(x) for x in ex][:40],"count",len(ex))
# step counts
for lim in (3*10**6,10**7,10**8):
    k=int(np.searchsorted(P,lim)); st=k-1
    dec=Tf[1:k]<Tf[:k-1]
    print(f"N={lim}: pi={k} steps(all n)={st} dec={int(dec.sum())}; steps(n>=10)={st-9} dec={int(dec[9:].sum())}")
