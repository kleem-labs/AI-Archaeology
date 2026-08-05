# Mistakes — 021

## Wrong Idea #1

Use zero for correct and one for wrong. It treats barely wrong and confidently wrong as equal. Use ordinary distance between probabilities; it does not directly price the information wasted by the prediction.

**Problem:** Cross-entropy judges probabilities, so the model outputs must form a valid distribution. It tells us the error but not yet how each weight caused it.

## Correct Idea

Charge the information cost assigned by the predicted distribution to the outcome that actually occurred.
