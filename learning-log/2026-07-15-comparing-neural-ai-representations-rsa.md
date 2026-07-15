# Learning Log — Comparing Neural and AI Representations (RSA)

Date: 2026-07-15
Type: Course notes (live tutorial/lecture)
Source: Fathom recording — "Impromptu Zoom Meeting" (https://fathom.video/calls/748210137)
Status: raw

## Context

Tutorial-style lecture introducing **geometric methods for comparing neural and AI
representations**. Central premise: to compare very different systems (e.g. mouse
visual cortex vs. a CNN), compare *representations*, not architectures.

## Core Question

How can we make valid, quantitative comparisons between systems as different as a
biological brain and an artificial network, when their internals are not directly
comparable?

## One-Sentence Summary

Represent each system's response to a set of stimuli as a cloud of points in a
high-dimensional space, then compare the *shape* (geometry) of those clouds across
systems using Representational Similarity Analysis (RSA).

## Key Concepts

### 1. Why direct comparisons fail
- **Architectures** — different architectures can implement identical functions, so
  architecture alone tells you little.
- **Connectivity** — a node-to-node connection means different things in different
  networks; connectivity isn't comparable across systems.
- **Weights** — only meaningfully comparable between nearly identical networks.
- **Output-only comparison** — valid but limited; discards all information about
  internal processing.

### 2. Representational geometry (the reframing)
- Treat a system's response to a stimulus as a **point in high-dimensional space**.
- The **shape of the resulting point cloud** — pairwise distances, angles, curvature —
  *is* the representation.
- This shape can be compared across systems even when their dimensions/units differ.

### 3. Representational Similarity Analysis (RSA) — the primary method
1. **Compute RDMs** (Representational Dissimilarity Matrices): for each system, build
   a matrix whose entries are the dissimilarity between the responses to each pair of
   stimuli.
2. **Compare RDMs**: use a symmetric comparison function (e.g. Pearson or Spearman
   correlation) to measure how similar two systems' RDMs are.
- Key move: the RDM abstracts away from the raw feature space, so two systems with
  incomparable internal spaces become comparable at the level of dissimilarity structure.

### 4. Alternative: linear encoding models
- Fit a **linear map** from a model's features to measured brain responses.
- Contrast with RSA: encoding models predict responses directly; RSA compares geometry.

### 5. Quantifying uncertainty with bootstrapping
- **Purpose**: produce error bars and run statistical tests, accounting for "nuisance
  variation" from:
  - **Stimuli** — different stimulus sets give different results.
  - **Subjects** — individual differences between brains.
  - **AI training** — random initialization, learning rate, and other training choices.
- **Single-factor bootstrap** (resample stimuli only, or subjects only) works well.
- **Naive two-factor bootstrap** (resample *both* subjects and stimuli) severely
  **overestimates variance** — reportedly ~1.4× on the standard deviation, i.e. ~2× on
  the variance.
  - **Cause**: the noise variance gets **triple-counted** (subject noise, stimulus
    noise, and their interaction).
- **Correction**: a formula derived from variance decomposition (subjects + stimuli +
  interaction) recovers the true variance, restoring the two-factor bootstrap to the
  reliability of the single-factor case (and restoring statistical power).

## Tutorial Logistics (from the session)
- **Format**: five self-assignable breakout rooms — Tutorial 1A, 1B, 2A, 2B, 3 —
  so participants can move at their own pace (start with 1A or 1B).
- **Data**: part of the NaturalC / "Natural Scenes"-style dataset (7 Tesla fMRI).
  *(Dataset name heard as "NaturalC" — verify exact name.)*
- **Tool**: a provided **RSA toolbox** handles the resampling and the variance
  correction automatically.

## Connection to NeuroAI
- RSA is a core tool for **brain–model alignment**: scoring how well an AI model's
  internal representations match neural data without needing matched architectures.
- Fits the repo's working frame of separating *strict equivalence* from *structural
  similarity* — RSA measures structural (geometric) similarity, not equivalence.

## Open Questions / To Verify
- Exact name and citation of the fMRI dataset (heard as "NaturalC" — likely the
  Natural Scenes Dataset?).
- Which RDM distance to use (correlation distance, Euclidean, Mahalanobis/crossnobis)
  and when each is appropriate.
- Precise statement of the variance-correction formula from the variance decomposition.
- When to prefer RSA vs. linear encoding models for a given comparison.
- Name of the specific RSA toolbox used in the tutorial (rsatoolbox?).

## Possible Outputs
- [ ] Concept note: `notes/` entry on representational geometry + RDMs
- [ ] Concept note: bootstrapping nuisance variation + two-factor variance correction
- [ ] Code experiment: compute an RDM for a small CNN and correlate two RDMs (RSA)
- [ ] Paper connection: original RSA reference (Kriegeskorte et al.) + Natural Scenes Dataset
- [ ] Research question added to backlog on brain–model alignment metrics
