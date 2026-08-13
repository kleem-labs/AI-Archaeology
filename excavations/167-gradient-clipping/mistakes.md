# Mistakes — Excavation 167

## Tempting idea

Discard the entire batch whenever any gradient coordinate looks large.

## Evidence that breaks it

Useful directional evidence is lost, and one arbitrary coordinate threshold ignores the size of the full update vector.

## Requirement carried forward

Preserve the gradient's direction but scale its whole norm down only when it exceeds a chosen ceiling.

A wrong idea belongs here because its failure exposes information the successful design must preserve.
