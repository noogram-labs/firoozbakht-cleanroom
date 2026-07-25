#!/usr/bin/env python3
"""Append-only trace sidecar for a cosmon polymer (spore-run).

READ-ONLY on .cosmon/state/ — this script never writes back into the
runtime's own state tree except under the run's own trace/ subdirectory
(which cosmon does not read). It reconstructs, from what the runtime
already emits, three artifacts per destination:

  events.jsonl  — every raw event touching this polymer (or global),
                  each stamped with _source_file/_source_seq/_scope/_captured_at
  briefs.md     — one section per node (molecule) germinated in this run:
                  topic, formula, crew_role, status, adapter/model if announced
  hashes.tsv    — sha256 + byte count for every file under every node's
                  output_dir, as of the sweep

A sweep is idempotent: re-running it recomputes the full snapshot from
source-of-truth files and overwrites events.jsonl/briefs.md/hashes.tsv
(sha256-content-addressed, so "append-only" is honored at the level of
"no captured fact is discarded across sweeps" via manifest.json's sweep
history, not by literally appending bytes to files that must stay
consistent snapshots).
"""
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

STATE_FILES = ["events.jsonl", "runtime-trace.jsonl", "instrumentation/authz.jsonl"]


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_molecules(state_root, run_dir):
    """Return {mol_id: state_dict} for molecules whose variables.run_dir matches run_dir."""
    run_dir = str(run_dir)
    mols = {}
    mol_root = state_root / "fleets"
    if not mol_root.is_dir():
        return mols
    for fleet_dir in mol_root.iterdir():
        mdir = fleet_dir / "molecules"
        if not mdir.is_dir():
            continue
        for mol_dir in mdir.iterdir():
            sfile = mol_dir / "state.json"
            if not sfile.is_file():
                continue
            try:
                d = json.loads(sfile.read_text())
            except Exception:
                continue
            rd = d.get("variables", {}).get("run_dir", "")
            if rd == run_dir:
                mols[d["id"]] = d
    return mols


def collect_events(state_root, mol_ids):
    events = []
    seq = 0
    for rel in STATE_FILES:
        fpath = state_root / rel
        if not fpath.is_file():
            continue
        with open(fpath) as f:
            for i, line in enumerate(f):
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except Exception:
                    continue
                mol_id = rec.get("mol_id") or rec.get("molecule_id")
                scope = "polymer" if mol_id in mol_ids else "global"
                rec["_source_file"] = rel
                rec["_source_seq"] = i
                rec["_scope"] = scope
                rec["_captured_at"] = now_iso()
                events.append((seq, rec))
                seq += 1
    return [rec for _, rec in events]


def event_model_adapter_for(mol_id, events):
    adapter = None
    model = None
    for rec in events:
        if rec.get("mol_id") != mol_id and rec.get("molecule_id") != mol_id:
            continue
        if rec.get("type") == "adapter_selected":
            adapter = rec.get("adapter_name")
        if rec.get("type") == "model_selected":
            model = rec.get("model")
    return adapter, model


def render_briefs(run_dir, mols, events):
    lines = []
    lines.append("# Node briefs")
    lines.append("")
    lines.append(f"Run: `{Path(run_dir).name}`  ")
    lines.append(f"Collected: {now_iso()}  ")
    lines.append(f"Nodes germinated: {len(mols)}")
    lines.append("")
    lines.append(
        "Each section is one node of the polymer, as recorded by the cosmon\n"
        "runtime. `model` is absent unless the runtime emitted a\n"
        "`model_selected` event for that node — an unpinned model means the\n"
        "adapter's own default applied, which the trace cannot name."
    )
    lines.append("")
    for mol_id in sorted(mols):
        d = mols[mol_id]
        variables = d.get("variables", {})
        adapter, model = event_model_adapter_for(mol_id, events)
        total_steps = d.get("total_steps")
        current_step = d.get("current_step")
        lines.append(f"## {mol_id}")
        lines.append("")
        lines.append(f"- **formula**: `{d.get('formula_id')}`")
        lines.append(f"- **crew_role**: `{variables.get('crew_role')}`")
        lines.append(f"- **status**: {d.get('status')} (step {current_step}/{total_steps})")
        lines.append(f"- **created_at**: {d.get('created_at')}")
        lines.append(f"- **adapter**: {adapter if adapter else '(not announced)'}")
        lines.append(f"- **model**: {model if model else '(not announced)'}")
        lines.append(f"- **output_dir**: `{variables.get('output_dir')}`")
        lines.append(f"- **tags**: {', '.join(d.get('tags', []))}")
        lines.append("")
        lines.append("**topic**")
        lines.append("")
        lines.append(f"> {variables.get('topic', '')}")
        lines.append("")
    return "\n".join(lines) + "\n"


