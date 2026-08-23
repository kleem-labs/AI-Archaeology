# Excavation 080 — Vision Transformers

<!-- book-prose-v2 -->

A convolutional hierarchy builds local parts into objects. Some decisions depend on distant regions that a fixed local pathway connects only after many layers, inviting the image patches to communicate directly.

The first defensible move is to treat every pixel as a token.

There is a real principle behind this restraint: the complexity of vision transformers must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

Now keep that rule fixed and let the difficult case enter: the sequence becomes enormous and individual pixels carry little stable structure.

That distinction is the hinge on which vision transformers turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: group pixels into patches, embed them as tokens, add position, and apply attention.

We have earned the chapter's shorter name: **Vision Transformers**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that vision transformers is necessary rather than decorative. Delete its new responsibility and use the earlier plan to treat every pixel as a token. Immediately, the sequence becomes enormous and individual pixels carry little stable structure. Reintroduce the single job to group pixels into patches, embed them as tokens, add position, and apply attention. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can group pixels into patches, embed them as tokens, add position, and apply attention. Because the old plan to treat every pixel as a token is the only displaced piece, the reader can locate exactly where vision transformers changes the outcome.

## Understanding vision transformers

A 224×224 image with 16×16 patches becomes 196 tokens instead of 50,176 pixel tokens.

The name vision transformers is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## Where vision transformers runs out

Patch size trades detail for cost and needs substantial data.

The weakness is not an accidental footnote. Every operation in vision transformers serves the narrower purpose to group pixels into patches, embed them as tokens, add position, and apply attention; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take vision transformers to the workbench

Understanding vision transformers now means predicting its intermediate results before asking software for an answer. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running vision transformers, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the vision transformers result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 081](../081-autoencoders/README.md)
