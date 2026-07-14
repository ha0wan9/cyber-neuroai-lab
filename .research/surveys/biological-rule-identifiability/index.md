# biological-rule-identifiability

> Master record for a BFS literature survey. Sub-questions and scope are fixed
> at frame time; this survey has not begun evidence collection.

## Identity

- Survey ID: `biological-rule-identifiability`
- Created UTC: `2026-07-13`
- Owner: repository user
- Status: `framed`
- Survey root: `.research/surveys/biological-rule-identifiability`
- Parent / superseded: none

## Research Question

How should the Neuromatch Microlearning research project be formulated so that
it tests whether biologically motivated learning rules can be distinguished
from longitudinal network observables, rather than conflating rule
identifiability, task performance, and biological mechanism claims?

## Scope

| Dimension | In scope | Out of scope |
|---|---|---|
| Signal type | weights, activations, updates, learning trajectories, task metrics | direct claims about unmeasured synaptic mechanisms |
| Model scale | toy and small research networks; feedforward and recurrent extensions | frontier-scale model training |
| Time range | foundational work plus current methods relevant to project design | exhaustive history of plasticity |
| Language / region | English-language primary and authoritative sources | regional comparison |
| Deployment target | virtual experiments and future neuroscience measurement design | clinical or production deployment |

## Sub-Questions

1. SQ1: Which biological implausibilities of backpropagation are addressed by each candidate rule, and which remain?
2. SQ2: Which observable statistics are theoretically or empirically linked to learning-rule identity?
3. SQ3: Under what data splits and nuisance-variable shifts is a rule-identification result valid?
4. SQ4: How do task performance and optimization geometry confound learning-rule decoding?
5. SQ5: Which observables are accessible under realistic neural recording, subsampling, and noise constraints?
6. SQ6: How robust are reported signatures across architectures, tasks, curricula, hyperparameters, and initializations?
7. SQ7: What negative results or non-identifiability arguments limit inference from aggregate observables?
8. SQ8: What minimal experiment is reproducible and informative within a two-week course project?

## Active Evidence Dimensions

| Sub-question | theory | experiment | survey | critical-review | dataset |
|---|---|---|---|---|---|
| SQ1 | yes |  | yes | yes |  |
| SQ2 | yes | yes |  |  |  |
| SQ3 | yes | yes |  | yes |  |
| SQ4 | yes | yes |  | yes |  |
| SQ5 |  | yes | yes | yes | yes |
| SQ6 |  | yes |  | yes | yes |
| SQ7 | yes | yes |  | yes |  |
| SQ8 |  | yes | yes | yes | yes |

## Star Rating Rubric

Use the four-dimension relevance, evidence quality, recency, and authority
rubric defined by the installed `deep-survey-bfs` skill. No project-specific
override has been set.

## Bias Audit Thresholds

| Bucket | Threshold | Notes |
|---|---:|---|
| Institution | 60% | trigger targeted re-search |
| Country | 60% | trigger targeted re-search |
| Year | 60% | report foundational-paper concentration separately |
| Method route | 60% | distinguish perturbation, feedback, local-objective, and recurrent routes |
| Deployment regime | 60% | distinguish virtual and biological experiments |
| Venue type (preprint) | 60% | prefer canonical peer-reviewed versions when available |

## Round 1 Source Plan

| Source | Keywords / queries | Cap |
|---|---|---:|
| arXiv | learning-rule identifiability; neural-network observables; biological credit assignment; local learning | 30–50 candidates |
| OpenReview | NeurIPS, ICLR, ICML learning-rule inference and biologically plausible learning | 10–20 candidates |
| DBLP | canonical venue and author confirmation for seed papers | 5–15 confirmations |
| Semantic Scholar | citation BFS from Nayebi et al. (2020) and Lillicrap et al. (2020) | as needed |

## Pointers

- `paper_index.md` — paper rows (empty until Round 1)
- `claims.jsonl` — claim evidence contract
- `coverage_matrix.md` — sub-question × evidence-dimension matrix
- `survey.md` — not created until the coverage audit passes
- `notes/neuroai/biological-credit-assignment.md` — current project-formulation note

## Changelog

| UTC | Change | Reason |
|---|---|---|
| 2026-07-13 | framed survey and fixed eight sub-questions | explore the Neuromatch project's formulation before broader search |

