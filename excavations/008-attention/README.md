# Excavation 008 — Attention

## The Problem

Consider:

> The animal did not cross the street because **it** was tired.

To interpret *it*, the model should use *animal* more than *street*. A fixed word embedding cannot do this alone. Each token needs a context-dependent representation.

## First Attempt: Compress Everything

Earlier sequence models repeatedly compressed the past into one state. Information from distant tokens could fade, and one fixed summary had to serve every later question.

## The Invention

Let a token inspect all relevant tokens and take a weighted mixture of their information:

$$
\text{output}_i = \sum_j \alpha_{ij}\mathbf{v}_j
$$

The weight $\alpha_{ij}$ says how much token $i$ uses token $j$. This is **attention**.

## Three Operations

For each token:

1. Score how relevant every other token is.
2. Convert scores into nonnegative weights that sum to one.
3. Take the weighted sum of their vectors.

The result is contextual: the same word can produce different outputs in different sentences.

## Attention Is Information Routing

Attention does not declare a single human-readable explanation. It creates a differentiable route through which information can flow. Multiple layers and heads may distribute a behavior across many routes.

## The New Problem

Raw relevance scores can be negative, unbounded, and on incompatible scales. We need a principled way to turn them into normalized weights. That function is softmax.

---

Previous: [007 — Embeddings](../007-embeddings/README.md) · Next: [009 — Softmax](../009-softmax/README.md)
