# Microlearning Project — Two Main Research Directions

Date: 2026-07-13  
Source: `Microlearning Project Slides.pdf`, especially pages 10–21  
Status: structured explanation; project direction not locked

## The Split in One Sentence

The project map separates a **forward/design problem** from an
**inverse/identification problem**:

1. **Direction A:** invent or test a candidate learning rule, then ask whether
   it learns well under biologically relevant constraints.
2. **Direction B:** observe the traces left by learning, then ask whether those
   traces reveal which hidden learning rule generated them.

These directions study the same credit-assignment problem from opposite ends.

## Shared Starting Point — Credit Assignment

A multilayer network receives a global outcome or error, but each individual
synapse must decide how it should change. Backpropagation solves this efficiently
in artificial networks, but it requires operations with no established direct
biological implementation, especially symmetric forward/backward weights.

The slides therefore introduce candidate alternatives such as Hebbian learning,
spike-timing-dependent plasticity (STDP), node or weight perturbation, feedback
alignment, and the Kolen–Pollack rule. Both directions start from this candidate
space, but they ask different scientific questions.

## Direction A — Can We Devise Biologically Plausible Algorithms That Learn Well?

### Core question

Can a learning rule respect more biological constraints while still learning
accurately, efficiently, robustly, and at useful scale?

This is primarily a **construction and stress-testing** direction. The learning
rule is known because the researchers choose and implement it.

### Experimental logic

```text
choose or implement a learning rule
→ train a network
→ make the task or environment harder
→ measure learning quality and update quality
→ compare with backpropagation and other rules
```

### What “learn well” means

The slides suggest several outcome families:

- final task performance;
- learning speed and sample efficiency;
- generalization to unseen data;
- robustness to noise, task switching, non-stationarity, and online learning;
- scalability to deeper networks and harder tasks;
- bias and variance of proposed weight updates relative to backpropagation's
  gradient updates.

The last item is important. A rule can fail because its update is systematically
pointed in the wrong direction (**bias**) or because individual updates are too
noisy and unstable (**variance**). A useful rule should ideally control both.

### Project-map examples

- **Q6:** test additional biologically plausible rules under harder conditions,
  such as online learning, non-stationary data, or noise.
- **Q10 under Direction A:** implement more complex rules such as target
  propagation, predictive coding, STDP, or BurstProp.

### What counts as success

A successful Direction A result shows that a specific rule–architecture–task
combination improves a defined trade-off, for example:

- similar accuracy with less weight symmetry;
- better online adaptation at acceptable variance;
- greater noise robustness without losing clean performance;
- a clear boundary describing where the method stops scaling.

“It is inspired by biology” is not itself a successful result.

### Main risk

Implementation complexity can consume the two-week project. A sophisticated
rule may require special neuron dynamics, feedback pathways, multiple phases, or
careful hyperparameter tuning. A negative performance result can also be
ambiguous: the rule may be weak, or the implementation/tuning may be incomplete.

## Direction B — Can We Infer Which Learning Rule the Brain Is Using?

### Core question

If the learning rule is hidden, do its observable consequences contain a stable
enough signature to identify it?

This is primarily an **inverse problem or system-identification** direction. The
researcher observes learning curves, weight-update statistics, representations,
or neural activity and tries to recover the rule that generated them.

### Why identification matters

The value is not merely attaching an algorithm name to the brain. It is reducing
the set of learning mechanisms compatible with the evidence.

1. **Separate outcome from mechanism.** Different learning rules can reach the
   same task accuracy or similar final neural representations. Identifying a
   rule requires signatures of *how learning unfolded*, preventing endpoint fit
   from being mistaken for a mechanistic explanation.
2. **Make biological-plausibility claims falsifiable.** A proposed rule becomes
   scientifically stronger when it predicts observations that competing rules
   do not, such as a characteristic adaptation curve, update-noise structure,
   response to perturbation, or change in population dynamics.
3. **Reveal the information required for credit assignment.** Even if the exact
   algorithm is not identifiable, evidence may discriminate between rule
   families that require global error signals, local eligibility traces,
   feedback pathways, perturbations, or neuromodulatory broadcasts.
