# Bayesian Hidden State

## Core Question

How can an observer infer a hidden binary or categorical state from noisy observations over time?

## Minimal Setup

- Use a tiny hidden-state model with synthetic observations.
- Implement the first version as a script under `src/`.
- Save posterior traces or summary tables under `outputs/`.

## Variables

- Hidden states.
- State transition probability.
- Observation likelihood.
- Observation noise.
- Prior belief.
- Sequence length.

## Mechanism

The observer updates beliefs by combining prior state probabilities with new evidence from observations. Sequential updates should accumulate information while respecting uncertainty.

## Expected Result

When observations are informative, posterior probability should track the true hidden state more accurately than the prior alone. This is a hypothesis for the scaffold, not a completed result.

## Verification Command Placeholder

```bash
python src/run_bayesian_hidden_state.py
```

## Interpretation

Use this experiment to connect probabilistic inference with latent cognitive or neural-state tracking. Keep the distinction clear between toy hidden states and real latent variables.

## Failure Modes

- Likelihoods are not normalized.
- Priors accidentally dominate all evidence.
- True state generation and inference model are conflated.
- Numerical underflow appears in longer sequences.

## Follow-Up Questions

- How does transition probability affect belief inertia?
- What happens when the observer has the wrong likelihood model?
- How can the same setup be extended to continuous hidden states?
