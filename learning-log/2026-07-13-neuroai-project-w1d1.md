# NeuroAI Research Project — W1D1 Exploration Log

Date: 2026-07-13  
Course day: W1D1  
Status: active; group inputs pending

## Today's Purpose

Explore candidate directions, form or align with the group, and reduce the
candidate space without prematurely locking a project.

## Candidate Set

1. e-prop and neural similarity — current working lead.
2. Dendritic Localized Learning.
3. Counter-Current Learning.
4. Sign-Symmetry fine-tuning — current low-cost backup.

The evidence and preliminary comparison are stored in
[`research-project-phase-1-credit-assignment.md`](../indexes/research-project-phase-1-credit-assignment.md).

## What Is Already Prepared

- four candidates are tied to primary sources;
- a preliminary feasibility/fit matrix exists;
- a draft e-prop trajectory question exists;
- the distinction between biological plausibility and biological mechanism is
  explicit;
- a fallback direction is identified.

These are draft inputs for discussion, not a group decision.

## Group Discussion Prompts

1. Does the group want Direction A (design/stress-test a learning rule) or
   Direction B (infer a hidden rule from observable signatures)? See
   [`microlearning-project-two-directions.md`](../notes/neuroai/microlearning-project-two-directions.md).
2. Which direction can every group member explain and contribute to within two
   weeks?
3. What compute, GPU access, data access, and implementation experience does the
   group actually have?
4. Is the group more interested in a neuroscience-facing result
   (e-prop/neural similarity) or a lower-risk AI robustness result
   (Sign-Symmetry)?
5. What result would still be worth presenting if reproduction fails?
6. Who will own the W1D2 feasibility check for the lead and backup directions?

## Decisions Pending

- [ ] group members and roles;
- [ ] available compute and time per person;
- [ ] two candidates surviving to W1D2;
- [ ] working lead and backup accepted by the group;
- [ ] owner for each W1D2 feasibility check.

## Preference Signal

- Track A currently feels more attractive because it offers a larger
  construction and evaluation space.
- This is a W1D1 preference, not a locked direction.
- The recommended two-week interpretation is **existing rule + one new stress
  condition + a small metric set**, rather than inventing a complete learning
  algorithm from scratch.
- A Track A version of the e-prop idea would compare e-prop with BPTT under one
  temporal challenge such as non-stationarity, task switching, online learning,
  or controlled noise. The earlier trajectory-identification question can be
  retained as an optional analysis rather than the project's primary identity.

## Advisor Opinion — Provisional

Prefer **Track A**, scoped as an existing biologically constrained rule under
one new stress condition. The leading concrete option is:

> Compare e-prop with BPTT on one recurrent temporal task under a controlled
> non-stationary shift or task switch, measuring adaptation, retention, and one
> update-quality diagnostic.

Reasons:

- it matches the group's two-week need for a tangible experimental result;
- it fits an AI/CV engineering workflow while retaining a real NeuroAI credit-
  assignment question;
- both a positive trade-off and a clear failure boundary are presentable;
- it produces controlled learning signatures that could support a later Track
  B identification project;
- Track B currently carries greater identifiability and confounding risk for
  the available time.

This is an advisor recommendation for W1D1 discussion, not a group decision.

## W1D1 Group Pitch — Draft

> At this stage, I lean toward Track A. More specifically, I would like to
> Given our two-week time frame, I would like to benchmark one or two recently
> proposed biologically plausible learning algorithms, such as e-prop, against
> BPTT and stress-test them under a carefully chosen challenging condition. By
> identifying where and why these methods succeed or fail relative to the BPTT
> baseline, we could generate
> concrete hypotheses for designing better learning rules and lay the
> groundwork for a longer-term research project through the Impact Scholars
> Program.

Scope note: “one or two recent algorithms” is intentional. “The latest advances
in the field” would imply a survey-scale benchmark beyond the two-week project.

## Exit Condition

W1D1 is complete when the group has reduced the four directions to at most two
and recorded why the others were deferred. A final research question is not
required today.

## Next Course-Day Action

On W1D2, test the lead and backup against environment setup, public data/code,
expected runtime, and the W1D4 proposal requirements. Do not begin the full
experiment matrix before this feasibility pass.
