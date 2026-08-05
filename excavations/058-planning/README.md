# Excavation 058 — Planning — Turning a Goal into Checkable Steps

[Previous: Excavation 057](../057-prompt-injection/README.md)

## Take the First Step Yourself

> **Your problem:** “Move my website to a new host” contains dependencies: back up data, configure the destination, test it, change traffic, and preserve rollback.

> **Try your first idea:** Ask the agent to take the next action that sounds useful until the goal appears complete.

> **Now try to break your idea:** It changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive.

> Stop here. State what a repair must guarantee without using the chapter title.

## The Observation

“Move my website to a new host” contains dependencies: back up data, configure the destination, test it, change traffic, and preserve rollback.

## Your First Attempt

Ask the agent to take the next action that sounds useful until the goal appears complete.

## Break Your First Attempt

It changes DNS before verifying the new server, loses the rollback path, and discovers a missing database only after users arrive.

Name the missing guarantee before continuing.

## Repair Your Attempt

Represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions.

## What You Have Just Invented

**Represent the goal as ordered steps with prerequisites, expected evidence, risk, and rollback conditions. Re-plan when observations contradict assumptions.**

## Rebuild the Discovery with a Concrete Case

Before changing traffic, the plan requires a successful backup ID, a passing health check, and a rollback target. Missing evidence blocks the irreversible step.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Real-World Limit

A plan is a hypothesis, not reality. Long plans become stale and must yield to new observations.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 059](../059-memory/README.md)
