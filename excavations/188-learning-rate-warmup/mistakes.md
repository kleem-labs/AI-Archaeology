# Mistakes — Excavation 188

## Tempting idea

Begin immediately at the peak learning rate chosen for the stable middle of training.

## Evidence that breaks it

The first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused.

## Requirement carried forward

Increase the learning rate gradually from zero or a small value during a recorded warmup interval, then hand control to the main schedule.

The wrong idea remains because its failure exposes information the successful design must preserve.
