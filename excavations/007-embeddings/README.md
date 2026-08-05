# Excavation 007 — Embeddings

## The Problem

A context-count vector needs one dimension for every word in the vocabulary. Most entries are zero, and adding a vocabulary word changes the size of every representation.

We need a dense, compact map of meaning.

## The Invention

An **embedding** assigns each item a learned vector:

$$
\text{word} \longrightarrow \mathbf{e} \in \mathbb{R}^d
$$

The dimension $d$ might be hundreds even when the vocabulary contains tens of thousands of words. Individual coordinates need not have names. Meaning lives in relationships between vectors.

## Learning the Map

Start with random vectors. Use them to predict a word from its context, or a context from its word. When a prediction is wrong, adjust the relevant vectors. Across many examples, words useful in similar situations receive similar updates.

## Similarity

Cosine similarity compares the angle between embeddings:

$$
\cos(\theta)=\frac{\mathbf{x}\cdot\mathbf{y}}{\|\mathbf{x}\|\|\mathbf{y}\|}
$$

It emphasizes the pattern across dimensions more than overall magnitude.

## Lookup as Matrix Multiplication

Place every word vector in an embedding matrix. Selecting a word's row is equivalent to multiplying a one-hot vector by that matrix. A discrete symbol has become a point where continuous computation can begin.

## The New Problem

An embedding is initially the same wherever its word appears. But *bank* means different things near *river* and *money*. A representation must use surrounding words dynamically. This requires attention.

---

Previous: [006 — Meaning](../006-meaning/README.md) · Next: [008 — Attention](../008-attention/README.md)
