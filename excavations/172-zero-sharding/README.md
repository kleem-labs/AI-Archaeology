# Excavation 172 — ZeRO — Stop Replicating the Same Training State

<!-- book-prose-v2 -->

Recomputation makes the forward graph fit, but AdamW stores parameters, gradients, first moments, and second moments. Ordinary data parallelism copies all of them onto every device.

If the old idea can be stretched one step farther, we should add devices and replicate the full training state on each one.

If the proposal works on every relevant case, zero is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The proposal breaks for a specific reason, not by authority: compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns.

Nothing magical creates zero. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.

This boundary between the failed rule and its repair is the subject later work calls **ZeRO**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize zero; try to break it by subtraction. Remove the part that knows how to partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them, leaving only the attempt to add devices and replicate the full training state on each one. What returns is not a vague weakness but the original contradiction: compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to add devices and replicate the full training state on each one receives the same test as the rule to partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them. Their different outcomes reveal what zero contributes without asking the reader to trust historical convention.

## Stop Replicating the Same Training State

Four workers each keep roughly one quarter of a large moment vector rather than four complete copies, then cooperate for the update.

Hold the setting, evidence, and desired outcome fixed while testing zero. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## The calculation hidden inside zero

Do not read the coming ZeRO line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Adam's moment state has twelve equal chunks and four devices are cooperating. Replication gives every device all twelve; sharding gives each device three. Asking for state per device therefore means sharing the total across P owners: total divided by P. The approximation sign remains because temporary gathers and uneven tensor sizes prevent the physical memory from being exactly that ideal share.

M_total is shardable model state and P is the number of cooperating devices under an ideal balanced partition.

### Why no cheaper operation does the same job

[Division](../../MATHEMATICAL_MOVES.md#division) expresses an equal share per device. Multiplication describes the failed replicated system's total cluster memory, not the amount one device must hold. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) admits temporary gathers, buffers, and uneven tensors.

Every symbol in ZeRO can now be read back into an action already performed. The whole procedure fits in one line:

$$
M_{\text{state per device}}\approx\frac{M_{\text{total state}}}{P}
$$

## Where zero runs out

Because a worker no longer owns a complete state by itself, sharding trades redundant memory for communication and makes recovery and state ownership more complex.

This is where zero runs out for a causal reason. We gave it enough structure to partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take zero to the workbench

A mathematical story about zero earns trust only when the failed and repaired paths can both be reproduced. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running zero, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the zero result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Tensor Parallelism — Split One Matrix That No Device Can Hold](../173-tensor-parallelism/README.md)
