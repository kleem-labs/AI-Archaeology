# Exercises — Query, Key, Value

## Translate the Idea

1. Explain Q, K, and V with a library analogy, then with a restaurant-menu analogy.
2. Identify where each analogy breaks down.
3. Explain why changing a query changes routing without changing available content.

## Calculate

4. Dot query `[1, 0]` with keys `[1, 0]`, `[0, 1]`, and `[1, 1]`.
5. Scale those scores by $\sqrt{2}$ and compute their softmax.
6. Mix values `[1, 0]`, `[0, 2]`, and `[1, 1]` using your weights.
7. Write the full score matrix for two queries and three keys.

## Experiment

8. Run `implementation.py` and explain every attention row.
9. Enable causal masking. Verify that every weight above the allowed diagonal becomes zero.
10. Change one value without changing its key. Which quantities stay fixed?
11. Change one key without changing its value. Which quantities change?

## Reconstruct

12. Implement one small query, key, and value projection using the matrix multiplication from Excavation 005, then feed the results into `scaled_dot_product_attention`.
