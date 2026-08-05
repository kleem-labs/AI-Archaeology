# Excavation 010 — Query, Key, Value

## The Final Missing Piece

Attention needs scores and information vectors. Why not compare the token embeddings directly and then average those same embeddings?

Because matching and contributing are different jobs.

In a library, a search request might ask for “introductory books about astronomy.” Catalog fields determine which books match. The content retrieved from a selected book is not merely its catalog entry. Search description and delivered information are related but distinct.

## Failed Attempt: One Vector Does Everything

Suppose a token vector contains grammatical role, topic, position, and many other properties. The dimensions useful for deciding relevance may not be the dimensions we want to send onward.

If one vector must serve both purposes, every improvement to matching may disturb content, and every improvement to content may disturb matching.

## The Invention: Three Learned Views

From each token representation $\mathbf{x}$, create three projections:

$$
\mathbf{q}=W_Q\mathbf{x},\qquad
\mathbf{k}=W_K\mathbf{x},\qquad
\mathbf{v}=W_V\mathbf{x}
$$

- **Query:** What kind of information is this receiving position seeking?
- **Key:** What kind of match does this source position offer?
- **Value:** What information will this source contribute if selected?

These are learned roles, not fixed human-readable labels.

## Step 1: Compare Queries with Keys

For receiving token $i$ and possible source $j$:

$$
s_{ij}=\mathbf{q}_i\cdot\mathbf{k}_j
$$

Worked example:

```text
query = [1, 0]
key A = [0.9, 0.1]
key B = [0.1, 0.9]
```

The scores are 0.9 and 0.1. The query aligns much more strongly with key A.

For all tokens at once, stack queries and keys into matrices:

$$
S=QK^T
$$

Entry $S_{ij}$ contains the score from query $i$ to key $j$.

## Step 2: Why Divide by $\sqrt{d_k}$?

If query and key coordinates have roughly unit variance, adding $d_k$ coordinate products makes dot products grow in typical magnitude as the dimension grows. Large scores push softmax into a nearly one-hot region where gradients can become very small.

Scaling stabilizes them:

$$
S=\frac{QK^T}{\sqrt{d_k}}
$$

The square root is not decorative. It compensates for how the variance of a sum grows with dimension.

## Step 3: Normalize Each Query's Scores

Apply softmax across each row:

$$
A=\operatorname{softmax}(S)
$$

Every row now describes where one receiving token gathers information. Row $i$ sums to one independently of all other rows.

## Step 4: Mix Values

Use those weights to combine the value vectors:

$$
O=AV
$$

Putting the steps together:

$$
\operatorname{Attention}(Q,K,V)=
\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

This single expression is no longer mysterious. It says: match requests to offers, normalize the match strengths, and retrieve a weighted mixture of content.

## Worked Miniature Example

Let one query produce softmax weights `[0.75, 0.25]`, with values:

```text
value A = [1, 0]
value B = [0, 2]
```

The output is:

$$
0.75[1,0]+0.25[0,2]=[0.75,0.5]
$$

Notice that keys have disappeared after determining the weights. Values supply the output content.

## Causal Masking

When predicting the next token, position 3 must not inspect position 4. Otherwise training would leak the answer. Before softmax, forbidden scores are replaced with $-\infty$:

$$e^{-\infty}=0$$

Their attention weights become exactly zero. The mask changes which information routes are allowed, not the learned query/key matching rule itself.

## Code Walkthrough

`implementation.py` implements the complete algorithm without NumPy:

1. `dot` compares one query and key.
2. `softmax` normalizes one row of scores.
3. `weighted_sum` mixes values.
4. `scaled_dot_product_attention` repeats these steps for every query.

Run:

```bash
python3 excavations/010-query-key-value/implementation.py
```

Each printed row shows one token's attention distribution and resulting contextual vector. Change `causal=False` to `causal=True` in the call and print again. Earlier positions will lose access to future values.

## Common Misconceptions

**“Q, K, and V are copies of the same vector.”** They begin from the same token representation but use different learned matrices.

**“Keys contain the returned information.”** Keys support matching; values supply the mixture.

**“Attention always attends to words.”** It operates on representations. Depending on the model, these may correspond to subword tokens, image patches, audio frames, or other elements.

**“The largest attention weight explains the whole output.”** The value vectors and subsequent layers matter just as much as the routing weights.

## The New Problem

One attention mechanism creates one geometry of matching. Language may simultaneously require grammatical, positional, referential, and semantic relationships. Next we let several attention mechanisms work in parallel: multi-head attention.

---

Previous: [009 — Softmax](../009-softmax/README.md) · Next: [011 — Multi-Head Attention](../011-multi-head-attention/README.md)
