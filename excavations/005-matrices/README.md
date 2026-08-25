# Excavation 005 — Matrices

One vector can now describe one particular change. The rangers next want a reusable machine: give it any animal report and let the same set of rules produce several new judgments. Adding one fixed change cannot do that, because a heavy slow animal and a light fast animal should not be altered identically.

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

## The calculation hidden inside matrices

A ranger must turn two observations—how heavy an animal looks and how fast it moves—into two decisions: danger and whether pursuit is possible. For danger she counts the weight clue twice and the speed clue three times. For pursuit she ignores weight and counts speed four times. Writing the two recipes as rows lets one reusable machine apply both judgments to every animal report.

### Naming what is already on the table

- The right-hand vector **[4,5]** is shorthand for weight signal 4 and speed signal 5.
- Each matrix row describes one output; each row needs one weight per input.
- Multiplication measures one input's contribution to one output.
- Addition combines all contributions reaching that output.
- The result **[23,20]** contains one value per matrix row.

Row-by-column multiplication is not a ritual. Each row is one output asking how much every input should contribute.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) lets each clue's importance scale that clue. A zero weight silences it; a weight of three makes it count three times.
[Addition](../../MATHEMATICAL_MOVES.md#addition) combines the scaled clues because they are separate contributions to the same judgment. Multiplying them would make any zero clue erase the entire decision and would claim interaction we never asked for.
[Each equals sign](../../MATHEMATICAL_MOVES.md#equals) records that the verbal judgment, its arithmetic recipe, and its final score are three descriptions of the same result.

Trace each operation by touch rather than by name: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. Together they form the smallest mechanism that survives the counterexample.

The dust-map already contains the complete matrices mechanism. Mathematics gives that mechanism a form small enough to carry:

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

<!-- book-prose-v2 -->
<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Foundations and representation

## The first constellation

The valley began with unnamed observations. A feature kept one distinction; a vector kept several; distance turned disagreement into separation; a matrix turned several judgments into one reusable machine. None was a separate school subject. Each was the shape left behind when the earlier tool broke.

```text
observation → feature → vector → distance → transformation
```

The trail called *the first constellation* is what remains when one necessity becomes another.
