# Mistakes — 060

## First idea

Let the conversation prose serve as the workflow state.

## Counterexample

The model says “refund completed” after merely drafting it, or issues it twice after losing track of an earlier tool result.

## Repair

Represent allowed states and transitions explicitly. Move state only when required evidence arrives from the responsible system.
