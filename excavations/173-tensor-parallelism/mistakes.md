# Mistakes — Excavation 173

## Tempting idea

Assign whole layers to different devices and pass every activation through them sequentially.

## Evidence that breaks it

One oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work.

## Requirement carried forward

Split a matrix across its columns or rows, compute partial results concurrently, and communicate only the pieces needed to assemble the exact layer output.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
