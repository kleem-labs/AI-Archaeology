# Mistakes — Excavation 014

## Wrong idea 1 — Use one global scale

**Why it fails:** Each token can drift differently.

## Better but incomplete

Apply the repair without checking its assumptions. This fails when representation, scale, context, or data violates those assumptions.

## Discovery

Normalize each token across its features. The chapter derives why this repair exists before naming **layer normalization**.
