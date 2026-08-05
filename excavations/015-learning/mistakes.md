# Mistakes — Excavation 015

## Wrong idea 1 — Randomly wiggle one weight at a time

**Why it fails:** The search explodes with billions of weights.

## Better but incomplete

Apply the repair without checking its assumptions. This fails when representation, scale, context, or data violates those assumptions.

## Discovery

Trace sensitivity backward and step downhill. The chapter derives why this repair exists before naming **gradient learning**.
