# Excavation 155 — Rotary Position Embeddings — Let Distance Enter the Match

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Linear Algebra & Geometry](../../MATHEMATICS_ATLAS.md#linear-algebra) · [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Numerical Analysis & Scientific Computing](../../MATHEMATICS_ATLAS.md#numerical)
>
> **Applied territory:** Model systems and engine optimization

Packed training supplies dense sequences, but the learned absolute position cards from our first GPT bind each slot to a private identity rather than making relative displacement part of the query-key match.

Inside the Engine Cavern, the old method is given an honest chance. The enginewright places the evidence on the brass reference machine and tries to learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples.

Nothing about this first move is careless. To learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: moving the same phrase from positions 10–12 to 110–112 changes every position vector although the internal distances are unchanged.

The important discovery is not merely that trying to learn an unrelated vector for every absolute position and hope the model infers all relative distances from examples failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the brass reference machine, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to rotate pairs of query and key coordinates by a position-dependent angle so their dot product naturally depends on the angle difference. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Rotary Position Embeddings**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Let Distance Enter the Match

Rotate the two coordinates of tiger by angle mθ and river by nθ. Their match depends on (m−n)θ, so shifting both tokens together preserves their separation signal.

## The calculation hidden inside rotary position embeddings

The enginewright carries the rotary position embeddings scene to the brass reference machine. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

Imagine the pair of coordinates as a clock hand beginning at [1,0]. At position one, a quarter-turn sends it to [0,1]; at position two, another quarter-turn sends it to [−1,0]. The hand's length never changes—only its angle does. Multiplying position p by the chosen turn theta tells us the total angle; the four cosine-and-sine entries record how any starting pair must contribute to its two rotated coordinates.

p is token position, theta is one rotation frequency, and R rotates one coordinate pair without changing its length.

### Why the melody needs these exact notes

[Function application](../../MATHEMATICAL_MOVES.md#function-application) applies the same rotation rule at each position. [Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) mixes the two coordinates according to cosine and sine; [addition](../../MATHEMATICAL_MOVES.md#addition) combines their signed contributions. Squaring or adding p would change magnitude instead of encoding position as an angle whose differences survive a shared shift.

The symbols are about to change costume, but their work has appeared before: **the lock and key**—one influence matters through another, and either missing factor can close the path; and **the joining river**—separate contributions meet without losing where they came from. This is how distant excavations begin to sound like variations of one melody.

The brass reference machine already contains the complete rotary position embeddings mechanism. Mathematics gives that mechanism a form small enough to carry:

$$
R(p\theta)=\begin{bmatrix}\cos(p\theta)&-\sin(p\theta)\\\sin(p\theta)&\cos(p\theta)\end{bmatrix}
$$

## Where rotary position embeddings runs out

RoPE supplies structured relative position, but distances far beyond training still produce unfamiliar phases.

Here the new path ends honestly. Rotary Position Embeddings can do the job that summoned it; it cannot cross the next boundary without another observation, another failure, and another invention.

## Return to the brass reference machine

Rebuild the rotary position embeddings scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [Diagram of the measured failure and repair](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Relative Position Bias — What Should Happen Beyond the Seen Window?](../156-relative-position-bias/README.md)
