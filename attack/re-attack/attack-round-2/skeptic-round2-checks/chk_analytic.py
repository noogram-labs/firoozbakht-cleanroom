"""Skeptic round-2: independent recomputation of the ANALYTIC claims.
Written from the STATEMENTS in the round-2 attempts, not from their code."""
from mpmath import mp, mpf, log, exp, sqrt, findroot
mp.dps = 50

L1 = log(mpf(1772201))          # ell_1  (Axler a=1 row)
LA = log(mpf(6690557))          # ell_A  (Axler a=2.1 row)
LD = log(mpf(10)**8)            # ell_D  (FFM Dusart small-branch cutoff)
L0d = log(mpf(60184))           # Dusart (D-low) threshold
lam64 = log(mpf(2)**64)

print("=== basic constants ===")
print("ell_1  =", L1)
print("ell_A  =", LA)
print("ell_D  =", LD)
print("log 60184 =", L0d)
print("log 2^64 =", lam64, " lam^2-1.1lam =", lam64**2 - mpf('1.1')*lam64)

# ---------- bars ----------
def v_ax(l, a):      # Axler row (a,0,0,0):  v = l^2 - l - 1 - a/l
    return l*l - l - 1 - mpf(a)/l
def v_du(l):         # Dusart:  v = l^2 - l
    return l*l - l

def bar_tight(l, a=1):
    v = v_ax(l, a); x = exp(l); return v*(1+v/x)
def bar_row1(l):     # v(1+l^2/x)
    v = v_ax(l,1); x = exp(l); return v*(1+l**2/x)
def bar_row2(l):     # v + l^4/x  (additive weakening)
    v = v_ax(l,1); x = exp(l); return v + l**4/x
def bar_row3(l):     # v(1+l^4/x)  -- as printed in PA-0
    v = v_ax(l,1); x = exp(l); return v*(1+l**4/x)
def bar_dusart(l):
    v = v_du(l); x = exp(l); return v*(1+v/x)

# ---------- required d, SOLVED from Lemma W's hypothesis  C(p_m) <= A(p_n0) ----------
def req_d_axler(l, barfn):        # A(lam) = lam^2 - lam - 1.17
    C = barfn(l)
    lam = (1 + sqrt(1 + 4*(C + mpf('1.17'))))/2
    return lam - l
def req_d_dusart(l):              # A(lam) = lam^2 - 1.1 lam
    C = bar_dusart(l)
    lam = (mpf('1.1') + sqrt(mpf('1.21') + 4*C))/2
    return lam - l

def scan(f, a, b, n=40000):
    best = mpf(-10); arg = None
    for i in range(n+1):
        l = a + (b-a)*mpf(i)/n
        y = f(l)
        if y > best: best, arg = y, l
    return best, arg

print("\n=== UVR §3.1 table: max required d over [ell_1, 300], solved from Lemma W ===")
for name, fn in [("row0 tight v(1+v/x)", lambda l: req_d_axler(l, bar_tight)),
                 ("row1 v(1+l^2/x)",     lambda l: req_d_axler(l, bar_row1)),
                 ("row2 v+l^4/x",        lambda l: req_d_axler(l, bar_row2)),
                 ("row3 v(1+l^4/x) PRINTED", lambda l: req_d_axler(l, bar_row3))]:
    m, arg = scan(fn, L1, mpf(300))
    print(f"  {name:26s} max={mp.nstr(m,12)}  at ell={mp.nstr(arg,10)}   (<=0.004479? {m<=mpf('0.004479')})")

print("\n=== UVR error terms at ell_1 (V1) ===")
v = v_ax(L1,1); x = exp(L1)
print("  v(ell_1)            =", mp.nstr(v,15))
print("  tight   v(1+v/x)    =", mp.nstr(bar_tight(L1),15), " err=", mp.nstr(bar_tight(L1)-v,12))
print("  row1    v(1+l^2/x)  =", mp.nstr(bar_row1(L1),15), " err=", mp.nstr(bar_row1(L1)-v,12))
print("  row2    v+l^4/x     =", mp.nstr(bar_row2(L1),15), " err=", mp.nstr(bar_row2(L1)-v,12))
print("  row3    v(1+l^4/x)  =", mp.nstr(bar_row3(L1),15), " err=", mp.nstr(bar_row3(L1)-v,12))
print("  ratio printed/tight err =", mp.nstr((bar_row3(L1)-v)/(bar_tight(L1)-v),10))

print("\n=== UVR Prop R1 certificates ===")
E  = lambda l: v_ax(l,1)**2 * exp(-l)
q  = lambda l: l*l - 5*l + 1 - 1/l - 2/(l*l)
dstar = lambda l: (mpf('0.17') - 1/l + E(l))/(2*l-1)
print("  E(ell_1)        =", mp.nstr(E(L1),12))
print("  q(ell_1)        =", mp.nstr(q(L1),10), "(claim 135.98903)")
print("  4/l-1/l^2 at l1 =", mp.nstr(4/L1 - 1/L1**2,10), " 2K =", mp.nstr(2*(mpf('0.17')+E(L1)),10))
print("  d*(ell_1)       =", mp.nstr(dstar(L1),12), "(claim 0.004363567696)")
m,arg = scan(dstar, L1, mpf(300)); print("  max d* on [l1,300] =", mp.nstr(m,12), "at", mp.nstr(arg,10))
print("  psi(l1)=l1^5 e^-l1 =", mp.nstr(L1**5*exp(-L1),12), "(claim 0.3478955285)")
print("  l1*E(l1)           =", mp.nstr(L1*E(L1),12), "(claim 0.2978804323)")
print("  0.17/(2l1-1)       =", mp.nstr(mpf('0.17')/(2*L1-1),12), "(claim 0.006120509446)")
print("  PA-0 displayed crit max (0.17-1/l+l^4/x)/(2l-1):")
m,arg = scan(lambda l:(mpf('0.17')-1/l+l**4*exp(-l))/(2*l-1), L1, mpf(300))
print("     ", mp.nstr(m,12), "at", mp.nstr(arg,10), "(claim 0.0044887225)")
print("  e^-0.0043635677 =", mp.nstr(exp(-mpf('0.0043635677')),10), " e^-0.004479 =", mp.nstr(exp(-mpf('0.004479')),10))

