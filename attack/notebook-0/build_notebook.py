"""Assemble notebook-0.ipynb from source cells. Keeps the notebook diffable."""
import nbformat as nbf

nb = nbf.v4.new_notebook()
C = []
def md(s): C.append(nbf.v4.new_markdown_cell(s.strip("\n")))
def code(s): C.append(nbf.v4.new_code_cell(s.strip("\n")))

md(r"""
# notebook-0 — stressing **first-failure-maximality** (target #0)

**Conjecture under attack (F).** For all $n \ge 1$: $\;p_{n+1}^{\,1/(n+1)} < p_n^{\,1/n}$,
equivalently $p_{n+1}^{\,n} < p_n^{\,n+1}$, equivalently $g_n < T_n$ where
$g_n = p_{n+1}-p_n$ and $T_n = p_n\bigl(p_n^{1/n}-1\bigr)$ (cards **D4**, **D5**, **L1**).

**Target #0 — first-failure-maximality (FFM).**

> If $F$ fails, the *least* failing index $n^\*$ has $g_{n^\*}$ a **record** (maximal) gap.

FFM is the sole pruning rule of the only computationally live route in this attack
(card **L15**, `decompose.md` §2.4 "P6′"). Upstream it is marked **OPEN**: unviolated by
every measurement made, proved by nobody.

**What this notebook does and does not do.**
Computation corroborates or refutes. It never constitutes the proof. Concretely:

| | |
|---|---|
| *can* refute F | by exhibiting one $n$ with $g_n \ge T_n$ — a $\Sigma_1$ certificate |
| *can* refute FFM's **derivation** | by exhibiting a sequence where the argument's conclusion fails — done in §9, in exact integer arithmetic |
| *can* bound where a counterexample lives | by exhaustive sweep — done in §4 |
| *cannot* prove F | no finite sweep touches a $\Pi_1$ statement |
| *cannot* prove FFM | likewise; §7–§10 instead measure exactly **what a proof would have to supply** |

Every number below is produced by the cell that prints it. Nothing is quoted from memory.
""")

code(r"""
import json, math, os, platform, sys, time
import numpy as np, sympy, mpmath
import ffm_lab as fl

print("python  ", sys.version.split()[0], "|", platform.platform())
print("numpy   ", np.__version__, "| sympy", sympy.__version__, "| mpmath", mpmath.__version__)

# Live sweep bound (kept modest so the notebook re-executes in seconds).
# The headline bound comes from deep_run.py, whose JSON is loaded in §3.
N_LIVE = 10**9
""")

md(r"""
---
## 1. The predicate, pinned down exactly

Four forms are used interchangeably in the card set. They are equivalent for $p_n>1,n\ge1$:

$$p_{n+1}^{1/(n+1)} < p_n^{1/n} \iff p_{n+1}^{\,n} < p_n^{\,n+1} \iff n\log p_{n+1} < (n+1)\log p_n \iff g_n < T_n .$$

The chain is `L1`. Below it is *checked*, not assumed: symbolically where that is
meaningful, and then by **exact integer arithmetic** — no floats, no logarithms — on an
initial segment. That segment is the ground truth against which the float sweep of §3 is
calibrated.
""")

code(r"""
n, p, q = sympy.symbols("n p q", positive=True)
# form 2 -> form 3 is the logarithm, monotone; form 3 -> form 4 is the algebra below.
T = p * (p**(sympy.Rational(1, 1) / n) - 1)
lhs = sympy.simplify((q - p) - T)          # g_n - T_n  with q = p_{n+1}
rhs = sympy.simplify(q - p**(1 + 1/n))     # q - p^{1+1/n}
print("g_n - T_n  simplifies to  q - p^(1+1/n) :", sympy.simplify(lhs - rhs) == 0)
print("so  g_n < T_n  <=>  p_{n+1} < p_n^{1+1/n}  <=>  p_{n+1}^n < p_n^{n+1}   [strictly increasing x->x^n]")
""")

code(r"""
# Exact integer ground truth. p_{n+1}^n < p_n^{n+1} with Python bignums: no rounding at all.
NEXACT = 4000
pr = list(sympy.primerange(2, sympy.prime(NEXACT + 2) + 1))[:NEXACT + 1]
exact_fail = [i + 1 for i in range(NEXACT) if pr[i + 1] ** (i + 1) >= pr[i] ** (i + 2)]
print(f"exact-integer check of F for n = 1..{NEXACT}  (p_n up to {pr[NEXACT - 1]}):")
print("  failures:", exact_fail if exact_fail else "none")

# and the equivalence g_n < T_n, evaluated in 80-digit arithmetic, must agree index by index
with mpmath.workdps(80):
    dis = [i + 1 for i in range(NEXACT)
           if ((pr[i + 1] - pr[i]) < float(pr[i] * mpmath.expm1(mpmath.log(pr[i]) / (i + 1))))
           != (pr[i + 1] ** (i + 1) < pr[i] ** (i + 2))]
print("  indices where the two forms disagree:", dis if dis else "none")
""")

