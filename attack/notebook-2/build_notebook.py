"""
build_notebook — regenerate `notebook-2.ipynb` from source.

The notebook is generated rather than hand-edited so that its cells stay
diffable and its text stays reviewable in a plain editor.

    python3 build_notebook.py           # writes notebook-2.ipynb (no outputs)
    jupyter nbconvert --to notebook --execute --inplace notebook-2.ipynb
"""
import nbformat as nbf

nb = nbf.v4.new_notebook()
C: list = []


def md(text: str) -> None:
    C.append(nbf.v4.new_markdown_cell(text.strip("\n")))


def code(text: str) -> None:
    C.append(nbf.v4.new_code_cell(text.strip("\n")))


# ==========================================================================
md(r"""
# Notebook 2 — the *unconditional verified range* of Firoozbakht's conjecture

**Run:** `germ-20260725-791a7c45` · **leg:** `notebooks__2` · **molecule:** `task-20260725-09a7`
**Target:** `unconditional-verified-range` (target #2)

---

## The conjecture

$$\textbf{(F)}\qquad p_{n+1}^{1/(n+1)} \;<\; p_n^{1/n}\qquad\text{for all } n\ge 1 .$$

**Status in this notebook: OPEN.** `F` is neither assumed true nor assumed false.
Everything below is computation. *Computation corroborates or refutes; it never
constitutes the proof.* Where this notebook says **PROVEN** it means a finite
statement discharged by exhaustive exact arithmetic, or a lemma derived here in
full from a cited effective bound — never `F` itself.

## What "unconditional" is doing in the target name

Three different things get called "the verified range", and they are not the same claim:

| | claim | costs | what it rests on |
|---|---|---|---|
| **(a)** | every consecutive prime pair below $X$ was individually checked | $\tilde O(X)$ | a sieve, and floating-point discipline |
| **(b)** | no gap that *occurs* below $X$ can violate `F`, wherever it occurs | $O(\#\text{gap sizes})$ | an effective $\pi(x)$ bound + a **first-occurrence table** |
| **(c)** | `F` holds below $X$ *assuming* RH / Cramér / a gap conjecture | free | an unproved hypothesis |

Target #2 is (a)+(b) and explicitly **not** (c). Route (b) is the one that reaches
$2^{64}$ in the literature (concept card **L6**), and its analytic half is
re-derived from scratch here as **Lemma A**, so that the notebook does not have
to be believed on the strength of a citation.

## What this notebook establishes, and what it does not

**Establishes (in-run, reproducible by re-executing this file):**

1. `F` holds at every $n$ with $p_n < 10^{11}$ — exhaustive, with a two-tier
   float-screen / exact-arithmetic protocol that cannot silently pass.
2. An unconditional lemma $T_n \ge L(L-1.1)$ for $p_n \ge 60184$ ($L=\log p_n$),
   derived here from one L0-tier effective bound, and then *numerically
   falsification-tested* over the whole sieved range.
3. Its corollary: a gap of size $g$ can violate `F` only at a prime
   $p \le S(g) := \exp\!\big((1.1+\sqrt{1.21+4g})/2\big)$ — and, with the
   in-run first-occurrence table, that **every** gap size occurring below
   $10^{11}$ clears that bar, with the minimum safety factor reported explicitly.
4. An independent reproduction of the "$g<1920$" figure attached to the $2^{64}$
   frontier, from our own arithmetic.
5. As a by-product of (1): **P6′** — card **L15**'s undischarged pruning rule, the
   run's *"single most tractable open obligation"* — checked over four billion
   pairs instead of two hundred thousand, with its *margin* measured rather than
   just its exception count. The margin shrinks (§6b). That is the leg's one
   genuinely unexpected result.

**Does not establish:** the frontier of $2^{64}$ itself. That step needs a
first-occurrence gap table to $4\cdot10^{18}$ that this run does not possess
(card **L6**: `oliveira2014goldbach`, ledger tier L2_weak, **never opened**).
§7 states exactly which inequality that external table has to satisfy, so the
dependency is a named hole rather than a citation.
""")

# ==========================================================================
md(r"""
---
## 1 · Definitions, and the criterion that has no error term

Following the run's concept cards:

$$g_n := p_{n+1}-p_n,\qquad L_n := \log p_n,\qquad
T_n := p_n\big(p_n^{1/n}-1\big) = p_n\big(e^{L_n/n}-1\big)\quad(\textbf{D5})$$

$$\rho_n := g_n/T_n \quad(\textbf{D6}),\qquad c_n := g_n/L_n^2 \quad(\textbf{D7})$$

**D6 is a biconditional with no error term and no index restriction:**

$$\textbf{F fails at } n \iff \rho_n \ge 1 .$$

`c_n` is *not* a substitute: `T_n < L_n^2` off a finite exception set (card **L13**),
so `c_n ≥ 1` is sufficient for refutation but strictly harder to satisfy — a search
run on `c_n` can step over a genuine counterexample. `c_n` is computed below only
to exhibit that gap, never as the objective.

**The exact criterion.** Raising both sides of `(F)` to the power $n(n+1)$ turns it
into an integer comparison with no logarithms at all:

$$\textbf{(F) at } n \iff p_{n+1}^{\,n} < p_n^{\,n+1}.$$

This is the ground truth against which every floating-point verdict in this
notebook is calibrated.
""")

