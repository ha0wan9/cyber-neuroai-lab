# NeuroAI Prerequisite — Domain Knowledge Map

A concept-first map of the **knowledge domain** underlying NeuroAI: the ideas, facts, and
definitions you must hold, organized by their intellectual structure — **not** by any course,
day, or tutorial. Use it to build the skeleton fast and to place every detail you later read.

- How to read: the tree is the domain; each leaf carries a one-line **fact or definition**.
- Bolded terms are the load-bearing vocabulary; if you can restate each in your own words, you own the skeleton.
- All statements are standard field-level definitions for orientation, not citation. Verify when accuracy matters.

---

## The domain in one sentence

NeuroAI compares **biological** and **artificial** neural systems by asking, for each: how does it
**represent** the world, **transform** those representations, **learn** them from experience, and
**evolve** them in time — and how do we **measure, model, and causally explain** any of it.

Six pillars. Everything else is detail hanging off one of them.

```text
NEUROAI PREREQUISITE DOMAIN
├── A. Neural substrate ......... what a brain is made of & how we observe it
├── B. Models & fitting ........ how any system's behavior is captured mathematically
├── C. Representation & geometry  the internal coordinate system (the core of NeuroAI)
├── D. Dynamics ................ how state evolves in time
├── E. Learning & adaptation ... how the parameters get set by experience
└── F. Causality ............... telling mechanism apart from mere correlation
```

---

## A. Neural substrate — the biological hardware

```text
A. NEURAL SUBSTRATE
├── A1. The neuron & signaling
│   ├── Membrane potential — voltage across the cell membrane; the neuron's state variable
│   ├── Action potential (spike) — all-or-none voltage pulse; the unit of neural communication
│   ├── Synapse — junction where one neuron influences another (chemical or electrical)
│   ├── Neurotransmitters — chemical messengers; drive excitation or inhibition
│   └── Excitation / Inhibition (E/I) — push toward vs away from firing; their balance shapes computation
├── A2. The neural code — how information is carried
│   ├── Rate code — information in firing rate (spikes per second)
│   ├── Temporal code — information in precise spike timing
│   ├── Population code — information distributed across many neurons jointly
│   ├── Tuning curve — a neuron's average response as a function of a stimulus feature
│   └── Stimulus representation — how an external variable maps onto neural activity
└── A3. How we observe the brain — measurement & behavior
    ├── Single-cell: spiking (electrophysiology), calcium imaging — cell-level precision
    ├── Population/field: LFP, EEG, MEG — aggregate signals; timing-rich, spatially blurry
    ├── Hemodynamic: fMRI — mm spatial, but slow (seconds) proxy via blood oxygen
    ├── KEY FACT: every method trades SPATIAL against TEMPORAL resolution — no tool has both
    └── Behavior / psychophysics — measuring perception & action as the readout of computation
```

---

## B. Models & fitting — capturing behavior mathematically

```text
B. MODELS & FITTING
├── B1. What is a model
│   ├── WHAT / HOW / WHY taxonomy — describe a phenomenon / propose a mechanism / argue it is optimal
│   ├── Encoding model — predict neural response FROM stimulus
│   └── Decoding model — reconstruct stimulus FROM neural response
├── B2. Fitting a model to data
│   ├── Loss / cost function — scalar measuring model error; fitting = minimizing it
│   ├── Least squares (MSE) — minimize squared error; = MLE under Gaussian noise
│   ├── Maximum likelihood (MLE) — maximize probability the model assigns to the data
│   └── Gradient descent + autograd — step parameters downhill on the loss; the universal fitting engine
├── B3. Generalization machinery — fitting that transfers
│   ├── Overfitting — modeling noise, not signal; fits training data, fails new data
│   ├── BIAS–VARIANCE trade-off — too simple underfits (bias); too complex overfits (variance)
│   ├── Cross-validation — hold out data to estimate generalization, not memorization
│   ├── Regularization (L1/L2) — penalize complexity; L1 also induces sparsity
│   ├── Bootstrapping — resample data to estimate uncertainty (confidence intervals)
│   └── Double descent — with heavy overparameterization, test error can fall again past the interpolation point
├── B4. Generalized Linear Models (GLM)
│   └── linear predictor + link function + noise family — the standard encoding-model tool
└── B5. Bayesian inference & decisions
    ├── posterior ∝ likelihood × prior — update belief with evidence
    └── Decision under uncertainty — choose the action minimizing expected loss given the posterior
```

---

## C. Representation & geometry — the core of NeuroAI