4. **Guide experiments and measurements.** Model-based identification can show
   which observable is informative and which is not, helping experimentalists
   choose when to measure neural activity, plasticity, behavior, or responses
   to controlled perturbations.
5. **Explain differences in adaptation.** Rules that reach similar endpoints
   may differ in online learning, continual adaptation, noise robustness,
   generalization, energy demands, or recovery after damage. These differences
   matter for both neuroscience and engineering.
6. **Establish limits of inference.** A well-designed failure to identify a rule
   demonstrates observational equivalence: the available measurements cannot
   support a unique mechanistic claim. This is useful because it prevents
   overinterpretation and identifies what new evidence is needed.

A realistic hierarchy of identification targets is:

```text
most defensible: required signals or rule family
                 ↓
harder:          mechanism class and constraints
                 ↓
hardest:         one exact algorithm and its hyperparameters
```

For example, data may support a three-factor rule involving eligibility traces
and a modulatory signal without proving that the brain implements the exact
published e-prop equations.

### Experimental logic

```text
train networks with several known candidate rules
→ collect only the metrics an observer could plausibly access
→ learn or define a rule-identification procedure
→ hide the rule labels on held-out runs
→ test whether the procedure recovers the correct rule
→ degrade or shift the observations to test robustness
```

The artificial networks are a validation environment: because their true rules
are known, one can test whether the proposed inference method works before
making any claim about the brain.

### Observable signatures

Possible measurements include:

- learning speed and final performance;
- bias and variance of weight updates;
- alignment between approximate updates and the backpropagation gradient;
- changes in representations or recurrent dynamics across training;
- robustness and generalization profiles;
- partial, noisy, or temporally sparse versions of these measurements.

### Project-map examples

- **Q5:** add more candidate rules and test whether their observable metrics are
  internally consistent and distinguishable.
- **Q8:** vary network hyperparameters and ask whether a rule's signature
  survives those changes.
- **Q10 under Direction B:** lower measurement quality and determine when rule
  inference breaks down.

### What counts as success

A successful Direction B result demonstrates **identifiability**, not just
separation on the training runs:

- a rule can be recovered on held-out random seeds;
- identification survives relevant architecture or hyperparameter changes;
- accuracy is above a preregistered baseline with uncertainty reported;
- a confusion matrix reveals which rules are genuinely indistinguishable;
- performance degrades predictably as measurement quality is reduced.

A particularly useful negative result is that two rules cannot be distinguished
from the chosen observables. That shows the measurements are insufficient for a
claim about biological learning.

### Main risk

The inference procedure may learn confounds instead of learning-rule signatures.
For example, it may identify optimizer settings, task accuracy, architecture,
initialization, or checkpoint timing. Held-out seeds, paired initialization,
accuracy matching, and tests across hyperparameters are therefore central, not
optional extras.

Even a successful artificial-network classifier does not prove which rule the
brain uses. Applying the method to biology additionally requires observables
that are measurable in animals and a candidate set broad enough to avoid forcing
the answer to be one of a few convenient algorithms.

## Direct Comparison

| Dimension | Direction A — design/test | Direction B — infer/identify |
|---|---|---|
| Problem type | forward, constructive | inverse, diagnostic |
| Learning rule | known and manipulated | hidden at evaluation time |
| Main input | algorithm + benchmark/scenario | observable metrics from trained/learning systems |
| Main output | performance and plausibility trade-off | predicted rule or uncertainty over rules |
| Central control | fair training and tuning across rules | removal of confounds and held-out-condition testing |
| Typical failure | method does not learn or scale | different rules leave indistinguishable signatures |
| Strong negative result | clear boundary of a rule's usefulness | evidence that chosen measurements cannot identify the rule |
| Relation to the brain | proposes a possible learning mechanism | tests what evidence could discriminate mechanisms |

## Two Common Misreadings

### Track A does not require a novel algorithm

Track A may design a new neuro-inspired rule, but it can also implement an
existing candidate and test it under a harder or more biologically relevant
condition. Its objective is broader than closing an accuracy gap with
backpropagation: it studies the trade-off among biological constraints,
accuracy, learning speed, sample efficiency, generalization, robustness,
scalability, and update bias/variance.

