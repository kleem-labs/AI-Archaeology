# Excavation 121 — Formal Verification

<!-- book-prose-v2 -->

Program synthesis turns examples into candidate procedures. Tests inspect selected cases; a safety-critical system may need proof that a property holds for every input permitted by the specification.

For a moment, remain loyal to the simplest proposal: add more random tests and call the property proven.

Its appeal is not ignorance but economy. Formal Verification should not be added until an observation exposes the exact thing the older procedure cannot preserve.

The world supplies the one comparison the shortcut hoped never to face: an untested edge case can remain.

Notice what the counterexample has accomplished for formal verification. It has not handed us a standard technique. It has told us the property any successful repair must preserve.

So the new mechanism must do one additional job: state assumptions and desired properties formally, then prove or mechanically check that every transition preserves them.

Humanity eventually gathered this problem and its repairs under the name **Formal Verification**. The name comes after the need; it must never conceal the observation that gave it meaning.

Now perform a small thought experiment. Keep the whole situation fixed but replace formal verification with the old instruction to add more random tests and call the property proven. The result is again that an untested edge case can remain. Put back only the requirement to state assumptions and desired properties formally, then prove or mechanically check that every transition preserves them. The repaired result is possible because one missing distinction, not an arbitrary collection of machinery, has been restored.

The comparison has one invariant: the world does not become kinder when formal verification is introduced. The same evidence that defeated the attempt to add more random tests and call the property proven is presented again. Only the ability to state assumptions and desired properties formally, then prove or mechanically check that every transition preserves them changes, so the repaired conclusion cannot be credited to a conveniently different example.

## Understanding formal verification

Prove a refund state machine can issue at most one payment per idempotency key.

Run the formal verification scene twice in your head. First obey the shortcut exactly. Then change only the rule that failed. The comparison separates a necessary mathematical move from decorative notation.

## Where formal verification runs out

Proof covers the formal model, which may omit real-world behavior.

Why does that boundary remain? Formal Verification was built for one responsibility: state assumptions and desired properties formally, then prove or mechanically check that every transition preserves them. Solving that responsibility does not manufacture evidence about the separate decision above. The unfinished job becomes the next chapter's observation.

## Take formal verification to the workbench

The argument for formal verification is still provisional until a runnable case can make it fail. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running formal verification, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the formal verification result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 122](../122-differential-privacy/README.md)
