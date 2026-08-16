# Invention Exercises — Excavation 194

1. Reconstruct the tempting design without using the accepted method's name: let every worker write its local tensors and call the directory a checkpoint.
2. Create the smallest named corpus or training run that makes this failure visible: A worker fails before writing, two shards belong to different steps, or a filename is reused. The directory exists but cannot reconstruct one globally consistent training state.
3. Explain why the chosen operation answers the job and why its nearest alternative does not.
4. Change one concrete value from the chapter, predict the new intermediate result, and then run `implementation/pure_python.py`.
5. Design an audit for this remaining limitation: A complete checkpoint limits lost work but consumes storage and I/O bandwidth; frequent synchronous saves can dominate training time.
