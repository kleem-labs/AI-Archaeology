# Excavation 051 — Scaling Laws — What Improves When We Add More?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Probability & Statistics](../../MATHEMATICS_ATLAS.md#probability) · [Optimization](../../MATHEMATICS_ATLAS.md#optimization) · [Mathematical Foundations & Measurement](../../MATHEMATICS_ATLAS.md#foundations)
>
> **Applied territory:** Language models and useful answers

Data quality asks what patterns the training process actually repeated. Once the lessons are trustworthy, the builders must decide whether the next unit of computation should buy more data, a larger model, or longer training.

Inside the Hall of Voices, the old method is given an honest chance. The public archivist places the evidence on the listening table and tries to make the model as large as possible and assume capability follows parameter count.

Nothing about this first move is careless. To make the model as large as possible and assume capability follows parameter count is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns.

The important discovery is not merely that trying to make the model as large as possible and assume capability follows parameter count failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the listening table, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Scaling Laws**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## The calculation hidden inside scaling laws

The public archivist carries the scaling laws scene to the listening table. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Models with 1, 2, and 4 million effective units achieve losses 4.0, 3.2, and 2.8. Improvement continues but shrinks. The curve helps estimate whether doubling again is worth the cost; it does not promise a new capability.

### Naming what is already on the table

N is the resource being scaled. The negative exponent makes loss fall as N grows. Alpha controls how quickly returns diminish. A scales the improvable part; B is the floor this simple trend cannot beat.

### Why the melody needs these exact notes

[The negative power](../../MATHEMATICAL_MOVES.md#powers) makes the improvable part fall as resource N grows, with α controlling how quickly returns diminish.
[A scales that falling term](../../MATHEMATICAL_MOVES.md#multiplication) to the observed problem; adding A would create a floor instead of changing improvement size.
[Adding B](../../MATHEMATICAL_MOVES.md#addition) represents a remaining floor this simple scaling route does not remove. Multiplying by B would force the whole loss toward zero instead of allowing an irreducible remainder.

The symbols are about to change costume, but their work has appeared before: **the echoing chamber**—large departures return with greater force while opposite signs stop cancelling; **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. This is how distant excavations begin to sound like variations of one melody.

The story of scaling laws has become longer than its calculation, which is exactly when notation becomes merciful. Its whole path is:

$$
L(N)=A N^{-\alpha}+B
$$

## Where scaling laws runs out

A fitted trend applies within observed regimes. Data quality, architecture changes, and new bottlenecks can bend it.

One unsolved mark remains on the listening table. None of the responsibilities inside Scaling Laws can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the listening table

Rebuild the scaling laws scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 052](../052-instruction-tuning/README.md)
