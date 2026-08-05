# Exercises — Embeddings

## Calculate

1. Compute cosine similarity between `[1, 0]` and `[1, 1]`.
2. Compute it again after multiplying the second vector by 10. Explain the result.
3. Compare Euclidean and cosine relationships among `[1, 0]`, `[2, 0]`, and `[0, 1]`.

## Reason

4. Why does a one-hot representation encode identity but not similarity?
5. Can nearby embeddings be antonyms? Give an example.
6. Explain why a learned coordinate need not have one human-readable meaning.

## Experiment

7. Run `implementation.py` and add *puppy*, *bus*, and *kitten*.
8. Create a zero vector and observe the deliberate error. Why is cosine undefined?
9. Implement an embedding lookup using a list as the matrix and integer IDs as row indices.

## Reconstruct

10. Invent two corpora that would give the word *python* different neighbors. Explain how training objective and data shape the resulting geometry.
