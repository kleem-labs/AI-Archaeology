# Excavation 151 — A Reproducible Baseline — Improve Something That Actually Exists

<!-- book-prose-v2 -->

> **PART XII — REBUILDING THE ENGINE WITHOUT BREAKING THE SYSTEM**
>
> The research loop is bounded. We may now improve the model—but every faster path must preserve a reference path and earn its evidence.

The bounded loop can approve a candidate, but approval is meaningless if nobody can reconstruct the system it is supposed to improve.

Before naming anything new, try to keep the final score and the model file; those should be enough to compare the next idea.

Its appeal is not ignorance but economy. A Reproducible Baseline should not be added until an observation exposes the exact thing the older procedure cannot preserve.

One counterexample is enough to expose the missing job: a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied.

Notice what the counterexample has accomplished for a reproducible baseline. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline.

Humanity eventually gathered this problem and its repairs under the name **A Reproducible Baseline**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace a reproducible baseline with the old instruction to keep the final score and the model file; those should be enough to compare the next idea. The result is again that a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied. Put back only the requirement to freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when a reproducible baseline is introduced. The same evidence that defeated the attempt to keep the final score and the model file; those should be enough to compare the next idea is presented again. Only the ability to freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Improve Something That Actually Exists

Run the same tiny tiger-language model twice from the recorded seed. Only after its loss curve and held-out score agree do we permit one component to change.

Run the a reproducible baseline scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## The calculation hidden inside a reproducible baseline

Before A Reproducible Baseline receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

The frozen run scores 2.4 and the candidate scores 2.1 on the same loss test. Looking at 2.1 alone cannot tell you whether anything improved. Remove the old 2.4 from the new 2.1: the remaining −0.3 is the candidate's change. We call the old measurement m_baseline, the new one m_candidate, and the remainder delta m only after doing that comparison.

m_baseline is the frozen model's measurement; m_candidate is measured by the same procedure; delta m names only the change between them.

### Why no cheaper operation does the same job

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the common baseline and isolates the candidate's change. Addition would make two large scores look impressive even when they are identical. The order fixes the sign: positive means the candidate raised this metric.

Every symbol in A Reproducible Baseline can now be read back into an action already performed. The whole procedure fits in one line:

$$
\Delta m=m_{\text{candidate}}-m_{\text{baseline}}
$$

## Where a reproducible baseline runs out

Reproducibility makes differences attributable; it does not tell us which component is worth changing.

Why does that boundary remain? A Reproducible Baseline was built for one responsibility: freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take a reproducible baseline to the workbench

The argument for a reproducible baseline is still provisional until a runnable case can make it fail. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running a reproducible baseline, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the a reproducible baseline result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Profiling — Measure Where the Time Went](../152-profiling/README.md)
