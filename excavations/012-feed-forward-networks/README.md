# Excavation 012 — Feed-Forward Networks

## The Problem: Communication Is Not Thought

Attention answers, “Which other tokens should this token consult?” After gathering information, every token still needs to process what it received.

Imagine a token has collected evidence for *not*, *very*, and *hot*. Routing brings those signals together. The model must now build a useful transformation—perhaps a feature closer to “mild.” A weighted average alone is limited.

## Failed Attempt: Add Another Matrix

Apply matrix $A$, then matrix $B$:

$$B(A\mathbf{x})=(BA)\mathbf{x}$$

No matter how many purely linear layers we stack, they collapse into one matrix. They can rotate, scale, and mix dimensions, but cannot create a bend, threshold, or conditional response.

## The Invention: Linear, Nonlinear, Linear

A transformer feed-forward network applies the same small neural network independently to every token:

$$
\operatorname{FFN}(\mathbf{x})=W_2\,\sigma(W_1\mathbf{x}+\mathbf{b}_1)+\mathbf{b}_2
$$

$W_1$ usually expands the width, the activation $\sigma$ introduces nonlinearity, and $W_2$ projects back to model width.

## Worked ReLU Example

Let an intermediate result be `[-2, 0.5, 3]`. ReLU computes:

$$\operatorname{ReLU}(z)=\max(0,z)$$

so the result is `[0, 0.5, 3]`. This simple gate makes the transformation input-dependent. Different inputs activate different intermediate features; the two surrounding matrices can no longer collapse into one fixed matrix.

## Why Expand the Hidden Width?

The wider internal space gives the layer room to detect many candidate patterns. The projection back compresses those activated patterns into the shared model representation. It resembles asking many learned questions, gating their responses, then recombining them.

## Position-Wise Means Shared, Not Connected

The FFN is applied separately to every token with the same parameters. It does not mix token positions; attention already performed communication. This creates a clean rhythm:

1. Attention: exchange information across tokens.
2. FFN: transform information within each token.

## Code Walkthrough

`implementation.py` implements affine transformations, ReLU, and a two-layer FFN. Run it, inspect the hidden pre-activations, and note which coordinates ReLU turns off. Change the input slightly and watch the active pattern change.

## Common Misconceptions

**“Feed-forward means information moves through the sentence.”** Here it moves through layers inside one token position.

**“ReLU merely deletes negative numbers.”** Its importance is that it makes the overall mapping nonlinear and input-dependent.

**“Attention does all transformer computation.”** FFNs contain a large fraction of parameters and perform much of the feature transformation.

## The New Problem

We can now stack attention and FFNs. But deep stacks can damage information and make optimization fragile. We need a path that lets each block refine a representation without replacing it completely.

---

Previous: [011 — Multi-Head Attention](../011-multi-head-attention/README.md) · Next: [013 — Residual Connections](../013-residual-connections/README.md)
