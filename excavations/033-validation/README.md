# Excavation 033 — Validation — Testing Without Peeking at the Final Exam

<!-- book-prose-v2 -->

Regularization changes which fitted explanation the learner prefers. Choosing its strength by repeatedly checking the final exam would quietly turn that exam into more training data.

At this point the shortest path seems to be to use training loss for every choice; it rewards memorization.

This is how validation ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

The world supplies the one comparison the shortcut hoped never to face: check the test set repeatedly; every decision leaks test information back into development.

The wrong answer makes the need for validation inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end.

The usual name, **Validation**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to use training loss for every choice; it rewards memorization. produces the observed failure: check the test set repeatedly; every decision leaks test information back into development. Starting with the repaired demand to split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end preserves the information the shortcut lost. The subject of validation lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to split data by role: training changes weights, validation changes design decisions, and test data is opened once at the end instead of merely trying to use training loss for every choice; it rewards memorization.. That controlled contrast is what turns a plausible explanation of validation into an understandable derivation.

## The calculation hidden inside validation

Before Validation receives symbols, its procedure must be possible in ordinary language. Notation is useful here only because it lets us repeat that same reasoning without ambiguity.

The repair solves the immediate failure, but random splits fail when future, users, families, or duplicated records leak across boundaries. The split must match the real deployment question.

With 100 examples, use 60 to change weights, 20 to choose learning rate, and keep 20 sealed. If the sealed 20 guide choices, they stop being an honest final test.

### Names for pieces we have already used

**D** is all available data.
The three named subsets exist because weight learning, design choices, and final measurement must not share feedback.
Union means they reconstruct the available collection.
The intended split also requires no example to leak between sets, even though the compact union symbol alone does not state disjointness.

### Why no cheaper operation does the same job

[Union](../../MATHEMATICAL_MOVES.md#union) says the complete dataset contains the members assigned to training, validation, or test roles. Ordinary addition is for numeric quantities, not for joining collections of examples.
Separate names preserve separate responsibilities; the union sign alone does not guarantee the sets do not overlap, so the split procedure must enforce that boundary.

The notation is finally shorter than the story that created it:

$$
D=D_{\text{train}}\cup D_{\text{validation}}\cup D_{\text{test}}
$$

## Validation beyond this one case

A practice exam guides study. A sealed final exam measures what survived without feedback.

## Take validation to the workbench

The reader has reconstructed validation in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Build the failed idea before the repair. Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running validation, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the validation result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Mistakes worth preserving](mistakes.md); [The chapter diagram](diagram.md); [Invention exercises](exercises.md); [Primary research trail](references.md); and [Visual brief](images/README.md).

[Next: Excavation 034](../034-generalization/README.md)
