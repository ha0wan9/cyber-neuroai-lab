# NeuroAI Field Map

> Master record for a breadth-first literature survey of the fields named in
> the user-provided NeuroAI timeline image. Sub-questions and scope are fixed
> at frame time; later changes are versioned rather than silently substituted.

## Identity

- Survey ID: `neuroai-field-map`
- Created UTC: `2026-07-14T19:27Z`
- Owner: repository owner + Codex research assistant
- Status: `synthesized-with-documented-limitations`
- Survey root: `papers/literature-maps/neuroai-field-map/`
- Parent / superseded: none
- Source image: `Screenshot 2026-07-14 at 21.27.42.png` supplied in the task

## Research Question

For every named domain in the supplied NeuroAI summary diagram, which primary
papers are the most representative entry points, and how many papers should be
allowed into each domain's list when the cap is scaled to the estimated size
and intellectual breadth of that domain? The result should preserve historical
lineage, distinguish foundational from later field-defining work, expose
ambiguous boundaries, and remain usable as a staged reading map.

## Scope

| Dimension | In scope | Out of scope |
|---|---|---|
| Named fields | All 41 boxes in the image; the duplicated “Neurons as multi-layered ANNs” box is represented once but its two placements are recorded | Adjacent fields absent from the image, except when needed to explain lineage |
| Publication type | Primary research papers, historically decisive technical reports/books only when they are the canonical source, and a small number of field-defining position/review papers | Generic textbooks, popular accounts, undifferentiated “most cited” lists |
| Time range | Earliest canonical antecedents through 2026-07-14 | Unpublished rumors and work appearing after the cutoff |
| Language | English-language scholarly record, including translated/canonical English editions | Exhaustive multilingual coverage |
| Evidence | Bibliographic identity, venue/year, contribution, lineage role, and primary/authoritative URL | Full claim-by-claim replication of every experiment |
| Ranking target | Representativeness for learning and field orientation | A claim of objective global rank or raw citation-count rank |
| Granularity | One paper may represent several overlapping boxes, but is listed and annotated per relevant field | Artificial deduplication that hides a paper's cross-field importance |

## Diagram Inventory

The image contains 41 boxes but 40 unique labels. “Neurons as multi-layered
ANNs” occurs twice (once at an algorithmic level and once near the hardware /
low-level row); it is treated as one domain with two biological scales.

1. Cybernetics
2. Biologically inspired perception
3. Hebbian learning
4. Cognitive architectures
5. MLPs
6. Perceptrons
7. Parallel distributed processing
8. Catastrophic forgetting
9. Recurrent neural networks
10. CNNs
11. Neuromorphic computing
12. Predictive coding
13. Sparse coding
14. Reinforcement learning
15. Spiking neural networks
16. Free-energy principle (FEP)
17. Reservoir computing
18. Hierarchical temporal memory
19. Neurosymbolic architectures
20. Animats and hybrots
21. Neuro-inspired XAI
22. Intuitive physics
23. Neural Turing machines
24. Computation through dynamics
25. Neurons as multi-layered ANNs (two placements in the image)
26. Dendrites
27. Consciousness in AI
28. Neural style transfer
29. CNNs → ventral stream
30. Attention
31. Using neuro data to realign AI
32. Self-supervised learning (Barlow Twins)
33. Geometry of learning
34. Theoretical deep learning
35. Biologically plausible backprop
36. Neurogenesis
37. Neuroconnectionism
38. Geometric deep learning
39. Embodied intelligence & embodied Turing test
40. Whole-brain emulation (WBE)

## Sub-Questions

1. **SQ1 — Boundary:** What does each diagram label denote, which labels overlap, and where would a modern literature taxonomy split or merge them?
2. **SQ2 — Scale:** What transparent proxy bundle can estimate each field's size and justify a field-specific top-k cap without pretending to have exact publication counts?
3. **SQ3 — Roots:** Which pre-1980 works established the conceptual and mathematical roots represented by the first image column?
4. **SQ4 — Classical connectionism:** Which 1980s–1990s works made distributed representations, neural architectures, recurrent computation, and learning operational?
5. **SQ5 — Biological mechanisms:** Which papers most strongly connect plasticity, spikes, dendrites, predictive/sparse coding, and neural dynamics to computation?
6. **SQ6 — Cognitive systems:** Which works define cognitive architectures, reinforcement learning, memory, intuitive physics, consciousness, and embodied intelligence as computational research programs?
7. **SQ7 — Brain-inspired hardware and agents:** Which works define neuromorphic hardware, animats/hybrots, neurogenesis-inspired systems, and whole-brain emulation?
8. **SQ8 — Representation and alignment:** Which works connect CNNs, ventral-stream models, self-supervision, neuro-data alignment, and neuro-inspired explainability?
9. **SQ9 — Modern architecture families:** Which works define attention, external-memory networks, neurosymbolic systems, geometric deep learning, and neuroconnectionism?
10. **SQ10 — Learning theory and credit assignment:** Which works best represent theoretical deep learning, learning geometry, and biologically plausible alternatives to backpropagation?
11. **SQ11 — Historical lineage:** For each field, which small set covers origin, consolidation, and a later reframing rather than clustering around one era or lab?
12. **SQ12 — Limits:** What boundary disputes, failed promises, negative results, or evidence gaps must accompany the representative list?

