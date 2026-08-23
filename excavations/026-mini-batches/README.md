# Excavation 026 — Mini-Batches — Learning from More Than One Example

<!-- book-prose-v2 -->

Gradient descent can update the network after one example. One muddy footprint can now steer every weight, and the next unusual footprint can pull the whole machine back again.

Nothing yet appears to demand a new invention. We can use one example per update.

There is a real principle behind this restraint: the complexity of mini-batches must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Its hidden assumption becomes visible as soon as we observe that it is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read.

That distinction is the hinge on which mini-batches turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently.

We have earned the chapter's shorter name: **Mini-Batches**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that mini-batches is necessary rather than decorative. Delete its new responsibility and use the earlier plan to use one example per update.. Immediately, it is fast, but noisy accidents dominate. Use every observation before each update. It is stable, but painfully slow and cannot react until the whole archive is read. Reintroduce the single job to average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can average the evidence from a small group. Each batch is large enough to soften accidents and small enough to update frequently. Because the old plan to use one example per update. is the only displaced piece, the reader can locate exactly where mini-batches changes the outcome.

## The calculation hidden inside mini-batches

Do not read the coming Mini-Batches line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

The repair solves the immediate failure, but batch gradients are still estimates. Batch size changes noise, memory use, and sometimes what kind of solution training finds.

A tiger detector has two adjustable dials: how much to trust stripes and how much to trust movement. A clear morning photograph recommends raising those dials by 2 and 4. A muddy side view recommends 4 and 2. A night photograph recommends 3 and 3. For the stripe dial, the three witnesses propose 2+4+3=9, so their average advice is 3. The movement dial also averages to 3. If we merely added their advice, inviting three witnesses instead of one would triple the step even when their average opinion had not changed.

### Names for pieces we have already used

**B** is the selected mini-batch and **|B|** its number of examples.
**Lᵢ** is loss for example i; **∇_θLᵢ** is that example's proposed parameter direction.
Summing combines the witnesses.
Dividing by batch size prevents merely using more examples from making the step proportionally larger.
**g_B** is the batch's less noisy gradient estimate.

### Why no cheaper operation does the same job

[The sum](../../MATHEMATICAL_MOVES.md#summation) lets every selected example contribute its proposed parameter correction. Multiplying gradients would turn one zero coordinate into a veto and would not represent a council's combined advice.
[Dividing by |B|](../../MATHEMATICAL_MOVES.md#division) asks for advice per example, so merely inviting twice as many witnesses does not double the update.
[i ∈ B](../../MATHEMATICAL_MOVES.md#membership) restricts the sum to examples actually selected for this mini-batch; [|B|](../../MATHEMATICAL_MOVES.md#cardinality) means the number of those examples.

The notation is finally shorter than the story that created it:

$$
g_B=\frac{1}{|B|}\sum_{i\in B}\nabla_\theta L_i
$$

## Mini-Batches beyond this one case

A council does not ask one witness or the entire nation. It hears a manageable panel, makes a decision, then hears another.

## Take mini-batches to the workbench

Understanding mini-batches now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running mini-batches, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the mini-batches result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 027](../027-learning-rate/README.md)
