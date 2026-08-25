# Excavation 115 — Tree Search

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Continual learning, reasoning, and research

Model-based planning can simulate possible action sequences. Their number grows exponentially with depth, making exhaustive imagination impossible long before the world model runs out of detail.

Inside the Hall of Possible Worlds, the old method is given an honest chance. The keeper of unfinished questions places the evidence on the table of mirrored maps and tries to expand every branch equally.

Nothing about this first move is careless. To expand every branch equally is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: most computation is wasted on obviously poor branches.

The important discovery is not merely that trying to expand every branch equally failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the table of mirrored maps, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Tree Search**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## Understanding tree search

A game search revisits a move that won often while still testing a less explored alternative.

## The calculation hidden inside tree search

The keeper of unfinished questions carries the tree search scene to the table of mirrored maps. Every quantity already has a visible owner and every operation already has a job; the symbols will only keep those moves precise when the calculation is repeated.

A cave explorer can investigate the river tunnel or the ridge tunnel. The river tunnel has produced good finds in eight visits; the ridge has been tried only once. Choosing only the better average may ignore an undiscovered ridge chamber, while choosing only the least visited branch wastes known evidence. The search score adds an uncertainty bonus that is large for neglected branches and shrinks as visits supply evidence.

The average reward records how well one branch has performed.
Visit count shrinks the exploration bonus as evidence accumulates.
Total visits increase pressure to reconsider neglected branches.
The constant controls how much uncertainty competes with known reward.

### Why the melody needs these exact notes

[The bar over R](../../MATHEMATICAL_MOVES.md#symbol-decorations) marks the mean return, keeping what a branch has already demonstrated; see [mean](../../MATHEMATICAL_MOVES.md#mean).
[log N](../../MATHEMATICAL_MOVES.md#logarithm) lets exploration pressure grow slowly as the parent receives more visits instead of growing in direct proportion forever.
[Dividing by nₐ](../../MATHEMATICAL_MOVES.md#division) makes an often-tested action less uncertain; [the square root](../../MATHEMATICAL_MOVES.md#square-root) tempers how sharply that exploration bonus changes.
[c scales curiosity](../../MATHEMATICAL_MOVES.md#multiplication) and [addition](../../MATHEMATICAL_MOVES.md#addition) places that exploration bonus beside observed reward. Multiplying reward and curiosity would make either zero erase the other.

The symbols are about to change costume, but their work has appeared before: **the spiral stair**—compounded chances become steps that can be accumulated; **the fair cup**—a total is judged per person, per step, or per unit rather than admired for being large; and **the road home**—a squared construction returns to the scale of the world that created it. This is how distant excavations begin to sound like variations of one melody.

The keeper of unfinished questions reads the journey of tree search once more across the table of mirrored maps, then lets the words contract without losing their order:

$$
\mathrm{score}(a)=\overline R_a+c\sqrt{\frac{\log N}{n_a}}
$$

## Where tree search runs out

Search quality depends on simulations and evaluation estimates.

The table of mirrored maps answers today's question and falls silent at the next. That silence is precise: Tree Search was built to repair one failure, not to pretend every later boundary is already solved.

## Return to the table of mirrored maps

Rebuild the tree search scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 116](../116-reasoning-and-verification/README.md)
