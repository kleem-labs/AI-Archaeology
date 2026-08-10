# Excavation 061 — Verification — How Does the Agent Know It Succeeded?

[Previous: Excavation 060](../060-state-machines/README.md)

A coding agent edits a function and announces the bug is fixed.

A reasonable place to begin is: Trust the absence of an error message or the model’s own description of its work.

Now place that proposal under pressure: The changed code compiles but breaks another case. Confidence is not evidence of the requested outcome. Name the missing guarantee before continuing.

What broke tells us what the replacement must preserve: Define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state.

## Now work a case you can see

For “fix CSV import,” success requires the original failing file to load, existing import tests to remain green, and malformed rows to produce the agreed error.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

Verification can test only stated properties. A passing check suite may omit the most important behavior.

The repair is explicit: define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state. Its power is also its boundary; anything not represented in those operations remains undecided.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 062](../062-retries-idempotency/README.md)
