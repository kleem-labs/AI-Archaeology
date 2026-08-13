# Excavation 168 — Mixed Precision — Stop Storing Every Number with Unneeded Detail

Stable gradients now expose the physical bill: weights, activations, and gradients are stored and moved as wide numbers even when many operations tolerate fewer bits.

Perhaps we convert every value and every update permanently to half precision.

It survives until the measured run answers back. Small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range.

Now the missing requirement is concrete. Use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision.

## Let one run decide

A million activation values require roughly two megabytes at 16 bits instead of four at 32 bits, while a 32-bit master weight accumulates tiny updates safely.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Place one million model activation numbers in memory. At 32 bits each they occupy 32 million bits; at 16 bits each, 16 million bits. Hardware reports bytes, with eight bits in each byte, so divide either total by eight: four megabytes versus two. N counts the values, b is the chosen bits per value, and M is the resulting payload in bytes.

N is the number of stored scalar values, b is bits per value, and division by eight converts bits into bytes.

### Why these operations are forced

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because every one of N values consumes b bits. [Division](../../MATHEMATICAL_MOVES.md#division) converts units using eight bits per byte; adding eight would not perform a unit conversion. The equality describes payload memory and intentionally omits allocator overhead.

Only now can we compress the procedure:

$$
M=\frac{N b}{8}\ \text{bytes}
$$

## What this repair cannot do

Mixed precision reduces representation cost, but numeric range—not only bit count—still threatens small gradients.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Loss Scaling — Rescue Gradients Too Small to Represent](../169-loss-scaling/README.md)