## Active Evidence Dimensions

| Sub-question | theory | experiment | survey | critical-review | dataset |
|---|---:|---:|---:|---:|---:|
| SQ1 | ✓ |  | ✓ | ✓ |  |
| SQ2 | ✓ |  | ✓ | ✓ |  |
| SQ3 | ✓ | ✓ | ✓ |  |  |
| SQ4 | ✓ | ✓ | ✓ | ✓ |  |
| SQ5 | ✓ | ✓ | ✓ | ✓ |  |
| SQ6 | ✓ | ✓ | ✓ | ✓ | ✓ |
| SQ7 | ✓ | ✓ | ✓ | ✓ |  |
| SQ8 | ✓ | ✓ | ✓ | ✓ | ✓ |
| SQ9 | ✓ | ✓ | ✓ | ✓ |  |
| SQ10 | ✓ | ✓ | ✓ | ✓ |  |
| SQ11 | ✓ | ✓ | ✓ | ✓ |  |
| SQ12 | ✓ | ✓ | ✓ | ✓ |  |

## Top-k Allocation Rule

“Field size” is an estimate, not an observed bibliometric total. Each field is
scored 0–2 on four proxies: historical depth, venue/community breadth,
methodological branching, and current activity. The summed size score maps to
a cap:

| Size score | Label | Top-k cap | Interpretation |
|---:|---|---:|---|
| 0–2 | S / focused | 3 | A narrow mechanism, single proposal, or speculative/emerging program |
| 3–4 | M / established niche | 5 | A recognizable line with several distinct phases or methods |
| 5–6 | L / broad field | 8 | A mature subfield with multiple communities and long-running branches |
| 7–8 | XL / foundational ecosystem | 12 | A very broad paradigm whose history cannot be represented responsibly by a short handful |

The cap is a maximum, not a quota. A list may stop below its cap when additional
papers add redundancy rather than a new lineage role. Ties favor: (1) origin or
decisive formalization, (2) field-defining empirical demonstration, (3) a new
method branch, (4) correction/limitation, and (5) a recent reframing. Citation
counts are supporting signals only and are not compared naively across eras.

## Star Rating Rubric

Reference: the Deep Survey BFS `paper-rating-rubric.md`. For this orientation
map, the four dimensions are relevance to the exact box, evidential quality,
influence/lineage value, and source/metadata confidence. Three-star papers are
eligible for the final top-k; two-star papers may be retained as alternates or
boundary evidence; one-star candidates are excluded from synthesis.

## Bias Audit Thresholds

| Bucket | Threshold | Notes |
|---|---:|---|
| Institution | 60% | Trigger targeted search if one institution dominates three-star papers |
| Country | 60% | Historical country concentration is reported, not silently “corrected” |
| Year/era | 60% | Applied per field where k ≥ 5; origin-only fields may be exempt with reason |
| Method route | 60% | Trigger search for a materially distinct route when the field is plural |
| Venue type (preprint) | 60% | Recent/emerging fields may exceed this only with an explicit warning |

## Round 1 Source Plan

| Source | Keywords / queries | Cap |
|---|---|---:|
| Primary publisher / proceedings | Exact-title and author queries for canonical metadata/DOI | As needed for every selected paper |
| arXiv | Fielded title/abstract queries for modern candidates and accepted-version links | 120 candidates |
| OpenReview | ICLR/NeurIPS-era candidates in representation learning, theory, credit assignment, and alignment | 40 candidates |
| DBLP | Canonical venue/year confirmation for computer-science papers | 80 confirmations |
| Semantic Scholar / OpenAlex | Citation-lineage BFS and broad influence sanity check from seed works | As needed; not used as the sole authority |
| PubMed / journal sites | Neuroscience, cognition, consciousness, dendrites, and neural data | 100 confirmations |

## Pointers

- `paper_index.md` — stable paper rows (`P001`, `P002`, …)
- `claims.jsonl` — anti-hallucination claim contract
- `coverage_matrix.md` — sub-question × dimension coverage
- `survey.md` — final field-by-field reading map
- `audits/` — coverage and bias checks

## Changelog

| UTC | Change | Reason |
|---|---|---|
| 2026-07-14T19:27Z | Framed survey and transcribed 41 boxes / 40 unique labels | Initial user request |
| 2026-07-14T21:10Z | Amended SQ2/SQ7 dataset cells to N/A | Audit found no dataset is appropriate for an explicitly estimated size rule or a heterogeneous historical hardware/WBE lineage |
| 2026-07-14T21:12Z | Centralized 179 unique works and passed coverage audit | All 40 fields have caps, ≥3 works, links, and boundary/limitation coverage |
| 2026-07-14T21:32Z | Corrected field-appearance total from 187 to 189 | Machine count found 70 classical + 36 biological + 83 modern appearances; the 179 unique-paper total is unchanged |
| 2026-07-14T21:39Z | Independent claims-adversary returned PASS-WITH-WARNINGS | Structure, cap math, IDs, field tags and claims contract passed; final reviewer did not individually revisit all 179 URLs |