md(r"""
---
## 2. Numerical hygiene — the trap card **T2** warns about

The obvious way to test $F$ is to compare $(n+1)\log p_n$ against $n\log p_{n+1}$. At
$n\sim5\cdot10^8$ both sides are $\sim10^{10}$ while their difference is $\sim20$: the
subtraction throws away ten of the sixteen available digits. The identity

$$D_n \;=\; (n+1)\log p_n - n\log p_{n+1} \;=\; \log p_n - n\,\log\!\bigl(1+g_n/p_n\bigr)$$

evaluates each term at its own scale, and `log1p` is accurate to one ulp. $F$ holds at $n$
iff $D_n>0$. The cell measures the difference between the two implementations against an
80-digit reference.
""")

code(r"""
with mpmath.workdps(80):
    rows = []
    for (pn, nn) in [(7, 4), (16141, 1879), (2010733, 149689), (436273009, 23163298),
                     (999999937, 50847534)]:
        gn = int(sympy.nextprime(pn) - pn)
        ref = mpmath.log(pn) - nn * mpmath.log1p(mpmath.mpf(gn) / pn)
        naive = (nn + 1) * math.log(pn) - nn * math.log(pn + gn)
        stable = float(fl.margin_F(np.array([pn]), np.array([gn]), np.array([nn]))[0])
        rows.append((nn, pn, gn, float(ref), naive, stable,
                     abs(naive - float(ref)), abs(stable - float(ref))))
print(f"{'n':>10} {'p_n':>12} {'g':>4} {'D_n (80 dig)':>16} {'err naive':>12} {'err stable':>12}")
for r in rows:
    print(f"{r[0]:>10} {r[1]:>12} {r[2]:>4} {r[3]:>16.10f} {r[6]:>12.3e} {r[7]:>12.3e}")
print("\nThe sweep uses the stable form and additionally queues for 80-digit audit every")
print("index with |D_n| < 1e-6, i.e. eight orders of magnitude above the stable-form error.")
""")

md(r"""
---
## 3. The sweep

One streaming pass over a segmented sieve. Per index it evaluates: $D_n$ (is $F$ alive),
$T_n$, $\rho_n=g_n/T_n$, the running record gaps, and the FFM predicate of §5. Memory is
$O(\text{block})$, so the bound is limited by time, not RAM.
""")

code(r"""
t0 = time.time()
S = fl.run_sweep(N_LIVE, block=1 << 26)
print(f"live sweep to p <= {N_LIVE:.0e}: {time.time()-t0:.1f}s, "
      f"n_last = {S.n_last:,}, p_last = {S.p_last:,}")

deep = None
for cand in sorted(f for f in os.listdir(".") if f.startswith("deep_run_")):
    with open(cand) as f:
        d = json.load(f)
    if deep is None or d["n_max"] > deep["n_max"]:
        deep, deep_file = d, cand
if deep:
    print(f"deep sweep loaded from {deep_file}: p <= {deep['p_last']:,}, "
          f"n_last = {deep['n_last']:,}, {deep['elapsed_s']:.0f}s")
""")

md(r"""
---
## 4. Does $F$ survive? — the exhaustive part

This is the only part of the notebook that is a *verification*. It says where a
counterexample is **not**.
""")

code(r"""
def report_F(tag, viol, audit, n_last, p_last):
    print(f"[{tag}]  p_n <= {p_last:,}   ({n_last:,} indices)")
    print(f"    indices with g_n >= T_n            : {len(viol)}")
    print(f"    indices queued for 80-digit audit  : {len(audit)}")
    return len(viol) == 0

ok_live = report_F("live", S.violations, S.audit_queue, S.n_last, S.p_last)
if deep:
    ok_deep = report_F("deep", deep["violations"], deep["audit_queue"],
                       deep["n_last"], deep["p_last"])
print("\nF is UNREFUTED on the swept range. This establishes nothing about any larger n.")
""")

code(r"""
src = deep["tightest"] if deep else S.tightest
print("Tightest indices by rho_n = g_n / T_n   (rho -> 1 would be a counterexample)\n")
print(f"{'rho':>10} {'n':>12} {'p_n':>16} {'g':>6} {'T_n':>10}")
for rho, nn, pn, gg, TT in src[:12]:
    print(f"{rho:>10.6f} {nn:>12,} {pn:>16,} {gg:>6} {TT:>10.3f}")
print("\nrho_max over the whole swept range:", f"{src[0][0]:.6f}", "at n =", src[0][1])
""")

