# Invention Exercises — Excavation 173

1. Reconstruct the tempting design without using the chapter's accepted name: Assign whole layers to different devices and pass every activation through them sequentially.
2. Create the smallest measurement that reveals this failure: One oversized layer still cannot fit, and devices responsible for later layers wait while earlier ones work.
3. Explain why the chosen arithmetic operation answers the job and why its nearest alternative does not.
4. Change one number in the worked run, predict every intermediate result, and only then run `implementation/pure_python.py`.
5. Invent a deployment where this limitation matters: Tensor parallelism introduces communication inside every layer, so a slow interconnect can erase its benefit.
