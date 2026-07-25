"""
deep_run — run fb_core.scan at several scales and record the results.

The notebook itself runs at a small default scale so that it executes in
seconds.  The large scales are recorded here, once, into `deep-runs.json`,
and the notebook reads that file.  Same code path in both cases: the notebook
imports `fb_core`, and so does this script.

    python3 deep_run.py                 # 1e7 .. 1e10
    python3 deep_run.py 11              # 1e7 .. 1e11

Timing observed on the run machine (Apple silicon, CPython 3.10, numpy 2.2):
1e8 ~ 0.4 s, 1e9 ~ 4 s, 1e10 ~ 60 s, 1e11 ~ 12 min.
"""
import json
import sys

import fb_core as fb


def jsonable(r: dict) -> dict:
    out = dict(r)
    out["first_occ"] = {str(k): list(v) for k, v in r["first_occ"].items()}
    out["records"] = [list(x) for x in r["records"]]
    out["top"] = [list(x) for x in r["top"]]
    out["escalations"] = [list(x) for x in r["escalations"]]
    out["violations"] = [list(x) for x in r["violations"]]
    out["max_f2"] = list(r["max_f2"])
    out["max_c"] = list(r["max_c"])
    return out


def main() -> None:
    top_exp = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    runs = {}
    for e in range(7, top_exp + 1):
        N = 10**e
        seg = 10**7 if e <= 9 else 2 * 10**8
        r = fb.scan(N, seg=seg)
        runs[str(N)] = jsonable(r)
        with open("deep-runs.json", "w") as fh:
            json.dump(runs, fh, indent=1)
        print(f"  wrote 1e{e}: max rho {r['top'][0][0]:.7f} at n={r['top'][0][1]} "
              f"p={r['top'][0][2]} g={r['top'][0][3]}; "
              f"violations={len(r['violations'])}; "
              f"max gap {r['records'][-1][2]} at p={r['records'][-1][1]}",
              flush=True)


if __name__ == "__main__":
    main()
