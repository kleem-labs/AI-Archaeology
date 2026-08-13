# Invention Exercises — Excavation 165

1. Reconstruct the tempting design without using the chapter's accepted name: Use the same raw gradient step scale for every parameter.
2. Create the smallest measurement that reveals this failure: A rate safe for frequent large gradients barely moves sparse coordinates; a rate large enough for sparse coordinates makes noisy ones unstable.
3. Explain why the chosen arithmetic operation answers the job and why its nearest alternative does not.
4. Change one number in the worked run, predict every intermediate result, and only then run `implementation/pure_python.py`.
5. Invent a deployment where this limitation matters: Adaptive scaling can generalize differently from SGD and introduces extra state for every parameter.
