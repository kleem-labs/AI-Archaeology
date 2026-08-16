# Excavation 186 — The Token Budget — Convert a Training Plan into a Count of Lessons

Seeded mixture sampling can produce an ordered stream. The run still says “train for a while,” so neither cost nor source exposure is bounded.

Using what we have, we stop when the wall clock reaches an affordable date.

The plan survives only until the evidence is counted. Faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence.

The lost information tells us what must come next. Define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute.

## Let one run decide

A tiny run uses 2,000 updates with 32 sequences of 128 real tokens each. Every update carries 4,096 lessons, so the complete plan exposes 8,192,000 tokens.

## The arithmetic we have earned

T is the planned number of optimizer updates, B_tokens counts real loss-bearing tokens in one global batch, and N_tokens is the complete exposure budget.

### Why these operations are forced

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) appears because every one of T updates consumes B_tokens lessons. Addition would count only one update plus one batch. Padding is excluded because it occupies hardware but contributes no language target.

Only now can we compress the procedure:

$$
N_{\text{tokens}}=T B_{\text{tokens}}
$$

## What this repair cannot do

Equal token counts do not imply equal compute when model size, sequence length, sparsity, or hardware efficiency differs.

## Enter the laboratory

Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [A chapter-specific diagram](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Compute-Optimal Allocation — Buy a Larger Memory or More Experience?](../187-compute-optimal-allocation/README.md)
