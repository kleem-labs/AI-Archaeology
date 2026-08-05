# Mistakes — 094

## First idea

Copy and fine-tune all parameters for every task.

## Counterexample

Storage and training cost multiply, and the base model is harder to preserve.

## Repair

Freeze the base and learn a small low-rank correction to selected matrices.
