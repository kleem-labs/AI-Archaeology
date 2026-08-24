# Excavation 153 — The Input Pipeline — Stop Making the Accelerator Wait

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical) · [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra)
>
> **Applied territory:** Model systems and engine optimization

Profiling reveals that the accelerator repeatedly waits for the next token batch. The model is ready, but its evidence is still being read and prepared.

Morning reaches the Engine Cavern before anyone has a name for today's difficulty. Beside the brass reference machine, the enginewright tries the smallest continuation of what already works: load a batch, wait until loading finishes, compute it, and only then begin loading the next one.

Then the quiet test arrives: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle. What looked like simplicity is revealed as a missing distinction.

*The enginewright sketches the break before changing it:*

```text
OLD PATH:  request ──▶ load a batch, wait until loading… ──▶ data time and compute time are paid…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ prepare the next batch while the… ──▶ accountable result
```

The enginewright turns the brass reference machine toward the light. Through the old engraving, load a batch, wait until loading finishes, compute it, and only then begin loading the next one, the evidence ends in the same contradiction: data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle. A second engraving adds only the power to prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The enginewright circles the place where the two input pipeline cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering. The enginewright writes **The Input Pipeline** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The enginewright does not memorize input pipeline. Instead, the enginewright memorizes a motion: begin with the old rule, let the counterexample press against it, then open a place where the method can prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering. The formal name merely lets that motion be shared.

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
