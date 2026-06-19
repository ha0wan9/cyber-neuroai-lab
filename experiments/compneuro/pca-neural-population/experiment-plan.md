# Experiment Plan

## Aim

Build a small synthetic population-activity experiment that demonstrates dimensionality reduction and variance explained.

## Steps

1. Generate low-dimensional latent activity.
2. Mix latent factors into a larger set of synthetic neurons.
3. Add controlled noise.
4. Center the activity matrix.
5. Compute principal components with a simple implementation or lightweight numeric helper.
6. Save variance-explained values and a compact diagnostic artifact under `outputs/`.

## Constraints

- Keep matrices small.
- Do not add large datasets.
- Document centering and scaling choices.

## Verification

Run the command documented in `README.md` after the script exists.
