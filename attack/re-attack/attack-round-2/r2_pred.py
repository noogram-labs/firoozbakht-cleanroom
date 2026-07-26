"""Round-2: the three predicates, with the trivial self-pair excluded, and (C)
formalised exactly as card L15's prose reads it."""
import numpy as np

def sieve(N):
    s = np.ones(N + 1, dtype=bool); s[:2] = False
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]: s[i*i::i] = False
    return np.flatnonzero(s)

def run(N):
    P = sieve(N).astype(np.int64); K = len(P)
    n = np.arange(1, K+1, dtype=np.float64); Pf = P.astype(np.float64)
    T = Pf * np.expm1(np.log(Pf)/n)
    g = np.diff(P).astype(np.int64); M = K-1
    runmax = np.maximum.accumulate(g)
    is_rec = np.empty(M, bool); is_rec[0]=True; is_rec[1:] = g[1:] > runmax[:-1]
    rec = np.flatnonzero(is_rec)                     # 0-based
    recvals = g[rec]

    # --- (A) P6'-gov : m(n) = largest record index <= n ; exclude m(n)=n
    gov = np.zeros(M, np.int64); cur=-1; ptr=0
    for k in range(M):
        if ptr < len(rec) and rec[ptr]==k: cur=rec[ptr]; ptr+=1
        gov[k]=cur
    okA = gov < np.arange(M)
    mA = T[:M]-T[gov]
    jA = int(np.argmin(np.where(okA, mA, np.inf)))
    print(f"  (A) P6'-gov  exc={int(((mA<0)&okA).sum())}/{int(okA.sum())}  "
          f"min={mA[jA]:.6e} at n={jA+1}, p={P[jA]}")

    # --- (B) P6'-min : m(n) = min{m : g_m >= g_n} ; exclude m(n)=n
    pos = np.searchsorted(recvals, g, side='left'); mmin = rec[pos]
    okB = mmin < np.arange(M)
    mB = T[:M]-T[mmin]
    jB = int(np.argmin(np.where(okB, mB, np.inf)))
    print(f"  (B) P6'-min  exc={int(((mB<0)&okB).sum())}/{int(okB.sum())}  "
          f"min={mB[jB]:.6e} at n={jB+1}, p={P[jB]}, m={mmin[jB]+1}, p_m={P[mmin[jB]]}")

    # --- (C) P6'-pair : for all m<n with a record index r, m<=r<n : T_m<=T_n
    #     tightest over m is max{T_m : m<=r},  r = largest record index < n
    lastrec = np.full(M, -1, np.int64); cur=-1; ptr=0
    for k in range(M):
        lastrec[k]=cur
        if ptr < len(rec) and rec[ptr]==k: cur=rec[ptr]; ptr+=1
    pref = np.maximum.accumulate(T[:M])
    okC = lastrec >= 0
    mC = T[:M] - np.where(okC, pref[np.maximum(lastrec,0)], -np.inf)
    jC = int(np.argmin(np.where(okC, mC, np.inf)))
    exc = np.flatnonzero((mC<0)&okC)
    print(f"  (C) P6'-pair exc={len(exc)}/{int(okC.sum())}  "
          f"min={mC[jC]:.6e} at n={jC+1}, p={P[jC]}")
    if len(exc):
        e=exc[:6]
        print(f"      first exceptions n= {[int(x)+1 for x in e]}  p={[int(P[x]) for x in e]}")
        print(f"      largest exception n={int(exc[-1])+1}, p={int(P[exc[-1]])}")

for N in (3_000_000, 10_000_000, 100_000_000):
    print(f"===== N={N:.0e}"); run(N)
