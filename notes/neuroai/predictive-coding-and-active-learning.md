# Predictive Coding and Active Learning in Neural AI

Date: 2026-07-14  
Status: structured draft; core claims checked against primary or official paper
pages at the abstract/method-orientation level

## 1. Core Question

How do predictive coding and active learning change, respectively, **how a
neural system learns from an observation** and **which observation it chooses
to learn from next**?

## 2. One-Sentence Summary

Predictive coding organizes inference and learning around hierarchical
prediction errors, while active learning allocates a limited labeling budget
to selected examples; they can be combined, but they solve different parts of
the learning problem.

## 3. Terminology Boundary

The phrase “active learning” has two nearby but non-equivalent meanings in this
area.

| Term | Main question | What changes? | Typical external signal |
|---|---|---|---|
| Predictive coding | How should latent states and parameters explain current sensory input? | Internal states and model parameters | Prediction error |
| Active learning in ML | Which unlabeled item should be sent to an oracle next? | Composition of the labeled training set | Label returned by a human, experiment, or other oracle |
| Active sensing | Where or how should the agent measure next? | Sensor pose, viewpoint, fixation, or measurement | New sensory observation |
| Active inference | Which action best reduces expected uncertainty and/or realizes preferred outcomes under a generative model? | Policy or action | Consequences of acting in the environment |

**Established distinction:** active learning in machine learning is not a
synonym for active inference. Active learning normally assumes an unlabeled
pool and an oracle. Active inference is a generative-model account of
perception, learning, and action. They can share information-gain objectives,
but their algorithms and scientific commitments differ.

## 4. Predictive Coding

### 4.1 Intuition

Instead of treating perception as a single bottom-up pass, a hierarchical
system repeatedly does two things:

1. a higher level predicts activity at the level below;
2. the lower level reports the residual between prediction and observation.

The internal representation is adjusted until the residual errors are small.
The model parameters can then be updated so that future predictions improve.
In the Rao–Ballard visual model, feedback connections carry predictions and
feedforward connections carry residual errors.

This is best understood as a **family of models**, not one universally agreed
neural circuit or training algorithm.

### 4.2 Minimal Mathematical Object

For a hierarchy in which state `x_(l+1)` predicts state `x_l`, write

```text
x_hat_l = f_l(x_(l+1); W_l)
epsilon_l = x_l - x_hat_l
E = 1/2 * sum_l epsilon_l^T Pi_l epsilon_l
```

where:

- `epsilon_l` is the prediction error at level `l`;
- `Pi_l` is a precision matrix that controls how strongly that error is
  trusted;
- `E` is a precision-weighted prediction-error objective.

Two coupled update processes follow:

```text
inference:  dx_l/dt  = - partial E / partial x_l
learning:   delta W_l proportional to - partial E / partial W_l
```

Inference changes neural activities or latent states for the current sample.
Learning changes synaptic weights across samples. Keeping those timescales
separate prevents the common misconception that every reduction in current
prediction error is already parameter learning.

### 4.3 Applications in Neural AI

#### A. A model of cortical computation

Predictive coding supplies a computational interpretation of recurrent,
top-down, and bottom-up cortical interactions. It has been used to model visual
context effects and to formulate testable hypotheses about error-like and
prediction-like neural populations.

**Evidence boundary:** success at reproducing a neural response pattern does
not establish that the brain implements that exact predictive-coding
algorithm. The model may be one of several mechanisms compatible with the
observation.

#### B. Local alternatives or approximations to backpropagation

Some predictive-coding networks update weights from quantities available at
nearby units and synapses. Under specific architectures, dynamics, and
parameter conditions, such updates can approximate or even reproduce
backpropagation updates. This makes predictive coding relevant to biologically
constrained credit assignment.

**Important qualification:** “can match backpropagation under stated
conditions” is not the same claim as “the brain performs backpropagation” or
“predictive coding is generally cheaper than backpropagation.” Iterative
inference adds compute and latency, and equivalence results depend on the exact
formulation.

#### C. Generative and self-supervised representation learning

A network trained to predict lower-level input, future input, or missing input
can learn latent factors without a label for every example. The useful bridge
to modern AI is the idea that representation learning can be driven by the
structure of sensory prediction rather than only by supervised targets.

**Boundary:** next-token prediction, masked prediction, predictive state
models, and predictive coding are related by a broad predictive objective, but
they are not automatically the same architecture or learning rule.

#### D. Online adaptation and anomaly signals

Prediction error can mark a mismatch between the current model and incoming
data. This is useful for anomaly detection, surprise-triggered updating, and
continual learning. Raw error is not automatically epistemic uncertainty: it
may also be caused by irreducible noise, corrupted measurements, or an
underpowered decoder.

#### E. Active sensing and embodied agents

A predictive model can evaluate which viewpoint, fixation, or measurement is
likely to resolve an ambiguity. The agent then changes its input by acting,
rather than waiting passively for a new sample. This is the closest operational
bridge from predictive coding to active sensing and active inference.

