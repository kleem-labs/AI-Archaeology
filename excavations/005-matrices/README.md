# Excavation 005 — Matrices

[Previous: Vectors as Change](../004-vectors-as-change/README.md)

Imagine two arrows starting at the same point. A machine stretches both, but sends them toward different final places depending on their original directions.

Does that matter? You answered simply:

> Yes. They end up in different places.

That answer exposes the need. A transformation cannot be one fixed movement added to everything. It must respond to the input vector.

## First attempt: store a separate answer

We could write a transformed result for every possible vector. But there are infinitely many vectors. A lookup table can memorize examples; it cannot describe a general rule.

## Second attempt: transform each coordinate alone

Suppose output one depends only on input one and output two only on input two. That can stretch or shrink axes, but it cannot let weight influence danger while speed also influences danger. Real representations interact.

We need a compact machine in which every output may receive a chosen contribution from every input.

```text
input features → weighted contributions → output features
```

Take an input `[4, 5]`. One output question might say: take twice the first feature and three times the second. Another might ignore the first and take four times the second.

Each question needs a row of weights:

```text
[2, 3]
[0, 4]
```

Stacking the questions creates a **matrix**. Only after that idea is clear do we calculate:

## Walk It Once with Concrete Values

For input [4,5], let the first output use two copies of 4 and three copies of 5: 8+15=23. Let the second use zero copies of 4 and four copies of 5: 0+20=20. The two recipes become the two matrix rows.

## Why Every Term Must Exist Before the Equation

- The right-hand vector **[4,5]** is the input with two features.
- Each matrix row describes one output; each row needs one weight per input.
- Multiplication measures one input's contribution to one output.
- Addition combines all contributions reaching that output.
- The result **[23,20]** contains one value per matrix row.


Row-by-column multiplication is not a ritual. Each row is one output asking how much every input should contribute.

Only now can we compress that reasoning:

$$
\begin{bmatrix}2&3\\0&4\end{bmatrix}
\begin{bmatrix}4\\5\end{bmatrix}
=
\begin{bmatrix}2(4)+3(5)\\0(4)+4(5)\end{bmatrix}
=
\begin{bmatrix}23\\20\end{bmatrix}
$$


## Why order and shape matter

If the input has three features, every output question needs three weights. A matrix with four rows asks four questions and therefore creates four output features.

```text
4 questions × 3 input features
          ↓
3 input numbers → 4 output numbers
```

Shape is the contract between what the machine expects and what it produces.

## The AI connection

A neural network layer repeatedly does this: receive one representation, mix its features according to learned weights, and produce another representation. The matrix is a transformation machine. Training will eventually decide the weights; for now we only needed a coherent way to express all interactions together.

## Challenge

Design a two-row matrix for an animal vector `[weight, speed]`. Let the first output depend only on weight and the second depend on both. Explain each row in words before multiplying.

## What the next excavation needs

We can transform measurable properties. Language gives us a harder object: a word whose meaning is not available from any physical measuring instrument.

[Next: Meaning](../006-meaning/README.md)
