# Excavation 053 — Preference Learning — When Several Answers Are Correct but Not Equally Helpful

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Information Theory](../../MATHEMATICS_ATLAS.md#information)
>
> **Applied territory:** Language models and useful answers

Instruction tuning turns continuation into cooperation on demonstrated tasks. Several answers can obey the same instruction while differing sharply in clarity, honesty, safety, and usefulness.

The previous discovery reaches the Hall of Voices carrying one unfinished problem. Beside the listening table, the public archivist first tries to write one perfect target response for every prompt and train only to imitate it.

There is good reason to begin this way. If we write one perfect target response for every prompt and train only to imitate it, the old method continues doing useful work and nothing new is invented merely because a modern name exists for it. In familiar situations, that restraint makes the system simpler to inspect and easier to trust. The proposal deserves to survive unless a concrete observation proves that it merges two situations whose consequences are different.

That rule is not foolish; it works until the missing distinction matters. Here is the precise contradiction: many answers can be valid. A single target penalizes harmless alternatives and cannot express that answer A is preferred to B without being the only possible answer.

This failure cannot be repaired by performing the instruction to write one perfect target response for every prompt and train only to imitate it more confidently. Confidence only strengthens the path that produced the contradiction. Nor is it enough to attach a special exception to this one example; the same missing distinction can return in countless forms. What is needed is a reusable responsibility that explains both why the simple case worked and why this case did not. The repaired method must face the same evidence on the listening table; otherwise a changed answer could be mistaken for an explanation.

The evidence has earned one extension and no more. We need to collect comparisons between candidate responses, learn which properties predict preference, and use that signal to improve the response policy. The point of the extension is not sophistication. It is to make room for information that was present in the world but absent from the old decision.

Once this responsibility becomes part of the method, we have built what is called **Preference Learning**. The name is simply a handle for the distinction already reconstructed.

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
