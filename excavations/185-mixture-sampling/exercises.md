# Invention Exercises — Excavation 185

1. Reconstruct the tempting design without using the accepted method's name: round each domain's desired share independently and concatenate the resulting blocks.
2. Create the smallest named corpus or training run that makes this failure visible: Independent rounding can exceed the budget, and long blocks make training order depend on domain. A small domain may vanish when its expected count rounds to zero.
3. Explain why the chosen operation answers the job and why its nearest alternative does not.
4. Change one concrete value from the chapter, predict the new intermediate result, and then run `implementation/pure_python.py`.
5. Design an audit for this remaining limitation: Sampling realizes probabilities only approximately in a finite run, and replacement can repeat scarce documents enough to increase memorization.
