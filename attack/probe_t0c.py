import math
# uniform separation constants, including the exponential correction eps
print("=== Dusart form: need 2*l*d + d^2 - 1.1*d - 0.1*l >= eps,  eps=(l^2-l)^2/p, p=max(e^l,60184)")
worst=0
for l in [x/20 for x in range(220, 4000)]:
    p=max(math.exp(l),60184.0); eps=(l*l-l)**2/p
    d=(0.1*l+eps)/(2*l-1.1)
    if d>worst: worst=d; wl=l
print(f"  max required d = {worst:.6f} at l={wl:.3f}  -> window 1-e^-d = {1-math.exp(-worst):.4%}")
print(f"  check d=0.0623 valid everywhere: {all((0.1*l+ (l*l-l)**2/max(math.exp(l),60184.0)) <= 0.0623*(2*l-1.1) for l in [x/20 for x in range(220,8000)])}")

print("=== Axler form: need d*(2l-1) >= 0.17 - 1/l + eps,  eps=(l^2)^2/p, p=max(e^l,1772201)")
worst=0
for l in [x/20 for x in range(288, 4000)]:
    p=max(math.exp(l),1772201.0); eps=(l*l)**2/p
    d=(0.17-1/l+eps)/(2*l-1)
    if d>worst: worst=d; wl=l
print(f"  max required d = {worst:.6f} at l={wl:.3f}  -> window {1-math.exp(-worst):.4%}")
for l in (math.log(2**64), 50., 100., 200.):
    p=math.exp(l); eps=(l*l)**2/p; d=(0.17-1/l+eps)/(2*l-1)
    print(f"  l={l:8.3f}: d={d:.6g}  window={1-math.exp(-d):.5%}   0.085/l={0.085/l:.6g}")
