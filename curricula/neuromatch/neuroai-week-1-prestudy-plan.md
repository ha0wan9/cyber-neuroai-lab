# Neuromatch NeuroAI Week 1 — Pre-study Plan

Date created: 2026-07-13  
Status: ready to use  
Format: 7 sessions × 2 hours (14 hours total)  
Learner profile: AI/CV engineer transitioning toward NeuroAI and computational
cognitive neuroscience

## Goal

Arrive at Week 1 able to explain the organizing questions, recognize the main
mathematical objects, and predict what each notebook experiment is testing.
Pre-study is not an attempt to complete the tutorials in advance.

The plan is based on the repository's existing
[`prep-knowledge-map.md`](prep-knowledge-map.md). It gives extra weight to
representational geometry and statistical inference because W1D3 is the central
bridge from an AI/CV background to brain–model comparison.

## Materials

- [Week 1 imported notebooks](resources/notebooks/neuroai/README.md)
- [NeuroAI course content index](content-index/neuroai.md#w1d1)
- [Prerequisite domain knowledge map](prep-knowledge-map.md)
- [Representation-similarity toy experiment](../../experiments/neuroai/representation-similarity-toy/README.md)
- [Learning-unit template](../../templates/learning-unit-template.md)

## Completion Rule

A session is complete when its exit check can be answered without notes. Put
uncertain claims and unanswered questions in a dated learning log; do not turn
them into settled project memory yet.

If only 7 hours are available, do the **Core** block in every session and skip
the Extension block. If 4 hours per day are available, pair Sessions 1–2,
3–4, and 5–6, then keep Session 7 separate.

## Session 1 — Readiness Gate and Execution Setup

**Core — 90 minutes**

1. Take the seven-question self-check at the end of
   [`prep-knowledge-map.md`](prep-knowledge-map.md) closed-book.
2. Mark each answer `green`, `yellow`, or `red`.
3. Skim the four Intro notebooks only; record each day's central question.
4. Choose the default execution path:
   - Colab for notebooks that install packages or download models/data;
   - local Jupyter only when an isolated environment and enough storage are
     already available.
5. Inspect, but do not blindly execute, every setup and download cell in the
   first notebook you plan to run.

**Extension — 30 minutes**

- Create a dated learning-log entry from the learning-unit template with the
  readiness colors and the top three gaps.

**Exit check:** Can I name the four teaching days, their core questions, and my
three highest-risk prerequisites?

## Session 2 — W1D1 Generalization Across AI, Neuroscience, and Cognition

**Core — 90 minutes**

1. Review distribution shift, train/test separation, regularization, transfer
   learning, data augmentation, inductive bias, and sample complexity.
2. Skim the objectives and Big Picture sections of all three W1D1 tutorials.
3. Build a three-column comparison:
   - AI: performance under out-of-distribution inputs;
   - neuroscience: task-driven models, robustness, and biological data;
   - cognitive science: one-shot learning and structured priors.
4. For the RNN tutorial, state what evidence would show only behavioral fit,
   representational similarity, or mechanistic equivalence. Keep these claims
   separate.

**Extension — 30 minutes**

- Write one failure case for each generalization strategy: scale, augmentation,
  regularization, synthetic data, and stronger priors.

**Exit check:** Can I explain why good in-distribution accuracy is insufficient
and give three distinct meanings of “generalization” used on W1D1?

## Session 3 — W1D2 Objectives Shape Representations

**Core — 90 minutes**

1. Review classification, regression, autoencoding, inpainting, and their loss
   functions.
2. Draw one CNN trunk with four task heads. For each head, label the target,
   loss, information that must be retained, and likely nuisance information.
3. Review cosine similarity, positive/negative pairs, embeddings, and the idea
   of contrastive loss.
4. Review POMDP, episode, policy, value, regret, exploration/exploitation, and
   the distinction between learning within an episode and across episodes.

**Extension — 30 minutes**

- Predict which learned representation should transfer best to digit
  classification and write the assumptions behind the prediction.

**Exit check:** Can I explain how changing only the objective can change the
geometry and transferability of a representation?

## Session 4 — W1D3 Representational Geometry Foundations

**Core — 90 minutes**

1. Review vectors, matrices, dot products, cosine similarity, Euclidean
   distance, covariance, and linear regression.
2. By hand, construct a 4 × 4 representational dissimilarity matrix for four
   toy stimuli.
3. Explain why an RDM removes the original coordinate axes while preserving a
   pattern of pairwise relations.
4. Skim W1D3 Tutorials 1–2 and trace this chain:

   `stimuli → layer activations → distances → RDM → comparison across layers`

5. Revisit the local
   [representation-similarity toy experiment](../../experiments/neuroai/representation-similarity-toy/README.md)
   and identify what it demonstrates versus what it cannot establish.

**Extension — 30 minutes**

- Predict how standard and adversarially robust models might differ across
  layers. Mark the prediction explicitly as a working hypothesis.

**Exit check:** Given an activation matrix, can I describe exactly how to build
an RDM and what an RDM comparison does—and does not—show?

## Session 5 — W1D3 Statistical Inference and Dynamics

**Core — 90 minutes**

1. Review measurement noise, stimulus sampling, subject sampling,
   cross-validation, bootstrapping, and uncertainty intervals.
2. Explain why a high RSA score on one stimulus set and one subject is not a
   population-level result.
3. Skim Tutorials 3–5, including the bonus tutorial only at the objective and
   Big Picture level.
4. Make a comparison table for Euclidean, correlation/cosine, Mahalanobis, and
   cross-validated distance: what each is sensitive to and its noise risk.
5. Distinguish static representational similarity from similarity between
   trajectories or dynamical systems.

**Extension — 30 minutes**

- Sketch a two-factor resampling diagram with stimuli on one axis and subjects
  on the other.

**Exit check:** Can I name the sampling population behind an RSA claim and
explain why cross-validation changes the interpretation of a distance estimate?

## Session 6 — W1D5 Microcircuit Computations

**Core — 90 minutes**

1. Review population, lifetime, and connection sparsity; compare
   `l0`, `l1`, cardinality, and kurtosis as measures or proxies.
2. Explain sparse coding as reconstruction with a constrained or penalized set
   of active components; recognize the role of dictionary learning and OMP.
3. Compare divisive normalization, layer normalization, and normalization as an
   inductive bias. Do not assume that similarly named operations imply the same
   biological mechanism.
4. Review query, key, value, dot-product attention, multiplicative gating, and
   the permutation-related inductive bias of self-attention.

**Extension — 30 minutes**

- Make a mechanism table with rows for sparsity, normalization, and attention,
  and columns for biological observation, artificial implementation, shared
  computation, and overclaiming risk.

**Exit check:** Can I describe each computation without treating the brain and
the artificial implementation as strictly equivalent?

## Session 7 — Integration and Course-Day Strategy

**Core — 90 minutes**

1. Draw one concept map connecting:

   `objective → inductive bias → learned representation → geometry → generalization`

   Add sparsity, normalization, attention, noise, and statistical inference at
   the appropriate points.
2. Re-take the seven-question readiness check. Any remaining red item becomes a
   just-in-time lookup target, not a reason to delay the whole course.
3. Select one notebook per teaching day to run deeply:
   - W1D1: Tutorial 2 if the neuroscience bridge is the priority;
   - W1D2: Tutorial 2 for representation learning, or Tutorial 3 for meta-RL;
   - W1D3: Tutorial 3 for research-grade comparison methodology;
   - W1D5: Tutorial 1 for sparse coding, or Tutorial 3 for attention.
4. Create a question queue with no more than three questions per teaching day.

**Extension — 30 minutes**

- Create the dated learning-log scaffold that will be filled during Week 1.

**Exit check:** Can I explain the Week 1 story in five minutes without walking
through the course in page order?

## Just-in-Time Preflight Before Each Teaching Day

Spend 15 minutes immediately before starting a day's notebooks:

1. Read the Intro notebook.
2. State the day's core question from memory.
3. Check network/GPU/data requirements in setup cells.
4. Choose one deep tutorial; treat the others as structured skims unless time
   allows.
5. End the day with a short synthesis note and unresolved questions, not merely
   executed cells.

## Week 1 Readiness Checklist

- [ ] I can distinguish behavioral fit, representational similarity, and
  mechanistic equivalence.
- [ ] I can explain OOD generalization and inductive bias with one AI and one
  neuroscience example.
- [ ] I can map task objectives to loss functions and representation demands.
- [ ] I can construct and interpret an RDM.
- [ ] I can identify stimulus, subject, and measurement uncertainty in an RSA
  claim.
- [ ] I can distinguish static geometry comparison from dynamical similarity.
- [ ] I can explain sparsity, normalization, and attention without overclaiming
  biological equivalence.
- [ ] I know which notebooks need network downloads and will review setup cells
  before execution.

## Expected Durable Outputs

During pre-study and Week 1, route work into small artifacts rather than one
large course summary:

- a dated readiness and learning-log entry;
- a modular note on RDM/RSA and its inference limits;
- a task-objective-to-representation comparison table;
- a brain-versus-AI microcircuit mechanism table;
- updates to the existing representation-similarity experiment only after a
  specific runnable extension has been chosen.

