# Exercises — Why Features Exist

## Design

1. Choose five features for distinguishing apples from oranges.
2. Reuse them to predict ripeness. Which become weak or useless, and what must be added?
3. Design features for recognizing dogs that remain stable under lighting and camera changes.

## Find the Failure

4. Construct an example where “has stripes” is misleading.
5. Explain why an identifying name is poor for classifying an unseen animal.
6. Give one proxy feature that could introduce unfair bias without explicitly naming a sensitive property.

## Experiment

7. Run `implementation.py`. Add a wolf and a crocodile.
8. Remove one required measurement and explain why failure is safer than silently using zero.
9. Add an irrelevant feature with random values. Predict how it might hurt a similarity calculation.

## Reconstruct

10. Build a feature specification for predicting whether a bicycle needs repair. Include units, allowed ranges, missing-value behavior, and one known limitation.
