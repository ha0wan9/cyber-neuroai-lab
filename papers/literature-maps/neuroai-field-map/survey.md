# NeuroAI 汇总图领域代表论文地图

> 版本：2026-07-14。AI 辅助生成的研究草案；论文元数据以 DOI、出版社、
> 官方 proceedings、PMLR、OpenReview 或 arXiv 页面核对。这里的 “top” 指
> 对理解领域谱系最有代表性，不等于按引用数或最新 benchmark 排名。

## §1 研究问题与结论

- 原图共有 **41 个框、40 个唯一标签**；“Neurons as multi-layered
  ANNs”在图中出现两次，本地图合并为一个领域，并同时保留算法级与细胞级含义。
- 共收录 **189 个论文×领域条目、179 篇去重文献**。跨领域核心论文复用同一
  `Pxxx` ID，例如 Fukushima 1980、Yamins 2014、Hopfield 1982、
  Whittington & Bogacz 2017。
- top-k 上限不是配额：领域越大，允许的谱系角色越多；若第 6 篇只是重复第 5 篇
  的作用，就停在 5 篇，不为填满上限而扩张。
- 原图混合了不同粒度：有完整生态（RL、CNN、attention），有单一架构族
  （HTM、Neural Turing Machines），也有研究纲领（FEP、neuroconnectionism、
  WBE）。因此不能给所有框同一个 k。

## §2 top-k 分配方法

每个领域按四个代理量分别打 0–2 分：**历史深度 / 社群与 venue 广度 /
方法分支 / 当前活跃度**。总分映射为：S=0–2 → cap 3，M=3–4 → cap 5，
L=5–6 → cap 8，XL=7–8 → cap 12。此处的分数是透明的策展估计，不是精确
的 bibliometric 计数。

| # | 原图领域 | 四项分数 | 规模 | k 上限 | 实收 n |
|---:|---|---|---|---:|---:|
| 1 | Cybernetics | 2/1/2/0 | L | 8 | 5 |
| 2 | Biologically inspired perception | 2/2/2/1 | XL | 12 | 5 |
| 3 | Hebbian learning | 2/2/2/1 | XL | 12 | 5 |
| 4 | Cognitive architectures | 2/1/2/1 | L | 8 | 5 |
| 5 | MLPs | 2/2/2/2 | XL | 12 | 5 |
| 6 | Perceptrons | 2/1/1/0 | M | 5 | 5 |
| 7 | Parallel distributed processing | 2/1/2/0 | L | 8 | 5 |
| 8 | Catastrophic forgetting | 2/2/2/2 | XL | 12 | 5 |
| 9 | Recurrent neural networks | 2/2/2/2 | XL | 12 | 5 |
| 10 | CNNs | 2/2/2/2 | XL | 12 | 5 |
| 11 | Neuromorphic computing | 2/2/2/2 | XL | 12 | 3 |
| 12 | Predictive coding | 2/2/2/2 | XL | 12 | 5 |
| 13 | Sparse coding | 2/2/2/1 | XL | 12 | 5 |
| 14 | Reinforcement learning | 2/2/2/2 | XL | 12 | 5 |
| 15 | Spiking neural networks | 2/2/2/2 | XL | 12 | 3 |
| 16 | Free-energy principle | 2/2/2/1 | XL | 12 | 3 |
| 17 | Reservoir computing | 1/2/2/2 | XL | 12 | 5 |
| 18 | Hierarchical temporal memory | 1/1/1/0 | M | 5 | 3 |
| 19 | Neurosymbolic architectures | 2/1/2/1 | L | 8 | 5 |
| 20 | Animats and hybrots | 1/1/0/0 | S | 3 | 3 |
| 21 | Neuro-inspired XAI | 1/1/1/1 | M | 5 | 3 |
| 22 | Intuitive physics | 1/1/2/2 | L | 8 | 5 |
| 23 | Neural Turing machines | 1/1/1/0 | M | 5 | 5 |
| 24 | Computation through dynamics | 2/2/2/2 | XL | 12 | 3 |
| 25 | Neurons as multi-layered ANNs | 1/1/1/1 | M | 5 | 3 |
| 26 | Dendrites | 2/2/2/2 | XL | 12 | 3 |
| 27 | Consciousness in AI | 1/1/1/1 | M | 5 | 5 |
| 28 | Neural style transfer | 1/2/2/1 | L | 8 | 5 |
| 29 | CNNs → ventral stream | 2/1/2/1 | L | 8 | 5 |
| 30 | Attention | 2/2/2/2 | XL | 12 | 8 |
| 31 | Using neuro data to realign AI | 1/1/1/1 | M | 5 | 5 |
| 32 | Self-supervised learning (Barlow Twins) | 2/2/2/2 | XL | 12 | 8 |
| 33 | Geometry of learning | 1/1/1/1 | M | 5 | 5 |
| 34 | Theoretical deep learning | 2/2/2/2 | XL | 12 | 8 |
| 35 | Biologically plausible backprop | 2/2/2/2 | XL | 12 | 3 |
| 36 | Neurogenesis | 2/1/1/0 | M | 5 | 3 |
| 37 | Neuroconnectionism | 0/1/0/1 | S | 3 | 3 |
| 38 | Geometric deep learning | 2/2/2/2 | XL | 12 | 8 |
| 39 | Embodied intelligence & embodied Turing test | 2/2/2/2 | XL | 12 | 8 |
| 40 | Whole-brain emulation | 1/1/1/0 | M | 5 | 3 |

