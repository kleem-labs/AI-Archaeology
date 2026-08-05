# Mistakes — 037

## Wrong Idea #1 — Use token IDs as quantities

**Problem:** arbitrary numbering invents false magnitude and distance.

## Wrong Idea #2 — Keep one-hot vectors as the representation

**Problem:** vectors are enormous, sparse, and all distinct tokens remain equally unrelated.

## Wrong Idea #3 — Hand-design every semantic coordinate

**Problem:** language contains more interacting patterns than a fixed human feature list can anticipate.

## Correct Idea

Use IDs only as addresses into a compact table whose rows are changed by prediction error.
