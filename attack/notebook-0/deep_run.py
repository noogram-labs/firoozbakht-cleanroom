"""Headline deep sweep. Writes a JSON summary next to the notebook."""
import json, sys, time
import ffm_lab as fl

N = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**11
BLOCK = 1 << 30
t0 = time.time()
last = [t0]
def prog(S):
    now = time.time()
    print(f"  p<={S.p_last:>14,}  n={S.n_last:>14,}  recs={len(S.records)}  "
          f"viol={len(S.violations)}  ffm_exc={len(S.ffm_exceptions)}  "
          f"minmarg={S.ffm_min_margin:.6f}  [{now-t0:7.1f}s]", flush=True)
    last[0] = now

S = fl.run_sweep(N, block=BLOCK, progress=prog)
el = time.time() - t0
out = dict(
    n_max=N, elapsed_s=el, n_last=S.n_last, p_last=S.p_last,
    violations=S.violations, audit_queue=S.audit_queue,
    records=S.records, n_records=len(S.records),
    ffm_exceptions=S.ffm_exceptions, ffm_min_margin=S.ffm_min_margin,
    ffm_argmin=S.ffm_argmin, ffm_by_decade={str(k): v for k, v in S.ffm_by_decade.items()},
    t_dip_max=S.t_dip_max, t_dip_argmax=S.t_dip_argmax,
    t_dip_by_decade={str(k): v for k, v in S.t_dip_by_decade.items()},
    t_down_steps=S.t_down_steps, t_steps=S.t_steps,
    tightest=S.tightest,
)
with open(f"deep_run_{N:.0e}.json".replace("+", ""), "w") as f:
    json.dump(out, f, indent=1)
print(f"DONE {N:.0e} in {el:.1f}s -> viol={len(S.violations)} ffm_exc={len(S.ffm_exceptions)} "
      f"minmarg={S.ffm_min_margin}", flush=True)
