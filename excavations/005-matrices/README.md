# Excavation 005 — Matrices

[Previous: Vectors as Change](../004-vectors-as-change/README.md)


## Take the First Step Yourself

> **Your problem:** How can one reusable machine turn any animal report into several new scores?

> **Try your first idea:** Store an answer for every possible report, then forbid different inputs from interacting. Break both ideas.

> **Now try to break your idea:** Find the smallest case where it loses information, invents a false relationship, leaks an answer, or cannot scale. Write the properties a repair must have—but do not name the repair yet.

> Stop here. Write your repair in ordinary language. Do not continue until you can say what information must survive and what operation the failure forces.

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

## Build Every Piece from the Concrete Example

Our animal report has normalized weight signal 4 and speed signal 5.

The first output is a threat score: two copies of weight plus three copies of speed, giving 2×4 + 3×5 = 23.

The second is a chase score: ignore weight and take four copies of speed, giving 0×4 + 4×5 = 20.

~~~text
threat = 2×weight + 3×speed = 2×4 + 3×5 = 23
chase  = 0×weight + 4×speed = 0×4 + 4×5 = 20
~~~

Only after these named recipes do they become two matrix rows.

### Give Short Names Only After We Know the Pieces

- The right-hand vector **[4,5]** is shorthand for weight signal 4 and speed signal 5.
- Each matrix row describes one output; each row needs one weight per input.
- Multiplication measures one input's contribution to one output.
- Addition combines all contributions reaching that output.
- The result **[23,20]** contains one value per matrix row.


Row-by-column multiplication is not a ritual. Each row is one output asking how much every input should contribute.

Only now can we compress that reasoning:

$$
\text{threat score}=2(4)+3(5)=23
$$

$$
\text{chase score}=0(4)+4(5)=20
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
