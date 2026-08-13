# Invention Exercises — Excavation 167

1. Reconstruct the tempting design without using the chapter's accepted name: Discard the entire batch whenever any gradient coordinate looks large.
2. Create the smallest measurement that reveals this failure: Useful directional evidence is lost, and one arbitrary coordinate threshold ignores the size of the full update vector.
3. Explain why the chosen arithmetic operation answers the job and why its nearest alternative does not.
4. Change one number in the worked run, predict every intermediate result, and only then run `implementation/pure_python.py`.
5. Invent a deployment where this limitation matters: Clipping limits damage; it can hide a broken loss, corrupt data, or an unsuitable learning rate if used without diagnosis.
