# Excavation 061 — Verification — How Does the Agent Know It Succeeded?

<!-- book-prose-v2 -->

A state machine records what transitions are allowed and which events occurred. Reaching a state named `done` is still only a claim unless observable evidence proves the requested outcome in the outside world.

For a moment, remain loyal to the simplest proposal: trust the absence of an error message or the model’s own description of its work.

Its appeal is not ignorance but economy. Verification should not be added until an observation exposes the exact thing the older procedure cannot preserve.

Reality now asks a question the retained information cannot answer: the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome.

Notice what the counterexample has accomplished for verification. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state.

Humanity eventually gathered this problem and its repairs under the name **Verification**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace verification with the old instruction to trust the absence of an error message or the model’s own description of its work. The result is again that the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome. Put back only the requirement to define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when verification is introduced. The same evidence that defeated the attempt to trust the absence of an error message or the model’s own description of its work is presented again. Only the ability to define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state changes, so the repaired conclusion cannot be credited to a conveniently different example.

## How Does the Agent Know It Succeeded

For “fix CSV import,” success requires the original failing file to load, existing import tests to remain green, and malformed rows to produce the agreed error.

Verification earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

Run the verification scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## Where verification runs out

Verification can test only stated properties. A passing check suite may omit the most important behavior.

Why does that boundary remain? Verification was built for one responsibility: define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take verification to the workbench

The argument for verification is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running verification, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the verification result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 062](../062-retries-idempotency/README.md)
