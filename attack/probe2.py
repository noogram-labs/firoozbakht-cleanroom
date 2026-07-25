import math
N=3_000_000
sieve=bytearray([1])*(N+1); sieve[0]=sieve[1]=0
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=bytearray(len(sieve[i*i::i]))
p=[i for i in range(N+1) if sieve[i]]
best=[]
for i in range(9,len(p)-1):   # n>=10
    n=i+1; pn=p[i]; g=p[i+1]-pn; L=math.log(pn)
    T=pn*math.expm1(L/n)
    best.append((g/T,n,pn,g,T,g/(L*L)))
best.sort(reverse=True)
for b in best[:6]:
    print(f"g/T={b[0]:.6f} n={b[1]} p_n={b[2]} g={b[3]} T={b[4]:.3f} g/L^2={b[5]:.4f}")
# maximal gaps (records) in range
rec=0; recs=[]
for i in range(len(p)-1):
    g=p[i+1]-p[i]
    if g>rec: rec=g; recs.append((i+1,p[i],g))
print("num record gaps:",len(recs),"last:",recs[-3:])
# is T monotone along n?
dec=0
for i in range(9,len(p)-2):
    n=i+1;pn=p[i];L=math.log(pn);T1=pn*math.expm1(L/n)
    pn2=p[i+1];L2=math.log(pn2);T2=pn2*math.expm1(L2/(n+1))
    if T2<T1: dec+=1
print("steps where T decreases (n>=10):",dec,"of",len(p)-11)