## 5. Active Learning in Machine Learning

### 5.1 Intuition

Suppose labels are expensive but unlabeled inputs are abundant. A model starts
with a small labeled set, scores the unlabeled pool, asks an oracle to label a
small batch, retrains, and repeats.

```text
small labeled set L + unlabeled pool U
-> train model
-> score candidates with acquisition function a(x)
-> query a batch B from an oracle
-> move labeled B from U to L
-> retrain and evaluate under the same label budget
```

The basic selection rule is

```text
x* = argmax_(x in U) a(x; model, L)
```

The scientific question is not merely whether final accuracy is high. It is
whether a query policy reaches a target performance with fewer labels than a
strong random-sampling baseline, after accounting for repeated training cost.

### 5.2 Main Acquisition Families

| Family | Signal | Strength | Main failure mode |
|---|---|---|---|
| Uncertainty sampling | entropy, margin, least confidence | simple and often competitive | confidently wrong or poorly calibrated models |
| Bayesian information gain | expected reduction in parameter uncertainty, such as BALD | separates some epistemic uncertainty from output ambiguity | posterior approximation can be expensive or inaccurate |
| Diversity / core-set | coverage in representation space | avoids redundant batches | geometry may not track task relevance |
| Gradient embeddings | expected update magnitude plus diversity, such as BADGE | connects selection to model change | depends on pseudo-labels and current representation |
| Expected model change / error reduction | estimated benefit after labeling | directly tied to learning progress | costly counterfactual estimation |

### 5.3 Applications in Neural AI

- **Medical and scientific imaging:** prioritize samples whose expert
  annotation is expensive.
- **Neural-data annotation:** select trials, time windows, units, or behavioral
  segments for curation; the oracle may be a human annotator or an additional
  experiment.
- **BCI and personalized decoding:** choose calibration trials that most
  improve a user-specific decoder.
- **Robotics and embodied learning:** request labels or demonstrations only for
  ambiguous states, while active sensing decides where to observe.
- **Large neural models:** use human feedback or costly evaluation on the
  examples expected to be most informative, subject to safety and sampling-
  bias controls.
- **Closed-loop neuroscience:** adapt stimulus selection to distinguish
  competing encoding models. This is closer to Bayesian experimental design
  than ordinary pool-based labeling, but it shares the logic of allocating an
  information budget.

### 5.4 Evaluation Discipline

Active learning results are sensitive to initialization, the initial labeled
pool, batch size, representation quality, and random seed. A 2024 cross-domain
benchmark found that a method could appear better or worse than random
depending on the sampled runs. Therefore a credible small experiment needs:

- random sampling as a required baseline;
- the same initial labeled set for paired comparisons;
- multiple seeds and uncertainty intervals;
- an accuracy-versus-label-budget curve, not one final point;
- a record of training compute and annotation cost;
- inspection for class imbalance, outliers, and redundant queries.

## 6. How Predictive Coding and Active Learning Can Work Together

### 6.1 Complementary roles

```text
predictive model
-> predicts an input or latent state
-> produces error and uncertainty signals
-> acquisition policy combines informativeness and diversity
-> oracle or environment returns a new observation/label
-> inference and learning update the model
```

Predictive coding supplies a model and internal error dynamics. Active learning
supplies a policy for spending a data-acquisition budget. Active sensing adds a
policy for moving the sensor. None of these substitutions is automatic.

### 6.2 Prediction error as an acquisition signal

A tempting rule is “query the examples with the largest prediction error.” It
can work when error reveals a correctable model gap, but it can fail by
selecting sensor corruption, irreducible noise, or out-of-distribution samples
that do not help the target task.

A more defensible working hypothesis is:

> A prediction-error score becomes more useful when combined with uncertainty,
> representational diversity, and an explicit rule for rejecting pathological
> outliers.

This is a hypothesis, not an established general result.

### 6.3 Three timescales

Keeping three loops separate makes system design easier:

1. **fast inference:** adjust latent state for the current observation;
2. **parameter learning:** update the predictive model across observations;
3. **data acquisition or action:** choose which observation, label, or sensory
   consequence arrives next.

## 7. Failure Modes and Misconceptions

1. **Prediction error is not reward-prediction error.** The first usually means
   mismatch between predicted and observed sensory/activity variables; the
   second is a temporal-difference signal about expected reward.
2. **Prediction error is not calibrated uncertainty.** A large residual may be
   noise; a wrong model may also be confidently wrong with a small residual.
3. **Predictive coding is not one algorithm.** Results about one formulation do
   not transfer automatically to all predictive-coding networks.
4. **Local updates do not prove biological implementation.** Local information
   availability is one biological-plausibility criterion, not complete neural
   evidence.
5. **Active learning is not free data efficiency.** It adds repeated training,
   acquisition computation, oracle latency, and sampling bias.
6. **Beating passive training is not enough.** The comparison must be against a
   matched random-query loop with the same budget and initialization.
7. **Active learning is not active inference.** The former typically asks an
   oracle for labels; the latter selects actions under a generative model and
   preference structure.

