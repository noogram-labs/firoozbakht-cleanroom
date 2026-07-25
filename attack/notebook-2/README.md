# notebook-2 — the unconditional verified range

Leg `notebooks__2` of run `germ-20260725-791a7c45`, molecule `task-20260725-09a7`.
Target: **`unconditional-verified-range`** (target #2).

Firoozbakht's conjecture `F` is **OPEN** here. Nothing in this directory proves it.
Computation corroborates or refutes; it never constitutes the proof.

## Files

| file | what it is |
|---|---|
| `notebook-2.ipynb` | the deliverable, executed with outputs |
| `findings.md` | the findings note: what is supported, what is refuted, at what scale, what is missing |
| `fb_core.py` | sieve, ρ-scan, exact / certified verdicts, Lemma A and its certificates |
| `test_fb_core.py` | every claim the notebook makes, as a headless assertion |
| `deep_run.py` | records the large-scale runs into `deep-runs.json` |
| `deep-runs.json` | results at 1e7 … 1e11 (the notebook reads this; it does not re-run them) |
| `build_notebook.py` | regenerates `notebook-2.ipynb` from source |

## Run it

```sh
python3 test_fb_core.py                                     # ~40 s, exits non-zero on failure
python3 deep_run.py 10                                      # ~70 s   (add `11` for ~13 min more)
python3 build_notebook.py
jupyter nbconvert --to notebook --execute --inplace notebook-2.ipynb
```

Requires `numpy`, `matplotlib`, `nbformat`, `jupyter`. No network access, no data
files, no external tables — see `findings.md` §"Declared gaps" for the one
external table the *published* frontier needs and this run does not have.
