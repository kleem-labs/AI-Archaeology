# Excavation 060 — State Machines — Knowing What Has Actually Happened

Memory carries chosen information across contexts. Remembering that an email was intended does not establish that it was sent; real workflows need an authoritative account of which events actually changed state.

Perhaps we let the conversation prose serve as the workflow state.

But the model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result.

Now we can see what is missing: we must represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system.

## Let the case decide

A refund moves requested → approved only with an approval record, then approved → issued only with a payment transaction ID. A sentence alone changes nothing.

No new equation is needed. The invention is a boundary, procedure, or system contract. Adding symbols would not make it more rigorous.

## The boundary of the discovery

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
