# Excavation 164 — Weight Tying — Use One Word Geometry Twice

SwiGLU improves the block, but the model stores one large table for input embeddings and another large matrix for scoring the same vocabulary at output.

Perhaps we let both matrices learn independently because reading a token and predicting it are different jobs.

It survives until the measured run answers back. The model spends parameters learning two unrelated geometries for the same set of word identities, and rare tokens receive weak evidence in both places.

Now the missing requirement is concrete. Reuse the embedding table transposed as the output scoring matrix, while retaining any necessary output bias.

## Let one run decide

The tiger vector used to enter the model also becomes the direction a final hidden state must align with to predict tiger.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

The input table already contains a row pointing in the learned direction of tiger. At the output, predicting tiger means asking how strongly the final hidden state points along that same direction. Turning table rows into scoring columns changes only their orientation. E names the existing table, T marks that turn, and equality says W_out is the very same learned values—not a second copy trained to resemble them.

E stores one embedding row per token; transpose turns those rows into output-scoring columns without changing their values.

### Why these operations are forced

[Equality](../../MATHEMATICAL_MOVES.md#equals) imposes shared parameters rather than merely similar initialization. Transposition changes orientation so matrix shapes fit; it does not relearn or numerically transform the coordinates. Using addition would combine two matrices instead of making one geometry perform both roles.

Only now can we compress the procedure:

$$
W_{\text{out}}=E^{\mathsf T}
$$

## What this repair cannot do

Tying reduces parameters and imposes a useful constraint, but separate input and output roles may sometimes benefit from extra freedom.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Adam — Give Each Parameter Its Own Step Scale](../165-adam/README.md)
