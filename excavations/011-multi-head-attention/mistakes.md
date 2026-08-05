# Mistakes — Excavation 011

## Wrong idea 1 — Make one attention head wider

**Why it fails:** Different relationships still compete in one distribution.

## Better but incomplete

Apply the repair without checking its assumptions. This fails when representation, scale, context, or data violates those assumptions.

## Discovery

Use parallel learned relationship spaces. The chapter derives why this repair exists before naming **multi-head attention**.
