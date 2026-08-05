# Mistakes — 019

## Wrong Idea #1

Measure information by message length. A long predictable greeting can contain less news than one unexpected word. Use raw surprise such as one divided by probability, but independent surprises then multiply instead of add.

**Problem:** Information depends on the probability model. A surprise to one observer may be expected to another.

## Correct Idea

Rare events should carry more information, certain events none, and independent messages should add. The negative logarithm satisfies all three needs.
