# Excavation 195 — Deterministic Resume — Continue the Same Experiment, Not a Similar One

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics)
>
> **Applied territory:** Data and pretraining operations

The sharded checkpoint can reconstruct every distributed tensor. If it omits the sampler cursor, random-number generators, scheduler phase, or overflow state, restart follows a different future.

Night gathers around the Archive Foundry. Under the light of the chain-of-custody ledger, the archivist-engineer refuses to invent prematurely and begins with the plain rule: restore model weights and let every other component start fresh.

Then the quiet test arrives: adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run. What looked like simplicity is revealed as a missing distinction.

*The archivist-engineer sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ restore model weights and let every… ──▶ blurred: adam forgets its moments, warmup may…
      │
      └── new lens ──▶ checkpoint every state variable that… ──▶ distinction survives
```

The archivist-engineer turns the chain-of-custody ledger toward the light. Through the old engraving, restore model weights and let every other component start fresh, the evidence ends in the same contradiction: adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run. A second engraving adds only the power to checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The archivist-engineer circles the place where the two deterministic resume cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps. The archivist-engineer writes **Deterministic Resume** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The archivist-engineer places a finger over the new distinction. At once the two cases collapse and adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run. Lifting the finger restores only this capacity: checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps. That tiny reversible motion is the chapter's proof of necessity.

<!-- memory-film-v1:start -->
> **Memory realm 13 of 18 — [Archive Foundry](../../MEMORY_PALACE.md#realm-13)**
>
> **The question carried into this chamber:** What fails if we restore model weights and let every other component start fresh?

## When the chamber changes

The Deterministic Resume room does not ask you to memorize its name. It asks you to watch one object change.

First hold the failed picture still: The lantern follows the tempting path—restore model weights and let every other component start fresh. Then the evidence answers: adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run.

Now let the chamber move: The archivist-engineer changes one moving part. The lantern can now checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps.

The object that should remain after the terminology disappears is **the deterministic resume lantern mounted on the chain-of-custody ledger**.

> **Memory seal — Deterministic Resume**
>
> Deterministic Resume keeps the missing power: checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps.

Give the idea a bodily path: Touch the deterministic resume lantern in imagination: close one fist around the lost information, then open it as the repair restores that information.
<!-- memory-film-v1:end -->

## Continue the Same Experiment, Not a Similar One

The station stops after update 200, restores weights, Adam moments, schedule position, scaler, RNG streams, and each data cursor, then reproduces updates 201 through 205 byte for byte on the reference implementation.

## Where deterministic resume runs out

Exact replay can still fail across nondeterministic kernels, changed hardware, libraries, or distributed timing; the required reproducibility level must be stated.

One unsolved mark remains on the chain-of-custody ledger. None of the responsibilities inside Deterministic Resume can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the chain-of-custody ledger

Rebuild the deterministic resume scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road](../196-loss-spike-recovery/README.md)
