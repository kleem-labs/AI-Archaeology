# Mistakes — Excavation 168

## Tempting idea

Convert every value and every update permanently to half precision.

## Evidence that breaks it

Small updates disappear when rounded into large weights, and some intermediate values overflow or underflow the smaller numeric range.

## Requirement carried forward

Use reduced precision for bulk arithmetic while keeping selected master state and sensitive reductions in wider precision.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
