# Mistakes — Excavation 154

## Tempting idea

Pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste.

## Evidence that breaks it

The loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions.

## Requirement carried forward

Pack several short examples into each fixed-length row and mask their boundaries so examples cannot read one another.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