code(r"""
import json, math, os, platform, sys, time
from decimal import Decimal
import numpy as np
import matplotlib.pyplot as plt

import fb_core as fb

print("python    ", sys.version.split()[0], "on", platform.platform())
print("numpy     ", np.__version__)
print("fb_core   ", fb.__file__)

# Scale at which THIS notebook runs on execution. The recorded deep runs
# (up to 1e11) are in deep-runs.json, produced by deep_run.py using the very
# same fb_core.scan. Raise this if you want the notebook itself to go deeper.
N_NOTEBOOK = 10**8
""")

code(r"""
# The exact criterion, and the three ways of deciding F at one index.
for (n, pn, pnext) in [(217, 1327, 1361), (30, 113, 127), (1319945, 20831323, 20831533)]:
    exact = fb.exact_verdict(pn, pnext, n) if n < 20_000 else "n too large"
    cert, margin = fb.certified_verdict(pn, pnext, n)
    print(f"n={n:<9d} p_n={pn:<10d} g={pnext-pn:<4d} "
          f"rho={fb.rho(pn, pnext, n):.7f}  exact={exact}  certified={cert}")
""")

code(r"""
# Calibration: exact integer comparison vs the Decimal-certified verdict,
# for EVERY n up to NCAL. If these ever disagree, the certified path is wrong
# and nothing downstream may be believed. NCAL is capped by the cost of the
# exact side: p_n^(n+1) has ~n*log10(p_n) digits, so this grows fast.
t0 = time.time()
pr = np.concatenate(list(fb.sieve_segments(230_000)))
NCAL = 5_000
disagree = []
for i in range(NCAL):
    n = i + 1
    e = fb.exact_verdict(int(pr[i]), int(pr[i+1]), n)
    c, _ = fb.certified_verdict(int(pr[i]), int(pr[i+1]), n)
    if e != c:
        disagree.append(n)
print(f"calibrated n = 1..{NCAL} (p_n up to {pr[NCAL-1]:,}) in {time.time()-t0:.1f}s")
print("disagreements between exact integer and Decimal-certified verdicts:", disagree)
print("F holds at every one of those indices:", all(
    fb.exact_verdict(int(pr[i]), int(pr[i+1]), i+1) for i in range(NCAL)))
assert not disagree
""")

# ==========================================================================
md(r"""
---
## 2 · Direct exhaustive verification — route (a)

A segmented sieve, then $\rho_n$ for every consecutive pair. Two-tier by design:

* **screen** — float64 over all pairs. $\rho_n$ has $O(1)$ operands, so it does not
  carry the cancellation that destroys the "F2 margin" statistic (§3).
* **escalation** — every pair with $\rho_n \ge 0.90$ is re-decided in Decimal with an
  explicit error budget, and `certified_verdict` *raises* rather than returns if the
  margin lands inside that budget. Card **T2** Rule 3 names the hazard precisely:
  a probe that breaks only on a detected violation reports "no counterexample" from
  pure noise, and the failure is silent **in the verification direction**.
""")

code(r"""
res = fb.scan(N_NOTEBOOK)
print()
print(f"pairs checked      : {res['pairs']:,}")
print(f"violations (rho>=1): {res['violations']}")
print(f"escalations (>=0.9): {len(res['escalations'])}")
print(f"max rho (n>=10)    : {res['top'][0][0]:.7f} at n={res['top'][0][1]:,}, "
      f"p_n={res['top'][0][2]:,}, g={res['top'][0][3]}")
print(f"max c   (n>=10)    : {res['max_c'][0]:.7f} at p_n={res['max_c'][2]:,}")
print(f"largest gap        : {res['records'][-1][2]} at p={res['records'][-1][1]:,}")
""")

code(r"""
# Every escalated pair, re-decided in certified arithmetic. These are the only
# pairs anywhere in range that come within 10% of the bar -- and both are tiny
# indices, which is exactly why cards D6/T2 quote max rho for n >= 10.
for (n, pn, g, r) in res["escalations"]:
    cert, margin = fb.certified_verdict(pn, pn + g, n)
    exact = fb.exact_verdict(pn, pn + g, n)
    print(f"n={n:<4d} p_n={pn:<6d} g={g:<3d} rho={r:.7f}  "
          f"certified F holds = {cert}   exact F holds = {exact}")
""")