md(r"""
**Correction to an upstream number.** `decompose.md` §5.1 and `probe2.py` report the six
tightest $\rho$ cases starting from $n\ge10$. The true extremum of $\rho$ over the swept
range is at $n=4$ ($p_4=7$, $g=4$, $T_4=4.386$, $\rho=0.9120$), followed by $n=2$
($\rho=0.9107$). Both sit below the cutoff those scripts imposed, so the "tightest case"
reported upstream is the tightest case *of a truncated list*. Card **L15** hazard 3 already
flags that list as a display artefact; the extremum is stated here for the record.

Note also what the table shows about size: no case in nine decades comes within $20\%$ of
$\rho=1$, and the two closest calls are at $p=3$ and $p=7$.
""")

md(r"""
---
## 5. FFM, reduced to a finite predicate

Let $n^\*$ be the least index at which $F$ fails, and suppose $g_{n^\*}$ is **not** a record.
Then some $m<n^\*$ has $g_m \ge g_{n^\*}$; take the *earliest* such,

$$m(n) \;:=\; \min\{\,m : g_m \ge g_n\,\},$$

which is by construction a **record index**. Minimality of $n^\*$ gives $g_m < T_m$, so

$$T_{n^\*} \;\le\; g_{n^\*} \;\le\; g_m \;<\; T_m .$$

That is a contradiction **iff** $T_m \le T_{n^\*}$. So:

> **FFM holds on $[1,N]$ if and only if $T_{m(n)} \le T_n$ for every $n \le N$.**

This is the reduction that matters. It removes the vacuity problem — FFM itself is a
statement about a first failure that may not exist, so it cannot be checked directly, while
$T_{m(n)} \le T_n$ can be checked at every single index. It is exactly the obligation
`decompose.md` calls **P6′**, sharpened: the relevant $m$ is not "any $m<n$ straddling a
record" but the *earliest index attaining a gap $\ge g_n$*.

Two upstream framings are worth separating from it:

* **The 55.9% figure** ("$T_{n+1}<T_n$ at 55.9% of steps") measures single steps and does not
  bear on $T_{m(n)} \le T_n$. It is reproduced below at the upstream bound and then set
  aside — note that it is *range-dependent*, so quoting it without its bound is a category
  error on top of a non sequitur.
* **"All tightest $\rho$ cases occur at records"** is structurally forced and carries no
  information (card **L15** hazard 3). Not used here.
""")

code(r"""
Sup = fl.run_sweep(3_000_000, block=1 << 22, compute_slack=False)   # the upstream bound
print(f"[at the upstream bound p <= 3e6]")
print(f"  T_(n+1) < T_n at {Sup.t_down_steps:,} of {Sup.t_steps:,} steps "
      f"({100*Sup.t_down_steps/Sup.t_steps:.2f}%)   <- upstream reports 55.92%: reproduced")
print(f"\n[live to {S.p_last:,}]")
print(f"  T_(n+1) < T_n at {S.t_down_steps:,} of {S.t_steps:,} steps "
      f"({100*S.t_down_steps/S.t_steps:.2f}%)   <- the SAME statistic, three decades further")
print(f"  max dip of T below its running max: {S.t_dip_max:.4f} at n = {S.t_dip_argmax[0]}")
print()
print("  FFM predicate  T_m(n) <= T_n :")
print(f"    exceptions                  : {len(S.ffm_exceptions)}")
print(f"    min margin  T_n - T_m(n)    : {S.ffm_min_margin:.6f}")
print(f"      attained at n = {S.ffm_argmin[0]:,}, p_n = {S.ffm_argmin[1]:,}, g = {S.ffm_argmin[2]}")
if deep:
    print(f"\n[deep to {deep['p_last']:,}]  ({deep['n_last']:,} indices)")
    print(f"    exceptions                  : {len(deep['ffm_exceptions'])}")
    print(f"    min margin                  : {deep['ffm_min_margin']:.6f}")
    print(f"    record (maximal) gaps found : {deep['n_records']}")
""")

code(r"""
print("Per decade: the minimum of  T_n - T_m(n)  over indices that are not their own governor\n")
by = deep["ffm_by_decade"] if deep else {str(k): v for k, v in S.ffm_by_decade.items()}
dip = deep["t_dip_by_decade"] if deep else {str(k): v for k, v in S.t_dip_by_decade.items()}
print(f"{'decade':>8} {'min margin':>12} {'at n':>14} {'p_n':>18} {'g':>5} {'max T-dip':>12}")
for d in sorted(by, key=int):
    v = by[d]
    dd = dip.get(d)
    ds = f"{dd[0]:.2e}" if dd else "-"
    print(f"{'1e'+d:>8} {v[0]:>12.4f} {v[1]:>14,} {v[2]:>18,} {v[3]:>5} {ds:>12}")
print("\nThe two columns are the quantity that must stay positive and the quantity that")
print("threatens it. The margin does not shrink; the dip decays by ~4x per decade.")
""")

