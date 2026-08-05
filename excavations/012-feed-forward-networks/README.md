# Excavation 012 — Feed-Forward Networks

[Previous: Multi-Head Attention](../011-multi-head-attention/README.md)

Attention lets tokens communicate. Communication is not the same as thinking.

Imagine several experts place evidence on your desk. You still need to interpret it, combine patterns, and form a new conclusion. In a Transformer, each token needs a private processing step after it gathers information.

## Failed attempt: stack transformation matrices

Apply one matrix, then another, then another. This looks deep, but if every step is purely linear, the whole chain can be replaced by one matrix. More layers have added notation without adding a new kind of behavior.

The missing ability is to respond differently depending on which patterns are present—to open some paths and close others.

## A small internal workshop

For each token independently:

1. expand its representation into a wider workspace;
2. allow only some intermediate signals through;
3. recombine the surviving signals back into the shared width.

```text
token → many candidate features → gate → recombined token
```

A simple gate such as ReLU turns negative signals off and leaves positive ones available. Because different inputs activate different intermediate features, the surrounding matrices no longer collapse into one fixed transformation.

Only now does the familiar expression describe an understood machine:

## Build Every Piece from the Concrete Example

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
\operatorname{FFN}(\mathbf{x})
=W_2\,\sigma(W_1\mathbf{x}+\mathbf{b}_1)+\mathbf{b}_2
$$


## Challenge

Explain why two linear transformations in succession can still act like one linear transformation, and identify what the gate changes.

## What the next excavation needs

If every workshop completely replaces its input, useful information can be damaged as it passes through many layers. We need a safer way to build depth.

[Next: Residual Connections](../013-residual-connections/README.md)
