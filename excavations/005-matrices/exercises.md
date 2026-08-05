# Exercises — Matrices

## Calculate

1. Multiply `[[2, 0], [0, 3]]` by `[4, 5]` by hand.
2. Construct a matrix that swaps `[x, y]`, then test it on `[3, 7]`.
3. Find a matrix whose outputs are the sum and difference of two inputs.
4. Multiply a scaling matrix and rotation matrix in both orders. Compare results.

## Interpret

5. Explain each row as a weighted question and each column as the destination of a basis vector.
6. Why can an `m × n` matrix not consume a vector with `n + 1` features?
7. Show algebraically why two consecutive matrix transformations collapse into one matrix.

## Experiment

8. Run `implementation.py` and verify every printed value by hand.
9. Add a reflection across the horizontal axis and compose it with rotation.
10. Trigger both validation errors. Explain the mathematical problem behind each message.

## Reconstruct

11. Design a matrix that turns `[area, bedrooms, age]` into two invented house scores. Explain every weight and its limitations.
