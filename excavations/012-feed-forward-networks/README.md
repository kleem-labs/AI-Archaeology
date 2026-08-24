# Excavation 012 — Feed-Forward Networks

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

## The calculation hidden inside feed-forward networks

Attention tells the word *tiger* what the rest of the sentence said. Now imagine several small workshops inside that token: one notices whether an animal is dangerous, another recognizes whether it is acting or being described. A gate closes workshops whose evidence is negative and leaves useful ones open. A second mixing step combines only the surviving discoveries. Without the gate, the two mixing steps collapse into one fixed recipe and no conditional workshop can exist.

### Naming what is already on the table

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

### Why the melody needs these exact notes

[Each matrix multiplication](../../MATHEMATICAL_MOVES.md#multiplication) lets learned weights decide how strongly one incoming feature should affect each hidden or outgoing feature.
[Adding a bias](../../MATHEMATICAL_MOVES.md#addition) lets a detector have a baseline threshold even when all incoming features are zero; multiplication alone must always map zero input to zero output.
[The activation function](../../MATHEMATICAL_MOVES.md#function-application) bends the intermediate result. Without that nonlinearity, the two matrix stages collapse into one linear transformation.

Inside feed-forward networks, familiar operations return with stricter duties: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Every mark needed for feed-forward networks is now visible on the long cedar table. The symbols do not add an idea; they bind the discovered moves into one line:

$$
\mathrm{FFN}(\mathbf{x})
=W_2 \sigma(W_1\mathbf{x}+\mathbf{b}_1)+\mathbf{b}_2
$$

## Challenge

Explain why two linear transformations in succession can still act like one linear transformation, and identify what the gate changes.

## What the next excavation needs

If every workshop completely replaces its input, useful information can be damaged as it passes through many layers. We need a safer way to build depth.

[Next: Residual Connections](../013-residual-connections/README.md)

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->
