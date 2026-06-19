# Wilson-Cowan

## Core Question

How do coupled excitatory and inhibitory population dynamics produce stable activity, oscillation, or runaway behavior in a toy circuit?

## Minimal Setup

- Implement the dynamical system in a small script under `src/`.
- Use simple parameter sweeps before adding visualization.
- Keep outputs compact and reproducible.

## Variables

- Excitatory self-coupling.
- Inhibitory self-coupling.
- Excitatory-to-inhibitory coupling.
- Inhibitory-to-excitatory coupling.
- External input.
- Time constants.
- Activation-function gain and threshold.

## Mechanism

Excitatory and inhibitory activity variables evolve through coupled differential equations. Their interactions determine whether activity settles, oscillates, or diverges under a parameter regime.

## Expected Result

Balanced excitation and inhibition should permit stable trajectories for some parameter settings, while stronger feedback may shift the dynamics. This must be verified by simulation.

## Verification Command Placeholder

```bash
python src/run_wilson_cowan.py
```

## Interpretation

Use the model to reason about qualitative population dynamics. Do not identify toy regimes with real brain states without additional evidence.

## Failure Modes

- Parameter choices create saturation everywhere.
- Integration step is too coarse.
- Activation function is undocumented.
- Stability claims are made from too short a simulation.

## Follow-Up Questions

- Which parameters produce oscillatory trajectories?
- How do nullclines clarify the phase portrait?
- What changes when the external input is pulsed rather than constant?
