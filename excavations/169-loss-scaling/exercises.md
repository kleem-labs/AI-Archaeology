# Invention Exercises — Excavation 169

1. Reconstruct the tempting design without using the chapter's accepted name: Increase the learning rate so small updates become visible.
2. Create the smallest measurement that reveals this failure: The learning rate acts after gradients are formed; it cannot recover values that already underflowed to zero, and it enlarges every surviving update.
3. Explain why the chosen arithmetic operation answers the job and why its nearest alternative does not.
4. Change one number in the worked run, predict every intermediate result, and only then run `implementation/pure_python.py`.
5. Invent a deployment where this limitation matters: A scale large enough to prevent underflow can cause overflow, so practical systems adjust it dynamically.
