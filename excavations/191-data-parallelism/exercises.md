# Invention Exercises — Excavation 191

1. Reconstruct the tempting design without using the accepted method's name: send the same mini-batch to every worker and average their gradients.
2. Create the smallest named corpus or training run that makes this failure visible: All workers repeat the same computation and return the same evidence, so hardware cost rises without increasing batch diversity or reducing step time meaningfully.
3. Explain why the chosen operation answers the job and why its nearest alternative does not.
4. Change one concrete value from the chapter, predict the new intermediate result, and then run `implementation/pure_python.py`.
5. Design an audit for this remaining limitation: Because one shared update cannot proceed until every worker's evidence has joined the average, synchronous data parallelism waits for the slowest worker and communicates a full update's worth of gradient information.

<!-- memory-film-v1:start -->
## Close-book memory test

Close every file. Reconstruct the five frames beginning only from **the data parallelism prism mounted on the chain-of-custody ledger**. Explain the failure before naming the accepted idea; perform this gesture while recovering the repair: Touch the data parallelism prism in imagination: tap five fingertips in order—question, object, failure, transformation, seal—without saying the formal name. If the formal name arrives before the necessity, replay the scene more slowly.
<!-- memory-film-v1:end -->
