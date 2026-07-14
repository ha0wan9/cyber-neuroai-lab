# Neuromatch NeuroAI Notebooks

This directory contains the official student notebooks selected for the local
NeuroAI learning path. The notebooks are curriculum inputs, not completed
learning artifacts.

## Week 1 Import

- Imported: 2026-07-13
- Upstream repository: <https://github.com/neuromatch/NeuroAI_Course>
- Upstream commit: [`c4b079c657ccda35943dafc7adbc3dfc13e14ab3`](https://github.com/neuromatch/NeuroAI_Course/commit/c4b079c657ccda35943dafc7adbc3dfc13e14ab3)
- Rendered coursebook: <https://neuroai.neuromatch.io/>
- Scope: all Week 1 student-facing Intro, Tutorial, and Outro notebooks
- Count: 22 notebooks: 4 Intro, 14 Tutorial, and 4 Outro
- License: upstream course content is CC BY 4.0; software elements are also
  available under BSD 3-Clause. See the upstream
  [licensing statement](https://github.com/neuromatch/NeuroAI_Course#licensing).

The official tutorial schedule has no W1D4 teaching block, so the imported
notebooks cover W1D1, W1D2, W1D3, and W1D5. The separate research-project
schedule uses W1D4 as the project-proposal milestone; see
[`neuroai-project-schedule-2026-07-13-to-2026-07-24.md`](../../../neuroai-project-schedule-2026-07-13-to-2026-07-24.md).

## Imported Course Blocks

| Day | Theme | Local directory | Notebooks |
|---|---|---|---:|
| W1D1 | Generalization | [`w1d1-generalization/`](w1d1-generalization/) | 5 |
| W1D2 | Comparing tasks | [`w1d2-comparing-tasks/`](w1d2-comparing-tasks/) | 5 |
| W1D3 | Comparing artificial and biological networks | [`w1d3-comparing-artificial-and-biological-networks/`](w1d3-comparing-artificial-and-biological-networks/) | 7 |
| W1D5 | Microcircuits | [`w1d5-microcircuits/`](w1d5-microcircuits/) | 5 |

### W1D1 — Generalization

- [`w1d1-intro.ipynb`](w1d1-generalization/w1d1-intro.ipynb)
- [`w1d1-tutorial1.ipynb`](w1d1-generalization/w1d1-tutorial1.ipynb) — Generalization in AI
- [`w1d1-tutorial2.ipynb`](w1d1-generalization/w1d1-tutorial2.ipynb) — Generalization in Neuroscience
- [`w1d1-tutorial3.ipynb`](w1d1-generalization/w1d1-tutorial3.ipynb) — Generalization in Cognitive Science
- [`w1d1-outro.ipynb`](w1d1-generalization/w1d1-outro.ipynb)
- Coursebook pages: [W1D1 index](../../../content-index/neuroai.md#w1d1)

### W1D2 — Comparing Tasks

- [`w1d2-intro.ipynb`](w1d2-comparing-tasks/w1d2-intro.ipynb)
- [`w1d2-tutorial1.ipynb`](w1d2-comparing-tasks/w1d2-tutorial1.ipynb) — Task definition and generalization
- [`w1d2-tutorial2.ipynb`](w1d2-comparing-tasks/w1d2-tutorial2.ipynb) — Contrastive learning for object recognition
- [`w1d2-tutorial3.ipynb`](w1d2-comparing-tasks/w1d2-tutorial3.ipynb) — Reinforcement learning across temporal scales
- [`w1d2-outro.ipynb`](w1d2-comparing-tasks/w1d2-outro.ipynb)
- Coursebook pages: [W1D2 index](../../../content-index/neuroai.md#w1d2)

### W1D3 — Comparing Artificial and Biological Networks

- [`w1d3-intro.ipynb`](w1d3-comparing-artificial-and-biological-networks/w1d3-intro.ipynb)
- [`w1d3-tutorial1.ipynb`](w1d3-comparing-artificial-and-biological-networks/w1d3-tutorial1.ipynb) — Generalization and representational geometry
- [`w1d3-tutorial2.ipynb`](w1d3-comparing-artificial-and-biological-networks/w1d3-tutorial2.ipynb) — Computation as transformation of representational geometries
- [`w1d3-tutorial3.ipynb`](w1d3-comparing-artificial-and-biological-networks/w1d3-tutorial3.ipynb) — Statistical inference on representational geometries
- [`w1d3-tutorial4.ipynb`](w1d3-comparing-artificial-and-biological-networks/w1d3-tutorial4.ipynb) — Bonus: representational geometry and noise
- [`w1d3-tutorial5.ipynb`](w1d3-comparing-artificial-and-biological-networks/w1d3-tutorial5.ipynb) — Dynamical Similarity Analysis
- [`w1d3-outro.ipynb`](w1d3-comparing-artificial-and-biological-networks/w1d3-outro.ipynb)
- Coursebook pages: [W1D3 index](../../../content-index/neuroai.md#w1d3)

### W1D5 — Microcircuits

- [`w1d5-intro.ipynb`](w1d5-microcircuits/w1d5-intro.ipynb)
- [`w1d5-tutorial1.ipynb`](w1d5-microcircuits/w1d5-tutorial1.ipynb) — Sparsity and sparse coding
- [`w1d5-tutorial2.ipynb`](w1d5-microcircuits/w1d5-tutorial2.ipynb) — Normalization
- [`w1d5-tutorial3.ipynb`](w1d5-microcircuits/w1d5-tutorial3.ipynb) — Attention
- [`w1d5-outro.ipynb`](w1d5-microcircuits/w1d5-outro.ipynb)
- Coursebook pages: [W1D5 index](../../../content-index/neuroai.md#w1d5)

## Import and Execution Policy

- Filenames were normalized to lowercase kebab-case; notebook content was not
  edited during import.
- Instructor notebooks and extracted solution files are intentionally excluded.
  They are answer keys, not first-pass study inputs.
- Static figures remain referenced at their official upstream URLs.
- Large datasets and pretrained models are not mirrored. Several notebooks
  download MNIST, CIFAR-10, model checkpoints, or small course datasets at
  runtime.
- Notebook setup cells may install packages and assume a network connection.
  Colab is the lowest-friction execution path; local execution should use an
  isolated environment and review setup cells before running them.
- Videos, slides, datasets, and further-reading lists remain linked through the
  coursebook and local content index unless a later learning artifact needs a
  durable local copy.

## Related Artifact

- [`neuroai-week-1-prestudy-plan.md`](../../../neuroai-week-1-prestudy-plan.md)
