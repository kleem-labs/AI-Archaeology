# Excavation 163 — SwiGLU — Let One Learned Path Gate Another

<!-- book-prose-v2 -->

Pre-normalization lets gradients reach deep blocks, but the ordinary feed-forward network applies one fixed activation independently to one projection.

Before naming anything new, try to make the hidden layer merely wider and trust more coordinates to express every conditional interaction.

Its appeal is not ignorance but economy. SwiGLU should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Then a case arrives in which convenience and truth separate: width adds capacity but still asks one projection both to create content and decide when that content matters.

Notice what the counterexample has accomplished for swiglu. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: create one content projection and one gate projection; use the smooth gate to scale content feature by feature.

Humanity eventually gathered this problem and its repairs under the name **SwiGLU**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace swiglu with the old instruction to make the hidden layer merely wider and trust more coordinates to express every conditional interaction. The result is again that width adds capacity but still asks one projection both to create content and decide when that content matters. Put back only the requirement to create one content projection and one gate projection; use the smooth gate to scale content feature by feature. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when swiglu is introduced. The same evidence that defeated the attempt to make the hidden layer merely wider and trust more coordinates to express every conditional interaction is presented again. Only the ability to create one content projection and one gate projection; use the smooth gate to scale content feature by feature changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Let One Learned Path Gate Another

For a token describing a river bank, one path proposes financial features while the gate suppresses them; in a money context the same content path can be opened.

Run the swiglu scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## The calculation hidden inside swiglu

Before SwiGLU receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Picture one candidate feature saying 'river-bank meaning: 5.' A separate learned gate examines this occurrence of bank. Near the river it may open close to 1, allowing almost all 5 through; near money it may close near 0, silencing that feature. This demands multiplication: zero times content must become zero. W_v creates the candidate, W_g creates gate evidence, SiLU shapes that evidence, and the circled product pairs each gate with its own feature.

W_g creates gate evidence, SiLU bends it smoothly, W_v creates candidate content, and the circled product combines matching hidden coordinates.

### Why no cheaper operation does the same job

[Function application](../../MATHEMATICAL_MOVES.md#function-application) makes the gate depend on this token. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because a zero gate must silence its matching content and a partial gate must scale it. Addition would let closed content leak through. The elementwise mark means aligned coordinates interact rather than forming every pair.

Every symbol in SwiGLU can now be read back into an action already performed. The whole procedure fits in one line:

$$
\mathrm{SwiGLU}(x)=\mathrm{SiLU}(xW_g)\odot(xW_v)
$$

## Where swiglu runs out

Gating improves useful capacity but increases projection parameters and does not explain what every hidden feature means.

Why does that boundary remain? SwiGLU was built for one responsibility: create one content projection and one gate projection; use the smooth gate to scale content feature by feature. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take swiglu to the workbench

The argument for swiglu is still provisional until a runnable case can make it fail. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running swiglu, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the swiglu result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Weight Tying — Use One Word Geometry Twice](../164-weight-tying/README.md)
