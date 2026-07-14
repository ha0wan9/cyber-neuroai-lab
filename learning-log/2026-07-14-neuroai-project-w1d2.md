# NeuroAI Research Project — W1D2 Feasibility and Direction Lock

Date: 2026-07-14  
Course day: W1D2  
Status: planning scaffold; group constraints and decision pending

## Today's Required Outcome

By the end of W1D2, reduce the project to:

1. one required research question;
2. one optional analysis that can be cut without damaging the project;
3. one internal scope reduction and one external backup;
4. a verified code/data/compute path for the lead;
5. named owners and a concrete action before W1D3.

The goal is a proposal-ready decision, not a full experiment run.

## Planning Drift to Resolve First

Two current artifacts point in different directions:

- [`research-project-phase-1-credit-assignment.md`](../indexes/research-project-phase-1-credit-assignment.md)
  frames the lead as **Track B**: identify learning-rule signatures from
  representational trajectories.
- [`2026-07-13-neuroai-project-w1d1.md`](2026-07-13-neuroai-project-w1d1.md)
  records a later preference for **Track A**: stress-test e-prop against BPTT
  under one non-stationary shift or task switch.

This is not a minor wording difference. It changes the primary dependent
variables, minimum implementation, and interpretation. W1D2 should choose one
as required and demote the other to optional before any experiment matrix is
expanded.

## Working Recommendation for the Two-Week Project

Use **Track A as the required project** and retain one trajectory analysis as
optional.

> Under a single controlled task switch or non-stationary shift, how do e-prop
> and BPTT differ in adaptation and retention when architecture,
> initialization, training budget, and evaluation are matched?

Why this is the lower-risk primary question:

- it yields a direct learning-curve result even if neural data or advanced
  similarity metrics are blocked;
- it makes a negative result interpretable: the tested condition did not
  reveal a useful trade-off;
- it retains the core credit-assignment comparison;
- trajectory geometry can still explain a result, but the project does not
  depend on successfully solving an inverse-identification problem.

This is an advisor recommendation, not a recorded group decision.

## Proposal Question Stack

### Required question

How do e-prop and BPTT compare in post-shift adaptation speed and retained
pre-shift performance under one matched recurrent task?

### Secondary diagnostic

Are any performance differences accompanied by a difference in update quality,
such as update alignment, variance, or another diagnostic already exposed by
the selected implementation?

### Optional question

Do the two rules follow distinguishable representational trajectories after
matching task performance and initial weights?

Cut the optional question first if it requires new infrastructure, neural data,
or more than one additional metric family.

## Minimal Credible Experiment

| Component | Required choice | W1D2 evidence |
|---|---|---|
| Learning rules | e-prop and BPTT | both enter the same runnable training path |
| Task | one recurrent task only | data are public or generated; metric is understood |
| Stress condition | one task switch or one non-stationary change | exact change point and changed variable are specified |
| Controls | same architecture, paired initial weights where possible, same training/evaluation budget | configuration diff is inspected |
| Replication | smoke test first; later use multiple paired seeds | runtime per seed is measured before fixing the final count |
| Primary outcomes | post-shift recovery and retention | formulas and plotting inputs are specified before W2D1 |
| Optional outcome | one representation-trajectory measure | runnable only after the primary pipeline passes |

### Suggested primary metrics

- recovery time to a preregistered fraction of post-shift performance;
- post-shift area under the learning curve;
- retained performance on the pre-shift task;
- final task performance, reported alongside adaptation rather than alone.

Choose one primary metric before W1D4. The others are supporting diagnostics.

## Fallback Ladder

| Level | Trigger | Deliverable |
|---|---|---|
| A — intended | both e-prop and BPTT run and the shift is implementable | matched stress-test comparison plus one diagnostic |
| B — internal scope reduction | both rules run, but shift or checkpoint analysis is unstable | bounded reproduction on one task plus matched learning curves |
| C — external backup | e-prop environment/data remain blocked after the W1D2 timebox | switch to the already identified Sign-Symmetry project, with its adaptive-attack caveat |

Do not use predictive coding as a third rule or active learning as an additional
data-selection loop in this course project. Their conceptual relationship and
a future microproject are captured in
[`predictive-coding-and-active-learning.md`](../notes/neuroai/predictive-coding-and-active-learning.md).

## W1D2 Feasibility Timebox

### Block 1 — 30 minutes: group constraints

- [ ] Record group members and available hours through W2D5.
- [ ] Record CPU/GPU access and whether every owner can run the code.
- [ ] Choose Track A or Track B as the required question.
- [ ] Confirm that Sign-Symmetry remains the external backup.

### Block 2 — 60 minutes: environment and data probe

- [ ] Clone or inspect the selected official implementation.
- [ ] Record runtime environment, dependency versions, and license.
- [ ] Run the smallest available e-prop and BPTT smoke test.
- [ ] Verify that the same architecture and initial weights can be used.
- [ ] Verify that metrics and checkpoints can be exported without changing the
  learning rule.
- [ ] Record wall-clock runtime and hardware for one smoke run.

### Block 3 — 30 minutes: scope and failure audit

- [ ] Specify the one task and one shift.
- [ ] Choose the primary metric and the smallest supporting metric set.
- [ ] List confounds: unequal tuning, unequal performance, initialization,
  checkpoint timing, and metric sensitivity.
- [ ] Decide the exact trigger for Level B and Level C fallbacks.

### Block 4 — 30 minutes: prepare W1D3

- [ ] Assign one owner to the 2020 e-prop mechanism paper.
- [ ] Assign one owner to the 2025 e-prop/neural-similarity paper or the
  primary stress-test source.
- [ ] Assign one owner to implementation feasibility and runtime logging.
- [ ] Write a one-paragraph project decision for the shared group channel.

## Stop Rules

- If a common e-prop/BPTT smoke path cannot run within a two-hour W1D2
  environment timebox, activate Level B or C rather than spending W1D3 on
  dependency repair.
- If the proposed shift requires changing the learning-rule implementation
  itself, choose a simpler shift.
- If matching architecture and initialization is not possible, do not make a
  causal claim about the learning rule.
- If only one seed is affordable, frame the output as a pipeline demonstration,
  not a robust comparison.
- Do not rescue a null result by adding unplanned metrics or multiple shifts.

## Decision Record — To Complete With the Group

| Field | Decision |
|---|---|
| Required track | TODO: Track A or Track B |
| One-sentence question | TODO |
| Task and shift | TODO |
| Primary metric | TODO |
| Optional analysis | TODO |
| Lead code/data path | TODO |
| Measured runtime | TODO |
| Compute budget | TODO |
| Internal scope reduction | TODO |
| External backup | TODO: confirm Sign-Symmetry or replace with reason |
| Owners | TODO |
| Next action and deadline | TODO |

## W1D2 Exit Gate

W1D2 is complete only when the decision record is filled and at least one
lead-path smoke test has either succeeded or produced a concrete blocker that
triggers the fallback ladder.

Do not start the full seed matrix before this gate passes.
