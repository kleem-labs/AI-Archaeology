# Mistakes — Excavation 172

## Tempting idea

Add devices and replicate the full training state on each one.

## Evidence that breaks it

Compute capacity grows while per-device model-state memory remains almost unchanged, so the same memory wall returns.

## Requirement carried forward

Partition optimizer states, gradients, and eventually parameters across data-parallel workers, gathering pieces only when computation needs them.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
