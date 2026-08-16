# Excavation 195 — Deterministic Resume — Continue the Same Experiment, Not a Similar One

The sharded checkpoint can reconstruct every distributed tensor. If it omits the sampler cursor, random-number generators, scheduler phase, or overflow state, restart follows a different future.

We first try to restore model weights and let every other component start fresh.

That confidence lasts only until the first measurement. Adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run.

What broke tells us what the next design must preserve. Checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps.

## Let one run decide

The station stops after update 200, restores weights, Adam moments, schedule position, scaler, RNG streams, and each data cursor, then reproduces updates 201 through 205 byte for byte on the reference implementation.

## What this repair cannot do

Exact replay can still fail across nondeterministic kernels, changed hardware, libraries, or distributed timing; the required reproducibility level must be stated.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road](../196-loss-spike-recovery/README.md)
