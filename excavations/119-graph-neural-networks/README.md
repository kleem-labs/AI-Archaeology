# Excavation 119 — Graph Neural Networks

<!-- book-prose-v2 -->

A knowledge graph preserves who relates to whom. To make predictions, each entity must learn from a variable number of neighbors without depending on the arbitrary order in which those neighbors are listed.

The previous discovery seems almost sufficient: we could assign a fixed input slot to every possible neighbor.

The shortcut appears to retain everything graph neural networks needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

One counterexample is enough to expose the missing job: graphs vary in size and neighbor order should not change meaning.

The counterexample teaches graph neural networks. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: we need to apply the same message rule to each edge and aggregate neighbor messages without depending on order.

Now—and not earlier—we may introduce **Graph Neural Networks**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to assign a fixed input slot to every possible neighbor, and the case answers that graphs vary in size and neighbor order should not change meaning. With the narrow repair—to we need to apply the same message rule to each edge and aggregate neighbor messages without depending on order—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Graph Neural Networks returns to the same counterexample, replaces the attempt to assign a fixed input slot to every possible neighbor with the responsibility to we need to apply the same message rule to each edge and aggregate neighbor messages without depending on order, and must succeed where the shortcut failed.

## Understanding graph neural networks

A molecule atom receives messages from bonded atoms, sums them, then updates its representation.

A formula for graph neural networks is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## The calculation hidden inside graph neural networks

Before Graph Neural Networks receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Three villages share borders. The river village wants to update its flood-risk estimate using reports from its upstream neighbors. Each neighbor converts its own rainfall and elevation into the same kind of message; the river village adds those messages, then combines them with its existing local estimate. Addition works whether it has two neighbors or five and does not pretend that the order in which reports arrive changes geography.

Node v keeps its current representation.
Every neighbor u sends a message computed by the same rule.
Summation combines a variable number of messages without depending on neighbor order.
The update rule joins the old node state with the aggregated neighborhood evidence.

### Why no cheaper operation does the same job

[M(hᵥ,hᵤ)](../../MATHEMATICAL_MOVES.md#function-application) creates a message that depends on both receiving and neighboring nodes.
[Summing over neighbors](../../MATHEMATICAL_MOVES.md#summation) combines a variable-size, unordered neighborhood into one fixed-size message. Concatenation would depend on neighbor count and arbitrary listing order.
[U](../../MATHEMATICAL_MOVES.md#function-application) then updates the old node state using both its own previous information and the neighborhood evidence.

Every symbol in Graph Neural Networks can now be read back into an action already performed. The whole procedure fits in one line:

$$
h_v^\prime=U\left(h_v,\sum_{u\in N(v)}M(h_v,h_u)\right)
$$

## Where graph neural networks runs out

Repeated aggregation can blur distinct nodes.

The boundary can be predicted from the construction itself. Graph Neural Networks performs the repair to we need to apply the same message rule to each edge and aggregate neighbor messages without depending on order; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take graph neural networks to the workbench

Move graph neural networks from imagination to evidence by making the shortcut fail under controlled inputs. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running graph neural networks, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the graph neural networks result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 120](../120-program-synthesis/README.md)
