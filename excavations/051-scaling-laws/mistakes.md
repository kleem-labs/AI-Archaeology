# Mistakes — 051

## First idea

Make the model as large as possible and assume capability follows parameter count.

## Counterexample

A huge model trained on too little data repeatedly studies the same evidence; abundant data cannot help a model too small to compress its patterns.

## Repair

Run controlled experiments across sizes, fit the observed trend, and balance model capacity, data, and compute rather than worship one number.
