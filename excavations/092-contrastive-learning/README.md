# Excavation 092 — Contrastive Learning

<!-- book-prose-v2 -->

Multimodal alignment places an image near its matching caption. Pulling pairs together alone permits every pair to collapse to the same point; meaning appears only when the correct match wins against plausible alternatives.

The first defensible move is to pull every observed pair together without negatives.

There is a real principle behind this restraint: the complexity of contrastive learning must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The proposal breaks for a specific reason, not by authority: the trouble appears immediately: all representations can collapse to one point.

That distinction is the hinge on which contrastive learning turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: compare each true pair against mismatched alternatives in the same batch.

We have earned the chapter's shorter name: **Contrastive Learning**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that contrastive learning is necessary rather than decorative. Delete its new responsibility and use the earlier plan to pull every observed pair together without negatives. Immediately, the trouble appears immediately: all representations can collapse to one point. Reintroduce the single job to compare each true pair against mismatched alternatives in the same batch. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can compare each true pair against mismatched alternatives in the same batch. Because the old plan to pull every observed pair together without negatives is the only displaced piece, the reader can locate exactly where contrastive learning changes the outcome.

## Understanding contrastive learning

One tiger image chooses its caption among 31 wrong captions; success requires relative alignment.

The name contrastive learning is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## The calculation hidden inside contrastive learning

Do not read the coming Contrastive Learning line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

Place four wildlife photographs beside four captions. The tiger photograph should prefer “a striped predator” over “a river,” “a truck,” and “a sleeping dog.” Pulling only the correct pair together is insufficient: every photograph and caption could collapse to the same location. Making the tiger compete against all candidate captions forces its correct caption to be closer *relative to the alternatives*.

zi and ti are the matched image and text vectors.
Their dot product is the named alignment score.
Temperature T controls how sharply alternatives compete.
The denominator includes every candidate caption, preventing all examples from collapsing to one point.
The negative log penalizes the true pair when mismatches receive comparable scores.

### Why no cheaper operation does the same job

[Each dot product](../../MATHEMATICAL_MOVES.md#dot-product) measures aligned agreement between one image representation and one candidate text representation.
[Dividing by temperature](../../MATHEMATICAL_MOVES.md#division) controls how strongly score gaps matter before [exponentiation](../../MATHEMATICAL_MOVES.md#exponential) converts them into positive relative weights.
[The denominator sum](../../MATHEMATICAL_MOVES.md#summation) makes the correct pair compete against all candidates, preventing every representation from winning by collapsing to one point.
[Negative log](../../MATHEMATICAL_MOVES.md#logarithm) turns the correct pair's probability share into additive cost and punishes confident preference for the wrong match.

Every symbol in Contrastive Learning can now be read back into an action already performed. The whole procedure fits in one line:

$$
L_i=-\log\frac{\exp(z_i\cdot t_i/T)}{\sum_j\exp(z_i\cdot t_j/T)}
$$

## Where contrastive learning runs out

False negatives may actually describe the same concept.

The weakness is not an accidental footnote. Every operation in contrastive learning serves the narrower purpose to compare each true pair against mismatched alternatives in the same batch; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take contrastive learning to the workbench

Understanding contrastive learning now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running contrastive learning, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the contrastive learning result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 093](../093-speech-audio/README.md)
