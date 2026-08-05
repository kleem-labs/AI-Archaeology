# Mistakes — 062

## First idea

Retry the action whenever a response is missing.

## Counterexample

The first payment succeeded and the retry charges the customer twice.

## Repair

Give each logical action a stable idempotency key, query existing state, and make repeated requests return the first result instead of repeating the effect.
