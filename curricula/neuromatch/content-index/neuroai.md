# Neuromatch NeuroAI — Content Index

Source coursebook: <https://neuroai.neuromatch.io/>  
Extracted: 2026-06-19 · 46 tutorial pages

> Structured per-tutorial index: title, learning objectives, and section structure with source URLs. Per repo policy, no long passages are copied — open the linked page for full text, equations, and code.

## Days

- [W1D1](#w1d1) (5 pages)
- [W1D2](#w1d2) (5 pages)
- [W1D3](#w1d3) (7 pages)
- [W1D5](#w1d5) (5 pages)
- [W2D1](#w2d1) (5 pages)
- [W2D2](#w2d2) (5 pages)
- [W2D3](#w2d3) (3 pages)
- [W2D4](#w2d4) (7 pages)
- [W2D5](#w2d5) (4 pages)


## W1D1

### Intro

- Source: <https://neuroai.neuromatch.io/w1d1-intro/>
- Sections:
  - Prerequisites
  - Video
  - Slides
  - Diagram

### Tutorial 1: Generalization in AI

- Source: <https://neuroai.neuromatch.io/w1d1-tutorial1/>
- Estimated time: 75 minutes
- Objectives:
  - Identify and articulate common objectives pursued by AI researchers and developers, such as:
  - Out-of-Distribution (OOD) robustness; Latency; Size, Weight, Power, and Cost (SWaP-C)
  - Explainability and understanding
  - Explain at least three strategies for enhancing the generalization capabilities of AI systems, including the contemporary trend of training generic large-scale models on extensive datasets (foundation models).
  - Gain practical experience with the fundamentals of deep learning and PyTorch.
- Sections:
  - Definitions
  - Section 1: Motivation: building a handwriting recognition app with AI
  - Interactive demo 1: TrOCR
  - Discussion point 1
  - Section 2: Measuring out-of-distribution generalization in TrOCR
  - Think! 1
  - Coding activity 1: Measuring out-of-distribution generalization
  - Code exercise 1.1: Calculate CER and WER
  - Code exercise 1.2: Calculate CER and WER across all subjects
  - Code exercise 1.3: Measure OOD generalization
  - Discussion
  - Section 3: Dissecting TrOCR
  - Section 3.1: The encoder
  - Code exercise 3.1: Understanding the inputs and outputs of the encoder
  - Section 3.2: The decoder
  - Interactive exploration 3.2: What the model pays attention to
  - Section 4: The magic in the data
  - Section 4.1: Transfer learning
  - Reflection
  - Section 4.2: Generalization via augmentation
  - Section 4.3: Generalization via synthetic data
  - Discussion point
  - Interactive demo 4.1: Generating handwriting style data
  - Conclusion
  - The Big Picture

### Tutorial 2: Generalization in Neuroscience

- Source: <https://neuroai.neuromatch.io/w1d1-tutorial2/>
- Estimated time: 75 minutes
- Objectives:
  - Understand core goals in neuroscience. Examine the fundamental questions that drive neuroscience research, such as the ‘What’, ‘How’, and ‘Why’ behind neurological functions and behaviors.
  - Conceptualize what generalization means in the context of neuroscience, understanding how principles of neural generalization can inform and be informed by artificial intelligence.
  - Evaluate the impact of architectural choices. Discuss how different architectural decisions and the selection of priors in model design can introduce inductive biases, affecting the generalization capabilities of both neural and artificial systems.
  - Illustrate robustness in noisy environments. Identify and describe real-world instances where the pursuit of robustness against noise has led to converging strategies in both neuroscience and artificial intelligence.
- Sections:
  - Set device (GPU or CPU). Execute set_device()
  - Set random seed, when using pytorch
  - Definitions
  - Section 1: Motivation: How the brain generates motor commands
  - Section 2: Training an unregularized task-driven neural network
  - Coding exercise 2.1: Defining an unregularized RNN
  - Coding exercise 2.2: Evaluate function
  - Activity 2.1: Evaluating the model
  - Activity 2.2: Comparing trained RNN with the brain
  - Section 3: Training a regularized task-driven neural network
  - Activity 3.1: Evaluating the model
  - Activity 3.2: Comparing trained RNN with real data
  - Discussion point
  - Section 4: Robustness to change in RNNs and the brain
  - Coding exercise 4.1: Weights perturbation
  - Discussion point 1
  - Discussion point 2
  - The Big Picture

### Tutorial 3: Generalization in Cognitive Science

- Source: <https://neuroai.neuromatch.io/w1d1-tutorial3/>
- Estimated time: 30 minutes
- Objectives:
  - Explore the goals of cognitive science. Understand the aims of cognitive science such as unraveling the complexities of human cognition.
  - Define one-shot learning and sample complexity. Perform a task that involves one-shot learning.
  - Explore how a neurosymbolic model with strong inductive biases could explain one-shot learning on Omniglot.
- Sections:
  - Section 1: How people recognize new characters
  - Reflection activity 1.1
  - Reflection activity 1.2
  - Section 2: Model of one-shot learning
  - The Big Picture

### W1D1 Outro

- Source: <https://neuroai.neuromatch.io/w1d1-outro/>


## W1D2

### Intro

- Source: <https://neuroai.neuromatch.io/w1d2-intro/>
- Sections:
  - Prerequisites
  - Video
  - Slides

### Tutorial 1: Task definition, application, relations and impacts on generalization

- Source: <https://neuroai.neuromatch.io/w1d2-tutorial1/>
- Objectives:
  - Formulate different tasks in terms of cost functions
  - Train a network to accomplish these tasks and compare the performance of these networks
  - Measure how well different representations generalize
- Sections:
  - Set device (GPU or CPU)
  - Set random seed
  - Section 1: Tasks as Cost Functions
  - Review of CNNs
  - Preparing the data
  - Visualizing some samples from the dataset
  - Preparing the data loaders
  - Section 1.1: Classification
  - Code exercise 1: Cost Function
  - Training
  - Cost Function
  - Defining the model
  - Training on different dataset sizes
  - Test performance
  - Discussion point 1
  - Section 1.2: Regression
  - Task objective
  - Output layer
  - Code exercise 2: Cost function
  - Dataset preparation
  - Model training and evaluation
  - Discussion point 2
  - Section 1.3: Auto-encoder
  - Autoencoder architecture
  - Code exercise 3: Cost Function
  - Dataset
  - Discussion point 3
  - Section 1.4: Self-supervised - Inpainting
  - Random masking
  - Autoencoder Cost Function
  - Discussion point 4
  - Section 2: Generalization of representations
  - Section 2.1: Transfer
  - Taskonomy
  - Transfer learning
  - Copy weights
  - Transfer example 1: regression to classification
  - Discussion point 5
  - Transfer example 2: autoencoder to classification
  - Discussion point 6
  - Transfer example 3: inpainting to classification
  - Discussion point 7
  - Bonus discussion point 8
  - The Big Picture

### Tutorial 2: Contrastive learning for object recognition

- Source: <https://neuroai.neuromatch.io/w1d2-tutorial2/>
- Estimated time: 40 minutes
- Objectives:
  - Understand why we want to do contrastive learning.
  - Understand the losses used in contrastive learning.
  - Train a network using contrastive learning on MNIST.
- Sections:
  - Section 1: Building the model
  - What is contrastive learning?
  - Constructing the model
  - Building the model from residual blocks
  - The geometry of the untrained network
  - Reflection
  - Section 2: Training the model and visualizing feature similarity
  - The contrastive loss function
  - Decoupled contrastive learning
  - Batching and numerical stability
  - Code exercise 2: The decoupled contrastive learning loss function
  - Matching and Non-Matching Pairs
  - Visualizing the cosine similarity after training
  - Visualizing the geometry of the embeddings before and after training
  - Using the network to identify nearest neighbours from the train set
  - How is contrastive learning used in practice?
  - Discussion point
  - The Big Picture

### Tutorial 3: Reinforcement learning across temporal scales

- Source: <https://neuroai.neuromatch.io/w1d2-tutorial3/>
- Objectives:
  - Review how a reinforcement learning algorithm can be evaluated
  - Formulate a simple meta-reinforcement learning framework where an algorithm learns how to learn in different episodes
  - Investigate learning at different temporal scales
- Sections:
  - Definitions
  - Section 1: An Introduction to POMDPs
  - Section 2: Reinforcement learning across temporal scales
  - Reinforcement learning review
  - Discussion point 1
  - Evaluating decision-making strategies
  - Discussion point 2
  - Demo 1: Binary bandit
  - A fixed agent in a changing world
  - Discussion point 3
  - Section 3: Meta-learning and meta-reinforcement learning
  - Prefrontal cortex as a meta-reinforcement learning system
  - Learning at different time scales
  - Architecture
  - Uncorrelated vs. correlated settings, seen through cumulative regret
  - The learned model dynamics implement an RL algorithm
  - Discussion point 4
  - Summary
  - The Big Picture

### W1D2 Outro

- Source: <https://neuroai.neuromatch.io/w1d2-outro/>


## W1D3

### Intro

- Source: <https://neuroai.neuromatch.io/w1d3-intro/>
- Sections:
  - Prerequisites
  - Video
  - Slides

### Tutorial 1: Generalization and representational geometry

- Source: <https://neuroai.neuromatch.io/w1d3-tutorial1/>
- Estimated time: 40 minutes
- Objectives:
  - Understand the concept of representational geometry and the representational dissimilarity matrix.
  - Understand the connection between generalization and representational similarity in the linear case.
  - Understand how the analytic solution for linear regression can be seen as a weighted sum of training values, weighted by the test inputs’ similarity to the training inputs.
  - Question on comparing RDMs.
  - Question on the relationship between RDMs and model performances.
  - Interactive exercise on how similarity structure affects predictions.
- Sections:
  - Set random seed
  - Set device (GPU or CPU)
  - Section 1: MNIST DNN Comparisons
  - Understanding the MNIST DNNs
  - Defining the MNIST Model
  - MNIST Model
  - Training the Standard Model
  - Build and train the model
  - Grab a pretrained model
  - Adversarial Attack & Model Robustness
  - Grab 5 test images from each category and visualize them
  - Generate adversarial images for the standard model
  - Training the Adversarially Robust Model
  - Train adversirially robust model
  - Grab an adversarially pretrained model
  - Generate adversarial images for the adversarially trained model
  - Evaluating Model Robustness
  - Test model
  - Extracting Model Features and Analyzing Representations
  - Extract model features with torchlens
  - What is an RDM?
  - Visualizing RDMs
  - RDMs for the labels (see the category structures)
  - For standard model + standard images
  - For adversarially trained model + standard images
  - Think!
  - For standard model + adversarial images
  - For adversarially trained model + adversarial images
  - Section 3: Interactive Exploration with Widgets
  - Interactive exercise
  - Execute to see the widget!
  - The Big Picture

### Tutorial 2: Computation as transformation of representational geometries

- Source: <https://neuroai.neuromatch.io/w1d3-tutorial2/>
- Estimated time: 40 minutes
- Objectives: We’ll see that each transformation can remove information, preserve other information, and change the format in which the information is represented.Download slides
- Sections:
  - Set random seed
  - Set device (GPU or CPU)
  - Section 1: Computation & representational geometries
  - Grab a standard model
  - Just sample 5 per category to show the order
  - Computational steps
  - Features for different layers
  - Calculating and plotting the RDMs
  - Putting it all together
  - Dimensionality reduction
  - Sequential image representation clustering
  - Comparing RDMs
  - Representational Path
  - Think!
  - Test your idea by executing this cell!
  - Adversarial images
  - Representational geometry in standard network
  - Representational geometry in an adversarially trained network
  - Grab an adversarially robust model
  - Test an adversarially robust model
  - Dimensionality reduction visualization
  - Plot the representational geometry changes
  - Comparing representational geometry paths between models
  - Compare representational paths
  - The Big Picture

### Tutorial 3: Statistical inference on representational geometries

- Source: <https://neuroai.neuromatch.io/w1d3-tutorial3/>
- Estimated time: 50 minutes
- Objectives:
  - Understand Representational Similarity Analysis (RSA), including its theoretical foundations, practical applications, and its significance in the context of machine learning and computational neuroscience.
  - Extract neural network activations; understand the structure of neural networks, the role of activations in interpreting neural network decisions, and practical techniques for accessing these activations.
  - Discuss frequentist model comparison: This part of the tutorial will cover the basics of frequentist model comparison methods. It will provide an overview of the principles underlying these methods and their applications.
  - Identify sources of estimation error and the motivation for model-comparative frequentist inference. You will learn about the three main sources of estimation error in statistical inference—measurement noise, stimulus sampling, and subject sampling. Additionally, the tutorial will explore how these sources of error justify the use of model-comparative frequentist inference, particularly through the application of the 2-factor bootstrap method. This section will detail the impact of each source of error on statistical inference and demonstrate how the 2-factor bootstrap accounts for our uncertainty about model performance during model comparison.
- Sections:
  - Section 1: Data Acquisition
  - Define constants
  - Show image
  - Load the images and get image size
  - Visualize images
  - Section 2: Get artificial neural network activations
  - Load AlexNet model pretrained on ImageNet
  - Preprocess NSD images as input to AlexNet
  - Inspect architecture
  - Make hooks in AlexNet to extract activations from different layers
  - Extract activations from AlexNet
  - Section 3: Create representational dissimilarity matrices (RDMs)
  - Creating RSA toolbox datasets
  - Create RSA datasets for each subject and ROI
  - Create RSA datasets for AlexNet activations
  - Computing the RDMs
  - Compute rdms for each subject and ROI
  - Coding Exercise 1: RDMs of AlexNet
  - Visualizing human RDMs
  - Coding Exercise 2: Human RDMs
  - Visualizing AlexNet RDMs
  - Section 4: RSA. Model comparison and statistical inference
  - Get the Model objects to use the rsa toolbox for model comparisons
  - Visualize AlexNet performance
  - Visualize RDMs
  - Visualize model evaluations
  - Discussion
  - Comparing representations statistically
  - Details of the figure above
  - Generalization to new images
  - Get the RDMs for a bootstrap sample of the images
  - Section 5: Model Comparison Using Two-factor Bootstrap
  - Summary
  - The Big Picture

### (Bonus) Tutorial 4: Representational geometry & noise

- Source: <https://neuroai.neuromatch.io/w1d3-tutorial4/>
- Estimated time: 45 minutes.
- Objectives:
  - Generating simulated neural data with different noise distributions. This section will guide you through the process of creating simulated neural data and introducing variability in noise distributions. This step will illustrate how different noise levels can affect data representation and subsequent analyses.
  - The Euclidean distance and Mahalanobis distance. Each of these metrics offers unique insights into the geometry of the data.
  - The relationship between distance metrics and binary classification performance. This part of the tutorial emphasizes the relationship between distance measurements and the performance of binary classification tasks on a given pair of stimuli. Understanding this relationship will help us develop more accurate and robust classification models.
  - The positive bias that arises when measuring distances from noisy pattern estimates and how cross-validation can correct this bias and give more accurate estimates of the underlying noise-free distance.
  - Using random projections to estimate distances. This section introduces the Johnson–Lindenstrauss Lemma, which states that random projections maintain the integrity of distance estimates in a lower-dimensional space. This concept is crucial for reducing dimensionality while preserving the relational structure of the data.
- Sections:
  - Section 1: Simulate neural data and visualize noise distributions
  - Coding Exercise 1
  - Generate data
  - Section 2: Distances and discriminability between a pair of stimuli
  - Coding exercise 2: Distance-metrics comparison
  - Coding Exercise 2 Discussion
  - Section 4: The Johnson-Lindenstrauss Lemma
  - Coding exercise 3: Random projections
  - Discussion
  - Summary
  - The Big Picture

### Tutorial 5: Dynamical Similarity Analysis (DSA)

- Source: <https://neuroai.neuromatch.io/w1d3-tutorial5/>
- Sections:
  - Set device (GPU or CPU)
  - Intro
  - Section 1: Visualization of Three Temporal Sequences
  - Multi-way Comparison
  - DSA Hyperparameters (n_delays and delay_interval)
  - Comparison with RSA
  - (Bonus) Representational Geometry of Recurrent Models
  - Grab a recurrent model
  - Representational geometry paths for recurrent models
  - The Big Picture

### W1D3 Outro

- Source: <https://neuroai.neuromatch.io/w1d3-outro/>


## W1D5

### Intro

- Source: <https://neuroai.neuromatch.io/w1d5-intro/>
- Sections:
  - Prerequisites
  - Video
  - Slides

### Tutorial 1: Sparsity and Sparse Coding

- Source: <https://neuroai.neuromatch.io/w1d5-tutorial1/>
- Estimated time: 1 hour 20 minutes
- Objectives:
  - Recognize various types of sparsity (population, lifetime, interaction).
  - Relate sparsity to inductive bias, interpretability, and efficiency.
- Sections:
  - Section 1: Introduction to sparsity
  - Sparsity in Neuroscience and Artificial Intelligence
  - How can we quantify sparsity?
  - Section 2: Computing and altering sparsity
  - Section 2.1: Sparsity via nonlinearity
  - Coding Exercise 2.1: Sparsity as the result of thresholding
  - Execute the cell to see the interactive widget!
  - Plot of change in pixel’s value over time
  - Plot your results
  - Threshold value impact on ReLU version of the signal
  - Kurtosis value comparison
  - Section 2.2: Sparsity from temporal differentiation
  - Coding Exercise 2.2: Temporal differencing signal
  - Observe the result
  - Histograms for the signal and its temporal differences
  - Kurtosis values for the signal and its temporal differences
  - Coding Exercise 2.3: Changes over longer delays
  - Histogram plots for different values of τ\tau
  - Plot sparsity (kurtosis) for different values of τ\tau
  - Exploring temporal differencing with a box filter
  - Filter visualization
  - Discussion
  - Plot signal and its temporal derivative on a longer timescale
  - Define different window values
  - Visualize temporal differences for different window sizes
  - Histogram for each of the window size
  - Compare sparsity (measured by kurtosis) for different window sizes
  - Section 3: Sparse coding
  - Section 3.1: Finding coefficients for sparse codes
  - Neuroscience measures of sparse responses
  - Computational Neuroscience model of sparse coding
  - ℓ0\ell_0
  - How can we find the sparse vector hh
  - Coding Exercise 3: OMP algorithm
  - Plot of 3 basis signals
  - Visualize basis features and signal reconstruction
  - OMP for different cardinality
  - Cardinality impact on reconstruction quality
  - Section 3.2: Hidden features as dictionary learning
  - What if we do not know the dictionary of features?
  - Coding Exercise 4: Dictionary Learning for MNIST
  - Visualization of features
  - Visualization of impact of features through the time
  - PCA components visualization
  - Dictionary Learning for CIFAR10
  - Load CIFAR-10 dataset
  - Create & explore video
  - Set default parameters
  - Images visualization
  - Load full model & visualize features
  - Sparse Activity of the components (hh
  - Summary
  - The Big Picture

### Tutorial 2: Normalization

- Source: <https://neuroai.neuromatch.io/w1d5-tutorial2/>
- Estimated time: 50 minutes
- Objectives:
  - Understand how nonlinearities may be universal function approximators, but not all functions are simple to learn
  - Implement a family of normalization mechanisms
  - Demonstrate how normalization helps in learning and information transmission
- Sections:
  - Set random seed
  - Set device (GPU or CPU)
  - Section 1: Can ReLUs implement normalization?
  - Generate y=1x+ϵy=\frac{1}{x+\epsilon}
  - Coding Exercise 1: ReLUNet
  - Training & Evaluating model
  - Plot Training Loss Dynamics
  - Vizualize ReLUs
  - Plot Weight Dynamics
  - Coding Exercise 1 Discussion
  - Coding Exercise 2: Test other non-linear activation functions
  - Train & Evaluate
  - Section 2: Benefits of normalization
  - Subsection 2.1: Explore normalization
  - Coding Exercise 2.1: Implement normalization
  - Interactive Demo 2.1
  - Effect of smoothing factor (σ\sigma
  - Subsection 2.2: Estimating latent properties
  - Interactive Demo 2.2.1
  - Plot correlation of estimated reflectance with true reflectance
  - Interactive Demo 2.2.2
  - Subsection 2.3: Layer Normalization
  - Get CIFAR3 scaled and unscaled dataloader
  - Visualize Images
  - Define CIFARNet model
  - Training & Evaluating the models
  - Test Generalization
  - Summary
  - The Big Picture

### Tutorial 3: Attention

- Source: <https://neuroai.neuromatch.io/w1d5-tutorial3/>
- Estimated time: 1 hour
- Objectives:
  - Learn how the brain and AI systems implement attention
  - Understand how multiplicative interactions allow flexible gating of information
  - Demonstrate the inductive bias of the self-attention mechanism towards learning functions of sparse subsets of variables
- Sections:
  - Set random seed
  - Set device (GPU or CPU)
  - Section 1: Intro to Multiplication
  - Exercise 1: Dot product attention
  - Execute this cell to enable the widget
  - Section 2: Self-Attention
  - Section 2.1: Tokens
  - Section 2.2: More multiplications
  - Bonus Section 2.3: Dimensions of Self-Attention
  - Bonus Exercise 2: Implement self-attention
  - Section 3: Inductive bias of self-attention: Sparse variable creation
  - Dataset
  - Exercise 3: MLP vs. Self-Attention
  - Exercise 3.1: MLP
  - Exercise 3.2: Self-Attention
  - Exercise 3.3: Coding Exercise Comparing results
  - Extra: Context-dependent Attention Weights
  - The Big Picture

### W1D5 Outro

- Source: <https://neuroai.neuromatch.io/w1d5-outro/>


## W2D1

### Intro

- Source: <https://neuroai.neuromatch.io/w2d1-intro/>
- Sections:
  - Prerequisites
  - Video
  - Slides

### Tutorial 1: Depth vs width

- Source: <https://neuroai.neuromatch.io/w2d1-tutorial1/>
- Estimated time: 1 hour
- Objectives:
  - The universal approximator theorem guarantees that we can approximate any complex function using a network with a single hidden layer. The catch is that the approximating network might need to be extremely wide and the theorem only states the existence of such a model (not exactly how neurons are required per task)
  - We will explore this issue by constructing a complex function and attempting to fit it with shallow networks of varying widths
  - To create this complex function, we’ll build a random deep neural network. This is an example of the student-teacher setting, where we attempt to fit a known teacher function (the deep network) using a student model (the shallow/wide network)
  - We will see that it can be either very easy or very difficult to learn from the deep (teacher) network and this difficulty is related to a form of chaos in the network activations
  - Each layer of a neural network can effectively expand and fold the input it receives from the previous layer. This repeated expansion and folding grants deep neural networks models high expressivity - ie. allows them to capture the behavior of a large number of different functions
- Sections:
  - Set random seed
  - Section 1: Introduction
  - Coding Exercise 1: Create an MLP
  - Network Implementation
  - Coding Exercise 2: Initialize model weights
  - Coding Exercise 3: Generate a dataset
  - Coding Exercise 4: Train model and compute loss
  - Coding Exercise 4 Discussion
  - Section 2: Fitting a deep network with a shallow network
  - Coding Exercise 5: Create learning problem
  - Coding Exercise 5 Discussion
  - Coding Exercise 6: Train net with the same architecture
  - Coding Exercise 7: Train a 2 layer neural net with varying widths
  - Coding Exercise 8: Network size prediction
  - Section 3: Deep networks in the quasi-linear regime
  - Coding Exercise 9: Create Dataset & Train a Student Network
  - Interactive Demo 1: Deep networks expressivity
  - Interactive Demo 1 Discussion
  - Summary
  - The Big Picture

### Tutorial 2: Double descent

- Source: <https://neuroai.neuromatch.io/w2d1-tutorial2/>
- Estimated time: 1 hour
- Objectives:
  - notions of low/high bias/variance
  - improvement of test performance with the network’s overparameterization, which leads to large model trends
  - the conditions under which double descent is observed and what affects its significance
  - the conditions under which double descent does not occur
- Sections:
  - Set random seed
  - Section 1: Overfitting in overparameterized models
  - Coding Exercise 1: Learning with a simple neural network
  - Sample and plot sinusoidal dataset
  - Coding Exercise 2: The Bias-Variance Trade-off
  - Coding Exercise 2 Discussion
  - Observe the performance on 5 hidden units
  - Observe the performance on 10 hidden units
  - Section 2: The Modern Regime
  - Observe the performance on 500 hidden units
  - Coding Exercise 3: Observing double descent
  - Interactive Demo 1: Interpolation point & predictions
  - Execute this cell to observe interactive plot
  - Section 3: Double Descent, Noise & Regularization
  - Coding Exercise 4: Noise & regularization impact
  - Observe the error plots with regularization term included
  - Section 4: Double Descent and Initialization
  - Coding Exercise 5: Initialization scale impact
  - Coding Exercise 5 Discussion
  - Execute the cell to observe the plot
  - The Big Picture

### Tutorial 3: Neural network modularity

- Source: <https://neuroai.neuromatch.io/w2d1-tutorial3/>
- Sections:
  - Set random seed
  - Section 1: RL agents in a spatial navigation task
  - Task setup
  - Parameters definition
  - Coding Exercise 1: Task environment
  - Coding exercise 2: RL agent
  - Agent observation
  - Observation dynamics
  - Actor-critic RL agent
  - Holistic actor
  - Test your implementation of `HolisticActor’!
  - Modular actor
  - Test your implementation of `ModularActor’!
  - Coding Exercise 2 Discussion
  - Section 2: Evaluate agents in the training task
  - Coding Exercise 3: Evaluation function
  - Sample 1000 targets
  - Coding Exercise 4: Agent trajectory in a single trial
  - Modular agent trajectory
  - Holistic agent trajectory
  - Coding Exercise 4 Discussion
  - Activity: Comparing performance of agents
  - Agent trajectories across trials
  - Modular agent’s trajectories
  - Holistic agent’s trajectories
  - Discussion
  - Agents trained with multiple random seeds
  - Load agents
  - Reward fraction comparison
  - Reward function comparison
  - Time spent comparison
  - Training curve
  - Load training curves
  - Visualize training curves
  - Section 3: A novel gain task
  - Load holistic & modular agents
  - Load data
  - Traveled distance comparison
  - Discussion:
  - Decoding analysis
  - Decoding error comparison
  - The Big Picture
  - Addendum: Generalization, but no free lunch

### W2D1 Outro

- Source: <https://neuroai.neuromatch.io/w2d1-outro/>


## W2D2

### W2D2 - Neurosymbolic Methods and Cognitive Architectures

- Source: <https://neuroai.neuromatch.io/w2d2-intro/>
- Sections:
  - Prerequisites
  - Video
  - Slides

### Tutorial 1: Basic operations of vector symbolic algebra

- Source: <https://neuroai.neuromatch.io/w2d2-tutorial1/>
- Estimated time: 1 hour
- Sections:
  - Set random seed
  - Section 1: High-dimensional vector symbols
  - Coding Exercise 1: Concepts as High-Dimensional Vectors
  - Coding Exercise 1 Discussion
  - Section 2: Bundling
  - Coding Exercise 2: A Composite Object - Shape
  - Coding Exercise 2 Discussion
  - Section 3: Binding & Unbinding
  - Coding Exercise 3: Colorful Shapes
  - Coding Exercise 4: Foundations of Colorful Shapes
  - Section 4: Cleanup
  - Coding Exercise 5: Cleanup Memories To Find The Best-Fit
  - Section 5: Iterated Binding
  - Coding Exercise 6: Representing Numbers
  - Background Material
  - Coding Exercise 7: Beyond Binding Integers
  - Coding Exercise 7 Discussion
  - Summary

### Tutorial 2: Learning with structure

- Source: <https://neuroai.neuromatch.io/w2d2-tutorial2/>
- Estimated time: 20 minutes
- Objectives: Download slides
- Sections:
  - Set random seed
  - Section 1: Wason Card Task
  - Coding Exercise 1: Wason Card Task
  - The Big Picture

### Tutorial 3: Question Answering with Memory

- Source: <https://neuroai.neuromatch.io/w2d2-tutorial3/>
- Objectives: This model shows a form of question answering with memory. You will bind two features (color and shape) by circular convolution and store them in a memory population. Then you will provide a cue to the model at a later time to determine either one of the features by deconvolution. This model exhibits better cognitive ability since the answers to the questions are provided at a later time and not at the same time as the questions themselves. These operations use the primitives we introduced in Tu
- Sections:
  - Intro
  - Nengo & Question Answering
  - Section 1: Define the input functions
  - Create the model
  - Probe the Model
  - Run the model
  - Plot the results
  - Coding Exercise
  - The Big Picture

### W2D2 Outro

- Source: <https://neuroai.neuromatch.io/w2d2-outro/>


## W2D3

### Intro

- Source: <https://neuroai.neuromatch.io/w2d3-intro/>
- Sections:
  - Prerequisites
  - Video
  - Slides

### Tutorial 1: Microlearning

- Source: <https://neuroai.neuromatch.io/w2d3-tutorial1/>
- Estimated time: 2 hours
- Objectives:
  - They optimize global objective functions that define behavioral/perceptual goals for an agent.
  - Unlike learning algorithms like backpropagation, they demonstrate how learning is ‘local’, i.e. it uses only information that could conceivably be available to a single synapse.
  - Relate local plasticity rules to estimates of loss gradients.
  - Understand the impact of variance and bias in gradient estimators and how they affect the scalability, performance, and generalization capabilities of learning algorithms.
  - Implement 2-3 learning rules in toy tasks.
  - Describe issues with biological plausibility in some learning algorithms, most notably, weight transport.
- Sections:
  - Section 1: Weight Perturbation
  - Exercise 1: Perturb the weights
  - Training an MLP on MNIST with weight perturbation
  - Hyperparameters definition
  - Train WeightPerturbMLP
  - Observe the performance of WeightPerturbMLP
  - Section 2: Node Perturbation
  - Train NodePerturbMLP
  - Observe the performance of NodePerturbMLP
  - Section 3: Assessing the variance of learning algorithms
  - Empirical demonstration
  - Section 4: Feedback Alignment
  - Exercise 2: Feedback alignment algorithm
  - Define hyperparameters
  - Train FeedbackAlignmentMLP
  - Observe the performance of FeedbackAlignmentMLP
  - Section 5: Kolen-Pollack
  - Exercise 3: Kolen-Pollack algorithm
  - Train KolenPollackMLP
  - Observe the performance of KolenPollackMLP
  - Section 6: Assessing the bias of learning algorithms
  - Classification accuracy comparison
  - Summary
  - The Big Picture

### W2D3 Outro

- Source: <https://neuroai.neuromatch.io/w2d3-outro/>


## W2D4

### Intro

- Source: <https://neuroai.neuromatch.io/w2d4-intro/>
- Sections:
  - Macrolearning
  - Prerequisites
  - Video
  - Slides

### Tutorial 1: The problem of changing data distributions

- Source: <https://neuroai.neuromatch.io/w2d4-tutorial1/>
- Estimated time: 30 minutes
- Objectives: Distribution shifts occur when the testing data distribution deviates from the training data distribution; that is, when a model is evaluated on data that somehow differs from what it was trained on.There are many ways that testing data can differ from training data. Two broad categories of distribution shifts are: covariate shift and concept shift. While we expect most of you to be familiar with the term concept, the term covariate is used in different ways in different fields and we want to cl
- Sections:
  - Section 1: Covariate shift
  - Coding Exercise 1: Fitting pricing data to MLP
  - Make sure you execute this cell to observe the plot!
  - Coding Exercise 1 Discussion
  - Interactive Demo 1: Covariate shift impact on predictability power
  - Interactive Demo 1 Discussion
  - Section 2: Concept shift
  - Exercise 2: Change in the day of supply
  - Exercise 2 Discussion
  - Think!: Examples of concept shift
  - Summary
  - The Big Picture

### Tutorial 2: Continual learning

- Source: <https://neuroai.neuromatch.io/w2d4-tutorial2/>
- Estimated time: 25 minutes
- Objectives: This is like the idea of learning a new idea by replacing an old one. This is a huge issue with the current AI models and deep neural networks and a very active area of research in the ML community. We are going to explore the problem in more detail and investigate some further issues connected to this idea, for example, how different learning schedules impact performance.Download slides
- Sections:
  - Set random seed
  - Section 1: Catastrophic Forgetting
  - Coding Exercise 1: Fitting new data
  - Section 2: Joint training
  - Coding Exercise 2a: Sequential joint training
  - Coding Exercise 2b: Interspersed training
  - Coding Exercise 2 Discussion
  - Summary
  - The Big Picture

### Tutorial 3: Meta-learning

- Source: <https://neuroai.neuromatch.io/w2d4-tutorial3/>
- Estimated time: 50 minutes
- Objectives: Download slides
- Sections:
  - Set random seed
  - Section 1: Introducing meta-learning task
  - Coding Exercise 1: Task space
  - Make sure you execute this cell to observe the plot!
  - Coding Exercise 1 Discussion
  - Section 2: Meta-training
  - Coding Exercise 2: All about training
  - Think 2: Dreaming about a model
  - Section 3: Adapt to a particular task
  - Coding Exercise 3: Fine-tuning model
  - Interactive Demo 1: Number of data points & gradient steps
  - Make sure you execute this cell to observe the widget!
  - The Big Picture

### Tutorial 4: Biological meta reinforcement learning

- Source: <https://neuroai.neuromatch.io/w2d4-tutorial4/>
- Estimated time: 70 minutes
- Objectives: Download slides
- Sections:
  - Set device (GPU or CPU)
  - Set random seed
  - Section 0: Let’s play a game!
  - Make sure you execute this cell to play the game!
  - Section 1: Harlow Experiment & Advantage Actor Critic (A2C) Agent
  - Make sure you execute this cell to observe the plot!
  - Section 2: Baldwin Effect
  - Agent’s Rate to Learn
  - Coding Exercise 1: Genetic Algorithm
  - Think!: Evolutionary Theories in Code
  - Section 3: Newbie & Experienced Bird
  - Summary
  - The Big Picture

### (Bonus) Tutorial 5: Replay

- Source: <https://neuroai.neuromatch.io/w2d4-tutorial5/>
- Estimated time: 40 minutes
- Objectives: This mirrors how mammals, particularly during sleep, reactivate neural patterns from recent experiences to consolidate memories and extract generalizable patterns. In artificial RL systems, experience replay enables more efficient learning by breaking temporal correlations between consecutive experiences and allowing multiple learning updates from single experiences (runs of a series of steps in an RL experiment). This biologically inspired approach has proven crucial for deep RL algorithms like
- Sections:
  - Set random seed
  - Section 0: Let’s play a new game!
  - Make sure you execute this cell to play the game!
  - Section 1: A Changing Environment
  - Exercise 1: Colorful State
  - Make sure you execute this cell to observe the plot!
  - Section 2: A2C Agent in a Changing Environment
  - Section 3: Replay Buffer
  - Coding Exercise 2: Experience Again
  - Test your implementation of ReplayBuffer!
  - Summary
  - The Big Picture

### W2D4 Outro

- Source: <https://neuroai.neuromatch.io/w2d4-outro/>


## W2D5

### Intro

- Source: <https://neuroai.neuromatch.io/w2d5-intro/>
- Sections:
  - Mysteries
  - Prerequisites
  - Video
  - Slides

### Tutorial 1: Consciousness

- Source: <https://neuroai.neuromatch.io/w2d5-tutorial1/>
- Estimated time: 120 minutes
- Objectives:
  - Understand and distinguish various aspects of consciousness including the hard problem of consciousness, the difference between phenomenal consciousness and access consciousness, as well as the distinctions between consciousness and sentience or intelligence.
  - Explore core frameworks for analyzing consciousness, including diagnostic criteria, and will compare objective probabilities with subjective credences.
  - Explore reductionist theories of consciousness, such as Global Workspace Theory (GWT), theories of metacognition, and Higher-Order Thought (HOT) theories.
- Sections:
  - Set device (GPU or CPU)
  - Section 1: Global Neuronal Workspace
  - Section 1a: Modularity Of The Mind
  - Modularity Recap
  - Recurrent Independent Mechanisms (RIMs)
  - Discussion point
  - Section 1b: A Shared Workspace
  - Coding Exercise 1: Creating a Shared Workspace
  - Section 2: Higher order assessment and metacognition
  - Second order model
  - Coding Exercise 2: Developing a Second-Order Network
  - Higher Order State Space (HOSS) model
  - Defining our Stimulus Space
  - Add in higher-order node for global detection
  - Introducing the “A” Level:
  - Model inference
  - Coding exercise
  - The Big Picture

### Tutorial 2: Ethics

- Source: <https://neuroai.neuromatch.io/w2d5-tutorial2/>
- Estimated time: 30-50 minutes (depends on chosen trajectory; see below)
- Objectives:
  - Understand the relationship between consciousness, intelligence, and moral status.
  - Discuss responsible, moral, ethical, and safe artificial intelligence.
- Sections:
  - Section 1: Ethics Intro & Moral Status
  - Discussion activity: moral status
  - Section 2: Ethical AI
  - Section 3: Fair AI
  - Summary

### Outro

- Source: <https://neuroai.neuromatch.io/w2d5-outro/>
- Sections:
  - Video
  - Slides

