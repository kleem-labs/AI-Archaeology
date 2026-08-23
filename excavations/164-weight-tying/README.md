# Excavation 164 — Weight Tying — Use One Word Geometry Twice

<!-- book-prose-v2 -->

SwiGLU improves the block, but the model stores one large table for input embeddings and another large matrix for scoring the same vocabulary at output.

The first defensible move is to let both matrices learn independently because reading a token and predicting it are different jobs.

There is a real principle behind this restraint: the complexity of weight tying must pay rent. Nothing new is earned until the old rule gives the same answer to situations reality requires us to distinguish.

The proposal breaks for a specific reason, not by authority: the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places.

That distinction is the hinge on which weight tying turns. The old method cannot be repaired by a more confident use of the same missing information; the decision must be represented differently.

What survives the counterexample is this requirement: reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias.

We have earned the chapter's shorter name: **Weight Tying**. Every time it appears, it should recall both the counterexample and the responsibility needed to survive it.

A reader can check that weight tying is necessary rather than decorative. Delete its new responsibility and use the earlier plan to let both matrices learn independently because reading a token and predicting it are different jobs. Immediately, the model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places. Reintroduce the single job to reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias. If that does not cure the counterexample, the chapter has not yet earned its method; if it does, every added piece has a reason to remain.

This is also an experiment in causality. The failed and repaired paths share their starting situation; they differ in whether the procedure can reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias. Because the old plan to let both matrices learn independently because reading a token and predicting it are different jobs is the only displaced piece, the reader can locate exactly where weight tying changes the outcome.

## Use One Word Geometry Twice

The tiger vector used to enter the model also becomes the direction a final hidden state must align with to predict tiger.

The name weight tying is still unimportant. What matters is that every object in the repaired procedure has a visible job and that removing any one of them recreates the witnessed failure.

## The calculation hidden inside weight tying

Do not read the coming Weight Tying line as an instruction dropped from above. Read it from left to right as a compressed record of the concrete decisions already made.

The input table already contains a row pointing in the learned direction of tiger. At the output, predicting tiger means asking how strongly the final hidden state points along that same direction. Turning table rows into scoring columns changes only their orientation. E names the existing table, T marks that turn, and equality says W_out is the very same learned values—not a second copy trained to resemble them.

E stores one embedding row per token; transpose turns those rows into output-scoring columns without changing their values.

### Why no cheaper operation does the same job

[Equality](../../MATHEMATICAL_MOVES.md#equals) imposes shared parameters rather than merely similar initialization. Transposition changes orientation so matrix shapes fit; it does not relearn or numerically transform the coordinates. Using addition would combine two matrices instead of making one geometry perform both roles.

Every symbol in Weight Tying can now be read back into an action already performed. The whole procedure fits in one line:

$$
W_{\text{out}}=E^{\mathsf T}
$$

## Where weight tying runs out

Tying reduces parameters and imposes a useful constraint, but separate input and output roles may sometimes benefit from extra freedom.

The weakness is not an accidental footnote. Every operation in weight tying serves the narrower purpose to reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias; none was designed to answer the new question. We have reached the honest edge of the invention.

## Take weight tying to the workbench

Understanding weight tying now means predicting its intermediate results before asking software for an answer. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running weight tying, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the weight tying result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Adam — Give Each Parameter Its Own Step Scale](../165-adam/README.md)
