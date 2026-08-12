# Excavation 121 — Formal Verification

Program synthesis turns examples into candidate procedures. Tests inspect selected cases; a safety-critical system may need proof that a property holds for every input permitted by the specification.

We first try to add more random tests and call the property proven.

Yet an untested edge case can remain.

That failure tells us to state assumptions and desired properties formally, then prove or mechanically check that every transition preserves them.

## Let the case decide

Prove a refund state machine can issue at most one payment per idempotency key.

## The boundary of the discovery

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