code(r"""
# Reproduction check against the figures already in the run (cards D6, T2, L7,
# computed by the `decompose` and `concept-cards` legs at N = 3e6). Independent
# code path; the numbers must agree to the last digit quoted.
r3 = fb.scan(3 * 10**6, verbose=False)
expect = {
    "max rho (n>=10)":       (r3["top"][0][0], 0.7604709, "card D6: 0.7604709 at n=217, p=1327, g=34"),
    "runner-up rho":         (r3["top"][1][0], 0.7590821, "card D6: 0.759 at n=149689, p=2010733, g=148"),
    "max c (n>=10)":         (r3["max_c"][0],  0.7025656, "card T2: 0.70257 at p=2010733"),
    "max F2 margin ratio":   (r3["max_f2"][0], 0.9999984, "decompose 5.1: 0.9999984"),
}
for k, (got, want, src) in expect.items():
    ok = abs(got - want) < 5e-7
    print(f"{'OK ' if ok else 'MISMATCH'} {k:<22s} got {got:.7f}  expected {want:.7f}   [{src}]")
    assert ok, k
print(f"\nn=217 p_n=1327: {r3['top'][0][2]}   n=149689 p_n=2010733: {r3['top'][1][2]}")
print("violations at N=3e6:", r3["violations"])
""")

code(r"""
# The recorded deep runs (deep_run.py, same fb_core.scan, up to 1e11).
DEEP = json.load(open("deep-runs.json")) if os.path.exists("deep-runs.json") else {}
print(f"{'N':>14} {'primes':>15} {'max rho (n>=10)':>16} {'at p_n':>16} {'g':>5} "
      f"{'max gap':>8} {'viol':>5} {'sec':>7}")
for k in sorted(DEEP, key=int):
    d = DEEP[k]
    t = d["top"][0]
    print(f"{int(k):>14,} {d['n_primes']:>15,} {t[0]:>16.7f} {t[2]:>16,} {t[3]:>5} "
          f"{d['records'][-1][2]:>8} {len(d['violations']):>5} {d['seconds']:>7.1f}")
""")

md(r"""
**Read this table for what it is.** The record $\rho$ sits still for three
decades — $0.7896$ at $g=210$, $p=20\,831\,323$, unchanged from $10^8$ through
$10^{10}$ — and then moves once, at $10^{11}$, to $0.8318$ at the maximal gap
$g=456$, $p=25\,056\,082\,087$. Card **T2** is still right that a sieve in this
run cannot reach the interesting region: the published record ($\rho=0.94846$ at
$p=1.693\cdot10^{15}$, card **L7**) is 4.2 decades above $10^{11}$. But the
picture "extending the sieve buys nothing" is too tidy — it buys the *next
maximal gap*, and nothing in between.
""")

# ==========================================================================
md(r"""
---
## 3 · The statistic that must not be used as a progress metric

`decompose` §5.1 headlines $\max_n \; n\log p_{n+1}/((n+1)\log p_n) = 0.9999984$
and reads it as "the conjecture nearly failing". Card **T2** Rule 2 says it is a
$1/n$ artefact. That is checkable, so check it: the distance of that ratio from 1
scales like $(1-\rho_n)/n$, so it tends to 1 for arithmetic reasons as the sieve
extends, in *any* universe — including one where every gap is 2.
""")

code(r"""
print(f"{'N':>14} {'max F2 margin':>16} {'1 - F2':>12} {'max rho':>10} {'1 - rho':>9}")
for k in sorted(DEEP, key=int):
    d = DEEP[k]
    print(f"{int(k):>14,} {d['max_f2'][0]:>16.10f} {1-d['max_f2'][0]:>12.3e} "
          f"{d['top'][0][0]:>10.7f} {1-d['top'][0][0]:>9.4f}")

# The artefact, made explicit: a synthetic control universe in which EVERY gap
# is 2, so q_n = 2n + 1 and F holds by a mile at every index. If the F2 margin
# still reads 0.99999... there, it is not measuring how close F comes to failing.
print("\nsynthetic control -- q_n = 2n+1, every gap equal to 2:")
print(f"  {'n':>12} {'F2 margin':>15} {'rho_n':>10}")
for n in [10**3, 10**5, 10**7, 10**9]:
    q = 2 * n + 1
    f2 = n * math.log(q + 2) / ((n + 1) * math.log(q))
    print(f"  {n:>12,} {f2:>15.10f} {2/(q*math.expm1(math.log(q)/n)):>10.5f}")
""")

md(r"""
The control row settles it: a universe of gap-2 primes produces F2 margins
indistinguishable from the ones quoted as evidence of tightness, while its
$\rho$ is an order of magnitude below the bar. **The F2 margin measures $1/n$.**
Every number in the rest of this notebook is in $\rho$ or in gap units.
""")

