# Excavation 151 — A Reproducible Baseline — Improve Something That Actually Exists

> **PART XII — REBUILDING THE ENGINE WITHOUT BREAKING THE SYSTEM**
>
> The research loop is bounded. We may now improve the model—but every faster path must preserve a reference path and earn its evidence.

The bounded loop can approve a candidate, but approval is meaningless if nobody can reconstruct the system it is supposed to improve.

Perhaps we keep the final score and the model file; those should be enough to compare the next idea.

It survives until the measured run answers back. A rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied.

Now the missing requirement is concrete. Freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline.

## Let one run decide

Run the same tiny tiger-language model twice from the recorded seed. Only after its loss curve and held-out score agree do we permit one component to change.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

The frozen run scores 2.4 and the candidate scores 2.1 on the same loss test. Looking at 2.1 alone cannot tell you whether anything improved. Remove the old 2.4 from the new 2.1: the remaining −0.3 is the candidate's change. We call the old measurement m_baseline, the new one m_candidate, and the remainder delta m only after doing that comparison.

m_baseline is the frozen model's measurement; m_candidate is measured by the same procedure; delta m names only the change between them.

### Why these operations are forced

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the common baseline and isolates the candidate's change. Addition would make two large scores look impressive even when they are identical. The order fixes the sign: positive means the candidate raised this metric.

Only now can we compress the procedure:

$$
\Delta m=m_{\text{candidate}}-m_{\text{baseline}}
$$

## What this repair cannot do

Reproducibility makes differences attributable; it does not tell us which component is worth changing.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Profiling — Measure Where the Time Went](../152-profiling/README.md)
