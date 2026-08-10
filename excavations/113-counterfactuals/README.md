# Excavation 113 — Counterfactuals

[Previous: Excavation 112](../112-causal-inference/README.md)

What would have happened to this same patient under a treatment they did not receive?

At first, the simplest answer is tempting: Compare them with any untreated person.

But the simplicity has discarded something important: Differences in age and illness confound the comparison.

The missing information determines the next move: Construct a comparable alternative world using causal assumptions and matched evidence.

## Now work a case you can see

Compare patients with the same relevant history except treatment, then estimate the missing outcome.

The named objects come first. We add notation only when it shortens a procedure the reader has already performed.

## Where your new idea still breaks

The individual counterfactual is never directly observed.

The reason is visible in the procedure. It knows how to construct a comparable alternative world using causal assumptions and matched evidence. The limitation above asks for another judgment, and no part of the procedure makes that judgment.

## Enter the laboratory

Follow [Pure Python → NumPy → PyTorch](implementation/README.md).

## Carry the discovery forward

- [Invention challenges](exercises.md)
- [Mistakes](mistakes.md)
- [Diagram](diagram.md)
- [References](references.md)
- [Visual brief](images/README.md)

[Next: Excavation 114](../114-model-based-planning/README.md)