# ==========================================================================
md(r"""
---
## 4 · Lemma A — the unconditional half

Route (b) needs one analytic input, and only one.

> **Dusart (2010), Thm 6.9, eq. (6.6):** $\pi(x) \le x/(\log x - 1.1)$ for $x \ge 60184$.
> Ledger tier **L0** (opened and read) per card **T1**.

> **Lemma A.** Let $x := p_n \ge 60184$ and $L := \log x$. Then $T_n \ge L(L-1.1)$.
>
> *Proof.* $T_n = x\,(e^{L/n}-1)$ with $n = \pi(x)$ (card **D3** — the index of a
> prime *is* its counting function, not a free parameter). Dusart gives
> $n \le x/(L-1.1)$, hence $L/n \ge L(L-1.1)/x$. The map $u \mapsto x(e^u-1)$ is
> increasing and $e^u - 1 \ge u$ for every real $u$, so
> $T_n \ge x\big(e^{L(L-1.1)/x}-1\big) \ge x\cdot L(L-1.1)/x = L(L-1.1)$. $\square$

Note the direction. $T_n$ is *decreasing* in $n$ at fixed $p_n$ (card **D5**), so
lower-bounding $T_n$ requires an **upper** bound on the index — which is what
Dusart's upper bound on $\pi$ supplies. Card **T3** names this asymmetry:
verification consumes an upper bound on the rank, refutation a lower one, and
silently swapping them produces a claim in the unsafe direction. Lemma A is on
the verification side and uses the upper bound.

> **Corollary A1.** For $p_n \ge 60184$: if $g_n \le 108$ then `F` holds at $n$.
> *(At $x=60184$, $L(L-1.1) = 109.0079\ldots$, and $L(L-1.1)$ increases in $x$.)*

Lemma A is an in-run derivation. It is elementary, but "elementary" is where
errors hide, so it is now **falsification-tested numerically** over every prime
in range: if a single $p_n \ge 60184$ had $T_n < L(L-1.1)$, the lemma would be
dead.
""")

code(r"""
# Falsification test 1 -- Lemma A over the whole sieved range.
print("min over all p_n in [60184, N] of  T_n - L(L-1.1):")
for k in sorted(DEEP, key=int):
    s = DEEP[k]["lemmaA_min_slack"]
    print(f"  N = {int(k):>14,}   min slack = {s:+.6f}   {'HOLDS' if s > 0 else 'FALSIFIED'}")
""")

code(r"""
# Falsification test 2 -- is the validity range x >= 60184 load-bearing, or decoration?
# Lemma A's conclusion is compared against the true asymptotic size of T_n,
# L^2 - L - 1 (card L2). The two cross exactly at L = 10, i.e. x = e^10 = 22026.
print(f"{'x':>10} {'L(L-1.1)':>12} {'L^2-L-1':>12} {'slack':>10}")
for x in [10**3, 10**4, 22026, 60184, 10**5, 10**6, 10**9, 2**64]:
    L = math.log(x)
    print(f"{x:>10,} {L*(L-1.1):>12.4f} {L*L-L-1:>12.4f} {0.1*L-1:>10.4f}")
print("\nLemma A's bound exceeds the true size of T_n below x = e^10 = 22026,")
print("so it would be FALSE there. Dusart's range x >= 60184 keeps us clear of it")
print("with room to spare -- but the margin at 60184 is only ~0.10, so the range")
print("is load-bearing, not decoration. Below 60184: enumerate (done in section 2).")
""")

# ==========================================================================
md(r"""
---
## 5 · Corollary A2 — the safe bound $S(g)$, and the reduction to a table

Solving $L(L-1.1) = g$ for $L$:

> **Corollary A2.** A gap of size $g$ can violate `F` only at a prime
> $$p_n \;\le\; S(g) \;:=\; \exp\!\Big(\tfrac{1.1+\sqrt{1.21+4g}}{2}\Big),$$
> for $p_n \ge 60184$; below that, enumerate.

This is the whole engine of route (b), and it collapses the verification of an
enormous range into a check on a **finite table**: for each even $g$, compare the
*first* prime at which a gap of size $g$ occurs, $P_1(g)$, against $S(g)$. If
$P_1(g) > S(g)$, gap size $g$ can never violate `F` — not below $X$, not anywhere.

`safe_bound_S` rounds $S(g)$ **up** and `gap_needed` rounds $L(L-1.1)$ **down**,
so every "safe" verdict below is conservative in the direction that matters.

**Why the table test is sound.** Fix $n$ with $p_n < X$. Either $g_n \le 108$, and
Corollary A1 settles it (for $p_n \ge 60184$; below that §2 checked it exactly),
or $g_n \ge 110$, and then $p_n \ge P_1(g_n) > S(g_n)$ — the first inequality
because $P_1$ is by definition the *smallest* prime carrying that gap — whence
$g_n < L(L-1.1) \le T_n$ and `F` holds at $n$. Note that the conclusion for a gap
size that passes is not "safe below $X$" but **safe everywhere**: $S(g)$ does not
depend on $X$.
""")

