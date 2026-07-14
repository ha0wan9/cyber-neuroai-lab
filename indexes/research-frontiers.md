# Research Frontiers

Purpose: track NeuroAI frontiers that may become research projects, paper clusters, experiments, or public writing. This index points to the full survey instead of duplicating it.

Primary source: `.research/surveys/neuroai-foundations-frontiers/survey.md`, especially sections 10-13.

## Frontier Map

| Frontier | Core question | Why it matters | Current status | First learning move |
| --- | --- | --- | --- | --- |
| Biologically constrained credit assignment | Can local or approximate learning rules be distinguished by the representations and dynamics they produce, rather than task accuracy alone? | Connects learning mechanisms to brain–model comparison and tests what neural similarity can reveal about learning. | working candidate — W1D1 | Use [`research-project-phase-1-credit-assignment.md`](research-project-phase-1-credit-assignment.md) to compare the lead and backup before W1D4. |
| Brain foundation models and digital twins | Can large neural-data models become reusable instruments for in-silico neuroscience? | Connects AI engineering with experimental neuroscience and model-brain alignment. | strategic frontier | Read P045, P047, P105 after encoding/decoding basics. |
| Foundation models of cognition | Can behavior-scale models predict human choices without collapsing into curve fitting? | Bridges cognitive science, LLMs, and human-AI interface design. | watch closely | Read P101 with P070 and P068 as critique companions. |
| LLMs and language cortex | Is language-model-brain alignment evidence of shared computation or shared objective pressure? | Important for cognitive neuroscience and AI interpretability. | active frontier | Read P036-P038, then P071. |
| Connectome-constrained modeling | Can anatomical wiring reduce free parameters and improve mechanistic explanation? | A possible route from prediction toward mechanism. | active frontier | Read P046, then compare with P047. |
| World models and visual intelligence | Does flexible intelligence require predictive, structured, object-centric world models? | Links AI agents, hippocampal cognitive maps, and visual reasoning. | active frontier | Read P082/P083 for brain side; P077/P078/P080 for AI side. |
| Embodied NeuroAI | Can embodied agents reveal neural representations that passive datasets miss? | Aligns with the embodied Turing test and sensorimotor cognition. | developing frontier | Read P004, then P065/P066. |
| Non-invasive neural decoding | How far can MEG/EEG/fMRI decoding scale, and what should interfaces do with it? | Direct bridge to human-AI interface and neuroethics. | applied frontier | Read P096, P103, P106 after basic decoding models. |
| Mechanistic interpretability as neuroscience of AI | Can tools for analyzing artificial networks become a shared language with neuroscience? | Connects AI engineering, representation geometry, and explanation. | strategic bridge | Read P049 with P048 and the prediction-vs-explanation critique. |
| Neuromorphic and spiking AI | Can spiking/event-based systems deliver useful efficiency without sacrificing capability? | Relevant to edge AI and biologically grounded computation. | defer unless active | Read P027/P031 before hardware papers. |

## Frontier Readiness

| Readiness | Meaning | Candidate frontiers |
| --- | --- | --- |
| Ready after Neuromatch | Needs only encoding/decoding, dynamics, and representation basics. | brain-model alignment, LLM-brain alignment, neural-data tools |
| Ready after extra ML study | Needs deep learning, sequence models, or foundation-model context. | brain foundation models, world models, mechanistic interpretability |
| Ready after cognitive-science study | Needs human learning, compositionality, or cognitive architecture context. | foundation models of cognition, visual intelligence, external cognition |
| Parked until project need | Needs hardware, clinical constraints, or ethics framing. | neuromorphic hardware, clinical BCI details |

## External Cognition Angle

The most relevant frontiers for this lab's external-cognition direction are:

- **Foundation models of cognition:** possible models of human task behavior, but must be checked against theory-deficit critiques.
- **Mechanistic interpretability:** a way to make AI systems inspectable as cognitive artifacts.
- **Human-AI interface and decoding:** a design space for augmenting communication, attention, memory, and action.
- **AI-assisted research systems:** not a standalone survey route, but a downstream application of the same map-building and claim-validation discipline.

## Open Questions

| Question | Related route | Status |
| --- | --- | --- |
| What evidence would convert model-brain alignment from prediction into explanation? | E, K, L | active |
| Can a brain foundation model support causal hypothesis testing, or only interpolation? | G, K | exploratory |
| What is the right benchmark for embodied intelligence beyond passive recognition? | J, M | exploratory |
| Do world models need explicit object/relational structure? | M | exploratory |
| Which neural-decoding capabilities should become interfaces, and which should remain research-only? | I | parked until ethics review |
