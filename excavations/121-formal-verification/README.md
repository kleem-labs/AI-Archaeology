# Excavation 121 — Formal Verification

[Previous: Excavation 120](../120-program-synthesis/README.md)

Tests sample cases. How can we guarantee a property for all allowed inputs?

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Add more random tests and call the property proven.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* An untested edge case can remain.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* State assumptions and desired properties formally, then prove or mechanically check that every transition preserves them.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

Prove a refund state machine can issue at most one payment per idempotency key.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

Proof covers the formal model, which may omit real-world behavior.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 122](../122-differential-privacy/README.md)
