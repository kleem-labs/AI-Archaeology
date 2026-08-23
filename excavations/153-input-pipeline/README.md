# Excavation 153 — The Input Pipeline — Stop Making the Accelerator Wait

<!-- book-prose-v2 -->

Profiling reveals that the accelerator repeatedly waits for the next token batch. The model is ready, but its evidence is still being read and prepared.

At this point the shortest path seems to be to load a batch, wait until loading finishes, compute it, and only then begin loading the next one.

This is how the input pipeline ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

The world supplies the one comparison the shortcut hoped never to face: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle.

The wrong answer makes the need for the input pipeline inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering.

The usual name, **The Input Pipeline**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to load a batch, wait until loading finishes, compute it, and only then begin loading the next one produces the observed failure: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle. Starting with the repaired demand to prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering preserves the information the shortcut lost. The subject of the input pipeline lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering instead of merely trying to load a batch, wait until loading finishes, compute it, and only then begin loading the next one. That controlled contrast is what turns a plausible explanation of the input pipeline into an understandable derivation.

## Stop Making the Accelerator Wait

If loading takes 35 ms and compute 45 ms, serial work costs 80 ms. Once overlapped, a steady-state step is governed mainly by the slower 45 ms stage.

There are now two histories of this the input pipeline case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## The calculation hidden inside the input pipeline

Before The Input Pipeline receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Now give the ranger station's data loader and accelerator separate workers and start both together. Loading finishes after 35 ms, but the next step is still waiting for computation at 45 ms. The pair is ready when the slower worker finishes—not after 35+45 ms. That finishing time is what T_overlapped records; the approximation sign leaves room for pipeline startup and coordination.

The two times describe stages allowed to run concurrently after the pipeline is filled.

### Why no cheaper operation does the same job

[Maximum](../../MATHEMATICAL_MOVES.md#maximum) appears because concurrent stages finish when the slower one finishes. Adding would describe serial execution—the failed design. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) admits startup, synchronization, and overhead that prevent perfect overlap.

Every symbol in The Input Pipeline can now be read back into an action already performed. The whole procedure fits in one line:

$$
T_{\text{overlapped}}\approx\max(T_{\text{data}},T_{\text{compute}})
$$

## Where the input pipeline runs out

Prefetching can hide latency, not unlimited data cost; workers, memory, or storage bandwidth can become the next limit.

Look back at what the input pipeline actually preserves: it can prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take the input pipeline to the workbench

The reader has reconstructed the input pipeline in words; the workbench tests whether those words specify a real procedure. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running the input pipeline, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the the input pipeline result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Sequence Packing — Stop Training on Empty Space](../154-sequence-packing/README.md)
