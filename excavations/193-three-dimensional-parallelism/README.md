# Excavation 193 — Three-Dimensional Parallelism — Give Each Memory Wall Its Own Axis

<!-- book-prose-v2 -->

Pipeline micro-batches keep layer stages busy. A large run may still exceed memory inside one layer, require more independent data witnesses, and contain too many layers for one device group.

For a moment, remain loyal to the simplest proposal: increase whichever parallel technique was introduced most recently until the model fits.

Its appeal is not ignorance but economy. Three-Dimensional Parallelism should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently.

Notice what the counterexample has accomplished for three-dimensional parallelism. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost.

Humanity eventually gathered this problem and its repairs under the name **Three-Dimensional Parallelism**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace three-dimensional parallelism with the old instruction to increase whichever parallel technique was introduced most recently until the model fits. The result is again that more pipeline stages increase bubbles, more tensor splits increase frequent communication, and more data replicas preserve full model memory. One axis cannot solve three different limits efficiently. Put back only the requirement to compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when three-dimensional parallelism is introduced. The same evidence that defeated the attempt to increase whichever parallel technique was introduced most recently until the model fits is presented again. Only the ability to compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Give Each Memory Wall Its Own Axis

Two tensor workers form each layer, four pipeline stages hold the depth, and three data replicas see different examples. The run uses 2×4×3=24 workers with each axis performing one named job.

Run the three-dimensional parallelism scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## The calculation hidden inside three-dimensional parallelism

Before Three-Dimensional Parallelism receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Each factor counts independent choices along one model-parallel axis. Selecting one tensor rank, one pipeline rank, and one data rank identifies exactly one worker; P_total counts all such combinations.

### Why no cheaper operation does the same job

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced by the product rule: every choice on one axis pairs with every choice on the others. Addition would count axis labels rather than workers. [Equality](../../MATHEMATICAL_MOVES.md#equals) assumes the grid is fully populated.

Every symbol in Three-Dimensional Parallelism can now be read back into an action already performed. The whole procedure fits in one line:

$$
P_{\text{total}}=P_{\text{tensor}}P_{\text{pipeline}}P_{\text{data}}
$$

## Where three-dimensional parallelism runs out

Three-dimensional parallelism increases coordination and configuration complexity; a poor mapping to the physical network can spend more time communicating than computing.

Why does that boundary remain? Three-Dimensional Parallelism was built for one responsibility: compose tensor parallelism within layers, pipeline parallelism across layer groups, and data parallelism across independent batch replicas, choosing each degree from topology and measured cost. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take three-dimensional parallelism to the workbench

The argument for three-dimensional parallelism is still provisional until a runnable case can make it fail. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running three-dimensional parallelism, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the three-dimensional parallelism result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Sharded Checkpoints — Save One Recoverable State Without Gathering It](../194-sharded-checkpoints/README.md)
