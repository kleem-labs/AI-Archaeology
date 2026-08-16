# Invention Exercises — Excavation 188

1. Reconstruct the tempting design without using the accepted method's name: begin immediately at the peak learning rate chosen for the stable middle of training.
2. Create the smallest named corpus or training run that makes this failure visible: The first noisy batches can make large updates before the optimizer's scale estimates become trustworthy, producing a loss spike that the later stable rate would not have caused.
3. Explain why the chosen operation answers the job and why its nearest alternative does not.
4. Change one concrete value from the chapter, predict the new intermediate result, and then run `implementation/pure_python.py`.
5. Design an audit for this remaining limitation: Warmup reduces early shock but cannot rescue an unsuitable peak rate, broken initialization, corrupt batch, or incorrect optimizer state.
