# The Mathematical Gist of AI Archaeology

This is the book's mathematical spine in discovery order. It is not a
formula sheet. Every entry keeps the concrete work and the explanation
of each term before allowing notation to compress the idea.

Use it after reading an excavation, or to revisit the chain of
mathematical inventions without rereading the entire narrative.
For the reusable meaning of an operation, follow its link into the
[Mathematical Moves guide](MATHEMATICAL_MOVES.md).

**57 equation-bearing excavations · 69 displayed equations**

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

### Only now do the symbols earn names

- **x** is the object we needed to carry as one package.
- **x₁ through xₙ** are its agreed measurements; subscripts preserve which feature is which.
- **n** exists because different problems keep different numbers of features.
- The brackets bind the measurements without adding or comparing them yet.

This says only: one object carries an ordered measurement for each of $n$ agreed features.

### Why these operations are forced

- [Brackets](MATHEMATICAL_MOVES.md#brackets) keep tiger weight, speed, and age together without pretending they should be added; each observation must remain recoverable.
- [Subscripts](MATHEMATICAL_MOVES.md#indices) give each retained feature an address. The dots mean the same pattern continues until feature n; they do not hide another operation.
- [The equals sign](MATHEMATICAL_MOVES.md#equals) says that **x** is our short name for this complete ordered list.

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

### Only now do the symbols earn names

- **x** is only a nickname for Tiger A's ordered measurements.
- **y** is only a nickname for Tiger B's ordered measurements.
- **x1 and y1** are their weights; index 2 means speed; index 3 means age.
- **xi−yi** abbreviates “compare the same named property,” exactly as above.
- Squaring repairs the cancellation we just witnessed.
- Summing combines weight, speed, and age into one answer.
- The root changes total 27 into distance 5.20.
- **d(x,y)** merely names “the one separation between these two tigers.”

### Why these operations are forced

- [Subtracting](MATHEMATICAL_MOVES.md#subtraction) tiger height from tiger height and tiger speed from tiger speed isolates each like-for-like disagreement. Adding would measure a total, not a gap.
- [Squaring](MATHEMATICAL_MOVES.md#powers) stops a smaller and larger feature from cancelling and makes a large mismatch count more strongly. Absolute value could stop cancellation too, but would produce a different geometry in which many small misses and one large miss trade differently.
- [Adding the squared disagreements](MATHEMATICAL_MOVES.md#summation) lets every retained feature contribute to one separation. Multiplying would let one perfect feature match erase all other disagreement by making the product zero.
- [The square root](MATHEMATICAL_MOVES.md#square-root) returns the accumulated squared separation to the features' ordinary scale; it is omitted when squared distance itself is all an algorithm needs.

Only now can we compress that reasoning:

$$
d(\mathbf{x},\mathbf{y})
=\sqrt{(x_1-y_1)^2+(x_2-y_2)^2+\cdots+(x_n-y_n)^2}
$$

The formula is your procedure written compactly.

[Return to the full excavation](excavations/003-distance/README.md)

---

## Excavation 004 — Vectors as Change

A rescue party marks its camp on a paper map. It walks five kilometres east and two kilometres south to reach an injured ranger. Those instructions still work if a second party begins from another camp: move five east and two south. Only after the route has a meaning do we record east–west and north–south change as `[5, -2]`.

### Only now do the symbols earn names

- **a** is the starting state and **b** the observed destination.
- Subtraction is forced because we need the change that remains after removing the start.
- **Δ** names that reusable change, including its signs and directions.
- Adding Δ back to a must recover b; this second equation checks the meaning of the first.

### Why these operations are forced

- [Destination minus starting point](MATHEMATICAL_MOVES.md#subtraction) is forced because we want the change that would carry **a** to **b**, not their combined location.
- [A negative coordinate](MATHEMATICAL_MOVES.md#negative-sign) keeps direction: −2 means move two units opposite that axis, not that the movement has an impossible size.
- [Adding the change back](MATHEMATICAL_MOVES.md#addition) is the check: starting place plus the discovered movement must recover the destination.

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

A ranger must turn two observations—how heavy an animal looks and how fast it moves—into two decisions: danger and whether pursuit is possible. For danger she counts the weight clue twice and the speed clue three times. For pursuit she ignores weight and counts speed four times. Writing the two recipes as rows lets one reusable machine apply both judgments to every animal report.

### Only now do the symbols earn names

- The right-hand vector **[4,5]** is shorthand for weight signal 4 and speed signal 5.
- Each matrix row describes one output; each row needs one weight per input.
- Multiplication measures one input's contribution to one output.
- Addition combines all contributions reaching that output.
- The result **[23,20]** contains one value per matrix row.

Row-by-column multiplication is not a ritual. Each row is one output asking how much every input should contribute.

### Why these operations are forced

- [Multiplication](MATHEMATICAL_MOVES.md#multiplication) lets each clue's importance scale that clue. A zero weight silences it; a weight of three makes it count three times.
- [Addition](MATHEMATICAL_MOVES.md#addition) combines the scaled clues because they are separate contributions to the same judgment. Multiplying them would make any zero clue erase the entire decision and would claim interaction we never asked for.
- [Each equals sign](MATHEMATICAL_MOVES.md#equals) records that the verbal judgment, its arithmetic recipe, and its final score are three descriptions of the same result.

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

### Why these operations are forced

- [The arrow](MATHEMATICAL_MOVES.md#arrows) means “represent this token as,” not equality: a word and its numerical representation are different kinds of object.
- [The membership sign](MATHEMATICAL_MOVES.md#membership) says the embedding is allowed to live among d-coordinate real vectors.
- [The superscript d](MATHEMATICAL_MOVES.md#powers) counts coordinate slots here; it is dimension, not an instruction to raise each number to a power.

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

Mary, John, and the book are possible sources for the word *she*. The sentence gives Mary the strongest relevance, the book a weaker connection, and John the weakest. Raw relevance can be negative or arbitrarily large, so it cannot yet say what share each source should contribute. Exponentiation turns every candidate into positive evidence; dividing by their shared total converts that evidence into portions of one whole.

### Only now do the symbols earn names

- **sᵢ** is the raw relevance score for candidate i.
- Exponentiation makes every weight positive, preserves ordering, suppresses negative evidence, and amplifies strong evidence.
- The denominator sums evidence from every candidate j because a weight is meaningful only relative to its competitors.
- Division makes all resulting weights sum to one.

For scores `[2, 4, 8]`, the largest score receives almost all the weight, but the others are not forbidden from contributing.

Softmax does not discover relevance. It converts already-computed relevance scores into a smooth distribution of attention.

### Why these operations are forced

- [Exponentiation](MATHEMATICAL_MOVES.md#exponential) makes every raw score positive while preserving order and turning score gaps into stable ratios. Squaring would make a large negative score look strong; clipping would destroy gap information.
- [The sum](MATHEMATICAL_MOVES.md#summation) gathers every candidate's positive weight because all candidates must share one unit of attention. A product would not describe a total available amount.
- [Dividing by that total](MATHEMATICAL_MOVES.md#division) converts each weight into its share. Without it, multiplying every score scale would change the amount of information mixed rather than only its distribution.

Only now can we compress that reasoning:

$$
\mathrm{softmax}(s_i)=\frac{e^{s_i}}{\sum_j e^{s_j}}
$$

[Return to the full excavation](excavations/009-softmax/README.md)

---

## Excavation 010 — Query, Key, and Value

A librarian hears, “Find me the book about a striped predator.” The request emphasizes *animal* and *stripes*. A catalogue card advertises the same properties; matching request-property to catalogue-property produces relevance. If that card wins three quarters of the attention, three quarters of the book's stored content—not three quarters of its catalogue description—travels into the answer. The request becomes the query, the catalogue becomes the key, and the retrievable content becomes the value only after those jobs are distinct.

### Only now do the symbols earn names

- **qᵢ** states what receiving token i needs; **kⱼ** states what source j offers.
- Multiplying matching coordinates rewards aligned needs and offers; opposite signs become negative evidence.
- Summing over feature r turns many alignments into one score sᵢⱼ.
- **αᵢⱼ** is that score after normalization: how much i listens to j.
- **vⱼ** is the content source j contributes; multiplying by α scales its voice.
- Summing over j combines every permitted source into output oᵢ.

Learned matrices create query, key, and value views from each current representation. Their formulas record three roles we already needed; they are not arbitrary symmetry.

### Why these operations are forced

- [The dot product](MATHEMATICAL_MOVES.md#dot-product) multiplies query height-need by key height-offer, stripe-need by stripe-offer, and so on, then adds those aligned agreements into one relevance score.
- [Multiplication inside the dot product](MATHEMATICAL_MOVES.md#multiplication) is required because a query feature should matter only when the matching key feature is present too; addition would reward a key for merely being large on unrelated features.
- [The first sum](MATHEMATICAL_MOVES.md#summation) combines feature-level evidence into one match. The second sum combines each source's value after its attention weight scales how loudly that source contributes.

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

In “The tiger that chased the deer was tired,” one reader follows grammar to discover what *was tired* describes, while another follows reference to keep tiger separate from deer. Averaging their notes too early destroys which evidence came from which question. Keeping the two notes side by side lets a later learned map decide how much grammar and reference the sentence needs.

### Only now do the symbols earn names

- **X** is the shared sequence of token representations.
- Each **headₕ** is an independent Q/K/V retrieval space, needed because relationships should not compete in one distribution.
- Concatenation preserves each report instead of averaging distinctions away.
- **H** counts the parallel heads.
- **W_O** is learned because the model must decide how the preserved reports should interact and return to the shared width.

Each head is the query–key–value mechanism from the previous excavation with independent learned projections.

The analogy has limits. Heads do not always become clean, human-readable professions. Some overlap; some are difficult to interpret. The architectural point is parallel relationship spaces, not a promise of tidy labels.

### Why these operations are forced

- [Concatenation](MATHEMATICAL_MOVES.md#concatenation) keeps the grammar expert, reference expert, and distance expert side by side. Adding them immediately would erase which head supplied which evidence.
- [Multiplication by the output matrix](MATHEMATICAL_MOVES.md#multiplication) lets the model learn how those preserved expert coordinates should interact; a fixed sum would impose the same mixture everywhere.

Only now can we compress that reasoning:

$$
\mathrm{MultiHead}(X)
=\mathrm{Concat}(\text{head}_1,\ldots,\text{head}_H)W_O
$$

[Return to the full excavation](excavations/011-multi-head-attention/README.md)

---

## Excavation 012 — Feed-Forward Networks

Attention tells the word *tiger* what the rest of the sentence said. Now imagine several small workshops inside that token: one notices whether an animal is dangerous, another recognizes whether it is acting or being described. A gate closes workshops whose evidence is negative and leaves useful ones open. A second mixing step combines only the surviving discoveries. Without the gate, the two mixing steps collapse into one fixed recipe and no conditional workshop can exist.

### Only now do the symbols earn names

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

### Why these operations are forced

- [Each matrix multiplication](MATHEMATICAL_MOVES.md#multiplication) lets learned weights decide how strongly one incoming feature should affect each hidden or outgoing feature.
- [Adding a bias](MATHEMATICAL_MOVES.md#addition) lets a detector have a baseline threshold even when all incoming features are zero; multiplication alone must always map zero input to zero output.
- [The activation function](MATHEMATICAL_MOVES.md#function-application) bends the intermediate result. Without that nonlinearity, the two matrix stages collapse into one linear transformation.

Only now can we compress that reasoning:

$$
\mathrm{FFN}(\mathbf{x})
=W_2 \sigma(W_1\mathbf{x}+\mathbf{b}_1)+\mathbf{b}_2
$$

[Return to the full excavation](excavations/012-feed-forward-networks/README.md)

---

## Excavation 013 — Residual Connections

A cartographer already has a useful map of the forest. A new survey reports that one trail bends half a kilometre east and one kilometre south. Replacing the whole map with that small report would destroy everything known; adding it as a correction preserves the map and changes only the trail. If the survey discovers nothing useful, adding a zero correction leaves the original untouched.

### Only now do the symbols earn names

- **x** is the representation worth preserving.
- **F(x)** is only the transformation's proposed correction, not a complete replacement.
- Addition keeps a direct route for x and makes “do nothing” possible when F(x)=0.
- **y** is the corrected state passed onward.

The block learns the **residual**—the difference between what exists and what should be added.

This direct route also gives learning signals a path that does not depend entirely on every learned transformation. Residual connections do not guarantee that a very deep model will train, but they make preservation and correction far easier.

Addition requires the input and proposal to have the same shape. That is why attention and feed-forward sublayers return to the model's shared width before joining the residual stream.

### Why these operations are forced

- [Addition](MATHEMATICAL_MOVES.md#addition) preserves the old message **x** and treats the block as a proposed change **F(x)**. Replacing x would force every block to reconstruct all useful old information.
- [F(x)](MATHEMATICAL_MOVES.md#function-application) says the proposed change depends on this exact incoming representation rather than being one fixed correction for every token.

Only now can we compress that reasoning:

$$
\mathbf{y}=\mathbf{x}+F(\mathbf{x})
$$

[Return to the full excavation](excavations/013-residual-connections/README.md)

---

## Excavation 014 — Layer Normalization

Three microphones hear the same roar at volumes 1, 2, and 3 because one sits closer to the tiger. Their shared centre is 2. Subtracting it leaves the pattern `[-1, 0, 1]`: quieter, typical, louder. Dividing by the pattern's spread makes that relative shape comparable with another set recorded by more sensitive microphones. A tiny safety amount is needed when all microphones report the same value and the spread is zero.

### Only now do the symbols earn names

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

### Why these operations are forced

- [Summing and dividing by d](MATHEMATICAL_MOVES.md#mean) finds the token's average feature level. A raw sum would grow merely because the representation has more coordinates.
- [Subtracting the mean](MATHEMATICAL_MOVES.md#subtraction) asks how each feature differs from this token's centre; addition would move the whole pattern farther from centre.
- [Squaring and averaging those differences](MATHEMATICAL_MOVES.md#variance) measures spread without quieter and louder features cancelling each other.
- [The square root](MATHEMATICAL_MOVES.md#square-root) returns variance to ordinary feature scale, and [division by that spread](MATHEMATICAL_MOVES.md#division) removes arbitrary volume while preserving relative shape.
- Adding ε is a safety floor: when every feature is identical, spread is zero and division would be undefined. See [addition](MATHEMATICAL_MOVES.md#addition) and [division](MATHEMATICAL_MOVES.md#division).

Only now can we compress that reasoning:

$$
\mu=\frac1d\sum_i x_i,
$$

$$
\sigma^2=\frac1d\sum_i(x_i-\mu)^2
$$

$$
\widehat{x}_i=\frac{x_i-\mu}{\sqrt{\sigma^2+\epsilon}}
$$

[Return to the full excavation](excavations/014-layer-normalization/README.md)

---

## Excavation 015 — How a Dead Brain Learns

A tiger alarm has one adjustable dial: how strongly a stripe should raise danger. The dial is currently 8, but repeated verified encounters suggest 3 would fit better. Its present squared mistake is 25, and a tiny upward test reveals that increasing the dial makes error rise with sensitivity 10. Reversing one tenth of that uphill suggestion moves the dial from 8 to 7 and lowers the mistake to 16.

### Only now do the symbols earn names

- **θ** is the current collection of learnable weights.
- **L** is the measured prediction failure.
- **∇L** collects how increasing each weight would increase loss.
- The minus sign reverses that uphill direction.
- **η** controls step size because direction alone does not say how far to move.
- The arrow means replace the old weights with the improved ones.

$\theta$ is the current state of the weights, $\nabla L$ is a vector of advised change, and $\eta$ controls how large a step to take.

### Why these operations are forced

- [The gradient](MATHEMATICAL_MOVES.md#gradient) collects one local loss sensitivity for every adjustable weight so the whole parameter state receives coordinated advice.
- [The minus sign](MATHEMATICAL_MOVES.md#negative-sign) reverses the gradient because the gradient points toward increasing loss and learning wants the locally decreasing direction.
- [Multiplying by η](MATHEMATICAL_MOVES.md#multiplication) chooses how much of that direction to trust. Without η, the gradient's magnitude would dictate the whole step even when it is too large or too small.
- The update arrow means “replace the old parameter state with this new one”; it is an action, not symmetric equality. See [arrows](MATHEMATICAL_MOVES.md#arrows).

Only now can we compress that reasoning:

$$
\theta\leftarrow\theta-\eta\nabla L
$$

[Return to the full excavation](excavations/015-learning/README.md)

---

## Excavation 017 — Probability — Counting What We Do Not Know

A tracker saw tigers after 2 of 10 comparable rustles. The raw count 2 means little without 10 opportunities. Dividing gives 0.2: under this evidence, two tenths of such rustles preceded a tiger.

### Only now do the symbols earn names

- **A** is the uncertain event we need to discuss.
- The numerator counts observations where A occurred.
- The denominator counts all comparable opportunities, because an isolated count has no scale.
- Division turns the count into a share between zero and one.
- **P(A)** names that evidence-dependent share, not a guarantee.

### Why these operations are forced

- [Division](MATHEMATICAL_MOVES.md#division) turns a tiger count into a share of comparable encounters. The count alone grows when we watch longer even if the underlying chance is unchanged.
- [Probability](MATHEMATICAL_MOVES.md#probability) preserves several possible causes as parts of one whole instead of forcing certainty from incomplete evidence.

Only now can we compress that reasoning:

$$
P(A)=\frac{\text{times }A\text{ occurred}}{\text{comparable observations}}
$$

[Return to the full excavation](excavations/017-probability/README.md)

---

## Excavation 018 — Likelihood — Which Hidden Story Produced This Evidence?

Story A says a deep print occurs 80% of the time; Story B says 20%. After observing a deep print, the same evidence has likelihood 0.8 under A and 0.2 under B, so A explains this clue four times as well.

### Only now do the symbols earn names

- **θ** is one proposed hidden explanation.
- **x** is the evidence already observed.
- The vertical bar means “under the assumption that.”
- **P(x|θ)** asks how expected this evidence would be if θ were true—the reversal forced by comparing stories.
- **L(θ|x)** names that same quantity when x is held fixed and explanations vary; it is not automatically a probability over θ.

### Why these operations are forced

- [The conditional bar](MATHEMATICAL_MOVES.md#conditional-bar) deliberately asks how expected this footprint would be **if** a tiger story were true. Reversing the two sides asks a different question and would silently mix evidence with prior belief.
- [Equality](MATHEMATICAL_MOVES.md#equals) renames that conditional evidence score as likelihood when θ is treated as the candidate story and x as fixed evidence.

Only now can we compress that reasoning:

$$
\mathcal{L}(\theta\mid x)=P(x\mid\theta)
$$

[Return to the full excavation](excavations/018-likelihood/README.md)

---

## Excavation 019 — Information — Why Surprise Needs a Number

An event with probability 1/2 carries 1 bit because -log₂(1/2)=1. An event with probability 1/8 carries 3 bits. The rarer observation eliminates more alternatives, so it teaches more.

### Only now do the symbols earn names

- **P(x)** measures how expected observation x was.
- The logarithm is needed because independent probabilities multiply while information from independent messages should add.
- Probabilities below one have negative logs, so the minus sign makes information nonnegative.
- A certain event has P=1 and therefore zero information; rarer events receive more.

### Why these operations are forced

- [The logarithm](MATHEMATICAL_MOVES.md#logarithm) is forced because independent probabilities multiply while learned information should accumulate by addition. It converts a product of probabilities into a sum of surprises.
- [The negative sign](MATHEMATICAL_MOVES.md#negative-sign) reverses the negative log of probabilities below one, making rare events carry larger positive information and a certain event carry zero.
- Using 1/P would also grow for rare events, but its independent surprises would multiply rather than add; that is why it fails the job we established.

Only now can we compress that reasoning:

$$
I(x)=-\log P(x)
$$

[Return to the full excavation](excavations/019-information/README.md)

---

## Excavation 020 — Entropy — Measuring the Uncertainty of a Whole Situation

For a fair coin, each outcome has probability 1/2 and information 1 bit. Weighting gives 0.5×1+0.5×1=1 expected bit. A coin guaranteed heads gives -log₂(1)=0, so its entropy is zero.

### Only now do the symbols earn names

- **pᵢ** is the probability of possible outcome i.
- **−log pᵢ** is the information received if i occurs.
- Multiplying by pᵢ weights that surprise by how often it is expected to occur.
- Summing over every i computes average surprise before the outcome is known.
- **H(P)** names uncertainty of the whole distribution P.

### Why these operations are forced

- [Multiplying each surprise by pᵢ](MATHEMATICAL_MOVES.md#multiplication) lets common outcomes speak more often than rare ones when measuring the uncertainty of the whole situation.
- [Summing](MATHEMATICAL_MOVES.md#summation) combines those mutually exclusive outcome contributions into one expected uncertainty; multiplying them would make any certain zero-surprise outcome erase all others.
- [The log](MATHEMATICAL_MOVES.md#logarithm) still converts probability products into additive information, and [the minus sign](MATHEMATICAL_MOVES.md#negative-sign) keeps that information nonnegative.

Only now can we compress that reasoning:

$$
H(P)=-\sum_i p_i\log p_i
$$

[Return to the full excavation](excavations/020-entropy/README.md)

---

## Excavation 021 — Cross-Entropy — Paying for Confidently Wrong Predictions

Reality says the answer is tiger. A model assigning tiger 0.9 pays -log(0.9), about 0.105. A model assigning 0.01 pays about 4.605. The confident wrong model is charged far more.

### Only now do the symbols earn names

- **P** is the distribution reality supplies; pᵢ weights which outcomes actually occur.
- **Q** is the model's proposed distribution; qᵢ is the probability it assigned outcome i.
- **−log qᵢ** makes confident neglect extremely costly.
- Summing the reality-weighted costs gives one expected prediction penalty H(P,Q).

### Why these operations are forced

- [−log qᵢ](MATHEMATICAL_MOVES.md#logarithm) charges a large price when the model assigns tiny probability to what occurs; logarithms also let sequence costs add instead of multiplying many small probabilities.
- [Multiplying by pᵢ](MATHEMATICAL_MOVES.md#multiplication) asks reality how often that charge should count. Without pᵢ, impossible and common outcomes would receive equal influence.
- [The sum](MATHEMATICAL_MOVES.md#summation) forms one expected bill across outcomes. A product would allow one zero-weighted outcome to erase every other prediction error.

Only now can we compress that reasoning:

$$
H(P,Q)=-\sum_i p_i\log q_i
$$

[Return to the full excavation](excavations/021-cross-entropy/README.md)

---

## Excavation 022 — Derivatives — Asking One Weight What It Changed

A village adjusts one alarm dial controlling how much smoke is needed before ringing a bell. At setting 3 the false-alarm cost is 9. Raising the dial by only 0.001 changes the cost to about 9.006001. The extra cost divided by the tiny dial movement is about 6. Repeating with ever smaller movements reveals the local sensitivity at the current setting rather than the effect of one arbitrary jump.

### Only now do the symbols earn names

- **w** is the one weight whose responsibility we are probing.
- **ε** is a small experimental nudge.
- **L(w+ε)−L(w)** measures the loss change caused by that nudge.
- Dividing by ε turns total change into change per unit of weight.
- The limit shrinks the nudge so the answer becomes local rather than dependent on an arbitrary test step.
- **dL/dw** names that local sensitivity.

### Why these operations are forced

- [The numerator subtracts](MATHEMATICAL_MOVES.md#subtraction) old loss from nudged loss to isolate what the nudge changed; adding them would mix level with change.
- [Division by the weight nudge](MATHEMATICAL_MOVES.md#division) converts raw loss change into loss change **per unit of weight change**, making different probe sizes comparable.
- [The limit](MATHEMATICAL_MOVES.md#limit) lets the probe approach zero so curvature across a large jump does not disguise the local slope; setting ε equal to zero directly would divide by zero.

Only now can we compress that reasoning:

$$
\frac{dL}{dw}=\lim_{\epsilon\to0}\frac{L(w+\epsilon)-L(w)}{\epsilon}
$$

[Return to the full excavation](excavations/022-derivatives/README.md)

---

## Excavation 023 — The Chain Rule — Following One Change Through Many Machines

Turn an oven knob slightly. The first mechanism doubles that movement into a fuel change; the next triples the fuel change into temperature; the bread-loss rule magnifies the temperature error fourfold. A one-unit knob change therefore becomes 2, then 6, then 24 units of final sensitivity. Each machine contributes one local multiplier, and the whole causal path requires all of them.

### Only now do the symbols earn names

- **w→x→y→L** is the causal path through successive machines.
- Each fraction is one local sensitivity: how its output changes when its input changes.
- Multiplication is forced because a change is scaled at every link it traverses.
- The product gives the effect of w on L without pretending they touch directly.

### Why these operations are forced

- Each [derivative](MATHEMATICAL_MOVES.md#derivative) is a local conversion rate: loss per y, y per x, and x per weight.
- [Multiplying the rates](MATHEMATICAL_MOVES.md#multiplication) is forced because one unit of weight change produces dx/dw units of x, each produces dy/dx units of y, and each of those produces dL/dy loss. Adding would mix rates with incompatible units.

Only now can we compress that reasoning:

$$
\frac{dL}{dw}=\frac{dL}{dy}\frac{dy}{dx}\frac{dx}{dw}
$$

[Return to the full excavation](excavations/023-chain-rule/README.md)

---

## Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It

One shared dough temperature affects two outcomes: crust and centre. The crust branch sends blame 3 through local sensitivity 2, contributing 6. The centre branch sends blame 4 through sensitivity 5, contributing 20. Because both outcomes depended on the same temperature, the baker must return total blame 26 to that shared decision. Computing either downstream suffix twice would add work without adding evidence.

### Only now do the symbols earn names

- **x̄** means accumulated sensitivity of final loss to intermediate x.
- A node can influence several child results y, so every downstream path must contribute.
- **ȳ** is blame already accumulated at child y.
- **∂y/∂x** says how strongly x affected that child locally.
- Multiplication passes blame through one edge; summation combines all outgoing paths.

### Why these operations are forced

- [The partial derivative](MATHEMATICAL_MOVES.md#partial-derivative) measures one local edge while other inputs are held fixed.
- [Multiplying child blame by edge sensitivity](MATHEMATICAL_MOVES.md#multiplication) passes downstream responsibility through that edge; either factor being zero should block that path.
- [Summing over children](MATHEMATICAL_MOVES.md#summation) reunites separate downstream routes that all depended on x. Multiplication would incorrectly make one zero-blame route erase every other route.

Only now can we compress that reasoning:

$$
\bar{x}=\sum_{y\in children(x)}\bar{y}\frac{\partial y}{\partial x}
$$

[Return to the full excavation](excavations/024-backpropagation/README.md)

---

## Excavation 025 — Gradient Descent — Teaching a Tiny Network

Return to the tiger alarm's stripe dial. It is 8; verified encounters suggest 3; the squared mistake is 25; and the local uphill sensitivity is 10. Moving the full ten units lands at −2, equally far from the target on the other side. Direction alone has not taught us distance. Taking one tenth of the proposed correction moves the dial to 7 and lowers the mistake to 16. That chosen fraction is the learning rate.

### Only now do the symbols earn names

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

### Why these operations are forced

- [The time indices](MATHEMATICAL_MOVES.md#indices) distinguish the parameter state before update t from the state after it.
- [The gradient](MATHEMATICAL_MOVES.md#gradient) supplies one local uphill sensitivity for each parameter; [the minus sign](MATHEMATICAL_MOVES.md#negative-sign) reverses that direction toward lower loss.
- [Multiplying by η](MATHEMATICAL_MOVES.md#multiplication) supplies the missing travel distance. A direction alone does not say whether to move one millimetre or one kilometre.

Only now can we compress the same procedure:

$$
\theta_{t+1}=\theta_t-\eta\nabla_\theta L
$$

[Return to the full excavation](excavations/025-gradient-descent/README.md)

---

## Excavation 026 — Mini-Batches — Learning from More Than One Example

A tiger detector has two adjustable dials: how much to trust stripes and how much to trust movement. A clear morning photograph recommends raising those dials by 2 and 4. A muddy side view recommends 4 and 2. A night photograph recommends 3 and 3. For the stripe dial, the three witnesses propose 2+4+3=9, so their average advice is 3. The movement dial also averages to 3. If we merely added their advice, inviting three witnesses instead of one would triple the step even when their average opinion had not changed.

### Only now do the symbols earn names

- **B** is the selected mini-batch and **|B|** its number of examples.
- **Lᵢ** is loss for example i; **∇_θLᵢ** is that example's proposed parameter direction.
- Summing combines the witnesses.
- Dividing by batch size prevents merely using more examples from making the step proportionally larger.
- **g_B** is the batch's less noisy gradient estimate.

### Why these operations are forced

- [The sum](MATHEMATICAL_MOVES.md#summation) lets every selected example contribute its proposed parameter correction. Multiplying gradients would turn one zero coordinate into a veto and would not represent a council's combined advice.
- [Dividing by |B|](MATHEMATICAL_MOVES.md#division) asks for advice per example, so merely inviting twice as many witnesses does not double the update.
- [i ∈ B](MATHEMATICAL_MOVES.md#membership) restricts the sum to examples actually selected for this mini-batch; [|B|](MATHEMATICAL_MOVES.md#cardinality) means the number of those examples.

Only now can we compress that reasoning:

$$
g_B=\frac{1}{|B|}\sum_{i\in B}\nabla_\theta L_i
$$

[Return to the full excavation](excavations/026-mini-batches/README.md)

---

## Excavation 027 — Learning Rate — How Large Should the Next Step Be?

The tiger alarm's stripe dial is again 8, and the local uphill sensitivity is 10. Moving opposite the entire suggestion sends the dial to −2 and jumps across the best setting. Trusting one tenth moves it to 7; trusting one hundredth moves it to 7.9. All three moves use the same downhill direction. The learning rate answers the separate human question: how much of that local advice should we trust now?

### Only now do the symbols earn names

- **g_t** is the downhill evidence measured at step t.
- **η_t** converts direction into a chosen travel distance and may change with time.
- The minus sign moves against increasing loss.
- **θ_t** and **θ_{t+1}** distinguish the old and updated parameter states.

### Why these operations are forced

- [gₜ](MATHEMATICAL_MOVES.md#gradient) gives direction but not distance.
- [Multiplying by ηₜ](MATHEMATICAL_MOVES.md#multiplication) turns the direction into a controllable step for this time t; adding η would shift every coordinate regardless of the gradient's direction.
- [Subtraction](MATHEMATICAL_MOVES.md#negative-sign) moves opposite the locally uphill gradient rather than making loss rise faster.

Only now can we compress that reasoning:

$$
\theta_{t+1}=\theta_t-\eta_t g_t
$$

[Return to the full excavation](excavations/027-learning-rate/README.md)

---

## Excavation 028 — Momentum — Remembering Which Way Downhill Persists

Three small groups inspect tiger tracks. Each recommends changing two detector dials: stripes and movement. Their advice is `[3,1]`, `[3,-1]`, and `[3,1]`. Now the coordinates are not anonymous: every group agrees that stripe trust should rise by 3, while movement advice flips with noisy tracks. Remembering recent directions reinforces the persistent stripe evidence and lets the contradictory movement evidence partly cancel.

### Only now do the symbols earn names

- **g_t** is the newest noisy gradient.
- **v_{t−1}** stores direction accumulated previously.
- **β** between zero and one controls how much old motion survives; repeated multiplication makes old advice fade.
- Addition combines memory with new evidence into velocity v_t.
- **η** scales that velocity before it changes θ.

### Why these operations are forced

- [Multiplying old velocity by β](MATHEMATICAL_MOVES.md#multiplication) fades memory instead of remembering every ancient gradient equally. β near zero forgets quickly; β near one preserves direction longer.
- [Adding the new gradient](MATHEMATICAL_MOVES.md#addition) lets current evidence join the surviving past direction. Multiplying them would erase memory wherever either vector contains zero.
- The final [η scaling](MATHEMATICAL_MOVES.md#multiplication) chooses travel distance and [the minus sign](MATHEMATICAL_MOVES.md#negative-sign) turns remembered uphill direction into a downhill update.

Only now can we compress that reasoning:

$$
v_t=\beta v_{t-1}+g_t
$$

$$
\theta_{t+1}=\theta_t-\eta v_t
$$

[Return to the full excavation](excavations/028-momentum/README.md)

---

## Excavation 029 — Initialization — Where Should Learning Begin?

Imagine one hundred weak sensors feeding an alarm. If every sensor signal and every connecting weight is typically near 1, adding all one hundred contributions produces a signal near 100; deeper layers can make it explode further. Giving the starting weights a typical size near one tenth keeps the combined signal near the scale of one useful observation. The factor `1/√100` is therefore a scale-preserving choice, not a magic constant.

### Only now do the symbols earn names

- **w** is one newly initialized weight.
- **Var(w)** measures the typical squared spread of starting weights, not their meaning.
- **n_in** counts signals entering the neuron.
- Dividing by n_in compensates for adding more independent inputs, preventing their combined signal scale from growing with width.
- “Approximately” leaves room for activation-specific constants such as Xavier or He scaling.

### Why these operations are forced

- [Variance](MATHEMATICAL_MOVES.md#variance) describes the typical squared size of random starting weights without requiring every sampled weight to have that exact magnitude.
- [Dividing by the number of incoming signals](MATHEMATICAL_MOVES.md#division) makes each individual weight smaller when more signals will be added, preventing total activation scale from growing with fan-in.
- [The approximately sign](MATHEMATICAL_MOVES.md#approximation) admits a design target rather than claiming every finite random sample has exactly this variance; see [equality](MATHEMATICAL_MOVES.md#equals) for the stronger claim it avoids.

Only now can we compress that reasoning:

$$
\mathrm{Var}(w)\approx\frac{1}{n_{\text{in}}}
$$

[Return to the full excavation](excavations/029-initialization/README.md)

---

## Excavation 030 — Activation Functions — Why a Network Must Bend

A gatekeeper receives a danger signal. Two ordinary scaling rules—double it, then triple it—always behave like one rule that multiplies by six. Adding more such rules has created no new decision. Put a gate between them: negative evidence is closed to zero while positive evidence continues. Now the same machinery treats warning evidence and reassuring evidence differently, something one multiplication cannot reproduce.

### Only now do the symbols earn names

- **x** is the incoming representation.
- **W** mixes its features; **b** permits learned thresholds and offsets.
- **φ** is the necessary nonlinear gate; without it, stacked layers collapse into one linear map.
- **h** is the hidden representation after both mixing and gating.

### Why these operations are forced

- [Wx](MATHEMATICAL_MOVES.md#multiplication) lets every learned input weight scale and mix its matching feature; [adding b](MATHEMATICAL_MOVES.md#addition) supplies a learnable baseline.
- [Applying φ](MATHEMATICAL_MOVES.md#function-application) bends the result. Without φ, repeated multiply-and-add stages remain one linear map, no matter how many layers are stacked.

Only now can we compress that reasoning:

$$
h=\phi(Wx+b)
$$

[Return to the full excavation](excavations/030-activation-functions/README.md)

---

## Excavation 031 — Overfitting — When Perfect Memory Pretends to Be Intelligence

A model has training loss 0.02 and unseen loss 0.17. Subtracting gives a gap of 0.15. The low training number shows memory; the gap measures how much success disappeared outside it.

### Only now do the symbols earn names

- **L_train** measures error on examples allowed to shape the model.
- **L_unseen** measures error on held-out observations.
- Subtraction isolates deterioration outside memory instead of confusing it with absolute task difficulty.
- A positive generalization gap is evidence that training success did not fully survive.

### Why these operations are forced

- [Unseen loss minus training loss](MATHEMATICAL_MOVES.md#subtraction) isolates how much performance deteriorates beyond memorized examples. Adding the losses would measure total error, not the transfer gap.
- The order matters: a positive answer naturally means unseen cases are worse. Reversing the subtraction would reverse that interpretation.

Only now can we compress that reasoning:

$$
\text{generalization gap}=L_{\text{unseen}}-L_{\text{train}}
$$

[Return to the full excavation](excavations/031-overfitting/README.md)

---

## Excavation 032 — Regularization — Making Memorization More Expensive

Two models have data loss 2. Model A has squared-weight sum 100; B has 4. With lambda 0.1, totals are 12 and 2.4. The penalty makes the equally fitting but less extreme model preferable.

### Only now do the symbols earn names

- **L_data** rewards fitting observations.
- **θ** contains the weights; squaring and summing them creates ||θ||² without signed cancellation.
- **λ** expresses how strongly we prefer smaller machinery relative to data fit.
- Addition forces training to negotiate prediction accuracy and complexity in one objective.

### Why these operations are forced

- [Addition](MATHEMATICAL_MOVES.md#addition) puts prediction cost and complexity cost on one bill so optimization cannot improve one without seeing the other.
- [The squared norm](MATHEMATICAL_MOVES.md#norm) combines all parameter magnitudes without positive and negative weights cancelling, while making exceptionally large weights cost disproportionately more.
- [λ scales the penalty](MATHEMATICAL_MOVES.md#multiplication) because the data cannot decide by itself how much simplicity to trade for fit. Adding λ as a constant would not change which parameters are preferred.

Only now can we compress that reasoning:

$$
L_{\text{total}}=L_{\text{data}}+\lambda\lVert\theta\rVert^2
$$

[Return to the full excavation](excavations/032-regularization/README.md)

---

## Excavation 033 — Validation — Testing Without Peeking at the Final Exam

With 100 examples, use 60 to change weights, 20 to choose learning rate, and keep 20 sealed. If the sealed 20 guide choices, they stop being an honest final test.

### Only now do the symbols earn names

- **D** is all available data.
- The three named subsets exist because weight learning, design choices, and final measurement must not share feedback.
- Union means they reconstruct the available collection.
- The intended split also requires no example to leak between sets, even though the compact union symbol alone does not state disjointness.

### Why these operations are forced

- [Union](MATHEMATICAL_MOVES.md#union) says the complete dataset contains the members assigned to training, validation, or test roles. Ordinary addition is for numeric quantities, not for joining collections of examples.
- Separate names preserve separate responsibilities; the union sign alone does not guarantee the sets do not overlap, so the split procedure must enforce that boundary.

Only now can we compress that reasoning:

$$
D=D_{\text{train}}\cup D_{\text{validation}}\cup D_{\text{test}}
$$

[Return to the full excavation](excavations/033-validation/README.md)

---

## Excavation 034 — Generalization — What Should Survive Beyond the Dataset?

Suppose future cases have losses 1,0,2,1. Their average is 1, our estimate of future risk. Averaging training losses instead would answer how well we remember the past, not deployment.

### Only now do the symbols earn names

- **θ** is one trained model and **f_θ(x)** its prediction for input x.
- **L(f_θ(x),y)** measures failure against outcome y.
- **P_future** names the deployment world we actually care about.
- Sampling (x,y) from that world prevents training data from silently defining success.
- The expectation averages loss over future cases; **R(θ)** names that future risk.

### Why these operations are forced

- [Expectation](MATHEMATICAL_MOVES.md#expectation) weights each future case by how often the deployment world produces it, rather than pretending every possible case is equally common.
- [fθ(x)](MATHEMATICAL_MOVES.md#function-application) feeds input x through the model with parameters θ; the outer loss compares that prediction with the actual y.
- The sampling mark ties the average to the future distribution. Training risk would answer a different question even if the same loss function were used.

Only now can we compress that reasoning:

$$
R(\theta)=\mathbb{E}_{(x,y)\sim P_{\text{future}}}[L(f_\theta(x),y)]
$$

[Return to the full excavation](excavations/034-generalization/README.md)

---

## Excavation 035 — A Tiny Neural Network — Assemble the Entire Learning Loop

Input 2 is mixed into a hidden signal, gated, and produces prediction 0.7. If the target is 1, loss sends correction backward through the same steps, changes weights, and the next forward pass may produce 0.8. The arrows are one loop.

### Only now do the symbols earn names

- **x** is observed input.
- **Wx+b** mixes features and supplies offsets.
- **φ** bends the mapping so depth adds new behavior.
- **ŷ** is the prediction and **L** measures its failure.
- **∇_θL** assigns local correction directions to all parameters θ.
- **θ′** is the updated state; the arrows show the forward path continuing into feedback rather than separate facts.

### Why these operations are forced

- [Arrows](MATHEMATICAL_MOVES.md#arrows) preserve process order: data is transformed, activated, predicted, priced, blamed, and only then used to update parameters. Equality would wrongly claim those stages are the same object.
- [The gradient stage](MATHEMATICAL_MOVES.md#gradient) changes a single loss into parameter-by-parameter advice; the final primed θ names the resulting new state.

Only now can we compress that reasoning:

$$
x\to Wx+b\to\phi(\cdot)\to\hat y\to L\to\nabla_\theta L\to\theta^\prime
$$

[Return to the full excavation](excavations/035-tiny-neural-network/README.md)

---

## Excavation 036 — Tokenization: What Can a Language Model See?

In low, lower, lowest, pair l-o appears three times, more than e-r once. Counting selects l-o; merging creates lo. Recounting can then select lo-w and create reusable low.

### Only now do the symbols earn names

- **a and b** are neighboring current tokens; c(a,b) counts their repeated adjacency because repetition is the evidence for reuse.
- The star marks the pair selected for merging.
- **arg max** returns the pair itself, not its count, because that pair must be replaced.
- Maximizing over every candidate pair makes the merge arise from the corpus rather than a hand-written linguistic rule.

Count, choose, merge, and repeat. The symbols only compress the procedure already needed.

### Why these operations are forced

- [The first equality](MATHEMATICAL_MOVES.md#equals) defines c(a,b) as the observed adjacency count; the parentheses keep the candidate pair together.
- [Arg max](MATHEMATICAL_MOVES.md#arg-max) returns the pair whose count is largest because the tokenizer must know **what to merge**. Max alone would return only the winning count.
- [The star](MATHEMATICAL_MOVES.md#symbol-decorations) marks the selected winner; it is a label on a and b, not multiplication or exponentiation.

Only now can we compress that reasoning:

$$
c(a,b)=\text{number of adjacent occurrences of }(a,b)
$$

$$
(a^*,b^*)=\underset{(a,b)}{\text{arg max}} c(a,b)
$$

[Return to the full excavation](excavations/036-tokenization/README.md)

---

## Excavation 037 — Input Embeddings: Giving Tokens Learnable Coordinates

The tokenizer assigns shelf address 2 to *tiger*. Looking up address 2 retrieves a small card of adjustable coordinates learned from tiger's usage. The address itself says nothing about meaning; moving the tiger card to shelf 7 would not change its learned contents. The table is therefore a collection of learned starting descriptions, while the token ID is merely the address used to fetch one.

### Only now do the symbols earn names

- **V** is the vocabulary and **|V|** its number of token addresses.
- **d** is the compact representation width chosen for the model.
- **E** therefore needs one row per token and d learnable coordinates per row.
- **i** is a token ID used only to select row E[i]; **x_i** is the retrieved meaning-bearing vector.
- **e_i** is the one-hot selector. Multiplying e_i by E produces the same row, explaining why direct lookup is valid and cheaper.

Multiplying by a one-hot vector merely selects one row, so an implementation can perform the lookup directly.

### Why these operations are forced

- [E ∈ ℝ](MATHEMATICAL_MOVES.md#membership) states the embedding table's allowed shape: one row per vocabulary token and d real coordinates per row.
- [E[i]](MATHEMATICAL_MOVES.md#indices) treats token ID i as a shelf address. It retrieves one row rather than using the ID as a meaningful magnitude.
- [One-hot multiplication](MATHEMATICAL_MOVES.md#multiplication) gives the same lookup because every zero row contribution vanishes and the single one-valued row survives; addition then combines the row contributions.

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

Compare “tiger chases deer” with “deer chases tiger.” The same three word cards appear, so content alone cannot distinguish hunter from hunted. Give the first slot one reusable position mark, the second another, and the third another. Adding the appropriate mark to each word leaves *tiger* recognizable while also telling later attention whether this occurrence came first or last.

### Only now do the symbols earn names

- **token_i** is the vocabulary address appearing at sequence location i.
- **E[token_i]** retrieves what that token currently represents.
- **P_i** represents where the occurrence sits.
- Addition is possible because both vectors share width and is necessary so every later operation receives content and position together.
- **z_i** is the combined input at position i.

### Why these operations are forced

- [Addition](MATHEMATICAL_MOVES.md#addition) overlays the token's learned content and this occurrence's position while keeping the vector width unchanged. Concatenation would widen every later layer and keep the two sources permanently separate.
- [The shared index i](MATHEMATICAL_MOVES.md#indices) forces the token and position from the same slot to meet; mismatched indices would attach the wrong location.

Only now can we compress that reasoning:

$$
z_i=E[token_i]+P_i
$$

The equation arrives after every operation has a job.

[Return to the full excavation](excavations/038-position/README.md)

---

## Excavation 039 — Causal Masking — Preventing the Future from Leaking Backward

While learning from “the tiger sleeps,” the model sees the complete training sentence. At the position after *the*, the correct next token *tiger* is already sitting to the right. Place an impassable barrier on every connection pointing into the future. In score language, those forbidden paths receive a value whose exponential contribution becomes zero, while present and earlier words remain available.

### Only now do the symbols earn names

- **i** is the receiving position and **j** a possible source position.
- When j≤i, the source is present or past, so adding zero leaves its attention score unchanged.
- When j>i, the source is future; adding −∞ makes its later softmax weight zero.
- **M_ij** stores that allowed-or-forbidden correction for every pair.

### Why these operations are forced

- [Cases](MATHEMATICAL_MOVES.md#cases) are forced because visible and forbidden positions obey genuinely different rules.
- [j ≤ i and j > i](MATHEMATICAL_MOVES.md#inequalities) divide earlier-or-current keys from future keys for query position i.
- Zero leaves an allowed attention score unchanged. [Negative infinity](MATHEMATICAL_MOVES.md#negative-sign) makes a forbidden score's exponential weight zero after softmax; a large positive value would do the opposite.

Only now can we compress that reasoning:

$$
M_{ij}=\begin{cases}0&j\le i\\-\infty&j>i\end{cases}
$$

The equation arrives after every operation has a job.

[Return to the full excavation](excavations/039-causal-mask/README.md)

---

## Excavation 040 — Next-Token Examples — One Sentence Becomes Many Lessons

Tokens [the,cat,slept] become inputs [the,cat] and targets [cat,slept]. One forward pass therefore asks “after the?” and “after the cat?” at separate positions.

### Only now do the symbols earn names

- **t₀…t_n** are consecutive tokens from one observed sequence.
- Input x stops one token early because each position needs an answer to its right.
- Target y starts one token later so y_i is exactly the next token after x_i.
- The shared length lets one forward pass create a supervised lesson at every position.

### Why these operations are forced

- [Parentheses](MATHEMATICAL_MOVES.md#brackets) keep each ordered token sequence intact; summing the tokens would destroy both identity and order.
- [The shifted indices](MATHEMATICAL_MOVES.md#indices) remove the final token from inputs and the first token from targets, so target position i is exactly the next token after input position i.

Only now can we compress that reasoning:

$$
x=(t_0,\ldots,t_{n-1})
$$

$$
y=(t_1,\ldots,t_n)
$$

The equation arrives after every operation has a job.

[Return to the full excavation](excavations/040-next-token-examples/README.md)

---

## Excavation 041 — Logits — Let Every Vocabulary Token Compete

After reading “the striped animal is a,” the model holds one contextual description. Every vocabulary candidate now presents a learned question: how well does this description support *tiger*, *river*, *sleeping*, and so on? Matching the same context against each candidate produces one raw score per word. Those scores are logits; they are competitors, not probabilities yet.

### Only now do the symbols earn names

- **h** is one contextual token vector containing what the Transformer currently knows.
- **W_vocab** has one scoring direction per vocabulary candidate; multiplication compares h with all candidates at once.
- **b** allows each token a learned baseline tendency.
- **ℓ_i** is the resulting unconstrained logit for candidate i—not yet a probability.

### Why these operations are forced

- [Multiplication by Wvocab](MATHEMATICAL_MOVES.md#multiplication) lets every contextual feature contribute a learned amount to every vocabulary candidate's score.
- [The bias](MATHEMATICAL_MOVES.md#addition) gives each vocabulary token a learned baseline tendency even when the contextual vector is zero.
- The index i selects one output candidate; it does not mean the token with the largest ID should win. See [indices](MATHEMATICAL_MOVES.md#indices).

Only now can we compress that reasoning:

$$
\ell_i=hW_{\text{vocab}}+b
$$

The equation arrives after every operation has a job.

[Return to the full excavation](excavations/041-logits/README.md)

---

## Excavation 042 — Vocabulary Probabilities — Turning Scores into a Prediction

Suppose *tiger* receives score 2 and *leopard* score 1 after “the striped animal is a.” Softmax turns them into shares of about 0.73 and 0.27. If the observed answer is *tiger*, the model pays the surprise of assigning it 0.73. Had it assigned tiger only 0.01, the penalty would be far larger. The loss therefore records not merely whether the guess won, but how much belief the model risked on reality.

### Only now do the symbols earn names

- **ℓ_i** is candidate i's raw score.
- Dividing exponentiated evidence by the sum over all j creates positive probabilities p_i that total one.
- **y** is the observed next-token index, so p_y is the probability assigned to what happened.
- The logarithm converts products across examples into sums and the minus sign makes low assigned probability a large positive loss L.

### Why these operations are forced

- [Exponentials](MATHEMATICAL_MOVES.md#exponential) create positive candidate weights and preserve score order; squaring would make strongly negative logits look desirable.
- [Summing all weights](MATHEMATICAL_MOVES.md#summation) measures the whole amount to be shared, and [division](MATHEMATICAL_MOVES.md#division) turns each candidate's weight into a probability share.
- [The log](MATHEMATICAL_MOVES.md#logarithm) turns the probability assigned to the observed token into additive information cost; [the minus sign](MATHEMATICAL_MOVES.md#negative-sign) makes low probability expensive and certainty cost zero.

Only now can we compress that reasoning:

$$
p_i=\frac{e^{\ell_i}}{\sum_j e^{\ell_j}}
$$

$$
L=-\log p_y
$$

The equation arrives after every operation has a job.

[Return to the full excavation](excavations/042-vocabulary-probabilities/README.md)

---

## Excavation 043 — Sampling — Choosing Without Always Taking the Maximum

After “the tiger,” suppose *sleeps* is more likely than *runs*, but both make sense. Always choosing the winner makes every story follow the same path. Imagine a temperature dial on indecision: cooling enlarges the evidence gap and makes *sleeps* dominate; heating shrinks the gap and lets *runs* remain plausible. Dividing every logit by the same temperature implements that dial before sampling.

### Only now do the symbols earn names

- **ℓ_i** is candidate i's raw logit.
- **T** is temperature: dividing by T changes score gaps before exponentiation.
- T<1 enlarges gaps and sharpens choices; T>1 shrinks gaps and spreads probability.
- Exponentiation preserves ranking while making evidence positive.
- Summing over every j and dividing normalizes the adjusted evidence into p_i(T).

### Why these operations are forced

- [Dividing every logit by T](MATHEMATICAL_MOVES.md#division) changes score gaps before probabilities are formed. T below one enlarges gaps; T above one shrinks them. Adding T would shift every score equally and softmax would not change at all.
- [Exponentiation](MATHEMATICAL_MOVES.md#exponential) then turns the adjusted gaps into positive ratios, while [summing](MATHEMATICAL_MOVES.md#summation) and dividing make one probability distribution.

Only now can we compress that reasoning:

$$
p_i(T)=\frac{e^{\ell_i/T}}{\sum_j e^{\ell_j/T}}
$$

The equation arrives after every operation has a job.

[Return to the full excavation](excavations/043-sampling/README.md)

---

## Excavation 044 — Context Windows — How Much Past Can the Model Carry?

Four words create sixteen possible question–source comparisons: each of four positions may inspect four positions. Eight words create sixty-four. The reader can see the growth by drawing the square table: doubling each side multiplies the number of cells by four. The cost comes from pairwise looking, not from storing eight words alone.

### Only now do the symbols earn names

- **n** is the number of tokens inside the active context.
- Each of n queries can compare with n keys, creating roughly n×n score pairs.
- That repeated pairwise work is why cost grows proportionally to n² rather than n.
- The proportional sign is used because heads, width, batching, and implementation add constants omitted from this scaling argument.

### Why these operations are forced

- [Proportionality](MATHEMATICAL_MOVES.md#proportionality) states the growth pattern without pretending every implementation has the same fixed cost.
- [The square](MATHEMATICAL_MOVES.md#powers) appears because each of n query positions can compare with n key positions, creating n×n pairs. A linear n would count only one comparison per token.

Only now can we compress that reasoning:

$$
\text{attention cost}\propto n^2
$$

The equation arrives after every operation has a job.

[Return to the full excavation](excavations/044-context-window/README.md)

---

## Excavation 045 — A Tiny GPT — Close the Prediction Loop

Begin with the prompt “the tiger.” Its token addresses fetch learned starting descriptions; position marks preserve order; masked attention gathers only allowed context; token workshops transform what was gathered; and the output scores every possible next word. Suppose sampling chooses *sleeps*. Appending that choice creates “the tiger sleeps,” and the same mechanism now faces a new prediction. The language model exists only when this entire loop closes.

### Only now do the symbols earn names

- **tokens** are discrete addresses produced by the tokenizer.
- **embeddings** turn addresses into vectors; Transformer **blocks** contextualize them under causal masking.
- **logits** score every next-token candidate; **loss** compares those scores with the observed answer.
- **update** changes parameters using backpropagated error.
- **sample** chooses a continuation and feeds it back as the next token.
- The arrows encode one closed causal loop, not an unexplained algebraic equality.

### Why these operations are forced

- [Arrows](MATHEMATICAL_MOVES.md#arrows) show dependency and order rather than equality: tokens become representations, representations produce scores, loss produces gradients, and an update changes what the next sample can be.
- The loop matters more than any isolated sign. Removing one arrow breaks the causal path by which observed text can change future generation.

Only now can we compress that reasoning:

$$
tokens\to embeddings\to blocks\to logits\to loss\to update\to sample
$$

The equation arrives after every operation has a job.

[Return to the full excavation](excavations/045-tiny-gpt/README.md)

---

## Excavation 046 — Perplexity — How Surprised Is the Model?

Model A assigns probability 0.5 to each of three observed next tokens. Each costs about 0.693 nats; the average is 0.693. Exponentiating gives 2. The model behaves as if it were choosing among two equally plausible options at each step.

### Only now do the symbols earn names

The token count divides total surprise so longer sentences are comparable. Negative logs turn small assigned probabilities into large costs. Exponentiation reverses the log and returns the result to a probability-like choice scale.

### Why these operations are forced

- [The log](MATHEMATICAL_MOVES.md#logarithm) converts the product of many observed-token probabilities into additive surprise, avoiding a tiny unstable product for a long sentence.
- [Summing](MATHEMATICAL_MOVES.md#summation) collects surprise from every actual next token, and [dividing by n](MATHEMATICAL_MOVES.md#division) makes sentences of different lengths comparable per token.
- [The minus sign](MATHEMATICAL_MOVES.md#negative-sign) makes low probabilities costly; [the final exponential](MATHEMATICAL_MOVES.md#exponential) reverses the log scale so the answer reads like an equivalent number of equally likely choices.

Only now can we compress the exact procedure:

$$
\mathrm{PPL}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\log p(t_i\mid t_{<i})\right)
$$

[Return to the full excavation](excavations/046-perplexity/README.md)

---

## Excavation 049 — Calibration — Does 80% Confidence Mean Eight Out of Ten?

Five predictions report 0.8 confidence. Exactly four are correct. Accuracy is 4/5=0.8, so this group is calibrated. If only two are correct, accuracy is 0.4 and the confidence gap is 0.4.

### Only now do the symbols earn names

Each group contains predictions with similar confidence. Accuracy counts how many were correct. The absolute difference measures the reliability gap; weighting by group size prevents tiny groups dominating.

### Why these operations are forced

- [Confidence minus accuracy](MATHEMATICAL_MOVES.md#subtraction) finds each bin's reliability gap; adding them would measure overall level rather than disagreement.
- [Absolute value](MATHEMATICAL_MOVES.md#absolute-value) makes overconfidence and underconfidence both count as error when this metric asks for magnitude rather than direction.
- [Multiplying by |Bᵦ|/n](MATHEMATICAL_MOVES.md#multiplication) gives a large bin proportionally more influence, and [the sum](MATHEMATICAL_MOVES.md#summation) combines all bin contributions. An unweighted mean would let a tiny bin count as much as a common one.

Only now can we compress the exact procedure:

$$
\mathrm{ECE}=\sum_b\frac{|B_b|}{n}\left|\mathrm{accuracy}(B_b)-\mathrm{confidence}(B_b)\right|
$$

[Return to the full excavation](excavations/049-calibration/README.md)

---

## Excavation 051 — Scaling Laws — What Improves When We Add More?

Models with 1, 2, and 4 million effective units achieve losses 4.0, 3.2, and 2.8. Improvement continues but shrinks. The curve helps estimate whether doubling again is worth the cost; it does not promise a new capability.

### Only now do the symbols earn names

N is the resource being scaled. The negative exponent makes loss fall as N grows. Alpha controls how quickly returns diminish. A scales the improvable part; B is the floor this simple trend cannot beat.

### Why these operations are forced

- [The negative power](MATHEMATICAL_MOVES.md#powers) makes the improvable part fall as resource N grows, with α controlling how quickly returns diminish.
- [A scales that falling term](MATHEMATICAL_MOVES.md#multiplication) to the observed problem; adding A would create a floor instead of changing improvement size.
- [Adding B](MATHEMATICAL_MOVES.md#addition) represents a remaining floor this simple scaling route does not remove. Multiplying by B would force the whole loss toward zero instead of allowing an irreducible remainder.

Only now can we compress the exact procedure:

$$
L(N)=A N^{-\alpha}+B
$$

[Return to the full excavation](excavations/051-scaling-laws/README.md)

---

## Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

For “How do I reset my router?”, answer A gives three safe ordered steps; answer B gives twenty vague paragraphs. A reviewer chooses A. Repeated comparisons teach concision and usefulness without declaring one exact sentence mandatory.

### Only now do the symbols earn names

The reward scores two responses to the same prompt. Their difference matters, not the absolute score. The logistic function turns that difference into a preference probability; larger positive differences favor the chosen answer.

### Why these operations are forced

- [rA−rB](MATHEMATICAL_MOVES.md#subtraction) discards any common reward offset and keeps only which answer reviewers prefer and by how much.
- [The inner negative](MATHEMATICAL_MOVES.md#negative-sign) makes larger preference gaps reduce the exponential term, so A's probability rises rather than falls.
- [Exponentiation](MATHEMATICAL_MOVES.md#exponential) turns an unbounded reward gap into positive odds; adding one and [taking the reciprocal](MATHEMATICAL_MOVES.md#division) squeeze the result between zero and one without changing order.

Only now can we compress the exact procedure:

$$
P(A\succ B)=\frac{1}{1+\exp(-(r_A-r_B))}
$$

[Return to the full excavation](excavations/053-preference-learning/README.md)

---

## Excavation 077 — Convolution — Reusing the Same Local Detector

A ranger photographs a tiger behind tall grass. Along one row, neighboring brightness values change from dark grass to bright stripe and back to dark fur. She builds one three-slot stripe detector and slides that same detector across the row. At every location she multiplies each observed brightness by the matching detector slot and adds the agreements. A large total says the local patch resembles the stripe pattern. Reusing the detector matters because a stripe should remain a stripe whether it appears on the left or right of the photograph.

- The signal values are neighboring brightness measurements.
- The kernel values are the same small detector reused at every location.
- Multiplication measures how each local measurement agrees with its detector weight.
- Summation combines the local evidence; shifting i moves the same detector instead of learning a new one.

### Why these operations are forced

- [Each multiplication](MATHEMATICAL_MOVES.md#multiplication) asks how strongly one local pixel agrees with the corresponding filter weight. A zero weight ignores that location; a negative one looks for contrast.
- [The sum](MATHEMATICAL_MOVES.md#summation) combines those aligned local contributions into one detector response. Multiplying all responses would let one zero pixel erase the entire pattern.
- [i+j](MATHEMATICAL_MOVES.md#indices) slides the same relative filter position j to a new image location i, which is how one detector is reused rather than relearned everywhere.

Only now can we compress the procedure:

$$
y_i=\sum_{j=0}^{k-1}x_{i+j}w_j
$$

[Return to the full excavation](excavations/077-convolution/README.md)

---

## Excavation 084 — Diffusion — Learning by Destroying

Print a clean tiger photograph on transparent film. At the first step, keep almost all of the photograph and mix in a faint sheet of random grain. At later steps, keep less tiger and add more grain until the animal is nearly lost. The two mixing amounts must be coordinated: increasing noise while keeping all the original image would make total intensity grow without bound. The square-root factors preserve a controlled overall scale while transferring influence from image to noise.

- The clean image is the named tiger image x0.
- Noise ε is the random corruption added during the forward process.
- The retained clean fraction and noise fraction change with step t.
- Square roots scale amplitudes so their variances combine as intended.

### Why these operations are forced

- [The two multiplications](MATHEMATICAL_MOVES.md#multiplication) scale how much clean image and fresh noise survive at time t.
- [Addition](MATHEMATICAL_MOVES.md#addition) overlays those two same-shaped image contributions. Concatenation would produce two images side by side rather than one corrupted image.
- [Square roots of the variance shares](MATHEMATICAL_MOVES.md#square-root) convert variance allocation into amplitude scaling; the two squared amplitudes then sum to one total variance.

Only now can we compress the procedure:

$$
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
$$

[Return to the full excavation](excavations/084-diffusion/README.md)

---

## Excavation 085 — Denoising — Predicting What the Noise Hid

Take one pixel from that corrupted tiger image. We know the random grain added to it was `+0.30`. The denoiser sees the corrupted image and the current noise step and predicts `+0.20`. Its error is `0.10`; squaring makes the contribution `0.01` and prevents a `-0.10` error elsewhere from cancelling it. Repeating this comparison across pixels and images teaches the network which part of a noisy observation should be removed.

- xt is the noisy image already constructed in the example.
- t tells the network how much corruption it faces.
- The network predicts the exact noise ε that hid the clean image.
- Squaring the pixel-by-pixel prediction error prevents cancellation; averaging trains across samples.

### Why these operations are forced

- [Subtracting predicted noise from actual noise](MATHEMATICAL_MOVES.md#subtraction) isolates the denoiser's error rather than their combined amount.
- [The squared norm](MATHEMATICAL_MOVES.md#norm) lets every pixel error contribute without opposite signs cancelling and penalizes large misses more strongly.
- [Expectation](MATHEMATICAL_MOVES.md#expectation) averages that error over images, noise samples, and times according to how training encounters them.

Only now can we compress the procedure:

$$
L=\mathbb{E}\left[\lVert\epsilon-\epsilon_\theta(x_t,t)\rVert^2\right]
$$

[Return to the full excavation](excavations/085-denoising/README.md)

---

## Excavation 089 — Q-Learning — Improving Values from Experience

A rescue robot reaches a fork. Moving left finds one injured hiker now, worth immediate reward 1, and leads to a state whose best known continuation is worth 5. If future reward is discounted by 0.9, the experience proposes `1 + 0.9×5 = 5.5` as the new target value for choosing left. The robot is not claiming certainty; it is joining what happened now with its best current estimate of what can follow.

- The immediate reward is what happened now.
- The largest next-state Q value represents the best continuation currently known.
- Discount γ reduces distant evidence and keeps unending sums bounded.
- Adding immediate and discounted future reward creates the target the old estimate moves toward.

### Why these operations are forced

- [Addition](MATHEMATICAL_MOVES.md#addition) combines reward received now with estimated value still available afterward because both contribute to total future return.
- [γ scales future value](MATHEMATICAL_MOVES.md#multiplication) to express delay or uncertainty; adding γ would give the same arbitrary bonus regardless of what future was reached.
- [Max](MATHEMATICAL_MOVES.md#maximum) uses the value of the best next action because Q-learning asks what return remains under optimal continuation. Averaging would evaluate a different future policy.

Only now can we compress the procedure:

$$
\text{target}=r+\gamma\max_{a^\prime}Q(s^\prime,a^\prime)
$$

[Return to the full excavation](excavations/089-q-learning/README.md)

---

## Excavation 090 — Policy Gradients — Improving the Choices Directly

A rescue robot sometimes chooses the river path and sometimes the ridge path. On one trip it samples the ridge with probability 0.30 and eventually reaches the hiker safely, earning a strong return. The learning signal should make that sampled choice somewhat more likely. On a failed trip, the return reverses the pressure. The policy gradient is the bookkeeping rule that connects how the trip ended to how the probability of the chosen action should change.

- The sampled action probability comes from policy πθ.
- Its log converts repeated action probabilities into additive learning signals.
- Return G says how the chosen action eventually turned out.
- The gradient changes θ in the direction that makes above-average rewarded actions more likely.

### Why these operations are forced

- [The policy log](MATHEMATICAL_MOVES.md#logarithm) turns a product of action probabilities along a trajectory into additive terms and yields a convenient relative sensitivity: how a small parameter change alters chosen-action probability.
- [Multiplying by return G](MATHEMATICAL_MOVES.md#multiplication) makes successful sampled actions more influential and harmful ones push the opposite way; adding G would shift advice without scaling responsibility.
- [Expectation](MATHEMATICAL_MOVES.md#expectation) averages this noisy sampled advice across trajectories according to how often the policy produces them.

Only now can we compress the procedure:

$$
\nabla_\theta J=\mathbb{E}\left[G\nabla_\theta\log\pi_\theta(a\mid s)\right]
$$

[Return to the full excavation](excavations/090-policy-gradients/README.md)

---

## Excavation 092 — Contrastive Learning

Place four wildlife photographs beside four captions. The tiger photograph should prefer “a striped predator” over “a river,” “a truck,” and “a sleeping dog.” Pulling only the correct pair together is insufficient: every photograph and caption could collapse to the same location. Making the tiger compete against all candidate captions forces its correct caption to be closer *relative to the alternatives*.

- zi and ti are the matched image and text vectors.
- Their dot product is the named alignment score.
- Temperature T controls how sharply alternatives compete.
- The denominator includes every candidate caption, preventing all examples from collapsing to one point.
- The negative log penalizes the true pair when mismatches receive comparable scores.

### Why these operations are forced

- [Each dot product](MATHEMATICAL_MOVES.md#dot-product) measures aligned agreement between one image representation and one candidate text representation.
- [Dividing by temperature](MATHEMATICAL_MOVES.md#division) controls how strongly score gaps matter before [exponentiation](MATHEMATICAL_MOVES.md#exponential) converts them into positive relative weights.
- [The denominator sum](MATHEMATICAL_MOVES.md#summation) makes the correct pair compete against all candidates, preventing every representation from winning by collapsing to one point.
- [Negative log](MATHEMATICAL_MOVES.md#logarithm) turns the correct pair's probability share into additive cost and punishes confident preference for the wrong match.

Only now can we compress the procedure:

$$
L_i=-\log\frac{\exp(z_i\cdot t_i/T)}{\sum_j\exp(z_i\cdot t_j/T)}
$$

[Return to the full excavation](excavations/092-contrastive-learning/README.md)

---

## Excavation 094 — Low-Rank Adaptation

A large language model already knows general English, but a park service needs it to understand a small set of ranger report conventions. Copying and changing its entire transformation matrix would be expensive. Instead, freeze the original map and learn two narrow maps: one compresses a report into a few adaptation directions, and the other expands those directions back into a correction with the original shape. Adding that correction preserves the base map while bending it toward ranger language.

- W is the frozen large matrix we refuse to duplicate.
- A and B are the two narrow trainable matrices.
- Their product BA creates a full-shaped correction while using far fewer values.
- Addition preserves the base behavior and applies only the learned adaptation.

### Why these operations are forced

- [BA](MATHEMATICAL_MOVES.md#multiplication) composes two narrow learned transformations, forcing the correction through a low-dimensional bottleneck instead of learning every entry of a full matrix.
- [Adding that correction to W](MATHEMATICAL_MOVES.md#addition) preserves the pretrained base and treats adaptation as a change. [The prime on W](MATHEMATICAL_MOVES.md#symbol-decorations) marks the adapted version; replacing W would discard the knowledge we intended to keep.

Only now can we compress the procedure:

$$
W^\prime=W+BA
$$

[Return to the full excavation](excavations/094-lora/README.md)

---

## Excavation 095 — Quantization

Suppose one learned weight is `0.73`, but the device can store only integer steps of size `0.10`. Dividing by the step size says the weight is 7.3 steps; rounding stores integer 7. During computation, multiplying 7 by `0.10` reconstructs `0.70`. The device has traded an error of `0.03` for cheaper storage and arithmetic. The scale decides which real differences survive.

- Real weight w is divided by scale s to express it in integer-sized steps.
- Rounding chooses the nearest allowed integer q.
- Multiplying q by s reconstructs the approximate weight used in computation.
- The scale is calibrated so important values fit the available integer range.

### Why these operations are forced

- [Dividing by scale s](MATHEMATICAL_MOVES.md#division) expresses a real weight in units of one quantization step.
- [Rounding](MATHEMATICAL_MOVES.md#rounding) chooses the nearest integer level because storage permits only discrete codes; this is the deliberate lossy step.
- [Multiplying q by s](MATHEMATICAL_MOVES.md#multiplication) converts the stored step count back to the weight's approximate real scale. [The hat on w](MATHEMATICAL_MOVES.md#symbol-decorations) marks this reconstructed approximation; addition would shift levels rather than restore their unit size.

Only now can we compress the procedure:

$$
q=\mathrm{round}(w/s)
$$

$$
\widehat w=sq
$$

[Return to the full excavation](excavations/095-quantization/README.md)

---

## Excavation 102 — Bayesian Updating

Before seeing tracks, a ranger considers tiger less common than deer: perhaps tiger receives prior share 1 and deer share 4. A deep round print is far more expected under tiger—say likelihood 8—than deer—say likelihood 1. Multiplying gives supports 8 for tiger and 4 for deer. Dividing each by total support 12 turns them into revised shares: two thirds tiger, one third deer. The print overcame the prior, but did not erase it.

- Tiger’s prior belief is its share before the footprint.
- The footprint likelihood says how expected this exact clue is if tiger is true.
- Multiplying gives tiger’s unnormalized support.
- The denominator repeats that multiplication for every story and adds them so final beliefs total one.

### Why these operations are forced

- [Likelihood times prior](MATHEMATICAL_MOVES.md#multiplication) requires a story to have both earlier plausibility and support from the new footprint. Addition would let overwhelming prior belief compensate linearly for evidence impossible under that story.
- [The denominator sums support](MATHEMATICAL_MOVES.md#summation) over every competing story to find the whole amount of belief available.
- [Division by that total](MATHEMATICAL_MOVES.md#division) turns each story's support into a share summing to one, while [the conditional bars](MATHEMATICAL_MOVES.md#conditional-bar) keep “evidence given story” distinct from “story after evidence.”

Only now can we compress the procedure:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{\sum_j P(E\mid H_j)P(H_j)}
$$

[Return to the full excavation](excavations/102-bayesian-updating/README.md)

---

## Excavation 115 — Tree Search

A cave explorer can investigate the river tunnel or the ridge tunnel. The river tunnel has produced good finds in eight visits; the ridge has been tried only once. Choosing only the better average may ignore an undiscovered ridge chamber, while choosing only the least visited branch wastes known evidence. The search score adds an uncertainty bonus that is large for neglected branches and shrinks as visits supply evidence.

- The average reward records how well one branch has performed.
- Visit count shrinks the exploration bonus as evidence accumulates.
- Total visits increase pressure to reconsider neglected branches.
- The constant controls how much uncertainty competes with known reward.

### Why these operations are forced

- [The bar over R](MATHEMATICAL_MOVES.md#symbol-decorations) marks the mean return, keeping what a branch has already demonstrated; see [mean](MATHEMATICAL_MOVES.md#mean).
- [log N](MATHEMATICAL_MOVES.md#logarithm) lets exploration pressure grow slowly as the parent receives more visits instead of growing in direct proportion forever.
- [Dividing by nₐ](MATHEMATICAL_MOVES.md#division) makes an often-tested action less uncertain; [the square root](MATHEMATICAL_MOVES.md#square-root) tempers how sharply that exploration bonus changes.
- [c scales curiosity](MATHEMATICAL_MOVES.md#multiplication) and [addition](MATHEMATICAL_MOVES.md#addition) places that exploration bonus beside observed reward. Multiplying reward and curiosity would make either zero erase the other.

Only now can we compress the procedure:

$$
\mathrm{score}(a)=\overline R_a+c\sqrt{\frac{\log N}{n_a}}
$$

[Return to the full excavation](excavations/115-tree-search/README.md)

---

## Excavation 119 — Graph Neural Networks

Three villages share borders. The river village wants to update its flood-risk estimate using reports from its upstream neighbors. Each neighbor converts its own rainfall and elevation into the same kind of message; the river village adds those messages, then combines them with its existing local estimate. Addition works whether it has two neighbors or five and does not pretend that the order in which reports arrive changes geography.

- Node v keeps its current representation.
- Every neighbor u sends a message computed by the same rule.
- Summation combines a variable number of messages without depending on neighbor order.
- The update rule joins the old node state with the aggregated neighborhood evidence.

### Why these operations are forced

- [M(hᵥ,hᵤ)](MATHEMATICAL_MOVES.md#function-application) creates a message that depends on both receiving and neighboring nodes.
- [Summing over neighbors](MATHEMATICAL_MOVES.md#summation) combines a variable-size, unordered neighborhood into one fixed-size message. Concatenation would depend on neighbor count and arbitrary listing order.
- [U](MATHEMATICAL_MOVES.md#function-application) then updates the old node state using both its own previous information and the neighborhood evidence.

Only now can we compress the procedure:

$$
h_v^\prime=U\left(h_v,\sum_{u\in N(v)}M(h_v,h_u)\right)
$$

[Return to the full excavation](excavations/119-graph-neural-networks/README.md)

---

## Excavation 122 — Differential Privacy

A clinic wants to publish an average recovery time. Imagine two almost identical worlds: one dataset includes Maya's record and the other does not. If the published number changes dramatically, an observer can infer Maya's participation. The privacy mechanism limits how much the probability of any released result may differ between those worlds. Clipping limits one person's influence; calibrated randomness makes the two possible output distributions overlap.

- D and D-prime are two datasets differing in one person.
- The same possible released result S is considered under both.
- Epsilon limits how much more likely that result may become because one person participated.
- A smaller epsilon makes the two worlds harder to distinguish.

### Why these operations are forced

- [The two probabilities](MATHEMATICAL_MOVES.md#probability) ask how likely the same released event S is with or without one person's record.
- [M(D) ∈ S](MATHEMATICAL_MOVES.md#membership) says the randomized mechanism's output landed in the set of outcomes being inspected.
- [e^ε](MATHEMATICAL_MOVES.md#exponential) turns the privacy budget into a multiplicative allowance: ε=0 requires equal probabilities, while larger ε permits a bounded ratio.
- [The ≤ sign](MATHEMATICAL_MOVES.md#inequalities) promises a ceiling rather than false equality; privacy needs the two distributions close, not identical for every dataset pair.

Only now can we compress the procedure:

$$
P(M(D)\in S)\le e^\epsilon P(M(D^\prime)\in S)
$$

[Return to the full excavation](excavations/122-differential-privacy/README.md)
