# Excavation 060 — State Machines — Knowing What Has Actually Happened

[Previous: Excavation 059](../059-memory/README.md)

## Take the First Step Yourself

> **Your problem:** A support agent may draft a refund, request approval, issue it, or report completion. These are different realities, not merely different sentences.

> **Try your first idea:** Let the conversation prose serve as the workflow state.

> **Now try to break your idea:** The model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result.

> Stop here. State what a repair must guarantee without using the chapter title.

## The Observation

A support agent may draft a refund, request approval, issue it, or report completion. These are different realities, not merely different sentences.

## Your First Attempt

Let the conversation prose serve as the workflow state.

## Break Your First Attempt

The model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result.

Name the missing guarantee before continuing.

## Repair Your Attempt

Represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system.

## What You Have Just Invented

**Represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system.**

## Rebuild the Discovery with a Concrete Case

A refund moves requested → approved only with an approval record, then approved → issued only with a payment transaction ID. A sentence alone changes nothing.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Real-World Limit

Real workflows have exceptions and concurrent events. State machines need recovery paths and authoritative external records.

## Implementation

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Exercises and Connections

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 061](../061-verification/README.md)
