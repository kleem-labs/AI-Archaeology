# Excavation 064 — Observability — Seeing Why an Agent Failed

[Previous: Excavation 063](../063-multi-agent-coordination/README.md)

An agent stops after twenty steps with a wrong result. The final answer does not reveal whether retrieval, planning, a tool, or verification failed.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Log only the final response, or log every hidden detail without structure.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* The first gives no diagnosis; the second creates an unreadable, expensive, privacy-sensitive transcript.

Name the missing guarantee before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Record structured events for decisions, tool calls, state changes, costs, timing, evidence, and outcomes while redacting sensitive content.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

A trace shows retrieval returned an outdated policy, the planner accepted it, and verification checked format but not date. The repair can now target the real failure.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

Logs describe what instrumentation captured. Missing fields, privacy limits, and misleading metrics still constrain diagnosis.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 065](../065-bounded-autonomy/README.md)
