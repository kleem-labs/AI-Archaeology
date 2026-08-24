# Excavation 168 — Mixed Precision — Stop Storing Every Number with Unneeded Detail

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Stable gradients now expose the physical bill: weights, activations, and gradients are stored and moved as wide numbers even when many operations tolerate fewer bits.

At the Engine Cavern, the enginewright returns to the brass reference machine. Yesterday's instrument still lies open, so the first move asks for no new magic: convert every value and every update permanently to half precision.

For a moment the mark looks complete. Then the evidence refuses to fit: small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range. The old line has not become false everywhere; it has reached the precise place where it can no longer see.

*The enginewright sketches the break before changing it:*

```text
reference evidence ──▶ shortcut: convert every value and every update…
                         │
                         └── mismatch: small updates disappear when rounded…

reference evidence ──▶ measured repair: use reduced precision for bulk…
```

The enginewright lays two translucent sheets over the brass reference machine. The first is inscribed, “convert every value and every update permanently to half precision.” Its path ends where small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range. The second receives the same evidence but is allowed to use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision. Held to the light, the sheets separate at exactly one decision.

No one reaches for a mixed precision formula. The only useful question is smaller: what did the first path lose that the second path must carry?

The enginewright changes only that one responsibility: use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision. When the ink dries, the name **Mixed Precision** is added in the margin—not as an answer from authority, but as the name of the doorway just crossed.

The brass reference machine keeps both histories. Its older mark still says, ‘convert every value and every update permanently to half precision’; beside it, the newer mark says, ‘use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision.’ The distance between those sentences is the exact shape of mixed precision: no larger than the failure required, and no smaller than reality permits.

## Stop Storing Every Number with Unneeded Detail

A million activation values require roughly two megabytes at 16 bits instead of four at 32 bits, while a 32-bit master weight accumulates tiny updates safely.

## The calculation hidden inside mixed precision

The enginewright carries the mixed precision scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Place one million model activation numbers in memory. At 32 bits each they occupy 32 million bits; at 16 bits each, 16 million bits. Hardware reports bytes, with eight bits in each byte, so divide either total by eight: four megabytes versus two. N counts the values, b is the chosen bits per value, and M is the resulting payload in bytes.

N is the number of stored scalar values, b is bits per value, and division by eight converts bits into bytes.

### Why the melody needs these exact notes

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because every one of N values consumes b bits. [Division](../../MATHEMATICAL_MOVES.md#division) converts units using eight bits per byte; adding eight would not perform a unit conversion. The equality describes payload memory and intentionally omits allocator overhead.

Listen beneath mixed precision: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. These are not ornamental comparisons. Each image keeps the exact job of an operation visible while its symbols change.

Every mark needed for mixed precision is now visible on the brass reference machine. The symbols do not add an idea; they bind the discovered moves into one line:

$$
M=\frac{N b}{8}\ \text{bytes}
$$

## Where mixed precision runs out

Mixed precision reduces representation cost, but numeric range—not only bit count—still threatens small gradients.

At the Engine Cavern, the enginewright leaves a blank beneath the new mark. Mixed Precision has no operation that can answer it, so the blank—not a promised solution—travels onward.

## Return to the brass reference machine

Rebuild the mixed precision scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Loss Scaling — Rescue Gradients Too Small to Represent](../169-loss-scaling/README.md)
