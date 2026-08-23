# Excavation 196 — Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road

<!-- book-prose-v2 -->

Deterministic resume makes failures reproducible. During a long run, the observed loss sometimes jumps; automatically rewinding every jump wastes compute, while ignoring a sustained instability can destroy the model.

If the old idea can be stretched one step farther, we should declare any loss larger than the previous loss a failure and restore immediately.

If the proposal works on every relevant case, loss spikes is unnecessary. A mathematical object is earned only when the world can force the old description into contradiction.

The proposal breaks for a specific reason, not by authority: ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule.

Nothing magical creates loss spikes. We retain the part that worked, restore the information the counterexample removed, and refuse every extra complication that performs no necessary job.

The lost distinction tells us what to build: compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response.

This boundary between the failed rule and its repair is the subject later work calls **Loss Spikes**. Naming it adds nothing; the discovery happened when the lost information became visible.

Do not memorize loss spikes; try to break it by subtraction. Remove the part that knows how to compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response, leaving only the attempt to declare any loss larger than the previous loss a failure and restore immediately. What returns is not a vague weakness but the original contradiction: ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule. The removed responsibility therefore has an observable job.

A name can make an invention feel inevitable, but this control removes that illusion. The rule to declare any loss larger than the previous loss a failure and restore immediately receives the same test as the rule to compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response. Their different outcomes reveal what loss spikes contributes without asking the reader to trust historical convention.

## Distinguish One Hard Batch from a Run Leaving the Road

Recent clean validation losses center near 2.0 with spread 0.1. One batch reaches 2.35 and then returns; another run stays above 2.5 while gradient norm grows. Only the persistent, corroborated event triggers recovery.

Hold the setting, evidence, and desired outcome fixed while testing loss spikes. Alter only the failed decision rule. If the answer now distinguishes cases the shortcut collapsed together, the repair has earned its place.

## The calculation hidden inside loss spikes

Do not read the coming Loss Spikes line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

L_t is the current monitored model loss, mu_t is its robust recent center, sigma_t is ordinary recent spread, and z_t says how many usual spreads the current value lies above or below that center.

### Why no cheaper operation does the same job

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the local baseline. [Division](../../MATHEMATICAL_MOVES.md#division) expresses the remainder in units of ordinary variation, making different loss scales comparable. A raw threshold would behave differently as normal loss falls during training.

Every symbol in Loss Spikes can now be read back into an action already performed. The whole procedure fits in one line:

$$
z_t=\frac{L_t-\mu_t}{\sigma_t}
$$

## Where loss spikes runs out

Thresholds detect symptoms, not causes; corrupt data, overflow, optimizer settings, hardware faults, and architectural instability require different repairs.

This is where loss spikes runs out for a causal reason. We gave it enough structure to compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response, and nothing more. The remaining uncertainty therefore survives by design and becomes pressure for the next discovery.

## Take loss spikes to the workbench

A mathematical story about loss spikes earns trust only when the failed and repaired paths can both be reproduced. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running loss spikes, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the loss spikes result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: A Validation Stream — Ask Whether Learning Survives Outside the Current Batch](../197-validation-stream/README.md)
