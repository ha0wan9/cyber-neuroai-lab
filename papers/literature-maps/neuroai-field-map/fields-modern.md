# III. 现代认知、表示与架构

## 19. Neurosymbolic architectures — L，cap 8，n=5

- **[P101]** Smolensky (1990), [“Tensor Product Variable Binding and the Representation of Symbolic Structures in Connectionist Systems”](https://doi.org/10.1016/0004-3702(90)90007-M), *Artificial Intelligence* — 分布式向量与组合符号结构的数学桥梁。
- **[P102]** Towell & Shavlik (1994), [“Knowledge-Based Artificial Neural Networks”](https://doi.org/10.1016/0004-3702(94)90105-8), *Artificial Intelligence* — 逻辑知识初始化网络后用梯度细化。
- **[P103]** Rocktäschel & Riedel (2017), [“End-to-End Differentiable Proving”](https://proceedings.neurips.cc/paper/2017/hash/b2ab001909a8a6f04b51920306046ce5-Abstract.html), *NeurIPS* — 后向链与合一的可微实现。
- **[P104]** Manhaeve et al. (2018), [“DeepProbLog”](https://arxiv.org/abs/1805.10872), *NeurIPS* — 神经感知与概率逻辑程序语义的整合。
- **[P105]** Mao et al. (2019), [“The Neuro-Symbolic Concept Learner”](https://openreview.net/forum?id=rJgMlhRctm), *ICLR* — 对象中心视觉推理、概念学习与可执行程序。

## 22. Intuitive physics — L，cap 8，n=5

- **[P106]** Baillargeon (1987), [“Object Permanence in 3½- and 4½-Month-Old Infants”](https://doi.org/10.1037/0012-1649.23.5.655), *Developmental Psychology* — 早期物理知识的 violation-of-expectation 证据。
- **[P107]** Battaglia, Hamrick & Tenenbaum (2013), [“Simulation as an Engine of Physical Scene Understanding”](https://doi.org/10.1073/pnas.1306572110), *PNAS* — 人类直觉物理作为近似概率模拟。
- **[P108]** Lerer, Gross & Fergus (2016), [“Learning Physical Intuition of Block Towers by Example”](https://proceedings.mlr.press/v48/lerer16.html), *ICML* — 学习视觉稳定性判断与 sim-to-real。
- **[P109]** Battaglia et al. (2016), [“Interaction Networks for Learning about Objects, Relations and Physics”](https://proceedings.neurips.cc/paper/2016/hash/3147da8ab4a0437c15ef51a5cc7f2dc4-Abstract.html), *NeurIPS* — 对象—关系消息传递作为可学习物理引擎。
- **[P110]** Bear et al. (2021), [“Physion”](https://arxiv.org/abs/2106.08261), *NeurIPS Datasets & Benchmarks* — 暴露人类与模型物理预测差距的 benchmark 纠偏。

## 23. Neural Turing machines — M，cap 5，n=5

- **[P111]** Graves, Wayne & Danihelka (2014), [“Neural Turing Machines”](https://arxiv.org/abs/1410.5401), technical report — 可微内容/位置寻址外部记忆的起点。
- **[P112]** Weston, Chopra & Bordes (2015), [“Memory Networks”](https://arxiv.org/abs/1410.3916), *ICLR* — 面向问答的并行外部记忆路线。
- **[P113]** Joulin & Mikolov (2015), [“Inferring Algorithmic Patterns with Stack-Augmented Recurrent Nets”](https://proceedings.neurips.cc/paper/2015/hash/26657d5ff9020d2abefe558796b99584-Abstract.html), *NeurIPS* — 可微结构化记忆学习简单算法。
- **[P114]** Sukhbaatar et al. (2015), [“End-To-End Memory Networks”](https://proceedings.neurips.cc/paper/2015/hash/8fb21ee7a2207526da55a679f0332de2-Abstract.html), *NeurIPS* — 去除强监督并引入多跳记忆注意。
- **[P115]** Graves et al. (2016), [“Hybrid Computing Using a Neural Network with Dynamic External Memory”](https://doi.org/10.1038/nature20101), *Nature* — DNC 的分配、时间链接、图推理与控制任务。

**限制：** 这一命名架构族目前相对不活跃，其功能议程已部分被 Transformer、
retrieval 与工具调用系统吸收。

## 27. Consciousness in AI — M，cap 5，n=5

- **[P116]** Dehaene, Kerszberg & Changeux (1998), [“A Neuronal Model of a Global Workspace”](https://doi.org/10.1073/pnas.95.24.14529), *PNAS* — global-workspace 计算实现的神经科学根。
- **[P117]** Shanahan (2006), [“A Cognitive Architecture That Combines Internal Simulation with a Global Workspace”](https://doi.org/10.1016/j.concog.2005.11.005), *Consciousness and Cognition* — 在模拟具身代理中实现 workspace 式访问。
- **[P118]** Bengio (2017), [“The Consciousness Prior”](https://arxiv.org/abs/1709.08568), workshop paper — 将意识启发的稀疏高层状态选择转成 ML prior。
- **[P119]** Dehaene, Lau & Kouider (2017), [“What Is Consciousness, and Could Machines Have It?”](https://doi.org/10.1126/science.aan8871), *Science* — 从意识理论到机器评估的框架。
- **[P120]** Butlin et al. (2023), [“Consciousness in Artificial Intelligence”](https://arxiv.org/abs/2308.08708), technical report — 将多种理论转为计算指标，同时保留证据不确定性。

## 28. Neural style transfer — L，cap 8，n=5

- **[P121]** Gatys, Ecker & Bethge (2016), [“Image Style Transfer Using Convolutional Neural Networks”](https://openaccess.thecvf.com/content_cvpr_2016/html/Gatys_Image_Style_Transfer_CVPR_2016_paper.html), *CVPR* — Gram 统计与优化式风格迁移的定型作。
- **[P122]** Johnson, Alahi & Fei-Fei (2016), [“Perceptual Losses for Real-Time Style Transfer”](https://arxiv.org/abs/1603.08155), *ECCV* — 迭代优化转为快速前馈感知损失训练。
- **[P123]** Huang & Belongie (2017), [“Arbitrary Style Transfer in Real-Time with Adaptive Instance Normalization”](https://openaccess.thecvf.com/content_iccv_2017/html/Huang_Arbitrary_Style_Transfer_ICCV_2017_paper.html), *ICCV* — 通过特征统计对齐实现未见风格迁移。
- **[P124]** Li et al. (2017), [“Universal Style Transfer via Feature Transforms”](https://arxiv.org/abs/1705.08086), *NeurIPS* — whitening/coloring transform 的通用路线。
- **[P125]** Deng et al. (2022), [“StyTr²”](https://openaccess.thecvf.com/content/CVPR2022/html/Deng_StyTr2_Image_Style_Transfer_With_Transformers_CVPR_2022_paper.html), *CVPR* — Transformer 对全局内容—风格依赖的重构。

## 29. CNNs → ventral stream — L，cap 8，n=5

- **[P126]** Riesenhuber & Poggio (1999), [“Hierarchical Models of Object Recognition in Cortex”](https://doi.org/10.1038/14819), *Nature Neuroscience* — HMAX 与腹侧视觉层级模型前身。
- **[P010]** Yamins et al. (2014), [“Performance-Optimized Hierarchical Models…”](https://doi.org/10.1073/pnas.1403112111), *PNAS* — task optimization 预测高阶视觉神经反应。
- **[P127]** Khaligh-Razavi & Kriegeskorte (2014), [“Deep Supervised, but Not Unsupervised, Models May Explain IT”](https://doi.org/10.1371/journal.pcbi.1003915), *PLOS Computational Biology* — 比较监督/非监督模型并展示剩余 IT 结构。
- **[P128]** Schrimpf et al. (2018), [“Brain-Score”](https://doi.org/10.1101/407007), bioRxiv — 神经与行为相似性的可扩展 benchmark。
- **[P129]** Kar et al. (2019), [“Evidence That Recurrent Circuits Are Critical to the Ventral Stream…”](https://doi.org/10.1038/s41593-019-0392-5), *Nature Neuroscience* — 对纯前馈 CNN 解释的关键纠偏。

## 30. Attention — XL，cap 12，n=8

- **[P130]** Broadbent (1958), [*Perception and Communication*](https://doi.org/10.1037/10037-000), Pergamon — 早期选择/过滤理论。
- **[P131]** Treisman & Gelade (1980), [“A Feature-Integration Theory of Attention”](https://doi.org/10.1016/0010-0285(80)90005-5), *Cognitive Psychology* — 注意在视觉特征绑定中的作用。
- **[P132]** Desimone & Duncan (1995), [“Neural Mechanisms of Selective Visual Attention”](https://doi.org/10.1146/annurev.ne.18.030195.001205), *Annual Review of Neuroscience* — biased competition 的综合。
- **[P133]** Mnih et al. (2014), [“Recurrent Models of Visual Attention”](https://proceedings.neurips.cc/paper_files/paper/2014/hash/3e456b31302cf8210edd4029292a40ad-Abstract.html), *NeurIPS* — 强化学习控制序列视觉 glimpse。
- **[P134]** Bahdanau, Cho & Bengio (2015), [“Neural Machine Translation by Jointly Learning to Align and Translate”](https://arxiv.org/abs/1409.0473), *ICLR* — 序列模型中的可微软对齐。
- **[P135]** Vaswani et al. (2017), [“Attention Is All You Need”](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need), *NeurIPS* — self-attention 成为核心计算架构。
- **[P136]** Jain & Wallace (2019), [“Attention Is Not Explanation”](https://doi.org/10.18653/v1/N19-1357), *NAACL* — 注意权重不必是忠实解释的纠偏。
- **[P137]** Dao et al. (2022), [“FlashAttention”](https://proceedings.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract.html), *NeurIPS* — IO-aware 精确注意的系统级转折。

## 31. Using neuro data to realign AI — M，cap 5，n=5

- **[P010]** Yamins et al. (2014), [“Performance-Optimized Hierarchical Models…”](https://doi.org/10.1073/pnas.1403112111), *PNAS* — task performance 与 neural predictivity 的双向研究程序。
- **[P128]** Schrimpf et al. (2018), [“Brain-Score”](https://doi.org/10.1101/407007), bioRxiv — 把神经/行为对齐转为模型选择 benchmark。
- **[P138]** Li et al. (2019), [“Learning from Brains How to Regularize Machines”](https://proceedings.neurips.cc/paper/2019/hash/70117ee3c0b15a2950f1e82a215e812b-Abstract.html), *NeurIPS* — 以小鼠视觉表征作鲁棒性正则。
- **[P139]** Safarani et al. (2021), [“Towards Robust Vision by Multi-Task Learning on Monkey Visual Cortex”](https://proceedings.neurips.cc/paper/2021/hash/06a9d51e04213572ef0720dd27a84792-Abstract.html), *NeurIPS* — 联合神经预测与分类迁移 V1 相关鲁棒性。
- **[P140]** Dapello et al. (2023), [“Aligning Model and Macaque IT Cortex Representations…”](https://openreview.net/forum?id=SMYdcXjJh1q), *ICLR* — 直接对齐改善行为与对抗鲁棒性，但收益受神经训练类别覆盖限制。

## 32. Self-supervised learning (Barlow Twins) — XL，cap 12，n=8

- **[P141]** Barlow (1961), [“Possible Principles Underlying the Transformation of Sensory Messages”](https://www.cns.nyu.edu/pub/lcv/barlow-1961.pdf), in *Sensory Communication* — Barlow Twins 直接继承的冗余约简原则。
- **[P142]** Vincent et al. (2008), [“Extracting and Composing Robust Features with Denoising Autoencoders”](https://doi.org/10.1145/1390156.1390294), *ICML* — corruption/reconstruction 的无标签表征路线。
- **[P143]** van den Oord, Li & Vinyals (2018), [“Representation Learning with Contrastive Predictive Coding”](https://arxiv.org/abs/1807.03748), arXiv — InfoNCE 与预测式对比学习。
- **[P144]** Chen et al. (2020), [“A Simple Framework for Contrastive Learning of Visual Representations”](https://proceedings.mlr.press/v119/chen20j.html), *ICML* — SimCLR 定型增强驱动的视觉对比学习。
- **[P145]** Grill et al. (2020), [“Bootstrap Your Own Latent”](https://arxiv.org/abs/2006.07733), *NeurIPS* — 无显式负样本的 teacher–student SSL。
- **[P146]** Zbontar et al. (2021), [“Barlow Twins”](https://proceedings.mlr.press/v139/zbontar21a.html), *ICML* — 以 cross-correlation 实现冗余约简并避免 collapse。
- **[P147]** He et al. (2022), [“Masked Autoencoders Are Scalable Vision Learners”](https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper.html), *CVPR* — 可扩展 masked-reconstruction 分支。
- **[P148]** Assran et al. (2023), [“Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture”](https://arxiv.org/abs/2301.08243), *CVPR* — JEPA 的表征空间预测重构。

## 33. Geometry of learning — M，cap 5，n=5

这里采用“信息几何 + 参数/损失景观几何”的窄定义。

- **[P149]** Amari (1998), [“Natural Gradient Works Efficiently in Learning”](https://doi.org/10.1162/089976698300017746), *Neural Computation* — 参数流形上的自然梯度。
- **[P150]** Dauphin et al. (2014), [“Identifying and Attacking the Saddle Point Problem…”](https://proceedings.neurips.cc/paper_files/paper/2014/hash/04192426585542c54b96ba14445be996-Abstract.html), *NeurIPS* — 从坏局部极小转向高维鞍点问题。
- **[P151]** Ollivier (2015), [“Riemannian Metrics for Neural Networks I”](https://arxiv.org/abs/1303.0818), *Information and Inference* — 系统化度量与 natural-gradient 类更新。
- **[P152]** Garipov et al. (2018), [“Loss Surfaces, Mode Connectivity, and Fast Ensembling”](https://proceedings.neurips.cc/paper/2018/hash/be3087e74e9100d4bc4c6268cdbe8456-Abstract.html), *NeurIPS* — 低损失路径连接表面不同的最优点。
- **[P153]** Li et al. (2018), [“Visualizing the Loss Landscape of Neural Nets”](https://proceedings.neurips.cc/paper_files/paper/2018/hash/a41b3bb3e6b050b6c9067c67f663b915-Abstract.html), *NeurIPS* — filter normalization 修正失真的景观可视化。

## 34. Theoretical deep learning — XL，cap 12，n=8

- **[P024]** Hornik, Stinchcombe & White (1989), [“Multilayer Feedforward Networks Are Universal Approximators”](https://doi.org/10.1016/0893-6080(89)90020-8), *Neural Networks* — 表达能力的经典定理。
- **[P154]** Glorot & Bengio (2010), [“Understanding the Difficulty of Training Deep Feedforward Neural Networks”](https://proceedings.mlr.press/v9/glorot10a.html), *AISTATS* — 激活/初始化统计与可训练性。
- **[P155]** Montúfar et al. (2014), [“On the Number of Linear Regions of Deep Neural Networks”](https://arxiv.org/abs/1402.1869), *NeurIPS* — 深度带来的分段线性表达能力。
- **[P156]** Zhang et al. (2017), [“Understanding Deep Learning Requires Rethinking Generalization”](https://openreview.net/forum?id=Sy8gdB9xx), *ICLR* — 对经典容量解释的决定性经验挑战。
- **[P157]** Jacot, Gabriel & Hongler (2018), [“Neural Tangent Kernel”](https://proceedings.neurips.cc/paper/2018/hash/5a4be1fa34e62bb8a6ec6b91d2462f5a-Abstract.html), *NeurIPS* — 无限宽极限下的核训练动力学。
- **[P158]** Belkin et al. (2019), [“Reconciling Modern ML Practice and the Classical Bias–Variance Trade-Off”](https://doi.org/10.1073/pnas.1903070116), *PNAS* — double descent 与插值泛化。
- **[P159]** Kaplan et al. (2020), [“Scaling Laws for Neural Language Models”](https://arxiv.org/abs/2001.08361), technical report — 模型、数据、计算的经验幂律。
- **[P160]** Hoffmann et al. (2022), [“Training Compute-Optimal Large Language Models”](https://arxiv.org/abs/2203.15556), *NeurIPS* — 以模型和 token 联合优化修正参数偏重的 scaling 配方。

## 37. Neuroconnectionism — S，cap 3，n=3

- **[P161]** Yamins & DiCarlo (2016), [“Using Goal-Driven Deep Learning Models to Understand Sensory Cortex”](https://doi.org/10.1038/nn.4244), *Nature Neuroscience* — task-driven ANN 作为可证伪脑模型的典型前身。
- **[P162]** Doerig et al. (2023), [“The Neuroconnectionist Research Programme”](https://doi.org/10.1038/s41583-023-00705-w), *Nature Reviews Neuroscience* — 定义标签及 ANN-as-modeling-language 纲领。
- **[P163]** Bowers et al. (2023), [“Deep Problems with Neural Network Models of Human Vision”](https://doi.org/10.1017/S0140525X22002813), *Behavioral and Brain Sciences* — 必要的对抗性观点：预测 benchmark 不自动等于共同机制。

## 38. Geometric deep learning — XL，cap 12，n=8

- **[P164]** Gori, Monfardini & Scarselli (2005), [“A New Model for Learning in Graph Domains”](https://doi.org/10.1109/IJCNN.2005.1555942), *IJCNN* — 早期循环图神经网络形式化。
- **[P165]** Bruna et al. (2014), [“Spectral Networks and Locally Connected Networks on Graphs”](https://arxiv.org/abs/1312.6203), *ICLR* — 现代谱图卷积起点。
- **[P166]** Cohen & Welling (2016), [“Group Equivariant Convolutional Networks”](https://proceedings.mlr.press/v48/cohenc16.html), *ICML* — 群等变 CNN 的对称性分支。
- **[P167]** Defferrard, Bresson & Vandergheynst (2016), [“Convolutional Neural Networks on Graphs…”](https://arxiv.org/abs/1606.09375), *NeurIPS* — Chebyshev 滤波使谱卷积局部高效。
- **[P168]** Kipf & Welling (2017), [“Semi-Supervised Classification with Graph Convolutional Networks”](https://openreview.net/forum?id=SJU4ayYgl), *ICLR* — 简化 GCN 并推动广泛采用。
- **[P169]** Gilmer et al. (2017), [“Neural Message Passing for Quantum Chemistry”](https://proceedings.mlr.press/v70/gilmer17a.html), *ICML* — 统一 message passing 并打开科学应用分支。
- **[P170]** Fuchs et al. (2020), [“SE(3)-Transformers”](https://arxiv.org/abs/2006.10503), *NeurIPS* — attention 与连续三维等变性。
- **[P171]** Bronstein et al. (2021), [“Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges”](https://arxiv.org/abs/2104.13478), monograph — 统一图、流形、群与 gauge 结构的领域综合。

## 39. Embodied intelligence & embodied Turing test — XL，cap 12，n=8

- **[P172]** Turing (1950), [“Computing Machinery and Intelligence”](https://doi.org/10.1093/mind/LIX.236.433), *Mind* — 后来从会话扩展到传感运动能力的行为测试根。
- **[P173]** Brooks (1991), [“Intelligence without Representation”](https://doi.org/10.1016/0004-3702(91)90053-M), *Artificial Intelligence* — situated/reactive/world-coupled intelligence 对离身符号规划的挑战。
- **[P174]** Bongard, Zykov & Lipson (2006), [“Resilient Machines Through Continuous Self-Modeling”](https://doi.org/10.1126/science.1133687), *Science* — 形态、自模型与损伤适应的实验。
- **[P175]** Ha & Schmidhuber (2018), [“World Models”](https://arxiv.org/abs/1803.10122), arXiv — 学习紧凑动力学模型用于具身控制。
- **[P176]** Ichter et al. (2023), [“Do As I Can, Not As I Say”](https://proceedings.mlr.press/v205/ichter23a.html), *CoRL* — SayCan 用机器人 affordance 约束语言计划。
- **[P177]** Driess et al. (2023), [“PaLM-E”](https://proceedings.mlr.press/v202/driess23a.html), *ICML* — 具身多模态 foundation model。
- **[P178]** Zador et al. (2023), [“Catalyzing Next-Generation Artificial Intelligence Through NeuroAI”](https://doi.org/10.1038/s41467-023-37180-x), *Nature Communications* — 提出动物相对的 embodied Turing test 作为 NeuroAI 挑战。
- **[P179]** Garimella et al. (2024), [“A Newborn Embodied Turing Test…”](https://openreview.net/forum?id=qhkEOCcVX9), *ICLR* — 匹配饲养环境的可操作 benchmark 与新生动物—机器泛化差距。

[返回总览](survey.md)
