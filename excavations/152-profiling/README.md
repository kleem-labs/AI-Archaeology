# Excavation 152 — Profiling — Measure Where the Time Went

<!-- book-prose-v2 -->

A reproducible baseline gives us a trustworthy before-state. Its first run is too slow for the ranger station, but a total runtime does not identify the guilty stage.

The first defensible move is to optimize the largest-looking matrix because attention is famous for being expensive.

There is a real principle behind this restraint: the complexity of profiling must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Now keep that rule fixed and let the difficult case enter: the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock.

That distinction is the hinge on which profiling turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: measure data loading, computation, communication, and idle time separately before choosing a repair.

We have earned the chapter's shorter name: **Profiling**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that profiling is necessary rather than decorative. Delete its new responsibility and use the earlier plan to optimize the largest-looking matrix because attention is famous for being expensive. Immediately, the device spends much of the run waiting for data and moving tensors. Making one matrix faster barely changes the wall clock. Reintroduce the single job to measure data loading, computation, communication, and idle time separately before choosing a repair. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can measure data loading, computation, communication, and idle time separately before choosing a repair. Because the old plan to optimize the largest-looking matrix because attention is famous for being expensive is the only displaced piece, the reader can locate exactly where profiling changes the outcome.

## Measure Where the Time Went

A 100 ms step contains 35 ms of loading, 45 ms of compute, 10 ms of communication, and 10 ms idle. The first engineering question is now visible in numbers.

The name profiling is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## The calculation hidden inside profiling

Do not read the coming Profiling line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Start a stopwatch with one training step. Loading ends at 35 ms; computation then carries the clock to 80; communication to 90; idle synchronization to 100. These are consecutive pieces of one elapsed interval, so you join them end to end. The name T_step is simply the final reading after T_data, T_compute, T_communication, and T_idle have all contributed.

Each T names elapsed time assigned to one non-overlapping stage of the same training step.

### Why no cheaper operation does the same job

[Addition](../../MATHEMATICAL_MOVES.md#addition) is forced because these non-overlapping durations occur along one wall-clock path and accumulate into total time. Multiplication would claim that doubling one stage scales every other stage. The equality is valid only when the measured categories cover the step without overlap.

Every symbol in Profiling can now be read back into an action already performed. The whole procedure fits in one line:

$$
T_{\text{step}}=T_{\text{data}}+T_{\text{compute}}+T_{\text{communication}}+T_{\text{idle}}
$$

## Where profiling runs out

A profile describes this workload on this hardware; changing sequence length or batch size can move the bottleneck.

The weakness is not an accidental footnote. Every operation in profiling serves the narrower purpose to measure data loading, computation, communication, and idle time separately before choosing a repair; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take profiling to the workbench

Understanding profiling now means predicting its intermediate results before asking software for an answer. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running profiling, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the profiling result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: The Input Pipeline — Stop Making the Accelerator Wait](../153-input-pipeline/README.md)
