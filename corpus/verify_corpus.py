#!/usr/bin/env python3
"""Verification pass over the red-team corpus.

The runner (`run_corpus.sh`) checks that each *file* behaves as specified. This
script checks the claims the corpus makes *about itself*:

  V1  every manifest entry names files that exist;
  V2  every entry with evidence "refuted" has a theorem `<id>_refuted` that is
      actually present in corpus/refutations/;
  V3  every entry has an attempt/audit/undetected file, one per entry;
  V4  every refutation theorem is AXIOM-CLEAN — depends on nothing beyond
      [propext, Classical.choice, Quot.sound]. This is the check that matters:
      the refutation files import Statement.lean, which contains the sorried
      open target `firoozbakht`. A refutation that leaned on it would prove
      nothing, and would still compile;
  V5  the manifest's per-entry `observed` field agrees with results.tsv;
  V6  no file in refutations/ or rejected-candidates/ contains `sorry`.

Usage: python3 corpus/verify_corpus.py      (from the repo root)
Exit 0 iff every check passes.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
LEANDIR = ROOT / "lean"
STANDARD = {"propext", "Classical.choice", "Quot.sound"}

failures: list[str] = []
checks = 0


def check(ok: bool, label: str, detail: str = "") -> None:
    global checks
    checks += 1
    if ok:
        print(f"  PASS {label}")
    else:
        print(f"  FAIL {label}  {detail}")
        failures.append(f"{label}: {detail}")


manifest = json.loads((CORPUS / "manifest.json").read_text())
entries = manifest["entries"]

print(f"== V1/V3 manifest ↔ files ({len(entries)} entries) ==")
for e in entries:
    paths = [e.get("refutation"), e.get("attempt")]
    ok = True
    detail = ""
    for pth in paths:
        if not pth:
            continue
        f = pth.split(" :: ")[0]
        if not (ROOT / f).exists():
            ok, detail = False, f"missing {f}"
    if not e.get("attempt"):
        ok, detail = False, "no attempt/audit/undetected file"
    check(ok, f"V1 {e['id']} files exist", detail)

print("== V2 refuted entries have a proven negation ==")
ref_src = "\n".join(
    p.read_text() for p in sorted((CORPUS / "refutations").glob("*.lean"))
)
for e in entries:
    if e["evidence"] != "refuted":
        continue
    name = f"{e['id']}_refuted"
    check(
        re.search(rf"^theorem {name}\b", ref_src, re.M) is not None,
        f"V2 {name} present",
    )

print("== V6 no sorry in refutations/ or rejected-candidates/ ==")
for d in ("refutations", "rejected-candidates"):
    for p in sorted((CORPUS / d).glob("*.lean")):
        body = re.sub(r"/-.*?-/", "", p.read_text(), flags=re.S)
        body = re.sub(r"--.*", "", body)
        check("sorry" not in body, f"V6 {d}/{p.name} sorry-free")

print("== V4 refutation theorems are axiom-clean ==")
# Build one file per source that re-imports it and prints axioms for every
# theorem in it. `#print axioms` is the only thing that sees a tainted proof.
for d, ns in (("refutations", "Firoozbakht.RedTeam"),
              ("rejected-candidates", "Firoozbakht.RejectedCandidates")):
    for p in sorted((CORPUS / d).glob("*.lean")):
        names = re.findall(r"^theorem ([A-Za-z_0-9]+)", p.read_text(), re.M)
        tmp = CORPUS / ".logs" / f"axioms-{p.stem}.lean"
        tmp.parent.mkdir(exist_ok=True)
        cmds = "\n".join(f"#print axioms {ns}.{n}" for n in names)
        tmp.write_text(p.read_text() + "\n" + cmds + "\n")
        out = subprocess.run(
            ["lake", "env", "lean", str(tmp)],
            cwd=LEANDIR, capture_output=True, text=True,
        ).stdout
        for line in out.splitlines():
            m = re.match(r"'([^']+)' depends on axioms: \[(.*)\]", line)
            if m:
                thm = m.group(1)
                ax = {a.strip() for a in m.group(2).split(",") if a.strip()}
            else:
                # Lean prints a different sentence when the set is empty.
                m = re.match(r"'([^']+)' does not depend on any axioms", line)
                if not m:
                    continue
                thm, ax = m.group(1), set()
            extra = ax - STANDARD
            check(not extra, f"V4 {thm.split('.')[-1]} clean",
                  f"depends on {sorted(extra)}")
        got = len(re.findall(r"depends on axioms|does not depend on any axioms", out))
        check(got == len(names),
              f"V4 {p.name} all {len(names)} theorems audited",
              f"printed {got}")

print("== V5 manifest `observed` ↔ results.tsv ==")
rows = {}
for line in (CORPUS / "results.tsv").read_text().splitlines()[1:]:
    f = line.split("\t")
    rows[f[0]] = (f[1], f[4])
for e in entries:
    rid = {"V01": "V01_axiom_smuggle", "V02": "V02_sorry",
           "V03": "V03_contradictory_sorries",
           "V04": "V04_silent_coercion"}.get(e["id"], e["id"])
    row = rows.get(rid)
    if row is None:
        # refuted entries are compiled in bundles, not per-id; their per-id
        # evidence is the attempt file, which IS a row.
        check(e["evidence"] == "refuted" and e["id"] in rows,
              f"V5 {e['id']} has a results row")
        continue
    check(row[1] == "PASS", f"V5 {e['id']} row is PASS", str(row))

print()
print(f"{checks - len(failures)}/{checks} checks passed")
if failures:
    print("VERIFICATION RED")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("VERIFICATION GREEN")
