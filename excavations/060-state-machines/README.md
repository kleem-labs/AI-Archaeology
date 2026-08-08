# Excavation 060 — State Machines — Knowing What Has Actually Happened

[Previous: Excavation 059](../059-memory/README.md)

A support agent may draft a refund, request approval, issue it, or report completion. These are different realities, not merely different sentences.

Pause here. You do not know the accepted method yet. What would you try?

*Your first move:* Let the conversation prose serve as the workflow state.

It sounds reasonable. Now make it face the smallest case that refuses to cooperate.

*The case that breaks it:* The model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result.

Name the missing guarantee before continuing.

Do not reach for terminology. Say—in ordinary language—what the repaired idea must preserve or accomplish.

*Your repair:* Represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system.

Only after that reasoning may we give your discovery its inherited name.

## Now work a case you can see

A refund moves requested → approved only with an approval record, then approved → issued only with a payment transaction ID. A sentence alone changes nothing.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## Where your new idea still breaks

Real workflows have exceptions and concurrent events. State machines need recovery paths and authoritative external records.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 061](../061-verification/README.md)
