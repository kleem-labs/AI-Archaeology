# Excavation 015 — Learning

## The Problem: Architecture Without Knowledge

Embeddings, attention heads, FFNs, residual paths, and normalization describe how information can flow. With random parameter values, the system still produces nonsense. We need a repeatable process that turns mistakes into parameter changes.

## Step 1: Define a Task

For language modeling, hide the future and ask the model to predict the next token:

> “The cat drank the ___”

The training example says the observed next token is *milk*. The model produces scores for every vocabulary item, then softmax probabilities.

## Step 2: Measure Error

If the model assigns the correct token probability $p$, cross-entropy loss is:

$$L=-\log p$$

Predicting *milk* with probability 0.8 yields about 0.223 loss. Probability 0.01 yields about 4.605. Confident mistakes are punished strongly.

## Failed Attempt: Randomly Wiggle Parameters

Change a weight, run the entire dataset, and keep the change if loss improves. This can work for a handful of parameters but becomes hopeless in billions of dimensions. We need to know which direction changes loss most efficiently.

## The Invention: Gradients

For each parameter $\theta$, the derivative

$$
\frac{\partial L}{\partial\theta}
$$

measures how a tiny increase in that parameter changes loss. Collect all derivatives into the gradient $\nabla L$. Move a small step in the opposite direction:

$$
\theta\leftarrow\theta-\eta\nabla L
$$

where $\eta$ is the learning rate.

## Worked One-Parameter Example

Suppose $L(w)=(w-3)^2$. Then:

$$\frac{dL}{dw}=2(w-3)$$

At $w=0$, the gradient is `-6`. With learning rate 0.1:

$$w\leftarrow0-0.1(-6)=0.6$$

Loss falls from 9 to 5.76. Repeated steps approach 3.

## Backpropagation: Reusing the Chain Rule

The loss depends on probabilities, which depend on logits, which depend on layer outputs, which depend on many earlier parameters. Backpropagation applies the chain rule from the loss backward through this computation graph, reusing intermediate derivatives efficiently.

It does not “send the correct answer backward.” It computes responsibility: how sensitive the loss was to each intermediate value and parameter.

## Batches and Generalization

Updating from one sentence may improve that example while harming others. A mini-batch averages evidence across several examples. Across many batches, useful patterns recur while accidents compete and often cancel.

Low training loss alone is not the goal. A model must perform well on examples it did not train on. That is generalization.

## Code Walkthrough

`implementation.py` learns the minimum of $(w-3)^2$ with gradient descent. It prints parameter, loss, and gradient at each step. Change the learning rate to `1.1`: updates overshoot and diverge. Change it to `0.001`: learning becomes safe but slow.

## Common Misconceptions

**“The gradient tells us the best final parameter.”** It gives local slope, not a complete map of the landscape.

**“Training stores every example verbatim.”** Models can memorize, but gradient training also discovers reusable statistical patterns.

**“Lower training loss always means a better model.”** Overfitting can improve training loss while hurting unseen data.

**“Learning means human-like comprehension.”** Optimization improves an objective. What capabilities emerge must be tested, not assumed.

## The New Problem

Local updates optimize next-token prediction, yet sufficiently large models develop abilities not explicitly programmed: translation, analogy, coding, planning, and more. How can simple training produce qualitatively surprising behavior? Our next excavation studies emergence.

---

Previous: [014 — Layer Normalization](../014-layer-normalization/README.md) · Next: Excavation 016 — Emergence *(coming next)*
