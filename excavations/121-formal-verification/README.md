# Excavation 121 — Formal Verification

[Previous: Excavation 120](../120-program-synthesis/README.md)

Tests sample cases. How can we guarantee a property for all allowed inputs?

A reasonable place to begin is: Add more random tests and call the property proven.

Now place that proposal under pressure: An untested edge case can remain.

What broke tells us what the replacement must preserve: State assumptions and desired properties formally, then prove or mechanically check that every transition preserves them.

## Now work a case you can see

Prove a refund state machine can issue at most one payment per idempotency key.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Proof covers the formal model, which may omit real-world behavior.

The repair is explicit: state assumptions and desired properties formally, then prove or mechanically check that every transition preserves them. Its power is also its boundary; anything not represented in those operations remains undecided.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 122](../122-differential-privacy/README.md)
