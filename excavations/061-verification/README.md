# Excavation 061 — Verification — How Does the Agent Know It Succeeded?

[Previous: Excavation 060](../060-state-machines/README.md)

## Take the First Step Yourself

> **Your problem:** A coding agent edits a function and announces the bug is fixed.

> **Try your first idea:** Trust the absence of an error message or the model’s own description of its work.

> **Now try to break your idea:** The changed code compiles but breaks another case. Confidence is not evidence of the requested outcome.

> Stop here. State what a repair must guarantee without using the chapter title.

## The Observation

A coding agent edits a function and announces the bug is fixed.

## Your First Attempt

Trust the absence of an error message or the model’s own description of its work.

## Break Your First Attempt

The changed code compiles but breaks another case. Confidence is not evidence of the requested outcome.

Name the missing guarantee before continuing.

## Repair Your Attempt

Define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state.

## What You Have Just Invented

**Define success before acting, then collect independent evidence: tests, queries, rendered output, checksums, or user-visible state.**

## Rebuild the Discovery with a Concrete Case

For “fix CSV import,” success requires the original failing file to load, existing import tests to remain green, and malformed rows to produce the agreed error.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Real-World Limit

Verification can test only stated properties. A passing check suite may omit the most important behavior.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 062](../062-retries-idempotency/README.md)
