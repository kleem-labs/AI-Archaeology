# Excavation 051 — Scaling Laws — What Improves When We Add More?

<!-- book-prose-v2 -->

Data quality asks what patterns the training process actually repeated. Once the lessons are trustworthy, the builders must decide whether the next unit of computation should buy more data, a larger model, or longer training.

The machinery already in our hands suggests that we make the model as large as possible and assume capability follows parameter count.

This is how scaling laws ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

Then a case arrives in which convenience and truth separate: a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns.

The wrong answer makes the need for scaling laws inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number.

The usual name, **Scaling Laws**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to make the model as large as possible and assume capability follows parameter count produces the observed failure: a huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns. Starting with the repaired demand to we need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number preserves the information the shortcut lost. The subject of scaling laws lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number instead of merely trying to make the model as large as possible and assume capability follows parameter count. That controlled contrast is what turns a plausible explanation of scaling laws into an understandable derivation.

## The calculation hidden inside scaling laws

Before Scaling Laws receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

Models with 1, 2, and 4 million effective units achieve losses 4.0, 3.2, and 2.8. Improvement continues but shrinks. The curve helps estimate whether doubling again is worth the cost; it does not promise a new capability.

### Names for pieces we have already used

N is the resource being scaled. The negative exponent makes loss fall as N grows. Alpha controls how quickly returns diminish. A scales the improvable part; B is the floor this simple trend cannot beat.

### Why no cheaper operation does the same job

[The negative power](../../MATHEMATICAL_MOVES.md#powers) makes the improvable part fall as resource N grows, with α controlling how quickly returns diminish.
[A scales that falling term](../../MATHEMATICAL_MOVES.md#multiplication) to the observed problem; adding A would create a floor instead of changing improvement size.
[Adding B](../../MATHEMATICAL_MOVES.md#addition) represents a remaining floor this simple scaling route does not remove. Multiplying by B would force the whole loss toward zero instead of allowing an irreducible remainder.

Every symbol in Scaling Laws can now be read back into an action already performed. The whole procedure fits in one line:

$$
L(N)=A N^{-\alpha}+B
$$

## Where scaling laws runs out

A fitted trend applies within observed regimes. Data quality, architecture changes, and new bottlenecks can bend it.

Look back at what scaling laws actually preserves: it can we need to run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take scaling laws to the workbench

The reader has reconstructed scaling laws in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running scaling laws, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the scaling laws result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 052](../052-instruction-tuning/README.md)
