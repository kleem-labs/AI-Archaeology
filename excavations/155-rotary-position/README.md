# Excavation 155 — Rotary Position Embeddings — Let Distance Enter the Match

Packed training supplies dense sequences, but the learned absolute position cards from our first GPT bind each slot to a private identity rather than making relative displacement part of the query-key match.

Perhaps we learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples.

It survives until the measured run answers back. Moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged.

Now the missing requirement is concrete. Rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference.

## Let one run decide

Rotate the two coordinates of tiger by angle mθ and river by nθ. Their match depends on (m−n)θ, so shifting both tokens together preserves their separation signal.

Nothing in that case was introduced because a modern model happens to use it. The measured failure created the job; the repair is only the shortest design that performs it.

## The arithmetic we have earned

Imagine the pair of coordinates as a clock hand beginning at [1,0]. At position one, a quarter-turn sends it to [0,1]; at position two, another quarter-turn sends it to [−1,0]. The hand's length never changes—only its angle does. Multiplying position p by the chosen turn theta tells us the total angle; the four cosine-and-sine entries record how any starting pair must contribute to its two rotated coordinates.

p is token position, theta is one rotation frequency, and R rotates one coordinate pair without changing its length.

### Why these operations are forced

[Function application](../../MATHEMATICAL_MOVES.md#function-application) applies the same rotation rule at each position. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) mixes the two coordinates according to cosine and sine; [addition](../../MATHEMATICAL_MOVES.md#addition) combines their signed contributions. Squaring or adding p would change magnitude instead of encoding position as an angle whose differences survive a shared shift.

Only now can we compress the procedure:

$$
R(p\theta)=\begin{bmatrix}\cos(p\theta)&-\sin(p\theta)\\\sin(p\theta)&\cos(p\theta)\end{bmatrix}
$$

## What this repair cannot do

RoPE supplies structured relative position, but distances far beyond training still produce unfamiliar phases.

That boundary is the opening condition of the next excavation.

## Enter the laboratory

Reproduce the waste first, then apply the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code.

## Continue the dig

- [Mistakes worth preserving](mistakes.md)
- [Diagram of the measured failure and repair](diagram.md)
- [Invention exercises](exercises.md)
- [Primary research trail](references.md)
- [Visual brief](images/README.md)

[Next: Relative Position Bias — What Should Happen Beyond the Seen Window?](../156-relative-position-bias/README.md)