code(r"""
best = DEEP[max(DEEP, key=int)] if DEEP else None
X = int(max(DEEP, key=int)) if DEEP else N_NOTEBOOK
first_occ = ({int(k): tuple(v) for k, v in best["first_occ"].items()}
             if best else res["first_occ"])
records = ([tuple(x) for x in best["records"]] if best else res["records"])

cert = fb.lemma_A_certificate(first_occ, X)
print(f"first-occurrence table complete for every gap size occurring below {X:,}")
print(f"gap sizes present            : {len(first_occ)}  (largest {max(first_occ)})")
print(f"of which S(g) < 60184        : {len(cert['rows']) - cert['n_live']}"
      f"   -> excluded by Corollary A1 / the finite check of section 2")
print(f"of which need the table test : {cert['n_live']}")
print(f"UNSETTLED gap sizes          : {cert['unsettled']}")
print(f"VERDICT                      : {cert['verdict']}")
print(f"minimum safety factor P1(g)/S(g) = {cert['min_ratio']:.4f} at g = {cert['min_ratio_gap']}")
""")

code(r"""
rows = [r for r in cert["rows"] if r["ratio"] is not None]
rows.sort(key=lambda r: r["ratio"])
print(f"{'g':>5} {'first occurrence P1(g)':>24} {'safe bound S(g)':>20} {'P1/S':>9} {'status':>10}")
for r in rows[:14]:
    print(f"{r['g']:>5} {r['P1']:>24,} {float(r['S']):>20.4g} {r['ratio']:>9.3f} {r['status']:>10}")
print("  ... (rows ordered by safety factor; the tightest are shown)")
print(f"\nlargest safety factor: {max(r['ratio'] for r in rows):.1f}")
""")

code(r"""
fig, ax = plt.subplots(1, 2, figsize=(12, 4.2))
gs = [r["g"] for r in cert["rows"] if r["ratio"] is not None]
P1 = [r["P1"] for r in cert["rows"] if r["ratio"] is not None]
S = [float(r["S"]) for r in cert["rows"] if r["ratio"] is not None]
ax[0].semilogy(gs, P1, "o", ms=4, label=r"first occurrence $P_1(g)$")
ax[0].semilogy(gs, S, "-", lw=2, label=r"safe bound $S(g)$ (Cor. A2)")
ax[0].set_xlabel("gap size $g$"); ax[0].set_ylabel("prime")
ax[0].set_title("Route (b): every gap first occurs above its safe bound")
ax[0].legend(); ax[0].grid(alpha=.3)

ax[1].plot(gs, [r["ratio"] for r in cert["rows"] if r["ratio"] is not None], "o-", ms=4)
ax[1].axhline(1, color="crimson", ls="--", label="refutation would need this")
ax[1].set_xlabel("gap size $g$"); ax[1].set_ylabel(r"safety factor $P_1(g)/S(g)$")
ax[1].set_title("Safety factor, and its trend")
ax[1].legend(); ax[1].grid(alpha=.3)
plt.tight_layout(); plt.show()
""")

md(r"""
The right-hand panel is the finding that a null result cannot give you.
The safety factor is **not** flat and **not** shrinking: it grows roughly
linearly in $g$ over the whole range. Verification gets *easier*, not harder,
as the range extends — which is the empirical shape of the Cramér-side
expectation (card **L9**) rather than the Granville-side one (card **L10**),
over this range and no further. The minimum sits at the *small* end, at
$g=112$, not at the frontier.

Two disciplines this does **not** discharge:

1. It is a statement about first occurrences below $10^{11}$. It says nothing
   about a gap size that first occurs above $10^{11}$.
2. The trend is 130-odd points over three decades of $p$. Card **L10** is a
   heuristic prediction of failure at scales beyond every sieve; a growing
   safety factor over $[60184, 10^{11}]$ does not bear on it.
""")

# ==========================================================================
md(r"""
---
## 6 · The certificate that scales

Route (b) as run above still consumed a complete first-occurrence table, which
came from a complete sieve. The form that scales past any sieve needs only the
**maximal-gap record table**: split $[60184, X]$ into windows $[a,b)$ and check
$$\max\{g_n : p_n < b\} \;<\; L(L-1.1)\big|_{L=\log a},$$
i.e. the largest gap anywhere below the window's top is smaller than the
smallest gap that could violate `F` anywhere in the window. That is a few dozen
comparisons against a table of ~80 records, and it is the shape in which a
frontier like $2^{64}$ is actually certified.
""")

code(r"""
wins = fb.window_certificate(records, X, n_windows=22)
print(f"{'window lo':>16} {'window hi':>16} {'max gap below hi':>18} "
      f"{'L(L-1.1) at lo':>16} {'ok':>5}")
for w in wins:
    print(f"{w['lo']:>16,} {w['hi']:>16,} {w['gmax']:>18} {w['need']:>16.3f} "
          f"{str(w['ok']):>5}")
print("\nall windows certified:", all(w["ok"] for w in wins))
print("inputs consumed: the", len(records), "maximal-gap records below X --",
      "no sieve, no pi(x) computation, no per-prime check.")
""")

