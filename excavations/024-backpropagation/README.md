# Excavation 024 — Backpropagation — Reusing Blame Instead of Recomputing It

<!-- book-prose-v2 -->

The chain rule follows responsibility through one sequence of machines. A real network is a branching graph with shared intermediate results, so tracing every route independently repeats the same downstream work.

The least expensive next move is to perturb each weight and rerun the model.

The proposal deserves a fair hearing. For backpropagation, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: this needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again.

The failure changes the question behind backpropagation. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream.

Only at this point does the inherited name **Backpropagation** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of backpropagation by mentally removing the repair. We fall back to the proposal to perturb each weight and rerun the model.; then this needs at least one extra forward pass per weight. Or trace paths independently and calculate the same suffix again and again. Restore only the ability to compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to perturb each weight and rerun the model. to requiring the system to compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to backpropagation.

## The calculation hidden inside backpropagation

Do not read the coming Backpropagation line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

One shared dough temperature affects two outcomes: crust and centre. The crust branch sends blame 3 through local sensitivity 2, contributing 6. The centre branch sends blame 4 through sensitivity 5, contributing 20. Because both outcomes depended on the same temperature, the baker must return total blame 26 to that shared decision. Computing either downstream suffix twice would add work without adding evidence.

### Names for pieces we have already used

**x̄** means accumulated sensitivity of final loss to intermediate x.
A node can influence several child results y, so every downstream path must contribute.
**ȳ** is blame already accumulated at child y.
**∂y/∂x** says how strongly x affected that child locally.
Multiplication passes blame through one edge; summation combines all outgoing paths.

### Why no cheaper operation does the same job

[The partial derivative](../../MATHEMATICAL_MOVES.md#partial-derivative) measures one local edge while other inputs are held fixed.
[Multiplying child blame by edge sensitivity](../../MATHEMATICAL_MOVES.md#multiplication) passes downstream responsibility through that edge; either factor being zero should block that path.
[Summing over children](../../MATHEMATICAL_MOVES.md#summation) reunites separate downstream routes that all depended on x. Multiplication would incorrectly make one zero-blame route erase every other route.

The notation is finally shorter than the story that created it:

$$
\bar{x}=\sum_{y\in children(x)}\bar{y}\frac{\partial y}{\partial x}
$$

## Backpropagation beyond this one case

A company traces one final loss through departments. Each department receives accumulated responsibility, then distributes it to the decisions that produced its output.

## Where backpropagation runs out

Backpropagation returns a local sensitivity for each weight: which infinitesimal direction would raise the loss, and how strongly. That information contains no instruction saying whether to take the whole suggested movement, one tenth of it, or one thousandth; choosing that fraction is a separate optimization decision. Nor does a local slope reveal the entire loss landscape. A downward direction from the present point cannot prove that a deeper valley does not exist elsewhere, so backpropagation alone cannot guarantee the best minimum.

The limit follows from the job assigned to backpropagation. Its repair knows how to compute the prediction once, remember intermediate values, then move backward. At each node, reuse the blame already accumulated from everything downstream. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take backpropagation to the workbench

A claim about backpropagation now exists on the page; the laboratory must be able to contradict it. Build the wrong idea first, break it, then use [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running backpropagation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the backpropagation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).
