# Softmax + Cross-Entropy 的数学性质

Date: 2026-07-14  
Source: 公式推导与文末参考资料  
Status: structured

## 1. 核心问题

为什么多分类模型通常把 softmax 和 cross-entropy 组合使用？这个组合在概率、几何、优化与数值计算上分别提供了什么性质，又有哪些容易忽略的退化方向和边界行为？

## 2. 一句话总结

Softmax + cross-entropy 把 logits 变成 categorical 分布并进行最大似然学习；合并后单样本损失是一个线性项加 `log-sum-exp`，所以对 logits 凸、梯度恰为“预测概率减目标概率”、Hessian 是 categorical 协方差矩阵，同时具有整体平移不变性。

## 3. 定义与合并形式

设类别数为 $K$，模型输出 logits

$$
z=(z_1,\ldots,z_K)\in\mathbb R^K.
$$

Softmax 给出概率

$$
p_i=\operatorname{softmax}(z)_i
=\frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}.
$$

令目标分布为 $q\in\Delta^{K-1}$，其中 $q_i\ge 0$ 且 $\sum_iq_i=1$。它可以是 one-hot 标签，也可以是软标签。交叉熵为

$$
\mathcal L(z;q)
=-\sum_i q_i\log p_i.
$$

把 softmax 代入并利用 $\sum_i q_i=1$：

$$
\boxed{
\mathcal L(z;q)
=\log\sum_j e^{z_j}-q^\top z
}
$$

这就是整个组合最重要的代数化简。若真实类别为 $t$，即 $q=e_t$，则

$$
\mathcal L(z;t)
=-\log p_t
=\log\sum_j e^{z_j}-z_t
=\log\left(1+\sum_{j\ne t}e^{z_j-z_t}\right).
$$

最后一个形式说明：损失只关心真实类别与其他类别之间的相对 margin，而不关心 logits 的绝对零点。

## 4. 概率性质

### 4.1 它就是 categorical 负对数似然

把 $p(z)$ 看成 categorical 模型，观察到类别 $t$ 的似然为 $p_t$，负对数似然就是 $-\log p_t$。因此在数据集上最小化该损失等价于最大化条件对数似然。

### 4.2 Cross-entropy = 不可约熵 + KL 散度

对真实条件分布 $q$，有

$$
H(q,p)
=H(q)+D_{\mathrm{KL}}(q\Vert p).
$$

其中 $H(q)$ 与预测 $p$ 无关，而且 $D_{\mathrm{KL}}\ge 0$，故期望损失在且仅在 $p=q$ 时达到最小值。这使 log loss 成为一个严格适当评分规则：若模型族和数据足够理想，如实输出真实概率分布是总体风险的唯一最优预测。

需要区分：

- 这是关于总体期望风险和概率预测的结论，不自动保证有限样本或过参数神经网络已经校准。
- Softmax 用有限 logits 只能表示单纯形内部的分布；只要目标 $q$ 含零分量（one-hot 是极端情形），最优目标就在边界上，只能由部分 logit 差趋于无穷来逼近。
- 类别加权、重采样和某些非标准标签平滑会改变模型实际拟合的目标分布或风险，因此概率解释也随之改变。

### 4.3 它是指数族的规范形式

Categorical 分布是指数族，logits 是自然参数，

$$
A(z)=\log\sum_j e^{z_j}
$$

是 log-partition function。于是

$$
\nabla A(z)=p,
\qquad
\mathcal L(z;q)=A(z)-q^\top z.
$$

所以 softmax 不是随意选择的归一化函数：它正是 log-partition 对自然参数的梯度。

## 5. 一阶性质：梯度为什么是 $p-q$

Softmax 的 Jacobian 为

$$
\frac{\partial p_i}{\partial z_j}
=p_i(\delta_{ij}-p_j),
$$

而合并损失直接给出

$$
\boxed{
\nabla_z\mathcal L=p-q
}.
$$

对 one-hot 标签：

$$
\frac{\partial\mathcal L}{\partial z_t}=p_t-1,
\qquad
\frac{\partial\mathcal L}{\partial z_j}=p_j\quad(j\ne t).
$$

这有几个直接含义：

1. 梯度是一个“概率残差”，并且各分量之和为零。
2. 梯度下降会提高真实类 logit，并按当前错误概率压低其他 logits。
3. 对极度自信但错误的样本，$p_t\to0$ 时真实类方向的梯度趋近 $-1$，不会因为 softmax 自身饱和而消失。这是联合求导相较于把 softmax 与平方误差机械串联的重要优势。
4. 对已经极度自信且正确的样本，$p_t\to1$ 时梯度趋近零；易样本自然被降权。
5. one-hot 情形下 $\|p-q\|_2\le\sqrt 2$，因此单样本对 logits 的梯度有界；但损失本身在 $p_t\to0$ 时无界。

若上一层为线性分类头 $z=Wh+b$，则

