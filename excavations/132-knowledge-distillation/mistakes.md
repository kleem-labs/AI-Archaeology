# Mistakes — Excavation 132

## Wrong idea

Train a small model only on the original hard labels.

## Why it fails

The labels reveal the winner but discard how the teacher distributed doubt among alternatives.

## Repair discovered

Let the student imitate the teacher's probability pattern as well as the observed answer.
