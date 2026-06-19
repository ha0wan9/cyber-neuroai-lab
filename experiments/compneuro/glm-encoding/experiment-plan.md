# Experiment Plan

## Aim

Create a minimal synthetic encoding-model workflow that generates stimulus-response data and fits or checks a simple GLM-like relationship.

## Steps

1. Generate a one-dimensional synthetic stimulus.
2. Choose known encoding parameters and a link function.
3. Sample spike counts or binary spikes from the generated rate.
4. Implement a minimal fitting or grid-search routine.
5. Compare recovered parameters with the generating parameters.
6. Save a compact output summary under `outputs/`.

## Constraints

- Keep the fitting method understandable.
- Avoid adding a machine-learning framework.
- Do not treat synthetic parameter recovery as evidence about real neural data.

## Verification

Run the command documented in `README.md` after the script exists.
