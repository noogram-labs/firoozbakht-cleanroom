# Licences — a map by file class

This repository mixes two kinds of work, and each gets the licence that fits it:

- **Code** is dual-licensed under **MIT** or **Apache-2.0**, at your option —
  the conventional permissive pair for software.
- **Content** (the paper, the proof exposition, the site prose, the wiki, the
  report) is licensed under **CC-BY-4.0** — the conventional licence for written
  and figurative work, so a reader who reuses the theorem, a figure, or a
  paragraph is bound to attribute it, and is free to do so.

The split matters: a software licence literally grants rights only over *"the
Software"*. Without a content licence, the paper and proof prose would be
copyrighted with no grant attached — readable, but not reusable. CC-BY-4.0
closes that gap.

## Map

| Class | Paths | Licence(s) |
|-------|-------|------------|
| **Code** | `python/` (library, tests, notebooks), `lean/` (Lean 4 source), `report/*.py` (collector + renderer) | [MIT](LICENSE-MIT) **or** [Apache-2.0](LICENSE-APACHE), at your option |
| **Content** | `paper/` (LaTeX, prose, figures), `docs/site/` (site prose), `docs/wiki/` (concept cards, source ledger), `report/` (narrative + rendered figures) | [CC-BY-4.0](LICENSE-CC-BY-4.0) |

Where a path holds both (e.g. `report/` has both `.py` renderers and the
narrative `report.md` + figures), the code is under MIT/Apache-2.0 and the prose
and figures are under CC-BY-4.0.

## Third-party

The Lean formalisation depends on **Mathlib** (Apache-2.0, © The Mathlib
Community). It is fetched at build time, not redistributed here. See
[`NOTICE`](NOTICE) for the pinned revision and attribution.

## Attribution & citation

- **Code © 2026 Noogram.**
- **Paper, proof exposition & site content © 2026 Noogram.**
- The **originating research question** was posed by **Gabriel Peyré** (CSD
  seminar, ENS, 2026-06-18). This is provenance, not authorship — the question
  is credited to its source; the work answering it is authored by Noogram.

To cite this work, use [`CITATION.cff`](CITATION.cff). A Zenodo DOI is reserved
and will be minted at the public flip.

Contact: <contact@noogram-labs.dev>.
