# NeuroAI Taxonomy

Purpose: provide a compact taxonomy for classifying notes, papers, and learning questions. The detailed taxonomy lives in `.research/surveys/neuroai-foundations-frontiers/index.md` and `.research/surveys/neuroai-foundations-frontiers/survey.md`.

## Axes

Classify each item along three axes:

| Axis | Values | Use |
| --- | --- | --- |
| Direction | brain -> AI; AI -> brain; bidirectional; applied | Prevents mixing inspiration, modeling, tooling, and application claims. |
| Level | neuron; circuit; population; system; cognition; behavior; interface | Prevents Marr-level mismatch. |
| Claim type | established result; interpretation; working hypothesis; analogy; speculation; open question | Keeps AI-generated synthesis intellectually honest. |

## Route Taxonomy

| Route | Scope | Foundation or frontier | Primary survey section |
| --- | --- | --- | --- |
| A. Foundations and framing | NeuroAI identity, Marr levels, field manifestos, falsifiability | foundation | SQ1; survey 3.A |
| B. Classical computational-neuroscience theory | sparse/efficient coding, predictive coding, Bayesian brain, normalization, population dynamics | foundation | SQ2; survey 3.B |
| C. Brain-inspired architectures | CNN lineage, attractor memory, differentiable memory, world-model architectures, grid codes | foundation to bridge | SQ3; survey 3.C |
| D. Brain-inspired learning and credit assignment | predictive-coding backprop, feedback alignment, dopamine RPE, meta-RL, replay | foundation to bridge | SQ4; survey 3.D |
| E. Deep nets as brain models | goal-driven vision/audition/language models, RSA, neural predictivity, Brain-Score | foundation to frontier | SQ5; survey 3.E |
| F. Spiking and neuromorphic computation | SNN training, surrogate gradients, neuromorphic chips, event-based computation | defer unless needed | SQ7; survey 3.F |
| G. AI for neural and behavioral data | LFADS, CEBRA, pose estimation, connectomics, neural-data foundation models | practical bridge | SQ8; survey 3.G |
| H. Cognitive-level and human-like learning | Bayesian program learning, compositionality, intuitive physics, cognitive architectures | strategic bridge | SQ6; survey 3.H |
| I. BCI and neural decoding | handwriting/speech BCIs, image reconstruction, semantic decoding, non-invasive decoding | applied frontier | SQ9; survey 3.I |
| J. Embodiment and agents | virtual animals, embodied Turing test, sensorimotor control, agent world models | strategic frontier | SQ10; survey 3.J |
| K. Convergence frontiers | connectome-constrained models, digital twins, LLM-brain alignment, mechanistic interpretability | strategic frontier | SQ11; survey 3.K |
| L. Critiques and limitations | prediction vs explanation, benchmark confounds, texture bias, theory deficit | cross-cutting discipline | SQ12; survey 3.L |
| M. Visual intelligence and world models | AI world models, cognitive maps, object-centric reasoning, inverse graphics, intuitive physics | strategic frontier | SQ13; survey 3.M |

## Foundation Stack

Use this ordering when converting the survey into daily learning:

1. **Conceptual frame:** Marr levels; objective/learning-rule/architecture; prediction vs explanation.
2. **Computational-neuroscience base:** coding, normalization, Bayesian inference, predictive coding, dynamics.
3. **Model comparison methods:** encoding models, decoding models, RSA, neural predictivity, benchmarks.
4. **Learning mechanisms:** reinforcement learning, dopamine RPE, credit assignment, replay, meta-learning.
5. **Route-specific frontiers:** language cortex, neural-data foundation models, world models, embodiment, BCI.

## Claim Checklist

Before adding a NeuroAI claim to a note, label it:

| Claim form | Acceptable wording |
| --- | --- |
| Established fact | "The paper shows..." only when the paper's evidence directly supports it. |
| Interpretation | "One interpretation is..." when mapping results into the learner's framework. |
| Working hypothesis | "A useful working hypothesis is..." when the claim guides future reading. |
| Analogy | "This is analogous to..." only when the level of analysis is explicit. |
| Speculation | "Speculatively..." when extrapolating beyond evidence. |
| Open question | "Open question: ..." when the evidence is insufficient or contested. |

## Misclassification Risks

- Treating neural predictivity as mechanistic explanation.
- Treating brain-inspired engineering as biological realism.
- Treating benchmark score as general cognitive competence.
- Treating clinical decoding results as generally reproducible engineering baselines.
- Treating corporate frontier reports as settled science.

Use the critique route, especially P070, P076, P068, and P005, whenever a claim starts to sound too clean.
