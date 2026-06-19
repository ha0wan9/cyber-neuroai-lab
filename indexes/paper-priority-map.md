# Paper Priority Map

Purpose: decide which NeuroAI papers to read next and what each paper should produce in the repository. Detailed bibliographic rows live in `.research/surveys/neuroai-foundations-frontiers/paper_index.md`; this file is a daily-learning priority layer.

## Priority Bands

| Priority | Use when | Expected output |
| --- | --- | --- |
| P0 | Paper is needed to understand a current concept, experiment, or claim. | Full paper note plus links to concepts/questions. |
| P1 | Paper anchors an important topic but is not blocking current work. | Structured summary and open questions. |
| P2 | Paper is useful context or a future citation candidate. | Short capture note or backlog entry. |
| Parked | Interesting but not aligned with the current phase. | One-line reason for parking. |

## Post-Neuromatch Reading Path

Read these after the computational-neuroscience basics are usable. Do not read the whole survey linearly.

| Order | Paper IDs | Read for | Priority | Output |
| --- | --- | --- | --- | --- |
| 1 | P003, P004 | Field frame: objective/learning-rule/architecture; embodied Turing test. | P0 | `notes/neuroai/neuroai-field-map.md` updates if needed |
| 2 | P032, P006 | Goal-driven deep nets as brain models. | P0 | Brain-model alignment note |
| 3 | P035, P040 | RSA and Brain-Score as comparison methods. | P0 | Metric caveat checklist |
| 4 | P070, P076 | Prediction vs explanation and human-machine divergence. | P0 | Misconception-index update |
| 5 | P023, P024 | Dopamine RPE and meta-RL bridge. | P1 | RL-in-brain concept note |
| 6 | P020, P022, P026 | Biological credit assignment and backprop alternatives. | P1 | Biological plausibility note |
| 7 | P041, P042, P045 | Latent dynamics and neural-data foundation models. | P1 | AI-for-neural-data map |
| 8 | P036-P038, P071 | LLMs and language cortex. | P1 | Language-brain frontier note |
| 9 | P082, P083, P077, P078, P080 | Brain and AI world models. | P1 | World-model route note |
| 10 | P046, P047, P105 | Connectome/digital-twin/brain-foundation frontier. | P2 until foundations are stable | Frontier brief |

## Topic Priority

| Topic | Candidate papers | Priority | Read for | Defer condition |
| --- | --- | --- | --- | --- |
| Neural coding and normative models | P007-P012 | P0/P1 | Build foundations for representation and dynamics. | Do not over-read before producing concept notes. |
| Encoding and decoding | P032, P035, P040, P058-P064 | P0 for methods; P2 for clinical BCI | Separate prediction, readout, reconstruction, and explanation. | Clinical implementation details can wait. |
| Representation similarity and alignment | P035, P040, P070, P076 | P0 | Learn what similarity metrics can and cannot claim. | None; needed for honest NeuroAI reading. |
| Brain-inspired learning | P020, P022-P026, P093, P095 | P1 | Understand credit assignment, RL, replay, and neuromodulation. | Deep algorithm details can wait until experiments. |
| Neural-data tooling | P041-P045, P100 | P1 | See how AI becomes a neuroscience instrument. | Read methods only when they connect to a toy experiment. |
| Cognitive-level modeling | P050-P055, P094, P101 | P1/P2 | Link human-like learning, compositionality, and behavior prediction. | Defer P101 until critique frame is clear. |
| World models and visual intelligence | P018, P019, P054, P077-P089 | P1/P2 | Connect AI agents with cognitive maps and structured perception. | Read after predictive coding/dynamics basics. |
| Embodiment | P004, P065-P067 | P2 | Understand the embodied Turing test and virtual animals. | Defer until sensorimotor learning is active. |
| Neuromorphic and spiking | P027-P031, P073-P075, P090, P098, P099 | P2/Parked | Learn efficient brain-inspired computation. | Park hardware unless an experiment requires it. |
| Non-invasive decoding and interface | P096, P103-P106 | P2 | Connect decoding to human-AI interface possibilities. | Park ethical/interface synthesis until methods are clear. |

## Foundation Papers

Use these to stabilize the core field:

- **P001:** Marr's levels of analysis.
- **P003:** objective, learning rule, architecture.
- **P004:** NeuroAI roadmap and embodied Turing test.
- **P007-P012:** sparse coding, predictive coding, Bayesian brain, normalization, population dynamics.
- **P023:** dopamine reward-prediction error.
- **P032:** founding goal-driven AI-to-brain model.
- **P035/P040:** RSA and Brain-Score.
- **P070/P076:** critique and texture-bias guardrails.

## Strategic Frontier Papers

Use these for research direction after the foundations:

- **P045/P047/P105:** neural-data and brain foundation models.
- **P046:** connectome-constrained modeling.
- **P036-P038/P071:** LLMs and language cortex.
- **P049/P048:** mechanistic interpretability and manifold geometry.
- **P077-P083:** AI and brain world models.
- **P096/P103-P106:** scalable non-invasive decoding.
- **P101:** foundation model of human cognition, with prediction-vs-explanation caveat.

## Reading Decision Checklist

Before reading a paper, record:

- Which concept or question does it unblock?
- Which misconception might it clarify?
- What artifact should it produce?
- Is this a methods paper, evidence paper, review, dataset, or opinion piece?
- What would count as a useful takeaway?

## Output Rule

Every P0 or P1 paper should update at least one of:

- `indexes/concept-graph.md`
- `indexes/misconception-index.md`
- `indexes/open-questions.md`
- `indexes/research-backlog.md`
- `indexes/research-frontiers.md`
- a concept note in `notes/`
- a paper note in `papers/`

