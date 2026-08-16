# Excavation 196 — Loss Spikes — Distinguish One Hard Batch from a Run Leaving the Road

Deterministic resume makes failures reproducible. During a long run, the observed loss sometimes jumps; automatically rewinding every jump wastes compute, while ignoring a sustained instability can destroy the model.

One tempting answer is to declare any loss larger than the previous loss a failure and restore immediately.

The shortcut reaches its first real document and breaks. Ordinary batches vary, so healthy learning triggers constant rollbacks. A slow divergence can rise without one dramatic step and escape the rule.

Now the missing job can be stated plainly. Compare current loss and gradient norm with robust running baselines, require persistence or corroborating signals, preserve the suspect batch, and recover from a verified clean checkpoint under a documented response.

## Let one run decide

Recent clean validation losses center near 2.0 with spread 0.1. One batch reaches 2.35 and then returns; another run stays above 2.5 while gradient norm grows. Only the persistent, corroborated event triggers recovery.

## The arithmetic we have earned

L_t is the current monitored model loss, mu_t is its robust recent center, sigma_t is ordinary recent spread, and z_t says how many usual spreads the current value lies above or below that center.

### Why these operations are forced

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the local baseline. [Division](../../MATHEMATICAL_MOVES.md#division) expresses the remainder in units of ordinary variation, making different loss scales comparable. A raw threshold would behave differently as normal loss falls during training.

Only now can we compress the procedure:

$$
z_t=\frac{L_t-\mu_t}{\sigma_t}
$$

## What this repair cannot do

Thresholds detect symptoms, not causes; corrupt data, overflow, optimizer settings, hardware faults, and architectural instability require different repairs.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: A Validation Stream — Ask Whether Learning Survives Outside the Current Batch](../197-validation-stream/README.md)