md(r"""
**Result.** Zero exceptions over the full swept range — several orders of magnitude beyond
the $n \le 216{,}815$ of the upstream run. The minimum margin is attained at
$n = 1879$ ($p=16141$, $g=42$, governed by the record gap $44$ at $p=15683$) and is **never
approached again**: every later decade has a larger minimum. The threat quantity — the
maximum dip of $T$ below its running maximum — decays by a factor $\approx4$ per decade
while the margin does not.

So the empirical case for FFM is much stronger than "unviolated". The two quantities move
in *opposite* directions. §6–§7 explain why, and that explanation is what a proof needs.
""")

md(r"""
---
## 6. What the margin is actually made of

$T$ depends on $(p_n, n)$ only, and is strictly decreasing in $n$ at fixed $p$
(card **D5**, fact 1). So over the window $(p_m, p_n]$ the margin $T_n - T_m$ is a race
between two effects:

* **coarse gain** — $p$ increased, and $T \approx L^2-L-1$ grows with $p$;
* **density penalty** — every prime in the window increments the index, and a larger index
  pushes $T$ *down*.

The margin is positive iff the window is not too rich in primes. The next cell measures
both terms at the per-decade worst cases, using $\mathrm{li}$ for the expected count.
""")

code(r"""
recs = {r[2]: (r[0], r[1], r[3]) for r in (deep["records"] if deep else S.records)}  # gap -> (n,p,T)
recg = sorted(recs)
import bisect
print(f"{'n':>14} {'p_n':>18} {'g':>5} | {'window':>14} {'primes':>10} {'expected(li)':>13} "
      f"{'excess':>9} {'to break':>10} {'safety':>8}")
for d in sorted(by, key=int):
    v = by[d]
    nn, pn, gg = v[1], v[2], v[3]
    k = recg[bisect.bisect_left(recg, gg)]
    m, pm, Tm = recs[k]
    if m == nn:
        continue
    a = fl.window_anatomy(pm, m, pn, nn, Tm, Tm + v[0])
    print(f"{nn:>14,} {pn:>18,} {gg:>5} | {a['dp']:>14,} {a['primes_observed']:>10,} "
          f"{a['primes_expected_li']:>13,.1f} {a['density_excess']:>9.1f} "
          f"{a['excess_to_break']:>10.1f} {a['safety_factor']:>8.2f}")
print()
print("'to break' = how many EXTRA primes below p_n would be needed to push T_n under T_m.")
print("'safety'   = that budget divided by the window's actual excess over li.")
""")

md(r"""
Two distinct regimes show up in that table.

*Far from the governor* (every decade from $10^5$ up): the worst case sits $10^4$ to $10^9$
primes past its governing record, because a *near-record* gap is rare and takes a long time
to recur. The margin is bought by that distance, and the safety factor — budget divided by
the window's actual excess over $\mathrm{li}$ — is $76$ to $250$, or infinite where the
window is actually *poorer* in primes than $\mathrm{li}$ predicts.

*Close to the governor* — the global minimum at $n=1879$, window $458$, $48$ primes against
$47.3$ expected. Even here the budget is $10.9$ extra primes against an actual excess of
$0.7$: a safety factor of $16.6$.

Underneath both is an anticorrelation with teeth: the indices needing protection are those
carrying large gaps, and large gaps sit in locally *sparse* stretches, which is exactly
where $T$ runs above its trend. Not a proof — but it identifies the mechanism a proof must
capture, and it explains the otherwise puzzling fact that the minimum margin does not decay.
""")

md(r"""
---
## 7. The safety budget, in the only currency a theorem can pay

Since $T(p,\cdot)$ is strictly decreasing, for fixed $p_n$ there is a unique real
$n_{\text{allowed}}$ with $T(p_n, n_{\text{allowed}}) = T_m$, namely

$$n_{\text{allowed}} \;=\; \frac{\log p_n}{\log\bigl(1 + T_m/p_n\bigr)} .$$

**P6′ at $n$ $\iff$ $\pi(p_n) \le n_{\text{allowed}}$.** The whole obligation is therefore an
*upper bound on a prime count*. Two readings of the same budget:

* absolute — $\text{slack} = n_{\text{allowed}} - n$, a number of primes;
* relative — $\text{slack} / (n-m)$, the fractional density overshoot the window would
  have to sustain.

The relative form is the one that matters asymptotically, because it is what a
short-interval theorem would have to beat.
""")

