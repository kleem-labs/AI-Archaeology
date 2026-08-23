# Excavation 155 — Rotary Position Embeddings — Let Distance Enter the Match

<!-- book-prose-v2 -->

Packed training supplies dense sequences, but the learned absolute position cards from our first GPT bind each slot to a private identity rather than making relative displacement part of the query-key match.

The previous discovery seems almost sufficient: we could learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples.

The shortcut appears to retain everything rotary position embeddings needs. The next observation must test that belief, not merely assert that a textbook prefers another method.

Then a case arrives in which convenience and truth separate: moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged.

The counterexample teaches rotary position embeddings. It reveals which sameness was false, which difference matters, and therefore what the replacement has to make visible.

Only one extra responsibility has been earned: rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference.

Now—and not earlier—we may introduce **Rotary Position Embeddings**. The words label the problem-and-repair pair whose necessity the reader can already test.

The invention can now defend itself. Without it, our best available move is to learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples, and the case answers that moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged. With the narrow repair—to rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference—the method can express the distinction reality demanded. That before-and-after comparison is the proof of need.

The logic would be weaker if the repaired method were tested on an easier scene. It is not. Rotary Position Embeddings returns to the same counterexample, replaces the attempt to learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples with the responsibility to rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference, and must succeed where the shortcut failed.

## Let Distance Enter the Match

Rotate the two coordinates of tiger by angle mθ and river by nθ. Their match depends on (m−n)θ, so shifting both tokens together preserves their separation signal.

A formula for rotary position embeddings is not yet needed. The experiment is already mathematical: we controlled what remained fixed, identified what changed, and demanded an observable consequence from that change.

## The calculation hidden inside rotary position embeddings

Before Rotary Position Embeddings receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Imagine the pair of coordinates as a clock hand beginning at [1,0]. At position one, a quarter-turn sends it to [0,1]; at position two, another quarter-turn sends it to [−1,0]. The hand's length never changes—only its angle does. Multiplying position p by the chosen turn theta tells us the total angle; the four cosine-and-sine entries record how any starting pair must contribute to its two rotated coordinates.

p is token position, theta is one rotation frequency, and R rotates one coordinate pair without changing its length.

### Why no cheaper operation does the same job

[Function application](../../MATHEMATICAL_MOVES.md#function-application) applies the same rotation rule at each position. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) mixes the two coordinates according to cosine and sine; [addition](../../MATHEMATICAL_MOVES.md#addition) combines their signed contributions. Squaring or adding p would change magnitude instead of encoding position as an angle whose differences survive a shared shift.

Every symbol in Rotary Position Embeddings can now be read back into an action already performed. The whole procedure fits in one line:

$$
R(p\theta)=\begin{bmatrix}\cos(p\theta)&-\sin(p\theta)\\\sin(p\theta)&\cos(p\theta)\end{bmatrix}
$$

## Where rotary position embeddings runs out

RoPE supplies structured relative position, but distances far beyond training still produce unfamiliar phases.

The boundary can be predicted from the construction itself. Rotary Position Embeddings performs the repair to rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference; the additional problem names a job outside that construction. Recognizing that edge prevents one successful equation or procedure from pretending to be a complete intelligence.

## Take rotary position embeddings to the workbench

Move rotary position embeddings from imagination to evidence by making the shortcut fail under controlled inputs. Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running rotary position embeddings, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the rotary position embeddings result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Relative Position Bias — What Should Happen Beyond the Seen Window?](../156-relative-position-bias/README.md)