$$
\nabla_W\mathcal L=(p-q)h^\top,
\qquad
\nabla_h\mathcal L=W^\top(p-q).
$$

这说明输出误差信号的结构很简单，但传到表示层后的方向仍由分类头 $W$ 决定。

## 6. 二阶性质：Hessian、凸性与 Fisher 信息

再次求导：

$$
\boxed{
\nabla_z^2\mathcal L
=\operatorname{diag}(p)-pp^\top
}.
$$

它与目标 $q$ 无关，并且正是 one-hot categorical 随机向量的协方差矩阵。对任意 $v\in\mathbb R^K$，

$$
v^\top\nabla^2\mathcal L\,v
=\sum_i p_i v_i^2-\left(\sum_i p_i v_i\right)^2
=\operatorname{Var}_{i\sim p}(v_i)\ge0.
$$

因此：

- 损失对 logits 是凸函数。
- Hessian 同时也是该 categorical 模型在自然参数坐标下的 Fisher 信息矩阵。
- 当所有 $p_i>0$ 时，Hessian 的秩为 $K-1$，零空间为 $\operatorname{span}\{\mathbf1\}$。
- 在完整 $K$ 维 logits 参数化中，最大特征值不超过 $1/2$，所以 logits 梯度在欧氏范数下是 $1/2$-Lipschitz。不要把它和单一 binary logit 的二阶导上界 $1/4$ 混淆；两者使用的坐标不同。

“对 logits 凸”不等于“对整个神经网络参数凸”。若 $z=f_\theta(x)$ 是深网络输出，$\mathcal L(f_\theta(x),q)$ 通常仍然对 $\theta$ 非凸。若 $z=Wx+b$ 是线性模型，则得到凸的多项 logistic regression，但仍可能因参数冗余或数据秩不足而不严格凸。

## 7. 对称性与不可辨识性

对任意常数 $c$，

$$
\operatorname{softmax}(z+c\mathbf1)=\operatorname{softmax}(z),
$$

从而

$$
\mathcal L(z+c\mathbf1;q)=\mathcal L(z;q).
$$

因此绝对 logit 水平不可辨识，只有差值有意义。这解释了：

- Hessian 必然有一个沿 $\mathbf1$ 的零特征值；
- 损失对完整 logits 不可能严格凸；
- 可固定一个参考类 logit 为零，或施加 $\sum_i z_i=0$，得到无冗余坐标；
- 数值计算时可以任意减去最大 logit，而不改变答案。

## 8. 熵对偶与最大熵视角

Log-sum-exp 的凸共轭在概率单纯形上是负熵。等价地，

$$
\log\sum_i e^{z_i}
=\max_{p\in\Delta^{K-1}}
\left(p^\top z+H(p)\right),
$$

且唯一最优解为 $p=\operatorname{softmax}(z)$。

这个公式给 softmax 一个很有用的解释：它在偏好高分数 $p^\top z$ 与保持高熵 $H(p)$ 之间做精确权衡。Softmax 不是 hard argmax，而是熵正则化的 argmax。

引入温度 $T>0$：

$$
p_i(T)=\frac{e^{z_i/T}}{\sum_j e^{z_j/T}}.
$$

- $T\to0^+$ 时趋近 hard argmax（并列最大值时在并列项上分配质量）。
- $T\to\infty$ 时趋近均匀分布。
- 若损失仍为 $-q^\top\log p(T)$，则 $\nabla_z\mathcal L=(p-q)/T$，Hessian 为 $\left(\operatorname{diag}(p)-pp^\top\right)/T^2$。

温度既改变概率锐度，也缩放梯度和曲率，不能只把它理解成可视化参数。

## 9. Margin、边界行为与隐式偏置

对真实类别 $t$，定义成对 margin $m_j=z_t-z_j$。则

$$
\mathcal L
=\log\left(1+\sum_{j\ne t}e^{-m_j}\right).
$$

由此可见：

- 任一错误类接近或超过真实类时，损失显著；
- 所有 margins 增大时，损失以指数尾部趋近零；
- one-hot 标签下，零损失通常只在 margins 趋向无穷时达到极限。

因此，在线性可分数据上，无正则的 logistic/softmax 回归可能没有有限参数范数的损失最小点：训练损失继续下降，权重范数继续增大，而分类边界可能已经稳定。已有理论表明，在特定线性可分设定下，梯度下降的方向会趋向某个最大间隔解；这一结论有明确假设，不能不加条件地外推到任意深网络。

## 10. 数值稳定性

不要先计算巨大或极小的 $e^{z_i}$，再取 softmax 和对数。利用平移不变性，令 $m=\max_i z_i$：

$$
\log\sum_i e^{z_i}
=m+\log\sum_i e^{z_i-m}.
$$

于是 one-hot 损失稳定地写成

$$
\mathcal L
=m+\log\sum_i e^{z_i-m}-z_t.
$$

