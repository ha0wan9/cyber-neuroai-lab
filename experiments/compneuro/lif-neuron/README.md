# Leaky Integrate-and-Fire Neuron

## Core Question

How do membrane leak, input current, threshold, and reset rules shape spike timing in a minimal neuron model?

## Minimal Setup

- Keep the first implementation to a single script under `src/`.
- Use Python standard library first; add only a small numeric dependency if the implementation clearly needs it.
- Write outputs such as plots or CSV summaries to `outputs/`.

## Variables

- Membrane time constant.
- Resting potential.
- Reset potential.
- Spike threshold.
- Constant or time-varying input current.
- Simulation time step and duration.

## Mechanism

The membrane voltage integrates input current while decaying back toward rest. A spike is recorded when voltage crosses threshold, then voltage is reset.

## Expected Result

Increasing input current should reduce inter-spike interval after the firing threshold is reached. This is an expected qualitative behavior, not an observed result yet.

## Verification Command Placeholder

```bash
python src/run_lif_neuron.py
```

## Interpretation

Use the simulation to connect differential-equation dynamics with observable spike trains. Treat firing-rate changes as model behavior, not biological evidence by themselves.

## Failure Modes

- Time step is too large and creates numerical artifacts.
- Units are mixed or undocumented.
- Reset or threshold logic creates off-by-one spike timing errors.
- Parameters are chosen so the neuron never spikes or spikes every step.

## Follow-Up Questions

- How does refractory period change the firing-rate curve?
- What changes when input current is noisy?
- How sensitive are results to the integration time step?
