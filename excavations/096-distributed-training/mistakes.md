# Mistakes — 096

## First idea

Let many machines train independent copies and combine them occasionally.

## Counterexample

Their parameters drift and duplicated work wastes computation.

## Repair

Partition data or model work, synchronize required results, and preserve one coherent update.
