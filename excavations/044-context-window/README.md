# Excavation 044 — Context Windows — How Much Past Can the Model Carry?

<!-- book-prose-v2 -->

Sampling allows several plausible futures instead of one repetitive path. Every chosen token is appended to the past, so the amount of history available to attention grows until computation or memory reaches a boundary.

The first defensible move is to attend to the entire history forever.

There is a real principle behind this restraint: the complexity of context windows must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The proposal breaks for a specific reason, not by authority: computation and memory grow, and the model eventually exceeds positions it was trained to handle.

That distinction is the hinge on which context windows turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past.

We have earned the chapter's shorter name: **Context Windows**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that context windows is necessary rather than decorative. Delete its new responsibility and use the earlier plan to attend to the entire history forever.. Immediately, computation and memory grow, and the model eventually exceeds positions it was trained to handle. Reintroduce the single job to choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can choose a maximum context, train within it, and reuse cached keys and values during generation instead of recomputing the unchanged past. Because the old plan to attend to the entire history forever. is the only displaced piece, the reader can locate exactly where context windows changes the outcome.

## The calculation hidden inside context windows

Do not read the coming Context Windows line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

A larger window is not perfect memory. Retrieval, compression, recurrence, and careful data are separate inventions.

Four words create sixteen possible question–source comparisons: each of four positions may inspect four positions. Eight words create sixty-four. The reader can see the growth by drawing the square table: doubling each side multiplies the number of cells by four. The cost comes from pairwise looking, not from storing eight words alone.

### Names for pieces we have already used

**n** is the number of tokens inside the active context.
Each of n queries can compare with n keys, creating roughly n×n score pairs.
That repeated pairwise work is why cost grows proportionally to n² rather than n.
The proportional sign is used because heads, width, batching, and implementation add constants omitted from this scaling argument.

### Why no cheaper operation does the same job

[Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) states the growth pattern without pretending every implementation has the same fixed cost.
[The square](../../MATHEMATICAL_MOVES.md#powers) appears because each of n query positions can compare with n key positions, creating n×n pairs. A linear n would count only one comparison per token.

The notation is finally shorter than the story that created it:

$$
\text{attention cost}\propto n^2
$$

The equation arrives after every operation has a job.

## Context Windows beyond this one case

A desk holds only a finite number of open pages. Notes and indexes can preserve selected information after pages leave the desk.

## Take context windows to the workbench

Understanding context windows now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running context windows, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the context windows result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 045](../045-tiny-gpt/README.md)
