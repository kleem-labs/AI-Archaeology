# Mistakes — 040

## Naive idea

Treat an entire sentence as one training example with one answer. Most of its transitions provide no learning signal.

## Failure

Padding and document boundaries can create false targets unless their losses are masked.

## Discovery

Shift the sequence by one position so every visible prefix predicts the token immediately following it.
