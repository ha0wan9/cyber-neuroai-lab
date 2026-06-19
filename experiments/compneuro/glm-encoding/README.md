# GLM Encoding

## Core Question

Can a simple generalized linear model recover how a synthetic stimulus variable drives spike probability?

## Minimal Setup

- Start with synthetic data generated in a small script under `src/`.
- Prefer standard library plus a lightweight numeric stack only if needed.
- Keep notebooks optional and small.

## Variables

- Stimulus feature values.
- Encoding weights.
- Bias term or baseline firing rate.
- Link function.
- Number of samples or time bins.
- Noise level.

## Mechanism

A stimulus is transformed through a linear filter and link function to produce a spike probability or count rate. Fitting should estimate parameters that explain the generated responses.

## Expected Result

For clean synthetic data, estimated parameters should approximately match the known generating parameters. This expectation must be verified by code before being treated as a result.

## Verification Command Placeholder

```bash
python src/run_glm_encoding.py
```

## Interpretation

Use this experiment to distinguish an encoding model as an explanatory mapping from stimulus variables to neural responses, not as a mechanistic circuit model.

## Failure Modes

- Confusing generated parameters with fitted parameters.
- Too few samples for stable estimates.
- Poorly scaled features causing unstable fitting.
- Reporting fit quality without a held-out or sanity-check comparison.

## Follow-Up Questions

- How does noise level affect parameter recovery?
- What changes with multiple correlated stimulus features?
- How should model quality be compared against a baseline firing-rate model?