## 8. Small Future Experiment

### Core question

Under a fixed labeling budget, does a prediction-error-based query score add
value beyond random and ordinary uncertainty sampling?

### Minimal setup

- Data: MNIST or Fashion-MNIST, with a deliberately small labeled seed set.
- Model: small classifier plus a lightweight reconstruction/prediction head.
- Acquisition strategies:
  1. random;
  2. predictive entropy or margin;
  3. reconstruction/prediction error;
  4. prediction error plus diversity.
- Primary metric: area under the test-accuracy-versus-label-count curve.
- Required controls: paired initial pools, equal batch sizes, equal retraining
  budget, at least five seeds, and query-composition diagnostics.

The reconstruction head is only an **engineering proxy** for a predictive
model. Calling this a full predictive-coding network would overstate the setup.

### Falsification condition

Treat prediction-error acquisition as unsupported in this setting if it does
not improve over paired random sampling across seeds, or if its apparent gain
is explained by class imbalance, outlier selection, or extra training compute.

## 9. Fit With the Current Project Roadmap

### Current decision

Do not add predictive coding as a third learning rule or active learning as a
second experimental loop to the 2026-07-13 to 2026-07-24 course project. The
current e-prop/BPTT plan already contains architecture, initialization,
learning-rule, task-shift, and representation-analysis decisions. Adding both
topics now would create a factorial scope that cannot be interpreted cleanly in
the remaining time.

### Recommended routing

- **Current course project:** retain e-prop versus BPTT; choose one primary
  Track A or Track B question on W1D2.
- **Current optional analysis:** predictive coding belongs only in the
  background comparison of local/error-driven learning rules.
- **Post-course microproject:** run the bounded prediction-error active-query
  experiment above after the current project reaches its direction-review
  gate.
- **Longer-term NeuroAI direction:** compare learning rules, acquisition rules,
  and observable neural/representational signatures only after each component
  has a stable baseline in isolation.

## 10. Open Questions

1. Which empirical neural signatures can distinguish predictive coding from
   alternative recurrent inference mechanisms?
2. When does sensory prediction error track epistemic uncertainty rather than
   aleatoric noise?
3. Can active stimulus selection make competing brain-model hypotheses more
   identifiable with fewer experimental trials?
4. Does a local predictive-coding learning rule improve online adaptation or
   continual learning relative to e-prop and BPTT under matched compute?
5. How should annotation cost, compute cost, and information gain be combined
   in one acquisition objective?

## 11. Source Map

### Predictive coding

- Rao and Ballard, [*Predictive coding in the visual cortex: a functional
  interpretation of some extra-classical receptive-field
  effects*](https://pubmed.ncbi.nlm.nih.gov/10195184/) (1999) — canonical
  hierarchical visual predictive-coding model.
- Whittington and Bogacz, [*An Approximation of the Error Backpropagation
  Algorithm in a Predictive Coding Network with Local Hebbian Synaptic
  Plasticity*](https://pmc.ncbi.nlm.nih.gov/articles/PMC5467749/) (2017) —
  local predictive-coding updates and conditions relating them to
  backpropagation.
- Millidge et al., [*Predictive Coding Approximates Backprop along Arbitrary
  Computation Graphs*](https://openreview.net/forum?id=PdauS7wZBfC) (2020) —
  extension of the relationship to general computation graphs.
- Zahid et al., [*Predictive Coding as a Neuromorphic Alternative to
  Backpropagation: A Critical
  Evaluation*](https://direct.mit.edu/neco/article/35/12/1881/117833/Predictive-Coding-as-a-Neuromorphic-Alternative-to)
  (2023) — analysis of assumptions and computational trade-offs.

### Active learning and active inference

- Gal, Islam, and Ghahramani, [*Deep Bayesian Active Learning with Image
  Data*](https://proceedings.mlr.press/v70/gal17a.html) (2017) — Bayesian
  uncertainty acquisition for deep image models.
- Sener and Savarese, [*Active Learning for Convolutional Neural Networks: A
  Core-Set Approach*](https://iclr.cc/virtual/2018/poster/194) (2018) —
  geometry and diversity-based batch acquisition.
- Ash et al., [*Deep Batch Active Learning by Diverse, Uncertain Gradient Lower
  Bounds*](https://iclr.cc/virtual/2020/poster/1502) (2020) — BADGE combines
  uncertainty and diversity in gradient space.
- Werner et al., [*A Cross-Domain Benchmark for Active
  Learning*](https://proceedings.neurips.cc/paper_files/paper/2024/hash/72de9826cfe582e175520f404eaad473-Abstract-Datasets_and_Benchmarks_Track.html)
  (2024) — evidence for domain and seed sensitivity in active-learning
  evaluation.
- Friston et al., [*Active inference and
  learning*](https://pmc.ncbi.nlm.nih.gov/articles/PMC5167251/) (2016) —
  active-inference account of choice and learning; included to mark the
  conceptual boundary with ML active learning.

