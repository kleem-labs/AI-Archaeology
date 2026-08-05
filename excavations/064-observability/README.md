# Excavation 064 — Observability — Seeing Why an Agent Failed

[Previous: Excavation 063](../063-multi-agent-coordination/README.md)

## Take the First Step Yourself

> **Your problem:** An agent stops after twenty steps with a wrong result. The final answer does not reveal whether retrieval, planning, a tool, or verification failed.

> **Try your first idea:** Log only the final response, or log every hidden detail without structure.

> **Now try to break your idea:** The first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript.

> Stop here. State what a repair must guarantee without using the chapter title.

## The Observation

An agent stops after twenty steps with a wrong result. The final answer does not reveal whether retrieval, planning, a tool, or verification failed.

## Your First Attempt

Log only the final response, or log every hidden detail without structure.

## Break Your First Attempt

The first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript.

Name the missing guarantee before continuing.

## Repair Your Attempt

Record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content.

## What You Have Just Invented

**Record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content.**

## Rebuild the Discovery with a Concrete Case

A trace shows retrieval returned an outdated policy, the planner accepted it, and verification checked format but not date. The repair can now target the real failure.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Real-World Limit

Logs describe what instrumentation captured. Missing fields, privacy limits, and misleading metrics still constrain diagnosis.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 065](../065-bounded-autonomy/README.md)
