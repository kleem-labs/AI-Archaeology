# Excavation 174 — Speculative Decoding — Let a Small Model Propose, Never Decide

Tensor parallelism makes one target-model step possible, but autoregressive dependence still serializes token generation.

Perhaps we let a cheap draft model emit several tokens and return them directly.

It survives until the measured run answers back. Speed improves by silently replacing the trusted target distribution with a weaker model's distribution.

Now the missing requirement is concrete. Let the draft propose a short continuation, score all proposed positions with the target in parallel, and accept only according to a correction rule that preserves target sampling.

## Let one run decide

The draft proposes “the tiger sleeps.” One target call verifies all three positions; an unsupported token is rejected and sampling resumes from the corrected target distribution.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

If the draft assigns tiger probability 0.8 but the target assigns 0.4, only half of those proposals have target support: 0.4/0.8=0.5. If the draft assigns 0.4 and the target 0.8, the ratio is 2, but acceptance cannot be 200 percent, so it stops at 1. The function a(x) names this capped acceptance chance for proposed token x.

q(x) is draft probability, p(x) is target probability, and a(x) is the probability of accepting the draft token under the correction step.

### Why these operations are forced

[Division](../../MATHEMATICAL_MOVES.md#division) compares target support per unit of draft support. [Minimum](../../MATHEMATICAL_MOVES.md#minimum) caps acceptance at one because probabilities cannot exceed certainty. Simply taking max or always accepting would change the target distribution; the ratio corrects proposals that the draft overproduces.

Only now can we compress the procedure:

$$
a(x)=\min\left(1,\frac{p(x)}{q(x)}\right)
$$

## What this repair cannot do

Speed depends on draft agreement and hardware utilization; poor proposals add work instead of removing it.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: A Modern Tiny Language Model — Assemble the Measured Engine](../175-modern-tiny-llm/README.md)
