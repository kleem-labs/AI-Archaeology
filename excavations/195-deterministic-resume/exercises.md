# Invention Exercises — Excavation 195

1. Reconstruct the tempting design without using the accepted method's name: restore model weights and let every other component start fresh.
2. Create the smallest named corpus or training run that makes this failure visible: Adam forgets its moments, warmup may begin again, dropout chooses different masks, and data workers repeat or skip documents. The loss curve after restart cannot be attributed to the original run.
3. Explain why the chosen operation answers the job and why its nearest alternative does not.
4. Change one concrete value from the chapter, predict the new intermediate result, and then run `implementation/pure_python.py`.
5. Design an audit for this remaining limitation: Exact replay can still fail across nondeterministic kernels, changed hardware, libraries, or distributed timing; the required reproducibility level must be stated.
