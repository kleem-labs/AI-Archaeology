# Mistakes — 022

## Wrong Idea #1

Try a large jump and keep it if loss falls. Large jumps can leap over improvements. Try every possible value; there are infinitely many.

**Problem:** A derivative is local advice. Curved landscapes can change direction, flatten, or hide better valleys elsewhere.

## Correct Idea

Nudge the weight by a tiny amount, observe the change in loss, and divide change in loss by change in weight. Then imagine the nudge shrinking toward zero.
