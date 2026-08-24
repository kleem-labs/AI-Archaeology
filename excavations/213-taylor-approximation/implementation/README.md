# Build Taylor Approximation Three Times

All three files reproduce the named experiment from Excavation 213.

1. [`pure_python.py`](pure_python.py) uses ordinary values, sets, lists, and loops so every responsibility remains visible.
2. [`numpy.py`](numpy.py) expresses the same repair with arrays and numerical operations.
3. [`pytorch.py`](pytorch.py) carries it into tensor machinery used by modern AI.

Run them in order. Before each run, say what should remain invariant and which intermediate value would expose the original failure.
