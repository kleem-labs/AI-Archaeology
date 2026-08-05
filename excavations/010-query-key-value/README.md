# Excavation 010 — Query, Key, Value

## The Problem

Using one vector both to decide relevance and to supply content forces it to do incompatible jobs. A token may be useful to match by one property but contribute different information once selected.

## The Invention

Create three learned projections of each token:

- **Query:** What am I looking for?
- **Key:** What kind of match do I offer?
- **Value:** What information will I contribute if selected?

These names are an analogy to retrieval systems, not fixed semantic labels.

## Scoring a Match

A query and key receive a high dot product when they point in similar directions:

$$
s_{ij}=\mathbf{q}_i\cdot\mathbf{k}_j
$$

In large dimensions, dot products tend to grow. Divide by $\sqrt{d_k}$ to keep softmax from becoming excessively sharp:

$$
S=\frac{QK^T}{\sqrt{d_k}}
$$

Apply softmax to each row and mix the values:

$$
\operatorname{Attention}(Q,K,V)=
\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

## The Complete Journey

For every receiving token:

1. Its query scores every token's key.
2. Softmax converts scores to attention weights.
3. Those weights blend the value vectors.
4. The blend becomes a context-dependent output.

The projection matrices that create $Q$, $K$, and $V$ are learned during training. The network discovers useful notions of seeking, matching, and contributing.

## Masking

During next-token prediction, a position must not inspect future tokens. A causal mask replaces forbidden scores with negative infinity before softmax, giving those positions zero weight.

## The New Problem

One attention pattern may track syntax while another follows reference or position. A single set of projections is a bottleneck. Next we will run several attention mechanisms in parallel: multi-head attention.

---

Previous: [009 — Softmax](../009-softmax/README.md) · Next: Excavation 011 — Multi-Head Attention *(coming next)*
