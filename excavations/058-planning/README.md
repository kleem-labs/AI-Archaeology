# Excavation 058 — Planning — Turning a Goal into Checkable Steps

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

<!-- flow-prose-v1 -->

<!-- mathematical-lineage-v1 -->
> **Mathematical roots:** [Dynamical Systems, Control & Decision Theory](../../MATHEMATICS_ATLAS.md#dynamics) · [Discrete Mathematics, Logic & Algorithms](../../MATHEMATICS_ATLAS.md#discrete)
>
> **Applied territory:** Agents and reliable action

Prompt-injection defenses keep evidence from silently becoming authority. A safe tool call can still be the wrong step in a long task unless the goal is decomposed into checkable dependencies.

A new case arrives at the Gatehouse of Consequences. Nothing yet demands a new invention, so the gatekeeper uses the iron threshold to ask the agent to take the next action that sounds useful until the goal appears complete.

This is precisely the kind of shortcut a careful builder should try first. The instruction to ask the agent to take the next action that sounds useful until the goal appears complete preserves the successful part of the earlier method and avoids paying for a distinction that may not matter. When the evidence is kind, the shortcut and a more elaborate construction give the same answer. Their difference becomes visible only when the world presents the case the shortcut cannot represent.

For a moment the answer looks complete. The next observation shows what the method could not preserve: it changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive.

The counterexample separates two questions that the attempt to ask the agent to take the next action that sounds useful until the goal appears complete had treated as one. Until now that collapse was invisible because both questions happened to lead to the same decision. Here they part company. A useful repair must keep them apart wherever the difference affects the result, without throwing away the information and economy the earlier construction had already earned. Keeping the iron threshold fixed makes the comparison honest: only the missing responsibility, rather than the surrounding story, is allowed to change.

Only the broken responsibility needs to change. The method must now represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions. With that change, the easy case is still understandable, while the counterexample no longer has to be forced into an answer known to be wrong.

This repaired capacity is the idea named **Planning**. Its name is shorter than the path that made it necessary, but the path remains the source of its meaning.

## Turning a Goal into Checkable Steps

Before changing traffic, the plan requires a successful backup ID, a passing health check, and a rollback target. Missing evidence blocks the irreversible step.

Planning earns a boundary, procedure, or system contract rather than a new equation. Symbols here would decorate the decision instead of clarifying it.

## Where planning runs out

A plan is a hypothesis, not reality. Long plans become stale and must yield to new observations.

The planning repair holds, but the world asks for something it was never given. At the Gatehouse of Consequences, that unmet need is preserved rather than hidden behind a stronger claim.

## Return to the iron threshold

Rebuild the planning scene in the [Pure Python, NumPy, and PyTorch implementations](implementation/README.md). Run the tempting rule first and predict its failure on paper. Then change only the responsibility earned in this excavation and compare every intermediate value. If the repaired path surprises you, the surprise belongs in the margin before the code is changed.

The rest of the evidence remains beside this excavation: [Invention challenges](exercises.md); [Mistakes](mistakes.md); [Diagram](diagram.md); [References](references.md); and [Visual brief](images/README.md).

[Next: Excavation 059](../059-memory/README.md)