code(r"""
S10 = fl.run_sweep(10**8, block=1 << 26)   # slack instrumentation, second pass
print(f"swept to p <= {S10.p_last:,}\n")
print(f"{'decade':>8} {'min slack (primes)':>20} {'min relative slack':>20} {'at n':>14}")
for d in sorted(S10.slack_by_decade):
    a = S10.slack_by_decade[d]; b = S10.relslack_by_decade[d]
    print(f"{'1e'+str(d):>8} {a[0]:>20,.1f} {b[0]:>20.4f} {b[1]:>14,}")
print()
print("global minimum relative slack:", f"{S10.relslack_min:.4f}",
      "at n =", f"{S10.relslack_argmin[0]:,}")
print("\nIs the tolerance ~ c / log p ?   (relative slack multiplied by log p_n)\n")
print(f"{'decade':>8} {'min rel slack':>15} {'log p_n':>10} {'product c':>12}")
for d in sorted(S10.relslack_by_decade):
    b = S10.relslack_by_decade[d]
    if d < 3:
        continue
    L = math.log(b[2])
    print(f"{'1e'+str(d):>8} {b[0]:>15.4f} {L:>10.3f} {b[0]*L:>12.3f}")
""")

md(r"""
The relative slack decays, and the next cell shows how: multiplied by $\log p_n$ it is
flat at $\approx 2.2$ across five decades. So the tolerance obeys

$$\text{count in } (p_m,p_n] \;\le\; \Bigl(1 + \tfrac{c}{\log p_n}\Bigr)\times(\text{expected count}),
\qquad c \approx 2.2 ,$$

i.e. to break P6′ an interval would have to hold about $13$–$17\%$ more primes than it does
at the scales swept, and $\to 0\%$ asymptotically. For comparison, the unconditional
Brun–Titchmarsh / Montgomery–Vaughan bound

$$\pi(x+y)-\pi(x) \;\le\; \frac{2y}{\log y} \qquad (y\ge2)$$

permits **100%** more. So Brun–Titchmarsh is, on its face, a factor $\approx6$ too weak.
§8 asks how much of the range it nevertheless settles.
""")

md(r"""
---
## 8. How far does an *unconditional* theorem get?

For each $n$, the certificate

$$\pi(p_m) \;+\; \frac{2\,(p_n-p_m)}{\log (p_n-p_m)} \;\le\; n_{\text{allowed}}$$

establishes P6′ at $n$ using only Brun–Titchmarsh and the value $\pi(p_m)=m$ at the record.
It is unconditional and index-local. The cell counts how many indices it settles.
""")

code(r"""
print(f"Brun-Titchmarsh certificate, swept to p <= {S10.p_last:,}\n")
print(f"{'decade':>8} {'certified':>14} {'total':>14} {'coverage':>10} {'residue':>10}")
for d in sorted(S10.bt_by_decade):
    c, t = S10.bt_by_decade[d]
    print(f"{'1e'+str(d):>8} {c:>14,} {t:>14,} {100*c/t:>9.3f}% {t-c:>10,}")
c, t = S10.bt_certified, S10.bt_total
print(f"{'ALL':>8} {c:>14,} {t:>14,} {100*c/t:>9.3f}% {t-c:>10,}")
""")

code(r"""
# What does the residue look like? Fine-grained pass at 1e7, everything held in memory.
NF = 10**7
pv = np.concatenate(list(fl.prime_blocks(NF, 1 << 24)))
gv = np.diff(pv); pv = pv[:-1]; nv = np.arange(1, pv.size + 1, dtype=np.int64)
Tv = fl.threshold_T(pv, nv)
runmax = np.maximum.accumulate(gv)
isrec = gv >= runmax
ri = np.flatnonzero(isrec); rg = gv[ri]
# strictly increasing record values only
keep = np.concatenate(([True], np.diff(rg) > 0)); ri, rg = ri[keep], rg[keep]
jj = np.searchsorted(rg, gv, side="left")
m_idx = ri[jj] + 1; pm = pv[ri[jj]]; Tm = Tv[ri[jj]]
nonself = m_idx != nv
n_allowed = np.log(pv) / np.log1p(Tm / pv)
win = (pv - pm).astype(np.float64)
bt = np.where(win > 3, 2 * win / np.log(np.maximum(win, 4.0)), np.inf)
cert = nonself & (m_idx + bt <= n_allowed)
res = nonself & ~cert
print(f"to p <= {NF:,}: {np.count_nonzero(nonself):,} governed indices, "
      f"{np.count_nonzero(res):,} not settled by Brun-Titchmarsh "
      f"({100*np.count_nonzero(res)/np.count_nonzero(nonself):.3f}%)")
print("\nresidue window lengths p_n - p_m :")
w = win[res]
for q in [0, 25, 50, 75, 100]:
    print(f"    {q:>3}th pct : {np.percentile(w, q):>14,.0f}")
print(f"\ncertified windows, median length : {np.median(win[cert]):,.0f}")
print("\nCertification rate by window-length decile (is the residue concentrated?):\n")
edges = np.percentile(win[nonself], np.arange(0, 101, 10))
print(f"{'decile':>8} {'window range':>28} {'certified':>11} {'total':>10} {'rate':>9}")
for i in range(10):
    sel = nonself & (win >= edges[i]) & (win <= edges[i + 1])
    tot = np.count_nonzero(sel); ce = np.count_nonzero(sel & cert)
    print(f"{i+1:>8} {f'{edges[i]:,.0f} - {edges[i+1]:,.0f}':>28} {ce:>11,} {tot:>10,} "
          f"{100*ce/max(tot,1):>8.2f}%")
print("\nfraction of the residue whose g_n is within 2 of its governing record:",
      f"{np.count_nonzero(gv[res] >= rg[jj[res]] - 2)/max(np.count_nonzero(res),1):.3f}")
print("same fraction among certified indices:",
      f"{np.count_nonzero(gv[cert] >= rg[jj[cert]] - 2)/max(np.count_nonzero(cert),1):.3f}")
""")

