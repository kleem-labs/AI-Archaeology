# Excavation 058 — Planning — Turning a Goal into Checkable Steps

<!-- book-prose-v2 -->

<!-- mathematical-world-v1 -->

Prompt-injection defenses keep evidence from silently becoming authority. A safe tool call can still be the wrong step in a long task unless the goal is decomposed into checkable dependencies.

The iron threshold at the Gatehouse of Consequences still carries the marks of the previous discovery. The gatekeeper follows them as far as they seem willing to go: ask the agent to take the next action that sounds useful until the goal appears complete.

The gatekeeper repeats the calculation, hoping for an arithmetic mistake. The same obstruction returns: it changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive. The failure is stable enough to become evidence.

*The gatekeeper sketches the break before changing it:*

```text
light / evidence
      │
      ├── old lens ──▶ ask the agent to take the next action… ──▶ blurred: it changes DNS before verifying the…
      │
      └── new lens ──▶ represent the goal as ordered steps… ──▶ distinction survives
```

Across the iron threshold, the old path and the repaired path run side by side. One carries “ask the agent to take the next action that sounds useful until the goal appears complete”; the other knows how to represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions. When the failure—it changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive—arrives, only one path still possesses a place to record the missing distinction.

The failure is no longer an embarrassment to planning. It is a compass: it points directly toward the information the next construction must retain.

The evidence permits one narrow invention: represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions. This problem and its repair will travel under the name **Planning**, but the name carries no knowledge the scene has not earned.

Under the latest ink, the first question is still legible: what if we followed the tempting rule—ask the agent to take the next action that sounds useful until the goal appears complete? The answer remains it changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive. The new construction earns its permanence by answering that old question without pretending it was foolish to ask.

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
