# Excavation 119 — Graph Neural Networks

[Previous: Excavation 118](../118-knowledge-graphs/README.md)

How can each node learn from a variable number of neighbors?

Our first construction is deliberately modest: Assign a fixed input slot to every possible neighbor.

It works—right up to this boundary: Graphs vary in size and neighbor order should not change meaning.

Crossing that boundary requires one additional idea: Apply the same message rule to each edge and aggregate neighbor messages without depending on order.

## Now work a case you can see

A molecule atom receives messages from bonded atoms, sums them, then updates its representation.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Build each piece from what just happened

- Node v keeps its current representation.
- Every neighbor u sends a message computed by the same rule.
- Summation combines a variable number of messages without depending on neighbor order.
- The update rule joins the old node state with the aggregated neighborhood evidence.

Only now can we compress the procedure:

$$
h_v^\prime=U\left(h_v,\sum_{u\in N(v)}M(h_v,h_u)\right)
$$

## Where your new idea still breaks

Repeated aggregation can blur distinct nodes.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 120](../120-program-synthesis/README.md)
