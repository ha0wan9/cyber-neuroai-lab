# biological-learning-vs-backprop

> Master record for this BFS literature survey. Sub-questions and scope are
> fixed at frame time; evidence collection has not yet passed a coverage audit.

## Identity

- Survey ID: `biological-learning-vs-backprop`
- Created UTC: `2026-07-14`
- Owner: repository user
- Status: `framed`
- Survey root: `.research/surveys/biological-learning-vs-backprop`
- Parent / superseded: none

## Research Question

What are the important similarities and differences between learning in the
brain and backpropagation, and which concepts from biological learning can be
translated into useful constraints for artificial intelligence—especially
explicit regularizers, auxiliary losses, architectural priors, or alternative
update rules?

## Scope

| Dimension | In scope | Out of scope |
|---|---|---|
| Biological level | synaptic plasticity, circuit credit assignment, neuromodulation, homeostasis, representation constraints | molecular detail without a learning-algorithm consequence |
| AI systems | differentiable neural networks, recurrent/spiking extensions, continual and representation learning | non-neural algorithms except as a contrast |
| Time range | foundational work plus representative modern methods | exhaustive chronological history |
| Evidence | English-language primary papers and authoritative reviews | untraceable popular analogies |
| Engineering target | regularization, auxiliary objectives, architectural constraints, update rules, measurable trade-offs | claims that a model is brain-equivalent merely because it borrows one mechanism |

## Sub-Questions

1. SQ1: What computation does canonical backpropagation perform, and which information, symmetry, memory, and timing assumptions does it require?
2. SQ2: Which experimentally supported biological plasticity and credit-assignment signals operate at synaptic, circuit, and behavioral timescales?
3. SQ3: In what precise senses can biological learning and backpropagation be considered similar—objective improvement, error signaling, feedback, or local eligibility traces?
4. SQ4: Which biological-plausibility objections to backpropagation are fundamental, and which candidate mechanisms partially address them?
5. SQ5: Which biological concepts can be expressed faithfully as explicit regularization terms in an AI objective?
6. SQ6: Which concepts instead require an auxiliary loss, architectural constraint, state variable, or non-gradient/local update rule?
7. SQ7: What empirical benefits and costs have these translations shown for accuracy, robustness, efficiency, representation quality, and continual learning?
8. SQ8: What controlled ablation would test whether a biologically motivated constraint contributes beyond ordinary hyperparameter regularization?

## Active Evidence Dimensions

| Sub-question | theory | experiment | survey | critical-review | dataset |
|---|---|---|---|---|---|
| SQ1 | yes |  | yes | yes |  |
| SQ2 | yes | yes | yes | yes |  |
| SQ3 | yes | yes |  | yes |  |
| SQ4 | yes | yes | yes | yes |  |
| SQ5 | yes | yes |  | yes |  |
| SQ6 | yes | yes |  | yes |  |
| SQ7 |  | yes | yes | yes | yes |
| SQ8 | yes | yes |  | yes | yes |

## Star Rating Rubric

Use the relevance, evidence quality, recency, and authority rubric defined by
the installed `deep-survey-bfs` skill. No project-specific scoring override is
set. A method paper is not evidence that the brain implements the method; that
claim requires separate biological evidence.

## Bias Audit Thresholds

| Bucket | Threshold | Notes |
|---|---:|---|
| Institution | 60% | trigger targeted re-search |
| Country | 60% | trigger targeted re-search |
| Year | 60% | report foundational-paper concentration separately |
| Method route | 60% | distinguish local plasticity, feedback, predictive, equilibrium, continual-learning, and representation routes |
| Deployment regime | 60% | distinguish feedforward, recurrent, spiking, and continual settings |
| Venue type (preprint) | 60% | prefer canonical peer-reviewed versions when available |

## Round 1 Source Plan

| Source | Keywords / queries | Cap |
|---|---|---:|
| arXiv | `ti:"biological credit assignment"`; `ti:"feedback alignment"`; `ti:"predictive coding" AND backpropagation`; `all:"homeostatic regularization"` | 30–50 candidates |
| OpenReview | ICLR/NeurIPS/ICML local learning, predictive coding, continual learning, topographic regularization | 10–20 candidates |
| DBLP | canonical venue and author confirmation for seed papers | 5–15 confirmations |
| Semantic Scholar | citation BFS from Lillicrap et al. (2020), Bellec et al. (2020), and Olshausen & Field (1996) | as needed |

## Pointers

- `paper_index.md` — paper rows (empty until Round 1)
- `claims.jsonl` — claim evidence contract
- `coverage_matrix.md` — sub-question × evidence-dimension matrix
- `survey.md` — built only after the coverage audit passes
- `notes/neuroai/brain-learning-and-backprop.md` — reader-facing concept note

## Changelog

| UTC | Change | Reason |
|---|---|---|
| 2026-07-14 | framed survey and fixed eight sub-questions | distinguish biological mechanisms, algorithmic analogies, and implementable AI constraints |
