# Representation Similarity Toy

## Core Question

How can representational similarity analysis compare two toy systems that encode the same set of stimuli differently?

## Minimal Setup

- Generate small synthetic representation matrices in a script under `src/`.
- Avoid downloading external models or datasets.
- Keep notebooks optional and tiny.

## Variables

- Number of stimuli.
- Representation dimensionality.
- Feature noise.
- Similarity metric.
- Distance metric.
- Alignment or transformation between representation spaces.

## Mechanism

Each system represents stimuli as vectors. Pairwise similarities produce representational similarity matrices that can be compared across systems.

## Expected Result

Representations generated from a shared latent structure should have more similar similarity matrices than unrelated random representations. This is the expected check, not a measured result yet.

## Verification Command Placeholder

```bash
python src/run_representation_similarity_toy.py
```

## Interpretation

Use this toy experiment to understand what RSA compares and what it ignores. Similarity between representational geometries does not by itself prove shared mechanisms.

## Failure Modes

- Comparing raw activations instead of pairwise geometry.
- Letting scale dominate the similarity metric.
- Using too few stimuli for stable comparison.
- Treating toy alignment as model-brain evidence.

## Follow-Up Questions

- How sensitive is RSA to the chosen similarity metric?
- What happens when one representation is a rotated version of another?
- How does RSA differ from linear decoding or probing?
