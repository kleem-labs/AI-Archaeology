# Invention Exercises — Excavation 158

1. Reconstruct the tempting design without using the chapter's accepted name: Preserve one complete KV cache for each query head because multi-head attention originally gave every head private projections.
2. Create the smallest measurement that reveals this failure: The caches grow with both sequence length and head count, and loading them dominates the arithmetic for one new token.
3. Explain why the chosen arithmetic operation answers the job and why its nearest alternative does not.
4. Change one number in the worked run, predict every intermediate result, and only then run `implementation/pure_python.py`.
5. Invent a deployment where this limitation matters: A single shared catalog can remove distinctions that genuinely need different key-value spaces.
