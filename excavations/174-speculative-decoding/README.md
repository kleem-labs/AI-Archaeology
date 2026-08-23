# Excavation 174 — Speculative Decoding — Let a Small Model Propose, Never Decide

<!-- book-prose-v2 -->

Tensor parallelism makes one target-model step possible, but autoregressive dependence still serializes token generation.

The obvious economy is to let a cheap draft model emit several tokens and return them directly.

The proposal deserves a fair hearing. For speculative decoding, it uses information we already possess, and if it survives there is no reason to burden the reader or the machine with another object.

The decisive test is this: speed improves by silently replacing the trusted target distribution with a weaker model's distribution.

The failure changes the question behind speculative decoding. We are no longer asking whether the first rule is convenient; we are asking what information it erased before reaching its answer.

The required repair is now narrow enough to state: let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling.

Only at this point does the inherited name **Speculative Decoding** help. It is a short handle for the failure, requirement, and repair we can now distinguish—not the discovery itself.

Test the necessity of speculative decoding by mentally removing the repair. We fall back to the proposal to let a cheap draft model emit several tokens and return them directly; then speed improves by silently replacing the trusted target distribution with a weaker model's distribution. Restore only the ability to let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling, and the counterexample finally has somewhere to go. That reversible test—not familiarity with the name—is the derivation.

Throughout that comparison, the surrounding evidence and desired outcome remain fixed. Only the rule changes—from trying to let a cheap draft model emit several tokens and return them directly to requiring the system to let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. This control matters: if we changed the data and the rule together, an apparent success could not be attributed to speculative decoding.

## Let a Small Model Propose, Never Decide

The draft proposes “the tiger sleeps.” One target call verifies all three positions; an unsupported token is rejected and sampling resumes from the corrected target distribution.

Put the old procedure beside speculative decoding. The first sees only its original inputs; the repaired one also carries the distinction exposed by the counterexample. Because everything else is held still, any difference in the conclusion belongs to that repaired information.

## The calculation hidden inside speculative decoding

Do not read the coming Speculative Decoding line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

If the draft assigns tiger probability 0.8 but the target assigns 0.4, only half of those proposals have target support: 0.4/0.8=0.5. If the draft assigns 0.4 and the target 0.8, the ratio is 2, but acceptance cannot be 200 percent, so it stops at 1. The function a(x) names this capped acceptance chance for proposed token x.

q(x) is draft probability, p(x) is target probability, and a(x) is the probability of accepting the draft token under the correction step.

### Why no cheaper operation does the same job

[Division](../../MATHEMATICAL_MOVES.md#division) compares target support per unit of draft support. [Minimum](../../MATHEMATICAL_MOVES.md#minimum) caps acceptance at one because probabilities cannot exceed certainty. Simply taking max or always accepting would change the target distribution; the ratio corrects proposals that the draft overproduces.

Every symbol in Speculative Decoding can now be read back into an action already performed. The whole procedure fits in one line:

$$
a(x)=\min\left(1,\frac{p(x)}{q(x)}\right)
$$

## Where speculative decoding runs out

Speed depends on draft agreement and hardware utilization; poor proposals add work instead of removing it.

The limit follows from the job assigned to speculative decoding. Its repair knows how to let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling. No step in that procedure can settle the additional question above, so the next excavation must supply information this one never receives.

## Take speculative decoding to the workbench

A claim about speculative decoding now exists on the page; the laboratory must be able to contradict it. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running speculative decoding, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the speculative decoding result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: A Modern Tiny Language Model — Assemble the Measured Engine](../175-modern-tiny-llm/README.md)
