# Excavation 063 — Multi-Agent Coordination — When Should Work Be Divided?

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Graphs & Relational Structures](../../MATHEMATICS_ATLAS.md#graphs) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Agents and reliable action

Idempotent retries make repetition safe. A large goal can nevertheless overwhelm one agent's context and tools, raising the question of when division of work reduces risk rather than multiplying it.

Inside the Gatehouse of Consequences, the old method is given an honest chance. The gatekeeper places the evidence on the iron threshold and tries to create many agents for every problem and let them freely edit shared state.

Nothing about this first move is careless. To create many agents for every problem and let them freely edit shared state is to ask whether the existing idea can stretch one step farther before another concept is added to the machine. If it can, the simpler rule should remain. If it cannot, the manner of its failure must tell us more than the fact that an answer was wrong; it must reveal which responsibility was absent.

The attempt reaches a boundary that greater confidence cannot cross: they duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving.

The important discovery is not merely that trying to create many agents for every problem and let them freely edit shared state failed; many bad guesses can fail. It is that the failure remains stable when the calculation is repeated and irrelevant details are changed. The same missing capacity keeps reappearing. That stability turns the counterexample into a design requirement: the next method must preserve the exact distinction the old one erased. Both paths will be tested against the iron threshold, so success cannot be manufactured by quietly replacing the original question.

The old construction is therefore not discarded. It is widened just enough to delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result. The width of the repair matters: too little reproduces the failure, while an unrelated addition would conceal why any new machinery was introduced.

The necessary extension now has a name: **Multi-Agent Coordination**. Nothing in the name adds to the requirement the evidence has already established; it only lets that requirement travel.

## When Should Work Be Divided

Three agents receive distinct questions and return evidence in the same schema. The coordinator resolves conflicts and alone edits the final report.

Multi-Agent Coordination earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

## Where multi-agent coordination runs out

Parallel agents amplify both capability and error. Shared resources, authority, and termination require careful control.

One unsolved mark remains on the iron threshold. None of the responsibilities inside Multi-Agent Coordination can move it, and so it becomes the observation from which the next excavation must begin.

## Return to the iron threshold

Rebuild the multi-agent coordination scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 064](../064-observability/README.md)
