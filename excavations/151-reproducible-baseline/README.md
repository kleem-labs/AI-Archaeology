# Excavation 151 — A Reproducible Baseline — Improve Something That Actually Exists

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Causality & Experimental Design](../../MATHEMATICS_ATLAS.md#causality) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Model systems and engine optimization

> **PART XII — REBUILDING THE ENGINE WITHOUT BREAKING THE SYSTEM**
>
> The research loop is bounded. We may now improve the model—but every faster path must preserve a reference path and earn its evidence.

The bounded loop can approve a candidate, but approval is meaningless if nobody can reconstruct the system it is supposed to improve.

Nothing in the Engine Cavern yet bears today's mathematical name. There is only the enginewright, the brass reference machine, and one plausible action: keep the final score and the model file; those should be enough to compare the next idea.

The rule survives the easy cases. The next case leaves a crack through the middle of it: a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied. More confidence cannot repair information that never entered the rule.

*The enginewright sketches the break before changing it:*

```text
observation
    │
    ▼
[keep the final score and the model…]
    │
    ╳  a rerun changes the data order,…
    │
    ▼
[freeze the model specification, data…]
```

Two trails now cross the brass reference machine. The pale trail bears the instruction “keep the final score and the model file; those should be enough to compare the next idea.” It disappears into the observed failure: a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied. The darker trail carries one additional capacity—to freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline. Nothing else in the scene moves, so the new branch cannot hide where its power came from.

The room becomes quiet around the failed reproducible baseline mark. Whatever comes next must distinguish these cases without destroying what the earlier method already did well.

So the brass reference machine is altered in exactly one way: freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline. Much later, people will call this territory **A Reproducible Baseline**. Here the name is only a memory of the failure it can survive.

The brass reference machine has become a palimpsest: observation below, failed shortcut above it, and repair written last. Read downward and reproducible baseline looks inevitable. Read upward—from the observation through the failure—and it becomes an invention a human mind could have made. The Engine Cavern lets reproducible baseline change speed, memory, or scale while the brass reference machine guards meaning. Equality here is not decoration; it is a promise that the optimized path performs the same mathematical responsibility by another physical route.

<!-- memory-film-v1:start -->
> **Memory realm 12 of 18 — [Engine Cavern](../../MEMORY_PALACE.md#realm-12)**
>
> **The question carried into this chamber:** What fails if we keep the final score and the model file; those should be enough to compare the next idea?

## When the chamber changes

Keep the formal name A Reproducible Baseline covered for another moment. The surviving image is enough to rebuild it.

First hold the failed picture still: The mirror follows the tempting path—keep the final score and the model file; those should be enough to compare the next idea. Then the evidence answers: a rerun changes the data order, random seed, tokenizer revision, and library behavior. Its score moves even though the proposed improvement was never applied.

Now let the chamber move: The enginewright changes one moving part. The mirror can now freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline.

The object that should remain after the terminology disappears is **the reproducible baseline mirror mounted on the brass reference machine**.

> **Memory seal — A Reproducible Baseline**
>
> A Reproducible Baseline keeps the missing power: freeze the model specification, data snapshot, seed, environment, training budget, and evaluation procedure as one named baseline.

Give the idea a bodily path: Touch the reproducible baseline mirror in imagination: tap five fingertips in order—question, object, failure, transformation, seal—without saying the formal name.
<!-- memory-film-v1:end -->

## Improve Something That Actually Exists

Run the same tiny tiger-language model twice from the recorded seed. Only after its loss curve and held-out score agree do we permit one component to change.

## The calculation hidden inside a reproducible baseline

The enginewright carries the reproducible baseline scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

The frozen run scores 2.4 and the candidate scores 2.1 on the same loss test. Looking at 2.1 alone cannot tell you whether anything improved. Remove the old 2.4 from the new 2.1: the remaining −0.3 is the candidate's change. We call the old measurement m_baseline, the new one m_candidate, and the remainder delta m only after doing that comparison.

m_baseline is the frozen model's measurement; m_candidate is measured by the same procedure; delta m names only the change between them.

### Why the melody needs these exact notes

[Subtraction](../../MATHEMATICAL_MOVES.md#subtraction) removes the common baseline and isolates the candidate's change. Addition would make two large scores look impressive even when they are identical. The order fixes the sign: positive means the candidate raised this metric.

Before the line is compressed, notice its recurring motions: **the chisel**—what is shared is removed so the remaining change can be seen. They are the handholds by which the reader can later climb back from notation to meaning.

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
