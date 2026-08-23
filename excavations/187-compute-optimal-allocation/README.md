# Excavation 187 — Compute-Optimal Allocation — Buy a Larger Memory or More Experience?

<!-- book-prose-v2 -->

The token budget fixes how much evidence the model will see. A fixed compute allowance still permits a wider model trained on fewer tokens or a smaller model trained on more.

Before naming anything new, try to spend nearly the entire budget on parameter count because a larger model can store more patterns.

Its appeal is not ignorance but economy. Compute-Optimal Allocation should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Then a case arrives in which convenience and truth separate: the large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence.

Notice what the counterexample has accomplished for compute-optimal allocation. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone.

Humanity eventually gathered this problem and its repairs under the name **Compute-Optimal Allocation**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace compute-optimal allocation with the old instruction to spend nearly the entire budget on parameter count because a larger model can store more patterns. The result is again that the large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence. Put back only the requirement to estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when compute-optimal allocation is introduced. The same evidence that defeated the attempt to spend nearly the entire budget on parameter count because a larger model can store more patterns is presented again. Only the ability to estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Buy a Larger Memory or More Experience

The station compares doubling parameters while halving tokens with keeping the smaller model and doubling tokens. Because both alter the same compute bill, held-out scaling runs decide which balance learns more.

Run the compute-optimal allocation scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## The calculation hidden inside compute-optimal allocation

Before Compute-Optimal Allocation receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

P is the number of trainable model parameters, D is the number of training tokens, and C is a rough count of floating-point work for dense Transformer training; six summarizes forward and backward work per parameter-token interaction.

### Why no cheaper operation does the same job

[Multiplication](../../MATHEMATICAL_MOVES.md#multiplication) is forced because every token exercises the model's parameters: doubling either P or D roughly doubles work. [Approximation](../../MATHEMATICAL_MOVES.md#approximation) preserves the scaling relation while admitting architecture and implementation details. Adding P and D would combine incompatible units.

Every symbol in Compute-Optimal Allocation can now be read back into an action already performed. The whole procedure fits in one line:

$$
C\approx 6PD
$$

## Where compute-optimal allocation runs out

Compute-optimal estimates are empirical and depend on architecture, data quality, optimizer, and the inference cost the project can afford afterward.

Why does that boundary remain? Compute-Optimal Allocation was built for one responsibility: estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take compute-optimal allocation to the workbench

The argument for compute-optimal allocation is still provisional until a runnable case can make it fail. Reproduce the failure first, then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Predict the intermediate values before running the code. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running compute-optimal allocation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the compute-optimal allocation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [A chapter-specific diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Learning-Rate Warmup — Let Adam Learn the Terrain Before Running](../188-learning-rate-warmup/README.md)
