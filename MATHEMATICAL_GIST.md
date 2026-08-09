# The Mathematical Gist of AI Archaeology

This is the book's mathematical spine in discovery order. It is not a
formula sheet. Every entry keeps the concrete work and the explanation
of each term before allowing notation to compress the idea.

Use it after reading an excavation, or to revisit the chain of
mathematical inventions without rereading the entire narrative.

**57 equation-bearing excavations · 64 displayed equations**

## Map

- [Excavation 002 — Vectors](#excavation-002-vectors)
- [Excavation 003 — Distance](#excavation-003-distance)
- [Excavation 004 — Vectors as Change](#excavation-004-vectors-as-change)
- [Excavation 005 — Matrices](#excavation-005-matrices)
- [Excavation 007 — A Place for Meaning to Live](#excavation-007-a-place-for-meaning-to-live)
- [Excavation 009 — From Scores to Attention](#excavation-009-from-scores-to-attention)
- [Excavation 010 — Query, Key, and Value](#excavation-010-query-key-and-value)
- [Excavation 011 — Multi-Head Attention](#excavation-011-multi-head-attention)
- [Excavation 012 — Feed-Forward Networks](#excavation-012-feed-forward-networks)
- [Excavation 013 — Residual Connections](#excavation-013-residual-connections)
- [Excavation 014 — Layer Normalization](#excavation-014-layer-normalization)
- [Excavation 015 — How a Dead Brain Learns](#excavation-015-how-a-dead-brain-learns)
- [Excavation 017 — Probability — Counting What We Do Not Know](#excavation-017-probability-counting-what-we-do-not-know)
- [Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?](#excavation-018-likelihood-which-hidden-story-produced-this-evidence)
- [Excavation 019 — Information — Why Surprise Needs a Number](#excavation-019-information-why-surprise-needs-a-number)
- [Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation](#excavation-020-entropy-measuring-the-uncertainty-of-a-whole-situation)
- [Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions](#excavation-021-cross-entropy-paying-for-confidently-wrong-predictions)
- [Excavation 022 — Derivatives — Asking One Weight What It Changed](#excavation-022-derivatives-asking-one-weight-what-it-changed)
- [Excavation 023 — The Chain Rule — Following One Change Through Many Machines](#excavation-023-the-chain-rule-following-one-change-through-many-machines)
- [Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It](#excavation-024-backpropagation-reusing-blame-instead-of-recomputing-it)
- [Excavation 025 — Gradient Descent — Teaching a Tiny Network](#excavation-025-gradient-descent-teaching-a-tiny-network)
- [Excavation 026 — Mini-Batches — Learning from More Than One Example](#excavation-026-mini-batches-learning-from-more-than-one-example)
- [Excavation 027 — Learning Rate — How Large Should the Next Step Be?](#excavation-027-learning-rate-how-large-should-the-next-step-be)
- [Excavation 028 — Momentum — Remembering Which Way Downhill Persists](#excavation-028-momentum-remembering-which-way-downhill-persists)
- [Excavation 029 — Initialization — Where Should Learning Begin?](#excavation-029-initialization-where-should-learning-begin)
- [Excavation 030 — Activation Functions — Why a Network Must Bend](#excavation-030-activation-functions-why-a-network-must-bend)
- [Excavation 031 — Overfitting — When Perfect Memory Pretends to Be Intelligence](#excavation-031-overfitting-when-perfect-memory-pretends-to-be-intelligence)
- [Excavation 032 — Regularization — Making Memorization More Expensive](#excavation-032-regularization-making-memorization-more-expensive)
- [Excavation 033 — Validation — Testing Without Peeking at the Final Exam](#excavation-033-validation-testing-without-peeking-at-the-final-exam)
- [Excavation 034 — Generalization — What Should Survive Beyond the Dataset?](#excavation-034-generalization-what-should-survive-beyond-the-dataset)
- [Excavation 035 — A Tiny Neural Network — Assemble the Entire Learning Loop](#excavation-035-a-tiny-neural-network-assemble-the-entire-learning-loop)
- [Excavation 036 — Tokenization: What Can a Language Model See?](#excavation-036-tokenization-what-can-a-language-model-see)
- [Excavation 037 — Input Embeddings: Giving Tokens Learnable Coordinates](#excavation-037-input-embeddings-giving-tokens-learnable-coordinates)
- [Excavation 038 — Position — Why Order Must Enter the Model](#excavation-038-position-why-order-must-enter-the-model)
- [Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward](#excavation-039-causal-masking-preventing-the-future-from-leaking-backward)
- [Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons](#excavation-040-next-token-examples-one-sentence-becomes-many-lessons)
- [Excavation 041 — Logits — Let Every Vocabulary Token Compete](#excavation-041-logits-let-every-vocabulary-token-compete)
- [Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction](#excavation-042-vocabulary-probabilities-turning-scores-into-a-prediction)
- [Excavation 043 — Sampling — Choosing Without Always Taking the Maximum](#excavation-043-sampling-choosing-without-always-taking-the-maximum)
- [Excavation 044 — Context Windows — How Much Past Can the Model Carry?](#excavation-044-context-windows-how-much-past-can-the-model-carry)
- [Excavation 045 — A Tiny GPT — Close the Prediction Loop](#excavation-045-a-tiny-gpt-close-the-prediction-loop)
- [Excavation 046 — Perplexity — How Surprised Is the Model?](#excavation-046-perplexity-how-surprised-is-the-model)
- [Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?](#excavation-049-calibration-does-80-confidence-mean-eight-out-of-ten)
- [Excavation 051 — Scaling Laws — What Improves When We Add More?](#excavation-051-scaling-laws-what-improves-when-we-add-more)
- [Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful](#excavation-053-preference-learning-when-several-answers-are-correct-but-not-equally-helpful)
- [Excavation 077 — Convolution — Reusing the Same Local Detector](#excavation-077-convolution-reusing-the-same-local-detector)
- [Excavation 084 — Diffusion — Learning by Destroying](#excavation-084-diffusion-learning-by-destroying)
- [Excavation 085 — Denoising — Predicting What the Noise Hid](#excavation-085-denoising-predicting-what-the-noise-hid)
- [Excavation 089 — Q-Learning — Improving Values from Experience](#excavation-089-q-learning-improving-values-from-experience)
- [Excavation 090 — Policy Gradients — Improving the Choices Directly](#excavation-090-policy-gradients-improving-the-choices-directly)
- [Excavation 092 — Contrastive Learning](#excavation-092-contrastive-learning)
- [Excavation 094 — Low-Rank Adaptation](#excavation-094-low-rank-adaptation)
- [Excavation 095 — Quantization](#excavation-095-quantization)
- [Excavation 102 — Bayesian Updating](#excavation-102-bayesian-updating)
- [Excavation 115 — Tree Search](#excavation-115-tree-search)
- [Excavation 119 — Graph Neural Networks](#excavation-119-graph-neural-networks)
- [Excavation 122 — Differential Privacy](#excavation-122-differential-privacy)

---

## Excavation 002 — Vectors

A tiger recorded as weight 220, speed 65, and age 6 becomes [220, 65, 6]. The first slot must always mean weight; otherwise [220, 65, 6] could describe nonsense.

### Give Short Names Only After We Know the Pieces

- **x** is the object we needed to carry as one package.
- **x₁ through xₙ** are its agreed measurements; subscripts preserve which feature is which.
- **n** exists because different problems keep different numbers of features.
- The brackets bind the measurements without adding or comparing them yet.


This says only: one object carries an ordered measurement for each of $n$ agreed features.

Only now can we compress that reasoning:

$$
\mathbf{x}=[x_1,x_2,\ldots,x_n]
$$

[Return to the full excavation](excavations/002-vectors/README.md)

---

## Excavation 003 — Distance

Tiger A has weight 220 kg, speed 65 km/h, and age 6 years.

Tiger B has weight 225 kg, speed 66 km/h, and age 5 years.

Compare the same property with the same property:

~~~text
weight difference = 225 - 220 =  5
speed difference  =  66 -  65 =  1
age difference    =   5 -   6 = -1
~~~

Adding gives 5 + 1 - 1 = 5. That is wrong: being one year younger cancelled part of the other disagreement.

~~~text
weight disagreement squared = 5 squared    = 25
speed disagreement squared  = 1 squared    =  1
age disagreement squared    = (-1) squared =  1
total                                      = 27
~~~

The total is in squared differences. Its square root gives one ordinary separation: about 5.20.

### Give Short Names Only After We Know the Pieces

- **x** is only a nickname for Tiger A's ordered measurements.
- **y** is only a nickname for Tiger B's ordered measurements.
- **x1 and y1** are their weights; index 2 means speed; index 3 means age.
- **xi−yi** abbreviates “compare the same named property,” exactly as above.
- Squaring repairs the cancellation we just witnessed.
- Summing combines weight, speed, and age into one answer.
- The root changes total 27 into distance 5.20.
- **d(x,y)** merely names “the one separation between these two tigers.”

Only now can we compress that reasoning:

$$
d(\mathbf{x},\mathbf{y})
=\sqrt{(x_1-y_1)^2+(x_2-y_2)^2+\cdots+(x_n-y_n)^2}
$$


The formula is your procedure written compactly.

[Return to the full excavation](excavations/003-distance/README.md)

---

## Excavation 004 — Vectors as Change

A traveler starts at [2,3] and ends at [7,1]. Removing the start coordinate by coordinate gives [5,-2]. Adding that change to a different start [10,10] produces [15,8], proving the instruction can travel.

### Give Short Names Only After We Know the Pieces

- **a** is the starting state and **b** the observed destination.
- Subtraction is forced because we need the change that remains after removing the start.
- **Δ** names that reusable change, including its signs and directions.
- Adding Δ back to a must recover b; this second equation checks the meaning of the first.

Only now can we compress that reasoning:

$$
\Delta=\mathbf{b}-\mathbf{a}=[7-2,1-3]=[5,-2]
$$

Add it back and the meaning becomes visible:

$$
\mathbf{a}+\Delta=\mathbf{b}
$$

[Return to the full excavation](excavations/004-vectors-as-change/README.md)

---

## Excavation 005 — Matrices

Our animal report has normalized weight signal 4 and speed signal 5.

The first output is a threat score: two copies of weight plus three copies of speed, giving 2×4 + 3×5 = 23.

The second is a chase score: ignore weight and take four copies of speed, giving 0×4 + 4×5 = 20.

~~~text
threat = 2×weight + 3×speed = 2×4 + 3×5 = 23
chase  = 0×weight + 4×speed = 0×4 + 4×5 = 20
~~~

Only after these named recipes do they become two matrix rows.

### Give Short Names Only After We Know the Pieces

- The right-hand vector **[4,5]** is shorthand for weight signal 4 and speed signal 5.
- Each matrix row describes one output; each row needs one weight per input.
- Multiplication measures one input's contribution to one output.
- Addition combines all contributions reaching that output.
- The result **[23,20]** contains one value per matrix row.


Row-by-column multiplication is not a ritual. Each row is one output asking how much every input should contribute.

Only now can we compress that reasoning:

$$
\text{threat score}=2(4)+3(5)=23
$$

$$
\text{chase score}=0(4)+4(5)=20
$$

[Return to the full excavation](excavations/005-matrices/README.md)

---

## Excavation 007 — A Place for Meaning to Live

Take one concrete snapshot. Suppose we decided that every word gets three
adjustable coordinates, and training has currently placed *tiger* here:

```text
tiger → [0.8, 0.2, -0.4]
```

Every part now has a job you already understand:

- *tiger* is the discrete token—the identity we started with.
- The arrow means “represent this token by,” not “these two things are equal.”
- `[0.8, 0.2, -0.4]` is the position training has produced so far.
- Three is the width we chose for this tiny world. A real model usually needs
  many more adjustable coordinates.
- The coordinates need not have private names. A relationship can be spread
  across several of them.

Only now is the compact notation useful:

$$
\text{token}\longrightarrow \mathbf{e}\in\mathbb{R}^d
$$

Here, $\mathbf{e}$ is merely a short name for the learned list of coordinates.
$d$ is how many coordinates we chose to provide. $\mathbb{R}^d$ says that all
$d$ entries may be ordinary real numbers—positive, negative, or zero. The
equation has added no new idea. It records the space you just constructed.

[Return to the full excavation](excavations/007-embeddings/README.md)

---

## Excavation 009 — From Scores to Attention

For scores [1,2], exponentiation gives about [2.72,7.39]. Their total is 10.11. Dividing produces [0.27,0.73]: both remain possible, the larger score gets more weight, and the weights total one.

### Give Short Names Only After We Know the Pieces

- **sᵢ** is the raw relevance score for candidate i.
- Exponentiation makes every weight positive, preserves ordering, suppresses negative evidence, and amplifies strong evidence.
- The denominator sums evidence from every candidate j because a weight is meaningful only relative to its competitors.
- Division makes all resulting weights sum to one.


For scores `[2, 4, 8]`, the largest score receives almost all the weight, but the others are not forbidden from contributing.

Softmax does not discover relevance. It converts already-computed relevance scores into a smooth distribution of attention.

Only now can we compress that reasoning:

$$
\mathrm{softmax}(s_i)=\frac{e^{s_i}}{\sum_j e^{s_j}}
$$

[Return to the full excavation](excavations/009-softmax/README.md)

---

## Excavation 010 — Query, Key, and Value

Let q=[1,2] and one key be [3,4]. Matching coordinates contribute 1×3=3 and 2×4=8, giving score 11. If its normalized weight is 0.75 and its value is [8,4], it contributes [6,3] to the output.

### Give Short Names Only After We Know the Pieces

- **qᵢ** states what receiving token i needs; **kⱼ** states what source j offers.
- Multiplying matching coordinates rewards aligned needs and offers; opposite signs become negative evidence.
- Summing over feature r turns many alignments into one score sᵢⱼ.
- **αᵢⱼ** is that score after normalization: how much i listens to j.
- **vⱼ** is the content source j contributes; multiplying by α scales its voice.
- Summing over j combines every permitted source into output oᵢ.


Learned matrices create query, key, and value views from each current representation. Their formulas record three roles we already needed; they are not arbitrary symmetry.

Only now can we compress that reasoning:

$$
s_{ij}=\mathbf{q}_i\cdot\mathbf{k}_j
=\sum_r q_{ir}k_{jr}
$$

For each receiving word, its whole query is compared with the whole key of every available source word. The feature-wise products happen inside each comparison; the sum creates one score per source.

### The next compression in this excavation

Query and key decide who matters. They do not say what information should travel.

When asked how three experts should contribute, you answered:

> Each expert contributes what they do—the knowledge related to their profession and domain.

Exactly. A historian's matching description is not the historical knowledge we want to retrieve. Each source therefore needs a **Value**: the content it contributes if selected.

```text
Query ↔ Key → score → softmax weight
Value × weight → contributed information
```

The output for one token is finally the weighted sum of source values:

$$
\mathbf{o}_i=\sum_j \alpha_{ij}\mathbf{v}_j
$$

[Return to the full excavation](excavations/010-query-key-value/README.md)

---

## Excavation 011 — Multi-Head Attention

Suppose one head returns [grammar=8,topic=1] and another [reference=7,distance=2]. Averaging would mix their coordinate roles. Concatenating keeps [8,1,7,2], after which the output matrix can learn the useful mixture.

### Give Short Names Only After We Know the Pieces

- **X** is the shared sequence of token representations.
- Each **headₕ** is an independent Q/K/V retrieval space, needed because relationships should not compete in one distribution.
- Concatenation preserves each report instead of averaging distinctions away.
- **H** counts the parallel heads.
- **W_O** is learned because the model must decide how the preserved reports should interact and return to the shared width.


Each head is the query–key–value mechanism from the previous excavation with independent learned projections.

The analogy has limits. Heads do not always become clean, human-readable professions. Some overlap; some are difficult to interpret. The architectural point is parallel relationship spaces, not a promise of tidy labels.

Only now can we compress that reasoning:

$$
\mathrm{MultiHead}(X)
=\mathrm{Concat}(\text{head}_1,\ldots,\text{head}_H)W_O
$$

[Return to the full excavation](excavations/011-multi-head-attention/README.md)

---

## Excavation 012 — Feed-Forward Networks

Let the first map turn [2,-1] into candidates [3,-4,1]. ReLU closes the -4 path, leaving [3,0,1]. The second map can now recombine different active paths; without the gate both maps reduce to one fixed linear recipe.

### Give Short Names Only After We Know the Pieces

- **x** is one token after communication.
- **W₁x+b₁** expands it into candidate features; b₁ lets a feature activate without forcing the boundary through zero.
- **σ** is the nonlinear gate that prevents two linear maps collapsing into one.
- **W₂** recombines active candidates into the model width.
- **b₂** permits an output offset after recombination.


The same workshop is applied separately to every token. It does not communicate across positions; attention already handled that.

```text
attention: who should I hear?
feed-forward: what do I make of what I heard?
```

The phrase “feed-forward” can sound like the entire model. Here it means the position-wise transformation inside each Transformer block.

Only now can we compress that reasoning:

$$
\mathrm{FFN}(\mathbf{x})
=W_2 \sigma(W_1\mathbf{x}+\mathbf{b}_1)+\mathbf{b}_2
$$

[Return to the full excavation](excavations/012-feed-forward-networks/README.md)

---

## Excavation 013 — Residual Connections

A layer receives [5,2]. If it discovers only a correction [0.5,-1], addition gives [5.5,1]. If no correction is needed, [0,0] preserves [5,2] exactly instead of relearning how to copy it.

### Give Short Names Only After We Know the Pieces

- **x** is the representation worth preserving.
- **F(x)** is only the transformation's proposed correction, not a complete replacement.
- Addition keeps a direct route for x and makes “do nothing” possible when F(x)=0.
- **y** is the corrected state passed onward.


The block learns the **residual**—the difference between what exists and what should be added.

This direct route also gives learning signals a path that does not depend entirely on every learned transformation. Residual connections do not guarantee that a very deep model will train, but they make preservation and correction far easier.

Addition requires the input and proposal to have the same shape. That is why attention and feed-forward sublayers return to the model's shared width before joining the residual stream.

Only now can we compress that reasoning:

$$
\mathbf{y}=\mathbf{x}+F(\mathbf{x})
$$

[Return to the full excavation](excavations/013-residual-connections/README.md)

---

## Excavation 014 — Layer Normalization

For [1,2,3], the mean is 2. Centering gives [-1,0,1]; their squared average is 2/3. Dividing by its square root gives a zero-centered, predictable-scale pattern. Epsilon matters for [4,4,4], whose spread is zero.

### Give Short Names Only After We Know the Pieces

- **xᵢ** is one feature of a token and **d** is its number of features.
- Summing and dividing by d creates μ, the token's average level.
- Subtracting μ recenters every feature.
- Squaring centered values prevents cancellation; averaging them creates variance σ².
- The square root converts variance to ordinary scale.
- Dividing produces comparable spread; ε prevents division by zero when no spread exists.
- **x̂ᵢ** is the normalized feature.


The small $\epsilon$ prevents division by zero when every feature is equal.

Forcing every representation to remain permanently standardized would itself be restrictive. Learned scale and shift parameters therefore let the model restore useful volumes and offsets after normalization.

Layer normalization is not intelligence and does not create meaning. It creates stable numerical conditions in which learned transformations can operate.

Only now can we compress that reasoning:

$$
\mu=\frac1d\sum_i x_i,
\qquad
\sigma^2=\frac1d\sum_i(x_i-\mu)^2
$$

$$
\widehat{x}_i=\frac{x_i-\mu}{\sqrt{\sigma^2+\epsilon}}
$$

[Return to the full excavation](excavations/014-layer-normalization/README.md)

---

## Excavation 015 — How a Dead Brain Learns

One weight is 8, its target is 3, and its local uphill sensitivity is 10. Taking one tenth of the reversed suggestion moves it to 7 and lowers squared error from 25 to 16.

### Give Short Names Only After We Know the Pieces

- **θ** is the current collection of learnable weights.
- **L** is the measured prediction failure.
- **∇L** collects how increasing each weight would increase loss.
- The minus sign reverses that uphill direction.
- **η** controls step size because direction alone does not say how far to move.
- The arrow means replace the old weights with the improved ones.


$\theta$ is the current state of the weights, $\nabla L$ is a vector of advised change, and $\eta$ controls how large a step to take.

Only now can we compress that reasoning:

$$
\theta\leftarrow\theta-\eta\nabla L
$$

[Return to the full excavation](excavations/015-learning/README.md)

---

## Excavation 017 — Probability — Counting What We Do Not Know

A tracker saw tigers after 2 of 10 comparable rustles. The raw count 2 means little without 10 opportunities. Dividing gives 0.2: under this evidence, two tenths of such rustles preceded a tiger.

### Give Short Names Only After We Know the Pieces

- **A** is the uncertain event we need to discuss.
- The numerator counts observations where A occurred.
- The denominator counts all comparable opportunities, because an isolated count has no scale.
- Division turns the count into a share between zero and one.
- **P(A)** names that evidence-dependent share, not a guarantee.

Only now can we compress that reasoning:

$$
P(A)=\frac{\text{times }A\text{ occurred}}{\text{comparable observations}}
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

[Return to the full excavation](excavations/017-probability/README.md)

---

## Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?

Story A says a deep print occurs 80% of the time; Story B says 20%. After observing a deep print, the same evidence has likelihood 0.8 under A and 0.2 under B, so A explains this clue four times as well.

### Give Short Names Only After We Know the Pieces

- **θ** is one proposed hidden explanation.
- **x** is the evidence already observed.
- The vertical bar means “under the assumption that.”
- **P(x|θ)** asks how expected this evidence would be if θ were true—the reversal forced by comparing stories.
- **L(θ|x)** names that same quantity when x is held fixed and explanations vary; it is not automatically a probability over θ.

Only now can we compress that reasoning:

$$
\mathcal{L}(\theta\mid x)=P(x\mid\theta)
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

[Return to the full excavation](excavations/018-likelihood/README.md)

---

## Excavation 019 — Information — Why Surprise Needs a Number

An event with probability 1/2 carries 1 bit because -log₂(1/2)=1. An event with probability 1/8 carries 3 bits. The rarer observation eliminates more alternatives, so it teaches more.

### Give Short Names Only After We Know the Pieces

- **P(x)** measures how expected observation x was.
- The logarithm is needed because independent probabilities multiply while information from independent messages should add.
- Probabilities below one have negative logs, so the minus sign makes information nonnegative.
- A certain event has P=1 and therefore zero information; rarer events receive more.

Only now can we compress that reasoning:

$$
I(x)=-\log P(x)
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

[Return to the full excavation](excavations/019-information/README.md)

---

## Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation

For a fair coin, each outcome has probability 1/2 and information 1 bit. Weighting gives 0.5×1+0.5×1=1 expected bit. A coin guaranteed heads gives -log₂(1)=0, so its entropy is zero.

### Give Short Names Only After We Know the Pieces

- **pᵢ** is the probability of possible outcome i.
- **−log pᵢ** is the information received if i occurs.
- Multiplying by pᵢ weights that surprise by how often it is expected to occur.
- Summing over every i computes average surprise before the outcome is known.
- **H(P)** names uncertainty of the whole distribution P.

Only now can we compress that reasoning:

$$
H(P)=-\sum_i p_i\log p_i
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

[Return to the full excavation](excavations/020-entropy/README.md)

---

## Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions

Reality says the answer is tiger. A model assigning tiger 0.9 pays -log(0.9), about 0.105. A model assigning 0.01 pays about 4.605. The confident wrong model is charged far more.

### Give Short Names Only After We Know the Pieces

- **P** is the distribution reality supplies; pᵢ weights which outcomes actually occur.
- **Q** is the model's proposed distribution; qᵢ is the probability it assigned outcome i.
- **−log qᵢ** makes confident neglect extremely costly.
- Summing the reality-weighted costs gives one expected prediction penalty H(P,Q).

Only now can we compress that reasoning:

$$
H(P,Q)=-\sum_i p_i\log q_i
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

[Return to the full excavation](excavations/021-cross-entropy/README.md)

---

## Excavation 022 — Derivatives — Asking One Weight What It Changed

Use L(w)=w² at w=3. Nudge to 3.001: loss changes from 9 to about 9.006001. Dividing the loss change by 0.001 gives about 6; smaller nudges approach the local sensitivity 6.

### Give Short Names Only After We Know the Pieces

- **w** is the one weight whose responsibility we are probing.
- **ε** is a small experimental nudge.
- **L(w+ε)−L(w)** measures the loss change caused by that nudge.
- Dividing by ε turns total change into change per unit of weight.
- The limit shrinks the nudge so the answer becomes local rather than dependent on an arbitrary test step.
- **dL/dw** names that local sensitivity.

Only now can we compress that reasoning:

$$
\frac{dL}{dw}=\lim_{\epsilon\to0}\frac{L(w+\epsilon)-L(w)}{\epsilon}
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

[Return to the full excavation](excavations/022-derivatives/README.md)

---

## Excavation 023 — The Chain Rule — Following One Change Through Many Machines

A weight change is doubled by the first machine, tripled by the second, and quadrupled by the loss. One unit at the start becomes 2, then 6, then 24. Multiplying 2×3×4 captures the complete path.

### Give Short Names Only After We Know the Pieces

- **w→x→y→L** is the causal path through successive machines.
- Each fraction is one local sensitivity: how its output changes when its input changes.
- Multiplication is forced because a change is scaled at every link it traverses.
- The product gives the effect of w on L without pretending they touch directly.

Only now can we compress that reasoning:

$$
\frac{dL}{dw}=\frac{dL}{dy}\frac{dy}{dx}\frac{dx}{dw}
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

[Return to the full excavation](excavations/023-chain-rule/README.md)

---

## Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It

Suppose x feeds two children. The first returns blame 3 through a local sensitivity 2, contributing 6. The second returns blame 4 through sensitivity 5, contributing 20. Total blame reaching x is 26, so both paths must be added.

### Give Short Names Only After We Know the Pieces

- **x̄** means accumulated sensitivity of final loss to intermediate x.
- A node can influence several child results y, so every downstream path must contribute.
- **ȳ** is blame already accumulated at child y.
- **∂y/∂x** says how strongly x affected that child locally.
- Multiplication passes blame through one edge; summation combines all outgoing paths.

Only now can we compress that reasoning:

$$
\bar{x}=\sum_{y\in children(x)}\bar{y}\frac{\partial y}{\partial x}
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

[Return to the full excavation](excavations/024-backpropagation/README.md)

---

## Excavation 025 — Gradient Descent — Teaching a Tiny Network

Forget θ for a moment. Our tiny model has one adjustable weight, currently **8**. We want it to become **3**, so its mistake is (weight − 3)². At weight 8, the mistake is 25.

A tiny upward nudge shows a local sensitivity of 10. In ordinary language: increasing the weight a little makes the mistake rise about ten times as much. Ten therefore points uphill. To reduce the mistake, we move the other way. That creates the minus sign.

Should we move the entire ten units?

~~~text
8 - 10 = -2
mistake at -2 = (-2 - 3)² = 25
~~~

We jumped across the valley and learned nothing. So direction is not enough. We need a knob controlling how much of the proposed movement we trust.

Try taking one tenth:

~~~text
suggested uphill direction = 10
reverse it                 = -10
take one tenth             = -1
new weight                 = 8 - 1 = 7
new mistake                = (7 - 3)² = 16
~~~

The mistake fell from 25 to 16. That one tenth is the **learning rate**, later written η. It is simply a caution knob:

- η = 1 takes the entire proposed movement;
- η = 0.1 takes one tenth;
- η = 0.01 takes one hundredth.

Too large can jump over the valley. Too small moves safely but slowly.

### Give Short Names Only After We Know the Pieces

- **θ_t** packages the current weights; our tiny example has only 8.
- **L** is the mistake measure; here it is (weight − 3)².
- **∇_θL** packages local sensitivities; our example has only 10.
- The minus sign reverses the uphill direction.
- **η** is the chosen fraction of the correction; here it is 0.1.
- **t** means before this correction; **t+1** means after it.

Substitute real values before compact symbols:

~~~text
next weight = current weight - learning rate × uphill sensitivity
            = 8              - 0.1           × 10
            = 7
~~~

Only now can we compress the same procedure:

$$
\theta_{t+1}=\theta_t-\eta\nabla_\theta L
$$


The equation is not the discovery. It is the shortest record of the discovery already reconstructed above.

[Return to the full excavation](excavations/025-gradient-descent/README.md)

---

## Excavation 026 — Mini-Batches — Learning from More Than One Example

Three examples propose gradients [2,4], [4,2], and [3,3]. Adding gives [9,9]; dividing by three gives [3,3]. Without division, merely enlarging the batch would triple the update.

### Give Short Names Only After We Know the Pieces

- **B** is the selected mini-batch and **|B|** its number of examples.
- **Lᵢ** is loss for example i; **∇_θLᵢ** is that example's proposed parameter direction.
- Summing combines the witnesses.
- Dividing by batch size prevents merely using more examples from making the step proportionally larger.
- **g_B** is the batch's less noisy gradient estimate.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
g_B=\frac{1}{|B|}\sum_{i\in B}\nabla_\theta L_i
$$

[Return to the full excavation](excavations/026-mini-batches/README.md)

---

## Excavation 027 — Learning Rate — How Large Should the Next Step Be?

At weight 8 the gradient is 10. Rate 1 moves to -2 and overshoots; rate 0.1 moves to 7; rate 0.01 moves to 7.9. The rate controls travel distance, not downhill direction.

### Give Short Names Only After We Know the Pieces

- **g_t** is the downhill evidence measured at step t.
- **η_t** converts direction into a chosen travel distance and may change with time.
- The minus sign moves against increasing loss.
- **θ_t** and **θ_{t+1}** distinguish the old and updated parameter states.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
\theta_{t+1}=\theta_t-\eta_t g_t
$$

[Return to the full excavation](excavations/027-learning-rate/README.md)

---

## Excavation 028 — Momentum — Remembering Which Way Downhill Persists

Successive gradients are [3,1], [3,-1], [3,1]. The sideways coordinate flips, while the first persists. A fading sum reinforces the repeated 3 direction and partly cancels the wobble.

### Give Short Names Only After We Know the Pieces

- **g_t** is the newest noisy gradient.
- **v_{t−1}** stores direction accumulated previously.
- **β** between zero and one controls how much old motion survives; repeated multiplication makes old advice fade.
- Addition combines memory with new evidence into velocity v_t.
- **η** scales that velocity before it changes θ.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
v_t=\beta v_{t-1}+g_t,\qquad\theta_{t+1}=\theta_t-\eta v_t
$$

[Return to the full excavation](excavations/028-momentum/README.md)

---

## Excavation 029 — Initialization — Where Should Learning Begin?

If 100 independent inputs each arrive near unit scale, weights near unit scale make their sum huge. Scaling typical weight spread by 1/sqrt(100)=0.1 keeps their combined signal near a workable scale.

### Give Short Names Only After We Know the Pieces

- **w** is one newly initialized weight.
- **Var(w)** measures the typical squared spread of starting weights, not their meaning.
- **n_in** counts signals entering the neuron.
- Dividing by n_in compensates for adding more independent inputs, preventing their combined signal scale from growing with width.
- “Approximately” leaves room for activation-specific constants such as Xavier or He scaling.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
\mathrm{Var}(w)\approx\frac{1}{n_{\text{in}}}
$$

[Return to the full excavation](excavations/029-initialization/README.md)

---

## Excavation 030 — Activation Functions — Why a Network Must Bend

Without a gate, multiplying by 2 and then 3 always equals multiplying once by 6. With ReLU between them, input -1 becomes -2, then 0, then 0—behavior no single multiply-by-6 rule reproduces for both signs.

### Give Short Names Only After We Know the Pieces

- **x** is the incoming representation.
- **W** mixes its features; **b** permits learned thresholds and offsets.
- **φ** is the necessary nonlinear gate; without it, stacked layers collapse into one linear map.
- **h** is the hidden representation after both mixing and gating.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
h=\phi(Wx+b)
$$

[Return to the full excavation](excavations/030-activation-functions/README.md)

---

## Excavation 031 — Overfitting — When Perfect Memory Pretends to Be Intelligence

A model has training loss 0.02 and unseen loss 0.17. Subtracting gives a gap of 0.15. The low training number shows memory; the gap measures how much success disappeared outside it.

### Give Short Names Only After We Know the Pieces

- **L_train** measures error on examples allowed to shape the model.
- **L_unseen** measures error on held-out observations.
- Subtraction isolates deterioration outside memory instead of confusing it with absolute task difficulty.
- A positive generalization gap is evidence that training success did not fully survive.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
\text{generalization gap}=L_{\text{unseen}}-L_{\text{train}}
$$

[Return to the full excavation](excavations/031-overfitting/README.md)

---

## Excavation 032 — Regularization — Making Memorization More Expensive

Two models have data loss 2. Model A has squared-weight sum 100; B has 4. With lambda 0.1, totals are 12 and 2.4. The penalty makes the equally fitting but less extreme model preferable.

### Give Short Names Only After We Know the Pieces

- **L_data** rewards fitting observations.
- **θ** contains the weights; squaring and summing them creates ||θ||² without signed cancellation.
- **λ** expresses how strongly we prefer smaller machinery relative to data fit.
- Addition forces training to negotiate prediction accuracy and complexity in one objective.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
L_{\text{total}}=L_{\text{data}}+\lambda\lVert\theta\rVert^2
$$

[Return to the full excavation](excavations/032-regularization/README.md)

---

## Excavation 033 — Validation — Testing Without Peeking at the Final Exam

With 100 examples, use 60 to change weights, 20 to choose learning rate, and keep 20 sealed. If the sealed 20 guide choices, they stop being an honest final test.

### Give Short Names Only After We Know the Pieces

- **D** is all available data.
- The three named subsets exist because weight learning, design choices, and final measurement must not share feedback.
- Union means they reconstruct the available collection.
- The intended split also requires no example to leak between sets, even though the compact union symbol alone does not state disjointness.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
D=D_{\text{train}}\cup D_{\text{validation}}\cup D_{\text{test}}
$$

[Return to the full excavation](excavations/033-validation/README.md)

---

## Excavation 034 — Generalization — What Should Survive Beyond the Dataset?

Suppose future cases have losses 1,0,2,1. Their average is 1, our estimate of future risk. Averaging training losses instead would answer how well we remember the past, not deployment.

### Give Short Names Only After We Know the Pieces

- **θ** is one trained model and **f_θ(x)** its prediction for input x.
- **L(f_θ(x),y)** measures failure against outcome y.
- **P_future** names the deployment world we actually care about.
- Sampling (x,y) from that world prevents training data from silently defining success.
- The expectation averages loss over future cases; **R(θ)** names that future risk.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
R(\theta)=\mathbb{E}_{(x,y)\sim P_{\text{future}}}[L(f_\theta(x),y)]
$$

[Return to the full excavation](excavations/034-generalization/README.md)

---

## Excavation 035 — A Tiny Neural Network — Assemble the Entire Learning Loop

Input 2 is mixed into a hidden signal, gated, and produces prediction 0.7. If the target is 1, loss sends correction backward through the same steps, changes weights, and the next forward pass may produce 0.8. The arrows are one loop.

### Give Short Names Only After We Know the Pieces

- **x** is observed input.
- **Wx+b** mixes features and supplies offsets.
- **φ** bends the mapping so depth adds new behavior.
- **ŷ** is the prediction and **L** measures its failure.
- **∇_θL** assigns local correction directions to all parameters θ.
- **θ′** is the updated state; the arrows show the forward path continuing into feedback rather than separate facts.


Every operation records a need established above; the equation is the fossil, not the living discovery.

Only now can we compress that reasoning:

$$
x\to Wx+b\to\phi(\cdot)\to\hat y\to L\to\nabla_\theta L\to\theta^\prime
$$

[Return to the full excavation](excavations/035-tiny-neural-network/README.md)

---

## Excavation 036 — Tokenization: What Can a Language Model See?

In low, lower, lowest, pair l-o appears three times, more than e-r once. Counting selects l-o; merging creates lo. Recounting can then select lo-w and create reusable low.

### Give Short Names Only After We Know the Pieces

- **a and b** are neighboring current tokens; c(a,b) counts their repeated adjacency because repetition is the evidence for reuse.
- The star marks the pair selected for merging.
- **arg max** returns the pair itself, not its count, because that pair must be replaced.
- Maximizing over every candidate pair makes the merge arise from the corpus rather than a hand-written linguistic rule.


Count, choose, merge, and repeat. The symbols only compress the procedure already needed.

Only now can we compress that reasoning:

$$
c(a,b)=\text{number of adjacent occurrences of }(a,b)
$$

$$
(a^*,b^*)=\underset{(a,b)}{\mathrm{arg\,max}}\;c(a,b)
$$

[Return to the full excavation](excavations/036-tokenization/README.md)

---

## Excavation 037 — Input Embeddings: Giving Tokens Learnable Coordinates

With four tokens and width two, the table might have rows [0.1,0.8], [-0.2,0.4], [0.7,-0.1], [0.3,0.2]. Token ID 2 selects [0.7,-0.1]; the number 2 is only the shelf address.

### Give Short Names Only After We Know the Pieces

- **V** is the vocabulary and **|V|** its number of token addresses.
- **d** is the compact representation width chosen for the model.
- **E** therefore needs one row per token and d learnable coordinates per row.
- **i** is a token ID used only to select row E[i]; **x_i** is the retrieved meaning-bearing vector.
- **e_i** is the one-hot selector. Multiplying e_i by E produces the same row, explaining why direct lookup is valid and cheaper.


Multiplying by a one-hot vector merely selects one row, so an implementation can perform the lookup directly.

Only now can we compress that reasoning:

$$
E\in\mathbb{R}^{|V|\times d}
$$

For token ID $i$, retrieve:

$$
\mathbf{x}_i=E[i]
$$

The one-hot view gives the same result:

$$
\mathbf{x}_i=\mathbf{e}_iE
$$

[Return to the full excavation](excavations/037-input-embeddings/README.md)

---

## Excavation 038 — Position — Why Order Must Enter the Model

Tiger at position 0 retrieves content [0.8,0.2] and position [0.1,-0.1], producing [0.9,0.1]. The same tiger at position 2 adds a different position vector, so content stays recognizable while order changes.

### Give Short Names Only After We Know the Pieces

- **token_i** is the vocabulary address appearing at sequence location i.
- **E[token_i]** retrieves what that token currently represents.
- **P_i** represents where the occurrence sits.
- Addition is possible because both vectors share width and is necessary so every later operation receives content and position together.
- **z_i** is the combined input at position i.

Only now can we compress that reasoning:

$$
z_i=E[token_i]+P_i
$$


The equation arrives after every operation has a job.

[Return to the full excavation](excavations/038-position/README.md)

---

## Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

For position i=2, sources j=0,1,2 receive mask value 0 and remain visible. Sources j=3,4 receive negative infinity; exponentiation turns those scores into zero weight.

### Give Short Names Only After We Know the Pieces

- **i** is the receiving position and **j** a possible source position.
- When j≤i, the source is present or past, so adding zero leaves its attention score unchanged.
- When j>i, the source is future; adding −∞ makes its later softmax weight zero.
- **M_ij** stores that allowed-or-forbidden correction for every pair.

Only now can we compress that reasoning:

$$
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases}
$$


The equation arrives after every operation has a job.

[Return to the full excavation](excavations/039-causal-mask/README.md)

---

## Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

Tokens [the,cat,slept] become inputs [the,cat] and targets [cat,slept]. One forward pass therefore asks “after the?” and “after the cat?” at separate positions.

### Give Short Names Only After We Know the Pieces

- **t₀…t_n** are consecutive tokens from one observed sequence.
- Input x stops one token early because each position needs an answer to its right.
- Target y starts one token later so y_i is exactly the next token after x_i.
- The shared length lets one forward pass create a supervised lesson at every position.

Only now can we compress that reasoning:

$$
x=(t_0,\ldots,t_{n-1}),\qquad y=(t_1,\ldots,t_n)
$$


The equation arrives after every operation has a job.

[Return to the full excavation](excavations/040-next-token-examples/README.md)

---

## Excavation 041 — Logits — Let Every Vocabulary Token Compete

Let hidden state be [2,1]. One candidate column [3,0] scores 6; another [0,4] scores 4. Adding each candidate bias adjusts its baseline. These raw comparisons are logits.

### Give Short Names Only After We Know the Pieces

- **h** is one contextual token vector containing what the Transformer currently knows.
- **W_vocab** has one scoring direction per vocabulary candidate; multiplication compares h with all candidates at once.
- **b** allows each token a learned baseline tendency.
- **ℓ_i** is the resulting unconstrained logit for candidate i—not yet a probability.

Only now can we compress that reasoning:

$$
\ell_i=hW_{\text{vocab}}+b
$$


The equation arrives after every operation has a job.

[Return to the full excavation](excavations/041-logits/README.md)

---

## Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

For logits [1,2], softmax gives about [0.27,0.73]. If the observed token is the second, loss is -log(0.73), about 0.31. Assigning it 0.01 would cost about 4.61.

### Give Short Names Only After We Know the Pieces

- **ℓ_i** is candidate i's raw score.
- Dividing exponentiated evidence by the sum over all j creates positive probabilities p_i that total one.
- **y** is the observed next-token index, so p_y is the probability assigned to what happened.
- The logarithm converts products across examples into sums and the minus sign makes low assigned probability a large positive loss L.

Only now can we compress that reasoning:

$$
p_i=\frac{e^{\ell_i}}{\sum_j e^{\ell_j}},\qquad L=-\log p_y
$$


The equation arrives after every operation has a job.

[Return to the full excavation](excavations/042-vocabulary-probabilities/README.md)

---

## Excavation 043 — Sampling — Choosing Without Always Taking the Maximum

For logits [1,2], T=1 keeps the original gap. T=0.5 turns them into [2,4], making the winner much sharper. T=2 turns them into [0.5,1], making alternatives more plausible.

### Give Short Names Only After We Know the Pieces

- **ℓ_i** is candidate i's raw logit.
- **T** is temperature: dividing by T changes score gaps before exponentiation.
- T<1 enlarges gaps and sharpens choices; T>1 shrinks gaps and spreads probability.
- Exponentiation preserves ranking while making evidence positive.
- Summing over every j and dividing normalizes the adjusted evidence into p_i(T).

Only now can we compress that reasoning:

$$
p_i(T)=\frac{e^{\ell_i/T}}{\sum_j e^{\ell_j/T}}
$$


The equation arrives after every operation has a job.

[Return to the full excavation](excavations/043-sampling/README.md)

---

## Excavation 044 — Context Windows — How Much Past Can the Model Carry?

With 4 tokens, attention forms 4×4=16 query-key comparisons. With 8 tokens it forms 8×8=64—not merely twice as many. This repeated pairing creates square growth.

### Give Short Names Only After We Know the Pieces

- **n** is the number of tokens inside the active context.
- Each of n queries can compare with n keys, creating roughly n×n score pairs.
- That repeated pairwise work is why cost grows proportionally to n² rather than n.
- The proportional sign is used because heads, width, batching, and implementation add constants omitted from this scaling argument.

Only now can we compress that reasoning:

$$
\text{attention cost}\propto n^2
$$


The equation arrives after every operation has a job.

[Return to the full excavation](excavations/044-context-window/README.md)

---

## Excavation 045 — A Tiny GPT — Close the Prediction Loop

Prompt IDs enter embeddings, pass through a masked block, and produce logits [1,3,0]. Softmax favors the second token; sampling selects it, appends it to the prompt, and runs the same loop again.

### Give Short Names Only After We Know the Pieces

- **tokens** are discrete addresses produced by the tokenizer.
- **embeddings** turn addresses into vectors; Transformer **blocks** contextualize them under causal masking.
- **logits** score every next-token candidate; **loss** compares those scores with the observed answer.
- **update** changes parameters using backpropagated error.
- **sample** chooses a continuation and feeds it back as the next token.
- The arrows encode one closed causal loop, not an unexplained algebraic equality.

Only now can we compress that reasoning:

$$
tokens\to embeddings\to blocks\to logits\to loss\to update\to sample
$$


The equation arrives after every operation has a job.

[Return to the full excavation](excavations/045-tiny-gpt/README.md)

---

## Excavation 046 — Perplexity — How Surprised Is the Model?

Model A assigns probability 0.5 to each of three observed next tokens. Each costs about 0.693 nats; the average is 0.693. Exponentiating gives 2. The model behaves as if it were choosing among two equally plausible options at each step.

### Give Short Names Only After We Know the Pieces

The token count divides total surprise so longer sentences are comparable. Negative logs turn small assigned probabilities into large costs. Exponentiation reverses the log and returns the result to a probability-like choice scale.

Only now can we compress the exact procedure:

$$
\mathrm{PPL}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(t_i\mid t_{<i})\right)
$$

[Return to the full excavation](excavations/046-perplexity/README.md)

---

## Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

Five predictions report 0.8 confidence. Exactly four are correct. Accuracy is 4/5=0.8, so this group is calibrated. If only two are correct, accuracy is 0.4 and the confidence gap is 0.4.

### Give Short Names Only After We Know the Pieces

Each group contains predictions with similar confidence. Accuracy counts how many were correct. The absolute difference measures the reliability gap; weighting by group size prevents tiny groups dominating.

Only now can we compress the exact procedure:

$$
\mathrm{ECE}=\sum_b\frac{|B_b|}{n}\left|\mathrm{accuracy}(B_b)-\mathrm{confidence}(B_b)\right|
$$

[Return to the full excavation](excavations/049-calibration/README.md)

---

## Excavation 051 — Scaling Laws — What Improves When We Add More?

Models with 1, 2, and 4 million effective units achieve losses 4.0, 3.2, and 2.8. Improvement continues but shrinks. The curve helps estimate whether doubling again is worth the cost; it does not promise a new capability.

### Give Short Names Only After We Know the Pieces

N is the resource being scaled. The negative exponent makes loss fall as N grows. Alpha controls how quickly returns diminish. A scales the improvable part; B is the floor this simple trend cannot beat.

Only now can we compress the exact procedure:

$$
L(N)=A N^{-\alpha}+B
$$

[Return to the full excavation](excavations/051-scaling-laws/README.md)

---

## Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

For “How do I reset my router?”, answer A gives three safe ordered steps; answer B gives twenty vague paragraphs. A reviewer chooses A. Repeated comparisons teach concision and usefulness without declaring one exact sentence mandatory.

### Give Short Names Only After We Know the Pieces

The reward scores two responses to the same prompt. Their difference matters, not the absolute score. The logistic function turns that difference into a preference probability; larger positive differences favor the chosen answer.

Only now can we compress the exact procedure:

$$
P(A\succ B)=\frac{1}{1+\exp(-(r_A-r_B))}
$$

[Return to the full excavation](excavations/053-preference-learning/README.md)

---

## Excavation 077 — Convolution — Reusing the Same Local Detector

- The signal values are neighboring brightness measurements.
- The kernel values are the same small detector reused at every location.
- Multiplication measures how each local measurement agrees with its detector weight.
- Summation combines the local evidence; shifting i moves the same detector instead of learning a new one.

Only now can we compress the procedure:

$$
y_i=\sum_{j=0}^{k-1}x_{i+j}w_j
$$

[Return to the full excavation](excavations/077-convolution/README.md)

---

## Excavation 084 — Diffusion — Learning by Destroying

- The clean image is the named tiger image x0.
- Noise ε is the random corruption added during the forward process.
- The retained clean fraction and noise fraction change with step t.
- Square roots scale amplitudes so their variances combine as intended.

Only now can we compress the procedure:

$$
x_t=\sqrt{\bar\alpha_t}\,x_0+\sqrt{1-\bar\alpha_t}\,\epsilon
$$

[Return to the full excavation](excavations/084-diffusion/README.md)

---

## Excavation 085 — Denoising — Predicting What the Noise Hid

- xt is the noisy image already constructed in the example.
- t tells the network how much corruption it faces.
- The network predicts the exact noise ε that hid the clean image.
- Squaring the pixel-by-pixel prediction error prevents cancellation; averaging trains across samples.

Only now can we compress the procedure:

$$
L=\mathbb{E}\left[\lVert\epsilon-\epsilon_\theta(x_t,t)\rVert^2\right]
$$

[Return to the full excavation](excavations/085-denoising/README.md)

---

## Excavation 089 — Q-Learning — Improving Values from Experience

- The immediate reward is what happened now.
- The largest next-state Q value represents the best continuation currently known.
- Discount γ reduces distant evidence and keeps unending sums bounded.
- Adding immediate and discounted future reward creates the target the old estimate moves toward.

Only now can we compress the procedure:

$$
\text{target}=r+\gamma\max_{a^\prime}Q(s^\prime,a^\prime)
$$

[Return to the full excavation](excavations/089-q-learning/README.md)

---

## Excavation 090 — Policy Gradients — Improving the Choices Directly

- The sampled action probability comes from policy πθ.
- Its log converts repeated action probabilities into additive learning signals.
- Return G says how the chosen action eventually turned out.
- The gradient changes θ in the direction that makes above-average rewarded actions more likely.

Only now can we compress the procedure:

$$
\nabla_\theta J=\mathbb{E}\left[G\,\nabla_\theta\log\pi_\theta(a\mid s)\right]
$$

[Return to the full excavation](excavations/090-policy-gradients/README.md)

---

## Excavation 092 — Contrastive Learning

- zi and ti are the matched image and text vectors.
- Their dot product is the named alignment score.
- Temperature T controls how sharply alternatives compete.
- The denominator includes every candidate caption, preventing all examples from collapsing to one point.
- The negative log penalizes the true pair when mismatches receive comparable scores.

Only now can we compress the procedure:

$$
L_i=-\log\frac{\exp(z_i\cdot t_i/T)}{\sum_j\exp(z_i\cdot t_j/T)}
$$

[Return to the full excavation](excavations/092-contrastive-learning/README.md)

---

## Excavation 094 — Low-Rank Adaptation

- W is the frozen large matrix we refuse to duplicate.
- A and B are the two narrow trainable matrices.
- Their product BA creates a full-shaped correction while using far fewer values.
- Addition preserves the base behavior and applies only the learned adaptation.

Only now can we compress the procedure:

$$
W^\prime=W+BA
$$

[Return to the full excavation](excavations/094-lora/README.md)

---

## Excavation 095 — Quantization

- Real weight w is divided by scale s to express it in integer-sized steps.
- Rounding chooses the nearest allowed integer q.
- Multiplying q by s reconstructs the approximate weight used in computation.
- The scale is calibrated so important values fit the available integer range.

Only now can we compress the procedure:

$$
q=\mathrm{round}(w/s),\qquad \widehat w=sq
$$

[Return to the full excavation](excavations/095-quantization/README.md)

---

## Excavation 102 — Bayesian Updating

- Tiger’s prior belief is its share before the footprint.
- The footprint likelihood says how expected this exact clue is if tiger is true.
- Multiplying gives tiger’s unnormalized support.
- The denominator repeats that multiplication for every story and adds them so final beliefs total one.

Only now can we compress the procedure:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{\sum_j P(E\mid H_j)P(H_j)}
$$

[Return to the full excavation](excavations/102-bayesian-updating/README.md)

---

## Excavation 115 — Tree Search

- The average reward records how well one branch has performed.
- Visit count shrinks the exploration bonus as evidence accumulates.
- Total visits increase pressure to reconsider neglected branches.
- The constant controls how much uncertainty competes with known reward.

Only now can we compress the procedure:

$$
\mathrm{score}(a)=\overline R_a+c\sqrt{\frac{\log N}{n_a}}
$$

[Return to the full excavation](excavations/115-tree-search/README.md)

---

## Excavation 119 — Graph Neural Networks

- Node v keeps its current representation.
- Every neighbor u sends a message computed by the same rule.
- Summation combines a variable number of messages without depending on neighbor order.
- The update rule joins the old node state with the aggregated neighborhood evidence.

Only now can we compress the procedure:

$$
h_v^\prime=U\left(h_v,\sum_{u\in N(v)}M(h_v,h_u)\right)
$$

[Return to the full excavation](excavations/119-graph-neural-networks/README.md)

---

## Excavation 122 — Differential Privacy

- D and D-prime are two datasets differing in one person.
- The same possible released result S is considered under both.
- Epsilon limits how much more likely that result may become because one person participated.
- A smaller epsilon makes the two worlds harder to distinguish.

Only now can we compress the procedure:

$$
P(M(D)\in S)\le e^\epsilon P(M(D^\prime)\in S)
$$

[Return to the full excavation](excavations/122-differential-privacy/README.md)
