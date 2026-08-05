"""Stage 2 — scaled dot-product attention, exposing array operations."""
try:
 import numpy as np
except ImportError as e:
 raise SystemExit("Install numpy for Stage 2") from e

# Run Stage 1 first. NumPy now replaces its explicit loops with arrays.
def inspect(values):
 array=np.asarray(values,dtype=float); return array, array.shape
