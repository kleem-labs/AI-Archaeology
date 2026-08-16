# Mistakes — Excavation 187

## Tempting idea

Spend nearly the entire budget on parameter count because a larger model can store more patterns.

## Evidence that breaks it

The large model is stopped after too little experience and remains undertrained, while much of its expensive capacity never receives enough varied evidence.

## Requirement carried forward

Estimate candidate parameter-and-token pairs under the same compute budget, run smaller scaling experiments, and choose the pair predicted to minimize held-out loss rather than maximizing either axis alone.

The wrong idea remains because its failure exposes information the successful design must preserve.
