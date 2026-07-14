# Research Project Phase I — Direction Selection and Question Design

Date: 2026-07-13  
Course day: W1D1 — explore and group up  
Status: candidate workspace; working lead identified; direction not locked  
Theme: biologically constrained credit assignment and learned representations

Schedule: [`neuroai-project-schedule-2026-07-13-to-2026-07-24.md`](../curricula/neuromatch/neuroai-project-schedule-2026-07-13-to-2026-07-24.md)

## Current Working Recommendation

Carry **e-prop and neural similarity** forward as the working lead for W1D1
group discussion. Keep Sign-Symmetry as the lower-cost backup. Neither direction
is locked before the W1D4 proposal milestone.

The project should not merely repeat the published end-state comparison between
e-prop and backpropagation through time (BPTT). Its sharper target is the
**trajectory of representational change during learning**:

> At matched architecture, initialization, and task performance, do e-prop and
> BPTT reach similarly brain-aligned recurrent representations through
> distinguishable learning trajectories?

This is a W1D1 recommendation, not a group decision or established scientific
claim. The lead ranks highly because it connects temporal credit assignment,
recurrent dynamics, and brain–model comparison while appearing testable with
public code and at least one public neural dataset. W1D2 must verify that this
fit survives the group's actual compute, time, and implementation constraints.

Project-map classification: the current e-prop trajectory question is primarily
**Direction B — inferring the learning rule from observable signatures**. The
source-map distinction and success criteria are explained in
[`microlearning-project-two-directions.md`](../notes/neuroai/microlearning-project-two-directions.md).

## Course Milestone Alignment

| Course window | Use of this artifact |
|---|---|
| W1D1–D2 | Explore, discuss group fit, and reduce four candidates to a lead plus backup. |
| W1D3 | Read the 2025 e-prop/neural-similarity paper and the 2020 e-prop mechanism paper; share the evidence and limitations. |
| W1D4 | Lock the proposal: motivation, approximately three questions, and workflow diagram. |
| W1D5 | Refine scope and experiment plan with TA feedback. |
| W2D1–D2 | Run the bounded reproduction and extension. |
| W2D3 | Report results, blockers, and next steps. |
| W2D4–D5 | Lock the credible result and tell the story. |

## Source Seed and Verification Rule

The direction set originated from a user-provided slide titled “Fresh ideas
from recent work.” The slide is treated as a discovery aid, not as evidence.
Claims below are tied to the four primary papers instead.

