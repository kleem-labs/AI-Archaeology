"""Stage 2: the same Backpropagation — Reusing Blame Instead of Recomputing It idea as array operations."""
import numpy as np

def inspect(values):
    array=np.asarray(values,dtype=float)
    return array,array.shape