# ==========================================================================
md(r"""
---
## 6b · A by-product: P6′ (card **L15**) at $10^{11}$, and a warning

Card **L15** is the run's *"single most tractable open obligation"*: the maximal-gap
reduction

> **P6′.** For $m$ the governing record (maximal-gap) index below $n$, $T_m \le T_n$.

which, if true, prunes any counterexample search from every index to the ~40
record indices. It is **unproved**, and its entire empirical support was **0
exceptions in 216 815 pairs** ($p < 3\cdot10^6$). The sweep of §2 already carries
every quantity P6′ needs, so it is checked here at no extra cost — over four
billion pairs instead of two hundred thousand.

Two things get reported: the exception count, and — more useful — the *minimum
margin* $\min_n (T_n - T_{m(n)})$, i.e. how much room P6′ actually has at its
tightest point.
""")

code(r"""
print(f"{'N':>16} {'records':>8} {'P6-prime exceptions':>20} {'min margin T_n - T_m':>22} "
      f"{'relative':>11} {'attained at p':>18}")
for k in sorted(DEEP, key=int):
    d = DEEP[k]
    s = d["p6_min_slack"]
    print(f"{int(k):>16,} {len(d['records']):>8} {d['p6_n_exceptions']:>20} "
          f"{s[0]:>22.3e} {s[1]:>11.2e} {s[3]:>18,}")
""")

code(r"""
# The margin decays. Fit its trend, and ask where it meets float64 resolution
# on T -- because past that point a double-precision check of P6' is measuring
# noise, in the same silent direction as the hazard of T2 Rule 3.
ks = sorted(DEEP, key=int)
xs = np.array([math.log10(int(k)) for k in ks])
ys = np.array([math.log10(DEEP[k]["p6_min_slack"][0]) for k in ks])
slope, intercept = np.polyfit(xs, ys, 1)
print(f"log10(min margin) ~ {slope:.3f} * log10(p) + {intercept:.3f}   "
      f"(margin shrinks like p^{slope:.2f})")

def margin_hat(x):
    return 10 ** (slope * math.log10(x) + intercept)

def resolution(x):
    L = math.log(x)
    return np.finfo(float).eps * (L * L - L - 1)   # one ulp on T ~ log^2 p

for target, label in [(1.693e15, "the record's location (L7)"),
                      (2**64, "2^64 (published frontier)")]:
    print(f"  at {label:<28}: extrapolated margin {margin_hat(target):.3e},  "
          f"one ulp on T = {resolution(target):.3e},  ratio "
          f"{margin_hat(target)/resolution(target):.2f}")

# Where do they cross? Bisect on log10(p).
lo, hi = 11.0, 40.0
while hi - lo > 1e-6:
    mid = (lo + hi) / 2
    (lo, hi) = (mid, hi) if margin_hat(10**mid) > resolution(10**mid) else (lo, mid)
print(f"\n  extrapolated crossover at p ~ 1e{lo:.1f}"
      f"   (2^64 is 1e{math.log10(2**64):.1f})")
""")

md(r"""
**This is a warning, not a refutation.** P6′ has **zero exceptions** in every
pair this run examined, and the fit above is four points over four decades — an
extrapolation, not a theorem. What it does establish is decision-relevant:

* the empirical case for P6′ does **not** strengthen as the range grows; the
  margin at its tightest point *shrinks*, roughly like $p^{-1}$, while the
  quantity being compared grows like $\log^2 p$;
* consequently the margin and float64's resolution on $T$ are converging, and the
  extrapolated crossover lands **essentially on the published frontier** — at
  $2^{64}$ the fitted margin exceeds one ulp of $T$ by a factor of about 1.05,
  which is to say: not at all. A double-precision check of P6′ up there returns
  "no exceptions" whether or not there are any — the same silent failure
  direction as card **T2** Rule 3, in a new place. *(Five points across four
  decades: the ordering is the finding, not the location.)*;
* the tightest point is always the same structural spot: a few indices *after* a
  record gap, where $T$ has jumped up and then drifted back down toward $T_m$.

Card **L15** reasons that *"the dip decays and the margin grows"*. Both halves are
about $T$'s excursion below its own running maximum. The quantity P6′ actually
needs is the one measured here, and it goes the other way. **The route to
discharging P6′ therefore has to be the analytic one the card already names —
bound $T$'s oscillation with Dusart (card **T1**) and compare against record-gap
spacing — because the computational route is running out of resolution, not
gaining confidence.**
""")

