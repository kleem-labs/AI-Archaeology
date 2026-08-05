# Implementation — 037

1. [Pure Python](pure_python.py) exposes table construction, row lookup, and one-row correction.
2. [NumPy](numpy.py) performs batched lookup and accumulated updates for repeated IDs.
3. [PyTorch](pytorch.py) uses the trainable embedding module found in real models.

Build direct-ID arithmetic and one-hot lookup first. Break them before using the dense table.
