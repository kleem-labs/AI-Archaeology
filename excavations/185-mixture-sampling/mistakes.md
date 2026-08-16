# Mistakes — Excavation 185

## Tempting idea

Round each domain's desired share independently and concatenate the resulting blocks.

## Evidence that breaks it

Independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero.

## Requirement carried forward

Use a seeded categorical schedule, track realized counts against expected counts, and define exhaustion or replacement rules for every source.

The wrong idea remains because its failure exposes information the successful design must preserve.
