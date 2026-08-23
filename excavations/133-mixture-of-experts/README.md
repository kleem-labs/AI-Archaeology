# Excavation 133 — Mixture of Experts — Spending Computation Where It Helps

<!-- book-prose-v2 -->

Distillation transfers a teacher's pattern of belief into a smaller student. A dense student still spends every parameter on every token, even when different inputs need different expertise.

For a moment, remain loyal to the simplest proposal: run every specialist for every token and average them.

Its appeal is not ignorance but economy. Mixture of Experts should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Reality now asks a question the retained information cannot answer: most computation is wasted on specialists irrelevant to the current token.

Notice what the counterexample has accomplished for mixture of experts. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: learn a router that sends each token to a small number of experts while balancing their workload.

Humanity eventually gathered this problem and its repairs under the name **Mixture of Experts**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace mixture of experts with the old instruction to run every specialist for every token and average them. The result is again that most computation is wasted on specialists irrelevant to the current token. Put back only the requirement to learn a router that sends each token to a small number of experts while balancing their workload. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when mixture of experts is introduced. The same evidence that defeated the attempt to run every specialist for every token and average them is presented again. Only the ability to learn a router that sends each token to a small number of experts while balancing their workload changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Spending Computation Where It Helps

Route a code token toward syntax experts and a biology token toward scientific-language experts, then combine only selected outputs.

Run the mixture of experts scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## Where mixture of experts runs out

Routers can collapse onto popular experts and leave others untrained.

Why does that boundary remain? Mixture of Experts was built for one responsibility: learn a router that sends each token to a small number of experts while balancing their workload. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take mixture of experts to the workbench

The argument for mixture of experts is still provisional until a runnable case can make it fail. Rebuild the tempting shortcut first, make its failure visible, and then implement the repair in [Pure Python, NumPy, and PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running mixture of experts, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the mixture of experts result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [The wrong ideas worth preserving](mistakes.md); [Diagram and dependency path](diagram.md); [Invention exercises](exercises.md); [References and reading trail](references.md); and [Visual asset brief](images/README.md).

[Next: Sparse Attention — Looking Without Comparing Everything](../134-sparse-attention/README.md)
