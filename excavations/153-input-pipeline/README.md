# Excavation 153 — The Input Pipeline — Stop Making the Accelerator Wait

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

Profiling reveals that the accelerator repeatedly waits for the next token batch. The model is ready, but its evidence is still being read and prepared.

The previous discovery reaches the Engine Cavern carrying one unfinished problem. Beside the brass reference machine, the enginewright first tries to load a batch, wait until loading finishes, compute it, and only then begin loading the next one.

There is good reason to begin this way. If we load a batch, wait until loading finishes, compute it, and only then begin loading the next one, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle.

This failure cannot be repaired by performing the instruction to load a batch, wait until loading finishes, compute it, and only then begin loading the next one more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the brass reference machine; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **The Input Pipeline**. The name is simply a handle for the distinction already reconstructed.

## Stop Making the Accelerator Wait

If loading takes 35 ms and compute 45 ms, serial work costs 80 ms. Once overlapped, a steady-state step is governed mainly by the slower 45 ms stage.

## The calculation hidden inside the input pipeline

The enginewright carries the input pipeline scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Now give the ranger station's data loader and accelerator separate workers and start both together. Loading finishes after 35 ms, but the next step is still waiting for computation at 45 ms. The pair is ready when the slower worker finishes—not after 35+45 ms. That finishing time is what T_overlapped records; the approximation sign leaves room for pipeline startup and coordination.

The two times describe stages allowed to run concurrently after the pipeline is filled.

### Why the melody needs these exact notes

[Maximum](../../MATHEMATICAL_MOVES.md#maximum) appears because concurrent stages finish when the slower one finishes. Adding would describe serial execution—the failed design. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) admits startup, synchronization, and overhead that prevent perfect overlap.

The calculation borrows several gestures already encountered elsewhere: **the highest lantern**—the strongest surviving possibility sets the visible ceiling. the input pipeline feels new because the objects are new; the gestures remain recognizably human.

The story of input pipeline has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
T_{\text{overlapped}}\approx\max(T_{\text{data}},T_{\text{compute}})
$$

## Where the input pipeline runs out

Prefetching can hide latency, not unlimited data cost; workers, memory, or storage bandwidth can become the next limit.

One unsolved mark remains on the brass reference machine. None of the responsibilities inside Input Pipeline can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the brass reference machine

Rebuild the input pipeline scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Sequence Packing — Stop Training on Empty Space](../154-sequence-packing/README.md)
