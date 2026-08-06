# Excavation 119 — Graph Neural Networks

[Previous: Excavation 118](../118-knowledge-graphs/README.md)

## Take the First Step Yourself

> **Your problem:** How can each node learn from a variable number of neighbors?

> **Try your first idea:** Assign a fixed input slot to every possible neighbor.

> **Now try to break your idea:** Graphs vary in size and neighbor order should not change meaning.

> Stop here. State the missing requirement without naming the repair.

## The Observation

How can each node learn from a variable number of neighbors?

## Your First Attempt

Assign a fixed input slot to every possible neighbor.

## Break Your First Attempt

Graphs vary in size and neighbor order should not change meaning.

## Repair Your Attempt

Apply the same message rule to each edge and aggregate neighbor messages without depending on order.

## What You Have Just Invented

**Apply the same message rule to each edge and aggregate neighbor messages without depending on order.**

## Rebuild the Discovery with a Concrete Case

A molecule atom receives messages from bonded atoms, sums them, then updates its representation.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Build Every Piece from the Concrete Example

- Node v keeps its current representation.
- Every neighbor u sends a message computed by the same rule.
- Summation combines a variable number of messages without depending on neighbor order.
- The update rule joins the old node state with the aggregated neighborhood evidence.

Only now can we compress the procedure:

$$
h_v^\prime=U\left(h_v,\sum_{u\in N(v)}M(h_v,h_u)\right)
$$

## Real-World Limit

Repeated aggregation can blur distinct nodes.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 120](../120-program-synthesis/README.md)
