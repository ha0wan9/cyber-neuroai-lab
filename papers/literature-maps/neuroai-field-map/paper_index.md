# Paper Index — NeuroAI Field Map

> 179 篇中心去重索引。条目按首次出现顺序分配稳定 ID；同一论文跨领域时只保留一个 ID，并合并领域标签。详细 top-k 语境见三个 `fields-*.md` 文件。

| ID | Fields | Citation and lineage role |
|---|---|---|
| P001 | Cybernetics | Rosenblueth, Wiener & Bigelow (1943), [“Behavior, Purpose and Teleology”](https://doi.org/10.1086/286788), *Philosophy of Science* — 把反馈、目的与行为连成控制论纲领。 |
| P002 | Cybernetics | McCulloch & Pitts (1943), [“A Logical Calculus of the Ideas Immanent in Nervous Activity”](https://doi.org/10.1007/BF02478259), *Bulletin of Mathematical Biophysics* — 神经活动作为逻辑计算的共同根。 |
| P003 | Cybernetics | Wiener (1948), [*Cybernetics: Or Control and Communication in the Animal and the Machine*](https://doi.org/10.7551/mitpress/11810.001.0001), MIT Press — 定名并整合反馈、通信、控制与生物系统。 |
| P004 | Cybernetics | Ashby (1956), [*An Introduction to Cybernetics*](https://doi.org/10.5962/bhl.title.5851), Chapman & Hall — 状态、稳定性、调节与必要多样性的系统化表述。 |
| P005 | Cybernetics | Conant & Ashby (1970), [“Every Good Regulator of a System Must Be a Model of That System”](https://doi.org/10.1080/00207727008920220), *International Journal of Systems Science* — 将有效调节与内部模型联系起来。 |
| P006 | Biologically inspired perception | Lettvin, Maturana, McCulloch & Pitts (1959), [“What the Frog’s Eye Tells the Frog’s Brain”](https://doi.org/10.1109/JRPROC.1959.287207), *Proceedings of the IRE* — 视网膜输出编码行为相关特征的经典证据。 |
| P007 | Biologically inspired perception | Hubel & Wiesel (1962), [“Receptive Fields, Binocular Interaction and Functional Architecture in the Cat’s Visual Cortex”](https://doi.org/10.1113/jphysiol.1962.sp006837), *Journal of Physiology* — 分层感受野与视觉皮层功能结构。 |
| P008 | Biologically inspired perception; CNNs | Fukushima (1980), [“Neocognitron”](https://doi.org/10.1007/BF00344251), *Biological Cybernetics* — 从简单/复杂细胞启发局部连接、层级与位移容忍；亦见 CNNs。 |
| P009 | Biologically inspired perception | Itti, Koch & Niebur (1998), [“A Model of Saliency-Based Visual Attention for Rapid Scene Analysis”](https://doi.org/10.1109/34.730558), *IEEE TPAMI* — 可运行的多尺度视觉显著性模型。 |
| P010 | Biologically inspired perception; CNNs → ventral stream; Using neuro data to realign AI | Yamins et al. (2014), [“Performance-Optimized Hierarchical Models Predict Neural Responses in Higher Visual Cortex”](https://doi.org/10.1073/pnas.1403112111), *PNAS* — 任务优化 CNN 与腹侧视觉流预测的桥梁；亦见领域 29、31。 |
| P011 | Hebbian learning | Hebb (1949), [*The Organization of Behavior*](https://www.routledge.com/The-Organization-of-Behavior-A-Neuropsychological-Theory/Hebb/p/book/9780805843002), Wiley — 细胞集与共同激活增强联结的原始纲领。 |
| P012 | Hebbian learning | Bliss & Lømo (1973), [“Long-Lasting Potentiation of Synaptic Transmission…”](https://doi.org/10.1113/jphysiol.1973.sp010273), *Journal of Physiology* — 长期增强的经典生理证据。 |
| P013 | Hebbian learning | Bienenstock, Cooper & Munro (1982), [“Theory for the Development of Neuron Selectivity”](https://doi.org/10.1523/JNEUROSCI.02-01-00032.1982), *Journal of Neuroscience* — BCM 滑动阈值修正简单 Hebbian 规则的不稳定性。 |
| P014 | Hebbian learning | Oja (1982), [“Simplified Neuron Model as a Principal Component Analyzer”](https://doi.org/10.1007/BF00275687), *Journal of Mathematical Biology* — 归一化 Hebbian 更新得到 PCA 并控制权重增长。 |
| P015 | Hebbian learning | Bi & Poo (1998), [“Synaptic Modifications in Cultured Hippocampal Neurons…”](https://doi.org/10.1523/JNEUROSCI.18-24-10464.1998), *Journal of Neuroscience* — STDP 时间窗的经典实验曲线。 |
| P016 | Cognitive architectures | Laird, Newell & Rosenbloom (1987), [“SOAR: An Architecture for General Intelligence”](https://doi.org/10.1016/0004-3702(87)90050-6), *Artificial Intelligence* — 问题空间、产生式规则与 chunking 的统一架构。 |
| P017 | Cognitive architectures | Newell (1990), [*Unified Theories of Cognition*](https://www.hup.harvard.edu/books/9780674921016), Harvard University Press — 以统一架构约束碎片化心理理论的纲领。 |
| P018 | Cognitive architectures | Meyer & Kieras (1997), [“A Computational Theory of Executive Cognitive Processes… Part 1”](https://doi.org/10.1037/0033-295X.104.1.3), *Psychological Review* — EPIC 把执行控制机制连接到多任务行为。 |
| P019 | Cognitive architectures | Anderson et al. (2004), [“An Integrated Theory of the Mind”](https://doi.org/10.1037/0033-295X.111.4.1036), *Psychological Review* — ACT-R 模块、缓冲区与产生式学习的综合陈述。 |
| P020 | Cognitive architectures | Langley, Laird & Rogers (2009), [“Cognitive Architectures: Research Issues and Challenges”](https://doi.org/10.1016/j.cogsys.2006.07.004), *Cognitive Systems Research* — 架构应解释的能力与评估难题。 |
| P021 | MLPs | Werbos (1974), [*Beyond Regression*](https://ntrs.nasa.gov/citations/19900001211), Harvard PhD thesis — 反向传播用于多层网络的关键早期形式化。 |
| P022 | MLPs; Parallel distributed processing | Rumelhart, Hinton & Williams (1986), [“Learning Representations by Back-Propagating Errors”](https://doi.org/10.1038/323533a0), *Nature* — 多层隐藏表征学习的决定性普及；亦见 PDP。 |
| P023 | MLPs | Cybenko (1989), [“Approximation by Superpositions of a Sigmoidal Function”](https://doi.org/10.1007/BF02551274), *Mathematics of Control, Signals and Systems* — 单隐层 sigmoid 网络的通用逼近定理。 |
| P024 | MLPs; Theoretical deep learning | Hornik, Stinchcombe & White (1989), [“Multilayer Feedforward Networks Are Universal Approximators”](https://doi.org/10.1016/0893-6080(89)90020-8), *Neural Networks* — 澄清通用逼近来自架构能力；亦见理论深度学习。 |
| P025 | MLPs | Hinton, Osindero & Teh (2006), [“A Fast Learning Algorithm for Deep Belief Nets”](https://doi.org/10.1162/neco.2006.18.7.1527), *Neural Computation* — 逐层预训练重启深层前馈网络研究，后来被更直接优化路线取代。 |
| P026 | Perceptrons | Rosenblatt (1958), [“The Perceptron”](https://doi.org/10.1037/h0042519), *Psychological Review* — 可学习线性阈值分类器及其神经解释的起点。 |
| P027 | Perceptrons | Block (1962), [“The Perceptron: A Model for Brain Functioning. I”](https://doi.org/10.1103/RevModPhys.34.123), *Reviews of Modern Physics* — 早期权威能力分析。 |
| P028 | Perceptrons | Minsky & Papert (1969), [*Perceptrons*](https://mitpress.mit.edu/9780262631112/perceptrons/), MIT Press — 单层 perceptron 的表达限制；不能外推成“多层网络不可能”。 |
| P029 | Perceptrons | Gallant (1990), [“Perceptron-Based Learning Algorithms”](https://doi.org/10.1109/72.80230), *IEEE Transactions on Neural Networks* — 学习算法与收敛性质的推广。 |
| P030 | Perceptrons | Freund & Schapire (1999), [“Large Margin Classification Using the Perceptron Algorithm”](https://doi.org/10.1023/A:1007662407062), *Machine Learning* — voted perceptron 与大间隔泛化的连接。 |
| P031 | Parallel distributed processing | McClelland & Rumelhart (1981), [“An Interactive Activation Model of Context Effects in Letter Perception”](https://doi.org/10.1037/0033-295X.88.5.375), *Psychological Review* — 分布式双向激活解释知觉上下文效应。 |
| P032 | Parallel distributed processing | Rumelhart, McClelland & PDP Research Group (1986), [*Parallel Distributed Processing, Vol. 1*](https://mitpress.mit.edu/9780262680530/parallel-distributed-processing/), MIT Press — PDP 的核心语言、模型族与研究纲领。 |
| P033 | Parallel distributed processing; Recurrent neural networks | Elman (1990), [“Finding Structure in Time”](https://doi.org/10.1207/s15516709cog1402_1), *Cognitive Science* — 将 PDP 扩展到时间结构；亦见 RNN。 |
| P034 | Parallel distributed processing | Plaut et al. (1996), [“Understanding Normal and Impaired Word Reading”](https://doi.org/10.1037/0033-295X.103.1.56), *Psychological Review* — PDP 对正常阅读、损伤模式与准规则映射的统一解释。 |
| P035 | Catastrophic forgetting | McCloskey & Cohen (1989), [“Catastrophic Interference in Connectionist Networks”](https://doi.org/10.1016/S0079-7421(08)60536-8), *Psychology of Learning and Motivation* — 顺序学习灾难性干扰的问题定义。 |
| P036 | Catastrophic forgetting | Ratcliff (1990), [“Connectionist Models of Recognition Memory”](https://doi.org/10.1037/0033-295X.97.2.285), *Psychological Review* — 独立展示新学习破坏旧表征及 rehearsal 的作用。 |
| P037 | Catastrophic forgetting | French (1999), [“Catastrophic Forgetting in Connectionist Networks”](https://doi.org/10.1016/S1364-6613(99)01294-2), *Trends in Cognitive Sciences* — 早期机制与解决路线的经典综合。 |
| P038 | Catastrophic forgetting | Kirkpatrick et al. (2017), [“Overcoming Catastrophic Forgetting in Neural Networks”](https://doi.org/10.1073/pnas.1611835114), *PNAS* — EWC 把突触巩固转成参数重要性正则。 |
| P039 | Catastrophic forgetting | Lopez-Paz & Ranzato (2017), [“Gradient Episodic Memory for Continual Learning”](https://proceedings.neurips.cc/paper/2017/hash/f87522788a2be2d171666752f97ddebb-Abstract.html), *NeurIPS* — episodic replay 与梯度约束的重要基线。 |
| P040 | Recurrent neural networks; Computation through dynamics | Hopfield (1982), [“Neural Networks and Physical Systems with Emergent Collective Computational Abilities”](https://doi.org/10.1073/pnas.79.8.2554), *PNAS* — 能量型循环网络与联想记忆；亦见动力学计算。 |
| P041 | Recurrent neural networks | Hochreiter & Schmidhuber (1997), [“Long Short-Term Memory”](https://doi.org/10.1162/neco.1997.9.8.1735), *Neural Computation* — 门控记忆缓解长期依赖与梯度问题。 |
| P042 | Recurrent neural networks | Cho et al. (2014), [“Learning Phrase Representations Using RNN Encoder–Decoder”](https://doi.org/10.3115/v1/D14-1179), *EMNLP* — GRU 与 encoder–decoder 序列建模。 |
| P043 | Recurrent neural networks | Sutskever, Vinyals & Le (2014), [“Sequence to Sequence Learning with Neural Networks”](https://proceedings.neurips.cc/paper_files/paper/2014/hash/a14ac55a4f27472c5d894ec1c3c743d2-Abstract.html), *NeurIPS* — 端到端 seq2seq 范式。 |
| P044 | CNNs | LeCun et al. (1998), [“Gradient-Based Learning Applied to Document Recognition”](https://doi.org/10.1109/5.726791), *Proceedings of the IEEE* — LeNet 的端到端训练与工程价值。 |
| P045 | CNNs | Krizhevsky, Sutskever & Hinton (2012), [“ImageNet Classification with Deep Convolutional Neural Networks”](https://arxiv.org/abs/1207.0580), *NeurIPS* — AlexNet 触发深度视觉的现代转折。 |
| P046 | CNNs | Simonyan & Zisserman (2015), [“Very Deep Convolutional Networks for Large-Scale Image Recognition”](https://arxiv.org/abs/1409.1556), *ICLR* — 小卷积核与深层堆叠的代表。 |
| P047 | CNNs | He et al. (2016), [“Deep Residual Learning for Image Recognition”](https://doi.org/10.1109/CVPR.2016.90), *CVPR* — 残差连接解决超深 CNN 优化退化。 |
| P048 | Predictive coding | Rao & Ballard (1999), [“Predictive Coding in the Visual Cortex”](https://doi.org/10.1038/4580), *Nature Neuroscience* — 现代层级预测误差模型的起点。 |
| P049 | Predictive coding | Friston & Kiebel (2009), [“Predictive Coding under the Free-Energy Principle”](https://doi.org/10.1098/rstb.2008.0300), *Philosophical Transactions B* — 预测编码进入变分自由能框架。 |
| P050 | Predictive coding | Bastos et al. (2012), [“Canonical Microcircuits for Predictive Coding”](https://doi.org/10.1016/j.neuron.2012.10.038), *Neuron* — 预测与误差信号的候选皮层微回路。 |
| P051 | Predictive coding | Lotter, Kreiman & Cox (2017), [“Deep Predictive Coding Networks for Video Prediction”](https://openreview.net/forum?id=B1ewdt9xe), *ICLR* — PredNet 将原则转为深度视频预测架构。 |
| P052 | Predictive coding; Biologically plausible backprop | Whittington & Bogacz (2017), [“An Approximation of the Error Backpropagation Algorithm in a Predictive Coding Network”](https://doi.org/10.1162/NECO_a_00949), *Neural Computation* — 连接预测编码、局部 Hebbian 学习与反向传播近似。 |
| P053 | Sparse coding | Olshausen & Field (1996), [“Emergence of Simple-Cell Receptive Field Properties by Learning a Sparse Code”](https://doi.org/10.1038/381607a0), *Nature* — 自然图像稀疏编码涌现 V1 类感受野。 |
| P054 | Sparse coding | Lewicki & Sejnowski (2000), [“Learning Overcomplete Representations”](https://doi.org/10.1162/089976600300015826), *Neural Computation* — 过完备字典与概率解释。 |
| P055 | Sparse coding | Rozell et al. (2008), [“Sparse Coding via Thresholding and Local Competition in Neural Circuits”](https://doi.org/10.1162/neco.2008.03-07-486), *Neural Computation* — 局部竞争式稀疏推断动力学。 |
| P056 | Sparse coding | Mairal et al. (2010), [“Online Learning for Matrix Factorization and Sparse Coding”](https://www.jmlr.org/papers/v11/mairal10a.html), *JMLR* — 大规模在线字典学习的标准算法。 |
| P057 | Sparse coding | Gregor & LeCun (2010), [“Learning Fast Approximations of Sparse Coding”](https://proceedings.mlr.press/v9/gregor10a.html), *ICML* — LISTA 开启迭代优化展开路线。 |
| P058 | Reinforcement learning | Sutton (1988), [“Learning to Predict by the Methods of Temporal Differences”](https://doi.org/10.1007/BF00115009), *Machine Learning* — TD 学习与在线预测。 |
| P059 | Reinforcement learning | Watkins & Dayan (1992), [“Q-Learning”](https://doi.org/10.1007/BF00992698), *Machine Learning* — 无模型、离策略最优控制更新。 |
| P060 | Reinforcement learning | Williams (1992), [“Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning”](https://doi.org/10.1007/BF00992696), *Machine Learning* — REINFORCE 与蒙特卡洛策略梯度。 |
| P061 | Reinforcement learning | Mnih et al. (2015), [“Human-Level Control through Deep Reinforcement Learning”](https://doi.org/10.1038/nature14236), *Nature* — DQN 结合深度表征、经验回放与 Q-learning。 |
| P062 | Reinforcement learning | Schulman et al. (2017), [“Proximal Policy Optimization Algorithms”](https://arxiv.org/abs/1707.06347), technical paper — 现代策略优化的简单稳定基线。 |
| P063 | Reservoir computing | Jaeger (2001), [“The ‘Echo State’ Approach to Analysing and Training Recurrent Neural Networks”](https://www.ai.rug.nl/minds/uploads/EchoStatesTechRep.pdf), GMD Technical Report 148 — Echo State Network 与只训练读出层的核心范式。 |
| P064 | Reservoir computing | Maass, Natschläger & Markram (2002), [“Real-Time Computing Without Stable States”](https://doi.org/10.1162/089976602760407955), *Neural Computation* — Liquid State Machine 与脉冲型 reservoir。 |
| P065 | Reservoir computing | Jaeger & Haas (2004), [“Harnessing Nonlinearity”](https://doi.org/10.1126/science.1091277), *Science* — 混沌预测与通信任务的实用验证。 |
| P066 | Reservoir computing | Verstraeten et al. (2007), [“An Experimental Unification of Reservoir Computing Methods”](https://doi.org/10.1016/j.neunet.2007.04.003), *Neural Networks* — ESN、LSM 等方法的统一比较。 |
| P067 | Reservoir computing | Lukoševičius & Jaeger (2009), [“Reservoir Computing Approaches to Recurrent Neural Network Training”](https://doi.org/10.1016/j.cosrev.2009.03.005), *Computer Science Review* — 训练方法、稳定性条件与主要变体的综合。 |
| P068 | Neuromorphic computing | Mead (1990), [“Neuromorphic Electronic Systems”](https://doi.org/10.1109/5.58356), *Proceedings of the IEEE* — 奠定类脑电子系统研究纲领。 |
| P069 | Neuromorphic computing | Merolla et al. (2014), [“A Million Spiking-Neuron Integrated Circuit…”](https://doi.org/10.1126/science.1254642), *Science* — TrueNorth 百万神经元芯片代表作。 |
| P070 | Neuromorphic computing | Davies et al. (2018), [“Loihi: A Neuromorphic Manycore Processor with On-Chip Learning”](https://doi.org/10.1109/MM.2018.112130359), *IEEE Micro* — 片上可塑性与异步脉冲计算平台。 |
| P071 | Spiking neural networks | Maass (1997), [“Networks of Spiking Neurons: The Third Generation of Neural Network Models”](https://doi.org/10.1016/S0893-6080(97)00011-7), *Neural Networks* — SNN 作为“第三代网络”的经典定义。 |
| P072 | Spiking neural networks | Bohte, Kok & La Poutré (2002), [“Error-Backpropagation in Temporally Encoded Networks of Spiking Neurons”](https://doi.org/10.1016/S0925-2312(01)00658-0), *Neurocomputing* — SpikeProp 与早期监督时序学习。 |
| P073 | Spiking neural networks | Bellec et al. (2020), [“A Solution to the Learning Dilemma for Recurrent Networks of Spiking Neurons”](https://doi.org/10.1038/s41467-020-17236-y), *Nature Communications* — e-prop 的局部、在线信用分配。 |
| P074 | Free-energy principle | Friston (2005), [“A Theory of Cortical Responses”](https://doi.org/10.1098/rstb.2005.1622), *Philosophical Transactions B* — 预测编码、变分推断与皮层响应的连接。 |
| P075 | Free-energy principle | Friston (2010), [“The Free-Energy Principle: A Unified Brain Theory?”](https://doi.org/10.1038/nrn2787), *Nature Reviews Neuroscience* — FEP 最有影响力的统一性陈述。 |
| P076 | Free-energy principle | Friston et al. (2017), [“Active Inference: A Process Theory”](https://doi.org/10.1162/NECO_a_00912), *Neural Computation* — 主动推断的感知—行动过程理论。 |
| P077 | Hierarchical temporal memory | George & Hawkins (2009), [“Towards a Mathematical Theory of Cortical Micro-circuits”](https://doi.org/10.1371/journal.pcbi.1000532), *PLOS Computational Biology* — 早期 HTM/皮层层级模型的概率与微回路形式化。 |
| P078 | Hierarchical temporal memory | Ahmad & Hawkins (2015), [“Properties of Sparse Distributed Representations…”](https://arxiv.org/abs/1503.07469), arXiv — HTM 的稀疏分布式表示基础。 |
| P079 | Hierarchical temporal memory | Cui, Ahmad & Hawkins (2016), [“Continuous Online Sequence Learning…”](https://doi.org/10.1162/NECO_a_00893), *Neural Computation* — temporal memory 的连续在线序列学习实现。 |
| P080 | Animats and hybrots | Wilson (1985), [“Knowledge Growth in an Artificial Animal”](https://dl.acm.org/doi/10.5555/645511.657141), *First International Conference on Genetic Algorithms* — animat 人工动物与适应性行为的早期标志。 |
| P081 | Animats and hybrots | DeMarse et al. (2001), [“The Neurally Controlled Animat”](https://doi.org/10.1023/A:1012407611130), *Autonomous Robots* — 培养神经元与虚拟身体形成闭环。 |
| P082 | Animats and hybrots | Warwick et al. (2010), [“Controlling a Mobile Robot with a Biological Brain”](https://doi.org/10.14429/dsj.60.14), *Defence Science Journal* — 活体培养神经网络控制实体移动机器人。 |
| P083 | Neuro-inspired XAI | Olds et al. (2019), [“Explainable AI: A Neurally-Inspired Decision Stack Framework”](https://arxiv.org/abs/1908.10300), arXiv — 以神经系统层级启发可解释决策栈。 |
| P084 | Neuro-inspired XAI | Olah et al. (2020), [“Zoom In: An Introduction to Circuits”](https://doi.org/10.23915/distill.00024.001), *Distill* — 类神经回路分析的 mechanistic-interpretability 范式。 |
| P085 | Neuro-inspired XAI | Kar, Kornblith & Fedorenko (2022), [“Interpretability of Artificial Neural Network Models in AI vs. Neuroscience”](https://arxiv.org/abs/2206.03951), arXiv — 澄清 AI 与神经科学解释目标的共同点和边界。 |
| P086 | Computation through dynamics | Churchland et al. (2012), [“Neural Population Dynamics During Reaching”](https://doi.org/10.1038/nature11129), *Nature* — 运动皮层旋转群体动力学的关键证据。 |
| P087 | Computation through dynamics | Sussillo & Barak (2013), [“Opening the Black Box”](https://doi.org/10.1162/NECO_a_00409), *Neural Computation* — 用固定点与低维动力学解释高维训练后 RNN。 |
| P088 | Neurons as multi-layered ANNs; Dendrites | Poirazi, Brannon & Mel (2003), [“Pyramidal Neuron as Two-Layer Neural Network”](https://doi.org/10.1016/S0896-6273(03)00149-1), *Neuron* — 树突子单元使单神经元表现为两层网络。 |
| P089 | Neurons as multi-layered ANNs | Gidon et al. (2020), [“Dendritic Action Potentials and Computation in Human Layer 2/3 Cortical Neurons”](https://doi.org/10.1126/science.aax6239), *Science* — 人类皮层树突中的非线性计算。 |
| P090 | Neurons as multi-layered ANNs | Beniaguev, Segev & London (2021), [“Single Cortical Neurons as Deep Artificial Neural Networks”](https://doi.org/10.1016/j.neuron.2021.07.002), *Neuron* — 用深层 ANN 拟合详细生物物理神经元。 |
| P091 | Dendrites | London & Häusser (2005), [“Dendritic Computation”](https://doi.org/10.1146/annurev.neuro.28.061604.135703), *Annual Review of Neuroscience* — 树突计算的权威综合框架。 |
| P092 | Dendrites | Branco, Clark & Häusser (2010), [“Dendritic Discrimination of Temporal Input Sequences”](https://doi.org/10.1126/science.1189664), *Science* — 树突判别输入时序的实验展示。 |
| P093 | Biologically plausible backprop | Lillicrap et al. (2016), [“Random Synaptic Feedback Weights Support Error Backpropagation”](https://doi.org/10.1038/ncomms13276), *Nature Communications* — feedback alignment 绕开权重传输问题。 |
| P094 | Biologically plausible backprop | Sacramento et al. (2018), [“Dendritic Cortical Microcircuits Approximate the Backpropagation Algorithm”](https://arxiv.org/abs/1810.11393), *NeurIPS* — 树突分区与皮层微回路的近似信用分配。 |
| P095 | Neurogenesis | Wiskott, Rasch & Kempermann (2006), [“A Functional Hypothesis for Adult Hippocampal Neurogenesis”](https://doi.org/10.1002/hipo.20167), *Hippocampus* — 神经发生缓解齿状回灾难性干扰的假说。 |
| P096 | Neurogenesis | Aimone, Wiles & Gage (2009), [“Computational Influence of Adult Neurogenesis on Memory Encoding”](https://doi.org/10.1016/j.neuron.2008.11.026), *Neuron* — 模式分离、时间编码与记忆的计算综合。 |
| P097 | Neurogenesis | Draelos et al. (2016), [“Neurogenesis Deep Learning”](https://arxiv.org/abs/1612.03770), arXiv — 神经元增生转译为网络结构增长与持续学习。 |
| P098 | Whole-brain emulation | Sandberg & Bostrom (2008), [“Whole Brain Emulation: A Roadmap”](https://gwern.net/doc/ai/scaling/hardware/2008-sandberg-wholebrainemulationroadmap.pdf), FHI Technical Report 2008-3 — 扫描、建模、算力和验证路径的系统拆解。 |
| P099 | Whole-brain emulation | Eliasmith et al. (2012), [“A Large-Scale Model of the Functioning Brain”](https://doi.org/10.1126/science.1225266), *Science* — Spaun 展示大规模脉冲脑模型整合多种认知任务。 |
| P100 | Whole-brain emulation | Markram et al. (2015), [“Reconstruction and Simulation of Neocortical Microcircuitry”](https://doi.org/10.1016/j.cell.2015.09.029), *Cell* — 数据约束皮层微回路重建与仿真的里程碑。 |
| P101 | Neurosymbolic architectures | Smolensky (1990), [“Tensor Product Variable Binding and the Representation of Symbolic Structures in Connectionist Systems”](https://doi.org/10.1016/0004-3702(90)90007-M), *Artificial Intelligence* — 分布式向量与组合符号结构的数学桥梁。 |
| P102 | Neurosymbolic architectures | Towell & Shavlik (1994), [“Knowledge-Based Artificial Neural Networks”](https://doi.org/10.1016/0004-3702(94)90105-8), *Artificial Intelligence* — 逻辑知识初始化网络后用梯度细化。 |
| P103 | Neurosymbolic architectures | Rocktäschel & Riedel (2017), [“End-to-End Differentiable Proving”](https://proceedings.neurips.cc/paper/2017/hash/b2ab001909a8a6f04b51920306046ce5-Abstract.html), *NeurIPS* — 后向链与合一的可微实现。 |
| P104 | Neurosymbolic architectures | Manhaeve et al. (2018), [“DeepProbLog”](https://arxiv.org/abs/1805.10872), *NeurIPS* — 神经感知与概率逻辑程序语义的整合。 |
| P105 | Neurosymbolic architectures | Mao et al. (2019), [“The Neuro-Symbolic Concept Learner”](https://openreview.net/forum?id=rJgMlhRctm), *ICLR* — 对象中心视觉推理、概念学习与可执行程序。 |
| P106 | Intuitive physics | Baillargeon (1987), [“Object Permanence in 3½- and 4½-Month-Old Infants”](https://doi.org/10.1037/0012-1649.23.5.655), *Developmental Psychology* — 早期物理知识的 violation-of-expectation 证据。 |
| P107 | Intuitive physics | Battaglia, Hamrick & Tenenbaum (2013), [“Simulation as an Engine of Physical Scene Understanding”](https://doi.org/10.1073/pnas.1306572110), *PNAS* — 人类直觉物理作为近似概率模拟。 |
| P108 | Intuitive physics | Lerer, Gross & Fergus (2016), [“Learning Physical Intuition of Block Towers by Example”](https://proceedings.mlr.press/v48/lerer16.html), *ICML* — 学习视觉稳定性判断与 sim-to-real。 |
| P109 | Intuitive physics | Battaglia et al. (2016), [“Interaction Networks for Learning about Objects, Relations and Physics”](https://proceedings.neurips.cc/paper/2016/hash/3147da8ab4a0437c15ef51a5cc7f2dc4-Abstract.html), *NeurIPS* — 对象—关系消息传递作为可学习物理引擎。 |
| P110 | Intuitive physics | Bear et al. (2021), [“Physion”](https://arxiv.org/abs/2106.08261), *NeurIPS Datasets & Benchmarks* — 暴露人类与模型物理预测差距的 benchmark 纠偏。 |
| P111 | Neural Turing machines | Graves, Wayne & Danihelka (2014), [“Neural Turing Machines”](https://arxiv.org/abs/1410.5401), technical report — 可微内容/位置寻址外部记忆的起点。 |
| P112 | Neural Turing machines | Weston, Chopra & Bordes (2015), [“Memory Networks”](https://arxiv.org/abs/1410.3916), *ICLR* — 面向问答的并行外部记忆路线。 |
| P113 | Neural Turing machines | Joulin & Mikolov (2015), [“Inferring Algorithmic Patterns with Stack-Augmented Recurrent Nets”](https://proceedings.neurips.cc/paper/2015/hash/26657d5ff9020d2abefe558796b99584-Abstract.html), *NeurIPS* — 可微结构化记忆学习简单算法。 |
| P114 | Neural Turing machines | Sukhbaatar et al. (2015), [“End-To-End Memory Networks”](https://proceedings.neurips.cc/paper/2015/hash/8fb21ee7a2207526da55a679f0332de2-Abstract.html), *NeurIPS* — 去除强监督并引入多跳记忆注意。 |
| P115 | Neural Turing machines | Graves et al. (2016), [“Hybrid Computing Using a Neural Network with Dynamic External Memory”](https://doi.org/10.1038/nature20101), *Nature* — DNC 的分配、时间链接、图推理与控制任务。 |
| P116 | Consciousness in AI | Dehaene, Kerszberg & Changeux (1998), [“A Neuronal Model of a Global Workspace”](https://doi.org/10.1073/pnas.95.24.14529), *PNAS* — global-workspace 计算实现的神经科学根。 |
| P117 | Consciousness in AI | Shanahan (2006), [“A Cognitive Architecture That Combines Internal Simulation with a Global Workspace”](https://doi.org/10.1016/j.concog.2005.11.005), *Consciousness and Cognition* — 在模拟具身代理中实现 workspace 式访问。 |
| P118 | Consciousness in AI | Bengio (2017), [“The Consciousness Prior”](https://arxiv.org/abs/1709.08568), workshop paper — 将意识启发的稀疏高层状态选择转成 ML prior。 |
| P119 | Consciousness in AI | Dehaene, Lau & Kouider (2017), [“What Is Consciousness, and Could Machines Have It?”](https://doi.org/10.1126/science.aan8871), *Science* — 从意识理论到机器评估的框架。 |
| P120 | Consciousness in AI | Butlin et al. (2023), [“Consciousness in Artificial Intelligence”](https://arxiv.org/abs/2308.08708), technical report — 将多种理论转为计算指标，同时保留证据不确定性。 |
| P121 | Neural style transfer | Gatys, Ecker & Bethge (2016), [“Image Style Transfer Using Convolutional Neural Networks”](https://openaccess.thecvf.com/content_cvpr_2016/html/Gatys_Image_Style_Transfer_CVPR_2016_paper.html), *CVPR* — Gram 统计与优化式风格迁移的定型作。 |
| P122 | Neural style transfer | Johnson, Alahi & Fei-Fei (2016), [“Perceptual Losses for Real-Time Style Transfer”](https://arxiv.org/abs/1603.08155), *ECCV* — 迭代优化转为快速前馈感知损失训练。 |
| P123 | Neural style transfer | Huang & Belongie (2017), [“Arbitrary Style Transfer in Real-Time with Adaptive Instance Normalization”](https://openaccess.thecvf.com/content_iccv_2017/html/Huang_Arbitrary_Style_Transfer_ICCV_2017_paper.html), *ICCV* — 通过特征统计对齐实现未见风格迁移。 |
| P124 | Neural style transfer | Li et al. (2017), [“Universal Style Transfer via Feature Transforms”](https://arxiv.org/abs/1705.08086), *NeurIPS* — whitening/coloring transform 的通用路线。 |
| P125 | Neural style transfer | Deng et al. (2022), [“StyTr²”](https://openaccess.thecvf.com/content/CVPR2022/html/Deng_StyTr2_Image_Style_Transfer_With_Transformers_CVPR_2022_paper.html), *CVPR* — Transformer 对全局内容—风格依赖的重构。 |
| P126 | CNNs → ventral stream | Riesenhuber & Poggio (1999), [“Hierarchical Models of Object Recognition in Cortex”](https://doi.org/10.1038/14819), *Nature Neuroscience* — HMAX 与腹侧视觉层级模型前身。 |
| P127 | CNNs → ventral stream | Khaligh-Razavi & Kriegeskorte (2014), [“Deep Supervised, but Not Unsupervised, Models May Explain IT”](https://doi.org/10.1371/journal.pcbi.1003915), *PLOS Computational Biology* — 比较监督/非监督模型并展示剩余 IT 结构。 |
| P128 | CNNs → ventral stream; Using neuro data to realign AI | Schrimpf et al. (2018), [“Brain-Score”](https://doi.org/10.1101/407007), bioRxiv — 神经与行为相似性的可扩展 benchmark。 |
| P129 | CNNs → ventral stream | Kar et al. (2019), [“Evidence That Recurrent Circuits Are Critical to the Ventral Stream…”](https://doi.org/10.1038/s41593-019-0392-5), *Nature Neuroscience* — 对纯前馈 CNN 解释的关键纠偏。 |
| P130 | Attention | Broadbent (1958), [*Perception and Communication*](https://doi.org/10.1037/10037-000), Pergamon — 早期选择/过滤理论。 |
| P131 | Attention | Treisman & Gelade (1980), [“A Feature-Integration Theory of Attention”](https://doi.org/10.1016/0010-0285(80)90005-5), *Cognitive Psychology* — 注意在视觉特征绑定中的作用。 |
| P132 | Attention | Desimone & Duncan (1995), [“Neural Mechanisms of Selective Visual Attention”](https://doi.org/10.1146/annurev.ne.18.030195.001205), *Annual Review of Neuroscience* — biased competition 的综合。 |
| P133 | Attention | Mnih et al. (2014), [“Recurrent Models of Visual Attention”](https://proceedings.neurips.cc/paper_files/paper/2014/hash/3e456b31302cf8210edd4029292a40ad-Abstract.html), *NeurIPS* — 强化学习控制序列视觉 glimpse。 |
| P134 | Attention | Bahdanau, Cho & Bengio (2015), [“Neural Machine Translation by Jointly Learning to Align and Translate”](https://arxiv.org/abs/1409.0473), *ICLR* — 序列模型中的可微软对齐。 |
| P135 | Attention | Vaswani et al. (2017), [“Attention Is All You Need”](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need), *NeurIPS* — self-attention 成为核心计算架构。 |
| P136 | Attention | Jain & Wallace (2019), [“Attention Is Not Explanation”](https://doi.org/10.18653/v1/N19-1357), *NAACL* — 注意权重不必是忠实解释的纠偏。 |
| P137 | Attention | Dao et al. (2022), [“FlashAttention”](https://proceedings.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract.html), *NeurIPS* — IO-aware 精确注意的系统级转折。 |
| P138 | Using neuro data to realign AI | Li et al. (2019), [“Learning from Brains How to Regularize Machines”](https://proceedings.neurips.cc/paper/2019/hash/70117ee3c0b15a2950f1e82a215e812b-Abstract.html), *NeurIPS* — 以小鼠视觉表征作鲁棒性正则。 |
| P139 | Using neuro data to realign AI | Safarani et al. (2021), [“Towards Robust Vision by Multi-Task Learning on Monkey Visual Cortex”](https://proceedings.neurips.cc/paper/2021/hash/06a9d51e04213572ef0720dd27a84792-Abstract.html), *NeurIPS* — 联合神经预测与分类迁移 V1 相关鲁棒性。 |
| P140 | Using neuro data to realign AI | Dapello et al. (2023), [“Aligning Model and Macaque IT Cortex Representations…”](https://openreview.net/forum?id=SMYdcXjJh1q), *ICLR* — 直接对齐改善行为与对抗鲁棒性，但收益受神经训练类别覆盖限制。 |
| P141 | Self-supervised learning (Barlow Twins) | Barlow (1961), [“Possible Principles Underlying the Transformation of Sensory Messages”](https://www.cns.nyu.edu/pub/lcv/barlow-1961.pdf), in *Sensory Communication* — Barlow Twins 直接继承的冗余约简原则。 |
| P142 | Self-supervised learning (Barlow Twins) | Vincent et al. (2008), [“Extracting and Composing Robust Features with Denoising Autoencoders”](https://doi.org/10.1145/1390156.1390294), *ICML* — corruption/reconstruction 的无标签表征路线。 |
| P143 | Self-supervised learning (Barlow Twins) | van den Oord, Li & Vinyals (2018), [“Representation Learning with Contrastive Predictive Coding”](https://arxiv.org/abs/1807.03748), arXiv — InfoNCE 与预测式对比学习。 |
| P144 | Self-supervised learning (Barlow Twins) | Chen et al. (2020), [“A Simple Framework for Contrastive Learning of Visual Representations”](https://proceedings.mlr.press/v119/chen20j.html), *ICML* — SimCLR 定型增强驱动的视觉对比学习。 |
| P145 | Self-supervised learning (Barlow Twins) | Grill et al. (2020), [“Bootstrap Your Own Latent”](https://arxiv.org/abs/2006.07733), *NeurIPS* — 无显式负样本的 teacher–student SSL。 |
| P146 | Self-supervised learning (Barlow Twins) | Zbontar et al. (2021), [“Barlow Twins”](https://proceedings.mlr.press/v139/zbontar21a.html), *ICML* — 以 cross-correlation 实现冗余约简并避免 collapse。 |
| P147 | Self-supervised learning (Barlow Twins) | He et al. (2022), [“Masked Autoencoders Are Scalable Vision Learners”](https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper.html), *CVPR* — 可扩展 masked-reconstruction 分支。 |
| P148 | Self-supervised learning (Barlow Twins) | Assran et al. (2023), [“Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture”](https://arxiv.org/abs/2301.08243), *CVPR* — JEPA 的表征空间预测重构。 |
| P149 | Geometry of learning | Amari (1998), [“Natural Gradient Works Efficiently in Learning”](https://doi.org/10.1162/089976698300017746), *Neural Computation* — 参数流形上的自然梯度。 |
| P150 | Geometry of learning | Dauphin et al. (2014), [“Identifying and Attacking the Saddle Point Problem…”](https://proceedings.neurips.cc/paper_files/paper/2014/hash/04192426585542c54b96ba14445be996-Abstract.html), *NeurIPS* — 从坏局部极小转向高维鞍点问题。 |
| P151 | Geometry of learning | Ollivier (2015), [“Riemannian Metrics for Neural Networks I”](https://arxiv.org/abs/1303.0818), *Information and Inference* — 系统化度量与 natural-gradient 类更新。 |
| P152 | Geometry of learning | Garipov et al. (2018), [“Loss Surfaces, Mode Connectivity, and Fast Ensembling”](https://proceedings.neurips.cc/paper/2018/hash/be3087e74e9100d4bc4c6268cdbe8456-Abstract.html), *NeurIPS* — 低损失路径连接表面不同的最优点。 |
| P153 | Geometry of learning | Li et al. (2018), [“Visualizing the Loss Landscape of Neural Nets”](https://proceedings.neurips.cc/paper_files/paper/2018/hash/a41b3bb3e6b050b6c9067c67f663b915-Abstract.html), *NeurIPS* — filter normalization 修正失真的景观可视化。 |
| P154 | Theoretical deep learning | Glorot & Bengio (2010), [“Understanding the Difficulty of Training Deep Feedforward Neural Networks”](https://proceedings.mlr.press/v9/glorot10a.html), *AISTATS* — 激活/初始化统计与可训练性。 |
| P155 | Theoretical deep learning | Montúfar et al. (2014), [“On the Number of Linear Regions of Deep Neural Networks”](https://arxiv.org/abs/1402.1869), *NeurIPS* — 深度带来的分段线性表达能力。 |
| P156 | Theoretical deep learning | Zhang et al. (2017), [“Understanding Deep Learning Requires Rethinking Generalization”](https://openreview.net/forum?id=Sy8gdB9xx), *ICLR* — 对经典容量解释的决定性经验挑战。 |
| P157 | Theoretical deep learning | Jacot, Gabriel & Hongler (2018), [“Neural Tangent Kernel”](https://proceedings.neurips.cc/paper/2018/hash/5a4be1fa34e62bb8a6ec6b91d2462f5a-Abstract.html), *NeurIPS* — 无限宽极限下的核训练动力学。 |
| P158 | Theoretical deep learning | Belkin et al. (2019), [“Reconciling Modern ML Practice and the Classical Bias–Variance Trade-Off”](https://doi.org/10.1073/pnas.1903070116), *PNAS* — double descent 与插值泛化。 |
| P159 | Theoretical deep learning | Kaplan et al. (2020), [“Scaling Laws for Neural Language Models”](https://arxiv.org/abs/2001.08361), technical report — 模型、数据、计算的经验幂律。 |
| P160 | Theoretical deep learning | Hoffmann et al. (2022), [“Training Compute-Optimal Large Language Models”](https://arxiv.org/abs/2203.15556), *NeurIPS* — 以模型和 token 联合优化修正参数偏重的 scaling 配方。 |
| P161 | Neuroconnectionism | Yamins & DiCarlo (2016), [“Using Goal-Driven Deep Learning Models to Understand Sensory Cortex”](https://doi.org/10.1038/nn.4244), *Nature Neuroscience* — task-driven ANN 作为可证伪脑模型的典型前身。 |
| P162 | Neuroconnectionism | Doerig et al. (2023), [“The Neuroconnectionist Research Programme”](https://doi.org/10.1038/s41583-023-00705-w), *Nature Reviews Neuroscience* — 定义标签及 ANN-as-modeling-language 纲领。 |
| P163 | Neuroconnectionism | Bowers et al. (2023), [“Deep Problems with Neural Network Models of Human Vision”](https://doi.org/10.1017/S0140525X22002813), *Behavioral and Brain Sciences* — 必要的对抗性观点：预测 benchmark 不自动等于共同机制。 |
| P164 | Geometric deep learning | Gori, Monfardini & Scarselli (2005), [“A New Model for Learning in Graph Domains”](https://doi.org/10.1109/IJCNN.2005.1555942), *IJCNN* — 早期循环图神经网络形式化。 |
| P165 | Geometric deep learning | Bruna et al. (2014), [“Spectral Networks and Locally Connected Networks on Graphs”](https://arxiv.org/abs/1312.6203), *ICLR* — 现代谱图卷积起点。 |
| P166 | Geometric deep learning | Cohen & Welling (2016), [“Group Equivariant Convolutional Networks”](https://proceedings.mlr.press/v48/cohenc16.html), *ICML* — 群等变 CNN 的对称性分支。 |
| P167 | Geometric deep learning | Defferrard, Bresson & Vandergheynst (2016), [“Convolutional Neural Networks on Graphs…”](https://arxiv.org/abs/1606.09375), *NeurIPS* — Chebyshev 滤波使谱卷积局部高效。 |
| P168 | Geometric deep learning | Kipf & Welling (2017), [“Semi-Supervised Classification with Graph Convolutional Networks”](https://openreview.net/forum?id=SJU4ayYgl), *ICLR* — 简化 GCN 并推动广泛采用。 |
| P169 | Geometric deep learning | Gilmer et al. (2017), [“Neural Message Passing for Quantum Chemistry”](https://proceedings.mlr.press/v70/gilmer17a.html), *ICML* — 统一 message passing 并打开科学应用分支。 |
| P170 | Geometric deep learning | Fuchs et al. (2020), [“SE(3)-Transformers”](https://arxiv.org/abs/2006.10503), *NeurIPS* — attention 与连续三维等变性。 |
| P171 | Geometric deep learning | Bronstein et al. (2021), [“Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges”](https://arxiv.org/abs/2104.13478), monograph — 统一图、流形、群与 gauge 结构的领域综合。 |
| P172 | Embodied intelligence & embodied Turing test | Turing (1950), [“Computing Machinery and Intelligence”](https://doi.org/10.1093/mind/LIX.236.433), *Mind* — 后来从会话扩展到传感运动能力的行为测试根。 |
| P173 | Embodied intelligence & embodied Turing test | Brooks (1991), [“Intelligence without Representation”](https://doi.org/10.1016/0004-3702(91)90053-M), *Artificial Intelligence* — situated/reactive/world-coupled intelligence 对离身符号规划的挑战。 |
| P174 | Embodied intelligence & embodied Turing test | Bongard, Zykov & Lipson (2006), [“Resilient Machines Through Continuous Self-Modeling”](https://doi.org/10.1126/science.1133687), *Science* — 形态、自模型与损伤适应的实验。 |
| P175 | Embodied intelligence & embodied Turing test | Ha & Schmidhuber (2018), [“World Models”](https://arxiv.org/abs/1803.10122), arXiv — 学习紧凑动力学模型用于具身控制。 |
| P176 | Embodied intelligence & embodied Turing test | Ichter et al. (2023), [“Do As I Can, Not As I Say”](https://proceedings.mlr.press/v205/ichter23a.html), *CoRL* — SayCan 用机器人 affordance 约束语言计划。 |
| P177 | Embodied intelligence & embodied Turing test | Driess et al. (2023), [“PaLM-E”](https://proceedings.mlr.press/v202/driess23a.html), *ICML* — 具身多模态 foundation model。 |
| P178 | Embodied intelligence & embodied Turing test | Zador et al. (2023), [“Catalyzing Next-Generation Artificial Intelligence Through NeuroAI”](https://doi.org/10.1038/s41467-023-37180-x), *Nature Communications* — 提出动物相对的 embodied Turing test 作为 NeuroAI 挑战。 |
| P179 | Embodied intelligence & embodied Turing test | Garimella et al. (2024), [“A Newborn Embodied Turing Test…”](https://openreview.net/forum?id=qhkEOCcVX9), *ICLR* — 匹配饲养环境的可操作 benchmark 与新生动物—机器泛化差距。 |

## Conventions

- ID 永不重编号；新增文献从 P180 开始。
- 领域标签是集合，不代表论文作者使用了该标签。
- 句末中文说明是策展解释；可核验事实以链接落地页为准。
