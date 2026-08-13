# Excavation 172 — ZeRO — Stop Replicating the Same Training State

Recomputation makes the forward graph fit, but AdamW stores parameters, gradients, first moments, and second moments. Ordinary data parallelism copies all of them onto every device.

Perhaps we add devices and replicate the full training state on each one.

It survives until the measured run answers back. Compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns.

Now the missing requirement is concrete. Partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.

## Let one run decide

Four workers each keep roughly one quarter of a large moment vector rather than four complete copies, then cooperate for the update.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Adam's moment state has twelve equal chunks and four devices are cooperating. Replication gives every device all twelve; sharding gives each device three. Asking for state per device therefore means sharing the total across P owners: total divided by P. The approximation sign remains because temporary gathers and uneven tensor sizes prevent the physical memory from being exactly that ideal share.

M_total is shardable model state and P is the number of cooperating devices under an ideal balanced partition.

### Why these operations are forced

[Division](../../MATHEMATICAL_MOVES.md#division) expresses an equal share per device. Multiplication describes the failed replicated system's total cluster memory, not the amount one device must hold. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) admits temporary gathers, buffers, and uneven tensors.

Only now can we compress the procedure:

$$
M_{\text{state per device}}\approx\frac{M_{\text{total state}}}{P}
$$

## What this repair cannot do

Because a worker no longer owns a complete state by itself, sharding trades redundant memory for communication and makes recovery and state ownership more complex.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Tensor Parallelism — Split One Matrix That No Device Can Hold](../173-tensor-parallelism/README.md)
