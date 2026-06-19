# Experiment Plan

## Aim

Create a minimal Wilson-Cowan simulation to explore qualitative excitatory-inhibitory population dynamics.

## Steps

1. Define the two coupled activity equations.
2. Choose a simple sigmoid or bounded activation function.
3. Implement Euler integration in `src/run_wilson_cowan.py`.
4. Run a small set of parameter regimes.
5. Save final activity values and a short trajectory summary under `outputs/`.

## Constraints

- Keep parameter sweeps small.
- Avoid large plotting or animation dependencies.
- Label all parameters clearly.

## Verification

Run the command documented in `README.md` after the script exists.
