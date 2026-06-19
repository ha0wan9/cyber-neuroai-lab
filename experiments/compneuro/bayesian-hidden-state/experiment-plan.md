# Experiment Plan

## Aim

Build a small sequential Bayesian inference demo for hidden-state tracking with noisy observations.

## Steps

1. Define two or more hidden states.
2. Generate a short hidden-state sequence.
3. Generate observations from state-dependent likelihoods.
4. Implement recursive belief updates.
5. Compare posterior beliefs with the generated hidden states.
6. Save a compact posterior trace or summary under `outputs/`.

## Constraints

- Keep the model discrete for the first version.
- Avoid probabilistic programming frameworks.
- Separate data generation from inference code.

## Verification

Run the command documented in `README.md` after the script exists.
