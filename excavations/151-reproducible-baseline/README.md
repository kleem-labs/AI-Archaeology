# Excavation 151 — A Reproducible Baseline — Improve Something That Actually Exists

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Model systems and engine optimization

> **PART XII — REBUILDING THE ENGINE WITHOUT BREAKING THE SYSTEM**
>
> The research loop is bounded. We may now improve the model—but every faster path must preserve a reference path and earn its evidence.

The bounded loop can approve a candidate, but approval is meaningless if nobody can reconstruct the system it is supposed to improve.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to keep the final score and the model file; those should be enough to compare the next idea.

Nothing about this first move is careless. To keep the final score and the model file; those should be enough to compare the next idea is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied.

The important discovery is not merely that trying to keep the final score and the model file; those should be enough to compare the next idea failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **A Reproducible Baseline**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Improve Something That Actually Exists

Run the same tiny tiger-language model twice from the recorded seed. Only after its loss curve and held-out score agree do we permit one component to change.

## The calculation hidden inside a reproducible baseline

The enginewright carries the reproducible baseline scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The frozen run scores 2.4 and the candidate scores 2.1 on the same loss test. Looking at 2.1 alone cannot tell you whether anything improved. Remove the old 2.4 from the new 2.1: the remaining −0.3 is the candidate's change. We call the old measurement m_baseline, the new one m_candidate, and the remainder delta m only after doing that comparison.

m_baseline is the frozen model's measurement; m_candidate is measured by the same procedure; delta m names only the change between them.

### Why the melody needs these exact notes

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the common baseline and isolates the candidate's change. Addition would make two large scores look impressive even when they are identical. The order fixes the sign: positive means the candidate raised this metric.

The calculation reuses familiar motions: **the chisel**—what is shared is removed so the remaining change can be seen. Together they keep the path from the concrete case to notation intact.

The enginewright reads the journey of reproducible baseline once more across the brass reference machine, then lets the words contract without losing their order:

$$
\Delta m=m_{\text{candidate}}-m_{\text{baseline}}
$$

## Where a reproducible baseline runs out

Reproducibility makes differences attributable; it does not tell us which component is worth changing.

The brass reference machine answers today's question and falls silent at the next. That silence is precise: Reproducible Baseline was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the brass reference machine

Rebuild the reproducible baseline scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Profiling — Measure Where the Time Went](../152-profiling/README.md)
