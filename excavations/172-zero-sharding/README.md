# Excavation 172 — ZeRO — Stop Replicating the Same Training State

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization)
>
> **Applied territory:** Model systems and engine optimization

Recomputation makes the forward graph fit, but AdamW stores parameters, gradients, first moments, and second moments. Ordinary data parallelism copies all of them onto every device.

Inside the Engine Cavern, every old tool is given one honest chance. The enginewright sets the brass reference machine between the evidence and the desired answer, then tries to add devices and replicate the full training state on each one.

The enginewright repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns. The failure is stable enough to become evidence.

*The enginewright sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ add devices and replicate the full… ──▶ blurred: compute capacity grows while…
      │
      └── new lens ──▶ partition optimizer states,… ──▶ distinction survives
```

Across the brass reference machine, the old path and the repaired path run side by side. One carries “add devices and replicate the full training state on each one”; the other knows how to partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them. When the failure—compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to zero. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them. This problem and its repair will travel under the name **ZeRO**, but the name carries no knowledge the scene has not earned.

What changed on the brass reference machine can be said without symbols. Before, the method could only add devices and replicate the full training state on each one; now it can also partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

<!-- memory-film-v1:start -->
> **Memory realm 12 of 18 — [Engine Cavern](../../MEMORY_PALACE.md#realm-12)**
>
> **The question carried into this chamber:** What fails if we add devices and replicate the full training state on each one?

## When the chamber changes

The ZeRO chamber leaves one scene behind so the idea can be recovered after its symbols fade.

First hold the failed picture still: The map follows the tempting path—add devices and replicate the full training state on each one. Then the evidence answers: compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns.

Now let the chamber move: The enginewright changes one moving part. The map can now partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.

The object that should remain after the terminology disappears is **the zero map mounted on the brass reference machine**.

> **Memory seal — ZeRO**
>
> ZeRO keeps the missing power: partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.

Give the idea a bodily path: Touch the zero map in imagination: point backward to the failed attempt, touch the present object, then point forward through the repair.
<!-- memory-film-v1:end -->

## Stop Replicating the Same Training State

Four workers each keep roughly one quarter of a large moment vector rather than four complete copies, then cooperate for the update.

## The calculation hidden inside zero

The enginewright carries the zero scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Adam's moment state has twelve equal chunks and four devices are cooperating. Replication gives every device all twelve; sharding gives each device three. Asking for state per device therefore means sharing the total across P owners: total divided by P. The approximation sign remains because temporary gathers and uneven tensor sizes prevent the physical memory from being exactly that ideal share.

M_total is shardable model state and P is the number of cooperating devices under an ideal balanced partition.

### Why the melody needs these exact notes

[Division](../../MATHEMATICAL_MOVES.md#division) expresses an equal share per device. Multiplication describes the failed replicated system's total cluster memory, not the amount one device must hold. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) admits temporary gathers, buffers, and uneven tensors.

Inside zero, familiar operations return with stricter duties: **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Cover the prose about zero and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
M_{\text{state per device}}\approx\frac{M_{\text{total state}}}{P}
$$

## Where zero runs out

Because a worker no longer owns a complete state by itself, sharding trades redundant memory for communication and makes recovery and state ownership more complex.

The zero repair holds, but the world asks for something it was never given. At the Engine Cavern, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the brass reference machine

Rebuild the zero scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Tensor Parallelism — Split One Matrix That No Device Can Hold](../173-tensor-parallelism/README.md)
