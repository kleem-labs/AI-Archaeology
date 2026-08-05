# Mistakes — 076

## First idea

Assign one label to the entire raw byte sequence.

## Counterexample

A one-pixel shift changes thousands of byte positions although the same tiger remains.

## Repair

Preserve local spatial arrangement and compare nearby color measurements.
