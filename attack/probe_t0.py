"""Numerical probe for proof-attempt-0: first-failure maximality.
Sieve to 3e6, 1-indexed primes.  Everything recomputed here."""
import math

N = 3_000_000
sieve = bytearray([1])*(N+1); sieve[0]=sieve[1]=0
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
P = [i for i in range(N+1) if sieve[i]]
NP = len(P)
print(f"primes to {N}: {NP}, largest {P[-1]}")

# 1-indexed: p_n = P[n-1]
def p(n): return P[n-1]
L = [math.log(x) for x in P]
g = [P[i+1]-P[i] for i in range(NP-1)]        # g[i] = g_{i+1}
T = [P[i]*math.expm1(L[i]/(i+1)) for i in range(NP)]   # T[i] = T_{i+1}

# ---- (0) no violation of F
viol = [i+1 for i in range(NP-1) if g[i] >= T[i]]
print("F violations:", viol[:5], "count", len(viol))

# ---- (1) S(x) = L^2 - L - 1.17 monotone; no S-breach in range?
def S(x):
    l = math.log(x); return l*l - l - 1.17
Sb = [i+1 for i in range(NP-1) if g[i] >= S(P[i])]
print("S-breaches (g_k >= L^2-L-1.17):", Sb[:20], "count", len(Sb))

# ---- (2) Lemma M sanity: first S-breach is a strict record?
maxg = 0; recs = []
for i in range(NP-1):
    if g[i] > maxg: maxg = g[i]; recs.append(i+1)
print("record indices count:", len(recs), "first 8:", recs[:8])
Sb10 = [k for k in Sb if k > 9]
print("S-breaches with k>9:", Sb10[:20], "count", len(Sb10))
print("max gap over m<=9:", max(g[:9]), " S(p_10)=S(29)=", S(29))
print("S(p_k) for k=10..14:", [round(S(P[k-1]),4) for k in range(10,15)])

# ---- (3) where does T_n > L^2-L-1.17 hold? and T_n < L^2-L-1 ?
lo_fail = [i+1 for i in range(NP) if T[i] <= L[i]**2 - L[i] - 1.17]
hi_fail = [i+1 for i in range(NP) if T[i] >= L[i]**2 - L[i] - 1.0]
print("T_n <= L^2-L-1.17 at n:", lo_fail[:12], "... count", len(lo_fail),
      "max such n", max(lo_fail) if lo_fail else None)
print("T_n >= L^2-L-1 at n: count", len(hi_fail), "max such n", max(hi_fail) if hi_fail else None,
      " p there", p(max(hi_fail)) if hi_fail else None)

# ---- (4) record-block monotonicity of T (reproduce the 0/216815 claim)
exc = 0; pairs = 0; worst = 0.0
gov = 0  # index (1-based) of governing record
ri = 0
for n in range(1, NP):           # n indexes gaps 1..NP-1
    if ri+1 < len(recs) and recs[ri+1] <= n: ri += 1
    gov = recs[ri]
    pairs += 1
    if T[n-1] < T[gov-1]:
        exc += 1
        worst = max(worst, T[gov-1]-T[n-1])
print(f"record-block pairs {pairs}, T_n < T_gov exceptions {exc}, worst drawdown {worst:.4f}")

# ---- (5) the exact first-order criterion:  T_m <= T_n  <->  k <= y*(1+1/L)*pi(p_m)/p_m
import random
random.seed(1)
ok=0; tot=0
for _ in range(20000):
    m = random.randrange(1000, NP-1); n = m + random.randrange(1, 400)
    if n >= NP: continue
    y = p(n)-p(m); k = n-m
    lhs = (T[m-1] <= T[n-1])
    rhs = (k <= y*(1+1/L[m-1])*(m/p(m)))
    tot+=1; ok += (lhs==rhs)
print(f"first-order criterion agreement: {ok}/{tot} = {ok/tot:.4%}")

# ---- (6) window widths
for lam in (21.7, math.log(2**64), 50.0, 100.0):
    d_ax = (0.17 - 1/lam)/(2*lam-1)
    d_du = (0.1*lam)/(2*lam-1.1)
    print(f"L={lam:8.4f}  axler window d*={d_ax:.6g} (rel {1-math.exp(-d_ax):.4%})"
          f"   dusart d*={d_du:.6g} (rel {1-math.exp(-d_du):.4%})")

# ---- (7) Cramer heuristic residual: expected # of m in window with g_m >= T_n
for lam in (math.log(2**64), 50.0, 100.0):
    x = math.exp(lam); d = (0.17-1/lam)/(2*lam-1)
    W = x*(1-math.exp(-d))
    expected = (W/lam)*math.exp(-(lam*lam-lam-1.17)/lam)
    print(f"L={lam:.4f}: window length {W:.4g}, expected competing gaps {expected:.4g}, 0.085/L^2={0.085/lam**2:.4g}")
