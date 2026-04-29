# Agent Instructions

This repository is a personal research and learning lab for NeuroAI, computational neuroscience, cognitive systems, and AI-assisted scientific workflows.

## Bootstrap Order

1. Read this file first.
2. Read `USER.md` if it exists locally. It is ignored by Git and stores user-specific collaboration preferences.
3. Inspect `README.md` lightly before full loading. Read the full README only when the task edits shared project docs or depends on global project semantics.
4. Load only the topical files needed for the current task:
   - `CONTRIBUTING.md` for content standards, file naming, AI-generated content rules, and commit-message style.
   - `ROADMAP.md` for phase planning, research direction, and backlog updates.
   - `agents/research-workflow.md` for AI-assisted learning-unit and paper workflows.
   - `notes/*/README.md` for domain-specific note organization.
   - `experiments/README.md` for experiment artifacts.
   - `papers/README.md` for paper-reading artifacts.
   - `learning-log/README.md` for chronological learning records.
   - `templates/*.md` when creating new learning units, paper notes, experiments, or weekly reviews.
5. If `RTK.md` exists in the repo root, read it before starting work that may affect research tooling or knowledge routines.

## Project Type

This is a documentation, research, and knowledge-base repository with a small experiments area. Treat Markdown artifacts as primary outputs unless a task explicitly asks for runnable code, notebooks, or automation.

## Working Rules

- Preserve the existing folder structure unless a durable reorganization is explicitly needed.
- Prefer small, modular Markdown artifacts over large mixed-purpose notes.
- Use lowercase kebab-case for new files.
- Treat AI-generated content as draft material. Important claims should distinguish established fact, interpretation, working hypothesis, analogy, speculation, and open question.
- Check important scientific claims against primary or authoritative sources when accuracy matters.
- Avoid copying large passages from source materials.
- Do not add secrets, local machine state, or unresolved hypotheses to committed project memory.
- Before jumping into a task, check whether an available skill or best-practice reference clearly applies, and use it when it reduces risk or repeated work.

## Validation

There is no project-wide build or test command yet. For documentation-only changes, validate by checking:

- Markdown structure and links in touched files.
- Consistency with `README.md`, `CONTRIBUTING.md`, `ROADMAP.md`, and the relevant topical README.
- Whether a durable learning artifact was produced when the task concerns learning or research synthesis.

For code or notebook work under `experiments/`, add or document the smallest runnable verification command in the affected artifact.

## Memory Writeback

Update this file when a future agent would otherwise repeat a repo-specific discovery or mistake. Keep updates concise and durable.

Use `USER.md` only for explicit, stable user preferences. Keep `USER.md` local-only.

## Knowledge Base

- `README.md` is the primary user-facing project explanation and is currently short enough for full reading when global context is needed.
- `agents/research-workflow.md` is the canonical agent-facing workflow for learning units and paper-reading assistance.
- The root currently has no package manager, dependency file, or project-wide test runner; do not invent one for documentation-only work.