## §3 分领域清单

- [I. 经典基础与连接主义](fields-classical.md)：领域 1–10、12–14、17
- [II. 生物机制、硬件与仿真](fields-biological.md)：领域 11、15–16、18、20–21、24–26、35–36、40
- [III. 现代认知、表示与架构](fields-modern.md)：领域 19、22–23、27–34、37–39
- [中心去重索引](paper_index.md)：稳定 `Pxxx` ID、跨领域复用关系与检索入口
- [覆盖审计](coverage_matrix.md) 与 [偏差审计](audits/bias-audit.md)

## §4 数据集与 benchmark：不适用

本调查回答的是“每个领域应从哪些论文建立谱系认识”，不是模型性能比较；因此没有
统一 dataset、metric 或 leaderboard 可列。若后续从本地图派生实验选型，应另建
任务—数据集—指标表，不能把论文的历史代表性当成实验效果证据。

## §5 Method-route comparison：两轴 taxonomy

原图本身的横轴是年代、纵轴近似 Marr 式抽象层级；为了避免只按年代理解，
本地图再加一条“知识流向”轴：

| 主轴：研究对象层级 | 典型领域 | 次轴：主要知识流向 |
|---|---|---|
| 理论/认知纲领 | Cybernetics, FEP, consciousness, cognitive architectures | brain/cognition → formal theory → AI |
| 学习与架构算法 | MLP, RNN, CNN, RL, attention, GDL, neurosymbolic | bidirectional 或 AI-internal |
| 神经机制 | Hebbian/STDP, predictive/sparse coding, dynamics, dendrites | brain → AI and AI → brain |
| 表征对齐 | CNN→ventral, Brain-Score, neuro-data realignment, neuroconnectionism | AI ↔ neural/behavioural data |
| 物理底座与闭环 | neuromorphic, SNN, hybrots, embodiment, WBE | biological substrate/world → engineered system |

按这两个轴看，P010、P052、P088、P128 等跨标签论文不是“重复”，而是不同
层级/流向之间的桥。

## §10 重要边界、争议与开放问题

1. **Self-supervised learning (Barlow Twins)**：按整个视觉 SSL 生态估计规模，
   但入选路线特意围绕 Barlow 的冗余约简思想，再取 contrastive、non-contrastive、
   masked prediction 和 JEPA 四条分支作对照。
2. **Geometry of learning ≠ geometric deep learning**：前者在这里指参数流形、
   loss landscape 与优化轨迹；后者指图、流形、群对称与等变网络。
3. **Attention** 同时包含认知/神经注意、可学习对齐与 Transformer self-attention；
   三者有谱系关联，但不是同一个机制。
4. **Neuro-inspired XAI** 仍是边界模糊的小领域；mechanistic interpretability
   与神经回路分析在方法上相似，不代表二者解释对象或证据标准相同。
5. **WBE** 必须与 whole-brain modelling 区分：后者可用于群体级动力学或认知模型，
   严格 WBE 要求对某一具体生物脑的功能相关结构进行足够精细的重建与运行。
6. **Consciousness indicators ≠ phenomenal consciousness evidence**：功能性指标或
   global-workspace 风格实现不能单独证明系统具有主观体验。

## §13 Recommended reading：建议阅读方式

第一次不要顺着 179 篇读完。先读每个感兴趣领域的第 1 篇（起点）与最后 1 篇
（转折/纠偏），再按问题回填中间机制。若目标是 NeuroAI 主线，推荐先走：

`Cybernetics → Hebbian learning → PDP/MLP → CNN/RNN → predictive & sparse coding
→ CNNs–ventral stream → computation through dynamics → neuro-data realignment
→ neuroconnectionism → embodied Turing test`。

### Entry tier（约 6–8 小时）

P002 → P011 → P022 → P040 → P008 → P048 → P010 → P135 → P162 → P178。

### Deep tier（按路线）

生物学习 P012–P015、P071–P076、P088–P094；现代架构 P101–P115、P141–P171；
具身与底座 P068–P082、P098–P100、P172–P179。

### Critical tier

P028、P037、P085、P110、P120、P129、P136、P140、P156、P163。

### Overview tier

P004、P020、P037、P067、P075、P091、P098、P120、P162、P171。

## §14 证据等级、复现性与限制

- 书籍、技术报告只在其确实是原始或领域定名来源时保留。
- 代表性判断是**策展解释**；论文的题名、作者、年份和 venue 才是可直接核验的事实。
- 古老领域天然偏向欧美经典机构；新领域天然偏向近年 ML 会议。偏差审计不把这种
  历史结构伪装成随机样本，而是明确记录。
- 这不是 PRISMA 式穷举系统综述，也不支持“漏掉的论文不重要”这一反向结论。
- 最终独立审稿没有逐个重新访问 179 个 landing URL；索引优先使用 DOI、出版社、
  官方 proceedings、PMLR、OpenReview 或 arXiv，但古老报告与外部存档仍可能发生 link rot。
- 未给 179 篇逐一分配 R1–R4 复现等级：本任务不比较准确率、速度或参数量，
  且大量奠基书籍/神经生理实验不适用现代代码仓库 rubric。若下一版用于实验选型，
  应只对候选实现论文另做代码、训练配方和第三方复现审计。

**Phase**: synthesize  **Survey**: neuroai-field-map  **Status**: synthesized; audit passed with documented limitations  **Next**: done
