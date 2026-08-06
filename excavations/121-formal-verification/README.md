# Excavation 121 — Formal Verification

[Previous: Excavation 120](../120-program-synthesis/README.md)

## Take the First Step Yourself

> **Your problem:** Tests sample cases. How can we guarantee a property for all allowed inputs?

> **Try your first idea:** Add more random tests and call the property proven.

> **Now try to break your idea:** An untested edge case can remain.

> Stop here. State the missing requirement without naming the repair.

## The Observation

Tests sample cases. How can we guarantee a property for all allowed inputs?

## Your First Attempt

Add more random tests and call the property proven.

## Break Your First Attempt

An untested edge case can remain.

## Repair Your Attempt

State assumptions and desired properties formally, then prove or mechanically check that every transition preserves them.

## What You Have Just Invented

**State assumptions and desired properties formally, then prove or mechanically check that every transition preserves them.**

## Rebuild the Discovery with a Concrete Case

Prove a refund state machine can issue at most one payment per idempotency key.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Real-World Limit

Proof covers the formal model, which may omit real-world behavior.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 122](../122-differential-privacy/README.md)
