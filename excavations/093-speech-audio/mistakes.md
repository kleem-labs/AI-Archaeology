# Mistakes — 093

## First idea

Treat every raw sample as an independent token.

## Counterexample

Sequences are huge and local frequency structure is hidden.

## Repair

Transform short windows into time-frequency features, then model their sequence.