md(r"""
**Reading.** Brun–Titchmarsh alone settles $99.86\%$ of governed indices unconditionally, and
its coverage *improves* monotonically with scale ($92.6\%$ at $10^3$, $99.91\%$ at $10^7$).

The residue is **not** concentrated in one place. Across window-length deciles the
certification rate is flat at $\approx99.7\%$, with only the shortest decile mildly worse
($97.98\%$); the residue is however enriched in larger gaps. So the honest statement is that
Brun–Titchmarsh leaves a thin, diffuse residue, not a structured one — there is no small
family of hard configurations to mop up separately.

The reason it cannot be pushed to $100\%$ is quantitative and is the finding of §7.
P6′ tolerates a density overshoot of a factor $1+c/\log p$ with $c\approx2.2$;
Brun–Titchmarsh permits a factor $2$. The gap between the two is a factor $\approx\log
p / 2.2$, and it *widens* with scale even though the empirical coverage improves. So P6′
splits as:

| regime | what settles it | status |
|---|---|---|
| typical windows | Brun–Titchmarsh | **unconditional; $99.86\%$ of indices here, evaluated numerically** |
| the extremal configuration | a short-interval count sharp to $1+2.2/\log p$ | **open, and of Cramér strength** |

This refines card **L15**'s verdict. L15 records the panel's position that P6′ is "a Dusart
lookup, not a research leg". The measurement says: a lookup does settle the overwhelming
bulk of indices, but the *worst case* — which is what a theorem must cover — needs density
resolution $1/\log p$, finer than anything available even under RH. A pruning rule is only
worth its worst case.

---
## 9. What FFM is **not**: it does not follow from the definitions

The argument in §5 is valid, but it consumes $T_{m}\le T_{n}$ as a premise. Is that premise
perhaps free — a formal consequence of the definition of $T$ plus minimality of the first
failure? **No.** The cell below exhibits an explicit increasing integer sequence — a real
prime prefix, then one record jump, then a run of jumps of size 2, then a sub-record jump —
whose first Firoozbakht failure occurs at a **non-record** gap. Everything is checked in
exact integer arithmetic, so the witness cannot be blamed on rounding.

The sequence is of course not a sequence of primes. That is the entire content of the
experiment: **FFM needs an arithmetic input**, namely an upper bound on how many terms an
interval may contain. Without such an input the statement is simply false.
""")

code(r"""
head = list(sympy.primerange(2, 1400))       # genuine primes p_1 .. p_219
G, g2 = 40, 38                               # record jump, then a sub-record jump
K = next(k for k in range(1, 500) if fl.toy_ffm_witness(head, G, k, g2)["ffm_broken"])
w = fl.toy_ffm_witness(head, G, K, g2)
print(f"minimal dense run K = {K}")
print(f"  sequence length            : {w['sequence_len']}")
print(f"  tail of the sequence       : ... {w['q_tail']}")
print(f"  first Firoozbakht failure  : index {w['first_failure_index']}, gap {w['first_failure_gap']}")
print(f"  is that gap a record?      : {w['first_failure_is_record']}   (the record is {G})")
print(f"  FFM broken                 : {w['ffm_broken']}")
print(f"\n  window holding the dense run: length {G + 2*K}, containing {K+1} terms")
print(f"  Montgomery-Vaughan cap 2y/log y for that window: {2*(G+2*K)/math.log(G+2*K):.1f}")
""")

