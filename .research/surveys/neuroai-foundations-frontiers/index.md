# neuroai-foundations-frontiers

> Master record for this BFS literature survey. Phase artifacts cross-reference
> this file. Sub-questions and scope are fixed at frame time.

## Identity

- Survey ID: `neuroai-foundations-frontiers`
- Created UTC: `2026-06-02T00:00Z`
- Owner: Haoran Wang
- Status: `v6-shipped`
- Survey root: `.research/surveys/neuroai-foundations-frontiers/`
- Parent / superseded: `none`

## Research Question

Map the field of **NeuroAI** — the intersection of computational and cognitive
neuroscience with artificial intelligence — from its foundational/cornerstone
work through its current frontiers. The survey must capture both directions of
the brain↔AI exchange: how neuroscience informs the design of learning machines
(brain → AI), and how trained AI systems serve as quantitative models and
analysis tools for biological brains (AI → brain). The user explicitly requires
a **taxonomy with no major omissions** across this broad field, spanning
classical computational-neuroscience theory, neuro-inspired architectures and
learning algorithms, deep-net models of neural representation, cognitive-level
modeling, spiking/neuromorphic computing, AI-for-neural-data tooling, brain–
computer interfaces, embodied agents, present-day convergence frontiers
(foundation models, LLMs↔language cortex, connectome-constrained models,
mechanistic interpretability), and the field's critiques and open problems.

## Scope

| Dimension | In scope | Out of scope |
|---|---|---|
| Disciplinary span | Computational neuroscience, cognitive science/AI, systems & theoretical neuroscience, ML/DL where it explicitly engages the brain | Pure ML with no brain claim; clinical neurology unrelated to computation; wet-lab molecular neuroscience without a computational model |
| Direction of influence | Both brain→AI (inspiration) and AI→brain (modeling/analysis) | One-off metaphors with no operationalized model |
| Model scale | Single-neuron models → population/circuit models → whole-network deep models → foundation/large models | — (all scales in scope) |
| Time range | Cornerstones from ~1940s–2010s (Hodgkin-Huxley, perceptron, Marr, backprop, efficient coding, predictive coding) through frontier work to mid-2026 | — |
| Signal/modality | Spikes, LFP/EEG/MEG, fMRI, calcium imaging, behavior, connectomes, and the AI models built on/for them | Genomics/transcriptomics-only methods without a neural-computation model |
| Application angle | BCI/neural decoding, neuromorphic hardware, neural-data analysis tooling, embodied control | General robotics/hardware with no neuroscience link |
| Language/region | Global; English-language venues primary, no regional restriction | — |

## Sub-Questions

Decomposition into 12 discrete answerable sub-questions. Together they tile the
NeuroAI field; each is answerable by ≥3 papers and partitions the space (pairwise
overlap kept <30% by separating *direction of influence* and *level of analysis*).

1. **SQ1 — Foundations & field framing**: What defines NeuroAI as a field, and
   what conceptual scaffolding underpins it (Marr's levels of analysis, the
   connectionism/PDP lineage, the bidirectional brain↔AI research program, and
   recent field-defining manifestos/roadmaps)?
2. **SQ2 — Classical computational-neuroscience cornerstones**: What foundational
   theories and models of neural computation does NeuroAI build on or must
   explain (biophysical & integrate-and-fire neuron models, efficient/sparse
   coding, predictive coding, the Bayesian brain, divisive normalization,
   population coding & dynamical-systems views)?
3. **SQ3 — Brain → AI architectures**: How has neuroscience inspired AI
   architectures and structural mechanisms (visual cortex → Neocognitron/CNNs,
   attention, memory-augmented networks / Neural Turing Machine–DNC, attractor &
   continuous-attractor networks, world-model architectures)?
4. **SQ4 — Brain → AI learning algorithms & credit assignment**: How do
   biologically motivated learning rules relate to deep learning's backprop
   (predictive coding, equilibrium propagation, feedback alignment, target prop,
   Hebbian/local rules, RL ↔ dopamine reward-prediction-error, meta-RL ↔
   prefrontal cortex, complementary learning systems ↔ replay)?
5. **SQ5 — AI → brain: deep nets as models of neural representation**: How well
   do task-trained deep networks predict and explain neural activity across
   systems (goal-driven ventral-stream/CNN vision models, auditory cortex models,
   language-model↔brain alignment, RSA & neural-predictivity methodology,
   emergent grid cells in navigation RNNs, motor-cortex dynamical RNNs)?
