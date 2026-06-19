# Neuromatch Source Registry

This registry maps official Neuromatch sources into the repository's learning system. It is intentionally structural: it records where each source fits, what it should feed, and what artifacts it should produce. It is not a course summary.

## Source Table

| Source name | URL | Role in the learning system | Stage | Repo folders it should feed into | Expected artifacts |
|---|---|---|---|---|---|
| Computational Neuroscience Coursebook | <https://compneuro.neuromatch.io/> | Primary foundation source for computational neuroscience concepts, mathematical intuition, modeling patterns, and neural-data analysis workflows. | Foundation | `notes/computational-neuroscience/`, `experiments/`, `learning-log/`, `inbox/` | Concept notes, worked-example notes, small simulations, decoding or modeling experiment sketches, learning-log entries, open-question lists. |
| Computational Neuroscience Schedule | <https://compneuro.neuromatch.io/tutorials/Schedule/daily_schedules.html> | Sequencing reference for turning computational neuroscience material into learning units, weekly plans, and progress checkpoints. | Foundation | `learning-log/`, `templates/`, `inbox/`, `notes/computational-neuroscience/` | Learning-unit plans, weekly review prompts, progress checklists, dependency maps, backlog items for unfinished topics. |
| Deep Learning Coursebook | <https://deeplearning.neuromatch.io/tutorials/intro.html> | Bridge source connecting neural computation foundations to modern artificial neural network methods used in NeuroAI. | Bridge | `notes/neuroai/`, `notes/computational-neuroscience/`, `experiments/`, `learning-log/` | Neural network concept notes, implementation exercises, model-comparison sketches, representation-learning notes, experiment plans. |
| NeuroAI Coursebook | <https://neuroai.neuromatch.io/> | Frontier source for organizing NeuroAI topics, research questions, model-brain comparison methods, and synthesis across neuroscience and AI. | Frontier | `notes/neuroai/`, `papers/`, `experiments/`, `learning-log/`, `inbox/` | NeuroAI concept notes, paper-reading queues, research question maps, analysis plans, experiment proposals, synthesis notes. |
| NeuroAI Prerequisites | <https://neuroai.neuromatch.io/prereqs/NeuroAI.html> | Readiness and gap-analysis source for identifying prerequisite knowledge before starting or deepening NeuroAI work. Automated URL checks may sometimes report this page as 404 depending on request method or static-site behavior. Treat it as the official NeuroAI prerequisites page unless manual browser/GET verification fails. | Bridge | `learning-log/`, `notes/computational-neuroscience/`, `notes/neuroai/`, `inbox/` | Prerequisite checklist, gap map, remediation plan, learning backlog, review questions, readiness notes. |

## Stage Definitions

- **Foundation:** prerequisite material that stabilizes mathematical, computational, and neuroscience basics.
- **Bridge:** material that translates foundations into methods needed for NeuroAI work.
- **Frontier:** NeuroAI-facing material that should generate research questions, paper reading, experiments, and synthesis artifacts.

## Maintenance Rules

- Add only durable, official, or clearly authoritative sources to this registry.
- Keep entries structural; put summaries, explanations, and personal interpretations in downstream notes instead.
- Prefer small downstream artifacts over one large course note.
- When a registered source leads to a runnable experiment, record the smallest verification command in the affected experiment artifact.