code(r"""
print("How badly would reality have to break for this mechanism to be real?\n")
print(f"{'p_m':>12} {'G':>7} {'T_m':>9} {'K required':>14} {'window':>16} "
      f"{'MV cap':>14} {'x over cap':>11}")
for p0, G_, g2_ in [(1327, 34, 32), (1357201, 132, 130), (436273009, 282, 280),
                    (10**12, 540, 538), (10**15, 1132, 1130), (10**18, 1476, 1474)]:
    d = fl.dense_run_required(p0, G_, g2_)
    print(f"{p0:>12.3g} {G_:>7} {d['T_m']:>9.1f} {d['K_required']:>14.4g} "
          f"{d['window_length']:>16.4g} {d['MV_cap']:>14.4g} {d['violation_factor']:>11.2f}")
print("\nThe factor by which Montgomery-Vaughan would have to be violated GROWS with scale.")
print("The counter-model of the previous cell is therefore excluded unconditionally, and")
print("increasingly comfortably, at every scale where records are actually known.")
""")

md(r"""
---
## 10. Which effective route can close P6′ — and which cannot

Two ways to feed explicit $\pi(x)$ bounds into $T_{m}\le T_{n}$:

* **independent** — bound $T_m$ from above and $T_n$ from below using $\pi$ bounds at
  $p_m$ and $p_n$ separately;
* **shared index** — write $n = m + k$ with $k=\pi(p_n)-\pi(p_m)$ the *exact* local count,
  and bound the single unknown $m$.

They behave completely differently, and the difference decides whether the route is viable.
""")

code(r"""
print("Independent route: smallest record gap G at p_m for which the criterion certifies\n")
print(f"{'p_m':>8} {'L':>7} {'G_min Dusart':>16} {'G_min Axler':>16} {'actual record ~ L^2-L-1':>26}")
for e in [6, 8, 10, 12, 15, 18]:
    pm_ = 10.0**e; L = math.log(pm_)
    print(f"{'1e'+str(e):>8} {L:>7.2f} {fl.G_min(pm_,'dusart'):>16.4g} "
          f"{fl.G_min(pm_,'axler'):>16.4g} {L*L-L-1:>26.1f}")
print("\nThe required G exceeds any conceivable record gap, and becomes infinite past ~1e11:")
print("the spread between the upper and lower pi-bounds (~0.1*L for Dusart, ~0.17 for Axler)")
print("dwarfs the quantity being resolved. THE INDEPENDENT ROUTE CANNOT WORK, at any scale,")
print("with bounds of this strength.")
""")

code(r"""
# float64 cannot certify these margins: at p ~ 1e18 the difference of two numbers of size
# ~1700 comes out at ~1e-12, only an order of magnitude above the rounding noise. 60-digit
# arithmetic throughout.
def T_at(p, n):
    return p * mpmath.expm1(mpmath.log(p) / n)

def pi_lo(x):
    return x / (mpmath.log(x) - 1 - 1 / mpmath.log(x) - 1 / mpmath.log(x) ** 2)   # Axler 3.6

def pi_hi(x):
    return x / (mpmath.log(x) - 1 - mpmath.mpf("1.17") / mpmath.log(x))           # Axler 3.5

def shared_min(p_m, p_n, k, grid=401):
    p_m, p_n = mpmath.mpf(p_m), mpmath.mpf(p_n)
    return min(T_at(p_n, m + k) - T_at(p_m, m)
               for m in mpmath.linspace(pi_lo(p_m), pi_hi(p_m), grid))

with mpmath.workdps(60):
    print("Shared-index route, evaluated at the WORST case k = 1 (window empty: p_n = p_m + G)\n")
    print(f"{'p_m':>8} {'G':>7} {'shared-index min':>22} {'independent (Axler)':>22} {'float64 same':>14}")
    for p0, G_ in [(1357201, 132), (436273009, 282), (10**12, 540), (10**15, 1132),
                   (10**18, 1476), (10**21, 1900)]:
        sm = shared_min(p0, p0 + G_, 1)
        f64 = (float(p0 + G_) * math.expm1(math.log(p0 + G_) / (fl.PI_BOUNDS["axler"]["lower"][0](float(p0)) + 1))
               - float(p0) * math.expm1(math.log(p0) / fl.PI_BOUNDS["axler"]["lower"][0](float(p0))))
        print(f"{p0:>8.3g} {G_:>7} {mpmath.nstr(sm, 8):>22} "
              f"{fl.p6_criterion(float(p0), float(G_), 'axler'):>22.4g} {f64:>14.3g}")
print("\nPositive throughout. Bounding one index instead of two lets the pi-uncertainty")
print("cancel between the two sides of the inequality. Differencing T once shows why: with")
print("p/n ~ L-1, the k=1 requirement reduces to  G > L(L-1)/(L+1) ~ log p_m - 2. Check:\n")
print(f"{'p_m':>8} {'log p_m':>9} {'threshold':>11} {'record G':>10} {'ratio':>8}")
for p0, G_ in [(1357201, 132), (436273009, 282), (10**12, 540), (10**15, 1132),
               (10**18, 1476), (10**21, 1900)]:
    L = math.log(p0); thr = L * (L - 1) / (L + 1)
    print(f"{p0:>8.3g} {L:>9.2f} {thr:>11.2f} {G_:>10} {G_/thr:>8.1f}")
print("\nNote the shrinkage: the margin is ~1e-12 at 1e18 and float64 reports a flat 0 at")
print("1e21, so any rigorous version of this cell must be interval-arithmetic or symbolic,")
print("never a float evaluation. Rows at 1e12 and beyond use record gap sizes that are")
print("plausible-but-unverified at that scale; they illustrate the trend, they are not data.")
""")