6. **SQ6 — Cognitive-level & human-like learning**: How do AI systems model
   higher cognition (Bayesian concept learning & program induction,
   compositionality & systematic generalization, intuitive physics/psychology &
   theory of mind, cognitive architectures, "machines that learn and think like
   people")?
7. **SQ7 — Spiking, neuromorphic & energy-efficient computation**: What is the
   state of spiking neural networks and neuromorphic hardware as a
   brain-inspired efficient-computation route (SNN training, surrogate gradients,
   event-based sensing, Loihi/TrueNorth/SpiNNaker-class systems)?
8. **SQ8 — AI as a tool for neural & behavioral data**: How is ML used to
   analyze neuroscience data (latent neural-dynamics models LFADS/CEBRA/pi-VAE,
   markerless pose estimation, connectomics segmentation, spike sorting,
   emerging neural-data foundation models)?
9. **SQ9 — Brain–computer interfaces & neural decoding (applied frontier)**:
   What are the applied decoding/BCI frontiers (handwriting & speech BCIs, motor
   intent decoding, and image/semantic reconstruction of perceived or imagined
   stimuli from brain activity)?
10. **SQ10 — Embodiment, sensorimotor control & agents**: How does embodied
    NeuroAI work (the embodied Turing test, virtual-animal models, biologically
    grounded motor control, and world-model / autonomous-agent programs)?
11. **SQ11 — Convergence frontiers**: Where are AI and neuroscience actively
    converging now (LLMs as models of language cortex, connectome-constrained &
    "digital-twin" whole-circuit models, mechanistic interpretability as a
    "neuroscience of AI", brain foundation models, representational-geometry /
    manifold-capacity theory)?
12. **SQ12 — Critiques, limitations & open problems** *(mandatory critical SQ)*:
    What does the field still get wrong (do DNNs really model biological vision?,
    benchmark/Brain-Score overfitting, biological-plausibility limits of backprop
    analogues, the brain-as-computer metaphor debate, reproducibility, and the
    persistent integration gap between the two parent disciplines)?
13. **SQ13 — Visual intelligence & world models (world cognition)** *(v2 added,
    2026-06-02)*: How do brains and AI build internal *world models* and achieve
    *visual intelligence beyond passive recognition* — predictive/generative world
    models (World Models, JEPA/V-JEPA, Dreamer, generative interactive
    "world simulators" like Genie; the "is video generation a world model?"
    debate), cognitive maps and the hippocampal-entorhinal world model
    (Tolman-Eichenbaum Machine, successor representation / predictive map),
    object-centric & relational visual reasoning (slot attention, neuro-symbolic
    concept learners), and vision-as-inverse-graphics / intuitive-physics-as-
    simulation? *(Added post-v1 as an explicit, changelogged frame amendment, not
    a silent edit; populated by Round 3. Existing paper IDs and claims unchanged.)*

## Active Evidence Dimensions

Per sub-question, dimensions required for closure (✓ = active; blank = N/A):

| Sub-question | theory | experiment | survey | critical-review | dataset |
|---|---|---|---|---|---|
| SQ1 | ✓ | | ✓ | ✓ | |
| SQ2 | ✓ | ✓ | ✓ | | |
| SQ3 | ✓ | ✓ | | | |
| SQ4 | ✓ | ✓ | | ✓ | |
| SQ5 | ✓ | ✓ | | ✓ | ✓ |
| SQ6 | ✓ | ✓ | | | ✓ |
| SQ7 | ✓ | ✓ | ✓ | | |
| SQ8 | ✓ | ✓ | | | ✓ |
| SQ9 | | ✓ | | | ✓ |
| SQ10 | ✓ | ✓ | | | |
| SQ11 | ✓ | ✓ | ✓ | | |
| SQ12 | | | ✓ | ✓ | |
| SQ13 | ✓ | ✓ | | | |

## Star Rating Rubric

Reference: `references/paper-rating-rubric.md`. No project-specific weight
overrides. Note: "Authority" is dimension-neutral — a clinical/biology venue
(Nature, Neuron, NEJM, Nature Neuroscience, eLife, PNAS) counts equally with ML
venues (NeurIPS/ICLR/ICML). Seminal-author bonus applies for field founders.

## Bias Audit Thresholds

Defaults: any single bucket exceeding 60% of ★★★ papers triggers a targeted
re-search. NeuroAI has known concentration risks (US/UK + a handful of labs:
DiCarlo/MIT, Stanford, DeepMind, Tenenbaum/MIT, Friston/UCL, Kriegeskorte) — watch
institution and country closely.

| Bucket | Threshold | Notes |
|---|---|---|
| Institution | 60% | Watch MIT / Stanford / DeepMind / UCL clustering |
| Country | 60% | Watch US/UK dominance; seek EU/Asia work |
| Year | 60% | Cornerstones must coexist with frontier; avoid all-recent skew |
| Method route | 60% | Avoid all-deep-net skew; keep spiking/Bayesian/dynamical routes |
| Direction of influence | 60% | Balance brain→AI vs AI→brain papers |
| Venue type (preprint) | 60% | Confirm peer-review status via OpenReview/DBLP |

## Round 1 Source Plan

| Source | Keywords / queries | Cap |
|---|---|---|
| arXiv | `cat:q-bio.NC`; `NeuroAI`; `deep learning neuroscience`; `predictive coding deep network`; `spiking neural network`; `goal-driven model visual cortex`; `language model brain encoding`; `biologically plausible backpropagation` | 30-50 candidates |
| OpenReview | NeurIPS, ICLR, ICML (+ workshops: "SVRHM", "NeurReps", "Real Neurons & Hidden Units", "From Neuroscience to AI") | 10-20 candidates |
| DBLP | seminal authors: Yamins, DiCarlo, Kriegeskorte, Tenenbaum, Lake, Richards, Lillicrap, Friston, Olshausen, Sussillo, Schrimpf | 5-15 confirmations |
| Semantic Scholar | citation BFS from seeds: Zador 2023 NeuroAI roadmap; Yamins & DiCarlo 2016; Richards et al. 2019 "deep learning framework for neuroscience"; Hassabis et al. 2017 "Neuroscience-inspired AI" | as needed |
| Web search (brave/tavily) | confirm venue, citation counts, and 2024–2026 frontier work not yet indexed | as needed |

## Pointers

- `paper_index.md` — paper rows (P001, P002, ...)
- `claims.jsonl` — anti-hallucination claim contract
- `coverage_matrix.md` — sub-question × dimension matrix
- `survey.md` — synthesized prose (built only after audit-passed)
- `audits/` — round-by-round audit reports

## Changelog

| UTC | Change | Reason |
|---|---|---|
| 2026-06-02T00:00Z | Survey framed: 12 sub-questions, scope, source plan, bias thresholds | Initial frame phase |
| 2026-06-02T00:30Z | Round 1: 70 papers indexed (49 ★★★) via 4 parallel multi-source search agents. Cap deviation documented (12 SQs). | round1 phase |
| 2026-06-02T00:45Z | Audit: 32/33 cells closed; SQ11-survey gap + country soft-trigger → Round 2. Bowers (P070) retagged SQ5. | audit phase |
| 2026-06-02T01:10Z | Round 2: +6 papers (P071–P076), P005 retagged SQ11. 33/33 closed, 0 gaps. Country limitation accepted+documented. audit-passed. | roundn+audit |
| 2026-06-02T01:40Z | Synthesized survey.md (14 §, 12-route taxonomy, lineage+critique Mermaid graphs, 77 claims). claims_validate + synthesize_self_check pass. | synthesize |
| 2026-06-02T02:10Z | **v2 frame amendment**: added SQ13 (visual intelligence & world models) per explicit user request (changelogged, not silent). Round 3 appended P077–P089 (8 ★★★) + cross-tagged P018/P019/P054/P067. | version (SQ13) |
| 2026-06-02T02:40Z | **v3 Round 4** (last round, cap=4): weak-cell + bias hardening. Added P090–P095 (NSD+THINGS ★★★ fix SQ5/SQ9 dataset cells; Roy/Whittington-Bogacz/Lieder-Griffiths/Doya ★★ diversify SQ7/SQ4/SQ6 + country). 35/35 closed. | roundn+version |
| 2026-06-02T03:00Z | **v4 Round 5** (user-directed France bias `version` pass): added P096–P100 (Défossez+Kheradpisheh ★★★; Dehaene/Denève/nilearn ★★). French ★★★ 2→4; US/UK share ~85%→~77%. Mallat dropped (rel=1). 35/35 closed. | version (France) |
| 2026-06-02T03:20Z | **v5 Round 6** (user-flagged big-lab frontier `version` pass): added P101–P104 — Centaur (Nature 2025, foundation model of cognition) + Meta Brain&AI line (TRIBE Algonauts-2025 winner, Benchetrit MEG decoding ★★★; Brain2Qwerty ★★). SQ5/6/11 frontier strengthened. 68 ★★★, 35/35 closed. | version (frontier) |
| 2026-06-02T03:40Z | **v6 Round 7** (user correction: TRIBE v2): corrected prior "TRIBE single-paper" error. Added P105 TRIBE v2 (in-silico-neuroscience foundation model; succeeds P102=v1) + P106 word-decoding (Nat Commun 2025, 723 ppl), both ★★★. 70 ★★★, 35/35 closed. | version (TRIBE v2) |
