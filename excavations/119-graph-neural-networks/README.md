# Excavation 119 — Graph Neural Networks

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Graphs & Relational Structures](../../MATHEMATICS_ATLAS.md#graphs) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Continual learning, reasoning, and research

A knowledge graph preserves who relates to whom. To make predictions, each entity must learn from a variable number of neighbors without depending on the arbitrary order in which those neighbors are listed.

Inside the Hall of Possible Worlds, the old method is given an honest chance. The keeper of unfinished questions places the evidence on the table of mirrored maps and tries to assign a fixed input slot to every possible neighbor.

Nothing about this first move is careless. To assign a fixed input slot to every possible neighbor is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: graphs vary in size and neighbor order should not change meaning.

The important discovery is not merely that trying to assign a fixed input slot to every possible neighbor failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the table of mirrored maps, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to apply the same message rule to each edge and aggregate neighbor messages without depending on order. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Graph Neural Networks**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

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

The calculation reuses familiar motions: **the chorus**—many witnesses contribute to one answer without one silence erasing the rest. Together they keep the path from the concrete case to notation intact.

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