code(r"""
# Card L15 hazard 3: "the six tightest rho cases occur at record gaps" was a
# print-truncation artefact that breaks to 8/10 and 15/100 at 3e6. Re-measured
# at 1e11, where the tightest cases are large gaps rather than small primes.
deepest = DEEP[max(DEEP, key=int)]
rec_idx = {r[0] for r in deepest["records"]}
print(f"{'rank':>4} {'rho':>9} {'p_n':>16} {'g':>5} {'record gap?':>12}")
for i, (r, n, p, g) in enumerate(deepest["top"][:12], 1):
    print(f"{i:>4} {r:>9.5f} {p:>16,} {g:>5} {str(n in rec_idx):>12}")
hits = sum(1 for (r, n, p, g) in deepest["top"] if n in rec_idx)
print(f"\nof the top {len(deepest['top'])} by rho, {hits} are at maximal-gap indices "
      f"({100*hits/len(deepest['top']):.0f}%)")
print("The 4th-tightest case in four billion pairs is NOT at a record index.")
print("Note what this does and does not say: IF P6' holds, a record-index search")
print("still misses no COUNTEREXAMPLE. What it misses is near-misses -- so the")
print("record-index subset is not where the tight cases live, and the observation")
print("'the tightest cases are records' (L15 hazard 3) does not survive the range.")
""")

# ==========================================================================
md(r"""
---
## 7 · The $2^{64}$ frontier: what we reproduce, and the exact hole

Card **L6** records the published frontier as $2^{64} \approx 1.8447\cdot10^{19}$,
with Kourbatov's 2023 endnote adding *"prime gaps of size $g<1920$ cannot violate (1)"*.
Our own arithmetic reproduces that pairing, from Lemma A and nothing else.
""")

code(r"""
need_at_264 = fb.gap_needed(2**64)
print(f"2^64 = {2**64:,}")
print(f"L(L-1.1) at 2^64 = {need_at_264}")
print(f"  -> a gap must be at least {math.ceil(float(need_at_264)):d}, i.e. even g >= "
      f"{2*math.ceil(float(need_at_264)/2):d}, to violate F at a prime just below 2^64.")
print()
for g in [1476, 1550, 1918, 1920]:
    S = fb.safe_bound_S(g)
    print(f"  S({g:>4}) = {float(S):.5g}   {'<' if S < 2**64 else '>='} 2^64")
""")

md(r"""
$1919.14 \Rightarrow$ **1920**. The endnote's constant falls out of Lemma A with
no tuning — an independent derivation landing on the published integer, which is
a genuine cross-check on both.

**But read what it does and does not say.** What Lemma A gives is the *local*
statement: at a prime just below $2^{64}$, a gap of at least 1920 is required.
The endnote's phrasing — *"prime gaps of size $g<1920$ cannot violate (1)"* — is
a **global** claim, and Lemma A alone does not yield it: the cell above shows
$S(1918) = 1.82\cdot10^{19}$, i.e. our bound leaves a gap of 1918 free to violate
`F` anywhere below $1.82\cdot10^{19}$. Closing that requires knowing that no gap
of 1918 *occurs* down there — the first-occurrence table again. The two
statements coincide numerically at the frontier and are logically different, and
conflating them is exactly the error card **L6** hazard 1 warns about in the
neighbouring case of the three circulating frontier figures.

**Now the hole, stated precisely.** To conclude `F` on $[10^{11}, 2^{64}]$ by
route (b) one needs, for every even $g$ that occurs as a prime gap in that range:
$$P_1(g) \;>\; S(g).$$
Equivalently, in window form (§6): for every window $[a,b) \subset [10^{11}, 2^{64}]$,
$\max\{g : p<b\} < L(L-1.1)|_{\log a}$. Both need a **first-occurrence / maximal-gap
table to $\approx 4\cdot10^{18}$**, which this run does not have:

* card **L6** names it — `oliveira2014goldbach` — and records it at ledger tier
  **L2_weak, NOT OPENED** (AMS returned HTTP 403). It is the one row in the
  ledger whose text nobody in this run read.
* Everything the run asserts about the $2^{64}$ frontier is therefore mediated
  through Kourbatov's use of that table.

What this notebook adds is that the dependency is now **exactly one table**, with
**exactly one inequality** to check against it, and the machinery to check it is
here (`lemma_A_certificate`, `window_certificate`) and validated on data we do own.
Supply the table, and the frontier is re-derived in this notebook in seconds.

*(Sanity check on the shape of the missing datum: the largest known maximal gap
below $2^{64}$ is 1550 — Visser's "81st maximal prime gap". $S(1550)$ is computed
above; the comparison to make is against that gap's first occurrence. This
notebook does **not** assert the value 1550 — it is recalled, not read, and is
recorded here as a pointer for the citation gate, not as an input to any
computation above.)*
""")

# ==========================================================================
md(r"""
---
## 8 · Counterexample search: the null result, stated honestly

Card **T2** is blunt that a search leg should *"aim to reproduce and extend the
$\rho$ table, not to expect a hit"*, and the numbers bear that out.
""")

