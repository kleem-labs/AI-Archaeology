# Excavation 171 — Activation Checkpointing — Remember Less, Recompute Exactly

Only one micro-batch is resident, yet backpropagation retains every layer's intermediate values until their gradients are computed.

Perhaps we delete all activations after the forward pass.

It survives until the measured run answers back. Backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly.

Now the missing requirement is concrete. Keep selected checkpoint activations and recompute the missing segments once when backward reaches them.

## Let one run decide

In a nine-layer chain, retain boundaries around three-layer segments. Backward rebuilds one segment at a time instead of storing all nine layers.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

In a model chain of nine layers, keeping every activation costs nine stored boundaries. Keep only layers 0, 3, and 6; during backward work, rebuild the three missing operations inside the needed segment. For a much longer chain, choosing about the square root of L boundaries creates segments of about the same length, balancing stored checkpoints against recomputation. Big-O records this growth pattern, not an exact byte count.

L is the number of sequential layers and the expression records the memory-growth order under a balanced basic checkpoint scheme.

### Why these operations are forced

[Square root](../../MATHEMATICAL_MOVES.md#square-root) appears because balancing roughly sqrt(L) stored boundaries with sqrt(L)-sized recomputed segments minimizes the larger side of the trade. [Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) is implicit in big-O: exact bytes depend on activation shapes and implementation.

Only now can we compress the procedure:

$$
M_{\text{activations}}=O(\sqrt{L})
$$

## What this repair cannot do

Checkpointing buys memory with extra computation; a poor partition can save little or recompute too much.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: ZeRO — Stop Replicating the Same Training State](../172-zero-sharding/README.md)
