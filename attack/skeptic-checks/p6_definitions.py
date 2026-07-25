import numpy as np, sys

N = int(float(sys.argv[1])) if len(sys.argv)>1 else 10**7
s = np.ones(N//2, dtype=bool); s[0]=False
for i in range(3, int(N**0.5)+1, 2):
    if s[i//2]:
        s[i*i//2::i] = False
primes = np.concatenate(([2], 2*np.nonzero(s)[0]+1)).astype(np.int64)
g = np.diff(primes); p = primes[:-1]
idx = np.arange(1, len(p)+1, dtype=np.int64)
L = np.log(p.astype(np.float64))
T = p.astype(np.float64)*np.expm1(L/idx)
print("primes:", len(primes), "largest p_n with gap:", p[-1])

# record (maximal gap) indices
runmax = np.maximum.accumulate(np.concatenate(([0], g[:-1])))
rec_pos = np.nonzero(g > runmax)[0]
print("records:", len(rec_pos))
rec_gaps = g[rec_pos]

# --- Definition A (notebook-2 / card L15): m = most recent record index <= n
gov = np.searchsorted(rec_pos, np.arange(len(g)), side='right') - 1
maskA = gov >= 0
mA = rec_pos[gov[maskA]]
slackA = T[maskA] - T[mA]
nz = mA != np.nonzero(maskA)[0]        # exclude n == its own record
jA = np.argmin(np.where(nz, slackA, np.inf))
print("DEF A (governing=most recent record): min slack = %.6g at n=%d p=%d" %
      (slackA[nz].min(), idx[maskA][jA], p[maskA][jA]))
print("   exceptions (<0):", int((slackA[nz] < 0).sum()))

# --- Definition B (notebook-0): m(n) = min{ m : g_m >= g_n }
j = np.searchsorted(rec_gaps, g, side='left')
mB = rec_pos[j]
slackB = T - T[mB]
own = (mB == np.arange(len(g)))
jB = np.argmin(np.where(~own, slackB, np.inf))
print("DEF B (first index with g_m >= g_n): min slack = %.6g at n=%d p=%d" %
      (slackB[~own].min(), idx[jB], p[jB]))
print("   exceptions (<0):", int((slackB[~own] < 0).sum()))

# non-monotonicity of T, n>=10
sel = idx[:-1] >= 10
down = int((T[1:][sel] < T[:-1][sel]).sum())
print("T_{n+1}<T_n for n>=10: %d / %d = %.4f%%" % (down, sel.sum(), 100*down/sel.sum()))
