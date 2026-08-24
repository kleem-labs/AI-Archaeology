# Excavation 196 — Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Data and pretraining operations

Deterministic resume makes failures reproducible. During a long run, the observed loss sometimes jumps; automatically rewinding every jump wastes compute, while ignoring a sustained instability can destroy the model.

Inside the Archive Foundry, every old tool is given one honest chance. The archivist-engineer sets the chain-of-custody ledger between the evidence and the desired answer, then tries to declare any loss larger than the previous loss a failure and restore immediately.

The archivist-engineer repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule. The failure is stable enough to become evidence.

*The archivist-engineer sketches the break before changing it:*

```text
possible road A ─┐
                 ├── old map: declare any loss larger than the…
possible road B ─┘              └── loses: ordinary batches vary, so healthy…

same roads ──▶ repaired map ──▶ compare current loss and gradient…
```

Across the chain-of-custody ledger, the old path and the repaired path run side by side. One carries “declare any loss larger than the previous loss a failure and restore immediately”; the other knows how to compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response. When the failure—ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to loss spikes. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response. This problem and its repair will travel under the name **Loss Spikes**, but the name carries no knowledge the scene has not earned.

What changed on the chain-of-custody ledger can be said without symbols. Before, the method could only declare any loss larger than the previous loss a failure and restore immediately; now it can also compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response. Everything that follows—notation, code, and machinery—is a way of repeating that one human distinction without losing it.

## Distinguish One Hard Batch from a Run Leaving the Road

Recent clean validation losses center near 2.0 with spread 0.1. One batch reaches 2.35 and then returns; another run stays above 2.5 while gradient norm grows. Only the persistent, corroborated event triggers recovery.

## The calculation hidden inside loss spikes

The archivist-engineer carries the loss spikes scene to the chain-of-custody ledger. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

L_t is the current monitored model loss, mu_t is its robust recent center, sigma_t is ordinary recent spread, and z_t says how many usual spreads the current value lies above or below that center.

### Why the melody needs these exact notes

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the local baseline. [Division](../../MATHEMATICAL_MOVES.md#division) expresses the remainder in units of ordinary variation, making different loss scales comparable. A raw threshold would behave differently as normal loss falls during training.

Inside loss spikes, familiar operations return with stricter duties: **the chisel**—what is shared is removed so the remaining change can be seen; and **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large. The metaphor is useful only as long as it predicts what the operation will do in the worked case.

Cover the prose about loss spikes and each mark can still be recovered from the case. Only now is the compressed form safe to write:

$$
z_t=\frac{L_t-\mu_t}{\sigma_t}
$$

## Where loss spikes runs out

Thresholds detect symptoms, not causes; corrupt data, overflow, optimizer settings, hardware faults, and architectural instability require different repairs.

The loss spikes repair holds, but the world asks for something it was never given. At the Archive Foundry, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the chain-of-custody ledger

Rebuild the loss spikes scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: A Validation Stream — Ask Whether Learning Survives Outside the Current Batch](../197-validation-stream/README.md)