print("\n=== UVR V5: ell where PRINTED required d falls to 0.004479 ===")
f = lambda l: req_d_axler(l, bar_row3) - mpf('0.004479')
r = findroot(f, mpf(21))
print("  ell =", mp.nstr(r,12), " p_m =", mp.nstr(exp(r),10), "(claim 21.00996466 / 1.332023e9)")

print("\n=== UVR V6 / FFM: Theorem C(a) exact required d ===")
m,arg = scan(req_d_dusart, L0d, mpf(300))
print("  max over [log 60184,300] =", mp.nstr(m,12), "at ell=", mp.nstr(arg,10), "(claim 0.062079811 at 11.005162)")
print("  eps(l0) = (l^2-l)^2 e^-l =", mp.nstr(v_du(L0d)**2*exp(-L0d),12), "(claim 0.20144665)")

print("\n=== FFM Theorem C-a' (Dusart, small branch raised to 1e8) ===")
m,arg = scan(req_d_dusart, LD, mpf(1000))
print("  EXACT max required d on [log1e8,1000] =", mp.nstr(m,12), "at", mp.nstr(arg,10), "(claim 0.051493457)")
# majorant over cells of width 0.01
def maj_a(a,b): return (mpf('0.1')*b + a**4*exp(-a))/(2*a-mpf('1.1'))
best=mpf(-1); barg=None; a=LD
while a < 1000:
    b=a+mpf('0.01'); y=maj_a(a,b)
    if y>best: best,barg=y,a
    a=b
print("  majorant max (cells 0.01) =", mp.nstr(best,12), "at a=", mp.nstr(barg,10), "(claim 0.051599027)")
print("  tail l>=1000: (100+1000^4 e^-1000)/1998.9 =", mp.nstr((mpf(100)+mpf(1000)**4*exp(-1000))/mpf('1998.9'),10))
print("  e^-0.0516 =", mp.nstr(exp(-mpf('0.0516')),10), "(claim 0.94970867)")

print("\n=== FFM Theorem C-b' (Axler a=2.1, threshold 6690557) ===")
bar_ffm = lambda l: bar_tight(l, a='2.1')
m,arg = scan(lambda l: req_d_axler(l, bar_ffm), LA, mpf(300))
print("  EXACT max required d on [l_A,300] =", mp.nstr(m,12), "at", mp.nstr(arg,10), "(claim 0.0017560603)")
def maj_b(a,b): return (mpf('0.17') - mpf('2.1')/b + a**4*exp(-a))/(2*a-1)
best=mpf(-1); barg=None; a=LA
while a < 300:
    b=a+mpf('0.01'); y=maj_b(a,b)
    if y>best: best,barg=y,a
    a=b
print("  majorant max (cells 0.01) =", mp.nstr(best,12), "at a=", mp.nstr(barg,10), "(claim 0.0017568759 at 24.40621)")
print("  tail l>=300: (0.17+300^4 e^-300)/599 =", mp.nstr((mpf('0.17')+mpf(300)**4*exp(-300))/599,10), "(claim 0.00028381)")
print("  e^-0.0017569 =", mp.nstr(exp(-mpf('0.0017569')),10), "(claim 0.99824467)")
print("  v(l_A) for a=2.1 =", mp.nstr(v_ax(LA,'2.1'),10), "(claim 230.1)")
print("  v(5393) dusart   =", mp.nstr(v_du(log(mpf(5393))),8), "(claim 65.2)")

print("\n=== RH: Lemma A.1 ===")
k = mpf(25)/22
xs = (2*k)**2
print("  x* =", mp.nstr(xs,17), " h(x*) =", mp.nstr(sqrt(xs)-k*log(xs),20), "(claim 0.40686238165947680)")

print("\n=== Kourbatov bar S(g) ===")
S  = lambda g: exp((mpf('1.1')+sqrt(mpf('1.21')+4*mpf(g)))/2)
SK = lambda g: exp((1+sqrt(1+4*(mpf(g)+mpf('1.17'))))/2)
print("  2^64 =", mp.nstr(mpf(2)**64,12))
for g in (1918,1920): print(f"  S({g}) =", mp.nstr(S(g),12))
for g in (1922,1924): print(f"  S_K({g}) =", mp.nstr(SK(g),12))
print("  B(60184)=L^2-1.1L =", mp.nstr(L0d**2-mpf('1.1')*L0d,12), "(claim 109.00791)")

print("\n=== UVR Prop 3 window ===")
h = lambda p: p - 25*log(p)**3*(log(p)-mpf('1.1'))
for p in (396738, 777600, 777601):
    print(f"  h({p}) =", mp.nstr(h(mpf(p)),10))
print("  root p* =", mp.nstr(findroot(h, mpf(777600)),12), "(claim 777600.7443)")

print("\n=== RH F8 shortfall ===")
sf = mpf(2)**64 - mpf('1.836e19')
print("  2^64-1.836e19 =", mp.nstr(sf,8), " pct =", mp.nstr(100*sf/mpf(2)**64,6), " /log2^64 =", mp.nstr(sf/lam64,6))
