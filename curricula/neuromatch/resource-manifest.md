# Neuromatch Resource Manifest

Purpose: route every non-note resource mentioned by the prep-phase course pages into a dedicated directory.

This is a routing manifest, not a content mirror. It records where companion materials should live when downloaded, captured, or summarized locally.

## Resource Types

| Resource type | Dedicated directory | Policy |
|---|---|---|
| Rendered student notebook pages / downloaded `.ipynb` notebooks | [`resources/notebooks/`](resources/notebooks/) | Save notebooks by course and day-topic. Keep source URL with the file. |
| Slides / slide decks | [`resources/slides/`](resources/slides/) | Save decks or pointer files by course and day-topic. |
| Datasets and data-loader sources | [`resources/datasets/`](resources/datasets/) | Prefer metadata and source links. Do not commit large raw data by default. |
| Embedded videos / video series | [`resources/videos/`](resources/videos/) | Keep link registries and viewing notes, not video mirrors. |
| Figures, screenshots, generated diagrams, supporting images | [`resources/figures/`](resources/figures/) | Keep only figures that support durable notes or experiments. Record provenance. |
| Raw HTML / markdown / parser snapshots | [`resources/raw-pages/`](resources/raw-pages/) | Use only when reproducible extraction needs local snapshots. |

## Prep-Phase Routing

| Course block | Resource mentions in local indexes | Dedicated local destination |
|---|---|---|
| CompNeuro W0D0 Neuro Video Series | Video-only source pages | `resources/videos/compneuro/w0d0-neuro-video-series/` |
| CompNeuro W1D1 Model Types | Rendered student notebook pages; Steinmetz spiking dataset mentions | `resources/notebooks/compneuro/w1d1-model-types/`; `resources/datasets/compneuro/steinmetz/` |
| CompNeuro W1D2 Model Fitting | Rendered student notebook pages; generated/resampled tutorial datasets | `resources/notebooks/compneuro/w1d2-model-fitting/`; `resources/datasets/compneuro/w1d2-model-fitting/` |
| CompNeuro W1D3 GLM | Rendered student notebook pages; retinal ganglion cell dataset with redistribution warning | `resources/notebooks/compneuro/w1d3-glm/`; `resources/datasets/compneuro/retinal-ganglion-cell/` |
| CompNeuro W1D4 Dimensionality Reduction | Rendered student notebook pages; MNIST examples | `resources/notebooks/compneuro/w1d4-dimensionality-reduction/`; `resources/datasets/shared/mnist/` |
| CompNeuro W2D3 Linear Systems | Rendered student notebook pages; synthetic process simulations | `resources/notebooks/compneuro/w2d3-linear-systems/`; `resources/datasets/compneuro/w2d3-synthetic-processes/` |
| CompNeuro W2D4 Biological Neuron Models | Rendered student notebook pages; simulated LIF and synapse data | `resources/notebooks/compneuro/w2d4-biological-neuron-models/`; `resources/datasets/compneuro/w2d4-simulated-neuron-models/` |
| CompNeuro W2D5 Dynamical Systems | Rendered student notebook pages; simulated Wilson-Cowan trajectories | `resources/notebooks/compneuro/w2d5-dynamical-systems/`; `resources/datasets/compneuro/w2d5-simulated-dynamics/` |
| CompNeuro W3D2 Bayesian Decisions | Rendered student notebook pages; generated hidden-state examples | `resources/notebooks/compneuro/w3d2-bayesian-decisions/`; `resources/datasets/compneuro/w3d2-generated-hidden-state/` |
| CompNeuro W3D3 Hidden Dynamics | Rendered student notebook pages; HMM, Kalman, eye-tracking, and spiking examples | `resources/notebooks/compneuro/w3d3-hidden-dynamics/`; `resources/datasets/compneuro/w3d3-hidden-dynamics/` |
| CompNeuro W3D4 Reinforcement Learning | Rendered student notebook pages; bandit/grid-world examples | `resources/notebooks/compneuro/w3d4-reinforcement-learning/`; `resources/datasets/compneuro/w3d4-rl-simulations/` |
| CompNeuro W3D5 Network Causality | Rendered student notebook pages; simulated neural systems | `resources/notebooks/compneuro/w3d5-network-causality/`; `resources/datasets/compneuro/w3d5-simulated-neural-systems/` |
| Deep Learning PyTorch / optimization / regularization bridge | Rendered student notebook pages; toy and course datasets | `resources/notebooks/deeplearning/w1-w2-basics-optimization-regularization/`; `resources/datasets/deeplearning/course-toy-data/` |
| Deep Learning CNN / modern ConvNet bridge | Rendered student notebook pages; EMNIST, Fashion-MNIST, Imagenette, face-recognition data mentions | `resources/notebooks/deeplearning/w2d2-w2d3-convnets/`; `resources/datasets/deeplearning/vision-datasets/` |
| Deep Learning self-supervised bridge | Rendered student notebook pages; dSprites dataset; supporting discussion images | `resources/notebooks/deeplearning/w3d3-self-supervised-learning/`; `resources/datasets/deeplearning/dsprites/`; `resources/figures/deeplearning/w3d3-self-supervised-learning/` |
| Deep Learning sequence / transformer bridge | Rendered student notebook pages; Yelp and NLP datasets; embeddings | `resources/notebooks/deeplearning/w2d5-w3d1-sequence-transformers/`; `resources/datasets/deeplearning/nlp/` |
| Deep Learning RL / Deep RL bridge | Rendered student notebook pages; game environments; one indexed tutorial mentions downloadable slides | `resources/notebooks/deeplearning/w3d4-w3d5-rl/`; `resources/datasets/deeplearning/rl-environments/`; `resources/slides/deeplearning/w3d5-mcts/` |
| NeuroAI prerequisites and future NeuroAI pages | Intro pages mention videos and slides; tutorial pages mention datasets, slides, RSA datasets, CIFAR-10, generated data, and video creation | `resources/slides/neuroai/`; `resources/videos/neuroai/`; `resources/notebooks/neuroai/`; `resources/datasets/neuroai/`; `resources/figures/neuroai/` |

## Minimal Pointer File Template

Use this when a resource is external, large, licensed, or not worth copying:

```markdown
# <resource-name>

- Source page:
- External resource URL:
- Resource type:
- Course block:
- Local use:
- License or access notes:
- Download status:
```
