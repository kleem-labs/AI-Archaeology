# Excavation 007 — Embeddings

## The Problem: A Million Empty Dimensions

Suppose our vocabulary contains 100,000 words. A context-count representation needs roughly 100,000 coordinates per word. Most are zero. Two words can be related even when they never appear in exactly the same local context.

We want a smaller space that captures recurring patterns behind the counts.

## Failed Attempt: Use One-Hot Vectors as Meaning

Give each word one private coordinate:

```text
cat = [1, 0, 0, 0]
dog = [0, 1, 0, 0]
car = [0, 0, 1, 0]
```

This represents identity perfectly. But every pair is equally distant and has dot product zero. Cat is no closer to dog than to car.

One-hot vectors say “different.” They cannot say “different in related ways.”

## The Invention: Dense Embeddings

Assign each word a short learned vector:

$$
\text{word}\longrightarrow\mathbf{e}\in\mathbb{R}^d
$$

For illustration, imagine:

```text
cat = [0.9, 0.8, 0.1]
dog = [0.8, 0.9, 0.1]
car = [0.1, 0.0, 0.9]
```

The coordinates need not literally mean “animalness” or “machineness.” The pattern across coordinates is what matters. Cat and dog point in similar directions; car points elsewhere.

## How Can the Vectors Be Learned?

Begin with random vectors. Repeatedly present a prediction task such as:

> Given “the cat drinks ___,” predict *milk*.

If the model predicts poorly, adjust the participating vectors slightly. Words that help make similar predictions receive similar pressures over millions of examples. Geometry emerges as a side effect of becoming useful at the task.

This is crucial: an embedding is not a hand-written definition. It is a set of parameters optimized through experience.

## Measuring Direction with Cosine Similarity

The dot product grows when vectors align, but it also grows with vector length. Cosine similarity divides out the lengths:

$$
\cos(\theta)=\frac{\mathbf{x}\cdot\mathbf{y}}
{\|\mathbf{x}\|\|\mathbf{y}\|}
$$

For `[1, 0]` and `[1, 1]`:

$$
\frac{1(1)+0(1)}{\sqrt{1^2+0^2}\sqrt{1^2+1^2}}
=\frac{1}{\sqrt2}\approx0.707
$$

Identical directions score 1, perpendicular directions score 0, and opposite directions score -1.

## The Embedding Matrix

Stack every word vector as a row of matrix $E$. Looking up word ID 2 selects row 2. Equivalently, multiply a one-hot vector by $E$:

$$
[0,0,1,0]E=E_2
$$

The one-hot vector identifies a row; the embedding matrix supplies its learned continuous representation.

## Worked Analogy—and Its Limit

Embeddings sometimes support directions such as:

$$
\mathbf{king}-\mathbf{man}+\mathbf{woman}\approx\mathbf{queen}
$$

This suggests that some relationships become approximately linear. It does not mean the model has isolated a perfect “gender coordinate,” nor that every analogy works. Geometry is distributed and shaped by training data.

## Code Walkthrough

`implementation.py` builds `dot`, `cosine`, and `nearest`. Run:

```bash
python3 excavations/007-embeddings/implementation.py
```

Dog should be the nearest listed word to cat. Multiply the cat vector by 10: Euclidean distance changes dramatically, while cosine similarity stays the same because direction is unchanged.

## Common Misconceptions

**“Each dimension has one clean human meaning.”** Meaning is usually distributed across many dimensions.

**“Nearby means synonymous.”** Neighbors may be related by topic, grammar, association, or contrast.

**“Embeddings are universal facts.”** Their geometry depends on corpus, objective, preprocessing, and model.

**“A word has one embedding forever.”** Static lookup provides a starting vector. Contextual models transform it for each occurrence.

## The New Problem

The lookup for *bank* is identical in “river bank” and “bank loan.” We need each token to gather relevant information from its present context. That operation is attention.

---

Previous: [006 — Meaning](../006-meaning/README.md) · Next: [008 — Attention](../008-attention/README.md)
