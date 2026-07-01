# Neuromatch Deep Learning — Content Index

Source coursebook: <https://deeplearning.neuromatch.io/tutorials/intro.html>  
Extracted: 2026-06-19 · W2–W3 days re-extracted 2026-07-01 after Neuromatch site restructure · 27 tutorial pages

> Structured per-tutorial index: title, learning objectives, and section structure with source URLs. Per repo policy, no long passages are copied — open the linked page for full text, equations, and code.

## Days

- [W1D1 — Basics And Pytorch](#w1d1) (1 pages)
- [W1D2 — Linear Deep Learning](#w1d2) (3 pages)
- [W1D3 — Multi Layer Perceptrons](#w1d3) (2 pages)
- [W1D4 — Optimization](#w1d4) (1 pages)
- [W2D1 — Regularization](#w2d1) (2 pages)
- [W2D2 — Convnets](#w2d2) (3 pages)
- [W2D3 — Generative Models And Deep Learning Discussion 1](#w2d3) (2 pages)
- [W2D4 — Diffusion Generative Models](#w2d4) (2 pages)
- [W2D5 — Time Series And Natural Language Processing](#w2d5) (3 pages)
- [W3D1 — Attention And Transformers](#w3d1) (2 pages)
- [W3D2 — Deep Learning Discussion 2](#w3d2) (1 pages)
- [W3D3 — Unsupervised And Self Supervised Learning](#w3d3) (1 pages)
- [W3D4 — Basic Reinforcement Learning](#w3d4) (1 pages)
- [W3D5 — Advanced Reinforcement Learning And Deep Learning Discussion 3](#w3d5) (2 pages)
- [Bonus — Deploy Models (Bonus)](#bonus) (1 pages)


## W1D1 — Basics And Pytorch

### Tutorial 1: PyTorch

- Source: <https://deeplearning.neuromatch.io/tutorials/W1D1_BasicsAndPytorch/student/W1D1_Tutorial1.html>
- Objectives:
  - Learn about PyTorch and tensors
  - Tensor Manipulations
  - Data Loading
  - GPUs and CUDA Tensors
  - Train NaiveNet
  - Get to know your pod
  - Start thinking about the course as a whole
- Sections:
  - Section 1: Welcome to Neuromatch Deep learning course
  - Video 1: Welcome and History
  - Video 2: Why DL is cool
  - Section 2: The Basics of PyTorch
  - Section 2.1: Creating Tensors
  - Video 3: Making Tensors
  - Numpy-like number ranges:
  - Coding Exercise 2.1: Creating Tensors
  - Section 2.2: Operations in PyTorch
  - Video 4: Tensor Operators
  - Coding Exercise 2.2 : Simple tensor operations
  - Section 2.3 Manipulating Tensors in Pytorch
  - Video 5: Tensor Indexing
  - Coding Exercise 2.3: Manipulating Tensors
  - Section 2.4: GPUs
  - Video 6: GPU vs CPU
  - Coding Exercise 2.4: Just how much faster are GPUs?
  - Section 2.5: Datasets and Dataloaders
  - Video 7: Getting Data
  - Coding Exercise 2.5: Display an image from the dataset
  - Video 8: Train and Test
  - Video 9: Data Augmentation - Transformations
  - Coding Exercise 2.6: Load the CIFAR10 dataset as grayscale images
  - Section 3: Neural Networks
  - Video 10: CSV Files
  - Section 3.1: Data Loading
  - Generate sample data
  - Section 3.2: Create a Simple Neural Network
  - Video 11: Generating the Neural Network
  - Coding Exercise 3.2: Classify some samples
  - Section 3.3: Train Your Neural Network
  - Video 12: Train the Network
  - Visualize the training process
  - Video 13: Play with it
  - Exercise 3.3: Tweak your Network
  - Video 14: XOR Widget
  - Interactive Demo 3.3: Solving XOR
  - Section 4: Ethics And Course Info
  - Video 15: Ethics
  - Video 16: Be a group
  - Video 17: Syllabus
  - Meet our lecturers
  - Week 1: the building blocks
  - Week 2: making things work
  - Week 3: more magic
  - Bonus - 60 years of Machine Learning Research in one Plot
  - Define Visualization using ALtair
  - Questions
  - Methods
  - Find Authors
  - Appendix
  - Official PyTorch resources:
  - Tutorials
  - Documentation
  - Google Colab Resources:
  - Books for reference:


## W1D2 — Linear Deep Learning

### Tutorial 1: Gradient Descent and AutoGrad

- Source: <https://deeplearning.neuromatch.io/tutorials/W1D2_LinearDeepLearning/student/W1D2_Tutorial1.html>
- Objectives:
  - Gradient descent
  - PyTorch Autograd
  - PyTorch nn module
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 0: Introduction
  - Video 0: Introduction
  - Section 1: Gradient Descent Algorithm
  - Section 1.1: Gradients & Steepest Ascent
  - Video 1: Gradient Descent
  - Analytical Exercise 1.1: Gradient vector (Optional)
  - Coding Exercise 1.1: Gradient Vector
  - Video 2: Gradient Descent - Discussion
  - Section 1.2: Gradient Descent Algorithm
  - Analytical Exercise 1.2: Gradients
  - Section 1.3: Computational Graphs and Backprop
  - Video 3: Computational Graph
  - Analytical Exercise 1.3: Chain Rule (Optional)
  - Section 2: PyTorch AutoGrad
  - Video 4: Auto-Differentiation
  - Section 2.1: Forward Propagation
  - Coding Exercise 2.1: Buiding a Computational Graph
  - Section 2.2: Backward Propagation
  - References and more
  - Section 3: PyTorch’s Neural Net module (nn.Module)
  - Video 5: PyTorch nn module
  - Section 3.1: Training loop in PyTorch
  - Generate the sample dataset
  - Coding Exercise 3.1: Training Loop
  - Summary
  - Video 6: Tutorial 1 Wrap-up

### Tutorial 2: Learning Hyperparameters

- Source: <https://deeplearning.neuromatch.io/tutorials/W1D2_LinearDeepLearning/student/W1D2_Tutorial2.html>
- Objectives:
  - Training landscape
  - The effect of depth
  - Choosing a learning rate
  - Initialization matters
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 1: A Shallow Narrow Linear Neural Network
  - Video 1: Shallow Narrow Linear Net
  - Section 1.1: A Shallow Narrow Linear Net
  - Analytical Exercise 1.1: Loss Gradients (Optional)
  - Solution
  - Coding Exercise 1.1: Implement simple narrow LNN (Optional)
  - Section 1.2: Learning landscapes
  - Video 2: Training Landscape
  - Video 3: Training Landscape - Discussion
  - Section 2: Depth, Learning rate, and initialization
  - Section 2.1: The effect of depth
  - Video 4: Effect of Depth
  - Interactive Demo 2.1: Depth widget
  - Video 5: Effect of Depth - Discussion
  - Section 2.2: Choosing a learning rate
  - Video 6: Learning Rate
  - Interactive Demo 2.2: Learning rate widget
  - Video 7: Learning Rate - Discussion
  - Section 2.3: Depth vs Learning Rate
  - Video 8: Depth and Learning Rate
  - Interactive Demo 2.3: Depth and Learning Rate
  - Video 9: Depth and Learning Rate - Discussion
  - Section 2.4: Why initialization is important
  - Video 10: Initialization Matters
  - Video 11: Initialization Matters - Discussion
  - Summary
  - Video 12: Tutorial 2 Wrap-up
  - Bonus
  - Hyperparameter interaction

### Tutorial 3: Deep linear neural networks

- Source: <https://deeplearning.neuromatch.io/tutorials/W1D2_LinearDeepLearning/student/W1D2_Tutorial3.html>
- Objectives:
  - Deep linear neural networks
  - Learning dynamics and singular value decomposition
  - Representational Similarity Analysis
  - Illusory correlations & ethics
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 0: Prelude
  - Coding Exercise 0: Re-initialization (Optional)
  - Section 1: Deep Linear Neural Nets
  - Video 1: Intro to Representation Learning
  - Run to generate and visualize training samples from tree
  - Interactive Demo 1: Training the deep LNN
  - Make sure you execute this cell to train the network and plot
  - Make sure you execute this cell to enable the widget!
  - Section 2: Singular Value Decomposition (SVD)
  - Video 2: SVD
  - Coding Exercise 2: SVD (Optional)
  - Video 3: SVD - Discussion
  - Section 3: Representational Similarity Analysis (RSA)
  - Video 4: RSA
  - Coding Exercise 3: RSA (Optional)
  - Make sure you execute this cell to enable widgets
  - Video 5: RSA - Discussion
  - Section 4: Illusory Correlations
  - Video 6: Illusory Correlations
  - Demonstration: Illusory Correlations
  - Exercise 4: Illusory Correlations
  - Video 7: Illusory Correlations - Discussion
  - Summary
  - Video 8: Outro
  - Bonus
  - Video 9: Linear Regression
  - Section 5.1: Linear Regression
  - Section 5.2: Vectorized regression
  - Section 5.3: Analytical Linear Regression
  - Coding Exercise 5.3.1: Analytical solution to LR
  - Demonstration: Linear Regression vs. DLNN
  - Video 10: Linear Regression - Discussion


## W1D3 — Multi Layer Perceptrons

### Tutorial 1: Biological vs. Artificial Neural Networks

- Source: <https://deeplearning.neuromatch.io/tutorials/W1D3_MultiLayerPerceptrons/student/W1D3_Tutorial1.html>
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 0: Introduction to MLPs
  - Video 0: Introduction
  - Section 1: The Need for MLPs
  - Video 1: Universal Approximation Theorem
  - Coding Exercise 1: Function approximation with ReLU
  - Section 2: MLPs in PyTorch
  - Video 2: Building MLPs in PyTorch
  - Coding Exercise 2: Implement a general-purpose MLP in Pytorch
  - Section 2.1: Classification with MLPs
  - Video 3: Cross Entropy
  - Coding Exercise 2.1: Implement Batch Cross Entropy Loss
  - Section 2.2: Spiral Classification Dataset
  - Section 2.3: Training and Evaluation
  - Video 4: Training and Evaluating an MLP
  - Coding Exercise 2.3: Implement it for a classfication task
  - Think! 2.3.1: What’s the point of .eval() and .train()?
  - Think! 2.3.2: Does it generalize well?
  - Summary
  - Bonus: Neuron Physiology and Motivation to Deep Learning
  - Video 5: Biological to Artificial Neurons
  - Leaky Integrate-and-fire (LIF) neuronal model
  - Simulating an LIF Neuron
  - Think!: Real and Artificial neuron similarities

### Tutorial 2: Deep MLPs

- Source: <https://deeplearning.neuromatch.io/tutorials/W1D3_MultiLayerPerceptrons/student/W1D3_Tutorial2.html>
- Objectives:
  - Can be deep or wide
  - Dependant on transfer functions
  - Sensitive to initialization
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Data Loader
  - Section 1: Wider vs deeper networks
  - Video 1: Deep Expressivity
  - Think! 1: Why the tradeoff?
  - Section 1.1: Where Wide Fails
  - Think! 1.1: Does a wide model generalize well?
  - Section 2: Deeper MLPs
  - Video 2: Case study
  - Coding Exercise 2: Dataloader on a real-world dataset
  - Think! 2: Why first layer features are high level?
  - Section 3: Ethical aspects
  - Video 3: Ethics: Hype in AI
  - Summary
  - Video 4: Outro
  - Bonus: The need for good initialization
  - Video 5: Need for Good Initialization
  - Xavier initialization
  - Initialization with transfer function
  - Best gain for Xavier Initialization with Leaky ReLU


## W1D4 — Optimization

### Tutorial 1: Optimization techniques

- Source: <https://deeplearning.neuromatch.io/tutorials/W1D4_Optimization/student/W1D4_Tutorial1.html>
- Objectives:
  - Necessity and importance of optimization
  - Introduction to commonly used optimization techniques
  - Optimization in non-convex loss landscapes
  - ‘Adaptive’ hyperparameter tuning
  - Ethical concerns
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 1. Introduction
  - Video 1: Introduction
  - Discuss: Unexpected consequences
  - Video 2: Case Study - MLP Classification
  - Section 2.1: Data
  - Run me!
  - Section 2.2: Model
  - Section 2.3: Loss
  - Section 2.4: Interpretability
  - Section 3: High dimensional search
  - Video 3: Optimization of an Objective Function
  - Coding Exercise 3: Implement gradient descent
  - Comparing updates
  - Think! 3: Gradient descent vs. random search
  - Section 4: Poor conditioning
  - Video 4: Momentum
  - Think 4!: How momentum works?
  - Coding Exercise 4: Implement momentum
  - Interactive Demo 4: Momentum vs. GD
  - Think! 4: Momentum and oscillations
  - Section 5: Non-convexity
  - Video 5: Overparameterization
  - Interactive Demo 5: Overparameterization to the rescue!
  - Think! 5.1: Width and depth of the network
  - Section 6: Full gradients are expensive
  - Video 6: Mini-batches
  - Interactive Demo 6.1: Cost of computation
  - Coding Exercise 6: Implement minibatch sampling
  - Interactive Demo 6.2: Compare different minibatch sizes
  - Section 7: Adaptive methods
  - Video 7: Adaptive Methods
  - Coding Exercise 7: Implement RMSprop
  - Interactive Demo 7: Compare optimizers
  - Think 7.1!: Compare optimizers
  - Locality of Gradients
  - Think! 7.2: Loss function and optimization
  - Section 8: Ethical concerns
  - Video 8: Ethical concerns
  - Summary
  - Bonus: Putting it all together
  - Video 9: Putting it all together
  - Exercise Bonus: Train your own model
  - Think! Bonus: Metrics
  - Evaluation


## W2D1 — Regularization

### Tutorial 1: Regularization techniques part 1

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D1_Regularization/student/W2D1_Tutorial1.html>
- Objectives:
  - Big Artificial Neural Networks (ANNs) are efficient universal approximators due to their adaptive basis functions
  - ANNs memorize some but generalize well
  - Regularization as shrinkage of overparameterized models: early stopping
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 0: Defining useful functions
  - Section 1: Regularization is Shrinkage
  - Video 1: Introduction to Regularization
  - Video 2: Regularization as Shrinkage
  - Coding Exercise 1: Frobenius Norm
  - Section 2: Overfitting
  - Video 3: Overparameterization and Overfitting
  - Section 2.1: Visualizing Overfitting
  - Animation (Run Me!)
  - Plot the train and test losses
  - Think! 2.1: Interpreting losses
  - Section 2.2: Overfitting on Test Dataset
  - Validation Dataset
  - Section 3: Memorization
  - Frobenius norm for AnimalNet before and after training
  - Data Visualizer
  - Section 4: Early Stopping
  - Video 4: Early Stopping
  - Coding Exercise 4: Early Stopping
  - Think! 4: Early Stopping
  - Summary
  - Bonus: Train with randomized labels
  - Think! Bonus: Does it Generalize?

### Tutorial 2: Regularization techniques part 2

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D1_Regularization/student/W2D1_Tutorial2.html>
- Objectives:
  - Regularization as shrinkage of overparameterized models: L1 and L2
  - Regularization by Dropout
  - Regularization by Data Augmentation
  - Perils of Hyper-Parameter Tuning
  - Rethinking generalization
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Dataloaders for the Dataset
  - Section 1: L1 and L2 Regularization
  - Video 1: L1 and L2 regularization
  - Section 1.1: Unregularized Model
  - Dataloaders for Regularization
  - Section 1.2: L1 Regularization
  - Coding Exercise 1.1: L1 Regularization
  - Section 1.3: L2 / Ridge Regularization
  - Coding Exercise 1.2: L2 Regularization
  - Visualize Norm of the Models (Train Me!)
  - Section 2: Dropout
  - Video 2: Dropout
  - Run to train the default network
  - Think 2.1!: Dropout
  - Section 2.1: Dropout Implementation Caveats
  - Think 2.2! Dropout caveats
  - Section 3: Data Augmentation
  - Video 3: Data Augmentation
  - Data Loader without Data Augmentation
  - Think 3.1!: Data Augmentation
  - Think! 3.2!: Overparameterized vs. Small NN
  - Section 4: Stochastic Gradient Descent
  - Video 4: SGD
  - Section 4.1: Learning Rate
  - Generating Data Loaders
  - Section 5: Hyperparameter Tuning
  - Video 5: Hyperparameter tuning
  - Think! 5: Overview of regularization techniques
  - Summary
  - Bonus: Adversarial Attacks
  - Video 6: Adversarial Attacks


## W2D2 — Convnets

### Tutorial 1: Introduction to CNNs

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D2_Convnets/student/W2D2_Tutorial1.html>
- Objectives:
  - Define what convolution is
  - Implement convolution as an operation
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 0: Recap
  - Video 1: Introduction to CNNs and RNNs
  - Section 1: Neuroscience motivation, General CNN structure
  - Video 2: Representations & Visual processing in the brain
  - Think! 1: What makes a representation good?
  - Section 2: Convolutions and Edge Detection
  - Video 3: Details about Convolution
  - Interactive Demo 2: Visualization of Convolution
  - Definitional Note
  - Coding Exercise 2.1: Convolution of a Simple Kernel
  - Coding Exercise 2.2: Convolution Output Size
  - Coding Exercise 2.3: Coding a Convolution
  - Convolution on the Chicago Skyline
  - Load images (run me)
  - Section 2.1: Demonstration of a CNN in PyTorch
  - Section 2.2: Padding and Edge Detection
  - Interactive Demo 2.2: Visualization of Convolution with Padding and Stride
  - Think! 2.2.1: Edge Detection
  - Think! 2.2.2 Kernel structure
  - Section 3: Kernels, Pooling and Subsampling
  - Download EMNIST dataset
  - Dataset/DataLoader Functions (Run me!)
  - Interactive Demo 3: Visualization of Convolution with Multiple Filters
  - Section 3.1: Multiple Filters
  - Think! 3.1: Do you see how these filters would help recognize an X?
  - Section 3.2: ReLU after convolutions
  - Section 3.3: Pooling
  - Video 4: Pooling
  - Interactive Demo 3.3: The effect of the stride
  - Coding Exercise 3.3: Implement MaxPooling
  - Section 4: Putting it all together
  - Video 5: Putting it all together
  - Section 4.1: Number of Parameters in Convolutional vs. Fully-connected Models
  - Interactive Demo 4.1: Number of Parameters
  - Video 6: Implement your own CNN
  - Coding Exercise 4: Implement your own CNN
  - Train/Test Functions (Run Me)
  - Section 5: Transfer Learning
  - Video 7: Transfer Learning
  - Section 5.1: Download and prepare the data
  - Download Data
  - Determine number of classes
  - Display Example Images
  - Section 5.2: Fine-tuning a ResNet
  - Finetune ResNet
  - Section 5.3: Train only classification layer
  - Finetune readout of ResNet
  - Section 5.4: Training ResNet from scratch
  - Train ResNet from scratch
  - Section 5.5: Head to Head Comparison
  - Plot Accuracies
  - Exercise 5.5.1: Pretrained ResNet vs. ResNet trained from scratch
  - Exercise 5.5.2: Training only the classification layer
  - Further Reading
  - Summary

### Bonus Tutorial: Writing Your Own Training Loop (Bonus)

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D2_Convnets/student/W2D2_Tutorial2.html>
- Objectives:
  - Train a CNN by writing your own training loop
  - Recognize the symptoms of overfitting and how to combat them
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 1: Write Your Own Training Loop
  - Video 1: Writing your own training loop
  - Section 1.1: Understand the Dataset
  - Download Fashion MNIST dataset
  - Loading Fashion-MNIST Data
  - Video 2: The Training Loop
  - Section 1.2: Backpropagation Reminder
  - Load a sample dataset (EMNIST)
  - Section 1.3: Fashion-MNIST Dataset
  - Getting the DataLoaders (Run Me)
  - Coding Exercise 1: Code the Training Loop
  - Think! 1: Overfitting

### Bonus Tutorial: Modern ConvNets and Facial Recognition (Bonus)

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D2_Convnets/student/W2D2_Tutorial3.html>
- Objectives:
  - Learn about the history of CNNs and modern CNN architectures (AlexNet, ResNet, Inception, ResNeXt, MobileNet)
  - Compare accuracy and training speed across different model backbones
  - Apply modern ConvNets to facial recognition
  - Understand ethical considerations in facial recognition systems
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 1: The History of Convnets
  - Video 1: History of convnets
  - Think! 1: Challenges of improving CNNs
  - Section 2: Big and Deep Convnets
  - Video 2: AlexNet & VGG
  - Section 2.1: Introduction to AlexNet
  - Import Alexnet
  - Section 2.2: What does AlexNet learn?
  - Think! 2.2.1: Filter Similarity
  - Interactive Demo 3.2: What does AlexNet see?
  - Think! 2.2.2 Filter Purpose
  - Further Reading
  - Section 3: Convnets After AlexNet
  - Video 3: Residual Networks (ResNets)
  - Download imagenette
  - Set Up Textual ImageNet labels
  - Map Imagenette Labels to Imagenet Labels
  - Prepare Imagenette Data
  - eval_imagenette function
  - Imagenette Train Loop
  - Coding Exercise 3.1: Use the ResNet model
  - Out-of-distribution examples
  - Section 4: Inception + ResNeXt
  - Video 4: Improving efficiency: Inception and ResNeXt
  - ResNet vs ResNeXt
  - Interactive Demo 4: ResNet vs. ResNeXt
  - Parameter Calculator
  - Think! 4: ResNet vs. ResNeXt
  - Section 5: Depthwise separable convolutions
  - Video 5: Improving efficiency: MobileNet
  - Section 5.1: Depthwise separable convolutions
  - Coding Exercise 5.1: Calculation of parameters
  - Think! 5.1: How do parameter savings depend the on number of input feature maps, 4 vs. 64?
  - Summary
  - Video 6: Summary and Outlook
  - Section 6: Speed-Accuracy Trade-Off / Different Backbones
  - Video 7: Speed-accuracy trade-off
  - Coding Exercise 6: Compare accuracy and training speed of different models
  - Imagenette Train Loop: train_loop(model, optimizer, train_loader, loss_fn, device)
  - Run the models: run_models(models, lr_rates)
  - Plot accuracies vs. training speed
  - Exercise 6.1: Finding the best model
  - Exercise 6.2: Speed and accuracy correlation
  - Section 7: Face Recognition
  - Section 7.1: Download and prepare the data
  - Download Faces Data
  - Video 8: Face Recognition using CNNs
  - Section 7.2: View and transform the data
  - Display Images
  - Image Preprocessing Function
  - Section 7.3: Embedding with a pretrained network
  - Think! 7.3: Embedding vectors
  - Section 8: Ethics – bias/discrimination due to pre-training datasets
  - Video 9: Ethical aspects
  - Section 8.1: Download the Data
  - Run this cell to get the data
  - Section 8.2: Load, view and transform the data
  - Visualize some example faces
  - Section 8.3: Calculate embeddings
  - Function to calculate pairwise distances
  - Visualize the distances
  - Exercise 8.1: Face similarity
  - Exercise 8.2: Embeddings
  - Section 8.4: Within Sum of Squares
  - Function to calculate WSS
  - Summary


## W2D3 — Generative Models And Deep Learning Discussion 1

### Tutorial 1: Introduction to generative models

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D3_GenerativeModelsAndDeepLearningDiscussion1/student/W2D3_Tutorial1.html>
- Objectives:
  - Think about unsupervised learning / Generative Models and get a bird's eye view of why it is useful
  - Build intuition about latent variables
  - See the connection between AutoEncoders and PCA
  - Start thinking about neural networks as generative models by contrasting AutoEncoders and Variational AutoEncoders
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Download wordnet dataset
  - Section 1: Generative models
  - Video 1: Generative Modeling
  - Section 1.1: Generating Images from BigGAN
  - Interactive Demo 1.1: BigGAN Generator
  - Think! 1.1: Generated images
  - Section 1.2: Interpolating Images with BigGAN
  - Interactive Demo 1.2: BigGAN Interpolation
  - Think! 1.2: Interpolating samples from the same category
  - Section 2: Latent Variable Models
  - Video 2: Latent Variable Models
  - (Bonus) Coding Exercise 2: pPCA
  - Section 3: Autoencoders
  - Video 3: Autoencoders
  - Select a dataset
  - Section 3.1: Conceptual introduction to AutoEncoders
  - Coding Exercise 3.1: Linear AutoEncoder Architecture
  - Comparison to PCA
  - Think! 3.1: PCA vs. Linear autoenconder
  - Section 3.2: Building a nonlinear convolutional autoencoder
  - Coding Exercise 3.2: Fill in code for the ConvAutoEncoder module
  - Section 4: Variational Auto-Encoders (VAEs)
  - Video 4: Variational Autoencoders
  - Section 4.1: Components of a VAE
  - Section 4.2: Generating novel images from the decoder
  - Coding Exercise 4.2: Generating images
  - Think! 4.2: AutoEncoders vs. Variational AutoEncoders
  - Section 5 (Bonus): State of the art VAEs and Wrap-up
  - Video 5: State-Of-The-Art VAEs
  - Summary

### Tutorial 2: Deep Learning Discussion 1: Cost Functions

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D3_GenerativeModelsAndDeepLearningDiscussion1/student/W2D3_Tutorial2.html>
- Objectives:
  - Appreciate the importance of cost function engineering
  - Translate domain knowledge into cost functions
  - Ask questions about DL systems and customer needs
- Sections:
  - Section 1: Intro to Deep Learning Discussion
  - Video 1: Intro to DL Discussion
  - Section 2: Cost function for neurons
  - Video 2: Spiking Neuron Predictions Vignette
  - Video 3: Spiking Neuron Predictions Set-up
  - Think! 1: Designing a cost function to predict neural activities
  - Video 4: Spiking Neurons Wrap-up
  - (Bonus) Think!: Non-Poisson neurons
  - Section 3: How can an ANN know its uncertainty
  - Video 5: ANN Uncertainty Vignette
  - Video 6: ANN Uncertainty Set-up
  - Think! 2: Designing a cost function so we measure uncertainty
  - Video 7: ANN Uncertainty Wrap-up
  - (Bonus) Think!: Negative standard deviations
  - Section 4: Embedding faces
  - Video 8: Embedding Faces Vignette
  - Video 9: Embedding Faces Set-up
  - Think! 3: Designing a cost function for face embedding
  - Video 10: Embedding Faces Wrap-up
  - Summary


## W2D4 — Diffusion Generative Models

### Tutorial 1: Diffusion models

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D4_DiffusionGenerativeModels/student/W2D4_Tutorial1.html>
- Objectives:
  - Understand the idea behind Diffusion generative models: using score to enable reversal of diffusion process.
  - Learn the score function by learning to denoise data.
  - Hands-on experience in learning the score to a generate certain distribution.
- Sections:
  - Section 1: Understanding Score and Diffusion
  - Notes: score-based model vs. diffusion model
  - Video 1: Intro and Principles
  - Video 2: Math Behind Diffusion
  - Section 1.1: Diffusion Process
  - Interactive Demo 1.1: Visualizing diffusion
  - 1D diffusion process
  - 2D diffusion process
  - Section 1.2: What is Score
  - Coding Exercise 1.2: Score for Gaussian Mixtures
  - Custom Gaussian Mixture class
  - Example: Gaussian mixture model
  - Visualize log density
  - Visualize Score
  - Score for Gaussian mixture
  - Score for each Gaussian mode
  - Compare Score of individual mode with that of the mixture.
  - Think! 1.2: What does score tell us?
  - Section 1.3: Reverse Diffusion
  - Bonus Exercise 1.3 (Optional): Score enables reversal of diffusion
  - Section 2: Learning the score by denoising
  - Think! 2: Denoising objective
  - Coding Exercise 2: Implementing Denoising Score Matching Objective
  - Test loss function
  - Define utils functions (Neural Network, and data sampling)
  - Test the Denoising Score Matching loss function
  - Plot the Loss
  - Test the Learned Score by Reverse Diffusion
  - Summary
  - Bonus: The Math behind Score Matching Objective

### Tutorial 2: Image Diffusion

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D4_DiffusionGenerativeModels/student/W2D4_Tutorial2.html>
- Objectives:
  - Understand the idea behind Diffusion generative models: score and reversal of diffusion process.
  - Learn the score function by denoising data.
  - Hands-on experience in learning the score to generate certain distributions.
- Sections:
  - Section 1: Neural Network Architecture
  - Video 1: Network architecture
  - Coding Exercise 1: Train Diffusion for MNIST
  - Network architecture
  - Time embedding and modulation
  - Time-dependent UNet score model
  - Think! 1: U-Net Architecture
  - Coding Exercise 2: Defining the loss function
  - Test loss function
  - Train and Test the Diffusion Model
  - Training the model
  - Define the Sampler
  - Sampling
  - Section 2: Ethical Considerations
  - Video 2: Ethical Consideration
  - Think! 2: Copyright of imagery generated from diffusion generated models
  - Summary


## W2D5 — Time Series And Natural Language Processing

### Tutorial 1: Introduction to processing time series

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D5_TimeSeriesAndNaturalLanguageProcessing/student/W2D5_Tutorial1.html>
- Sections:
  - Load Dataset from nltk
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 1: Intro: What time series are there?
  - Video 1: Time Series and NLP
  - Video 2: What is NLP?
  - Section 2: Embeddings
  - Video 3: NLP Tokenization
  - Section 2.1: Introduction
  - Creating Word Embeddings
  - Visualizing Word Embeddings
  - Think! 2.1: Similarity
  - Section 2.2: Embedding exploration
  - Video 4: Embeddings rule!
  - Video 5: Distributional Similarity and Vector Embeddings
  - Embedding Manipulation
  - Word Similarity
  - Interactive Demo 2.2.1: Check similarity between words
  - Homonym Similarity
  - Interactive Demo 2.2.2: Explore homonyms
  - Word Analogies
  - Section 2.3: Neural Net with word embeddings
  - Video 6: Using Embeddings
  - Coding Exercise 1: Simple feed forward net
  - Summary

### Tutorial 2: Natural Language Processing and LLMs

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D5_TimeSeriesAndNaturalLanguageProcessing/student/W2D5_Tutorial2.html>
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 1: NLP architectures
  - Video 1: Intro to NLPs and LLMs
  - Section 2: The NLP pipeline
  - Video 2: NLP pipeline
  - Tokenizers
  - Learning Goals
  - Generating a dataset
  - Tokenizer Features
  - Special Tokens
  - Think 2.1! Tokenizer good practices
  - Think 2.2: Chinese and English tokenizer
  - Section 3: Using BERT
  - Learning Goals
  - Video 3: BERT
  - Section 4: NLG with GPT
  - Learning goals
  - Video 4: NLG
  - Using state-of-the-art (SOTA) Models
  - Think 4.1! Tokenizers
  - Think 4.2! Using SOTA models
  - Fine-Tuning
  - Implement the code to fine-tune the model
  - Coding Exercise 4.1: Implement the code to generate text after fine-tuning.
  - Think 4.3! Accuracy metric observations
  - Section 5: GPT Today and Tomorrow
  - Video 5: Conclusion
  - Summary
  - Bonus Section: Using Large Language Models (LLMs)
  - Video 6: Using GPT

### Bonus Tutorial: Multilingual Embeddings

- Source: <https://deeplearning.neuromatch.io/tutorials/W2D5_TimeSeriesAndNaturalLanguageProcessing/student/W2D5_Tutorial3.html>
- Sections:
  - Install fastText
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Section 1 : Multilingual Embeddings
  - Training multilingual embeddings


## W3D1 — Attention And Transformers

### Tutorial 1: Learn how to work with Transformers

- Source: <https://deeplearning.neuromatch.io/tutorials/W3D1_AttentionAndTransformers/student/W3D1_Tutorial1.html>
- Objectives:
  - Explain the general attention mechanism using keys, queries, values
  - Name three applications where attention is useful
  - Explain why Transformer is more efficient than RNN
  - Implement self-attention in Transformer
  - Understand the role of position encoding in Transformer
- Sections:
  - Set environment variables
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Load Yelp dataset
  - load_yelp_data helper function
  - Tokenizer
  - Section 1: Attention overview
  - Video 1: Introduction
  - Think! 1: Application of attention
  - Section 2: Queries, keys, and values
  - Video 2: Queries, Keys, and Values
  - Interactive Demo 2: Intution behind Attention
  - Enter your own query/keys
  - Generate random words from the corpus
  - Check if a word is present in Corpus
  - Think! 2: Does this model perform well?
  - Coding Exercise 2: Dot product attention
  - Check Coding Exercise 2!
  - Section 3: Multihead attention
  - Video 3: Multi-head Attention
  - Coding Exercise 3: \(Q\), \(K\), \(V\) attention
  - Section 4: Transformer overview I
  - Video 4: Transformer Overview I
  - Coding Exercise 4: Transformer encoder
  - Section 5: Transformer overview II
  - Video 5: Transformer Overview II
  - Think! 5: Complexity of decoding
  - Section 6: Positional encoding
  - Video 6: Positional Encoding
  - Implement PositionalEncoding() function
  - Section 7: Training Transformers
  - Coding Exercise 7: Transformer Architecture for classification
  - Training the Transformer
  - Prediction
  - Section 8: Ethics in language models
  - Video 8: Ethical aspects
  - Interactive Demo 8: Find biases in the model
  - Probabilities of masked words
  - Think! 8.1: Problems of this approach
  - Hint
  - Think! 8.2: Biases of using these models in other fields
  - Section 9: Transformers beyond Language models
  - Summary

### Bonus Tutorial: Understanding Pre-training, Fine-tuning and Robustness of Transformers

- Source: <https://deeplearning.neuromatch.io/tutorials/W3D1_AttentionAndTransformers/student/W3D1_Tutorial2.html>
- Objectives:
  - Write down the objective of language model pre-training
  - Understand the framework of pre-training then fine-tuning
  - Name three types of biases in pre-trained language models
- Sections:
  - Set environment variables
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Bonus 1: Language modeling as pre-training
  - Video 1: Pre-training
  - Bonus Interactive Demo 1: GPT-2 for sentiment classification
  - Load the dataset
  - Bonus 1.1: Load Yelp reviews dataset ⌛🤗
  - Bonus 1.2: Setting up a text context ✍️
  - Bonus 1.3: Extending the review with pre-trained models 🤖
  - Bonus 1.4: Sentiment binary-classification with likelihood of positive and negative extensions of the review 👍👎
  - Bonus 2: Light-weight fine-tuning
  - Video 2: Fine-tuning
  - Bonus 2.1: Data Processing
  - Bonus 2.2: Model Loading
  - Bonus 2.3: Fine-tuning
  - Bonus 3: Model robustness
  - Video 3: Robustness
  - Bonus Interactive Demo 3: Break the model
  - Bonus 3.1: Load an original review
  - Bonus 3.2: Augment the original review
  - Bonus 3.3: Check model predictions


## W3D2 — Deep Learning Discussion 2

### Tutorial 1: Deep Learning Discussion 2: Architectures and Multimodal DL

- Source: <https://deeplearning.neuromatch.io/tutorials/W3D2_DeepLearningDiscussion2/student/W3D2_Tutorial1.html>
- Sections:
  - Section 1: Intro Deep Learning Discussion 2
  - Video 1: Intro to DL Discussion 2
  - Section 2: Getting More Data
  - Video 2: Getting More Data Vignette
  - Think! 1: Designing a strategy to get more data
  - Wrap-up
  - Video 3: Getting More Data Wrap-up
  - (Bonus) Think!: Class-based strategies
  - Section 3: Detecting Tumors - What to do if there still isn't enough data
  - Video 4: Detecting Tumors Vignette
  - Video 5: Detecting Tumors Set-up
  - Think! 2: Designing a strategy for detecting tumors
  - Wrap-up
  - Video 6: Detecting Tumors Wrap-up
  - Section 4: Brains on Forrest Gump
  - Video 7: Brains on Forrest Gump Vignette
  - Video 8: Brains on Forrest Gump Set-up
  - Think! 3: Designing a strategy for pulling shared info about brain data and Forrest Gump
  - Wrap-up
  - Video 9: Brains on Forrest Gump Wrap-up
  - Summary
  - Video 10: Wrap-up of DL Discussion 2


## W3D3 — Unsupervised And Self Supervised Learning

### Tutorial 1: Un/Self-supervised learning methods

- Source: <https://deeplearning.neuromatch.io/tutorials/W3D3_UnsupervisedAndSelfSupervisedLearning/student/W3D3_Tutorial1.html>
- Objectives:
  - Train logistic regressions (A) directly on input data and (B) on representations learned from the data.
  - Compare the classification performances achieved by the different networks.
  - Compare the representations learned by the different networks.
  - Identify the advantages of self-supervised learning over supervised or traditional unsupervised methods.
- Sections:
  - Set random seed
  - Set device (GPU or CPU). Execute set_device()
  - Pre-load variables (allows each section to be run independently)
  - Section 0: Introduction
  - Video 0: Introduction
  - Section 1: Representations are important
  - Video 1: Why do representations matter?
  - Section 1.1: Introducing the dSprites dataset
  - Interactive Demo 1.1.1: Exploring the dSprites dataset
  - Section 1.2: Training a classifier with and without representations
  - Encoder network schematic
  - Section 2: Supervised learning induces invariant representations
  - Video 2: Supervised Learning and Invariance
  - Section 2.1: Examining Representational Similarity Matrices (RSMs)
  - Coding Exercise 2.1.1: Complete a function that calculates RSMs
  - Supporting images for Discussion response examples for 2.1.1
  - Section 3: Random projections don’t work as well
  - Video 3: Random Representations
  - Section 3.1: Examining RSMs of a random encoder
  - Section 4: Generative approaches to representation learning can fail
  - Video 4: Generative models
  - Section 4.1: Examining the RSMs of a Variational Autoencoder
  - Discussion 4.1.1: How does the VAE perform on the reconstruction task?
  - Video 5: Modern Approach in Self-supervised Learning
  - Video 6: Data Transformations
  - Coding Exercise 6.1.1: Complete a SimCLR loss function
  - Video 7: Un/Self-Supervised Learning
  - Section 7.1: The consequences of training models on biased datasets
  - Discussion 7.1.2: How do these principles apply more generally?
  - Summary
  - Video 8: Conclusion
  - Bonus 1: Self-supervised networks learn representation invariance
  - Video 9: Invariant Representations
  - Bonus 2: Avoiding representational collapse
  - Video 10: Avoiding Representational Collapse
  - Bonus 3: Good representations enable few-shot learning
  - Video 11: Few-shot Supervised Learning


## W3D4 — Basic Reinforcement Learning

### Tutorial 1: Basic Reinforcement Learning

- Source: <https://deeplearning.neuromatch.io/tutorials/W3D4_BasicReinforcementLearning/student/W3D4_Tutorial1.html>
- Objectives: Reinforcement Learning (RL) is a powerful framework for defining and solving problems where an agent learns to take actions that maximize its reward. Essentially, an agent observes the current state of the world, selects an action, receives a reward, and uses this feedback to improve its future actions. RL provides a formal, optimal way of describing this learning process, which was initially derived from studies of animal behavior and later validated by observations of the brain in humans and a
- Sections:
  - Section 1: A history of RL
  - Video 1: Intro to RL
  - Section 2: What is RL
  - Section 2.1: Grid World
  - Video 2: Grid World
  - Coding Exercise 1: Code a shortest-path planner for GridWorld
  - Create the GridWorldPlanner object (defaults to simple example)
  - Section 2.2: Markov Decision Process (MDP)
  - Video 3: Markov Decision Process
  - Coding exercise 2: Create an MDP from the GridWorld specification
  - Section 2.3: \(Q\)-values
  - Video 4: Q-values
  - Coding exercise 3: Create a steps-to-go solver
  - Section 3: Value iteration
  - Video 5: Value iteration
  - Coding exercise 4: Implement value iteration
  - Section 4: Policy iteration
  - Video 6: Policy iteration
  - Coding exercise 5: Implement policy iteration
  - Section 5: \(Q\)-learning algorithm
  - Video 7: Q-learning
  - Coding exercise 6: Implement Q-learning
  - Section 6: \(\epsilon\)-greedy exploitation
  - Video 8: Epsilon-greedy exploration
  - Coding exercise 7: Implement epsilon-greedy exploration
  - Summary


## W3D5 — Advanced Reinforcement Learning And Deep Learning Discussion 3

### Tutorial 1: Deep Learning Discussion 3

- Source: <https://deeplearning.neuromatch.io/tutorials/W3D5_AdvancedReinforcementLearningAndDeepLearningDiscussion3/student/W3D5_Tutorial1.html>
- Sections:
  - Section 1: Intro to Deep Learning Discussion 3
  - Video 1: Intro to DL Discussion 3
  - Section 2: The Future
  - Video 2: The Future Vignette
  - Think! 1: The Future
  - Section 3: In-context Learning
  - Video 3: In-context Learning Vignette
  - Think! 2: In-context Learning
  - Section 4: Memories
  - Video 4: Memories Vignette
  - Think! 3: Memories
  - Section 5: Multiple Information Sources
  - Video 5: Multiple Information Sources Vignette
  - Think! 4: Multiple Information Sources
  - Section 6: Language for Robotics
  - Video 6: Language for Robotics Vignette
  - Think! 5: Language for Robotics
  - Summary

### Bonus Tutorial: Reinforcement Learning For Games

- Source: <https://deeplearning.neuromatch.io/tutorials/W3D5_AdvancedReinforcementLearningAndDeepLearningDiscussion3/student/W3D5_Tutorial2.html>
- Objectives:
  - Understand the format of two-players games, Othello specifically
  - Understand how to create random players
  - Understand how to implement a value-based player
  - Understand how to implement a policy-based player
  - Understand how to implement a player with Monte Carlo planner
- Sections:
  - Section 0: Introduction
  - Video 0: Introduction
  - Section 1: Create a game/agent loop for RL
  - Video 1: A game loop for RL
  - Section 1.1: Introduction to OthelloGame
  - Section 1.2: Create a random player
  - Coding Exercise 1.2: Implement a random player
  - Section 1.3: Compete random agents
  - Section 2: Train a value function from expert game data
  - Video 2: Train a value function
  - Section 2.1: Load expert data
  - Section 2.2: Define the Neural Network Architecture for Othello
  - Coding Exercise 2.2: Implement OthelloNNet for playing Othello
  - Section 2.3: Define the Value network
  - Coding Exercise 2.3: Implement the ValueNetwork
  - Section 2.4: Train the value network and observe the MSE loss progress
  - Section 2.5: Use a trained value network to play games
  - Video 3: Play games using a value function
  - Coding Exercise 2.5: Implement the Value-based player
  - Section 3: Train a policy network from expert game data
  - Video 4: Train a policy network
  - Section 3.1: Define the Policy network
  - Coding Exercise 3.1: Implement the PolicyNetwork
  - Section 3.2: Train the policy network
  - Section 3.3: Use a trained policy network to play games
  - Video 6: Play games using a policy network
  - Coding Exercise 3.3: Implement the PolicyBasedPlayer
  - Section 4: Player comparisons
  - Comparing a sampling-based policy based player versus a random player
  - Compare greedy policy based player versus value based player
  - Compare greedy policy based player versus sampling-based policy player
  - Section 5: Plan using Monte Carlo Rollouts
  - Video 7: Play using Monte-Carlo rollouts
  - Load in trained value and policy networks
  - Section 5.1: Define the Monte Carlo planner
  - Coding Exercise 5.1: Implement the MonteCarlo planner
  - Section 5.2: Use Monte Carlo simulations to play games
  - Video 8: Play with planning
  - Coding Exercise 5.2: Monte-Carlo simulations
  - Monte-Carlo player against Value-based player
  - Monte-Carlo player against Policy-based player
  - Section 6: Ethical aspects
  - Video 9: Unbeatable opponents
  - Summary
  - Video 19: Outro


## Bonus — Deploy Models (Bonus)

### Bonus Tutorial: Deploying Neural Networks on the Web

- Source: <https://deeplearning.neuromatch.io/tutorials/Bonus_DeployModels/student/Bonus_Tutorial1.html>
- Objectives:
  - Serve web pages with Flask
  - Apply the MVVM design pattern to write maintainable code
  - Create an interactive UI for your service
  - Deploy your deep learning models as a REST API
  - Deploying your application on Heroku
- Sections:
  - Section 1: Introduction
  - Video 1: Deploying Neural Networks on the Web
  - Section 2: Flask
  - Section 2.1: Your First Flask App
  - Video 2: Flask
  - Section 2.2: Using Jinja2 Templates
  - Video 3: Jinja Templates
  - Section 2.3: Apply the MVVM Design Pattern
  - Video 4: Using the MVVM Design Pattern
  - Section 2.4: Creating a REST API
  - Video 5: REST API
  - Section 3: Vue.js
  - Video 6: Vue.js
  - Section 3.1: Defining the Vue Template
  - Section 3.2: Serving the Vue.js App
  - Section 4: Model Presentation
  - Video 7: Deploying a PyTorch model
  - Section 4.1: Image Classification API
  - Video 8: Classification with a Pre-trained Model
  - Section 4.2: Create a Dynamic Application
  - Video 9: Create a Dynamic Application
  - Section 5: Deploy a Flask app on Heroku
  - Video 10: Deploy on Heroku
  - Section 5.1: Preparing Your Environment
  - Video 11: Prepare Python Environment
  - Section 5.2: Create Your Application
  - Video 12: Creating a Local Application
  - Section 5.3: Testing Your Application Locally
  - Section 5.4: Preparing for Deployment on Heroku
  - Video 13: Preparing for Heroku
  - Section 5.5: Deploying on Heroku
  - Video 14: Deploying on Heroku
  - Summary
  - Video 15: Summary
