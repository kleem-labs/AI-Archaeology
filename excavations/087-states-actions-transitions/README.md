# Excavation 087 — States, Actions, and Transitions

<!-- book-prose-v2 -->

A reward says how an outcome turned out. To learn from it, the agent must preserve the situation it occupied, the action it chose, and the situation that followed.

The machinery already in our hands suggests that we store only action and final reward.

This is how states, actions, and transitions ought to begin—not with terminology, but with an honest attempt to make the smallest existing tool perform its job.

One counterexample is enough to expose the missing job: the trouble appears immediately: the same action helps in one situation and harms in another.

The wrong answer makes the need for states, actions, and transitions inspectable. We can state the new job in ordinary language before allowing symbols to hide it.

We can now repair the procedure without guessing: we need to record current state, chosen action, reward, and resulting state.

The usual name, **States, Actions, and Transitions**, can finally enter without mystery. It abbreviates a distinction the reader has already reconstructed in ordinary language.

We can audit the discovery from both directions. Starting with the shortcut to store only action and final reward produces the observed failure: the trouble appears immediately: the same action helps in one situation and harms in another. Starting with the repaired demand to we need to record current state, chosen action, reward, and resulting state preserves the information the shortcut lost. The subject of states, actions, and transitions lives in the difference between those two causal stories.

Keep track of what did not change: the observation, the goal, and the difficult case. What changes is the procedure's capacity to we need to record current state, chosen action, reward, and resulting state instead of merely trying to store only action and final reward. That controlled contrast is what turns a plausible explanation of states, actions, and transitions into an understandable derivation.

## Understanding states, actions, and transitions

“Move right” from left of the door succeeds; the same action beside a cliff fails because state differs.

There are now two histories of this states, actions, and transitions case: one loses the decisive evidence, and one preserves it. The inherited name belongs to the second history only after we can explain that difference without using the name.

## Where states, actions, and transitions runs out

A state representation may omit information needed for future decisions.

Look back at what states, actions, and transitions actually preserves: it can we need to record current state, chosen action, reward, and resulting state. The unresolved case asks for a different distinction, absent from both its inputs and its procedure. More forceful use of the same mechanism cannot create missing evidence.

## Take states, actions, and transitions to the workbench

The reader has reconstructed states, actions, and transitions in words; the workbench tests whether those words specify a real procedure. Follow [Pure Python → NumPy → PyTorch](implementation/README.md). Keep the values small enough that every intermediate result can be predicted by hand before a library computes it. Before running states, actions, and transitions, write down the observation that would prove your repaired rule still misunderstood the problem; a laboratory that cannot surprise its designer is only a demonstration.

Explain the states, actions, and transitions result once without terminology, then once with the precise symbols or state transitions the implementation used.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 088](../088-value-functions/README.md)
