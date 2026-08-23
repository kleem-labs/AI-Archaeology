# Excavation 171 — Activation Checkpointing — Remember Less, Recompute Exactly

<!-- book-prose-v2 -->

Only one micro-batch is resident, yet backpropagation retains every layer's intermediate values until their gradients are computed.

The machinery already in our hands suggests that we delete all activations after the forward pass.

This is how activation checkpointing ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Then a case arrives in which convenience and truth separate: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly.

The wrong answer makes the need for activation checkpointing inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: keep selected checkpoint activations and recompute the missing segments once when backward reaches them.

The usual name, **Activation Checkpointing**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to delete all activations after the forward pass produces the observed failure: backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly. Starting with the repaired demand to keep selected checkpoint activations and recompute the missing segments once when backward reaches them preserves the information the shortcut lost. The subject of activation checkpointing lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to keep selected checkpoint activations and recompute the missing segments once when backward reaches them instead of merely trying to delete all activations after the forward pass. That controlled contrast is what turns a plausible explanation of activation checkpointing into an understandable derivation.

## Remember Less, Recompute Exactly

In a nine-layer chain, retain boundaries around three-layer segments. Backward rebuilds one segment at a time instead of storing all nine layers.

There are now two histories of this activation checkpointing case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## The calculation hidden inside activation checkpointing

Before Activation Checkpointing receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

In a model chain of nine layers, keeping every activation costs nine stored boundaries. Keep only layers 0, 3, and 6; during backward work, rebuild the three missing operations inside the needed segment. For a much longer chain, choosing about the square root of L boundaries creates segments of about the same length, balancing stored checkpoints against recomputation. Big-O records this growth pattern, not an exact byte count.

L is the number of sequential layers and the expression records the memory-growth order under a balanced basic checkpoint scheme.

### Why no cheaper operation does the same job

[Square root](../../MATHEMATICAL_MOVES.md#square-root) appears because balancing roughly sqrt(L) stored boundaries with sqrt(L)-sized recomputed segments minimizes the larger side of the trade. [Proportionality](../../MATHEMATICAL_MOVES.md#proportionality) is implicit in big-O: exact bytes depend on activation shapes and implementation.

Every symbol in Activation Checkpointing can now be read back into an action already performed. The whole procedure fits in one line:

$$
M_{\text{activations}}=O(\sqrt{L})
$$

## Where activation checkpointing runs out

Checkpointing buys memory with extra computation; a poor partition can save little or recompute too much.

Look back at what activation checkpointing actually preserves: it can keep selected checkpoint activations and recompute the missing segments once when backward reaches them. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take activation checkpointing to the workbench

The reader has reconstructed activation checkpointing in words; the workbench tests whether those words specify a real procedure. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running activation checkpointing, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the activation checkpointing result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: ZeRO — Stop Replicating the Same Training State](../172-zero-sharding/README.md)
