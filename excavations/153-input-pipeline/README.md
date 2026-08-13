# Excavation 153 — The Input Pipeline — Stop Making the Accelerator Wait

Profiling reveals that the accelerator repeatedly waits for the next token batch. The model is ready, but its evidence is still being read and prepared.

Perhaps we load a batch, wait until loading finishes, compute it, and only then begin loading the next one.

It survives until the measured run answers back. Data time and compute time are paid sequentially on every step, leaving expensive compute hardware idle.

Now the missing requirement is concrete. Prepare the next batch while the current batch computes, using bounded prefetching and deterministic ordering.

## Let one run decide

If loading takes 35 ms and compute 45 ms, serial work costs 80 ms. Once overlapped, a steady-state step is governed mainly by the slower 45 ms stage.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Now give the ranger station's data loader and accelerator separate workers and start both together. Loading finishes after 35 ms, but the next step is still waiting for computation at 45 ms. The pair is ready when the slower worker finishes—not after 35+45 ms. That finishing time is what T_overlapped records; the approximation sign leaves room for pipeline startup and coordination.

The two times describe stages allowed to run concurrently after the pipeline is filled.

### Why these operations are forced

[Maximum](../../MATHEMATICAL_MOVES.md#maximum) appears because concurrent stages finish when the slower one finishes. Adding would describe serial execution—the failed design. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) admits startup, synchronization, and overhead that prevent perfect overlap.

Only now can we compress the procedure:

$$
T_{\text{overlapped}}\approx\max(T_{\text{data}},T_{\text{compute}})
$$

## What this repair cannot do

Prefetching can hide latency, not unlimited data cost; workers, memory, or storage bandwidth can become the next limit.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Sequence Packing — Stop Training on Empty Space](../154-sequence-packing/README.md)
