# Brain Learning, Backpropagation, and Biologically Motivated Constraints

Date: 2026-07-14  
Source: focused synthesis of representative primary papers and authoritative reviews  
Status: structured draft; representative evidence, not a completed systematic review

## 1. Core Question

How is learning in biological brains similar to and different from
backpropagation, and which biological ideas can be translated into useful
regularizers or other inductive biases for artificial neural networks?

## 2. One-Sentence Summary

Brains and backpropagation both solve forms of credit assignment, but
backpropagation is an exact, global gradient-computation procedure whereas the
brain appears to combine many local, recurrent, modulatory, homeostatic, and
multi-timescale mechanisms; some biological principles translate cleanly into
regularizers, while others require changing the objective, architecture,
internal dynamics, or update rule.

## 3. First Clarification: There Is No Single Known “Brain Learning Algorithm”

The phrase **the brain's learning algorithm** is too singular. Evidence instead
supports interacting mechanisms at different scales: correlation- and
timing-dependent synaptic plasticity, neuromodulatory gating, eligibility
traces, homeostatic regulation, structural plasticity, replay and
consolidation. Different circuits and behavioral regimes need not use the same
combination.

Backpropagation is narrower. It is an efficient application of the chain rule
that computes derivatives of a chosen scalar loss with respect to parameters.
An optimizer such as SGD or Adam then uses those derivatives. Backpropagation
is therefore not, by itself, a task objective, optimizer, data curriculum, or
complete learning system. The classical neural-network formulation was
popularized by [Rumelhart, Hinton, and Williams
(1986)](https://www.nature.com/articles/323533a0).

## 4. Mechanism-Level Comparison

For a feedforward network,

\[
h_l=f_l(W_lh_{l-1}), \qquad
\delta_l=(W_{l+1}^{\mathsf T}\delta_{l+1})\odot f_l'(W_lh_{l-1}),
\]

and the gradient at a synapse has the outer-product form

\[
\frac{\partial \mathcal L}{\partial W_l}=\delta_lh_{l-1}^{\mathsf T}.
\]

This equation contains an important bridge to biology: **once a suitable
postsynaptic teaching signal \(\delta_l\) exists**, the final update is local in
the presynaptic activity and that signal. Many biological models use a related
three-factor form,

\[
\Delta w_{ij}\propto e_{ij}(\text{pre},\text{post},\text{local state})\,m_j,
\]

where \(e_{ij}\) is a local eligibility trace and \(m_j\) is a delayed reward,
novelty, error, or other modulatory signal. Experiments support temporally
specific dopaminergic gating of previously eligible synapses, but this does not
imply that dopamine carries the exact backpropagated derivative in every brain
circuit ([Yagishita et al.,
2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4225776/)).

| Dimension | Canonical backpropagation | Biological learning |
|---|---|---|
| Primary mathematical role | exact gradient of an explicit scalar objective | multiple local and system-level adaptation processes; the optimized quantity is often implicit or contested |
| Spatial credit | chain rule sends parameter-specific error through the computation graph | local plasticity must be coordinated by feedback, dendrites, modulators, circuit dynamics, or other signals |
| Temporal credit | BPTT unfolds a recurrent system and propagates derivatives backward through stored history | eligibility traces and slowly changing cellular states can preserve local credit until a later signal arrives |
| Local information | gradient at a weight depends indirectly on downstream weights and states | synaptic change is physically local, although local plasticity can be gated by nonlocal feedback or neuromodulation |
| Feedback weights | exact reverse-mode differentiation uses transposed Jacobians/forward weights | reciprocal pathways exist, but precise, continuously matched weight symmetry is not established |
| Timing | commonly separated forward and backward computational passes | inference, action, feedback, and plasticity overlap in continuous recurrent dynamics |
| Neuron and synapse model | usually differentiable rate-like units and stable numerical parameters | spikes, dendritic compartments, biochemical state, stochastic transmission, multiple plasticity timescales |
| Learning regime | often minibatch, approximately IID, offline, with many replayed examples | online, embodied, nonstationary, active, and strongly shaped by development and memory systems |
| Stability | normalization and regularization are engineered into the training pipeline | Hebbian change is counteracted by homeostasis, inhibition, consolidation, metaplasticity, and structural constraints |
| Resource constraint | compute and memory cost are engineering objectives unless explicitly penalized | wiring, firing, signaling, and plasticity have unavoidable energetic and anatomical costs |

## 5. Similarities Without Claiming Equivalence

1. **Both face credit assignment.** A useful internal connection must be
   changed according to how it contributed to a later outcome.
2. **Both can be error driven.** Error need not mean a class label; it can be a
   reward-prediction error, sensory-prediction error, target mismatch, or local
   dendritic prediction error.
3. **Both can produce distributed task-adapted representations.** Similar
   behavior and representations do not prove identical mechanisms.
4. **Exact gradients are not always necessary.** Feedback alignment showed
   that fixed random feedback can transmit useful approximate teaching signals
   without exact weight transport ([Lillicrap et al.,
   2016](https://www.nature.com/articles/ncomms13276)). Dendritic,
   predictive-coding, and equilibrium models provide other mathematical ways
   to approximate or recover gradients using local computations
   ([Sacramento et al.,
   2018](https://proceedings.neurips.cc/paper/2018/hash/1dc3a89d0d440ba31729b0ba74b93a33-Abstract.html);
   [Whittington & Bogacz,
   2017](https://direct.mit.edu/neco/article/29/5/1229/8261/An-Approximation-of-the-Error-Backpropagation);
   [Scellier & Bengio,
   2017](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2017.00024/full)).

These results are **existence proofs in models**, not evidence that one of the
models is the brain's universal learning algorithm. The field still lacks a
consensus mapping from neural hardware to a complete gradient-like learning
procedure ([Lillicrap et al.,
2020](https://www.nature.com/articles/s41583-020-0277-3)).

## 6. What Can Be Translated Into AI Regularization?

The answer is yes, but “regularization” should be used precisely. An explicit
regularizer adds a penalty \(R\) to the task loss,

\[
\mathcal L_{\mathrm{total}}=\mathcal L_{\mathrm{task}}+\lambda R.
\]

Some biological concepts have exactly this form. Others are better represented
as auxiliary objectives, hard parameterizations, state variables, or new
update rules.

| Biological concept | Possible AI translation | Best category | Candidate mathematical form | Main caveat |
|---|---|---|---|---|
| Sparse / energy-efficient activity | penalize high or dense hidden activity | explicit regularizer | \(R_{\text{sparse}}=\frac1B\sum_b\lVert h_b\rVert_1\) or a firing-cost surrogate | sparse activations are only a proxy for hardware energy |
| Firing-rate homeostasis | keep each unit near a target mean/range and prevent dead or saturated units | regularizer or adaptive threshold/state | \(R_{\text{homeo}}=\sum_j(\mathbb E_b[h_{bj}]-\rho_j)^2\) plus variance/range constraints | one shared target can erase useful unit heterogeneity |
| Redundancy reduction / efficient coding | decorrelate feature dimensions while preserving information | auxiliary or representation regularizer | \(R_{\text{decor}}=\lVert\operatorname{offdiag}(C_h)\rVert_F^2\) | complete decorrelation can discard task-relevant redundancy |
| Synaptic consolidation | resist changes to parameters important for old tasks | explicit continual-learning regularizer | \(R_{\text{cons}}=\sum_i\Omega_i(\theta_i-\theta_i^*)^2\) | parameter importance is approximate and may block transfer |
| Topography and wiring economy | place similar responses nearby and penalize long connections | regularizer plus structured architecture | \(R_{\text{wire}}=\sum_{ij}d_{ij}|w_{ij}|\), or a graph-Laplacian smoothness penalty | brain-likeness can trade off with raw task accuracy |
| Temporal continuity and prediction | predict future/local inputs or make representations stable over short time | auxiliary predictive/contrastive loss | \(R_{\text{pred}}=\sum_t\lVert h_{t+1}-g(h_t)\rVert^2\) | naive slowness collapses dynamic variables; negatives or variance constraints may be needed |
| Dale-like sign constraints and E/I organization | constrain a unit's outgoing weights to one sign and model inhibition separately | hard parameterization or architecture | \(W_{ij}=s_i\operatorname{softplus}(A_{ij})\), \(s_i\in\{-1,+1\}\) | a soft penalty permits violations and may not reproduce circuit dynamics |
| Three-factor Hebbian plasticity | local eligibility trace multiplied by a modulatory signal | update rule, not ordinary regularizer | \(\Delta w_{ij}=\eta e_{ij}m_j\) | the hard problem is constructing informative \(m_j\), not writing the local product |
| Dendritic error segregation / feedback alignment | separate feedforward activity from teaching feedback | architecture and credit-assignment rule | compartmental state or a distinct feedback matrix \(B_l\) | adding a loss penalty alone does not create the required information pathway |
| Replay / sleep-like consolidation | replay stored or generated past experience between online episodes | training protocol and memory system | replay loss on sampled past states/data | replay is not a parameter-only regularizer and introduces storage/generation choices |

### Representative precedents

- Learning a sparse code for natural images produced localized, oriented,
  band-pass receptive fields resembling properties of V1 simple cells
  ([Olshausen & Field,
  1996](https://klab.tch.harvard.edu/academia/classes/BAI/pdfs/OlshausenField_Nature1996.pdf)).
- BCM plasticity makes synaptic change depend on instantaneous pre/post
  activity and a slowly varying postsynaptic activity statistic, providing a
  classic bridge between Hebbian selectivity and homeostatic control
  ([Bienenstock, Cooper, & Munro,
  1982](https://pmc.ncbi.nlm.nih.gov/articles/PMC6564292/)). Synaptic scaling
  has also been observed experimentally after prolonged activity manipulation
  ([Turrigiano et al.,
  1998](https://www.nature.com/articles/36103.pdf)).
- Barlow Twins turns the efficient-coding idea of redundancy reduction into a
  cross-correlation objective for self-supervised representation learning
  ([Zbontar et al.,
  2021](https://proceedings.mlr.press/v139/zbontar21a.html)). This is a direct
  engineering use of a neuroscience principle, not a claim that cortex trains
  with the Barlow Twins loss.
- Elastic Weight Consolidation and Synaptic Intelligence instantiate
  consolidation as importance-weighted quadratic penalties and reduce
  forgetting in their evaluated sequential-learning settings
  ([Kirkpatrick et al.,
  2017](https://doi.org/10.1073/PNAS.1611835114);
  [Zenke, Poole, & Ganguli,
  2017](https://proceedings.mlr.press/v70/zenke17a)).
- Connectivity and sign constraints can produce cortex-like topographic
  organization in task-optimized visual models
  ([Blauch, Behrmann, & Plaut,
  2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8784138/)). This supports the
  idea that anatomical cost can be an informative inductive bias, but it does
  not establish a universal performance gain.

## 7. A Useful Composite Objective—and Its Boundary

For a conventional differentiable network, a practical biological-constraint
prototype could be

\[
\begin{aligned}
\mathcal L_{\mathrm{total}}=
&\;\mathcal L_{\mathrm{task}}
+\lambda_s\mathbb E\lVert h\rVert_1
+\lambda_h\sum_j(\mathbb E[h_j]-\rho_j)^2\\
&+\lambda_d\lVert\operatorname{offdiag}(C_h)\rVert_F^2
+\lambda_c\sum_i\Omega_i(\theta_i-\theta_i^*)^2.
\end{aligned}
\]

This combines activity cost, homeostasis, redundancy reduction, and
consolidation. It can still be optimized with ordinary backpropagation. That is
perfectly legitimate if the engineering question is “does a brain-derived
prior help AI?” It does **not** answer the mechanistic question “could a brain
learn this network?”

To study the latter, the update mechanism itself must change or be constrained.
Examples include feedback alignment, dendritic teaching signals, predictive
coding, equilibrium propagation, and eligibility-trace methods. In recurrent
spiking networks, e-prop uses local eligibility traces and instantaneous
learning signals instead of propagating errors backward through time; it
approached BPTT performance on the paper's evaluated tasks, but remained an
approximation with task-dependent gaps ([Bellec et al.,
2020](https://www.nature.com/articles/s41467-020-17236-y)).

## 8. Recommended Experimental Strategy

Do not begin with a “biological regularizer soup.” Use a factorial ablation:

1. Train a baseline with standard weight decay and matched tuning budget.
2. Add one constraint at a time: activity sparsity, firing-rate homeostasis,
   and representation decorrelation.
3. Add pairwise combinations only after the single-constraint effects are
   stable across seeds.
4. For continual learning, run a separate sequential-task experiment with EWC
   or Synaptic Intelligence; it answers a different question from
   representation regularization.
5. Measure task accuracy together with the property the constraint actually
   targets: activation density, dead/saturated-unit fraction, covariance
   spectrum/effective rank, calibration, corruptions/OOD performance, update
   energy proxy, and forgetting.
6. Compare against a non-biological control with similar capacity or penalty
   strength. A gain over the unregularized baseline alone does not show that
   the biological interpretation caused the gain.

A good first hypothesis is deliberately narrow:

> A homeostatic activity penalty will preserve a broader usable activation
> distribution under nonstationary training, improving plasticity at a fixed
> task-performance and tuning budget.

This is more falsifiable than “making the network more brain-like improves
intelligence.”

## 9. Failure Modes and Misconceptions

- **Regularizers are not learning rules.** A biologically inspired loss trained
  by backprop remains a backprop-trained system.
- **Local update does not imply local objective.** A synapse-local product can
  contain a teaching signal computed by a global process.
- **Gradient approximation does not imply biological implementation.** A
  model can recover gradients with local-looking equations while requiring
  restrictive initialization, phases, settling, or feedback assumptions.
- **Brain-likeness and engineering quality are separate axes.** A constraint
  can improve neural predictivity while hurting accuracy, or improve
  robustness without becoming more biologically faithful.
- **The brain is not merely sparsity plus Hebbian learning.** Stability,
  inhibition, modulators, replay, multiple memory systems, and embodiment
  matter.
- **A single benchmark cannot identify a mechanism.** Many objectives and
  update rules can yield similar performance or representations.

## 10. Evidence Status

### Established or directly source-supported

- Backpropagation efficiently computes parameter gradients through the chain
  rule.
- Biological synaptic change can depend on local activity, slowly varying
  eligibility, and temporally specific modulatory signals.
- Homeostatic synaptic scaling, sparse sensory coding, and multi-timescale
  plasticity are empirically or theoretically supported biological phenomena.
- Sparse-activity, decorrelation, wiring-cost, and consolidation penalties are
  implementable in artificial networks and have concrete published examples.

### Model-supported interpretation

- Feedback alignment, predictive coding, dendritic compartments, equilibrium
  propagation, burst-dependent learning, and e-prop show routes by which local
  mechanisms can approximate useful credit assignment. They establish
  computational possibility under their assumptions, not a universal cortical
  mechanism. See also [Payeur et al.
  (2021)](https://www.nature.com/articles/s41593-021-00857-x).

### Working hypotheses

- Combining homeostasis with decorrelation may improve representation
  diversity under distribution shift.
- Wiring/topographic constraints may improve robustness or interpretability
  when the task has spatial structure.
- Three-factor local rules may be especially useful for online or neuromorphic
  systems even when they do not match backpropagation's offline accuracy.

These hypotheses require controlled experiments; they should not be recorded
as established advantages.

## 11. Open Questions

1. Which biological constraint improves an engineering metric after matching
   parameter count, compute, and hyperparameter-search budget?
2. Do homeostatic activity targets preserve plasticity in large transformers,
   or do normalization layers already supply most of the benefit?
3. Can a local learning signal remain informative across depth and time at
   modern model scale?
4. Which measurements could distinguish two credit-assignment rules that reach
   similar task performance?
5. When does adding anatomical realism improve brain-model alignment but reduce
   task optimization, and is that trade-off scientifically useful?

## 12. Related Notes and Survey State

- [Biological Credit Assignment — Learning-Rule Identifiability](biological-credit-assignment.md)
- Survey scaffold: `.research/surveys/biological-learning-vs-backprop/`
- The survey is currently **framed**, not coverage-audited; the sources above
  are representative seeds rather than an exhaustive or bias-audited corpus.

