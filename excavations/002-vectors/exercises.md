# Exercises — Vectors

## Translate

1. Represent three houses using `[rooms, area_m², age_years]`.
2. Interpret `[3, 120, 40]` under that schema, then show how a different order corrupts it.
3. Plot `[1, 2]`, `[4, 3]`, and `[2, 6]`. Describe the two views of each vector.

## Calculate

4. Compute `[2, -1, 3] + [4, 5, 0]` and `3[2, -1, 3]`.
5. Normalize the values `[10, 20, 50]` to the range 0–1 by hand.
6. What should normalization return when every value in a feature is identical? Explain the implementation's choice.

## Experiment

7. Run `implementation.py` and explain every normalized coordinate.
8. Add a feature measured in millimeters with values near 100,000. Compare raw and normalized forms.
9. Trigger the dimension error in `add`. What modeling mistake might it reveal?

## Reconstruct

10. Design a vector representation for a song. State what each dimension means, which units need scaling, and what musical information is lost.
