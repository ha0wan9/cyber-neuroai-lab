# Neuromatch Companion Resources

This directory is for course-page companion resources that should not be mixed into notes or learning artifacts.

## Directory Rules

| Directory | Use |
|---|---|
| [`notebooks/`](notebooks/) | Downloaded or locally adapted Jupyter notebooks from Neuromatch course pages. |
| [`slides/`](slides/) | Slide decks linked from course pages. |
| [`datasets/`](datasets/) | Dataset links, dataset notes, checksums, licenses, and small local metadata files. Do not commit large raw datasets unless explicitly intended. |
| [`videos/`](videos/) | Video link registries and viewing notes. Do not mirror video files by default. |
| [`figures/`](figures/) | Course figures, screenshots, or generated visual references used for study artifacts. |
| [`raw-pages/`](raw-pages/) | Saved HTML, markdown exports, or metadata snapshots of course pages when needed for reproducible parsing. |

## Naming

Use lowercase kebab-case and keep course/day context in the path:

```text
resources/notebooks/compneuro/w1d2-model-fitting/
resources/slides/neuroai/w1d3/
resources/datasets/deeplearning/w3d3-self-supervised-learning/
```

When a resource has license, attribution, or redistribution constraints, keep only a pointer or metadata file here rather than copying the raw artifact.
