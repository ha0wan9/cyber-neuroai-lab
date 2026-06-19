# Experiment Plan

## Aim

Build a minimal executable leaky integrate-and-fire neuron simulation for learning the relationship between input drive and spike timing.

## Steps

1. Define a small parameter dictionary with voltage, current, and timing values.
2. Implement Euler integration in `src/run_lif_neuron.py`.
3. Record voltage trace and spike times.
4. Save a small text, CSV, or plot artifact under `outputs/`.
5. Add a short note explaining whether the output matches the expected qualitative trend.

## Constraints

- No heavy dependencies.
- No large notebooks.
- No claims about biological realism beyond the chosen toy model.

## Verification

Run the command documented in `README.md` after the script exists.
