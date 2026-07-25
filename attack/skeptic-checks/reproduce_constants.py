import numpy as np, math
N = 3000000
s = np.ones(N//2, dtype=bool); s[0]=False
for i in range(3,int(N**0.5)+1,2):
    if s[i//2]: s[i*i//2::i]=False
pr = np.concatenate(([2],2*np.nonzero(s)[0]+1)).astype(np.int64)
g=np.diff(pr); p=pr[:-1]; idx=np.arange(1,len(p)+1,dtype=np.int64)
L=np.log(p.astype(float)); T=p.astype(float)*np.expm1(L/idx)

# 1. down-steps with NO n>=10 cut
down_all = int((T[1:]<T[:-1]).sum())
print("1. down-steps ALL n: %d / %d = %.4f%%"%(down_all,len(T)-1,100*down_all/(len(T)-1)))

# 2. S-breaches  g_k >= L^2-L-1.17
S = L*L - L - 1.17
print("2. S-breaches k:", (idx[g>=S]).tolist())

# 3. max gaps below thresholds
for X in (60184, 1772201):
    m = p < X
    print("3. max gap below %d = %d at p=%d"%(X, g[m].max(), p[m][g[m].argmax()]))

# 4. Lemma3 slack min over p>=60184
m = p>=60184
sl = T[m]-L[m]*(L[m]-1.1)
print("4. min(T - L(L-1.1)) for p>=60184: %.9f at p=%d"%(sl.min(), p[m][sl.argmin()]))

# 5. Theorem C(a) d*
l0=math.log(60184)
def dstar(l): return (0.1*l+(l*l-l)**2*math.exp(-l))/(2*l-1.1)
ls=np.linspace(l0,400,400000); ds=np.array([dstar(x) for x in ls])
print("5. Dusart d* max = %.6f at l=%.5f  (l0=%.5f, d*(l0)=%.6f)"%(ds.max(),ls[ds.argmax()],l0,dstar(l0)))
l1=math.log(1772201)
def dstarA(l): return (0.17-1/l+l**4*math.exp(-l))/(2*l-1)
ls2=np.linspace(l1,200,200000); ds2=np.array([dstarA(x) for x in ls2])
print("5b. Axler d* max = %.6f at l=%.5f (l1=%.5f)"%(ds2.max(),ls2[ds2.argmax()],l1))

# 6. misclassification of T-increase rule at L-t
y = (pr[1:].astype(float))  # p_{n+1}
inc = T[1:]>=T[:-1]
for t in (0,1,2,3):
    pred = g[:-1] >= (L[:-1]-t)
    print("6. t=%d mis=%.4f%%"%(t,100*np.mean(pred!=inc)))

# 7. S(g) threshold
def Sg(gg): return math.exp((1.1+math.sqrt(1.21+4*gg))/2)
def Sk(gg): return math.exp((1+math.sqrt(1+4*(gg+1.17)))/2)
X=2**64
gg=2
while Sg(gg+2)<=X: gg+=2
print("7. largest even g with S(g)<=2^64 (Dusart):",gg, "S(g)=%.5g S(g+2)=%.5g"%(Sg(gg),Sg(gg+2)))
gg=2
while Sk(gg+2)<=X: gg+=2
print("7b. same under L^2-L-1.17:",gg)
Lx=math.log(X); print("7c. L(L-1.1) at 2^64 = %.10f ; L^2-L-1 = %.4f"%(Lx*(Lx-1.1), Lx*Lx-Lx-1))

# 9. max rho n>=10
rho=g/T; m=idx>=10
j=np.argmax(rho[m]); print("9. max rho (n>=10) = %.7f at n=%d p=%d g=%d"%(rho[m][j],idx[m][j],p[m][j],g[m][j]))
print("9b. max rho all n = %.6f at n=%d ; rho_2=%.6f rho_4=%.6f"%(rho.max(),idx[rho.argmax()],rho[1],rho[3]))

# 10. safety factor for gap first occurrences
first={}
for gv in np.unique(g):
    gv=int(gv); i=int(np.argmax(g==gv)); first[gv]=int(p[i])
best=None
for gv,P1 in first.items():
    if gv<2: continue
    S_=Sg(gv)
    if S_<60184: continue
    r=P1/S_
    if best is None or r<best[0]: best=(r,gv,P1,S_)
print("10. min safety factor P1(g)/S(g) = %.4f at g=%d P1=%d S=%.5g"%best)
print("10b. P1(112)=",first.get(112),"S(112)=%.6g"%Sg(112))
