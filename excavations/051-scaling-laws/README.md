# Excavation 051 — Scaling Laws — What Improves When We Add More?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Data quality asks what patterns the training process actually repeated. Once the lessons are trustworthy, the builders must decide whether the next unit of computation should buy more data, a larger model, or longer training.

Night gathers around the Hall of Voices. Under the light of the listening table, the public archivist refuses to invent prematurely and begins with the plain rule: make the model as large as possible and assume capability follows parameter count.

Then the quiet test arrives: a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns. What looked like simplicity is revealed as a missing distinction.

*The public archivist sketches the break before changing it:*

```text
             evidence
            /        \
   old lantern      hidden distinction
   make the model as large as possible… a huge model trained on too little…
            \        /
             \      /
              we need to run controlled experiments…
```

The public archivist turns the listening table toward the light. Through the old engraving, make the model as large as possible and assume capability follows parameter count, the evidence ends in the same contradiction: a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns. A second engraving adds only the power to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number. Superimposed, the two paths share every stroke until the precise place where the old one breaks.

The public archivist circles the place where the two scaling laws cases collapsed together. The repair must open that circle and preserve the difference inside it.

Only the missing distinction is restored: we need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number. The public archivist writes **Scaling Laws** beside the new mark, and the unfamiliar name feels strangely familiar because every part of it has already been needed.

The public archivist places a finger over the new distinction. At once the two cases collapse and a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns. Lifting the finger restores only this capacity: run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number. That tiny reversible motion is the chapter's proof of necessity.

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
