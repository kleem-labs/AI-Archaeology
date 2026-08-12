# Excavation 061 — Verification — How Does the Agent Know It Succeeded?

A state machine records what transitions are allowed and which events occurred. Reaching a state named `done` is still only a claim unless observable evidence proves the requested outcome in the outside world.

We first try to trust the absence of an error message or the model’s own description of its work.

Yet the changed code compiles but breaks another case. Confidence is not evidence of the requested outcome.

That failure tells us to define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state.

## Let the case decide

For “fix CSV import,” success requires the original failing file to load, existing import tests to remain green, and malformed rows to produce the agreed error.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## The boundary of the discovery

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
