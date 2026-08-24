# Excavation 119 — Graph Neural Networks

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Graphs & Relational Structures](../../MATHEMATICS_ATLAS.md#graphs) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

A knowledge graph preserves who relates to whom. To make predictions, each entity must learn from a variable number of neighbors without depending on the arbitrary order in which those neighbors are listed.

Nothing in the Hall of Possible Worlds yet bears today's mathematical name. There is only the keeper of unfinished questions, the table of mirrored maps, and one plausible action: assign a fixed input slot to every possible neighbor.

At the edge of the table of mirrored maps, the shortcut produces its consequence: graphs vary in size and neighbor order should not change meaning. That consequence, not a textbook, earns the next move.

*The keeper of unfinished questions sketches the break before changing it:*

```text
OLD PATH:  request ──▶ assign a fixed input slot to every… ──▶ graphs vary in size and neighbor…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ we need to apply the same message… ──▶ accountable result
```

The keeper of unfinished questions covers the new mark and the old contradiction returns: graphs vary in size and neighbor order should not change meaning. The cover is lifted, restoring the ability to apply the same message rule to each edge and aggregate neighbor messages without depending on order, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason graph neural networks exists.

What must change for graph neural networks is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: we need to apply the same message rule to each edge and aggregate neighbor messages without depending on order. That threshold is where **Graph Neural Networks** enters the story.

The marks on the table of mirrored maps form a small constellation: one point for the evidence, one for the shortcut, one for the contradiction, and one for the repair. graph neural networks is not any single point. It is the path connecting them in the only order that makes the last point necessary.

## Understanding graph neural networks

A molecule atom receives messages from bonded atoms, sums them, then updates its representation.

## The calculation hidden inside graph neural networks

The keeper of unfinished questions carries the graph neural networks scene to the table of mirrored maps. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Three villages share borders. The river village wants to update its flood-risk estimate using reports from its upstream neighbors. Each neighbor converts its own rainfall and elevation into the same kind of message; the river village adds those messages, then combines them with its existing local estimate. Addition works whether it has two neighbors or five and does not pretend that the order in which reports arrive changes geography.

Node v keeps its current representation.
Every neighbor u sends a message computed by the same rule.
Summation combines a variable number of messages without depending on neighbor order.
The update rule joins the old node state with the aggregated neighborhood evidence.

### Why the melody needs these exact notes

[M(hᵥ,hᵤ)](../../MATHEMATICAL_MOVES.md#function-application) creates a message that depends on both receiving and neighboring nodes.
[Summing over neighbors](../../MATHEMATICAL_MOVES.md#summation) combines a variable-size, unordered neighborhood into one fixed-size message. Concatenation would depend on neighbor count and arbitrary listing order.
[U](../../MATHEMATICAL_MOVES.md#function-application) then updates the old node state using both its own previous information and the neighborhood evidence.

Before the line is compressed, notice its recurring motions: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. They are the handholds by which the reader can later climb back from notation to meaning.

The table of mirrored maps already contains the complete graph neural networks mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
h_v^\prime=U\left(h_v,\sum_{u\in N(v)}M(h_v,h_u)\right)
$$

## Where graph neural networks runs out

Repeated aggregation can blur distinct nodes.

Here the new path ends honestly. Graph Neural Networks can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the table of mirrored maps

Rebuild the graph neural networks scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 120](../120-program-synthesis/README.md)
