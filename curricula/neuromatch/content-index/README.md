# Neuromatch Content Index

A structured, per-tutorial index of all learning content across the three official
Neuromatch coursebooks. Each entry records the tutorial title, learning objectives,
section structure, and source URL.

Per the repository's learning-system policy (`AGENTS.md`), this is a **structural
catalog, not a content copy**: no long passages are reproduced. Open the linked page
for full text, equations, figures, and code.

## Files

| File | Coursebook | Source | Tutorial pages |
|---|---|---|---|
| [`compneuro.md`](compneuro.md) | Computational Neuroscience | <https://compneuro.neuromatch.io/> | 75 |
| [`deeplearning.md`](deeplearning.md) | Deep Learning | <https://deeplearning.neuromatch.io/> | 28 |
| [`neuroai.md`](neuroai.md) | NeuroAI | <https://neuroai.neuromatch.io/> | 46 |

Total: 149 indexed pages. Extracted 2026-06-19.

## What each entry contains

- **Title** — the tutorial's heading.
- **Source URL** — the canonical student-notebook page.
- **Estimated time** — where the page declares one.
- **Objectives** — the tutorial's stated learning objectives (verbatim short bullets).
- **Sections** — the substantive section / exercise / demo headings, with setup and
  boilerplate cells filtered out.

## Provenance and limits

- Page lists are authoritative: derived from each book's `searchindex.js` (CompNeuro,
  Deep Learning) and `sitemap.xml` (NeuroAI), filtered to student tutorial pages.
- Coverage is the **student** track only; instructor variants and solution cells are
  not indexed.
- Pages without a "Tutorial Objectives" block (e.g. W0D0 video-series pages, day
  intro/outro pages) appear with sections only.
- Day-topic labels for CompNeuro and Deep Learning come from the source folder names;
  NeuroAI days are listed by code, with topic conveyed by the tutorial titles.

## Maintenance

Regenerate by re-fetching each book's page list and re-parsing titles, objectives, and
headings. Keep this index structural — put summaries, interpretation, and worked
understanding in `notes/` and `experiments/`, not here.
