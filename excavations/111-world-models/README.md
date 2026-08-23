# Excavation 111 — World Models

<!-- book-prose-v2 -->

Self-supervision extracts lessons from unlabeled observations. An acting system needs more than representations: before choosing, it must imagine how the world may change after each possible action.

The machinery already in our hands suggests that we learn only which action was rewarded in previously visited situations.

This is how world models ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

One counterexample is enough to expose the missing job: the agent cannot imagine untried sequences or reuse physical regularities.

The wrong answer makes the need for world models inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to learn a compact model that predicts next state and reward from current state and action.

The usual name, **World Models**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to learn only which action was rewarded in previously visited situations produces the observed failure: the agent cannot imagine untried sequences or reuse physical regularities. Starting with the repaired demand to we need to learn a compact model that predicts next state and reward from current state and action preserves the information the shortcut lost. The subject of world models lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to learn a compact model that predicts next state and reward from current state and action instead of merely trying to learn only which action was rewarded in previously visited situations. That controlled contrast is what turns a plausible explanation of world models into an understandable derivation.

## Understanding world models

From ball position and push direction, predict where the ball will move before choosing the push.

There are now two histories of this world models case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## Where world models runs out

Model errors compound during long imagined rollouts.

Look back at what world models actually preserves: it can we need to learn a compact model that predicts next state and reward from current state and action. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take world models to the workbench

The reader has reconstructed world models in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running world models, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the world models result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 112](../112-causal-inference/README.md)
