# Excavation 105 — Selective Prediction

<!-- book-prose-v2 -->

Active learning spends human effort where it should teach the most. A deployed system still encounters cases where no available evidence justifies any answer, even after labels have been chosen carefully.

At this point the shortest path seems to be to always return the highest-scoring answer.

This is how selective prediction ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

The world supplies the one comparison the shortcut hoped never to face: a forced answer converts uncertainty into confident-looking error.

The wrong answer makes the need for selective prediction inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: allow abstention and choose a coverage level whose retained answers meet a risk target.

The usual name, **Selective Prediction**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to always return the highest-scoring answer produces the observed failure: a forced answer converts uncertainty into confident-looking error. Starting with the repaired demand to allow abstention and choose a coverage level whose retained answers meet a risk target preserves the information the shortcut lost. The subject of selective prediction lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to allow abstention and choose a coverage level whose retained answers meet a risk target instead of merely trying to always return the highest-scoring answer. That controlled contrast is what turns a plausible explanation of selective prediction into an understandable derivation.

## Understanding selective prediction

The system answers 80 of 100 cases and is correct on 78; the other 20 go to a human rather than becoming guesses.

There are now two histories of this selective prediction case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## Where selective prediction runs out

Abstention shifts work and may fail unevenly across groups.

Look back at what selective prediction actually preserves: it can allow abstention and choose a coverage level whose retained answers meet a risk target. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take selective prediction to the workbench

The reader has reconstructed selective prediction in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running selective prediction, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the selective prediction result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 106](../106-catastrophic-forgetting/README.md)
