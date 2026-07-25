# Independent re-verification of the headline numbers quoted in synthesis.md.
# Written from the STATEMENTS, not from any upstream code path.
import math
from sympy import primerange

N = 3_000_000
P = list(primerange(2, N))
print("primes < 3e6:", len(P))

def T(p, n):  # n is 1-indexed rank of p
    return p * (math.exp(math.log(p)/n) - 1)

# --- 55.92% : steps where T decreases ---
Ts = [T(P[i], i+1) for i in range(len(P))]
dec_all = sum(1 for i in range(len(Ts)-1) if Ts[i+1] < Ts[i])
tot_all = len(Ts)-1
dec_10 = sum(1 for i in range(9, len(Ts)-1) if Ts[i+1] < Ts[i])
tot_10 = len(Ts)-1-9
print(f"n>=10 : {dec_10}/{tot_10} = {100*dec_10/tot_10:.4f}%")
print(f"all n : {dec_all}/{tot_all} = {100*dec_all/tot_all:.4f}%")

# --- max rho = g/T ---
best10 = max(((P[i+1]-P[i])/Ts[i], i+1, P[i], P[i+1]-P[i]) for i in range(9, len(P)-1))
bestall = max(((P[i+1]-P[i])/Ts[i], i+1, P[i], P[i+1]-P[i]) for i in range(len(P)-1))
print("max rho n>=10:", best10)
print("max rho all n:", bestall)

# --- violations of F ---
viol = sum(1 for i in range(len(P)-1) if (P[i+1]-P[i]) >= Ts[i])
print("violations of F below 3e6:", viol)

# --- L(L-1.1) at 2^64  (claimed 1919.1379834975...) ---
L = math.log(2**64)
print("L(L-1.1) at 2^64 =", repr(L*(L-1.1)))

# --- S(29) = log^2 - log - 1.17 ; max gap among j<=9 ---
l = math.log(29)
print("S(29) =", l*l - l - 1.17, " max g_j j<=9 =", max(P[i+1]-P[i] for i in range(9)))

# --- CMS envelope (22/25)sqrt(p)log p vs T at n=1,2,3 ---
for n in (1,2,3,4):
    p = P[n-1]
    print(f"n={n} p={p} B={0.88*math.sqrt(p)*math.log(p):.7f} T={T(p,n):.7f} B<T={0.88*math.sqrt(p)*math.log(p) < T(p,n)}")

# --- smooth model: derivative bracket sign at x=4, 4.05, 5 ---
for x in (4, 4.05, 5):
    print("bracket at", x, "=", 1 + 1/math.log(x) - math.log(x) - math.log(math.log(x)))
