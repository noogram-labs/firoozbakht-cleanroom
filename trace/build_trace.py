#!/usr/bin/env python3
"""Trace sidecar collector for polymer germ-20260725-791a7c45.

Read-only over .cosmon/state/ (cosmon runtime state, owned by the cs
runtime). Copies raw rows into trace/ under the worktree; never mutates
the source. Re-run any time to refresh the sidecar with newly-landed
runtime state.
"""
import hashlib
import json
import os

STATE_DIR = "/Users/eserie/galaxies/firoozbakht-cleanroom/.cosmon/state"
MOL_DIR = os.path.join(STATE_DIR, "fleets", "default", "molecules")
GERM_ID = "germ-20260725-791a7c45"
RUN_DIR = os.path.join(STATE_DIR, "spore-runs", GERM_ID)
EVENTS_PATH = os.path.join(STATE_DIR, "events.jsonl")
RUNTIME_TRACE_PATH = os.path.join(STATE_DIR, "runtime-trace.jsonl")
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

def discover_molecule_ids():
    ids = []
    if not os.path.isdir(MOL_DIR):
        return ids
    for name in sorted(os.listdir(MOL_DIR)):
        state_path = os.path.join(MOL_DIR, name, "state.json")
        if not os.path.isfile(state_path):
            continue
        try:
            with open(state_path) as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
        variables = data.get("variables", {})
        run_dir = variables.get("run_dir", "")
        if GERM_ID in run_dir:
            ids.append(name)
    return ids


def build_events_jsonl(molecule_ids):
    id_set = set(molecule_ids)
    lines_out = []
    if os.path.isfile(EVENTS_PATH):
        with open(EVENTS_PATH) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                mol_id = row.get("molecule_id") or row.get("mol_id")
                if mol_id in id_set:
                    lines_out.append(line)
    if os.path.isfile(RUNTIME_TRACE_PATH):
        with open(RUNTIME_TRACE_PATH) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                mol_id = row.get("molecule_id")
                if mol_id in id_set:
                    lines_out.append(line)
    out_path = os.path.join(OUT_DIR, "events.jsonl")
    with open(out_path, "w") as f:
        for line in lines_out:
            f.write(line + "\n")
    return out_path, len(lines_out)


def build_briefs_md(molecule_ids):
    rows = []
    for mol_id in molecule_ids:
        state_path = os.path.join(MOL_DIR, mol_id, "state.json")
        try:
            with open(state_path) as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            continue
        variables = data.get("variables", {})
        formula_id = data.get("formula_id", "<absent>")
        crew_role = variables.get("crew_role", "<absent>")
        status = data.get("status", "<absent>")
        topic = variables.get("topic", "<absent>")
        rows.append((mol_id, formula_id, crew_role, status, topic))

    out_path = os.path.join(OUT_DIR, "briefs.md")
    with open(out_path, "w") as f:
        f.write(f"# Germinated briefs — {GERM_ID}\n\n")
        f.write(
            "Source: `.cosmon/state/fleets/default/molecules/<id>/state.json` "
            "(`variables.topic`, `formula_id`, `variables.crew_role`), filtered to "
            f"molecules whose `variables.run_dir` contains `{GERM_ID}`.\n\n"
        )
        f.write(f"{len(rows)} molecules found.\n\n")
        for mol_id, formula_id, crew_role, status, topic in rows:
            f.write(f"## {mol_id}\n\n")
            f.write(f"- **formula:** `{formula_id}`\n")
            f.write(f"- **crew_role:** `{crew_role}`\n")
            f.write(f"- **status (at collection time):** `{status}`\n")
            f.write(f"- **topic:**\n\n  {topic}\n\n")
    return out_path, len(rows)


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_hashes_tsv(molecule_ids):
    rows = []

    # Molecule-directory artifacts (briefing.md, prompt.md, log.md, state.json)
    for mol_id in molecule_ids:
        mol_path = os.path.join(MOL_DIR, mol_id)
        if not os.path.isdir(mol_path):
            continue
        for fname in sorted(os.listdir(mol_path)):
            fpath = os.path.join(mol_path, fname)
            if not os.path.isfile(fpath):
                continue
            try:
                size = os.path.getsize(fpath)
                digest = sha256_of(fpath)
            except OSError:
                continue
            rel = os.path.relpath(fpath, STATE_DIR)
            rows.append((mol_id, rel, str(size), f"sha256:{digest}"))

    # Any artifacts already written under the run's spore-runs tree
    # (per-crew_role output directories, including our own trace/ mirror
    # under .cosmon/state — captured here read-only, not written to).
    if os.path.isdir(RUN_DIR):
        for dirpath, _dirnames, filenames in os.walk(RUN_DIR):
            for fname in sorted(filenames):
                fpath = os.path.join(dirpath, fname)
                try:
                    size = os.path.getsize(fpath)
                    digest = sha256_of(fpath)
                except OSError:
                    continue
                rel = os.path.relpath(fpath, STATE_DIR)
                rows.append(("<run_dir>", rel, str(size), f"sha256:{digest}"))

    out_path = os.path.join(OUT_DIR, "hashes.tsv")
    with open(out_path, "w") as f:
        f.write("molecule_id\trelative_path\tbytes\tsha256\n")
        for row in rows:
            f.write("\t".join(row) + "\n")
    return out_path, len(rows)


def main():
    molecule_ids = discover_molecule_ids()
    ev_path, ev_count = build_events_jsonl(molecule_ids)
    br_path, br_count = build_briefs_md(molecule_ids)
    ha_path, ha_count = build_hashes_tsv(molecule_ids)
    print(f"molecules discovered: {len(molecule_ids)}")
    print(f"{ev_path}: {ev_count} rows")
    print(f"{br_path}: {br_count} briefs")
    print(f"{ha_path}: {ha_count} hashed artifacts")


if __name__ == "__main__":
    main()