工程上应将原始 logits 直接交给融合实现，例如 PyTorch 的 `CrossEntropyLoss`；它在数学上等价于 `LogSoftmax` 后接 `NLLLoss`。不要在它之前额外应用 softmax，因为这既改变输入语义，也丢掉融合计算的数值优势。

## 11. 这个组合的优点与代价

### 优点

- 有清晰的最大似然与概率预测解释。
- 对预测概率是严格适当的评分规则。
- 对 logits 凸，梯度和 Hessian 都有简洁闭式。
- 对自信但错误的样本产生强纠错信号。
- 与 log-sum-exp 融合后数值稳定。
- 梯度是预测统计量与目标统计量的差，这与指数族最大似然的一般结构一致。

### 代价与失败模式

- 对自信错误的预测惩罚无界，因此对错标样本和异常样本可能很敏感。
- one-hot 目标持续推动 margins 变大，可能促成过度自信和 logit/权重范数增长。
- 类别不平衡时，平均交叉熵可能主要优化多数类风险。
- Softmax 强制类别互斥；它适合单标签多分类，不适合多个标签可同时为真的任务，后者通常使用逐类 sigmoid + binary cross-entropy。
- 概率归一化带来类别耦合：抬高一个类会相对压低其他类。
- 一个低 cross-entropy 的深网不因此获得生物学合理性；目标函数、数据、架构和优化过程都共同塑造表示。

## 12. 与神经科学 / NeuroAI 的连接

**已建立的数学事实：** softmax 可表示带熵正则的竞争性归一化，cross-entropy 提供全局监督误差信号。

**有用的建模类比：** softmax 中的指数增益和除法归一化，可以帮助讨论竞争、归一化与概率群体编码；温度可以类比选择随机性或响应增益。

**需要警惕的外推：** 这些数学相似性不证明大脑显式计算 softmax、交叉熵或反向传播的 $p-q$。在 NeuroAI 比较中，应把它们视为功能级计算假设，而不是已确认的生物机制。

一个更有辨识力的问题是：脑—模型表征对齐来自任务标签、cross-entropy 的概率几何、softmax 的竞争归一化，还是训练数据与架构？仅比较最终准确率无法区分这些因素。

## 13. 最小实验建议

用一个三分类二维线性模型验证以下现象：

1. 数值检查自动微分梯度是否等于 $p-q$。
2. 计算 Hessian 特征值，验证其半正定、存在一个近零特征值，并检查对应方向接近 $\mathbf1$。
3. 给所有 logits 加同一常数，验证概率与损失不变。
4. 比较朴素 `softmax -> log` 与稳定 `logsumexp` 在极端 logits 下的结果。
5. 在线性可分数据上持续训练，分别画训练错误、损失、权重范数和最小 margin，观察错误率归零后损失与参数仍继续变化。
6. 比较 one-hot、label smoothing 和不同温度对概率熵、梯度范数与校准误差的影响。

## 14. 常见误解

1. **“Cross-entropy 的输入应该是 softmax 概率。”** 数学定义可以接收概率，但常见融合 API 接收 raw logits。
2. **“损失对 logits 凸，所以神经网络训练是凸优化。”** 复合上深网络后通常不是。
3. **“Hessian 半正定，所以它正定。”** 整体平移不变性至少产生一个零方向。
4. **“梯度 $p-y$ 说明 softmax 没有饱和。”** 自信错误时纠错信号不消失，但自信正确时梯度确实趋零。
5. **“最小化 cross-entropy 必然得到校准概率。”** 严格适当性是总体风险性质；有限数据、模型错设、分布偏移和优化都会破坏实际校准。
6. **“Softmax 输出是各类别独立概率。”** 它们之和为一，并通过归一化相互耦合。

## 15. 开放问题

1. Label smoothing 改善泛化时，主要作用来自有限目标 logits、梯度重分配，还是隐式正则化？
2. 在脑—模型比较中，更接近神经数据的是 cross-entropy、对比学习目标，还是带生物约束的局部目标？
3. 温度变化对 representation similarity 的影响来自最终 readout，还是会通过训练动力学改变隐藏表示？
4. 如何设计消融实验，将架构、训练目标、归一化与数据贡献分离？

## 16. 参考资料

- Boyd, S. & Vandenberghe, L. (2004). [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/). 参见 log-sum-exp 的凸性、Hessian 以及其与负熵的凸共轭关系。
- PyTorch. [CrossEntropyLoss documentation](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html). 参见 logits 输入、软标签，以及与 `LogSoftmax + NLLLoss` 的等价关系。
- Gneiting, T. & Raftery, A. E. (2007). [Strictly Proper Scoring Rules, Prediction, and Estimation](https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf). 参见 logarithmic score 的严格适当性。
- Soudry, D. et al. (2018). [The Implicit Bias of Gradient Descent on Separable Data](https://jmlr.org/papers/v19/18-188.html). 参见特定线性可分设定下 logistic/cross-entropy 损失、参数发散与最大间隔方向。
