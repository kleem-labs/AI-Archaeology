# Invention Exercises — Excavation 171

1. Reconstruct the tempting design without using the chapter's accepted name: Delete all activations after the forward pass.
2. Create the smallest measurement that reveals this failure: Backward computation then lacks the local values needed for its derivatives and would require rebuilding the entire prefix repeatedly.
3. Explain why the chosen arithmetic operation answers the job and why its nearest alternative does not.
4. Change one number in the worked run, predict every intermediate result, and only then run `implementation/pure_python.py`.
5. Invent a deployment where this limitation matters: Checkpointing buys memory with extra computation; a poor partition can save little or recompute too much.
