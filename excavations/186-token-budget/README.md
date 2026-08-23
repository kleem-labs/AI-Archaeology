# Excavation 186 — The Token Budget — Convert a Training Plan into a Count of Lessons

<!-- book-prose-v2 -->

Seeded mixture sampling can produce an ordered stream. The run still says “train for a while,” so neither cost nor source exposure is bounded.

The obvious economy is to stop when the wall clock reaches an affordable date.

The proposal deserves a fair hearing. For the token budget, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

Its hidden assumption becomes visible as soon as we observe that faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence.

The failure changes the question behind the token budget. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute.

Only at this point does the inherited name **The Token Budget** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of the token budget by mentally removing the repair. We fall back to the proposal to stop when the wall clock reaches an affordable date; then faster hardware sees more tokens, interruptions see fewer, and two runs with the same calendar budget teach different amounts of evidence. Restore only the ability to define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to stop when the wall clock reaches an affordable date to requiring the system to define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to the token budget.

## Convert a Training Plan into a Count of Lessons

A tiny run uses 2,000 updates with 32 sequences of 128 real tokens each. Every update carries 4,096 lessons, so the complete plan exposes 8,192,000 tokens.

Put the old procedure beside the token budget. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside the token budget

Do not read the coming The Token Budget line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

T is the planned number of optimizer updates, B_tokens counts real loss-bearing tokens in one global batch, and N_tokens is the complete exposure budget.

### Why no cheaper operation does the same job

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) appears because every one of T updates consumes B_tokens lessons. Addition would count only one update plus one batch. Padding is excluded because it occupies hardware but contributes no language target.

Every symbol in The Token Budget can now be read back into an action already performed. The whole procedure fits in one line:

$$
N_{\text{tokens}}=T B_{\text{tokens}}
$$

## Where the token budget runs out

Equal token counts do not imply equal compute when model size, sequence length, sparsity, or hardware efficiency differs.

The limit follows from the job assigned to the token budget. Its repair knows how to define the run by optimization steps and real loss-bearing tokens per global batch, then derive the total token budget before reserving compute. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take the token budget to the workbench

A claim about the token budget now exists on the page; the laboratory must be able to contradict it. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running the token budget, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the the token budget result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Compute-Optimal Allocation — Buy a Larger Memory or More Experience?](../187-compute-optimal-allocation/README.md)
