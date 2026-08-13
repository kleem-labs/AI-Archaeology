# Invention Exercises — Excavation 154

1. Reconstruct the tempting design without using the chapter's accepted name: Pad every sentence to the longest sentence in its batch and trust the loss mask to ignore the waste.
2. Create the smallest measurement that reveals this failure: The loss ignores padding, but attention and matrix multiplication still spend time and memory carrying those empty positions.
3. Explain why the chosen arithmetic operation answers the job and why its nearest alternative does not.
4. Change one number in the worked run, predict every intermediate result, and only then run `implementation/pure_python.py`.
5. Invent a deployment where this limitation matters: Packing improves utilization only if masks and position resets prevent cross-example contamination.
