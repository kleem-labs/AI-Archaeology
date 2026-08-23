# Excavation 195 — Deterministic Resume — Continue the Same Experiment, Not a Similar One

<!-- book-prose-v2 -->

The sharded checkpoint can reconstruct every distributed tensor. If it omits the sampler cursor, random-number generators, scheduler phase, or overflow state, restart follows a different future.

The machinery already in our hands suggests that we restore model weights and let every other component start fresh.

This is how deterministic resume ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Then a case arrives in which convenience and truth separate: adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run.

The wrong answer makes the need for deterministic resume inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps.

The usual name, **Deterministic Resume**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to restore model weights and let every other component start fresh produces the observed failure: adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run. Starting with the repaired demand to checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps preserves the information the shortcut lost. The subject of deterministic resume lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps instead of merely trying to restore model weights and let every other component start fresh. That controlled contrast is what turns a plausible explanation of deterministic resume into an understandable derivation.

## Continue the Same Experiment, Not a Similar One

The station stops after update 200, restores weights, Adam moments, schedule position, scaler, RNG streams, and each data cursor, then reproduces updates 201 through 205 byte for byte on the reference implementation.

There are now two histories of this deterministic resume case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## Where deterministic resume runs out

Exact replay can still fail across nondeterministic kernels, changed hardware, libraries, or distributed timing; the required reproducibility level must be stated.

Look back at what deterministic resume actually preserves: it can checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take deterministic resume to the workbench

The reader has reconstructed deterministic resume in words; the workbench tests whether those words specify a real procedure. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running deterministic resume, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the deterministic resume result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road](../196-loss-spike-recovery/README.md)