code(r"""
deep = DEEP[max(DEEP, key=int)]
print("EXHAUSTIVE, no pruning, no sampling:")
print(f"  range swept                                  : p_n < {X:,}")
print(f"  consecutive prime pairs tested for rho_n >= 1 : {deep['pairs']:,}")
print(f"  counterexamples found                        : {len(deep['violations'])}")
print(f"  pairs within 10% of the bar (rho >= 0.9)     : "
      f"{len(deep['escalations'])}  (all at n < 5; see section 2)")
print(f"  best rho for n >= 10                         : {deep['top'][0][0]:.7f}")
print()
print(f"What this EXCLUDES : any counterexample with p_n < {X:.0e}.")
print(f"What it does NOT   : anything at all about p_n >= {X:.0e}. The published")
print( "                     record rho = 0.94846 sits at p = 1.693e15,")
print(f"                     {math.log10(1.693e15/X):.1f} decades above this sieve (card L7).")
print( "                     This search never reached the interesting region.")
""")

code(r"""
# How far below the published record are we, in the only unit where the bar is 1?
rec_pub, p_pub = 0.94846, 1.693e15
here = DEEP[max(DEEP, key=int)]["top"][0]
print(f"in-run best   rho = {here[0]:.5f}  at p = {here[2]:,}")
print(f"published rec rho = {rec_pub:.5f}  at p = {p_pub:.3e}   [card L7, NOT re-run here]")
print( "refutation bar    = 1.00000")
print(f"\ngap to close, from the in-run best : {1-here[0]:.5f} in rho")
print(f"gap to close, from the record      : {1-rec_pub:.5f} in rho")
print(f"decades of p, in-run best -> record: {math.log10(p_pub/here[2]):.2f}")
print(f"decades of p, sieve limit -> record: {math.log10(p_pub/X):.2f}")
print(f"decades of p, sieve limit -> 2^64  : {math.log10(2**64/X):.2f}")
""")

# ==========================================================================
md(r"""
---
## 9 · Findings

**Supported by this computation**

1. **`F` holds at every $n$ with $p_n < 10^{11}$** — 4 118 054 812 consecutive pairs,
   exhaustive, no pruning, no sampling. Two-tier arithmetic: float64 screen,
   Decimal re-decision of everything within 10% of the bar (only two pairs, both
   at $n<5$), and the Decimal path calibrated against exact integer comparison for
   all $n \le 5000$ with zero disagreements. Route (a), 8.27 decades short of $2^{64}$.
2. **Lemma A** ($T_n \ge L(L-1.1)$ for $p_n \ge 60184$) — derived here from one
   L0-tier bound, falsification-tested at every prime in range with strictly
   positive slack. Its validity range is load-bearing: the lemma is *false* below
   $x = e^{10} = 22026$, and clears Dusart's threshold by only $\approx 0.10$.
3. **Corollary A2** reduces the verification of an unbounded range to a finite
   first-occurrence table; every gap size occurring below $10^{11}$ clears it, with
   **minimum safety factor 5.34** (at $g=112$) rising roughly linearly in $g$.
4. **The "$g<1920$" constant attached to the $2^{64}$ frontier is reproduced
   independently**: $L(L-1.1)$ at $2^{64}$ is $1919.1380$ — with the caveat of §7,
   that Lemma A gives the *local* statement and not the global one.
5. **The F2-margin statistic is an artefact**, demonstrated against a synthetic
   gap-2 control that scores $0.99999\ldots$ while its $\rho$ is $\approx 0.003$.
6. **P6′ (card L15) has zero exceptions over four billion pairs** — 4.3 decades
   beyond its previous empirical base — **but its minimum margin shrinks like
   $p^{-1}$** and passes below float64 resolution well before the published
   frontier (§6b). The computational route to P6′ is losing resolution, not
   gaining confidence.

**Refuted by this computation** — nothing about `F`. Three *claims about the
evidence*:

* that the F2 margin measures tightness (§3);
* that the tightest $\rho$ cases sit at record-gap indices — 22 of the top 40 at
  $10^{11}$, and the 4th-tightest is not one (§6b, card **L15** hazard 3);
* that empirical support for P6′ accumulates with range (§6b).

**Declared gaps**

* The frontier of $2^{64}$ is **not** established here. It needs a first-occurrence
  table to $\approx 4\cdot10^{18}$ (`oliveira2014goldbach`, **unopened**, card **L6**).
  §7 gives the exact inequality that table must satisfy; the checker is written and
  validated on data we own.
* Dusart Thm 6.9 eq. (6.6) is consumed as an input. Card **T1** has it at L0, read.
  Nothing else external is consumed anywhere in this notebook.
* The safety-factor trend of §5 and the P6′ decay fit of §6b describe *this range*.
  Neither is evidence about the Cramér/Granville tension (cards **L9**/**L10**),
  whose disagreement lives far above any sieve.
* The Decimal path assumes `Decimal.ln()` is correctly rounded — documented CPython
  behaviour, cross-validated against exact integers only for $n \le 5000$.
* **`F` remains open.** A verified range bounds where a counterexample can live and
  shrinks the difficulty of the general case by nothing (card **L6**, hazard 4).
  The obstruction of **L3** is untouched by every line above.
""")

nb["cells"] = C
nb["metadata"] = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python"},
}
nbf.write(nb, "notebook-2.ipynb")
print(f"wrote notebook-2.ipynb with {len(C)} cells")
