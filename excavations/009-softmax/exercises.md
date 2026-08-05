# Exercises — Softmax

## Calculate

1. Compute softmax of `[0, 0]` without a calculator.
2. Approximate softmax of `[1, 0]` using $e\approx2.718$.
3. Add 100 to both scores and prove the result is unchanged.
4. Compare `[1, 2]` at temperatures `0.5`, `1`, and `2`.

## Diagnose

5. Show why dividing `[-2, 2]` by its sum fails.
6. Explain why winner-take-all is difficult to optimize smoothly.
7. What happens as temperature approaches zero? What about infinity?

## Experiment

8. Run `implementation.py` with `[1000, 1001, 1002]`.
9. Temporarily remove maximum subtraction and observe the failure.
10. Change one score gradually and record how every probability responds.

## Reconstruct

11. Explain stable softmax to someone who knows percentages but not exponentials, using a worked numerical story.
