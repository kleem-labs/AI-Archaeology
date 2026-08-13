# Mistakes — Excavation 166

## Tempting idea

Treat penalty gradients and data gradients identically because both appear in one total loss.

## Evidence that breaks it

Coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate.

## Requirement carried forward

Apply Adam's adaptive data update and parameter decay as separate operations.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
