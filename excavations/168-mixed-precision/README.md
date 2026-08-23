# Excavation 168 — Mixed Precision — Stop Storing Every Number with Unneeded Detail

<!-- book-prose-v2 -->

Stable gradients now expose the physical bill: weights, activations, and gradients are stored and moved as wide numbers even when many operations tolerate fewer bits.

The least expensive next move is to convert every value and every update permanently to half precision.

The proposal deserves a fair hearing. For mixed precision, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Now keep that rule fixed and let the difficult case enter: small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range.

The failure changes the question behind mixed precision. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision.

Only at this point does the inherited name **Mixed Precision** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of mixed precision by mentally removing the repair. We fall back to the proposal to convert every value and every update permanently to half precision; then small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range. Restore only the ability to use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to convert every value and every update permanently to half precision to requiring the system to use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to mixed precision.

## Stop Storing Every Number with Unneeded Detail

A million activation values require roughly two megabytes at 16 bits instead of four at 32 bits, while a 32-bit master weight accumulates tiny updates safely.

Put the old procedure beside mixed precision. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside mixed precision

Do not read the coming Mixed Precision line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Place one million model activation numbers in memory. At 32 bits each they occupy 32 million bits; at 16 bits each, 16 million bits. Hardware reports bytes, with eight bits in each byte, so divide either total by eight: four megabytes versus two. N counts the values, b is the chosen bits per value, and M is the resulting payload in bytes.

N is the number of stored scalar values, b is bits per value, and division by eight converts bits into bytes.

### Why no cheaper operation does the same job

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because every one of N values consumes b bits. [Division](../../MATHEMATICAL_MOVES.md#division) converts units using eight bits per byte; adding eight would not perform a unit conversion. The equality describes payload memory and intentionally omits allocator overhead.

Every symbol in Mixed Precision can now be read back into an action already performed. The whole procedure fits in one line:

$$
M=\frac{N b}{8}\ \text{bytes}
$$

## Where mixed precision runs out

Mixed precision reduces representation cost, but numeric range—not only bit count—still threatens small gradients.

The limit follows from the job assigned to mixed precision. Its repair knows how to use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take mixed precision to the workbench

A claim about mixed precision now exists on the page; the laboratory must be able to contradict it. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running mixed precision, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the mixed precision result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Loss Scaling — Rescue Gradients Too Small to Represent](../169-loss-scaling/README.md)
