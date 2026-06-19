# PCA Neural Population

## Core Question

How can low-dimensional structure be recovered from a synthetic population of correlated neural activity?

## Minimal Setup

- Generate synthetic population activity in a script under `src/`.
- Keep data small enough to inspect directly.
- Save only compact outputs under `outputs/`.

## Variables

- Number of neurons.
- Number of time points or trials.
- Latent dimensionality.
- Noise level.
- Strength of shared factors.
- Centering and scaling choices.

## Mechanism

Synthetic neural activity is generated from a small number of latent factors plus noise. PCA should identify directions that explain shared variance across neurons.

## Expected Result

When shared latent factors dominate noise, the first few principal components should explain most variance. This is an expectation to test, not a completed finding.

## Verification Command Placeholder

```bash
python src/run_pca_neural_population.py
```

## Interpretation

Use PCA as a descriptive tool for population structure. Avoid interpreting components as biological variables unless an additional analysis supports that mapping.

## Failure Modes

- Forgetting to center data before PCA.
- Using too few samples relative to neuron count.
- Treating arbitrary component sign as meaningful.
- Over-interpreting noisy components.

## Follow-Up Questions

- How does variance explained change with noise?
- Can latent trajectories be visualized over time?
- How does PCA compare with a supervised decoder on the same synthetic data?