### Track B is not a binary neuro-inspired detector

Track B does not mainly classify an algorithm as “neuro-inspired” or “not
neuro-inspired.” That label is imposed from the algorithm's assumptions and
available signals; it cannot generally be recovered from learning efficiency
alone.

Instead, Track B asks whether observable learning signatures can distinguish
which candidate rule—or at least which rule family—generated the data. Learning
efficiency is one possible signature, but final accuracy, learning curves,
weight-update bias/variance, gradient alignment, robustness profiles,
representational change, and network dynamics may all contribute. The central
test is whether these signatures remain diagnostic after controlling for
architecture, initialization, hyperparameters, and task performance.

### Track B is mechanistic explainability of learning

Track B is related to explainability, but its target is the **learning process**,
not an individual prediction. It asks which update mechanism could have produced
the observed learning trajectory. This is closer to system identification and
mechanistic inference than to saliency maps, feature attribution, or explaining
why one input received one output.

Three levels should remain distinct:

- prediction explainability: why did the trained model produce this output?;
- representation interpretability: what information is encoded internally?;
- learning-mechanism identification: which update rule produced the model's
  changing parameters, representations, and behavior?

Track B uses the first two as possible evidence for the third, but they do not
by themselves establish the learning mechanism.

## How the Current Candidate Ideas Map

| Candidate idea | Natural map | Reason |
|---|---|---|
| Dendritic Localized Learning | A | It proposes a rule/architecture and is naturally tested for performance, scaling, and biological constraints. |
| Counter-Current Learning | A | It proposes a dual-network credit-assignment mechanism whose learning behavior can be stress-tested. |
| Sign-Symmetry fine-tuning | A | Its immediate question is whether an approximate feedback rule provides useful fine-tuning performance or robustness. |
| e-prop matching BPTT/neural similarity | A → B bridge | Showing that e-prop learns well and matches neural activity is an A-style evaluation; asking whether its trajectory can be distinguished from BPTT is a B-style inference problem. |

## Implication for the Current W1D1 Working Question

The current question—whether e-prop and BPTT have distinguishable
representational learning trajectories after performance and initialization are
matched—is mainly **Direction B**.

Its intended observable signature is the trajectory of representation or
dynamics across checkpoints. Its success criterion should therefore be
held-out-rule identification or a well-supported failure of identifiability,
not merely a statistically different average metric on the same training runs.

This framing also sharpens the biological claim:

> The project can test whether model observables are informative about a hidden
> learning rule. It cannot, within two weeks and without longitudinal biological
> learning data, determine the rule used by the brain.

## W1D1 Decision Prompt

The group should decide which kind of contribution it wants:

- choose **Direction A** if the goal is to build or stress-test a learning rule;
- choose **Direction B** if the goal is to test whether learning rules are
  identifiable from limited observations;
- choose a deliberately narrow bridge only if the team can state separate
  success criteria for the learning-performance part and the inference part.

For the existing e-prop proposal, Direction B is the cleaner project identity.

## If the Group Prefers Track A

Track A has a larger combinatorial design space:

```text
learning rule × architecture × task regime × biological constraint × metric
```

That freedom is useful for discovery but dangerous in a two-week project. A
credible scope fixes almost every axis:

- one existing candidate rule;
- one backpropagation baseline;
- one new stress condition;
- two performance metrics plus one mechanism-facing metric;
- one preregistered success/failure criterion.

The preferred contribution is therefore a **novel evaluation or boundary**, not
necessarily a novel algorithm. A reusable question template is:

> Under [one difficult learning condition], does [one biologically constrained
> rule] offer a different performance–plausibility trade-off from BPTT, and is
> that difference associated with [one update or dynamics metric]?

For e-prop, the Track A version could study online or non-stationary temporal
learning, controlled noise, or task switching. For Sign-Symmetry, it could audit
robust fine-tuning under attacks that do not rely on the same gradients used for
training. The Track B trajectory-identification question can remain an optional
secondary analysis instead of the project identity.
