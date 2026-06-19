# NeuroAI Field Map

Purpose: turn the full survey in `.research/surveys/neuroai-foundations-frontiers/` into a daily-learning navigation map. This file is not a replacement for the survey; use it to decide what to study now, what to defer, and how each route connects to the lab's long-term directions.

Primary sources:

- Survey index: `.research/surveys/neuroai-foundations-frontiers/index.md`
- Survey synthesis: `.research/surveys/neuroai-foundations-frontiers/survey.md`
- Paper index: `.research/surveys/neuroai-foundations-frontiers/paper_index.md`

## Working Frame

NeuroAI is a bidirectional research program:

- **Brain -> AI:** use neuroscience and cognitive science to design better learning systems.
- **AI -> brain:** use trained AI systems as quantitative models, analysis tools, and hypothesis generators for brains and behavior.
- **Bidirectional/frontier:** build shared methods, benchmarks, digital twins, embodied agents, and cognitive tools.

Use Marr's levels and the objective/learning-rule/architecture decomposition as the default coordinate system before judging any paper's claim.

## Study Now

These topics connect directly to computational-neuroscience prerequisites and should receive daily-learning priority after or alongside Neuromatch.

| Route | Study target | Why now | Survey anchors |
| --- | --- | --- | --- |
| Foundations and framing | Marr levels, NeuroAI roadmap, objective/learning-rule/architecture | Prevents level confusion and vague brain-AI analogy. | SQ1; P001, P003, P004, P005 |
| Classical computational neuroscience | sparse coding, predictive coding, Bayesian brain, normalization, neural manifolds | These are the concepts deep models are supposed to explain or reuse. | SQ2; P007-P012 |
| Encoding, decoding, and brain-model alignment | goal-driven models, RSA, Brain-Score, prediction vs explanation | Builds directly on Neuromatch model fitting, dimensionality reduction, and decoding. | SQ5; P006, P032, P035, P040, P070 |
| Learning and credit assignment | dopamine RPE, feedback alignment, predictive-coding backprop, meta-RL | Connects reinforcement learning, biological plausibility, and deep-learning mechanisms. | SQ4; P020, P022-P026 |
| Neural-data tools | LFADS, CEBRA, pose estimation, neural-data foundation models | Useful for turning neuroscience data into latent dynamics and reusable representations. | SQ8; P041-P045 |

## Strategic Frontiers

Study these after the foundations are usable. They are important for research direction, but they depend on the earlier concepts.

| Frontier | Strategic question | Connects to | Survey anchors |
| --- | --- | --- | --- |
| Brain foundation models and digital twins | Can large neural-data models become reusable scientific instruments? | AI engineering, computational neuroscience | SQ11; P045-P047, P102, P105 |
| LLMs and language cortex | Does language-model alignment imply shared mechanism or only predictive correlation? | cognitive neuroscience, AI engineering | SQ5/SQ11; P036-P038, P071 |
| World models and visual intelligence | Are predictive world models enough for flexible cognition, or is structured representation required? | AI agents, cognitive maps, external cognition | SQ13; P077-P089, P018, P019 |
| Embodied agents | Can embodied AI provide better brain models than passive recognition systems? | cognitive neuroscience, AI engineering | SQ10; P004, P065-P067 |
| BCI and non-invasive decoding | What can neural decoders recover, and what privacy/ethics constraints follow? | human-AI interface | SQ9; P058-P064, P096, P103-P106 |
| Mechanistic interpretability as neuroscience of AI | Can neuroscience-style analysis explain artificial networks? | AI engineering, external cognition | SQ11; P049, P048 |

## Defer For Now

These are useful, but they are less urgent for the current computational-neuroscience learning phase unless a task explicitly needs them.

| Topic | Reason to defer | Revisit when |
| --- | --- | --- |
| Neuromorphic hardware details | Requires hardware/ecosystem specifics beyond current learning loop. | Energy-efficient AI or spiking-system experiments become active. |
| Clinical BCI implementation details | Evidence is often access-bound and clinical-N=1; first learn decoding concepts. | Human-AI interface or neuroethics writing becomes active. |
| Corporate frontier reports | Often early and partially reproducible; useful as frontier signals, not foundations. | Comparing research programs or writing a frontier brief. |
| Full paper-by-paper survey expansion | The survey already stores this. | A specific route becomes an active paper-reading project. |

## Direction Links

| Lab direction | Relevant NeuroAI routes | Useful first question |
| --- | --- | --- |
| AI engineering | brain-inspired architectures, credit assignment, world models, mechanistic interpretability | Which brain-inspired idea changes an engineering constraint rather than just a metaphor? |
| Cognitive neuroscience | goal-driven models, language cortex, cognitive maps, embodied agents | What behavior or neural data would distinguish model fit from mechanism? |
| Human-AI interface | BCI, cognitive foundation models, external cognition, decoding ethics | What should an interface augment: memory, attention, explanation, or action? |
| External cognition | AI-assisted research systems, mechanistic interpretability, foundation models of cognition | Can model outputs become durable reasoning artifacts rather than transient answers? |

## Daily Use

When choosing what to study next:

1. Prefer topics in **Study Now** until the key computational-neuroscience concepts are stable.
2. Use `indexes/paper-priority-map.md` to pick a paper only when it unblocks a concept note, experiment, or question.
3. Use `indexes/research-frontiers.md` for strategic direction, not for daily reading unless the foundation is already in place.
4. When in doubt, ask: does this topic clarify representation, dynamics, learning, decoding, or explanation?