```text
C. REPRESENTATION & GEOMETRY
├── C1. Data as geometry
│   ├── Data point = vector in feature space; a population's activity = a point per stimulus
│   └── Variance / covariance — spread and co-variation; the raw material of structure
├── C2. Dimensionality reduction
│   ├── PCA — rotate onto axes of maximum variance (eigenvectors of the covariance matrix)
│   ├── Low-rank reconstruction — keep few components, approximate the data
│   └── Nonlinear DR (t-SNE / manifold methods) — uncover curved low-dim structure
├── C3. Representational geometry — the comparison language
│   ├── RDM (representational dissimilarity matrix) — pairwise distances between responses to stimuli
│   ├── RSA (representational similarity analysis) — compare RDMs across models, layers, brains
│   └── KEY IDEA: a computation TRANSFORMS geometry — removes, preserves, or reformats information
├── C4. Deep-network representations
│   ├── MLP — stacked linear layers + nonlinearities; the basic learned representation
│   ├── CNN — convolution builds a spatial feature hierarchy (edges → parts → objects)
│   ├── Transfer / self-supervised learning — reuse or learn representations without task labels
│   └── Attention / Transformer — weight inputs by learned relevance (query–key–value)
└── BRIDGE: comparing biological vs artificial representations via shared geometry (RSA) is the
    central move of NeuroAI.
```

---

## D. Dynamics — how state evolves in time

```text
D. DYNAMICS
├── D1. Linear dynamical systems (LDS)
│   ├── State update x(t+1) = A·x(t) — a matrix drives the evolution
│   └── EIGENVALUES of A decide the regime: decay, growth, or oscillation (stability)
├── D2. Stochastic dynamics
│   ├── Markov process — next state depends only on current state, not full history
│   └── Autoregressive model — future = weighted past + noise
├── D3. Single-neuron dynamics
│   ├── Leaky Integrate-and-Fire (LIF) — voltage integrates input, leaks to rest, fires at threshold
│   └── Synaptic dynamics — static vs short-term-plastic (facilitating/depressing) transmission
├── D4. Population dynamics
│   ├── Neural rate models — describe average population activity, not individual spikes
│   ├── Wilson–Cowan — coupled excitatory/inhibitory populations; oscillations & fixed points
│   └── Attractor / fixed point — stable state a system settles into (memory, decision)
└── D5. Latent-state inference over time
    ├── SPRT — accumulate evidence, decide when a threshold is crossed
    ├── HMM (hidden Markov model) — observations emitted by an unseen Markov state
    └── Kalman filter — optimal recursive estimate of a hidden linear-Gaussian state (predict → correct)
```

---

## E. Learning & adaptation — setting the parameters from experience

```text
E. LEARNING & ADAPTATION
├── E1. Learning paradigms
│   ├── Supervised — learn from labeled input→target pairs
│   ├── Unsupervised / self-supervised — learn structure without external labels
│   └── Reinforcement — learn from reward signals via interaction
├── E2. Credit assignment — who to blame for the error
│   ├── Backpropagation — exact gradient of the loss w.r.t. every weight; powers deep learning
│   ├── Biological plausibility problem — backprop needs "weight transport" the brain likely lacks
│   └── Local / Hebbian rules & STDP — "fire together, wire together"; timing-based synaptic change
├── E3. Reinforcement learning (RL)
│   ├── Reward / value / policy — the objective, the expected return, the action rule
│   ├── TD learning (temporal difference) — learn value from prediction error (links to dopamine)
│   ├── Q-learning — model-free learning of action values
│   ├── Multi-armed bandit — explore/exploit with no state transitions
│   └── Model-based RL — learn a world model and plan, vs model-free caching of values
└── E4. Adaptation over time
    ├── Generalization — good behavior on data never trained on (the shared north star)
    ├── Inductive bias — priors/architecture (convolution, attention, regularization) that decide WHAT generalizes
    └── Catastrophic forgetting / continual & meta-learning — retaining old skills while learning new
```

---

## F. Causality — mechanism vs correlation

```text
F. CAUSALITY
├── Correlation ≠ causation — co-variation alone cannot establish a mechanism
├── Intervention / perturbation — actively changing a variable is the gold standard for causal claims
├── Simultaneous regression — control for confounds when isolating an effect
└── Instrumental variable — a handle that affects the cause but not the outcome directly, to recover
    causal effect without direct intervention
```

---

## Cross-cutting threads (recognize these and you navigate fast)

The domain is small once you see that the same ideas recur across all six pillars:

- **Generalization** — the north star everywhere: fitting (B), representation (C), dynamics (D), learning (E).
- **Geometry of representation** — PCA, RSA, and transformer features all speak the same language (C).
- **Optimization by a loss + gradient** — the shared engine of regression, GLMs, deep nets, and deep RL (B, C, E).
- **Uncertainty & noise** — bootstrapping, MLE, Bayes, Kalman are all noise-reasoning tools (B, D).
- **Biological vs artificial** — every artificial mechanism (backprop, attention) is paired against a brain analogue (E, A, C).
- **Inductive bias** — architectural/prior choices that decide what a system can and cannot learn (C, E).
- **Correlation vs causation** — shadows every "the model matches the brain" claim (F over all).

---

## Self-check — do you own the skeleton?

Cover the tree and try to answer:

1. Name the six pillars and the one question each answers.
2. Why does no brain-measurement method give both high spatial and high temporal resolution?
3. State the bias–variance trade-off and how cross-validation addresses it.
4. What does an RDM encode, and what does RSA let you compare?
5. What do the eigenvalues of an LDS transition matrix tell you?
6. Contrast backprop with a Hebbian/STDP rule on biological plausibility.
7. Give one reason correlation between two neurons does not prove one drives the other.

Terms you cannot answer are your real study list — go read the detail for those, and only those.
