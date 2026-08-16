# Mistakes — Excavation 195

## Tempting idea

Restore model weights and let every other component start fresh.

## Evidence that breaks it

Adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run.

## Requirement carried forward

Checkpoint every state variable that influences the next update, restore it before creating the next batch, and test an interrupted run against an uninterrupted reference for several exact steps.

The wrong idea remains because its failure exposes information the successful design must preserve.