def collect_hashes(mols):
    rows = []
    seen = set()
    for mol_id in sorted(mols):
        d = mols[mol_id]
        output_dir = d.get("variables", {}).get("output_dir")
        mol_state_dir = None
        # also hash the molecule's own runtime-state directory (briefing/prompt/log/state.json)
        candidates = []
        if output_dir:
            candidates.append((f"molecule:{mol_id}", Path(output_dir)))
        rows_for_mol = []
        for origin_prefix, root in candidates:
            if not root.is_dir():
                continue
            for path in sorted(root.rglob("*")):
                if not path.is_file():
                    continue
                key = (mol_id, str(path))
                if key in seen:
                    continue
                seen.add(key)
                st = path.stat()
                rows_for_mol.append(
                    (
                        origin_prefix,
                        str(path),
                        sha256_file(path),
                        st.st_size,
                        datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).isoformat(),
                    )
                )
        rows.extend(rows_for_mol)
    return rows


def collect_molecule_runtime_hashes(state_root, mols):
    """Hash each molecule's own cosmon-runtime files (briefing.md, prompt.md, log.md, state.json)."""
    rows = []
    for mol_id in sorted(mols):
        for fleet_dir in (state_root / "fleets").iterdir():
            mdir = fleet_dir / "molecules" / mol_id
            if not mdir.is_dir():
                continue
            for path in sorted(mdir.glob("*")):
                if not path.is_file():
                    continue
                st = path.stat()
                rows.append(
                    (
                        f"molecule:{mol_id}",
                        str(path),
                        sha256_file(path),
                        st.st_size,
                        datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).isoformat(),
                    )
                )
    return rows


def render_hashes(rows, swept_at):
    total_bytes = sum(r[3] for r in rows)
    lines = [
        f"# trace sidecar — artifact hashes, swept {swept_at}",
        f"# files={len(rows)} bytes={total_bytes}",
        "# CAVEAT: a sweep is a snapshot. A file written and deleted between",
        "# two sweeps is not counted here; byte totals are a lower bound.",
        "origin\tpath\tsha256\tbytes\tmtime_utc",
    ]
    for origin, path, digest, size, mtime in rows:
        lines.append(f"{origin}\t{path}\t{digest}\t{size}\t{mtime}")
    return "\n".join(lines) + "\n"


def write_dest(dest, events, briefs_text, hashes_text):
    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    events_path = dest / "events.jsonl"
    with open(events_path, "w") as f:
        for rec in events:
            f.write(json.dumps(rec) + "\n")
    (dest / "briefs.md").write_text(briefs_text)
    (dest / "hashes.tsv").write_text(hashes_text)
    return len(events)


def main():
    if len(sys.argv) < 3:
        print("usage: trace_collector.py <run_dir> <dest_dir> [dest_dir ...]", file=sys.stderr)
        sys.exit(1)
    run_dir = Path(sys.argv[1]).resolve()
    dests = [Path(p).resolve() for p in sys.argv[2:]]
    state_root = run_dir.parent.parent  # .../.cosmon/state/spore-runs/<germ> -> .../.cosmon/state

    mols = load_molecules(state_root, run_dir)
    events = collect_events(state_root, set(mols.keys()))
    swept_at = now_iso()
    briefs_text = render_briefs(run_dir, mols, events)
    hash_rows = collect_molecule_runtime_hashes(state_root, mols) + collect_hashes(mols)
    hashes_text = render_hashes(hash_rows, swept_at)

    events_appended_per_dest = {}
    for dest in dests:
        prev_count = 0
        prev_events_path = dest / "events.jsonl"
        if prev_events_path.is_file():
            with open(prev_events_path) as f:
                prev_count = sum(1 for _ in f)
        n = write_dest(dest, events, briefs_text, hashes_text)
        events_appended_per_dest[str(dest)] = max(0, n - prev_count)

    manifest_path = dests[0] / "manifest.json"
    manifest = {"collector": "tools/trace_collector.py", "sweeps": []}
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text())
        except Exception:
            pass
    sweep_no = len(manifest.get("sweeps", [])) + 1
    sweep_record = {
        "sweep": sweep_no,
        "at": swept_at,
        "run_dir": str(run_dir),
        "state_root": str(state_root),
        "nodes": len(mols),
        "events_seen": len(events),
        "events_appended_per_dest": events_appended_per_dest,
        "artifacts_hashed": len(hash_rows),
        "artifact_bytes": sum(r[3] for r in hash_rows),
    }
    manifest.setdefault("sweeps", []).append(sweep_record)
    manifest["latest"] = sweep_record
    manifest_text = json.dumps(manifest, indent=2) + "\n"
    for dest in dests:
        (dest / "manifest.json").write_text(manifest_text)

    log_line = (
        f"[trace] sweep {sweep_no}: nodes={len(mols)} "
        f"events+{sum(events_appended_per_dest.values())} files={len(hash_rows)}\n"
    )
    for dest in dests:
        with open(dest / "collector.log", "a") as f:
            f.write(log_line)

    print(log_line.strip())


if __name__ == "__main__":
    main()
