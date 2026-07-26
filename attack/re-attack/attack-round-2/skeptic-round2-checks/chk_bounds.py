import numpy as np
N=10**8
s=np.ones(N//2,dtype=bool); s[0]=False
for i in range(1,int(N**0.5)//2+1):
    if s[i]:
        p=2*i+1; s[(p*p)//2::p]=False
P=np.empty(int(s.sum())+1,dtype=np.int64); P[0]=2; P[1:]=2*np.nonzero(s)[0].astype(np.int64)+1
del s
print("pi(1e8)=",len(P), " pi(60184)=",int(np.searchsorted(P,60184)))
x=P.astype(np.float64); n=np.arange(1,len(P)+1,dtype=np.float64); L=np.log(x)
T=x*np.expm1(L/n)
# Axler upper bound (post-corrigendum statement): pi(x) < x/(L-1-1.17/L)
ub = x/(L-1-1.17/L)
ce = np.nonzero(n>=ub)[0]
print("Axler-upper counterexamples at x=p_n below 1e8:",len(ce), "smallest p=",int(P[ce[0]]),"n=",ce[0]+1,
      "largest p=",int(P[ce[-1]]))
print("  all below 2634800823?", bool(P[ce].max()<2634800823))
# Axler lower rows: pi(x) > x/(L-1-1/L-a/L^2) for x>=x0
for a,x0 in ((1,1772201),(2.1,6690557),(0,468049)):
    m=x>=x0
    lb=x[m]/(L[m]-1-1/L[m]-a/L[m]**2)
    print(f"  Axler lower (a={a}, x0={x0}): failures =",int((n[m]<=lb).sum()))
# (D-low): T_n > L^2-1.1L for p>=60184 ; (D-high): T_n <= v(1+v/x), v=L^2-L for p>=5393
m=x>=60184; print("  (D-low) failures:",int((T[m]<=L[m]**2-1.1*L[m]).sum()))
m=x>=5393; v=L[m]**2-L[m]; print("  (D-high) failures:",int((T[m]>v*(1+v/x[m])).sum()))
m=x>=6690557; v=L[m]**2-L[m]-1-2.1/L[m]; print("  (A-high') failures:",int((T[m]>v*(1+v/x[m])).sum()))
m=x>=1772201; v=L[m]**2-L[m]-1-1/L[m]; print("  (A-high*) failures:",int((T[m]>=v*(1+v/x[m])).sum()))
# Lemma 3 slack min on [60184, 2e6]
m=(x>=60184)&(x<=2*10**6); sl=T[m]-(L[m]**2-1.1*L[m])
print("  min T-B on [60184,2e6] =",f"{sl.min():.9f}","at p=",int(x[m][sl.argmin()]))
# Dusart 6.6 upper pi(x)<=x/(L-1.1) at primes in [60184,2e6]
m=(x>=60184)&(x<=2*10**6); print("  Dusart 6.6 upper failures:",int((n[m]>x[m]/(L[m]-1.1)).sum()))
# max gap below 60184
G=np.diff(P); k=int(np.searchsorted(P[:-1],60184)); j=int(G[:k].argmax())
print("  G0 = max gap p<60184:",int(G[j]),"at p=",int(P[j]))
