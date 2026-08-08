# Excavation 063 — Multi-Agent Coordination — When Should Work Be Divided?

[Previous: Excavation 062](../062-retries-idempotency/README.md)

A research task contains independent legal, technical, and market questions. One agent can process them sequentially, but specialization and parallel work may help.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Create many agents for every problem and let them freely edit shared state.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* They duplicate searches, contradict one another, overwrite files, and consume more time coordinating than solving.

Name the missing guarantee before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Delegate only separable work with explicit ownership, inputs, outputs, and merge rules. Keep one accountable coordinator for the final result.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Three agents receive distinct questions and return evidence in the same schema. The coordinator resolves conflicts and alone edits the final report.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

Parallel agents amplify both capability and error. Shared resources, authority, and termination require careful control.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 064](../064-observability/README.md)
