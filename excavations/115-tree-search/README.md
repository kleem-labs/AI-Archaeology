# Excavation 115 — Tree Search

<!-- book-prose-v2 -->

Model-based planning can simulate possible action sequences. Their number grows exponentially with depth, making exhaustive imagination impossible long before the world model runs out of detail.

Before naming anything new, try to expand every branch equally.

Its appeal is not ignorance but economy. Tree Search should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Then a case arrives in which convenience and truth separate: most computation is wasted on obviously poor branches.

Notice what the counterexample has accomplished for tree search. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: we need to balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward.

Humanity eventually gathered this problem and its repairs under the name **Tree Search**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace tree search with the old instruction to expand every branch equally. The result is again that most computation is wasted on obviously poor branches. Put back only the requirement to we need to balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when tree search is introduced. The same evidence that defeated the attempt to expand every branch equally is presented again. Only the ability to we need to balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Understanding tree search

A game search revisits a move that won often while still testing a less explored alternative.

Run the tree search scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## The calculation hidden inside tree search

Before Tree Search receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

A cave explorer can investigate the river tunnel or the ridge tunnel. The river tunnel has produced good finds in eight visits; the ridge has been tried only once. Choosing only the better average may ignore an undiscovered ridge chamber, while choosing only the least visited branch wastes known evidence. The search score adds an uncertainty bonus that is large for neglected branches and shrinks as visits supply evidence.

The average reward records how well one branch has performed.
Visit count shrinks the exploration bonus as evidence accumulates.
Total visits increase pressure to reconsider neglected branches.
The constant controls how much uncertainty competes with known reward.

### Why no cheaper operation does the same job

[The bar over R](../../MATHEMATICAL_MOVES.md#symbol-decorations) marks the mean return, keeping what a branch has already demonstrated; see [mean](../../MATHEMATICAL_MOVES.md#mean).
[log N](../../MATHEMATICAL_MOVES.md#logarithm) lets exploration pressure grow slowly as the parent receives more visits instead of growing in direct proportion forever.
[Dividing by nₐ](../../MATHEMATICAL_MOVES.md#division) makes an often-tested action less uncertain; [the square root](../../MATHEMATICAL_MOVES.md#square-root) tempers how sharply that exploration bonus changes.
[c scales curiosity](../../MATHEMATICAL_MOVES.md#multiplication) and [addition](../../MATHEMATICAL_MOVES.md#addition) places that exploration bonus beside observed reward. Multiplying reward and curiosity would make either zero erase the other.

Every symbol in Tree Search can now be read back into an action already performed. The whole procedure fits in one line:

$$
\mathrm{score}(a)=\overline R_a+c\sqrt{\frac{\log N}{n_a}}
$$

## Where tree search runs out

Search quality depends on simulations and evaluation estimates.

Why does that boundary remain? Tree Search was built for one responsibility: we need to balance exploring uncertain branches with deepening promising ones, then propagate outcomes backward. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take tree search to the workbench

The argument for tree search is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running tree search, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the tree search result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 116](../116-reasoning-and-verification/README.md)
