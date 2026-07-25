import math
N = 3_000_000
sieve = bytearray([1])*(N+1); sieve[0]=sieve[1]=0
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=bytearray(len(sieve[i*i::i]))
p=[i for i in range(N+1) if sieve[i]]
print("primes:",len(p),"last:",p[-1])

# check p_{n+1}^n < p_n^{n+1}  via logs (n is 1-indexed: p[0]=p_1)
worst=None; worst_csg=None
for i in range(len(p)-1):
    n=i+1
    pn=p[i]; pn1=p[i+1]
    lhs=n*math.log(pn1); rhs=(n+1)*math.log(pn)
    if lhs>=rhs: print("VIOLATION at n=",n,pn,pn1); break
    # margin ratio: how close  (want ratio<1)
    r=lhs/rhs
    if worst is None or r>worst[0]: worst=(r,n,pn,pn1)
    # CSG-style: g_n / T_n where T_n = pn*(exp(log pn / n)-1)
    L=math.log(pn); T=pn*math.expm1(L/n); g=pn1-pn
    c=g/T
    if worst_csg is None or c>worst_csg[0]: worst_csg=(c,n,pn,g,T)
print("no violation up to n =",len(p)-1)
print("max ratio n*log p_{n+1} / ((n+1) log p_n):",worst)
print("max g_n/T_n:",worst_csg)
# also Cramer-Shanks-Granville ratio g/(log p)^2
w=max(((p[i+1]-p[i])/math.log(p[i])**2, i+1, p[i], p[i+1]-p[i]) for i in range(len(p)-1))
print("max g/(log p)^2:",w)
# smooth-model threshold check: T_n vs L^2-L-1
for n in [10,100,10000,100000,len(p)-1]:
    pn=p[n-1]; L=math.log(pn); T=pn*math.expm1(L/n)
    print(f"n={n} p_n={pn} T_n={T:.4f}  L^2-L-1={L*L-L-1:.4f}")
