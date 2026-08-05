# Exercises — Distance

## Calculate

1. Compute Euclidean and Manhattan distance between `[0, 0]` and `[3, 4]`.
2. Find the nearest neighbor of `[2, 2]` among `[0, 0]`, `[2, 3]`, and `[5, 5]` under both metrics.
3. Compute weighted Euclidean distance between `[1, 4]` and `[3, 1]` using weights `[2, 0.5]`.

## Challenge the Metric

4. Construct two vectors whose signed coordinate differences cancel to zero.
5. Give a real task where Manhattan distance is more natural than straight-line distance.
6. Create a dataset where changing units from meters to millimeters changes the nearest neighbor.

## Experiment

7. Run `implementation.py`, then normalize each feature and run it again.
8. Add a duplicate irrelevant dimension ten times. How does it distort distance?
9. Implement a weighted Euclidean function using the existing style.

## Reconstruct

10. Define “similar restaurant” for two users with different priorities. Specify features, scaling, metric, and weights for each user.
