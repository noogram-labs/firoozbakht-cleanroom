import math
N=3_000_000
sv=bytearray([1])*(N+1); sv[0]=sv[1]=0
for i in range(2,int(N**0.5)+1):
    if sv[i]: sv[i*i::i]=bytearray(len(sv[i*i::i]))
P=[i for i in range(N+1) if sv[i]]; NP=len(P)
L=[math.log(x) for x in P]
T=[P[i]*math.expm1(L[i]/(i+1)) for i in range(NP)]

# Dusart-only two-sided bounds on T, in their stated ranges
badlo=[i+1 for i in range(NP) if P[i]>=60184 and T[i] <= L[i]**2-1.1*L[i]]
badhi=[i+1 for i in range(NP) if P[i]>=5393  and T[i] >= (L[i]**2-L[i])*(1+(L[i]**2-L[i])/P[i])]
print("Dusart lower T>L^2-1.1L  failures (x>=60184):",len(badlo))
print("Dusart upper T<(L^2-L)(1+..) failures (x>=5393):",len(badhi))
# how tight
for n in (10**4,10**5,216815):
    l=L[n-1]; print(f"n={n} p={P[n-1]} T={T[n-1]:.4f}  L^2-1.1L={l*l-1.1*l:.4f}  L^2-L={l*l-l:.4f}"
                    f"  L^2-L-1.17={l*l-l-1.17:.4f}  L^2-L-1={l*l-l-1:.4f}")

# Axler-derived bounds, only above their validity ranges -- unreachable in range; report the crossovers
lo=[i+1 for i in range(NP) if T[i]<=L[i]**2-L[i]-1.17]
hi=[i+1 for i in range(NP) if T[i]>=L[i]**2-L[i]-1]
print("largest n with T<=L^2-L-1.17 :",max(lo),"p=",P[max(lo)-1],"(Axler Cor3.5 range x>=2634800823 -> not contradicted)")
print("largest n with T>=L^2-L-1    :",max(hi),"p=",P[max(hi)-1],"(Axler Cor3.6 range x>=1772201  -> not contradicted)")

# Brun-Titchmarsh shortfall in the residual window
for lam in (math.log(2**64),50.,100.,200.):
    x=math.exp(lam); d=(0.17-1/lam)/(2*lam-1); y=x*(1-math.exp(-d))
    need = y/(lam-2)            # count we must not exceed (first-order)
    bt   = 2*y/math.log(y)      # Brun-Titchmarsh
    pnt  = y/lam                # expected
    print(f"L={lam:7.3f}: y={y:.3g}  needed<= {need:.4g}  PNT {pnt:.4g}  BT {bt:.4g}   BT/needed={bt/need:.4f}  needed/PNT={need/pnt:.4f}")
