# Excavation 119 — Graph Neural Networks

A knowledge graph preserves who relates to whom. To make predictions, each entity must learn from a variable number of neighbors without depending on the arbitrary order in which those neighbors are listed.

An obvious shortcut is to assign a fixed input slot to every possible neighbor.

The world refuses to cooperate: graphs vary in size and neighbor order should not change meaning.

We need to apply the same message rule to each edge and aggregate neighbor messages without depending on order.

## Let the case decide

A molecule atom receives messages from bonded atoms, sums them, then updates its representation.

## The arithmetic we have earned

Three villages share borders. The river village wants to update its flood-risk estimate using reports from its upstream neighbors. Each neighbor converts its own rainfall and elevation into the same kind of message; the river village adds those messages, then combines them with its existing local estimate. Addition works whether it has two neighbors or five and does not pretend that the order in which reports arrive changes geography.

- Node v keeps its current representation.
- Every neighbor u sends a message computed by the same rule.
- Summation combines a variable number of messages without depending on neighbor order.
- The update rule joins the old node state with the aggregated neighborhood evidence.

Only now can we compress the procedure:

$$
h_v^\prime=U\left(h_v,\sum_{u\in N(v)}M(h_v,h_u)\right)
$$

## The boundary of the discovery

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
