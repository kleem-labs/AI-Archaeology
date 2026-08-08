# Excavation 061 — Verification — How Does the Agent Know It Succeeded?

[Previous: Excavation 060](../060-state-machines/README.md)

A coding agent edits a function and announces the bug is fixed.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Trust the absence of an error message or the model’s own description of its work.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* The changed code compiles but breaks another case. Confidence is not evidence of the requested outcome.

Name the missing guarantee before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

For “fix CSV import,” success requires the original failing file to load, existing import tests to remain green, and malformed rows to produce the agreed error.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

Verification can test only stated properties. A passing check suite may omit the most important behavior.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 062](../062-retries-idempotency/README.md)
