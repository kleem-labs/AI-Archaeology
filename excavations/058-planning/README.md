# Excavation 058 — Planning — Turning a Goal into Checkable Steps

[Previous: Excavation 057](../057-prompt-injection/README.md)

“Move my website to a new host” contains dependencies: back up data, configure the destination, test it, change traffic, and preserve rollback.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Ask the agent to take the next action that sounds useful until the goal appears complete.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* It changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive.

Name the missing guarantee before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Before changing traffic, the plan requires a successful backup ID, a passing health check, and a rollback target. Missing evidence blocks the irreversible step.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

A plan is a hypothesis, not reality. Long plans become stale and must yield to new observations.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 059](../059-memory/README.md)
