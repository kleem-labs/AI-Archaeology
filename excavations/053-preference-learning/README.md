# Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Instruction tuning turns continuation into cooperation on demonstrated tasks. Several answers can obey the same instruction while differing sharply in clarity, honesty, safety, and usefulness.

A new case arrives at the Hall of Voices, but the public archivist first reaches for the familiar listening table. Its promise is simple: write one perfect target response for every prompt and train only to imitate it.

At the edge of the listening table, the shortcut produces its consequence: many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer. That consequence, not a textbook, earns the next move.

*The public archivist sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ write one perfect target response for… ──▶ blurred: many answers can be valid. A single…
      │
      └── new lens ──▶ collect comparisons between candidate… ──▶ distinction survives
```

The public archivist covers the new mark and the old contradiction returns: many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer. The cover is lifted, restoring the ability to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy, and the two cases separate again. The motion is small enough to perform by hand; its consequence is the whole reason preference learning exists.

What must change for preference learning is finally visible. Not the whole world, not every old tool—only the decision that erased this one necessary distinction.

The old instrument is not discarded; it is given the one capacity the counterexample demanded: collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy. That threshold is where **Preference Learning** enters the story.

The room has gained no magical instrument. It has gained a memory of where the old instrument failed. In preference learning, that memory takes a precise form: whenever many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer, preserve enough structure to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy.

## The calculation hidden inside preference learning

The public archivist carries the preference learning scene to the listening table. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

For “How do I reset my router?”, answer A gives three safe ordered steps; answer B gives twenty vague paragraphs. A reviewer chooses A. Repeated comparisons teach concision and usefulness without declaring one exact sentence mandatory.

### Naming what is already on the table

The reward scores two responses to the same prompt. Their difference matters, not the absolute score. The logistic function turns that difference into a preference probability; larger positive differences favor the chosen answer.

### Why the melody needs these exact notes

[rA−rB](../../MATHEMATICAL_MOVES.md#subtraction) discards any common reward offset and keeps only which answer reviewers prefer and by how much.
[The inner negative](../../MATHEMATICAL_MOVES.md#negative-sign) makes larger preference gaps reduce the exponential term, so A's probability rises rather than falls.
[Exponentiation](../../MATHEMATICAL_MOVES.md#exponential) turns an unbounded reward gap into positive odds; adding one and [taking the reciprocal](../../MATHEMATICAL_MOVES.md#division) squeeze the result between zero and one without changing order.

Trace each operation by touch rather than by name: **the chisel**—what is shared is removed so the remaining change can be seen; **the turning wind**—an uphill quantity is made to point downhill, or surprise is made to count as cost; and **the rising flame**—a small score difference becomes positive relative evidence. Together they form the smallest mechanism that survives the counterexample.

The listening table already contains the complete preference learning mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
P(A\succ B)=\frac{1}{1+\exp(-(r_A-r_B))}
$$

## Where preference learning runs out

Human preferences conflict, annotators make mistakes, and optimizing a learned reward can exploit its blind spots.

Here the new path ends honestly. Preference Learning can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the listening table

Rebuild the preference learning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 054](../054-retrieval-augmented-generation/README.md)
