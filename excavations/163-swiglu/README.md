# Excavation 163 — SwiGLU — Let One Learned Path Gate Another

Pre-normalization lets gradients reach deep blocks, but the ordinary feed-forward network applies one fixed activation independently to one projection.

Perhaps we make the hidden layer merely wider and trust more coordinates to express every conditional interaction.

It survives until the measured run answers back. Width adds capacity but still asks one projection both to create content and decide when that content matters.

Now the missing requirement is concrete. Create one content projection and one gate projection; use the smooth gate to scale content feature by feature.

## Let one run decide

For a token describing a river bank, one path proposes financial features while the gate suppresses them; in a money context the same content path can be opened.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Picture one candidate feature saying 'river-bank meaning: 5.' A separate learned gate examines this occurrence of bank. Near the river it may open close to 1, allowing almost all 5 through; near money it may close near 0, silencing that feature. This demands multiplication: zero times content must become zero. W_v creates the candidate, W_g creates gate evidence, SiLU shapes that evidence, and the circled product pairs each gate with its own feature.

W_g creates gate evidence, SiLU bends it smoothly, W_v creates candidate content, and the circled product combines matching hidden coordinates.

### Why these operations are forced

[Function application](../../MATHEMATICAL_MOVES.md#function-application) makes the gate depend on this token. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because a zero gate must silence its matching content and a partial gate must scale it. Addition would let closed content leak through. The elementwise mark means aligned coordinates interact rather than forming every pair.

Only now can we compress the procedure:

$$
\mathrm{SwiGLU}(x)=\mathrm{SiLU}(xW_g)\odot(xW_v)
$$

## What this repair cannot do

Gating improves useful capacity but increases projection parameters and does not explain what every hidden feature means.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Weight Tying — Use One Word Geometry Twice](../164-weight-tying/README.md)
