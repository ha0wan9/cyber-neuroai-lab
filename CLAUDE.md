<!-- MIRROR — not the source of truth.
     Canonical agent instructions live in AGENTS.md. Edit AGENTS.md, not this file.
     This mirror exists because Claude Code auto-loads CLAUDE.md but not AGENTS.md. -->

# Claude Code Entry Point

The canonical agent instructions for this repository are in **[AGENTS.md](AGENTS.md)**.

Read `AGENTS.md` first — it defines the bootstrap order, project type, working
rules, validation expectations, and memory-writeback policy. Then read local
`USER.md` (Git-ignored) if it exists, and load only the topical files relevant
to the current task.

Do not maintain a second set of rules here. If a global guardrail or the
bootstrap order changes, update `AGENTS.md` and re-sync this pointer only if the
canonical filename or routing changes.
