# Invention Exercises — Excavation 166

1. Reconstruct the tempting design without using the chapter's accepted name: Treat penalty gradients and data gradients identically because both appear in one total loss.
2. Create the smallest measurement that reveals this failure: Coordinates with different gradient histories receive different effective shrinkage even when the intended rule was to decay all selected weights at one rate.
3. Explain why the chosen arithmetic operation answers the job and why its nearest alternative does not.
4. Change one number in the worked run, predict every intermediate result, and only then run `implementation/pure_python.py`.
5. Invent a deployment where this limitation matters: Decoupled decay still requires choosing which parameters to decay and how strongly.