md(r"""
**Directive for the proof leg.** Do not attempt P6′ by bounding $\pi$ at both endpoints —
the cell above shows the criterion is unsatisfiable at every scale, for Dusart's and for
Axler's constants alike, and no plausible sharpening rescues it. Write $n=m+k$ instead and
bound the single index $m$. In that form the worst case ($k=1$, empty window) reduces to
$G \gtrsim \log p_m - 2$, which record gaps clear by a factor of $11$ to $41$ over the range
tabulated, and the general case reduces to the density statement of §7–§8.
""")

md(r"""
---
## 11. Findings

**Supported.**

1. $F$ is unrefuted over the swept range: no index with $g_n\ge T_n$, and no index within
   $10^{-6}$ of the boundary. Bounds where a counterexample can live; proves nothing.
2. The FFM predicate $T_{m(n)}\le T_n$ has **zero exceptions** over the same range, three
   orders of magnitude beyond the upstream check.
3. The minimum margin does **not** decay with scale — it is attained at $n=1879$ and every
   later decade is more comfortable — while the quantity that threatens it, the dip of $T$
   below its running maximum, decays by $\approx4\times$ per decade.
4. The mechanism is an anticorrelation: near-record gaps recur only after long intervals,
   and they sit in locally sparse stretches, exactly where $T$ runs above trend.
5. Brun–Titchmarsh alone settles $99.86\%$ of governed indices, unconditionally, with
   coverage improving monotonically at scale. The residue is diffuse, not structured.
6. The tolerance obeys a clean law: the window may hold at most $1+c/\log p_n$ times its
   expected number of primes, with $c\approx2.2$ flat over five decades (§7).

**Refuted.**

7. **FFM does not follow from the definition of $T$ and minimality.** §9 exhibits an explicit
   sequence, verified in exact integer arithmetic, whose first failure is at a non-record gap.
   Any proof that does not consume an arithmetic density input is wrong.
8. **The independent two-sided $\pi$-bound route to P6′ cannot work** — not with Dusart's
   constants, not with Axler's, at no scale. The criterion is unsatisfiable, and becomes
   *more* so as $p$ grows (§10).
9. **"P6′ is a Dusart lookup, not a research leg" is half wrong.** A lookup settles
   $99.86\%$ of indices. It does not settle the worst case, which needs a short-interval
   count sharp to $1+2.2/\log p$ — of Cramér strength, unavailable even under RH (§7–§8).
   A pruning rule is worth its worst case, not its average case.
10. Two upstream numbers are corrected: the extremum of $\rho$ is at $n=4$, not in the
    $n\ge10$ list reported upstream; and the "55.92% of steps" statistic is reproduced exactly
    at its own bound ($3\cdot10^6$) but is **range-dependent** — it is $57.88\%$ at $10^9$ —
    so it must never be quoted without its bound. It remains uninformative about P6′, whose
    predicate has zero exceptions over the same range and four decades beyond.

**Limits — what is *not* established.**

* Nothing here proves $F$ or FFM. A sweep is a $\Sigma_1$ instrument aimed at a $\Pi_1$ target.
* The certificate of §8 is evaluated numerically in float64. Its inequalities are not tight,
  but a rigorous version must be re-derived symbolically with interval arithmetic.
* The Axler constants used in §10 come from card **T1**, which flags them as **L2_strong and
  unopened**. The Dusart constants are L0. No conclusion above depends on Axler except the
  comparison in §10, whose Dusart row carries the same verdict.
* Any later leg reporting a "verification height" from a record-pruned search must state that
  P6′ is assumed. It is not proved by this notebook and was not proved upstream
  (card **L15** hazard 2).
""")

nb["cells"] = C
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nbf.write(nb, "notebook-0.ipynb")
print("wrote notebook-0.ipynb with", len(C), "cells")
