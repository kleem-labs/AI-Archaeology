# Excavation 115 — Tree Search

Model-based planning can simulate possible action sequences. Their number grows exponentially with depth, making exhaustive imagination impossible long before the world model runs out of detail.

We first try to expand every branch equally.

But most computation is wasted on obviously poor branches.

We need to balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward.

## Let the case decide

A game search revisits a move that won often while still testing a less explored alternative.

## The arithmetic we have earned

A cave explorer can investigate the river tunnel or the ridge tunnel. The river tunnel has produced good finds in eight visits; the ridge has been tried only once. Choosing only the better average may ignore an undiscovered ridge chamber, while choosing only the least visited branch wastes known evidence. The search score adds an uncertainty bonus that is large for neglected branches and shrinks as visits supply evidence.

- The average reward records how well one branch has performed.
- Visit count shrinks the exploration bonus as evidence accumulates.
- Total visits increase pressure to reconsider neglected branches.
- The constant controls how much uncertainty competes with known reward.

### Why these operations are forced

- [The bar over R](../../MATHEMATICAL_MOVES.md#symbol-decorations) marks the mean return, keeping what a branch has already demonstrated; see [mean](../../MATHEMATICAL_MOVES.md#mean).
- [log N](../../MATHEMATICAL_MOVES.md#logarithm) lets exploration pressure grow slowly as the parent receives more visits instead of growing in direct proportion forever.
- [Dividing by nₐ](../../MATHEMATICAL_MOVES.md#division) makes an often-tested action less uncertain; [the square root](../../MATHEMATICAL_MOVES.md#square-root) tempers how sharply that exploration bonus changes.
- [c scales curiosity](../../MATHEMATICAL_MOVES.md#multiplication) and [addition](../../MATHEMATICAL_MOVES.md#addition) places that exploration bonus beside observed reward. Multiplying reward and curiosity would make either zero erase the other.

Only now can we compress the procedure:

$$
\mathrm{score}(a)=\overline R_a+c\sqrt{\frac{\log N}{n_a}}
$$

## The boundary of the discovery

Search quality depends on simulations and evaluation estimates.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 116](../116-reasoning-and-verification/README.md)