| Candidate | Primary source | Source status | Verified orientation claim |
|---|---|---|---|
| e-prop and neural similarity | Liu, Yang, and Cueva, [*Can Biologically Plausible Temporal Credit Assignment Rules Match BPTT for Neural Similarity? E-prop as an Example*](https://arxiv.org/abs/2506.06904) (2025); [official code](https://github.com/Helena-Yuhan-Liu/LearningRuleSimilarities) | methods/results skim | At matched task accuracy, e-prop and BPTT can show comparable model–neural similarity; initialization and architecture can contribute more variation than learning-rule choice in the tested settings. |
| Dendritic Localized Learning (DLL) | Lv et al., [*Dendritic Localized Learning: Toward Biologically Plausible Algorithm*](https://proceedings.mlr.press/v267/lv25c.html), ICML 2025; [official code](https://github.com/Lvchangze/Dendritic-Localized-Learning) | abstract/method orientation | DLL uses a pyramidal-neuron-inspired compartmental construction and is designed to avoid weight symmetry, global error representation, and separate inference/training phases. |
| Counter-Current Learning (CCL) | Kao and Hariharan, [*Counter-Current Learning: A Biologically Plausible Dual Network Approach for Deep Learning*](https://proceedings.neurips.cc/paper_files/paper/2024/hash/82f05a105c928c10706213952bf0c8b7-Abstract-Conference.html), NeurIPS 2024; [official code](https://github.com/IandRover/CCL-NeurIPS24) | abstract/method orientation | CCL couples feedforward input processing with anti-parallel feedback target processing to provide an alternative credit-assignment route. |
| Sign-Symmetry fine-tuning | Berriche, Adjal, and Baghdadi, [*Sign-Symmetry Learning Rules are Robust Fine-Tuners*](https://arxiv.org/abs/2502.05925) (2025) | methods/results skim; code availability not confirmed | Sign-symmetry rules can fine-tune BP-pretrained visual models with competitive clean performance and reported robustness gains, but the paper notes that gradient-based attacks may be disadvantaged by approximate gradients and calls for attacks adapted to these rules. |

Do not promote any method's use of biological language into evidence that the
brain implements that method. Here, “biologically plausible” is an operational
constraint on information availability or update mechanics, not a mechanism
identification result.

## Candidate Evaluation

Scores are decision aids from 1 (weak) to 5 (strong). They reflect the current
repository, learner profile, and a small-project constraint; they are not
scientific rankings of the papers.

| Criterion | Weight | e-prop | DLL | CCL | Sign-Symmetry |
|---|---:|---:|---:|---:|---:|
| Fit with NeuroAI and the current representation/dynamics path | 25% | 5 | 4 | 4 | 3 |
| Small-project feasibility | 20% | 4 | 3 | 4 | 5 |
| Falsifiable question available now | 20% | 5 | 4 | 4 | 5 |
| Public implementation/data path | 15% | 4 | 4 | 4 | 2 |
| Non-trivial extension beyond the paper | 15% | 4 | 3 | 3 | 4 |
| Interpretation risk is containable | 5% | 3 | 2 | 3 | 3 |
| **Weighted score** | **100%** | **4.45** | **3.55** | **3.80** | **3.85** |

### Why the working lead currently ranks first

- It directly connects to W1D3 representational geometry, DSA, recurrent
  dynamics, and the existing
  [`representation-similarity-toy`](../experiments/neuroai/representation-similarity-toy/README.md)
  experiment.
- The originating paper exposes a useful identifiability problem: post-learning
  neural similarity may be insufficient to infer the learning rule.
- The official implementation reports short per-model training runs, making a
  bounded reproduction plausible before attempting a larger extension.
- The question supports a negative result: failure to distinguish trajectories
  after proper matching would itself constrain what model activity can reveal
  about learning rules.

### Why the other directions remain secondary

- **DLL:** scientifically relevant, but evaluating a dendritic analogy demands
  more biological and algorithmic validation than Phase I can responsibly
  provide. Keep it as a later mechanism-comparison paper.
- **CCL:** a strong executable backup and useful future baseline, but its
  immediate evidence is centered more on task learning than model–neural
  comparison.
- **Sign-Symmetry:** the easiest AI/CV pilot. It becomes the fallback project if
  recurrent/neural-data reproduction is blocked. Robustness must be tested with
  adaptive or transfer attacks so that approximate gradients do not create a
  false sense of security.

## Research Question Design

### Primary research question

At matched architecture, initialization, and task performance, do e-prop and
BPTT produce distinguishable **learning trajectories** in representation space
even when their final model–neural similarity is comparable?

### Scope

This project tests whether two learning rules leave distinguishable signatures
in trained model trajectories. It does **not** infer the brain's true learning
rule without longitudinal neural recordings during biological learning.

### Subquestions

1. How large is the learning-rule effect on trajectory geometry relative to
   random seed and recurrent-weight gain?
2. Does the conclusion survive more than one comparison family: Procrustes
   distance, CKA/RSA-style geometry, and DSA or another dynamical measure?
3. Can a trajectory-derived classifier distinguish e-prop from BPTT on held-out
   seeds and gains without using task accuracy as a shortcut?
4. Are any rule-specific differences concentrated early in learning and erased
   near convergence?

### Variables

| Role | Variables |
|---|---|
| Main independent variable | learning rule: e-prop vs BPTT |
| Controlled/matched | architecture, task, training budget, initialization seed or paired initial weights, checkpoint schedule, task-performance band |
| Deliberately varied | recurrent-weight gain; random seed; optionally activation or sparsity after the primary analysis |
| Main dependent variables | task accuracy/loss; distance to neural data; model-to-model representational distance; trajectory path length/velocity; dynamical similarity |
| Confounds to audit | unmatched accuracy, learning rate, optimizer behavior, hidden-unit permutation/rotation, metric dimensionality bias, checkpoint timing |

### Working hypotheses

- **H1 — established-paper-informed expectation:** final e-prop and BPTT
  model–neural distances will be similar when task accuracy and initialization
  regime are matched.
- **H2 — new working hypothesis:** the path to the final state will retain a
  learning-rule signature, especially at early or intermediate checkpoints.
- **H3 — interaction hypothesis:** initialization/gain will explain more final
  similarity variance than rule alone, while a rule × gain interaction may be
  visible in trajectory features.

H2 and H3 are hypotheses to test, not conclusions.

### Falsification conditions

Treat the trajectory-signature hypothesis as unsupported if all of the
following hold under the preregistered pilot:

- cross-rule trajectory distances are no larger than within-rule, across-seed
  distances after accuracy matching;
- a classifier evaluated on held-out seeds and gains remains at chance with
  uncertainty compatible with no useful effect;
- any apparent separation disappears under a second representation/dynamics
  metric or after controlling for task-performance and checkpoint differences.

Do not rescue a null result by unplanned metric shopping.

## Minimal Phase I Experiment

### Dataset and task

Start with the public Mante 2013 task/data path used by the source paper. Do not
make the non-redistributable Sussillo 2015 dataset a Phase I dependency. A
synthetic task-only smoke test may precede the neural-data comparison.

### Pilot design

- Rules: e-prop and BPTT.
- Recurrent gain: two values selected before running the full pilot.
- Seeds: five paired initializations per rule/gain cell.
- Checkpoints: fixed training iterations shared across all runs.
- Minimum design: 2 rules × 2 gains × 5 seeds = 20 runs.
- Primary comparison: accuracy-matched Procrustes trajectory to neural data.
- Secondary checks: one geometry metric and one dynamical metric.

The pilot estimates effect sizes and failure modes; it is not powered for a
strong population-level claim.

### Analysis discipline

1. Pair rule conditions by identical initial weights where implementation
   permits.
2. Plot task performance and similarity together; never compare rules only at
   unequal accuracy.
3. Report within-rule seed variability alongside between-rule differences.
4. Hold out complete seeds or gain settings for any trajectory classifier.
5. Report effect sizes and bootstrap intervals; treat small-sample p-values as
   descriptive at most.
6. Record metric disagreement instead of collapsing metrics into a single
   preferred story.

## Post-Proposal Experiment Gates

| Gate | Required evidence | Decision |
|---|---|---|
| G0 — source audit | full notes for the e-prop paper and original e-prop mechanism paper; runnable environment inventory | proceed to reproduction or document blocker |
| G1 — reproduction | recover the qualitative accuracy-matched final-similarity trend for one public task | proceed to trajectory extension only if the baseline is credible |
| G2 — trajectory pilot | complete the preregistered 20-run matrix with checkpointed metrics | expand, revise, or accept a null result |
| G3 — direction review | compare information gained, compute cost, and interpretability against the Sign-Symmetry fallback | choose Phase II project scope |

## Risks and Mitigations

| Risk | Consequence | Mitigation |
|---|---|---|
| One source dataset is not redistributable | incomplete reproduction of the paper | make Mante/public data the required path; treat Sussillo as optional |
| Metric choice manufactures a result | weak or contradictory conclusion | preregister one primary and two secondary metric families |
| Accuracy or initialization confounds rule effects | false learning-rule signature | paired initialization, accuracy matching, factorial rule × gain design |
| Model trajectories differ but have no neural interpretation | overclaiming | frame the output as model-rule identifiability unless biological learning trajectories are added |
| Reproduction stack is stale | time lost to environment repair | begin with a smoke test and preserve an environment manifest before scaling |
| Compute exceeds the personal-lab budget | stalled project | stop at G1 or run the Sign-Symmetry fallback pilot |

## Required Artifacts

- [x] W1D1 candidate comparison and working recommendation
- [ ] W1D2 feasibility check for lead and backup
- [ ] `papers/reading-notes/e-prop-neural-similarity.md`
- [ ] `notes/neuroai/biological-credit-assignment.md`
- [ ] W1D4 proposal with motivation, approximately three questions, and workflow diagram
- [ ] W1D5 experiment outline revised after TA feedback
- [ ] `experiments/neuroai/eprop-learning-trajectories/README.md`
- [ ] `experiments/neuroai/eprop-learning-trajectories/SOURCES.md`
- [ ] preregistered pilot configuration and seed list
- [ ] one figure separating accuracy, final similarity, and trajectory effects
- [ ] Phase I decision log recording whether to expand, pivot, or stop

## Definition of Phase I Complete

Phase I is complete when the repository contains:

1. group agreement on one direction and one explicit backup;
2. a W1D3 review of 1–2 primary papers;
3. a W1D4 proposal with motivation, approximately three ordered questions, and
   a workflow diagram;
4. a feasibility boundary covering data, code, compute, time, and stopping
   conditions.

Reproduction and the trajectory pilot belong to the post-proposal experimental
phase in Week 2, not to today's W1D1 exploration task.
