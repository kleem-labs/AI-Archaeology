# Excavation 171 — Activation Checkpointing — Remember Less, Recompute Exactly

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Calculus & Differential Change](../../MATHEMATICS_ATLAS.md#calculus) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Only one micro-batch is resident, yet backpropagation retains every layer's intermediate values until their gradients are computed.

Night gathers around the Engine Cavern. Under the light of the brass reference machine, the enginewright refuses to invent prematurely and begins with the plain rule: delete all activations after the forward pass.

Then the quiet test arrives: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly. What looked like simplicity is revealed as a missing distinction.

*The enginewright sketches the break before changing it:*

```text
OLD PATH:  request ──▶ delete all activations after the… ──▶ backward computation then lacks the…
                         ╲
                          ╲ missing boundary
NEW PATH:  request ──▶ keep selected checkpoint activations… ──▶ accountable result
```

The enginewright turns the brass reference machine toward the light. Through the old engraving, delete all activations after the forward pass, the evidence ends in the same contradiction: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly. A second engraving adds only the power to keep selected checkpoint activations and recompute the missing segments once when backward reaches them. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The enginewright circles the place where the two activation checkpointing cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: keep selected checkpoint activations and recompute the missing segments once when backward reaches them. The enginewright writes **Activation Checkpointing** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The enginewright places a finger over the new distinction. At once the two cases collapse and backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly. Lifting the finger restores only this capacity: keep selected checkpoint activations and recompute the missing segments once when backward reaches them. That tiny reversible motion is the chapter's proof of necessity.

## Remember Less, Recompute Exactly

In a nine-layer chain, retain boundaries around three-layer segments. Backward rebuilds one segment at a time instead of storing all nine layers.

## The calculation hidden inside activation checkpointing

The enginewright carries the activation checkpointing scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

In a model chain of nine layers, keeping every activation costs nine stored boundaries. Keep only layers 0, 3, and 6; during backward work, rebuild the three missing operations inside the needed segment. For a much longer chain, choosing about the square root of L boundaries creates segments of about the same length, balancing stored checkpoints against recomputation. Big-O records this growth pattern, not an exact byte count.

L is the number of sequential layers and the expression records the memory-growth order under a balanced basic checkpoint scheme.

### Why the melody needs these exact notes

[Square root](../../MATHEMATICAL_MOVES.md#square-root) appears because balancing roughly sqrt(L) stored boundaries with sqrt(L)-sized recomputed segments minimizes the larger side of the trade. [Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) is implicit in big-O: exact bytes depend on activation shapes and implementation.

The symbols are about to change costume, but their work has appeared before: **the road home**—a squared construction returns to the scale of the world that created it. This is how distant excavations begin to sound like variations of one melody.

The story of activation checkpointing has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
M_{\text{activations}}=O(\sqrt{L})
$$

## Where activation checkpointing runs out

Checkpointing buys memory with extra computation; a poor partition can save little or recompute too much.

One unsolved mark remains on the brass reference machine. None of the responsibilities inside Activation Checkpointing can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the brass reference machine

Rebuild the activation checkpointing scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: ZeRO — Stop Replicating the Same Training State](../172-zero-sharding/README.md)
