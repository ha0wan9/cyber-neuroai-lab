# Repository Audit — NeuroAI Readiness

Date: 2026-06-17  
Scope: structure-first readiness for NeuroAI, computational neuroscience, deep learning, and cognitive systems learning/research.

## Audit Frame

This audit treats the repository as a learning and research system, not as a finished knowledge base. All proposed additions below are recommendations, not claims that the repository is deficient for every possible use case.

Reviewed structure:

- `README.md`
- `ROADMAP.md`
- `CONTRIBUTING.md`
- `agents/research-workflow.md`
- `templates/learning-unit-template.md`
- `notes/*/README.md`
- `experiments/README.md`
- `papers/README.md`

## 1. Existing Strengths

- Clear repository identity: the project is framed as a long-term external cognition system for NeuroAI, computational neuroscience, cognitive systems, and AI-assisted research.
- Strong phase structure: `ROADMAP.md` separates repository setup, computational neuroscience foundations, NeuroAI bridge work, research direction formation, and public output.
- Good epistemic hygiene: contributor guidance and agent workflow already require separating facts, interpretations, hypotheses, analogies, speculation, and open questions.
- Useful domain separation: `notes/computational-neuroscience/`, `notes/neuroai/`, and `notes/cognitive-systems/` each define purpose, core questions, and candidate note areas.
- Durable artifact bias: the README and workflow emphasize converting learning units into notes, experiments, paper summaries, question maps, and weekly reviews.
- Experiment philosophy is appropriately lightweight: `experiments/README.md` recommends small simulations, neural-data notebooks, and NeuroAI probes rather than premature large projects.
- Paper workflow has research-map orientation: `papers/README.md` asks for problem, assumptions, method, evidence, contribution, uncertainty, and integration.
- Templates are mechanism-oriented: the learning-unit template asks for intuition, mechanism, mathematical object, simulation idea, neuroscience connection, AI/NeuroAI connection, misconceptions, and outputs.

## 2. Missing Execution Layers

Recommendations:

- Add a lightweight `indexes/` layer for maps, audits, backlogs, and cross-domain navigation.
  - This audit can be the first artifact in that layer.
  - Suggested follow-up: `indexes/research-question-backlog.md`.
- Add a monthly or biweekly operating cadence.
  - Suggested follow-up: `learning-log/weekly-reviews/` or `learning-log/monthly-reviews/` only when review files begin accumulating.
  - Keep the cadence simple: plan, learn, implement one artifact, review, consolidate.
- Add a course/session tracking layer.
  - Suggested follow-up: `indexes/course-map.md` linking external learning sources to repo outputs.
  - Track source, topic, output note, output experiment, related paper, and open question.
- Add an artifact status index.
  - Suggested statuses: `raw`, `structured`, `reviewed`, `consolidated`, `public-candidate`.
  - This should reference existing files rather than duplicate their content.
- Add a dependency map for concepts.
  - Recommended minimal form: a Markdown table of prerequisite relationships, not a graph system.
  - Example relationship types: `requires`, `supports`, `bridges-to`, `experiment-for`, `paper-evidence-for`.

## 3. Missing Concept Notes

The README files list many candidate notes, but the repository currently appears to have mostly scaffolding rather than filled concept notes. Recommended first concept notes:

### Computational Neuroscience

- `notes/computational-neuroscience/neural-code.md`
- `notes/computational-neuroscience/rate-coding.md`
- `notes/computational-neuroscience/spike-train.md`
- `notes/computational-neuroscience/population-coding.md`
- `notes/computational-neuroscience/tuning-curve.md`
- `notes/computational-neuroscience/encoding-model.md`
- `notes/computational-neuroscience/decoding-model.md`
- `notes/computational-neuroscience/dynamical-systems.md`
- `notes/computational-neuroscience/attractor.md`
- `notes/computational-neuroscience/pca-for-neural-data.md`

### NeuroAI

- `notes/neuroai/brain-model-alignment.md`
- `notes/neuroai/representation-similarity-analysis.md`
- `notes/neuroai/encoding-models-in-neuroai.md`
- `notes/neuroai/neural-representation.md`
- `notes/neuroai/representation-geometry.md`
- `notes/neuroai/brain-score.md`
- `notes/neuroai/biological-plausibility.md`

### Deep Learning Bridge

Recommendation: create a small deep-learning bridge only when needed by actual learning units. Possible locations:

- `notes/neuroai/deep-learning-bridge.md`, or
- `notes/neuroai/representation-learning.md`, or
- a future `notes/deep-learning/README.md` if the area becomes large enough.

Recommended bridge concepts:

- gradient descent as representation shaping;
- backpropagation as an engineering mechanism, with caveats about biological plausibility;
- convolutional networks and visual hierarchy as a comparison topic;
- recurrent neural networks as dynamical systems;
- transformers as sequence and representation models;
- embeddings and latent spaces;
- probing, linear readouts, and interpretability limits.

### Cognitive Systems

- `notes/cognitive-systems/external-cognition.md`
- `notes/cognitive-systems/structure-first-learning.md`
- `notes/cognitive-systems/learning-loop.md`
- `notes/cognitive-systems/agentic-workflows.md`
- `notes/cognitive-systems/research-question-backlog.md`
- `notes/cognitive-systems/paper-reading-workflow.md`

## 4. Missing Experiment Scaffolds

Recommendations:

- Add one experiment folder per runnable mechanism only when implementation starts.
- Start with experiments that directly support the first concept notes.
- Include a short `README.md` per experiment with the smallest runnable command.

Recommended initial experiment scaffolds:

1. `experiments/lif-neuron/`
   - Recommended question: how do membrane time constant, threshold, and input current affect spiking?
   - Recommended output: simple plot and parameter sweep.
2. `experiments/spike-train-statistics/`
   - Recommended question: how do simple spike-train summary statistics change under different generative assumptions?
   - Recommended output: synthetic spike rasters and basic summary metrics.
3. `experiments/population-coding/`
   - Recommended question: how can a variable be represented across a population rather than a single unit?
   - Recommended output: tuning curves and decoded estimate.
4. `experiments/encoding-decoding-toy/`
   - Recommended question: what differs between predicting neural response from stimulus and predicting stimulus from neural response?
   - Recommended output: paired toy encoding and decoding regressions.
5. `experiments/pca-neural-population/`
   - Recommended question: when does dimensionality reduction reveal useful latent structure?
   - Recommended output: synthetic population activity and PCA visualization.
6. `experiments/attractor-dynamics/`
   - Recommended question: how do initial conditions and recurrent dynamics shape state evolution?
   - Recommended output: phase portrait or trajectory plot.
7. `experiments/rsa-toy/`
   - Recommended question: how can representational similarity compare two systems without requiring unit-by-unit identity?
   - Recommended output: toy representational dissimilarity matrices and comparison metric.

## 5. Missing Course-to-Repo Mapping

Recommendation: add `indexes/course-map.md` before adding many course notes.

Suggested columns:

| Source | Unit | Core concept | Repo note | Experiment | Paper link | Status | Open question |
| --- | --- | --- | --- | --- | --- | --- | --- |

Recommended usage:

- One row per lecture, chapter, assignment, paper cluster, or self-study module.
- Do not store full course content.
- Track only the transformation from external input into repo-native artifacts.
- Prefer linking each course unit to exactly one primary durable output.
- Use the learning-unit template for units that require synthesis.

Potential first mappings:

- Computational neuroscience prerequisite material → neural coding, spike trains, encoding/decoding, dynamics, dimensionality reduction.
- Deep learning prerequisite material → representation learning, recurrent models, embeddings, probing, model comparison.
- NeuroAI papers → brain-model alignment, representation similarity, behavioral modeling, brain-guided model design.
- Cognitive systems readings → external cognition, agentic workflows, AI-assisted research reliability.

## 6. Missing Review / Consolidation Mechanisms

Recommendations:

- Add a recurring review artifact.
  - Suggested file pattern: `learning-log/YYYY-MM-DD-weekly-review.md` until volume justifies subfolders.
  - Use `templates/weekly-review-template.md` if it already matches current needs.
- Add a monthly consolidation checklist.
  - Recommended questions:
    1. Which concepts moved from `raw` to `structured`?
    2. Which notes became stable enough for `reviewed`?
    3. Which claims still need sources?
    4. Which experiments should be run next?
    5. Which paper notes changed the research direction?
    6. Which open questions became researchable?
- Add a cross-linking pass after every 3-5 artifacts.
  - Link concept notes to experiments.
  - Link paper notes to concept notes.
  - Link open questions to roadmap phases.
- Add a `public-candidate` review step.
  - Recommended purpose: identify notes that could become blog posts, diagrams, tutorials, or reproducible notebooks.
- Add a stale-artifact review.
  - Recommended cadence: monthly or after major topic shifts.
  - Purpose: archive, merge, or mark notes that no longer represent current understanding.

## 7. Priority-Ranked TODO List

### P0 — Immediate Structure

1. Create `indexes/` as the cross-repo navigation and audit layer.
2. Add `indexes/course-map.md` to connect learning inputs to durable outputs.
3. Add `indexes/research-question-backlog.md` to prevent questions from being trapped inside individual notes.
4. Add the first weekly or monthly review using the existing weekly review template.

### P1 — Foundational Concepts

5. Write `notes/computational-neuroscience/neural-code.md`.
6. Write `notes/computational-neuroscience/spike-train.md`.
7. Write `notes/computational-neuroscience/encoding-model.md`.
8. Write `notes/computational-neuroscience/decoding-model.md`.
9. Write `notes/computational-neuroscience/dynamical-systems.md`.
10. Write `notes/neuroai/brain-model-alignment.md`.
11. Write `notes/neuroai/representation-similarity-analysis.md`.

### P2 — Executable Understanding

12. Scaffold `experiments/lif-neuron/` with a README and minimal runnable script or notebook.
13. Scaffold `experiments/population-coding/` with a README and minimal runnable script or notebook.
14. Scaffold `experiments/encoding-decoding-toy/` with a README and minimal runnable script or notebook.
15. Scaffold `experiments/pca-neural-population/` with a README and minimal runnable script or notebook.
16. Scaffold `experiments/rsa-toy/` after the first NeuroAI alignment note exists.

### P3 — Integration and Consolidation

17. Add a status index for notes, experiments, and paper artifacts.
18. Add a concept dependency map.
19. Add a paper-to-concept map once paper notes begin accumulating.
20. Add a monthly consolidation checklist to the learning-log workflow.
21. Identify the first 1-2 `public-candidate` artifacts.

## Recommended Next Move

Recommended next move: create `indexes/course-map.md` and `indexes/research-question-backlog.md`, then write the first computational neuroscience concept note and pair it with one small experiment scaffold.
